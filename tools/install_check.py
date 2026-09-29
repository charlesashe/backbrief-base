"""Prove a built zip installs clean: the "served zip installs clean" gate.

Why this exists
---------------
Building a zip proves the repo was healthy. It does not prove the file a buyer downloads
unpacks into a working install. This script takes the zip itself, unpacks it into a temp
folder, does what the install guide tells the buyer to do (copy kit/.claude into the
project's .claude/ and kit/scaffold into the project root, never overwriting), then checks
mechanically what /verify-install steps 1 and 3 check. It reads the zip only, never the
repo's working tree.

Checks, one line each (PASS or FAIL; exit code 1 if any FAIL)
    zip            opens, CRC test, forward slashes only, no excluded names, one top folder;
                   also prints the zip sha256 and content digest (see build_zip.py) for the
                   release record
    layout         top folder holds LICENSE.md, VERSION, CHANGELOG.md, README.md and kit/
                   with .claude, scaffold, enforcement, memory-layer, status-layer,
                   INTEGRATION.md; kit/.claude/VERSION reads "Backbrief <top folder version>"
    install        copying kit/.claude and kit/scaffold never collides (a collision means
                   a shipped file would be silently dropped by a never-overwrite install)
    names          agents, commands, rules and skills on disk equal shipped_names in
                   reference-manifest.json (four lines)
    skills         every skill folder has a SKILL.md whose frontmatter parses and has a
                   description: (Claude Code cannot discover a skill without one)
    files          every reference file in the manifest exists and its sha256 (CRLF
                   normalized to LF) matches `current`
    payload_files  the same for CLAUDE.md and the rules
    scaffold       the project folders and starter files /verify-install step 1 expects

Manifest logic is reused from tools/manifest_build.py (its classify() and names_on_disk()
run against the scratch install by repointing that module's CLAUDE and SCAFFOLD paths), so
the check cannot drift from the gate that generated the manifest.

Usage:
    python tools/install_check.py <path to backbrief-<VERSION>.zip>
    python tools/install_check.py <zip> --keep      keep the scratch project and print its path

The scratch folder is deleted afterward unless --keep is given. Nothing here publishes.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import manifest_build as mb  # noqa: E402  (reused, not duplicated)
from build_zip import EXCLUDE_NAMES, content_digest, file_sha256  # noqa: E402

FAILED = False


def report(ok: bool, label: str, detail: str = "") -> None:
    global FAILED
    if not ok:
        FAILED = True
    print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f": {detail}" if detail else ""))


def copy_no_overwrite(src: Path, dest: Path) -> tuple[int, list[str]]:
    """Copy src tree into dest, never replacing an existing file. Returns (copied, collisions)."""
    copied, collisions = 0, []
    for path in sorted(src.rglob("*")):
        target = dest / path.relative_to(src)
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif target.exists():
            collisions.append(str(target.relative_to(dest)).replace("\\", "/"))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            copied += 1
    return copied, collisions


def frontmatter_description(text: str) -> bool:
    """True if the leading --- block has a non-empty description: (inline or folded/literal)."""
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return False
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return False
    for i in range(1, end):
        m = re.match(r"^description:\s*(.*)$", lines[i])
        if m:
            value = m.group(1).strip()
            if value and value not in (">", "|", ">-", "|-"):
                return True
            nxt = lines[i + 1] if i + 1 < end else ""
            return bool(nxt.strip()) and nxt[:1] in " \t"
    return False


def check_zip(zip_path: Path, work: Path) -> Path | None:
    try:
        zf = zipfile.ZipFile(zip_path)
    except (OSError, zipfile.BadZipFile) as exc:
        report(False, "zip", f"cannot open {zip_path}: {exc}")
        return None
    with zf:
        names = zf.namelist()
        problems = []
        if any("\\" in n for n in names):
            problems.append("backslash separators in entry names")
        if any(part in EXCLUDE_NAMES for n in names for part in n.split("/")):
            problems.append("an excluded name is inside the archive")
        tops = {n.split("/")[0] for n in names}
        if len(tops) != 1:
            problems.append(f"expected one top folder, found {sorted(tops)}")
        bad = zf.testzip()
        if bad is not None:
            problems.append(f"corrupt entry {bad}")
        if problems:
            report(False, "zip", "; ".join(problems))
            return None
        zf.extractall(work)
        digest = content_digest((n, zf.read(n)) for n in names if not n.endswith("/"))
    top = work / next(iter(tops))
    print(f"  zip sha256 {file_sha256(zip_path)}  content digest {digest}")
    report(True, "zip", f"{len(names)} entries, one top folder {top.name}/")
    return top


def check_layout(top: Path) -> bool:
    m = re.fullmatch(r"backbrief-(.+)", top.name)
    missing = [
        n
        for n in ("LICENSE.md", "VERSION", "CHANGELOG.md", "README.md", "kit/INTEGRATION.md", "kit/.claude/VERSION")
        if not (top / n).is_file()
    ] + [n for n in ("kit/.claude", "kit/scaffold", "kit/enforcement", "kit/memory-layer", "kit/status-layer") if not (top / n).is_dir()]
    if not m:
        report(False, "layout", f"top folder {top.name!r} is not backbrief-<VERSION>")
        return False
    if missing:
        report(False, "layout", "missing " + ", ".join(missing))
        return False
    version = m.group(1)
    stamps = {
        "VERSION": (top / "VERSION").read_text(encoding="utf-8").strip(),
        "kit/.claude/VERSION": (top / "kit/.claude/VERSION").read_text(encoding="utf-8").strip(),
    }
    if stamps["VERSION"] != version or stamps["kit/.claude/VERSION"] != f"Backbrief {version}":
        report(False, "layout", f"stamps disagree with folder version {version}: {stamps}")
        return False
    report(True, "layout", f"top-level files and kit/ parts present; stamps agree at {version}")
    return True


def check_install(top: Path, project: Path) -> None:
    (project / ".claude").mkdir(parents=True)
    n1, c1 = copy_no_overwrite(top / "kit" / ".claude", project / ".claude")
    n2, c2 = copy_no_overwrite(top / "kit" / "scaffold", project)
    collisions = c1 + c2
    report(not collisions, "install", f"copied {n1} .claude files and {n2} scaffold files" + (f"; collisions (would be dropped): {collisions}" if collisions else ", no collisions"))


def check_manifest(project: Path) -> None:
    claude = project / ".claude"
    manifest_path = claude / "reference-manifest.json"
    if not manifest_path.is_file():
        report(False, "manifest", "reference-manifest.json is not in the installed .claude/")
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mb.CLAUDE, mb.SCAFFOLD = claude, project  # scaffold lands at the project root

    disk = mb.names_on_disk()
    for kind in ("agents", "commands", "rules", "skills"):
        listed = manifest.get("shipped_names", {}).get(kind)
        if listed == disk[kind]:
            report(True, f"names.{kind}", f"{len(listed)} match shipped_names")
        else:
            extra = sorted(set(disk[kind]) - set(listed or []))
            gone = sorted(set(listed or []) - set(disk[kind]))
            report(False, f"names.{kind}", f"unexpected {extra}, missing {gone}")

    bad = []
    skills_dir = claude / "skills"
    for d in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        skill = d / "SKILL.md"
        if not skill.is_file():
            bad.append(f"{d.name} (no SKILL.md)")
        elif not frontmatter_description(skill.read_text(encoding="utf-8")):
            bad.append(f"{d.name} (frontmatter missing or no description:)")
    report(not bad, "skills", "every SKILL.md has a description in its frontmatter" if not bad else "; ".join(bad))

    for label, section, entries in (
        ("files", "files", manifest["files"]),
        ("payload_files", "payload_files", manifest["payload_files"]["files"]),
    ):
        problems = []
        for e in entries:
            state, _ = mb.classify(e, section)
            if state != mb.CURRENT:
                problems.append(f"{e['path']} is {state}")
        report(not problems, label, f"{len(entries)}/{len(entries)} exist and match current" if not problems else "; ".join(problems))


def check_scaffold(project: Path) -> None:
    dirs = ["context/strategy", "context/reference", "inputs", "outputs", "workflows", "workflows/active", "templates", "examples", "team", ".claude/memory"]
    files = [
        "CLAUDE.md",
        "context/strategy/current-state.md",
        "context/strategy/current-priorities.md",
        "context/reference/SOURCES.md",
        "examples/worked-example-business.md",
        ".claude/memory/decisions.md",
        ".claude/memory/preferences.md",
    ]
    missing = [d + "/" for d in dirs if not (project / d).is_dir()] + [f for f in files if not (project / f).is_file()]
    report(not missing, "scaffold", f"{len(dirs)} folders and {len(files)} starter files present" if not missing else "missing " + ", ".join(missing))


def main() -> int:
    ap = argparse.ArgumentParser(description="Check that a built zip installs clean.", formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("zip", type=Path)
    ap.add_argument("--keep", action="store_true", help="keep the scratch project and print its path")
    args = ap.parse_args()

    if not args.zip.is_file():
        print(f"no such file: {args.zip}")
        return 2
    work = Path(tempfile.mkdtemp(prefix="backbrief-install-check-"))
    print(f"--- install check: {args.zip.name} ---")
    try:
        top = check_zip(args.zip, work / "unpacked")
        if top is not None:
            check_layout(top)  # a layout failure is reported but does not stop the install steps
            if (top / "kit" / ".claude").is_dir() and (top / "kit" / "scaffold").is_dir():
                project = work / "project"
                check_install(top, project)
                check_manifest(project)
                check_scaffold(project)
            else:
                report(False, "install", "kit/.claude or kit/scaffold is absent: install steps not run")
    finally:
        if args.keep:
            print(f"  scratch kept at {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)
    print("INSTALL CHECK FAILED" if FAILED else "install check passed: the zip installs clean")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
