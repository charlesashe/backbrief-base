---
description: Watch the team work start to finish in about two minutes, using a recorded run. Writes nothing outside a demo/ folder.
---

Run DEMO when the owner types `/demo`, asks to see what this thing actually does, or has just installed and wants a look before committing to their own project. It is also the right answer to "show me an example" from someone who has not set up yet.

This is a **replay of a recorded run**, not a live one. Say that in your first line, plainly, before anything else: "This is a recorded run, a real one, captured on the date in the file, replayed here. Nothing is being graded live." A demo that lets someone believe five advisors are working right now is the exact dishonesty this product exists to argue against, and it would also be slow, expensive, and different every time.

## Hard rules for this run

1. **Dispatch nothing.** No subagents, no advisor panel, no `/grade`, no `/critique`. You are reading a file and narrating it.
2. **Ask nothing until the end.** The run is uninterrupted from the opening line to the close. The only question in this command is the last one.
3. **Write nothing outside `demo/`.** One file, `demo/trailnotes-demo.md`, written once at the end. Never touch `context/`, `outputs/`, `workflows/`, or `.claude/`. This command does not write to the decision log.
4. **The walkthrough goes on screen, in the conversation.** That is the demo. The file written at the end is a copy of it to keep, never a substitute for it, and "I wrote it to a file, go read it" is a failed run: the owner asked to watch the team work, not to be handed homework. Print all five beats and the trajectory table in your reply before you write anything.
5. **Keep it to about two minutes of reading.** Quote lines, never paste sections. If you are pasting a table you did not need, you have overrun.

## 1. Find the record

The record ships with the scaffold as Part 2 of `examples/worked-example-business.md`. Read it: Part 2 (TrailNotes) is the spine of this demo, Part 1 (NestPet) is one line at the close.

Two ways this can fail, and they look nothing alike on disk.

**Missing.** Stop and say so in one line: the worked example ships with the scaffold, so a missing file means the scaffold was not copied, and `/verify-install` will say which folders are absent.

**Present but the wrong record.** Check before narrating: the file's opening lines must say Part 2 was recorded on Backbrief 0.1.0 on 2026-09-29, and Part 2 must cover TrailNotes across three grading loops ending at `B (7.6)`. Older installs carry other records: a shorter version (NestPet only, one grading pass, an early exit, and NestPet graded `C (6.4)` rather than the re-recorded `C (5.9)`), or a TrailNotes run recorded on the predecessor product, Business OS 3.2.1, which ended at `B (7.7)`. The scaffold is copied with a never-overwrite rule, so an existing project keeps whatever example it was first installed with; a buyer can therefore have this command and an older record at the same time, and the file being present proves nothing about which record it is. If Part 2 is absent, or is a TrailNotes run recorded on anything but Backbrief 0.1.0, **stop**. Say plainly that the run this demo narrates is not in their copy of the record, name the mismatch you found, and tell them the current worked example is in the download they installed from: replacing `examples/worked-example-business.md` with the copy from the download's `kit/scaffold/examples/` folder fixes it, and `/verify-install` will confirm the rest of the payload's vintage.

In both cases: do not reconstruct the run from memory, and do not narrate it out of this file. The beats below carry quotes and a table precisely so a narrator can check them against the record: using them when the record does not back them is the invented demo this command exists to avoid, and it is worse than no demo. Do not offer to improvise a substitute walkthrough from whatever the file does contain either; that is a different demo nobody rehearsed.

## 2. Narrate the run in five beats, on screen

Write these out in your reply to the owner. One short paragraph per beat, each carrying one quoted line from the record so the owner can check you against the file. Say the recording note below word for word before beat 1. Name the moving parts as you go (the number recompute, the five-advisor panel, the grading rule) because the point of the demo is that the buyer sees who did what.

Recorded on Backbrief 0.1.0, 2026-09-29, from the specimen's brain dump; replayed here.

**1. The brief.** TrailNotes, in the brief's own line: *"Committed local hikers who go out most weekends and plan around conditions pay $6/month, monthly only, no annual plan yet, for the Thursday-night conditions email."* Nine months of operating history sit behind it: 240 paying subscribers, $1,440 MRR, 39 consecutive weekly issues. `/intake` wanted five answers from the owner (which metro, how the cost figure was arrived at, the owner's spare hours and money, which contributors would step in, what covers liability and tax) and the dump held none of them, so each went under Open unknowns instead of being answered. Say the disclosure out loud, because the record does: TrailNotes is an invented specimen business, its figures are the example's premise, and **the pipeline and every grading panel that ran on it were real.**

