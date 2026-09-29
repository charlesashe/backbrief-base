---
description: Turn the business brief into a gradeable business plan with 90-day execution units.
---

Run BUSINESS-PLAN. Requires outputs/business-brief.md (run /intake first if missing).

1. Orchestrator reads the brief, context/strategy/ if present, and the decision log.
2. Write workflows/active/business-plan-<name>.md from workflows/business-plan-template.md. Route research gaps to the researcher and the unit-economics section to the builder, loading the unit-economics skill, before finalizing the draft; if either agent is unavailable in this session, draft the section from the brief alone and mark it "flagged for routing."
3. Use only the brief's numbers; keep estimates marked. Where the brief says unknown, the plan says unknown: the grade will price that honestly. Two skills are available as planning support here (ceo-gate's stated exception): when the plan leans on market claims that have no evidence behind them, offer ONE market-validation pass (researcher) to build the evidence base /grade's market-realism dimension will ask for; when a load-bearing assumption is untested and cheap to test, offer experiment-designer to spec the smallest decisive test as a plan unit. Offer each at most once; take no for an answer.
4. Keep the 90-day units small, owned, and testable: every unit gets pass/fail acceptance criteria.
5. Finish with: "Draft plan ready. The next step is /grade: five advisors score it against the public rubric and will not flatter it." Then honor `guidance` in `.claude/memory/preferences.md`: on `manual`, stop; on `guided`, offer to run /grade and wait for a yes; on `auto-prep`, still STOP and ask, because /grade dispatches five advisors and is the most expensive step in the loop. Say that is why you are asking.
