---
description: First-time setup interview. Fills in the two context files by asking questions, so nobody has to edit files by hand.
---

Run SETUP once per project, right after installing Backbrief. It replaces "go edit these files" with a short conversation.

1. Check the install first. Confirm these exist and say so in one line each (a green check or a plain statement of what is missing):
   - `.claude/agents/` with the orchestrator, verifier, and the five council advisors present
   - `.claude/commands/` with critique, council, find-gap, handoff, pickup, intake, business-plan, grade, approve
   - `.claude/rules/` with at least the escalation and ceo-gate rules
   - `.claude/skills/` (the bundled skill library; the authoritative list is `shipped_names.skills` in `.claude/reference-manifest.json`, installed beside `VERSION`; on an install of the predecessor product from before its 3.14.0 release, which has no such file, check that the folder is populated and note that the roster check ran without the manifest)
   - `context/strategy/`, `inputs/`, `outputs/`, `workflows/`, `templates/`, `examples/` folders
   If the scaffold folders are missing, offer to create them now (copy the layout from Backbrief's scaffold, or create empty folders with the standard names) before continuing.
2. Interview the owner, one question at a time, in plain language. Do not ask everything at once:
   - "What is this project, in a sentence or two?"
   - "What are you trying to get done in the next few weeks?"
   - "Anything I should never do without asking you first, beyond the standard stops (spending, sending, publishing, deleting)?"
   - "Anything already done or decided that I should know about?"
   - "Do you have a knowledgebase the team should work from? That means documents you own (digital books, guides, product docs, style guides, standards, reports) AND links: a docs site, a Notion page, an online guide you trust. There is a `context/reference/` folder and an index for exactly this."
     If yes: copy files they name into `context/reference/` now (create the folder if the scaffold predates it), offer to fetch any freely available documents they point at (public docs, standards, their own published material), and record EVERY source (each file and each link) as a row in `context/reference/SOURCES.md` with a one-line note on when to use it (create the index from the scaffold template if it is missing; replace the example rows). Links live only in that index: a link that is not recorded there is a source the team cannot find later. Only material they have the right to use; do not go hunting for paywalled or pirated copies of anything. If they have nothing yet, say the folder and index are there whenever they do, that they can add sources any time just by naming them in chat, and that the researcher cites from the knowledgebase first.
   - "Is this project a business you want run through the Backbrief loop, or a build project?" If it is a business: point them at /intake as the next step after setup, and note the honest ground rule up front: execution work stays locked until a plan is graded and they record a GO with /approve. If it is a build project: the Backbrief commands simply stay unused; nothing to configure.
   Do NOT ask how much the team should drive. The owner has not seen the team work yet, so the answer would be a guess. Default the pace to `guided` (walk them through each step and ask before running it) and say so in one line: "I'll walk you through each step and ask before I run anything. Once you've seen the team work, I'll ask if you want a different pace." The real question is asked once, by /next, after the first unit of real work completes.
3. Write the answers into the files, in the owner's own words where possible:
   - `context/strategy/current-state.md`: one paragraph: what the project is and where it stands.
   - `context/strategy/current-priorities.md`: a ranked list of 3-5 priorities from their answer.
   - Extra constraints go in `current-priorities.md` as a "House rules" line, and anything already-decided becomes the first entry in `.claude/memory/decisions.md` (create the file if needed).
   - `.claude/memory/preferences.md`: write `guidance: guided`, `guidance-confirmed: no`, and `project-type:` from their answer (create the file from the scaffold template if it is missing). `guidance-confirmed: no` tells /next to ask the pace question once after the first real unit of work completes. This lives in `memory/` on purpose, because the payload never overwrites that folder, so the setting survives every future update.
4. Read the two files back to the owner in under 100 words and ask if anything is wrong. Fix what they correct.
5. Close with the orientation. For a build project, say exactly: "Setup is done. State a goal in plain words and the team will plan it, build it, and verify it. If you are ever unsure what to do, type /next and I will tell you where you stand. Also useful: /critique to stress-test an idea, /council for a five-advisor debate, /handoff to end a session, /pickup to start the next one." For a business project, say exactly: "Setup is done. Your next step is /intake: talk about your business for ten minutes and the team will turn it into a brief, then a plan, then a graded stress-test. If you are ever unsure what to do, type /next and I will tell you where you stand. Also useful: /critique, /council, /handoff to end a session, /pickup to start the next one."

   Then honor the default pace immediately: offer to run the next step now and wait for a yes.

Keep the whole thing under ten minutes. No jargon. If the owner says "skip" to any question, write a sensible placeholder and mark it with "(fill in later)".
