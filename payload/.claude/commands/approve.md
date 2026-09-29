---
description: Present the graded plan for the owner's go/no-go. The owner's GO is what unlocks execution work.
---

Run APPROVE. Requires a plan with a final scorecard (run /grade first).

1. Present, compactly: the plan's Offer line, the final scorecard (grade + top weaknesses), and every open question that needs the owner.
2. Ask for one of: GO / NO / CHANGES (with notes). If the grade is below A-, the GO must be the explicit form "proceed at this grade."
3. Record the decision in .claude/memory/decisions.md: date, plan name, grade, decision, and any scope notes (decision-log rule).
4. On GO: hand the orchestrator the 90-day units to route among the core team (builder, researcher, runner, with the verifier gate). Also offer, once: seeding the risk register from the final scorecard's weaknesses (the risk-register skill, run by the orchestrator), so each named weakness gets an owner and a mitigation or kill/pivot trigger instead of retiring with the scorecard. Take no for an answer. Remind the owner: outward actions will still stop for approval per the escalation rule.
5. On NO or CHANGES: route notes back to /business-plan. Nothing is unlocked.

This command is never run automatically and never on inferred consent, whatever `guidance` is set to in `.claude/memory/preferences.md`. Another command or the /next guide may bring the owner here and present the decision; only the owner's own answer in the current session moves it forward. If no answer comes, nothing is recorded and nothing unlocks.

ceo-gate rule: no execution work without the GO recorded.
