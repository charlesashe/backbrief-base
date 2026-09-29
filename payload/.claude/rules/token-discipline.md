# Token Discipline

Tokens are the kit's running cost. These habits keep it low without lowering quality. They apply to every agent and every command.

## Model ladder

Match the model to the work, not the work to one big model:

- **Cheap (Haiku)**: mechanical, verifiable work with explicit acceptance criteria: the runner.
- **Mid (Sonnet)**: routine production and structured judgment: builder, researcher, reviewer, and the five council advisors. This is the default working tier.
- **Strong (the session's top model)**: deep planning, coordination, and final verification: orchestrator, planner, verifier, and the chairman synthesis in /council. Reserve it for the passes where being wrong is expensive.

Agent definitions pin their tier in frontmatter (`model:`); the strong-tier agents (orchestrator, planner, verifier) pin `inherit`, which takes the session's own model, so the judgment tier always runs on the model you chose to run sessions with. Do not override an agent to a stronger model for routine work; do escalate a failed unit to the strong tier rather than looping a cheap model (agent-routing rule).

## Plan once, execute cheap

The expensive pass is planning. Run it once, on the strong model, and write the result down: a compact plan in workflows/active/ with units, owners, and acceptance criteria. Execution agents then receive ONE unit plus its criteria and the few files it names: never the whole plan history, never the chat. If an executor needs more context than its unit provides, that is a planning defect: fix the unit, do not widen the dispatch.

## Small dispatches, small returns

- A dispatch names the specific files and sections the agent needs (paths, not "look around the repo"). Point at `verifyUser in auth.js`, not at auth.js, and never at the codebase.
- Every agent returns its artifact plus a summary within its stated output budget (see each agent's guardrails). No transcripts, no restating inputs back, no essays around a table.
- State lives in files, not in chat: the plan doc, current-state.md, the decision log. An agent that needs history reads those files: nobody re-reads or re-sends conversation history.

## Keep the index small

The root CLAUDE.md is an index, not a spec: what exists and where it lives, in a couple of thousand tokens at most. Detail goes in separate files that agents read only when their unit needs them. If CLAUDE.md is growing, move content out, not in.

## Fresh chats are cheaper chats

A long thread re-reads its own history on every turn. Per the session-hygiene rule: /handoff at the end of a session, /clear (or a fresh chat) between tasks, /pickup to start the next one from files. One thread per work session or sprint phase: never one thread for days.
