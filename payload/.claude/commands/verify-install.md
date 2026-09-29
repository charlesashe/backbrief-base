---
description: Check that Backbrief is installed correctly and report a plain pass/fail list. Safe to run any time.
---

Run VERIFY-INSTALL when the owner wants to confirm the install is wired up (or when anything feels off after an install or update).

**Every step below runs, every time.** Step 1's payload table is the part that looks like the whole job and is not: step 2 checks whether the enforcement rules are actually in force, step 3 checks whether the documents on disk are the ones this release ships, step 4 checks whether the commands in this project are the ones actually running, and none of those failures are visible to step 1. Finishing at the table and printing a verdict is the single most likely way this command lies to an owner, because a complete-looking report is indistinguishable from a complete check. Every step gets its own row in the summary, including a step that could not run and why.

Check the payload where it was actually installed: the global `~/.claude/` for a global install, or this project's `.claude/` for a per-project install. If both hold a payload, say which parts of which copy are actually in force, because the answer is not the same for all of them and one sentence cannot cover it. Agents resolve project-first: `.claude/agents/` wins over `~/.claude/agents/`. Commands and skills resolve the other way (personal overrides project), so with Backbrief in both places, `/next` and every other command runs the copy in `~/.claude/`, not the one beside the agents it is coordinating. A buyer can therefore run this release's agents under an older release's commands and see nothing announcing it. Check the project copy in detail, but report both, their `.claude/VERSION` values, and this split. Two different versions in the two locations is worth saying out loud, and step 4 is where it gets resolved into which files actually run. Say which you checked either way. The project-folder rows below always refer to the current project.

Start by reporting the installed version from `.claude/VERSION` (for example "Backbrief 0.1.0"). If that file is missing but agents are present, the install predates version stamping: say so and offer to add it. If `.claude/` is missing entirely in a project that has `context/` and `outputs/` folders, that is the classic moved-or-copied-project failure: `.claude` is hidden, so it is easy to leave behind when a project is moved, copied, zipped, or synced. Say that plainly, because the symptom otherwise looks like the team silently forgetting how to work, and offer to reinstall from the download.

