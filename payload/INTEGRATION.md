# Integrate Backbrief into an existing Claude Code setup

## Who this is for

You already run Claude Code and you already have your own setup: your own agents under `~/.claude/agents/`, your own root `CLAUDE.md`, your own commands, or your own rules. You do not want to wipe any of that. You want to add the Backbrief pattern (the orchestrator, the specialist agents, the commands, and the coordination rules) on top of what you have, and keep everything you already built. This guide shows you how to do that without a fresh start, how to handle files whose names collide with yours, and how to take only the parts you want.

If you have no existing setup, or you are starting a new and empty project, you do not need this guide. Use the install routes in the README instead.

## The safe default: non-destructive install

Every copy command in the README is written to be non-destructive. On macOS and Linux the scaffold uses `cp -Rn`, where `-n` means never overwrite an existing file. On Windows the scaffold uses `robocopy` with `/XC /XN /XO`, which copies only files that do not already exist at the destination. Nothing you already have is replaced, and nothing you already have is lost. The worst case is that a kit file is skipped because you already have a file with the same name, and you decide later whether you want the kit's version.

That means the safest way to start is to run the same commands the README gives you and let the skip behavior protect your files. The rest of this guide is about the two things the plain copy cannot decide for you: how to merge your root `CLAUDE.md`, and what to do about the files that got skipped.

## Case A: you already have a CLAUDE.md

The kit ships its own root `CLAUDE.md` inside `kit/.claude/`. Do not let it replace yours. Your root `CLAUDE.md` is the file the orchestrator reads first, and it holds your project identity, so keep it as the source of truth.

Instead of overwriting, keep your file and add a short section to it that points at Backbrief's agents, commands, and rules. That way your existing instructions stay intact and the team still knows the coordination pieces exist. Open your existing `CLAUDE.md` and paste a block like this near the end:

```markdown
## Backbrief

This project uses Backbrief. Route multi-step work through the orchestrator agent, use
/critique and /council to pressure-test decisions, and follow the rules in .claude/rules/
(agent-routing, escalation, verify-before-delivery, ceo-gate). Business decisions run the
CEO loop: /intake, /business-plan, /grade, /approve.
```

Adjust the paths if you installed the team per-project rather than globally. The point is that your root file keeps its own content and gains one short pointer, rather than being swapped out.

## Case A2: your project already has its own CLAUDE.md

Case A is about the team's root file in `.claude/`. There is a second, separate collision: the scaffold ships a project `CLAUDE.md` for the root of your project folder, and if you already have one there, the non-destructive copy skips it. Your file is safe, but nothing in it mentions that a team just arrived, so the orchestrator reads a project file that describes the project without describing how work runs in it.

Fix it the same way: keep your file, add one short section near the end.

```markdown
## Backbrief

This project uses Backbrief. Route multi-step work through the orchestrator agent, use
/critique and /council to pressure-test decisions, and follow the rules in .claude/rules/
(agent-routing, escalation, verify-before-delivery, ceo-gate). Business decisions run the
CEO loop: /intake, /business-plan, /grade, /approve.
```

Skipping this is not fatal. The agents, commands, and rules work either way; you just lose the one line that tells a fresh session the team is here.

## Case A3: you already installed an earlier Backbrief product (the free Backbrief Kit or Backbrief Business OS)

This is an upgrade, not a merge, and it is the one case where you *want* the incoming files to win. The earlier product and this one share the same folder structure on purpose, so its agents, commands, and rules have counterparts here under the same names. If you run the plain non-destructive copy, every one of those collisions is skipped and you end up still running the earlier product while believing you upgraded.

Say "this is an upgrade from an earlier Backbrief product" when you install and it is handled for you. By hand, the distinction is:

**Replaced** (ours, and the point of upgrading): the shipped files under the same names, everything under `.claude/agents/`, `.claude/commands/`, `.claude/rules/`, `.claude/skills/`, the `.claude/CLAUDE.md`, and `.claude/VERSION`.

**Added** (new here, nothing to collide with): the video claim grader and the `/grade-video` command, and the niche picker and the `/pick-niche` command.

