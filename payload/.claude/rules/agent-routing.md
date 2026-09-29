# Agent Routing

Delegate by domain and tier:
- orchestrator: multi-step work spanning more than one agent, planning, or an unclear starting point.
- researcher: gathering facts, sources, prior art, options.
- planner: turning a goal into an ordered plan with acceptance criteria.
- builder: producing the actual artifact (code, copy, document, config).
- reviewer: a quality pass on a draft before it is finished (not the final gate).
- runner: cheap, mechanical, verifiable work with explicit acceptance criteria (a cheap model).
- verifier: the final fresh-context check against acceptance criteria before delivery.

Jurisdiction and regulated claims:
- Legal, tax, licensing, and disclosure requirements are local and they change. Advisors and planners reason from general knowledge, which is exactly where this fails: a statute that changed last year is invisible to them, and the answer still sounds confident.
- Any claim about what is legal, required, licensed, disclosed, or taxed in a named place goes through the researcher, with retrieval, BEFORE it can appear in an advisor's score, a plan's Risk section, or guidance the owner might act on.
- The trigger is the moment a jurisdiction becomes specific. "Is this business model legal" is a general question. "Is this legal in Indiana" is a retrieval task.
- Until that check has run, label the point in the output as an unverified local-law assumption and name the jurisdiction. Never reason past it silently.

Cost routing (see token-discipline for the full model ladder):
- Mechanical, fully-specified work goes to the runner (Haiku). Routine production and structured judgment (builder, researcher, reviewer, council advisors) run on the mid tier (Sonnet), pinned in their definitions. Deep planning, coordination, and final verification (planner, orchestrator, verifier) stay on the strong model.
- Cap runner retries at two; on the second failure, escalate to a strong model instead of looping.
- Never run an unattended loop without an iteration cap and stop criteria.
