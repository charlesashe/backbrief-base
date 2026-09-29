"""Build the buyer download, dist/backbrief-<VERSION>.zip, from this repo.

Why this exists
---------------
The predecessor's zips were rebuilt by hand several times, and one rebuild shipped
Windows backslash separators inside the archive. This script is the one way the zip is
made, and it refuses to build when a gate fails.

Layout inside the zip (top folder backbrief-<VERSION>/)
    kit/                  the contents of payload/ (.claude/, scaffold/, enforcement/,
                          memory-layer/, status-layer/, INTEGRATION.md)
    LICENSE.md            from the repo root
    VERSION               from the repo root
    CHANGELOG.md          from the repo root
    <every file in docs/> placed at the top folder's root, so docs/README.md is the
                          buyer README at backbrief-<VERSION>/README.md
Never shipped: .git, .gitkeep, __pycache__, .DS_Store, Thumbs.db. Directories that would
be empty once .gitkeep is dropped (scaffold inputs/, outputs/, workflows/active/) are kept
as explicit directory entries so the buyer's project gets the folders.

Gates (each a plain FAIL with the reason; all run, then the build stops if any failed)
    version      root VERSION is a release number and payload/.claude/VERSION reads
                 "Backbrief <VERSION>", so the two stamps cannot drift.
    manifest     tools/manifest_build.py (run as a subprocess, its exit code decides)
                 finds reference-manifest.json in sync with the payload. Reused, not copied.
    license      LICENSE.md exists at the repo root: nothing ships without a license.
    docs         docs/README.md exists: the buyer README is the first thing a buyer opens.
    skills       every folder under payload/.claude/skills/ has a SKILL.md, or Claude Code
                 cannot discover the skill and it fails silently.
    thirdparty   every skill named in THIRD-PARTY-LICENSES.md's table (Skills column)
                 exists and carries its upstream LICENSE file, as the MIT terms require.
    layout       no docs/ file collides with a name the script places itself.

After writing, the script re-opens the zip and checks it: forward slashes only, no
excluded names, one top folder, CRC test, and that the archive's contents match the source
files it was built from.

Reproducibility, stated plainly
-------------------------------
The zip is NOT byte-reproducible across runs: zip entries carry file modification times, so
builds of the same commit on a different checkout, machine or touch of a file produce
different bytes and a different zip sha256 (two back-to-back builds of an untouched working
tree can match, but nothing may rely on that). What is
reproducible is the CONTENT DIGEST this script also prints: sha256 over the sorted
(entry name, file sha256) pairs with CRLF normalized to LF, the same normalization the
manifest uses. Record both when releasing: the zip sha256 identifies the exact bytes that
were uploaded, and the content digest is what a rebuild from the same commit must match.

Usage, from the repo root:
    python tools/build_zip.py                    build dist/backbrief-<VERSION>.zip
    python tools/build_zip.py --check            run the gates only, build nothing
    python tools/build_zip.py --out <dir>        build into <dir> instead of dist/
    python tools/build_zip.py --out <dir> --skip-gates license,docs
                                                 DRY-RUN AID ONLY. Skips the named gates
                                                 (version, manifest, license, docs, skills,
                                                 thirdparty, layout), prints a loud DRY RUN
                                                 banner, names the zip ...-DRYRUN.zip, and
                                                 refuses to write into dist/ or without
                                                 --out. Never use it to release.

Nothing here tags, pushes, uploads or deploys. Those stay the owner's; the closing lines
of a successful build say what the owner does next.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAYLOAD = ROOT / "payload"
SKILLS = PAYLOAD / ".claude" / "skills"
DIST = ROOT / "dist"

EXCLUDE_NAMES = {".git", ".gitkeep", "__pycache__", ".DS_Store", "Thumbs.db"}
# Names the script places at the top folder's root itself; a docs/ file may not reuse them.
RESERVED_TOP = {"LICENSE.md", "VERSION", "CHANGELOG.md", "kit"}
GATE_NAMES = ["version", "manifest", "license", "docs", "skills", "thirdparty", "layout"]
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def read_version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


# --- gates: each returns a list of failure reasons (empty list = pass) -----------------


def gate_version() -> list[str]:
    version = read_version()
    if not VERSION_RE.match(version):
        return [f"root VERSION {version!r} is not a release number like 0.1.0"]
    stamp_file = PAYLOAD / ".claude" / "VERSION"
    if not stamp_file.is_file():
        return ["payload/.claude/VERSION is missing"]
    stamp = stamp_file.read_text(encoding="utf-8").strip()
    if stamp != f"Backbrief {version}":
        return [f"payload/.claude/VERSION reads {stamp!r}; expected 'Backbrief {version}' to match root VERSION"]
    return []


def gate_manifest() -> list[str]:
    script = ROOT / "tools" / "manifest_build.py"
    if not script.is_file():
        return ["tools/manifest_build.py is missing"]
    proc = subprocess.run(
        [sys.executable, str(script)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if proc.returncode == 0:
        return []
    tail = " | ".join(line.strip() for line in proc.stdout.strip().splitlines()[-6:] if line.strip())
    return [f"tools/manifest_build.py exited {proc.returncode}: {tail or proc.stderr.strip()}"]


def gate_license() -> list[str]:
    return [] if (ROOT / "LICENSE.md").is_file() else ["LICENSE.md is missing at the repo root (the license is the owner's to name and add)"]


def gate_docs() -> list[str]:
    return [] if (ROOT / "docs" / "README.md").is_file() else ["docs/README.md is missing (the buyer README)"]


def gate_skills() -> list[str]:
    if not SKILLS.is_dir():
        return ["payload/.claude/skills/ is missing"]
    return [
        f"skill folder {d.name} has no SKILL.md"
        for d in sorted(SKILLS.iterdir())
        if d.is_dir() and not (d / "SKILL.md").is_file()
    ]


def third_party_skills() -> list[str]:
    """Skill names from the Skills column of the attribution table in THIRD-PARTY-LICENSES.md."""
    text = (SKILLS / "THIRD-PARTY-LICENSES.md").read_text(encoding="utf-8")
    names: list[str] = []
    in_table = False
    for line in text.splitlines():
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not in_table:
                in_table = True  # header row
                continue
            if all(set(c) <= set("-: ") for c in cells):
                continue  # separator row
            names.extend(s.strip() for s in cells[-1].split(",") if s.strip())
        else:
            in_table = False
    return names


def gate_thirdparty() -> list[str]:
    table = SKILLS / "THIRD-PARTY-LICENSES.md"
    if not table.is_file():
        return ["payload/.claude/skills/THIRD-PARTY-LICENSES.md is missing"]
    names = third_party_skills()
    if not names:
        return ["no skills parsed from THIRD-PARTY-LICENSES.md's table (Skills column)"]
    fails = []
    for name in names:
        folder = SKILLS / name
        if not folder.is_dir():
            fails.append(f"third-party skill {name} is named in the table but has no folder")
        elif not any(p.is_file() and p.name.upper().startswith("LICENSE") for p in folder.iterdir()):
            fails.append(f"third-party skill {name} has no LICENSE file")
    return fails


def gate_layout() -> list[str]:
    docs = ROOT / "docs"
    if not docs.is_dir():
        return []
    fails = []
    for path in docs.rglob("*"):
        rel = path.relative_to(docs)
        if path.is_file() and not skip(rel) and rel.parts[0] in RESERVED_TOP:
            fails.append(f"docs/{rel.as_posix()} collides with {rel.parts[0]}, which the build places itself")
    return fails


GATES = {
    "version": gate_version,
    "manifest": gate_manifest,
    "license": gate_license,
    "docs": gate_docs,
    "skills": gate_skills,
    "thirdparty": gate_thirdparty,
    "layout": gate_layout,
}


def run_gates(skipped: set[str]) -> bool:
    ok = True
    for name in GATE_NAMES:
        if name in skipped:
            print(f"  SKIPPED  {name}")
            continue
        fails = GATES[name]()
        if fails:
            ok = False
            for reason in fails:
                print(f"  FAIL     {name}: {reason}")
        else:
            print(f"  PASS     {name}")
    return ok


# --- collecting and building ----------------------------------------------------------


def skip(rel: Path) -> bool:
    return any(part in EXCLUDE_NAMES for part in rel.parts)


def walk(src_root: Path, arc_root: str) -> tuple[list[tuple[Path, str]], list[str]]:
    """Files to ship as (path, archive name) and empty directories to keep as entries."""
    files: list[tuple[Path, str]] = []
    parents: set[Path] = set()
    for path in sorted(src_root.rglob("*")):
        rel = path.relative_to(src_root)
        if skip(rel) or not path.is_file():
            continue
        files.append((path, f"{arc_root}/{rel.as_posix()}" if arc_root else rel.as_posix()))
        parents.update(rel.parents)
    empty = []
    for path in sorted(src_root.rglob("*")):
        rel = path.relative_to(src_root)
        if path.is_dir() and not skip(rel) and rel not in parents:
            empty.append(f"{arc_root}/{rel.as_posix()}/" if arc_root else f"{rel.as_posix()}/")
    return files, empty


def collect(top: str) -> tuple[list[tuple[Path, str]], list[str]]:
    """(files as (path, archive name), empty-directory archive names) for the whole download."""
    files, dirs = walk(PAYLOAD, f"{top}/kit")
    for name in ("LICENSE.md", "VERSION", "CHANGELOG.md"):
        if (ROOT / name).is_file():  # a skipped license gate leaves LICENSE.md absent
            files.append((ROOT / name, f"{top}/{name}"))
    docs = ROOT / "docs"
    if docs.is_dir():
        d_files, d_dirs = walk(docs, top)
        files += d_files
        dirs += d_dirs
    return files, dirs


def content_digest(pairs) -> str:
    """sha256 over sorted (name, sha256 of content) pairs, CRLF normalized to LF."""
    h = hashlib.sha256()
    for name, data in sorted(pairs):
        h.update(name.encode("utf-8") + b"\0" + hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest().encode() + b"\n")
    return h.hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build(out_dir: Path, version: str, dry_run: bool) -> int:
    top = f"backbrief-{version}"
    files, empty_dirs = collect(top)
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / (f"{top}-DRYRUN.zip" if dry_run else f"{top}.zip")
    if zip_path.exists():
        zip_path.unlink()

    expected = {arc for _, arc in files}
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, arc in files:
            zf.write(path, arc)
        for arc in empty_dirs:
            zf.writestr(zipfile.ZipInfo(arc), b"")

    failures = []
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
        file_names = [n for n in names if not n.endswith("/")]
        if any("\\" in n for n in names):
            failures.append("entries contain backslashes")
        if any(part in EXCLUDE_NAMES for n in names for part in n.split("/")):
            failures.append("an excluded name (.git, .gitkeep, __pycache__, .DS_Store, Thumbs.db) is in the archive")
        if {n.split("/")[0] for n in names} != {top}:
            failures.append(f"archive does not have the single top folder {top}/")
        bad = zf.testzip()
        if bad is not None:
            failures.append(f"corrupt entry {bad}")
        if set(file_names) != expected:
            failures.append("archive file list differs from the source file list")
        digest = content_digest((n, zf.read(n)) for n in file_names)
    source_digest = content_digest((arc, path.read_bytes()) for path, arc in files)
    if digest != source_digest:
        failures.append("archive contents differ from the source files they were built from")
    if failures:
        for reason in failures:
            print(f"FAIL post-build: {reason}")
        zip_path.unlink(missing_ok=True)
        print(f"removed {zip_path.name}: a zip that failed its post-build check must not sit in the output folder")
        return 1

    print(f"\nwrote {zip_path}")
    print(f"  entries        {len(names)} ({len(file_names)} files, {len(names) - len(file_names)} empty-directory entries)")
    print(f"  size           {zip_path.stat().st_size:,} bytes")
    print(f"  zip sha256     {file_sha256(zip_path)}")
    print(f"  content digest {digest}")
    print("  note: the zip sha256 changes on every build (zip timestamps); the content digest does not.")
    if dry_run:
        print("  DRY RUN output: gates were skipped. Do not upload, tag or record this zip.")
    else:
        print("\nNext, all the owner's or on the owner's GO (this script did none of it):")
        print("  1. python tools/install_check.py " + str(zip_path))
        print("  2. record the zip sha256, content digest and commit in CHANGELOG.md, then commit")
        print(f"  3. tag v{version}, make the repo public, upload the zip to the site, deploy the page")
        print("  see workflows/release-checklist.md")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the buyer download zip.", formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="run the gates only, build nothing")
    ap.add_argument("--out", type=Path, help="output directory (default: dist/)")
    ap.add_argument("--skip-gates", default="", help="DRY-RUN AID: comma-separated gate names to skip; needs --out outside dist/")
    args = ap.parse_args()

    skipped = {g.strip() for g in args.skip_gates.split(",") if g.strip()}
    unknown = skipped - set(GATE_NAMES)
    if unknown:
        print(f"unknown gate name(s) {sorted(unknown)}; valid: {', '.join(GATE_NAMES)}")
        return 2

    out_dir = (args.out or DIST).resolve()
    dry_run = bool(skipped)
    if dry_run:
        inside_dist = out_dir == DIST.resolve() or DIST.resolve() in out_dir.parents
        inside_repo = out_dir == ROOT.resolve() or ROOT.resolve() in out_dir.parents
        if args.out is None or inside_dist or inside_repo:
            print("REFUSED: --skip-gates is a dry-run aid and will not write into dist/ or anywhere inside the repo. Pass --out <a folder outside the repo>.")
            return 2
        print("=" * 72)
        print(f"  DRY RUN: gates skipped: {', '.join(sorted(skipped))}")
        print("  This output is not a release candidate.")
        print("=" * 72)

    version = read_version()
    print(f"--- build gates for backbrief {version} ---")
    if not run_gates(skipped):
        print("\nGATES FAILED: nothing was built.")
        return 1
    if args.check:
        print("\nall gates passed (--check: nothing built).")
        return 0
    return build(out_dir, version, dry_run)


if __name__ == "__main__":
    sys.exit(main())