**Left in place** (the earlier product's, and the copy never deletes): files the earlier product shipped and this one does not, meaning its agents for the marketing, finance, web, and operations side of a business, its execution skills, and its skill-routing-business rule. The non-destructive copy leaves them where they are, and they keep running beside Backbrief. Whether to remove them is your call.

**Never touched** (yours): `.claude/memory/` and your decision log, `context/`, `inputs/`, `outputs/`, `workflows/` content you have written, and your project `CLAUDE.md`. Back up `.claude/memory/` before any by-hand upgrade anyway.

You can confirm which product is installed at any time by reading `.claude/VERSION`. It names the product and version, for example "Backbrief 0.1.0".

## Case B: existing orchestrator or same-named agents

The kit installs its agents under their own filenames, for example `orchestrator.md`, `planner.md`, `builder.md`, `reviewer.md`, `researcher.md`, `runner.md`, and `verifier.md`. If you already have an agent with one of those filenames, the non-destructive install skips the kit's copy so your version is untouched. You then have two ways to resolve the collision.

Option one, run both side by side. Copy Backbrief's version in under a new filename so it does not clash with yours. The copy never overwrites your file, and the original stays in the unzipped folder so a later update still has it. For example, to keep your `orchestrator.md` and also add the kit's:

```bash
# macOS / Linux, run from the unzipped folder
cp -n kit/.claude/agents/orchestrator.md ~/.claude/agents/orchestrator-backbrief.md
```

```powershell
# Windows (PowerShell), run from the unzipped folder
$dest = "$HOME\.claude\agents\orchestrator-backbrief.md"
if (Test-Path $dest) { "Skipped, $dest already exists" } else { Copy-Item "kit\.claude\agents\orchestrator.md" $dest }
```

Both agents are then available and you pick which one to call by name.

Option two, diff and adopt. Compare your version against the kit's and pull in only the parts you want, keeping your file as the base:

```bash
# macOS / Linux
diff ~/.claude/agents/orchestrator.md kit/.claude/agents/orchestrator.md
```

```powershell
# Windows (PowerShell)
Compare-Object (Get-Content "$HOME\.claude\agents\orchestrator.md") (Get-Content "kit\.claude\agents\orchestrator.md")
```

Read the differences, then hand-edit your file to add anything from the kit that you want. This keeps a single orchestrator that is yours, improved with the kit's ideas.

## Case C: cherry-pick

You may want only part of the kit. Because the payload is plain folders under `kit/.claude/`, you can copy just the subfolders you want.

To take only the rules (the coordination guardrails, without any new agents or commands):

```bash
# macOS / Linux, from the unzipped folder. -n never overwrites.
cp -Rn kit/.claude/rules/. ~/.claude/rules/
```

```powershell
# Windows (PowerShell), from the unzipped folder.
robocopy "kit\.claude\rules" "$HOME\.claude\rules" /E /XC /XN /XO
```

To take only the `/critique` and `/council` commands, copy the commands folder plus the agents those commands depend on. `/council` calls the five advisor agents (`advisor-contrarian.md`, `advisor-executor.md`, `advisor-expansionist.md`, `advisor-first-principles.md`, `advisor-outsider.md`), and both commands lean on the coordination rules, so copy the commands, those five advisor files, and the rules:

```bash
# macOS / Linux, from the unzipped folder
cp -Rn kit/.claude/commands/. ~/.claude/commands/
cp -n  kit/.claude/agents/advisor-*.md ~/.claude/agents/
cp -Rn kit/.claude/rules/. ~/.claude/rules/
```

```powershell
# Windows (PowerShell), from the unzipped folder
robocopy "kit\.claude\commands" "$HOME\.claude\commands" /E /XC /XN /XO
robocopy "kit\.claude\agents" "$HOME\.claude\agents" advisor-*.md /XC /XN /XO
robocopy "kit\.claude\rules" "$HOME\.claude\rules" /E /XC /XN /XO
```

Take as much or as little as you want. Each subfolder stands on its own.

## Case D: the enforcement layer in an existing setup

Backbrief ships an optional enforcement profile at `kit/enforcement/settings-enforcement.json`: permission rules that make Claude Code itself ask you before outward shell commands (git push, curl, deploys, and their wrapped forms) actually run. On an existing setup it is **off by default**: you already run a configuration you trust, and nothing here should change your setup's behavior without your explicit yes. What it changes if you say yes: you will start seeing approval prompts on outward commands. Everyday work (git commit, builds, file edits, tests) matches nothing in the profile.

If you want it, the installer merges it for you with the guards below. Doing it by hand, follow the same guards, in order, because `settings.json` is the one file here where a bad edit is worse than no edit: **an unparseable `settings.json` silently disables every permission rule in it, including the ones you already had.**

1. **Back up first**: copy your `.claude/settings.json` to `settings.json.backbrief-backup-<date>` in the same folder.
2. **Merge additively**: append the fragment's entries into your `permissions.ask` and `permissions.deny` arrays (create `permissions` or the arrays only if they do not exist). Skip any entry you already have. Do not remove, rewrite, or reorder anything of yours: Claude Code concatenates permission rules across scopes and files, so addition is all the merge ever needs.
3. **Validate before trusting it**: re-read the merged file and parse it as JSON (any JSON validator, or ask Claude to parse it back). If it does not parse, restore the backup and start over: never leave a broken settings file in place.
4. **Prove it, don't assume it**: run `/verify-install`. One timing rule, verified behavior: a settings file that already existed when your session started picks up edits immediately, but a settings file *created* after the session started is not read by that session at all. If the merge created your `.claude/settings.json` fresh, the proof needs a fresh session; when in doubt, a fresh session reads everything. The enforcement self-test diffs your settings against the full expected manifest and fires the canary probe; "LIVE: canary blocked" is the merge verified by the permission engine itself, not by anyone's assurance.

Your own pre-existing rules keep working exactly as before: permission arrays merge, and `deny` always wins over `ask` and `allow`, so our entries can loosen nothing you have tightened. To remove the layer later, delete the entries matching the fragment (they are listed in it exactly) or ask Claude to do it; nothing else depends on them.

## Skip the scaffold if you have your own structure

The scaffold (the `context/`, `inputs/`, `outputs/`, `workflows/`, and `.claude/memory/` folders, plus a project `CLAUDE.md` template) is meant for greenfield projects that have no working structure yet. If you already organize your project a different way, do not copy the scaffold. The agents do not require those exact folder names. They read whatever `context/` and `outputs/` locations you point them at through your `CLAUDE.md`. Keep your structure, tell the agents where things live in your root file, and skip the scaffold copy entirely.

## Verify it took

After you integrate, confirm the pieces are actually available in Claude Code. Open Claude Code in the project (or anywhere, if you installed globally) and check the two things you added:

- Type `/` and look for `critique` and `council` in the command list. If they appear, the commands are installed.
- List the agents directory to confirm the agent files landed where you expect: on macOS or Linux run `ls ~/.claude/agents/` (or `ls .claude/agents/` for a per-project install); on Windows run `Get-ChildItem "$HOME\.claude\agents\"` (or `Get-ChildItem ".claude\agents\"`). You should see the kit's agents, including any you renamed such as `orchestrator-backbrief.md`.

If the commands show up and the agent files are present, the integration took. State a goal and route it through the orchestrator to confirm the team runs end to end.