**Where the manifest lives.** Every step below that reads `reference-manifest.json` resolves it in this order: the installed copy at `.claude/reference-manifest.json`, beside `VERSION` (the predecessor product's installer shipped it there from its 3.14.0 release and Backbrief ships it from 0.1.0, and upgrades replace it like any shipped file), then the download this install came from, if it still exists. A predecessor install from before its 3.14.0 release whose download is gone has no manifest to read; each manifest-dependent row below then prints **not checked** with that reason, and the fix to offer is one line: the next upgrade installs the manifest, or copy `kit/.claude/reference-manifest.json` from a fresh download into `.claude/` now.

1. Check each item and print a one-line result per row, pass or fail, no jargon:
   - `.claude/agents/`: expect 12 agent files (7 core, 5 council advisors); name any that are missing.
   - `.claude/commands/`: expect the names listed under `shipped_names.commands` in `reference-manifest.json` (17 in this release: next, setup, verify-install, demo, critique, council, find-gap, grade-idea, grade-video, pick-niche, handoff, pickup, bb-status, intake, business-plan, grade, approve). Read the list from the manifest rather than this sentence where the two disagree: the manifest is generated from the payload, this sentence is typed.
   - **Leftover command files from a predecessor install before its 3.4.0 release:** if `.claude/commands/` still holds `resume.md` or `plan.md`, they are from an install that predates the rename and are not part of this release. Neither can ever run: Claude Code's built-in `/resume` and `/plan` own those names, which is why they were renamed to `/pickup` and `/business-plan`. Say so and offer to delete them, and get a yes first.
   - `.claude/rules/`: expect 12 rule files, including ceo-gate and grading; name any missing.
   - `.claude/skills/`: expect exactly the folders listed under `shipped_names.skills` in `reference-manifest.json`, plus THIRD-PARTY-LICENSES.md; name any missing or unexpected. Every skill folder has a SKILL.md. The third-party skills each carry a LICENSE file; the first-party Backbrief skills, named in THIRD-PARTY-LICENSES.md's first-party carve-out, ship without one by design - a missing LICENSE on a carve-out skill is not a finding.
   - Parse every SKILL.md's YAML frontmatter (the block between the opening `---` pair). A frontmatter block that fails to parse, or that lacks a `description:` field, means Claude Code cannot auto-discover that skill - it fails silently, with the folder sitting there looking installed. Name each such file as a FAIL, not a note.
   - Root `CLAUDE.md` present (global `~/.claude/` install or this project).
   - Project folders: `context/strategy/` (with the two strategy files), `context/reference/`, `inputs/`, `outputs/`, `workflows/`, `templates/`, `examples/` (with the worked business example). A missing `context/reference/` is a soft fail on installs from before kit 1.3.0: offer to create it.
   - `.claude/memory/decisions.md` present in the project (the decision log the decision-log rule writes to). If missing, offer to create it from the scaffold.
   - `.claude/memory/preferences.md` present. Missing is a soft fail on predecessor installs from before its 2.1.0 release: say /setup will write it, or offer to create it from the scaffold now.
   - Project root `CLAUDE.md`: if it exists but never mentions Backbrief or the orchestrator, the project predates this install. Say so in one line and offer to add a short pointer section; never rewrite their file. Separately, if it still holds scaffold placeholders such as `<PROJECT NAME>`, it has never been filled in: that is not a broken install, but say so and point at /setup, because mentioning the product is not the same as being set up.
   - Common mistake check: look for a nested `.claude/.claude/` folder. If found, say plainly that the copy went one level too deep and offer to fix it by moving the contents up.
2. Enforcement self-test (opt-in permission rules). The enforcement profile is a set of native permission rules the installer offers at install and merges into `.claude/settings.json` on a yes: it makes the escalation rule's stop mechanical for outward shell commands on the command path. This step checks it two ways: is the full rule set present (completeness), and is the engine applying it (liveness). Three outcomes; only one needs fixing.

   **Completeness.** Gather the `permissions.ask` and `permissions.deny` arrays from every settings file the engine reads here: this project's `.claude/settings.json` and `.claude/settings.local.json`, and the user-level `~/.claude/settings.json`. Permission rules merge across all of them, so an entry in any of those files counts as present. The expected manifest is at the end of this file: 177 `ask` rules (88 `Bash(...)` and 82 `PowerShell(...)` (every outward pattern ships in both shell namespaces, because a rule in one namespace does nothing for the other) plus 7 `Edit(...)` rules covering the settings files, the agent definitions, the rules, and the decision log) and 2 `deny` rules, 179 in total. The two `deny` rules for `backbrief-enforcement-canary` are the opt-in marker: they exist nowhere except this profile, so either one's presence tells you enforcement was installed, while an owner's own rule that happens to match one of ours (their own ask on `git push`, say) tells you nothing and must not turn this row into a finding.

   - **A canary rule present** → enforcement was opted into. Diff the union against the manifest. All 179 present → report "Enforcement: all 179 expected permission rules present (both shell namespaces, plus the settings-file guard)", then run the liveness probe below. Any missing → name each missing rule exactly and say plainly that a partial profile is partial coverage; offer to add the missing entries (get a yes first). Two shapes of partial deserve their own sentence. If one namespace's rules are largely present and the other's are largely absent (an older profile shipped `Bash(...)` rules only), say that this install is protected in one shell and unprotected in the other, and that the fix is merging the current two-namespace profile. And if the shell rules are all present but the three `Edit(...)` settings-file rules are missing (an older profile shipped before those were added), say plainly what that gap is: without them an agent that holds file-editing tools can edit the permission rules out of the settings file and take the outward action on its next step, because a registered settings file's rules are re-read live. The fix is merging the current profile. If the owner says they removed specific rules on purpose, that is their call: record the row as a pass with that note instead of a failure. An expected `ask` entry found in a `deny` array instead still counts: that is stricter, not broken; note it in one line.
   - **No canary rule, and few or none of the expected rules present** → enforcement was not opted into, which is a valid install, not a defect. Report "Enforcement: not installed (opt-in)" as a pass with a note, and mention once that the installer can merge it in any time from the download's `enforcement/` folder: the owner only has to ask.
   - **No canary rule, but most of the expected `ask` rules present** → that looks like a mangled merge, not a coincidence. Report it as partial, name the canary rules among the missing, and offer the same fix.

   **Liveness: run in every branch.** What is on disk and what this session is enforcing are two different states, and this command must never report one as the other. Run the shell command `backbrief-enforcement-canary` once, through whichever shell tool this session runs commands with (Bash or PowerShell, do not force one). The canary is a command that exists nowhere, so the probe is inert whatever happens: either the permission engine refuses it (a response saying permission was denied, proof the deny rule is in force, which a missing command cannot fake), or it reaches the shell and dies "command not found" (the PowerShell "not recognized" equivalent counts): proof no deny rule is in force on this path. Then report the PAIR:

   **Ask-layer liveness: run whenever the deny canary was refused.** The deny canary proves the profile is loaded; it cannot prove the `ask` rules - which are nearly the whole profile - are active in THIS session, because `deny` survives the bypassPermissions mode while `ask` prompts are off in an interactive bypass-mode session. So probe the ask layer the same way: run `backbrief-enforcement-askcanary` once, through the same shell tool. Three outcomes, each meaning one thing:

   - **A permission prompt appears** (interactive session, default mode) → the ask layer is active; the prompt itself is the proof. Tell the owner to answer no, and report "ask layer: ACTIVE (you just saw it work)."
   - **The command is refused without a prompt** (headless run) → the ask rules fail closed here; report "ask layer: ACTIVE (fails closed headless)." Measured behavior: in headless runs, ask rules fail closed in every permission mode, including bypass.
   - **The command executes and dies "command not found"** → this session is in an interactive bypass-style mode and the ask layer is OFF with it. Report the three lines honestly: "canary: LIVE (deny survives bypass) · ask layer: INACTIVE (bypass-mode session) · overall: NOT FULLY ENFORCED in this session." A LIVE deny canary over an inert ask layer must never be reported as full enforcement - that is a check passing with zero comparisons.

   - **Manifest complete + canary refused + ask layer active** → "Enforcement: LIVE: canary blocked by the permission engine."
   - **Manifest absent + canary not found** → the two halves agree; the "not installed (opt-in)" pass-with-note above stands.
   - **The two halves disagree: in either direction** → do not issue a verdict from whichever half you prefer. Report exactly this: the settings on disk and the settings in force in this session differ, and the session needs restarting before this command can say anything true about enforcement. Then the likely cause, by direction: rules on disk but canary not found → either the settings file was created after this session started (a session never reads a settings file born after it, verified behavior; edits to a file that existed at start do apply), or the session's shell tool and the rules' namespace do not line up (an older Bash-only profile in a PowerShell-shell session; the fix is merging the current two-namespace profile, not hand-editing JSON), or the file has a JSON syntax error: check in that order. Canary refused but rules absent from disk → the rules were removed or edited during this session and the engine is still enforcing what it registered; do NOT offer to install what is already live: restart first, then rerun this command.

   When enforcement is on, add this one-line bound to the report so the claim stays honest: these rules cover direct and wrapped shell invocations on the command path; script interiors and MCP server tools are governed by the escalation rule itself.

2b. Memory layer self-test (opt-in session-recall hook). The memory layer (`kit/memory-layer/` in the download) is a SessionStart hook the installer offers per project: it loads the newest handoff brief and the tail of the decision log into context at session start. A project that never asked for it is a pass, not a fail. Check both halves and report them as a pair; never report one alone.

   - **Completeness:** look in `.claude/settings.json` and `.claude/settings.local.json` (hooks in both fire) for a `SessionStart` hook entry whose command contains `backbrief-memory-recall`, AND confirm the script file that command points at actually exists on disk at the path it names.
   - **Liveness:** look at the CURRENT session's own context for a line beginning `[Backbrief memory]`. This cannot be faked by reading a file; it is either there because this session's start actually ran the hook, or it is not there.
   - Report exactly one of these three outcomes:
     - **Installed and live**: both halves present. Say so in one line. If the project's memory folder holds no handoff briefs yet, the hook has nothing to print and no marker appears; when completeness is present and the handoffs folder is empty, report "installed, nothing to recall yet" as the pass instead of a disagreement.
     - **Not installed**: neither half present. A valid opt-out: pass it, and name the folder where it can be added later (`kit/memory-layer/` in the download).
     - **The halves disagree**, in either direction: do not guess which one is right. Report that either the settings changed after this session started or the project was moved or renamed (the hook carries an absolute path on Windows, so a moved project goes quiet rather than erroring), and that a restart is needed before this check can say anything true. Never install or repair the layer while the halves disagree.

3. Shipped reference files: vintage, not just presence. A file can be present, complete, and still be the copy from an install two releases ago: the scaffold is copied with a never-overwrite rule, so an upgrade replaces the team but never the documents the team ships alongside it. Presence checks cannot see this, and it is exactly how a buyer ends up reading a worked example that no longer matches the product.

   The manifest is `reference-manifest.json`, resolved per the order above (installed copy first, download as fallback). It lists only files Backbrief ships read-only, for the owner to read rather than fill in. Files the owner authors (`context/strategy/`, `.claude/memory/`, the project `CLAUDE.md`, `context/reference/SOURCES.md`) are deliberately absent from it and are never hashed or compared. If the manifest is not to hand in either location (a pre-3.14.0 install whose download is gone, the folder is outside this session's reach, or no hashing tool is available), print the row as **not checked**, with the reason, and carry that into the verdict below as a check that did not run. Never guess at vintage from a file's contents, and never let a skipped check disappear into "everything checks out": a check that silently does not run is indistinguishable from a check that passed, which is the failure this step exists to catch.

   For each listed path, hash the installed copy and compare. **Normalize line endings before hashing** (CRLF to LF) or a file that was only ever line-ending-converted reads as modified; four of eleven real installed copies checked on 2026-08-18 carried CRLF, so this is the common case, not the corner case. Use the session's own shell (`sha256sum`, `shasum -a 256`, or PowerShell's `Get-FileHash -Algorithm SHA256`) after normalizing. If none is available, say the vintage check could not run and move on; do not substitute a guess from the file's contents.

   Print one line for **every** path in the manifest, including the ones that pass and the ones you are deliberately leaving alone. This is a per-file vintage report, not a single verdict on the install: files ship and change independently, and "the download is newer than the install" is a different statement from "this document is from an earlier release." Do not compare `.claude/VERSION` against the manifest's release as a substitute for hashing the files: a stamp is what the install claims, the hashes are what it holds.

   Four outcomes, one line each:
   - **Hash matches `current`** → pass, nothing to say beyond the row.
   - **Hash matches a `known_prior` entry** → report it plainly: present, but from release X, and this release ships a newer one. Name what the buyer is actually missing where you know it. Offer to replace it from the download's `kit/scaffold/` folder (or from a fresh download, if the original is gone - the manifest resolving from the installed copy no longer implies the download still exists), and get a yes first: a hash proving the file is unmodified proves nothing about whether the owner wants it changed.
   - **Hash matches nothing in the manifest** → the file was modified, or it came from a build this manifest does not know. Leave it alone and say so. Never replace on an unrecognized hash: an incomplete manifest must degrade into today's behavior, never into overwriting something the owner wrote.
   - **File absent** → the scaffold copy was partial; offer to copy it from the download.

4. Name collisions: which copy of each command actually runs. Commands and skills are one namespace, and across levels **personal overrides project**: a skill or command in `~/.claude/` replaces the same-named one in this project, silently. Nothing warns, nothing errors, and the shadowing file just runs instead. Subagents go the other way (`.claude/agents/` outranks `~/.claude/agents/`), which is why this step is about commands and skills only. Within one level, a skill beats a command of the same name.

   Take the shipped names from `shipped_names` in `reference-manifest.json`. Compare them, case-normalized (lower-case, then drop everything that is not a letter or digit), against the names present in `~/.claude/commands/**/*.md` (including subfolders - a command file in a subdirectory still claims its bare name) and `~/.claude/skills/*/`. Normalize rather than matching exactly: over-reporting a near-miss costs one line, under-reporting hides a command the owner is not actually running. Plugin skills are namespaced (`plugin:skill`) and cannot collide; ignore them.

   **Third namespace: Claude Code's own built-in commands.** A built-in lives in neither
   `~/.claude/commands/` nor `~/.claude/skills/`, so a check that compares only those two folders
   reports "no collisions" with total confidence while a shipped command is unreachable. That is
   exactly how `/resume` and `/plan` shipped broken for several releases, and it is why this
   sub-step exists.

   **`/resume` is taken outright:** typing it opens the session picker and a command file of that
   name never runs. Observed and reproducible. **`/plan` is contested rather than dead:** a command
   file of that name DOES run in the Claude Code desktop app, so which one wins depends on the
   client. The likely reason is that the built-in `/plan` declares `requires: {ink: true}` and the
   built-in `/resume` declares no such requirement. Most built-ins take no name at all: a project
   command named `context`, `agents`, `diff`, or `export` runs instead of the built-in. Do not
   generalize in any direction. Test the specific name in the client you actually use.

   How to test one in ten seconds: type it in an interactive session. If the built-in's own
   behavior appears, the shipped file is unreachable. Typing `/` alone lists the built-in names
   the app offers, which is the cheapest way to spot a new collision after a Claude Code update.
   If a shipped name matches a built-in, say plainly that typing it never reaches our file, and
   name the command that replaces it. As of this release no shipped name collides: `/resume`
   became `/pickup` and `/plan` became `/business-plan`.

   Before classing any shadow as identical to or differing from the shipped copy, normalize line endings on both sides (CRLF to LF), exactly as the vintage check in step 3 hashes. A copy that differs only in line endings is the same file wearing Windows newlines - the common case on real installs, not the corner case - and it reports as identical, never as a differing shadow. A raw-byte compare on a real install (2026-08-31) reported five commands and ten skills as differing global copies when only two actually differed; the other thirteen were line endings.

   Report one line per collision, and name the file that wins, not the file that loses:

   - **A personal file shadows a shipped command or skill** → say which shipped name is not running, which file runs instead, and that this is the documented behavior rather than a fault. Do not offer to delete or rename anything in `~/.claude/`: it is the owner's, it may be deliberate, and renaming someone's own command to fix ours is not a repair.
   - **The shadowing file differs from the shipped copy.** Before calling it stale, establish whose bytes it holds: hash it (CRLF normalized to LF) against the current and `known_prior` entries in `payload_files` in `reference-manifest.json`, exactly as the upgrade path does. Also read its opening lines - an owner who deliberately forked a file may have said so in it. Three outcomes:
     - **Hash matches an older shipped vintage** → Backbrief itself at an older version (a global install from an earlier release sitting over this project's newer one). This is the common case and the most misleading, because both copies are Backbrief and nothing looks wrong. Say plainly that the project's agents are this release's while the commands running are the older global ones, and that the fix is upgrading the global install to match, not deleting either.
     - **Hash matches nothing in the manifest** → the owner changed it, or it was never ours. **Never offer to overwrite it**, however stale it looks - "older and larger than the shipped file" describes a customized file exactly as well as a stale one, and overwriting a deliberate fork destroys work that exists nowhere else. Report it as an owner-modified override, pass with note, the same verdict the manifest's upgrade guard gives an edited rule.
     - **File not in `payload_files`** (skills and most commands are not hash-tracked) → you cannot settle vintage mechanically. Say which copy runs and that it differs, but offer no fix in either direction; the owner knows which one they mean.
   - **No collisions** → one line saying so, and say which namespaces you compared (personal commands, personal skills, and the built-ins). A verdict that does not name what it checked is indistinguishable from one that checked less. Worth stating out loud, because its absence is what makes the rest of this report mean anything.

   This step is why the install procedure runs `/verify-install` by explicit file path rather than as a slash command: a shadowed detector reports on an install it is not part of.

**4a. Team-parity summary line.** When more than one person runs this product against the same project, "is everyone's install correct" is not a question one run can answer: this check only ever sees the machine it runs on. What it can do is produce one short, literal line that is trivial to compare against a teammate's:

   ```
   PARITY: v<version> | rules:<LIVE|off|MISMATCH> | shadows:<n>
   ```

   - `v<version>`: the bare number from `.claude/VERSION` (the same file the opening version report reads); `v?` if the file is missing.
   - `rules:`: `LIVE` only if step 2's completeness scan found the full expected rule set AND the deny canary was refused AND the ask-layer probe read active; `ask-inert` if the deny canary was refused but the ask-layer probe executed (a bypass-mode session: the profile is installed and NOT fully enforcing here); `off` only if step 2's "not installed (opt-in)" pass fired with no canary and no expected rules present; `MISMATCH` for every other outcome, including a partial rule set or a disagreement between what is on disk and what this session is enforcing.
   - `shadows:<n>`: the count of name collisions found in step 4.

   Print this line once, at the end of the report, exactly in this format. Two teammates with identical lines are at parity. Any differing field names the exact thing to reconcile, and it is the field, not the whole report, that tells you where to start: a version mismatch means someone has not upgraded, a `rules` mismatch means enforcement is not consistently live, and a `shadows` mismatch means someone has a personal file overriding the shipped one that the other person does not. This line does not replace running the full check; it replaces guessing whether the full check needs running at all.

5. End with one of exactly two verdicts:
   - "Everything checks out. If you have not run /setup yet, that is the next step."
   - "N items need attention", followed by the shortest fix for each (offer to do the fixes yourself; get a yes before moving or copying anything).

   "Everything checks out" means every check ran and passed. If any check could not run (no manifest, no hashing tool, a folder out of reach), say so in the same breath as the verdict and name which one, so a clean-looking report is never mistaken for a complete one.

Never modify anything without the owner's yes. Apart from the canary probe (one deliberately inert command that either gets blocked or fails to exist), this command only reads, reports, and offers.

## Expected enforcement manifest

The parsed values of this list (every rule string, in this order) must equal the arrays in the shipped `enforcement/settings-enforcement.json`; the build's validate step cross-checks the two. Do not edit one without the other. `Bash(...)` and `PowerShell(...)` are separate permission namespaces: a rule matches only commands sent through its own shell tool, which is why every pattern below appears twice.

`ask`: Bash namespace (88):

```
Bash(git push:*)
Bash(git -C * push *)
Bash(git -C * push)
Bash(vercel:*)
Bash(npx vercel:*)
Bash(npx * vercel *)
Bash(npx * vercel)
Bash(bunx vercel:*)
Bash(bunx * vercel *)
Bash(bunx * vercel)
Bash(netlify:*)
Bash(npx netlify:*)
Bash(npx * netlify *)
Bash(npx * netlify)
Bash(npx netlify-cli:*)
Bash(npx * netlify-cli *)
Bash(npx * netlify-cli)
Bash(bunx netlify-cli:*)
Bash(bunx * netlify-cli *)
Bash(bunx * netlify-cli)
Bash(wrangler:*)
Bash(npx wrangler:*)
Bash(npx * wrangler *)
Bash(npx * wrangler)
Bash(bunx wrangler:*)
Bash(bunx * wrangler *)
Bash(bunx * wrangler)
Bash(gh:*)
Bash(npm publish:*)
Bash(pnpm publish:*)
Bash(yarn publish:*)
Bash(bun publish:*)
Bash(pnpm dlx:*)
Bash(pnpm * dlx *)
Bash(yarn dlx:*)
Bash(yarn * dlx *)
Bash(curl:*)
Bash(wget:*)
Bash(mail:*)
Bash(sendmail:*)
Bash(ssh:*)
Bash(scp:*)
Bash(rsync:*)
Bash(stripe:*)
Bash(docker exec:*)
Bash(direnv exec:*)
Bash(devbox run:*)
Bash(mise exec:*)
Bash(bash -c:*)
Bash(bash * -c *)
Bash(bash -lc:*)
Bash(sh -c:*)
Bash(sh * -c *)
Bash(sh -lc:*)
Bash(zsh -c:*)
Bash(zsh * -c *)
Bash(zsh -lc:*)
Bash(eval:*)
Bash(pwsh -Command:*)
Bash(pwsh * -Command *)
Bash(pwsh -c:*)
Bash(pwsh * -c *)
Bash(pwsh -EncodedCommand:*)
Bash(pwsh * -EncodedCommand *)
Bash(powershell -Command:*)
Bash(powershell * -Command *)
Bash(powershell -c:*)
Bash(powershell * -c *)
Bash(powershell -EncodedCommand:*)
Bash(powershell * -EncodedCommand *)
Bash(cmd /c:*)
Bash(cmd * /c *)
Bash(cmd /C:*)
Bash(cmd * /C *)
Bash(cmd /k:*)
Bash(cmd * /k *)
Bash(cmd /K:*)
Bash(cmd * /K *)
Bash(xargs:*)
Bash(watch:*)
Bash(setsid:*)
Bash(ionice:*)
Bash(flock:*)
Bash(find * -exec *)
Bash(find * -delete *)
Bash(find * -delete)
Bash(find -delete:*)
Bash(backbrief-enforcement-askcanary:*)
```

`ask`: PowerShell namespace (82):

```
PowerShell(git push *)
PowerShell(git -C * push *)
PowerShell(git -C * push)
PowerShell(vercel *)
PowerShell(npx vercel *)
PowerShell(npx * vercel *)
PowerShell(npx * vercel)
PowerShell(bunx vercel *)
PowerShell(bunx * vercel *)
PowerShell(bunx * vercel)
PowerShell(netlify *)
PowerShell(npx netlify *)
PowerShell(npx * netlify *)
PowerShell(npx * netlify)
PowerShell(npx netlify-cli *)
PowerShell(npx * netlify-cli *)
PowerShell(npx * netlify-cli)
PowerShell(bunx netlify-cli *)
PowerShell(bunx * netlify-cli *)
PowerShell(bunx * netlify-cli)
PowerShell(wrangler *)
PowerShell(npx wrangler *)
PowerShell(npx * wrangler *)
PowerShell(npx * wrangler)
PowerShell(bunx wrangler *)
PowerShell(bunx * wrangler *)
PowerShell(bunx * wrangler)
PowerShell(gh *)
PowerShell(npm publish *)
PowerShell(pnpm publish *)
PowerShell(yarn publish *)
PowerShell(bun publish *)
PowerShell(pnpm dlx *)
PowerShell(pnpm * dlx *)
PowerShell(yarn dlx *)
PowerShell(yarn * dlx *)
PowerShell(curl *)
PowerShell(wget *)
PowerShell(Invoke-WebRequest *)
PowerShell(Invoke-RestMethod *)
PowerShell(mail *)
PowerShell(sendmail *)
PowerShell(ssh *)
PowerShell(scp *)
PowerShell(rsync *)
PowerShell(stripe *)
PowerShell(docker exec *)
PowerShell(direnv exec *)
PowerShell(devbox run *)
PowerShell(mise exec *)
PowerShell(bash -c *)
PowerShell(bash * -c *)
PowerShell(bash -lc *)
PowerShell(sh -c *)
PowerShell(sh * -c *)
PowerShell(sh -lc *)
PowerShell(zsh -c *)
PowerShell(zsh * -c *)
PowerShell(zsh -lc *)
PowerShell(pwsh -Command *)
PowerShell(pwsh * -Command *)
PowerShell(pwsh -c *)
PowerShell(pwsh * -c *)
PowerShell(pwsh -EncodedCommand *)
PowerShell(pwsh * -EncodedCommand *)
PowerShell(powershell -Command *)
PowerShell(powershell * -Command *)
PowerShell(powershell -c *)
PowerShell(powershell * -c *)
PowerShell(powershell -EncodedCommand *)
PowerShell(powershell * -EncodedCommand *)
PowerShell(cmd /c *)
PowerShell(cmd * /c *)
PowerShell(cmd /k *)
PowerShell(cmd * /k *)
PowerShell(Invoke-Expression *)
PowerShell(xargs *)
PowerShell(find * -exec *)
PowerShell(find * -delete *)
PowerShell(find * -delete)
PowerShell(find -delete *)
PowerShell(backbrief-enforcement-askcanary *)
```

`ask`: file namespace (7):

```
Edit(.claude/settings.json)
Edit(.claude/settings.local.json)
Edit(~/.claude/settings.json)
Edit(.claude/agents/**)
Edit(.claude/rules/**)
Edit(.claude/memory/decisions.md)
Edit(decisions.md)
```

These Edit rules are not shell rules and are not a third shell namespace: they guard the layer itself. The first three cover the settings files. A registered settings file's rules are re-read live, so an agent holding file-editing tools could otherwise remove the rules above and take the outward action on its very next step, with no restart and no prompt. `Edit(...)` rules cover every file-editing tool, including Write: a `Write(...)` rule is not matched by file permission checks at all, which is why none ships.

The next two cover the agent definitions and the rules, for the same reason one level up. An agent definition's frontmatter sets that agent's own tool allowlist, and it can also set `permissionMode: bypassPermissions`, so an agent able to edit `.claude/agents/` can hand itself back the tools its definition withholds, or select the mode where Claude Code's own guard on `.claude` stops applying. `.claude/rules/` holds the escalation and ceo-gate rules the product rests on. Both are `ask`. In headless runs they fail closed in every permission mode, including `bypassPermissions` (probed, with a no-rule control that executed while the matching rule blocked); in an interactive bypass-mode session ask prompts are off and these guards are off with them, which is what the ask-layer probe in step 2 detects and reports. The final two cover the decision log itself, at both of its conventional paths, and this is a deliberate reversal of an earlier design call: benchmark measurement found the decision log is where a session under social pressure records the entry that legitimizes everything after it (a standing spend waiver, a governance change framed as an owner decision), so a write to it is now loud. The cost is stated, not hidden: a legitimate decision entry prompts once when written interactively, and in a headless run the write fails closed and the entry belongs in the session's report instead. `.claude/memory/preferences.md` and the handoff briefs remain uncovered on the original reasoning - they are written constantly, and prompting through every normal run trains the owner to click through. One bound, same as the settings guard: these are `Edit(...)` rules, so they govern the file-editing tools; a shell redirect that appends to the same file is a shape the command rules do not match (probed, with a control), and the decision-log rule's own words govern that path.

`deny` (2):

```
Bash(backbrief-enforcement-canary:*)
PowerShell(backbrief-enforcement-canary *)
```
