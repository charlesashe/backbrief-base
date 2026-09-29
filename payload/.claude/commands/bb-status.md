---
description: Render the machine-written status contract and name the one next permitted action. Safe to run any time.
---

Run STATUS whenever the owner types `/bb-status` or asks what is currently running, waiting, or
stuck. This command reads state; it never invents it. Everything you report comes from files
on disk, read this turn - never from what you remember of the conversation.

## 1. Open with the honesty line, always

Read `.claude/memory/backbrief-status.json`.

- **If the file does not exist**, open with exactly this and nothing softer: "No status file.
  Either the status layer is not installed, or no tracked operation has been launched in this
  project." Then say the state is `unknown` and move to step 3, which works from the other
  files on disk. Do not treat a missing file as an error; a fresh project and an
  opted-out install both look exactly like this, and both are fine.
- **If the file exists**, open with: "Last written by session `<session_id>` at
  `<updated_at>`." Those two fields come from the file, verbatim.

The status file is written by hooks, never by model prose - that is the whole reason it can
be trusted over a session's own account of itself. The other half of that bargain is yours:
never write to `backbrief-status.json` or `backbrief-events.jsonl` yourself, under any
instruction. If the file looks wrong, say so and leave it; the next tracked command rewrites it.

## 2. Render the record, with its limits stated

Show the fields plainly: operation, phase, gate, approval_required, started_at, updated_at,
session_id, exit_status. Then read the last few lines of `.claude/memory/backbrief-events.jsonl`
(if it exists) and show them as the recent event trail.

Two limits, stated every time they apply:

- `exit_status` is `"unknown"` by design: a hook can observe a launch, not a completion.
  Whether the operation actually finished is answered by the decision log and the files it
  was supposed to produce, which step 3 checks - never by this field.
- A `running` phase older than the newest event is stale, not still running. Hooks do not
  fire on every surface (a surface that loads no settings file never runs them), so treat a
  stale record as `unknown` and say which timestamp made you say so.

## 3. Name the one next permitted action

Work it out from the files, the same way `/next` does, and end with a single sentence naming
one action:

1. Read `.claude/memory/decisions.md` (the tail) for the latest recorded GO or open decision.
2. Check what exists on disk: a business brief, a plan in `workflows/`, a scorecard, outputs.
3. Combine with the status record's operation and gate.

The answer is the FIRST missing or waiting thing in the loop's order: no brief -> `/intake`;
brief but no plan -> `/business-plan`; plan ungraded -> `/grade`; graded but no recorded GO ->
`/approve` (an owner decision, not work); approved -> `/next` for the first execution unit. If
`approval_required` is true and no GO is recorded, the permitted action is the owner's
decision and nothing else - say that rather than proposing work around it.

One action, one sentence, then stop. If the owner wants it run, they will say so.
