# This folder is the Backbrief download

You are Claude Code, opened in the folder the owner unzipped. This file is the installer. When the owner says "install this", "set this up", or "read the README and install it", run the procedure below. If they ask for something else, skip this file. Do the work yourself instead of handing the owner shell commands, and use syntax that matches their operating system and shell.

## Start here

Read `VERSION` beside this file. Your first line to the owner is "This is Backbrief <version>." with the number read from that file, never typed from memory. The line asks nothing.

Look in this folder's parent for other Backbrief downloads (`VERSION` at the top, `kit/.claude/` inside). If one is newer, say so and ask whether to install from it instead. Compare versions as numbers, part by part: 0.10.0 is newer than 0.2.0.

## Refuse three things

- **An older version over a newer one.** Compare this folder's `VERSION` with the target's `.claude/VERSION` (numeric part; it reads like "Backbrief 0.1.0"). If this download is older, stop, name both versions, and install nothing unless the owner asks for a rollback in so many words.
- **Anything outward.** No network calls, no accounts, nothing sent anywhere. Every step is local copying and editing.
- **Installing into this folder.** The project belongs to the owner.

## Ask, one question at a time

1. **Project folder path.** If none exists, offer to create one under a name the owner picks.
2. **Global or per project.** Global (`~/.claude/`) puts Backbrief in every project. Per project (that project's `.claude/`) keeps it in one. Either way the project gets its own scaffold.

Then run "Detect the existing setup". Then ask three layer questions, each naming what it changes. Ask them once per project, whichever scope the owner chose. Defaults: on a fresh install enforcement is recommended and goes on if the owner states no preference (its README says so); when merging into an existing setup, or for the memory and status layers in every case, the default is no.

3. **Enforcement** (`kit/enforcement/README.md`). "Want Claude Code to ask you before outward shell commands run, such as git push, curl or a deploy? Commits, builds and file edits stay untouched. On a fresh install this is recommended and goes on unless you say no; on an existing setup it stays off unless you say yes."
4. **Memory layer** (`kit/memory-layer/README.md`). "Want each new session to load your latest handoff note and recent decisions? It costs a few hundred tokens at session start."
5. **Status layer** (`kit/status-layer/README.md`). "Want a hook to record which Backbrief command you launched last, so `/bb-status` can report it?"

An unclear answer is no. Then state in three lines what you will do, and do it.

## Detect the existing setup

Read the target `.claude/` and the project root before copying. More than one case can apply. Route each to `kit/INTEGRATION.md`.

- **An earlier Backbrief product (Case A3, an upgrade).** `.claude/VERSION` names Backbrief Business OS, Backbrief Kit, or an older name (Business OS, Shiproom Kit, Agent OS Kit). With no stamp, look for a `.claude/CLAUDE.md` opening with one of those headings plus our agent and rule names. If the signals disagree, or the folder mixes ours and theirs, show what you found and ask.
- **The owner's own `.claude/` files (Cases A to D).** The copy below skips every file that exists. Report each name collision and offer Case B's options.
- **A project `CLAUDE.md` (Case A2).** See "Copy".

**Case A3, in order.**
1. Say which version they move from and to, and get a yes.
2. Copy `.claude/memory/` to `<project>/_backbrief-backups/<old-version>-<date>-<time>/`, outside `.claude/`, with a colon-free time like `1432`. Say where.
3. Replace the shipped files (agents, commands, rules, skills, `CLAUDE.md`, `VERSION`, `reference-manifest.json`). For `CLAUDE.md` and each rule, first hash the installed file (sha256, CRLF normalized to LF) against `payload_files` in `kit/.claude/reference-manifest.json`. A match with `current` or `known_prior` means it is ours: replace it. No match means the owner edited it: leave it and name it. A global `~/.claude/CLAUDE.md` that matches nothing is the owner's own configuration; offer the pointer block below instead.
4. Add what this release adds. Leave in place any file the earlier product shipped and this one does not, list them, and say removal is the owner's call.
5. Leave `.claude/memory/`, `context/`, `inputs/`, `outputs/`, `workflows/` and the project `CLAUDE.md` alone. Confirm `.claude/VERSION` now reads "Backbrief <version>".

## Copy

Copy the contents of `kit/.claude/` into `TEAM` (`~/.claude/` or `<project>/.claude/`, created if missing) and the contents of `kit/scaffold/` into `PROJECT` (the project root, even on a global install). Run from this folder. Before copying, note which destination files exist; afterward, list what was copied and what was skipped because it already existed.

```bash
# macOS, Linux, Git Bash
mkdir -p "$TEAM"
cp -Rn kit/.claude/. "$TEAM"/
cp -Rn kit/scaffold/. "$PROJECT"/
```

```powershell
# Windows PowerShell
New-Item -ItemType Directory -Force "$TEAM" | Out-Null
robocopy "kit\.claude" "$TEAM" /E /XC /XN /XO
robocopy "kit\scaffold" "$PROJECT" /E /XC /XN /XO
```

Guards:

- **No nesting.** Copy contents, not the `.claude` folder itself, or you get `.claude/.claude/`. Check for it afterward and move the contents up if it appears.
- **Scaffold stays out of `.claude/`.** It carries its own hidden `.claude/memory/`, which belongs in the project. Confirm `.claude/memory/decisions.md` landed.
- **Robocopy's summary table is normal output.** Exit codes 0 to 7 mean success; 8 or higher means failure.

**A project `CLAUDE.md` already exists (Case A2).** The scaffold copy skips it. Show the owner INTEGRATION.md's Case A2 pointer block verbatim and ask before appending it. Update an existing Backbrief section in place. If they decline, the team works either way. A skipped global `~/.claude/CLAUDE.md` gets the same treatment, using Case A.

## Layers (only on a yes)

Layers write to `<project>/.claude/settings.json`, and an unparseable settings file disables every permission rule in it. Guard every write:

1. **No settings file:** create one holding only the new entries. **A file exists:** back it up beside itself as `settings.json.backbrief-backup-<date>` (add the time if that name exists) and say where.
2. **Merge additively, as a text splice.** Add entries into the existing arrays, skip ones the owner has, and remove, reorder or rewrite nothing. Do not round-trip the file through a JSON serializer, which reflows their formatting.
3. **Re-read and parse the result as JSON.** If it fails, restore the backup, say so, and leave that layer uninstalled.
4. **Show before and after,** so the owner sees their own entries survive.
5. **A settings file created after this session started is not read by it.** Say the layers take effect in a fresh session opened in the project.

**Enforcement.** Merge `kit/enforcement/settings-enforcement.json` into `permissions.ask` and `permissions.deny`, creating `permissions` or an array only if absent (INTEGRATION.md, Case D). Summarize by category. If their settings already hold the `backbrief-enforcement-canary` deny rule, offer only the missing entries.

**Memory layer.** Copy both scripts from `kit/memory-layer/hooks/` into `<project>/.claude/hooks/`. Build the entry from `kit/memory-layer/settings-memory-template.json`: the `sh` form on macOS and Linux, the `windows` form on Windows, with `<ABSOLUTE-PROJECT-PATH>` replaced by the real path, each backslash doubled for JSON. Merge into `hooks.SessionStart` beside any hook already there. Say that moving the project folder later silences the hook.

**Status layer.** Same shape, using `kit/status-layer/hooks/` and its template; merge the `UserPromptSubmit` and `Stop` entries. Then prove it: run the installed script for this OS once from the project root, with `CLAUDE_PROJECT_DIR` set to the project and `{"hook_event_name":"UserPromptSubmit","session_id":"install-check","prompt":"/next"}` on stdin. Confirm `.claude/memory/backbrief-status.json` parses, then delete it and `.claude/memory/backbrief-events.jsonl` if this run created them.

## Verify

Follow `kit/.claude/commands/verify-install.md` by file path, from this folder. A personal command of the same name in `~/.claude/commands/` would shadow the shipped one and report on an install it is not part of. Treat the chosen project as the current project and check the `.claude/` you installed into. Run every step; a step that cannot run prints "not checked" with the reason.

Two rows cannot be proven from here: enforcement liveness (the canary probe) and memory-layer liveness. This session does not read a settings file created after it started, and the rules and hooks live in the project's scope. Do not run the canary here. Report both rows as not checked. The first `/verify-install` in a fresh session opened in the project is the proof; with enforcement on, it should end "LIVE: canary blocked."

Show the result, and name any step that failed. Then offer `/setup`: freshly copied commands do not load in this session, so tell the owner to open Claude Code in the project and run it there. Once the check is green, the unzipped folder can be deleted; the download can be fetched again. Offer that, and do not delete it unasked.
