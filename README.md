# Backbrief

The base product: grade the plan before you build it.

Part of the Backbrief product line (restructured 2026-09-27). This folder is the canonical clone for
this product. The payload that ships to buyers lives under `payload/.claude/`; everything else is
build material. See `PRODUCT.md` for scope and the component manifest, and
`C:\business\vault\backbrief-hq` for the business that runs it.

Status: payload assembled, unreleased. Version 0.1.0 is reserved for the first release.

## What payload/ holds

- `payload/.claude/`: the team. Agents, commands, rules and skills, plus the index `CLAUDE.md` and the `VERSION` stamp.
- `payload/scaffold/`: the project folders and templates the team reads from and writes to, with a project `CLAUDE.md` and the decision log.
- The opt-in layers: `payload/enforcement/` (permission rules that stop outward shell commands), `payload/memory-layer/`, and `payload/status-layer/` (the machine-written status contract). Each has its own README and none installs unless you say yes.
- `payload/INTEGRATION.md`: how to add Backbrief to a setup you already have without losing any of it.

## Install by hand into a project

There are two copies to make: the team (`payload/.claude/`) and the scaffold (`payload/scaffold/`). Run the commands from this folder. Both copies copy the contents of the source folder, and neither overwrites a file you already have. If your setup already has files under the same names, they are skipped and stay yours; `payload/INTEGRATION.md` covers what to do about each one.

### Step 1: Install the team

Install it globally into `~/.claude/` (every project) or into one project's `.claude/`. Pick one.

macOS / Linux:

```bash
# Global. -n = never overwrite an existing file.
mkdir -p ~/.claude
cp -Rn payload/.claude/. ~/.claude/

# OR per-project. Replace the path with your project.
mkdir -p /path/to/your-project/.claude
cp -Rn payload/.claude/. /path/to/your-project/.claude/
```

Windows (PowerShell):

```powershell
# Global. /XC /XN /XO = copy only files that do not already exist at the destination.
New-Item -ItemType Directory -Force "$HOME\.claude" | Out-Null
robocopy "payload\.claude" "$HOME\.claude" /E /XC /XN /XO

# OR per-project. Replace the path with your project.
New-Item -ItemType Directory -Force "C:\path\to\your-project\.claude" | Out-Null
robocopy "payload\.claude" "C:\path\to\your-project\.claude" /E /XC /XN /XO
```

Updating from an earlier version? The copies above never overwrite, so they will not replace old files with new ones. Delete Backbrief's own files at the destination first, and never bulk-overwrite `~/.claude/` if it also holds work of your own.

### Step 2: Install the scaffold into your project

Copy the scaffold into the root of the project you want the team to work in, even if you installed the team globally.

macOS / Linux:

```bash
# Replace the path with your project root. -n = never overwrite existing files.
cp -Rn payload/scaffold/. /path/to/your-project/
```

Windows (PowerShell):

```powershell
# Replace the path with your project root.
robocopy "payload\scaffold" "C:\path\to\your-project" /E /XC /XN /XO
```

On Windows, robocopy prints a summary table; that is normal, not an error. Then open Claude Code in the project and run `/verify-install`.
