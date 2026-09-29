---
description: Show where this project stands and what to do next, then offer to run it. Safe to run any time.
---

Run NEXT whenever the owner types `/next`, asks what to do now, or sounds unsure of where they are. This is the command someone runs when they are lost, so answer plainly and never make them feel behind.

## 1. Read, do not remember

Work out the stage from what is actually on disk, never from this chat's history. The owner may be in a brand new session (session-hygiene rule), so the files are the only reliable source.

Read `.claude/memory/preferences.md` for `guidance` and `project-type`. If the file is missing, treat guidance as `guided`, infer the project type from whether `outputs/business-brief.md` or a business plan exists, and offer to create the file at the end.

## 2. Work out the stage

**Business project** (`project-type: business`), first match wins:

| What you find | Where they are | Next step |
|---|---|---|
| `context/strategy/` missing, or both files still template placeholders | not set up | `/setup` |
| set up, no `outputs/business-brief.md` | ready to start | `/intake` |
| brief exists, no `workflows/active/business-plan-*.md` | brief written | `/business-plan` |
| plan exists, no `workflows/scorecard-*-loop*.md` | plan drafted | `/grade` |
| scorecard exists, average below 8.5, fewer than 3 loop files | graded, not passing yet | revise the two lowest dimensions, then `/grade` again |
| scorecard exists, 3 loop files, still below 8.5 | plateaued at the cap | the owner's three options: proceed at this grade, pivot, or kill |
| scorecard at or above 8.5, no GO in `.claude/memory/decisions.md` | waiting on the owner | `/approve` |
| a GO recorded in the decision log | approved and running | state a 90-day unit and the orchestrator routes it |

Count loops from the scorecard filenames (`scorecard-<name>-loop1.md`, `loop2`, `loop3`).

An artifact only counts as done if it has the owner's real content in it. A template that was created and saved but never filled in does not advance the stage: treat it as still missing, say so plainly, and offer to finish it. This applies to the brief, the plan, and the scorecard, not just the strategy files.

While you are reading, glance at the knowledgebase. If the project is set up but `context/reference/` holds nothing beyond the shipped templates (no files added, no real rows in `SOURCES.md`: the example rows do not count), add one line to your answer: "No knowledgebase registered yet: if you have guides, docs, or links the team should work from, name them and I will file them." Say it once, as an aside, never as a required step, and drop it entirely once the owner has sources registered or has declined in this session.

**Build project** (`project-type: build`): not set up → `/setup`; set up → state a goal in plain words and the orchestrator plans, routes, and gates it through the verifier; work finished → `/handoff` to close the session.

## 3. Say where they are

Two short lines, plain language, no jargon: where they are, and what comes next and why it matters. Name the file that told you, so the owner can check you. If a previous step produced something they have not looked at (a brief, a plan, a scorecard), offer to show it before moving on.

If `/critique` or `/council` would genuinely help right here, mention it as optional and say why in one line. Never insert them as a required step and never run them without being asked.

## 4. Then act on the guidance preference

- **`manual`**: name the next step and stop. Run nothing.
- **`guided`** (the default): offer to run the next step now and wait for a yes. One word is enough.
- **`auto-prep`**: run the next step without asking, but ONLY when it is `/setup`, `/intake`, or `/business-plan`. Announce what you are running as you go. Stop at everything else.

Run at most ONE step per invocation, whatever the mode. When it finishes, stop, re-read the files, and report the new stage. Never chain steps together in a single run.

## 5. Never automatic, whatever the preference says

`auto-prep` does not relax any of these. If the next step is on this list, stop and hand the decision to the owner, and say plainly that you are stopping because the decision is theirs.

1. **`/approve` never runs on its own.** It is the owner's recorded GO and the only unlock for execution work. Silence is never approval (escalation rule).
2. **Proceeding past a failing grade is never automatic.** Below A-, the GO has to be the explicit "proceed at this grade" and is recorded with the real grade (ceo-gate rule).
3. **Anything that results in a new `/grade` pass always confirms first**, however it is phrased. "Revise the two lowest dimensions and regrade" is a grading pass and counts. It runs five advisors and is the most expensive thing here. Say which loop is starting and that the cap is three.
4. **Every outward action stops for the owner**: sending, publishing, spending, granting access (escalation rule).
5. **No execution work before the recorded GO** (ceo-gate rule).
6. **Nothing the owner wrote is deleted or overwritten** without an explicit yes.
7. **Jurisdiction-specific legal, tax, or licensing claims** go through the researcher before they appear in output (agent-routing rule).

## 6. Close

End with the one thing to do next, and remind them once that `/next` works any time they are unsure. If they want a different pace, tell them they can say so and you will update `.claude/memory/preferences.md`.

**The deferred pace question.** If preferences show `guidance-confirmed: no` (or the key is absent) AND the files show at least one completed unit of real work beyond setup (a business brief, a plan, or a first artifact in `outputs/`), ask it now, once: "You've seen the team work. Do you want me to keep walking you through each step and asking first, just tell you what to run and wait, or run the early setup-type steps without asking?" Record the one-word answer (`guided`, `manual`, `auto-prep`) in `.claude/memory/preferences.md` and set `guidance-confirmed: yes`. Say the honest limit out loud, whichever they pick: nothing skips an approval, an outward action, or a new grading loop. Those always stop for them. Never ask this question twice.