**2. The plan: where the product found a defect in its own example.** `/business-plan` routed the numbers to the **builder, loading the unit-economics skill**, which recomputed the specimen's stated cost stack from the brief's own rates and did not agree with it: *"The brief's cost lines sum to $391.76/month at current scale (Substack 10% of $1,440 = $144.00; Stripe 2.9% of $1,440 plus $0.30 on 240 charges = $113.76; tools $54; gas $80), not the brief's stated "about $340/month, all-in": a $51.76 gap, 15.2% of the stated figure, that cannot be closed from the brief's numbers."* The plan carried both totals as an open item rather than picking one. One researcher pass added outside prices read from vendor pages. This is the beat that matters most: the crack was reported, not sanded down.

**3. The grade.** Five advisors (contrarian, first-principles, expansionist, outsider, executor) scored six dimensions, every score citing the plan's own text, per `.claude/rules/grading.md`. Loop 1 came back **B (7.1)**, with Differentiation lowest at **5.9** and Market realism at **6.4**, both for claims nobody had checked: *"The claim that no one else does this is the owner's own, unchecked against any outside source, and the clone risk is unmitigated (risk 7)."* Financial viability scored 7.8 with the cost gap still open: the panel docked the plan where its own words admitted no evidence.

**4. The revise loop, and what moved without earning it.** A revision may address only the two lowest dimensions, then the whole rubric is regraded. Loop 2: **B (7.4)**. Market realism went 6.4 → 6.8 and Differentiation 5.9 → 6.4, and the record says what earned it: *"The gain comes from stating the limits, not from new proof."* Then say what the table shows, because it differs from a run where untouched dimensions sit still: three dimensions nobody revised also rose in that pass, and the chairman traced each. Risk went up on the clone alarm the revision had added. Execution went up on nothing new, and the scorecard says so: *"reported as advisor drift, not closure."* Untouched dimensions do not simply hold still; the record names which rises a revision earned and which it did not. Clarity, never revised, was 8.8 in all three passes.

**5. The cap, and the gate.** Loop 3: **B (7.6)**. Below the 8.5 pass line by 0.9, at the three-pass cap, so the loop stopped. It did not run a fourth pass, round up, or soften the bar for a plan that was closer. It printed the owner's three options (proceed at this grade, pivot, or kill) and unlocked nothing, because the ceo-gate rule opens execution work only on a recorded owner GO, and `/approve` was never run. Close the beat on the record's own line: *"A plan that plateaus is a result, not a failure of the system."*

Then show the trajectory table from the record (six dimensions and the average: it is the single strongest thing here, so this one you do paste):

| Dimension | Loop 1 | Loop 2 | Loop 3 |
|---|---|---|---|
| Clarity of offer | 8.8 | 8.8 | 8.8 |
| Market realism | 6.4 | 6.8 | 7.1 |
| Financial viability | 7.8 | 8.1 | 8.2 |
| Execution feasibility | 7.1 | 7.4 | 7.4 |
| Risk coverage | 6.5 | 7.0 | 7.3 |
| Differentiation | 5.9 | 6.4 | 6.8 |
| **Average** | **7.1 (B)** | **7.4 (B)** | **7.6 (B)** |

One line under it, and keep it to what the table can carry: Clarity held at 8.8, the two revised dimensions (Market realism and Differentiation) gained 0.7 and 0.9, and Risk coverage, never revised, gained 0.8, of which the record traces 0.5 to the clone alarm the Differentiation revision added and the rest to drift.
## 3. Write the one file: only after the walkthrough is on screen

With all five beats and the table printed, write `demo/trailnotes-demo.md` (create `demo/` if it does not exist): the same recording note, five beats and table, an opening line stating it is a replay of a recorded run and naming `examples/worked-example-business.md` as the source, and a closing line saying the folder is disposable. It is a keepsake of what they just read, so the owner has it after the chat is gone.

If `demo/` already exists and holds the owner's own files, leave every one of them alone and add only this file. If `demo/trailnotes-demo.md` is already there from an earlier run, overwrite it: the replay is deterministic, so the content is the same.

## 4. Close

Three short things, then stop:

- **What they just watched**, in one sentence: a plan built, graded by an adversarial panel against a public rubric, revised, regraded, and stopped at a grade nobody wanted, with the decision left to the owner.
- **The next step**, one line, chosen from the files: if `context/strategy/` is missing or still holds template placeholders, that is `/setup`, the interview that writes their context files. Otherwise it is `/next`, which reads the project and says where they are. Never both.
- **The offer to clean up**, as one question: delete `demo/trailnotes-demo.md` and the `demo/` folder if the demo created it. Get a yes: deleting is never automatic (escalation rule), and never remove a folder holding files the demo did not write. If they say no, that is fine and the file stays; do not ask twice.

Two optional lines, each only if the owner asks a question that calls for it, never volunteered as a lecture:

- The full record, including Part 1 (**NestPet**, a real business that graded **C (5.9)** and whose owner's recorded decision was to pivot), is in `examples/worked-example-business.md`.
- The optional enforcement layer (permission rules that make the escalation rule's stop mechanical for outward shell commands) is not part of this demo and is not exercised by it. `/verify-install` is the command that proves whether it is installed and live.
