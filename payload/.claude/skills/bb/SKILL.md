---
name: bb
description: The plain-language front door to Backbrief. Presents the six core actions - start intake, create the plan, grade the plan, approve the plan, run the next step, verify the install - each with one sentence on what it does and which gate applies, then hands off to the real command unchanged. Use when someone types /bb, asks where to start, asks what this system can do, or seems lost among the commands.
version: 1.0.0
category: Decision & Control
domain: governance
author: Backbrief (first-party)
status: draft
updated: 2026-08-31
activation_triggers:
  - "/bb"
  - "where do I start"
  - "what can this do"
  - "which command do I use"
  - "how do I use this"
  - "front door"
  - "show me the menu"
---

# bb - the front door

The system ships more than a dozen commands, and someone opening it for the first time has
no obvious first one. This skill is the answer to that: one entry point, six plain-language
actions, each explained in one sentence with its gate named, each handing off to the shipped
command exactly as it is. This skill adds no runtime of its own - it presents, explains, and
routes. It never re-implements a command, and it never skips a gate a command carries.

## When it runs

The owner typed `/bb`, asked where to start, or asked what the system can do. Read the room
first: if the project has no context files yet, `/setup` is the honest first suggestion, and
if they are mid-loop, open with where they are (a plan exists, a grade exists) rather than
the full menu.

## The menu

Present these six, in loop order, each as: what it does in one sentence, and the gate that
applies. Then ask which they want, and on their answer run that command exactly as shipped.

1. **Start intake** -> `/intake`. Turns your brain dump - text, notes, files - into a
   structured business brief the team can plan from. Gate: none; nothing leaves your machine.
2. **Create the plan** -> `/business-plan`. Turns the brief into a business plan with 90-day
   execution units. Gate: planning support under the ceo-gate - producing artifacts FOR the
   business stays locked until an approved plan.
3. **Grade the plan** -> `/grade`. Five advisors score the plan against the public
   six-dimension rubric, every score citing the plan's own text, capped at three passes.
   Gate: the grading rule; a pass is a stress-test survived, never a success prediction.
4. **Approve the plan** -> `/approve`. Records YOUR go or no-go in the decision log; the
   recorded GO is the only unlock for execution work. Gate: this one is a decision,
   not work - only the owner can give it, and silence is not approval.
5. **Run the next step** -> `/next`. Reads the files on disk, says where the project stands,
   and offers to run the next unit. Gate: whatever the unit itself carries; outward actions
   still stop for the owner (escalation rule).
6. **Verify the install** -> `/verify-install`. Plain pass/fail check of the whole install,
   including whether the guardrails are live in this session. Gate: none; safe any time.

If the status layer is installed, `/bb-status` shows the machine-written record of what was
last launched; offer it when someone asks what is currently running rather than what to do.

## Boundaries

- **Hand off, never absorb.** On a choice, run the shipped command. Do not summarize what
  the command would do and call it done, and do not blend two commands into one pass.
- **Gates travel with the command, not the menu.** Naming a gate here informs; the command's
  own text is what enforces it. If a menu sentence and a command ever disagree, the command
  is right and this file has the defect.
- **No new claims.** This skill describes the six actions in the commands' own terms. It
  never promises an outcome a command does not promise.
