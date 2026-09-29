"""Build or check this product's reference-manifest.json from the payload on disk.

Why this exists
---------------
/verify-install reads `shipped_names` and the file hashes from
`payload/.claude/reference-manifest.json`. Counts and lists typed into prose go stale;
this file is generated from the payload, so it cannot disagree with what ships. The
predecessor's release tooling learned this the hard way (its 3.7.0 upgrade defect: hashes
nobody regenerated made the installer refuse to replace the product's own files).

What it does
------------
  --check   (default) Hash every tracked file and classify it against the manifest.
            Exits 1 if any tracked file is unrecognized or missing. Also exits 1 if
            shipped_names differ from the folders on disk.
  --fix     Regenerate: shipped_names from disk; for each tracked file whose hash
            changed, demote the old `current` into `known_prior` (release label kept,
            so lineage is never lost) and stamp a new `current` at the root VERSION.
            Creates the manifest if none exists.
  --seed-from <path>
            On first generation only: read a predecessor manifest and carry its
            `current` and `known_prior` hashes for the same paths into `known_prior`,
            so an install upgrading from the predecessor is recognized as ours rather
            than as owner-modified.

Hashes are sha256 over the bytes with CRLF normalized to LF (the predecessor found four
of eleven real installs carried CRLF; without normalization every one reads modified).

Usage, from the repo root:
    python tools/manifest_build.py
    python tools/manifest_build.py --fix
    python tools/manifest_build.py --fix --seed-from <predecessor reference-manifest.json>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAYLOAD = ROOT / "payload"
CLAUDE = PAYLOAD / ".claude"
SCAFFOLD = PAYLOAD / "scaffold"
MANIFEST = CLAUDE / "reference-manifest.json"

# Reference documents shipped read-only for the owner to read (never to fill in).
# Paths are relative to the scaffold, which lands at the project root.
REFERENCE_FILES = [
    "examples/worked-example-business.md",
    "templates/business-brief-template.md",
    "workflows/business-plan-template.md",
    "workflows/plan-template.md",
    "workflows/scorecard-template.md",
    "context/reference/README.md",
]

CURRENT, PRIOR, UNRECOGNIZED, MISSING = "current", "prior", "unrecognized", "missing"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def payload_file_paths() -> list[str]:
    """CLAUDE.md plus every rule, relative to the installed .claude/."""
    return ["CLAUDE.md"] + sorted(f"rules/{p.name}" for p in (CLAUDE / "rules").glob("*.md"))


def resolve(rel: str, section: str) -> Path | None:
    root = CLAUDE if section == "payload_files" else SCAFFOLD
    candidate = root / rel
    return candidate if candidate.is_file() else None


def names_on_disk() -> dict[str, list[str]]:
    return {
        "commands": sorted(p.stem for p in (CLAUDE / "commands").glob("*.md")),
        "skills": sorted(d.name for d in (CLAUDE / "skills").iterdir() if d.is_dir()),
        "agents": sorted(p.stem for p in (CLAUDE / "agents").glob("*.md")),
        "rules": sorted(p.stem for p in (CLAUDE / "rules").glob("*.md")),
    }


def classify(entry: dict, section: str) -> tuple[str, str | None]:
    path = resolve(entry["path"], section)
    if path is None:
        return MISSING, None
    got = digest(path)
    if got == entry["current"]["sha256"]:
        return CURRENT, got
    if any(got == p["sha256"] for p in entry.get("known_prior", [])):
        return PRIOR, got
    return UNRECOGNIZED, got


def skeleton() -> dict:
    return {
        "note": "Shipped reference files: documents this product ships read-only for the owner to read, never to fill in. Buyer-authored files (context/strategy/, .claude/memory/, the project CLAUDE.md, context/reference/SOURCES.md) are deliberately absent and are never touched by hash.",
        "hash": "sha256 over the file's bytes with CRLF normalized to LF. Normalization is required, not cosmetic: real installed copies carry CRLF and would read as modified without it.",
        "unknown_hash_means": "modified or unrecognized - leave the file alone and say so. Never replace on a hash that is not in this manifest.",
        "files": [],
        "shipped_names": {},
        "payload_files": {
            "note": "On a GLOBAL install, ~/.claude/CLAUDE.md is frequently the owner's own configuration and will match nothing here. That is the case this list exists to catch.",
            "files": [],
        },
        "built_ins": "Claude Code's own built-in commands are a third namespace, in neither ~/.claude/commands/ nor ~/.claude/skills/, so a folder comparison cannot see them. /resume is taken outright by the built-in: typing it opens the session picker and a command file of that name never runs. /plan is contested rather than dead - a command file of that name does run in the Claude Code desktop app - so which one wins depends on the client. This product ships /pickup and /business-plan to avoid both. Re-check after a Claude Code update.",
        "shipped_names_notes": {
            "why": "A personal-level skill or command with any of these names silently replaces the shipped one; nothing warns. Commands and skills are one namespace. Compare case-normalized.",
            "normalize": "lower-case, then drop everything that is not a letter or digit. Deliberately looser than an exact match: over-reporting a near-miss costs a line in a report, under-reporting hides a command the owner is not running.",
        },
    }


def seed_priors(seed_path: Path) -> dict[str, list[dict]]:
    """Predecessor hashes per path: its current and its known priors, all as priors here."""
    seed = json.loads(seed_path.read_text(encoding="utf-8"))
    out: dict[str, list[dict]] = {}
    for entries in (seed.get("files", []), seed.get("payload_files", {}).get("files", [])):
        for e in entries:
            priors = list(e.get("known_prior", []))
            cur = e.get("current")
            if cur:
                priors.append({"releases": f"Backbrief Business OS {cur['release']}", "sha256": cur["sha256"]})
            out[e["path"]] = priors
    return out


def report(manifest: dict) -> bool:
    ok = True
    for section, entries in (("payload_files", manifest["payload_files"]["files"]), ("files", manifest["files"])):
        current = 0
        for e in entries:
            state, _ = classify(e, section)
            if state == CURRENT:
                current += 1
                continue
            ok = False
            print(f"  {state.upper():13} {e['path']} (stamped {e['current']['release']})")
        print(f"  {section}: {current}/{len(entries)} match the current stamp")
    disk = names_on_disk()
    for kind, names in disk.items():
        if manifest.get("shipped_names", {}).get(kind) != names:
            ok = False
            print(f"  shipped_names.{kind}: stale ({len(manifest.get('shipped_names', {}).get(kind, []))} listed, {len(names)} on disk)")
    return ok


def fix(manifest: dict, version: str, seed: dict[str, list[dict]]) -> int:
    changed = 0
    manifest["shipped_names"] = names_on_disk()
    wanted = {"payload_files": payload_file_paths(), "files": REFERENCE_FILES}
    for section, paths in wanted.items():
        holder = manifest["payload_files"]["files"] if section == "payload_files" else manifest["files"]
        by_path = {e["path"]: e for e in holder}
        holder[:] = []
        for rel in paths:
            path = resolve(rel, section)
            if path is None:
                print(f"  MISSING ON DISK {rel}: a tracked file is not in the payload; fix the packaging")
                continue
            got = digest(path)
            entry = by_path.get(rel) or {"path": rel, "current": None, "known_prior": []}
            if entry["current"] is None:
                entry["known_prior"] = [p for p in seed.get(rel, []) if p["sha256"] != got]
                entry["current"] = {"release": version, "sha256": got}
                changed += 1
                print(f"  stamped   {rel} at {version}" + (f" ({len(entry['known_prior'])} prior hashes carried)" if entry["known_prior"] else ""))
            elif entry["current"]["sha256"] != got:
                old = entry["current"]
                if not any(p["sha256"] == old["sha256"] for p in entry["known_prior"]):
                    entry["known_prior"].append({"releases": old["release"], "sha256": old["sha256"]})
                entry["current"] = {"release": version, "sha256": got}
                changed += 1
                print(f"  restamped {rel}: {old['release']} -> {version}")
            holder.append(entry)
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true", help="regenerate the manifest, keeping lineage")
    ap.add_argument("--seed-from", type=Path, help="predecessor manifest whose hashes become known priors (first generation only)")
    args = ap.parse_args()

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    exists = MANIFEST.exists()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if exists else skeleton()
    print(f"--- reference-manifest against the payload at {version} ({'existing' if exists else 'new'} manifest) ---")

    if not args.fix:
        if not exists:
            print("  no manifest yet; run with --fix to generate it")
            return 1
        ok = report(manifest)
        print("  in sync" if ok else "  NOT in sync; run with --fix")
        return 0 if ok else 1

    seed = seed_priors(args.seed_from) if (args.seed_from and not exists) else {}
    if args.seed_from and exists:
        print("  --seed-from ignored: the manifest already exists and carries its own lineage")
    changed = fix(manifest, version, seed)
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  {changed} entr{'y' if changed == 1 else 'ies'} written")
    print("--- re-checking its own work ---")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ok = report(manifest)
    print("  manifest is in sync" if ok else "  STILL NOT CLEAN after --fix; look by hand")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
