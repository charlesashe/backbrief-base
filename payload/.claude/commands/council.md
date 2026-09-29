---
description: Run a five-advisor council on a decision. Five distinct advisors, blind peer review, chairman, and the clash.
---

Run COUNCIL MODE on the decision the user gave. Do not skip steps.

Before starting, ask up to 3 questions only if context is genuinely missing. Otherwise proceed.

Token discipline: first compress the decision into a brief of at most 300 words (the decision, the constraints, the numbers that matter), plus, when a document is central to the decision, up to 200 words of verbatim key figures or quotes from it. Every advisor receives ONLY that brief: never the chat history or full documents. If the decision cannot be stated in that space, say so and ask the user to name what matters most before dispatching. Advisors run on their pinned mid-tier model and answer within 200 words each; the chairman synthesis stays here on the strong model.

0. LOCAL LAW CHECK: if the decision turns on what is legal, licensed, required, disclosed, or taxed in a named place, dispatch the researcher on that point BEFORE the advisors run, and put the retrieved answer and its citation in the brief. Advisors reason from general knowledge and will confidently miss a statute that changed recently, which is how a compliance requirement reaches the owner unmentioned. If the check has not been run, every advisor touching the point labels it an unverified local-law assumption instead of reasoning past it (agent-routing rule).
1. FIVE ADVISORS: dispatch five subagents and present their answers, genuinely distinct, with no convergence. Use these agent types, one each: advisor-contrarian (only why it fails), advisor-first-principles (rebuild from base truths, name the user's assumptions), advisor-expansionist (upside and the bigger option being missed), advisor-outsider (no industry knowledge, common-sense "dumb" questions that expose blind spots), advisor-executor (only what the user does Monday). Run them in parallel where possible.
2. BLIND PEER REVIEW: relabel the five answers as A-E, shuffled so the labels do not reveal which advisor is which. For each, state the single strongest and single weakest point among the others.
3. CHAIRMAN: open the synthesis with one line a reader can act on without reading further: the recommendation as GO, HOLD, or NO, one sentence of reasoning, then "First move:" and the single next action, drawn from the executor's answer. Then give the full reasoning and 3 next steps. The opening line compresses the verdict; it never replaces the reasoning and never softens a disagreement the clash below has to carry.
4. THE CLASH: name the one place the advisors disagreed hardest and why that is the user's real unresolved blind spot.

Obey the constraints rule: make claims measurable; do not combine unrelated tasks without section breaks.
