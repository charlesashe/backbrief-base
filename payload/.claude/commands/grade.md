---
description: Stress-test the business plan against the public rubric. Five advisors, cited scores, capped revise loop.
---

Run GRADE on workflows/active/business-plan-<name>.md. Obey .claude/rules/grading.md exactly.

0. Before the first pass only: if the plan's market-realism claims rest on nothing but the plan's own words (no named buyers, no comparable products, no sourced signals), say so and offer ONE market-validation pass (researcher, planning support under ceo-gate) before spending advisors on a dimension that will score low for lack of evidence. Take no for an answer and proceed.
1. Dispatch the five council advisors (contrarian, first-principles, expansionist, outsider, executor) in parallel. Each receives ONLY the plan document and the rubric (never the chat history or the whole workspace) and scores all six rubric dimensions through its own lens, citing the plan's text for every score. Advisors run on their pinned mid-tier model with a budget of 60 words per dimension; the chairman consolidation stays here on the strong model.
2. Consolidate as chairman into workflows/scorecard-<name>-loop<n>.md from workflows/scorecard-template.md: per-dimension consensus score, the citation, and the ranked weaknesses. Divergent advisor scores are reported, not averaged away silently.
3. If average >= 8.5 (A-): stop and direct the owner to /approve. Never run /approve yourself, on any guidance setting. It is the owner's recorded GO and the only unlock for execution work; silence is not approval.
4. If below and loops remain (max 3 grading passes total; the third pass is the cap): revise ONLY the two lowest dimensions of the plan, then regrade from step 1. Before starting each new grading pass, say which loop is beginning, that the cap is three, and get a yes first. This holds on every guidance setting including `auto-prep`, because each pass runs five advisors. On regrade passes, each advisor also receives the previous scorecard's scores for its lens and re-scores against the revised plan (confirming or adjusting with a citation) instead of rebuilding its analysis from scratch. The full rubric is still re-scored every pass; only the redundant re-derivation is cut.
5. If below at the cap, or if the owner declares a lowest dimension unfixable (early exit per the grading rule): STOP. Present the scorecard, top 3 unresolved weaknesses, and the owner's options (proceed at this grade, pivot, kill). Never auto-proceed.

The grade is "no confident weaknesses left un-named," never a promise of success. Say that when reporting it.
