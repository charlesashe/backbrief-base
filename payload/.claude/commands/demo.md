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

The run lives in the project scaffold at `examples/worked-example-business.md`. Read it: Part 2 (TrailNotes) is the spine of this demo, Part 1 (NestPet) is one line at the close.

Two ways this can fail, and they look nothing alike on disk.

**Missing.** Stop and say so in one line: the worked example ships with the scaffold, so a missing file means the scaffold was not copied, and `/verify-install` will say which folders are absent.

**Present but the wrong record.** Check before narrating: the file must contain a Part 2 covering TrailNotes across three grading loops. Older installs carry a shorter version: NestPet only, one grading pass, an early exit, and NestPet graded `C (6.4)` rather than the re-recorded `C (5.9)`. The scaffold is copied with a never-overwrite rule, so an existing project keeps whatever example it was first installed with; a buyer can therefore have this command and an older record at the same time, and the file being present proves nothing about which record it is. If Part 2 is absent, **stop**. Say plainly that the run this demo narrates is not in their copy of the record, name the mismatch you found, and tell them the current worked example is in the download they installed from: replacing `examples/worked-example-business.md` with the copy from the download's `kit/scaffold/examples/` folder fixes it, and `/verify-install` will confirm the rest of the payload's vintage.

In both cases: do not reconstruct the run from memory, and do not narrate it out of this file. The beats below carry quotes and a table precisely so a narrator can check them against the record: using them when the record does not back them is the invented demo this command exists to avoid, and it is worse than no demo. Do not offer to improvise a substitute walkthrough from whatever the file does contain either; that is a different demo nobody rehearsed.

## 2. Narrate the run in five beats, on screen

Write these out in your reply to the owner. One short paragraph per beat, each carrying one quoted line from the record so the owner can check you against the file. Say the recording note below word for word before beat 1. Name the moving parts as you go (the number recompute, the five-advisor panel, the grading rule) because the point of the demo is that the buyer sees who did what.

Recorded on Backbrief Business OS 3.2.1, the predecessor product, which routed the plan's numbers to a cfo agent. In Backbrief that recompute is the builder's, with the unit-economics skill; everything else in the recording runs here as shown.

**1. The brief.** TrailNotes: *"a $6/month weekly email of local hiking trail conditions for one metro,"* with nine months of operating history behind it: 240 paying subscribers, $1,440 MRR, 39 consecutive weekly issues. Say the disclosure out loud, because the record does: TrailNotes is an invented specimen business, its figures are the example's premise, and **the pipeline and every grading panel that ran on it were real.**

**2. The plan: where the product found a defect in its own example.** `/business-plan` routed the numbers to the **cfo**, which recomputed the specimen's stated cost stack and did not agree with it: *"That sums to $391.76/month, not the brief's stated 'about $340/month, all-in'... roughly a $52 (15%) gap that cannot be closed from the numbers given."* The plan carried the gap as an open item rather than smoothing it over. This is the beat that matters most: the crack was reported, not sanded down.

**3. The grade.** Five advisors (contrarian, first-principles, expansionist, outsider, executor) scored six dimensions, every score citing the plan's own text, per `.claude/rules/grading.md`. Loop 1 came back **C (6.9)**, with Financial viability at **5.8** for exactly the gap the cfo had just found: *"The system stress-tested its own example's numbers and docked its own example's grade."*

**4. The revise loop, and what did not move.** A revision may address only the two lowest dimensions, then the whole rubric is regraded. Loop 2: **B (7.3)**: financial went 5.8 → 7.8 because *"The plan now budgets on the worse number"*, and market moved on a retrieved outside referent. The record's own line about the rest: *"Nothing else moved up: the never-revised dimensions sat still."* Say it that precisely, because the table you are about to print shows two un-revised dimensions drifting DOWN a tenth or two in the same pass: the claim is that nothing climbed without earning it, not that nothing moved. Clarity, never revised in any pass, was 8.4 in all three. The contrarian conceded only what was earned, calling the fix *"arithmetic hygiene, not new margin."*

**5. The cap, and the gate.** Loop 3: **B (7.7)**. Below the 8.5 pass line, at the three-pass cap, so the loop stopped. It did not run a fourth pass, round up, or soften the bar for a plan that was close. It printed the owner's three options (proceed at this grade, pivot, or kill) and unlocked nothing: nothing was unlocked, because the ceo-gate rule opens execution work only on a recorded owner GO. Close the beat on the record's own line: *"A plan that plateaus is a result, not a failure of the system."*

Then show the trajectory table from the record (six dimensions and the average: it is the single strongest thing here, so this one you do paste):

| Dimension | Loop 1 | Loop 2 | Loop 3 |
|---|---|---|---|
| Clarity of offer | 8.4 | 8.4 | 8.4 |
| Market realism | 6.2 | 7.4 | 7.4 |
| Financial viability | 5.8 | 7.8 | 7.8 |
| Execution feasibility | 6.8 | 6.6 | 7.6 |
| Risk coverage | 7.4 | 7.2 | 7.4 |
| Differentiation | 6.6 | 6.6 | 7.6 |
| **Average** | **6.9 (C)** | **7.3 (B)** | **7.7 (B)** |

One line under it, and keep it to what the table can carry: every gain came from a revision closing a cited defect, and no dimension climbed without one.

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
