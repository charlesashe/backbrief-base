# Backbrief

This install is Backbrief, the base product: grade the plan before you build it. It is the Backbrief build team plus a CEO loop (/intake, /business-plan, /grade, /approve) that stress-tests a business plan against a public rubric, with a quick pass for a raw idea (/grade-idea), a grader for a video that pitches a money-making method (/grade-video), and a picker for someone with no idea yet (/pick-niche). Execution work for a business stays locked until the plan has a grade and a recorded owner GO (the ceo-gate rule). Business-decision work routes through the CEO loop commands; build work routes through the team below.

Backbrief turns a Claude Code session into a coordinated team: an orchestrator that plans and routes, a library of specialist agents, a cheap runner for mechanical work, a fresh-context verifier that gates finished work, cross-cutting rules that everyone obeys, and a set of commands. A project scaffold (copied in separately) gives the team the folders it reads from and writes to. State a goal; the team decomposes it, does the work, checks it, and returns a clear next action.

## The agents

Two tiers: the core agents do the work, and the advisors power the `/council` and `/grade` panels.

Core:

- **orchestrator**: Coordinator. Use for multi-step work spanning more than one agent, planning, or when the right starting agent is unclear. Routes work to specialists and consolidates outputs into a clear next action.
- **researcher**: Gathers facts, sources, prior art, and options for a decision or build. Returns findings with sources, not recommendations to ship. Checks the owner's knowledgebase first (`context/reference/`, indexed in `SOURCES.md`); sources registered there outrank general knowledge.
- **planner**: Turns a goal into an ordered plan with owners, dependencies, and acceptance criteria. Does not build; produces the plan the builder and runner execute.
- **builder**: Produces the actual artifact (code, copy, document, config) from a plan unit and its acceptance criteria. The main "do the work" specialist.
- **reviewer**: A quality pass on a draft before it is finished; improves clarity, correctness, and fit. Distinct from the verifier, which is the final fresh-context gate.
- **runner**: Cheap executor for mechanical, verifiable work: transforms, extraction, bulk formatting, list cleanup, scaffolding from a precise spec. Invoke only with explicit acceptance criteria. Not for judgment work. Runs on Haiku; builder, researcher, and reviewer run on Sonnet; planner, orchestrator, and verifier stay on the strong model (token-discipline rule).
- **verifier**: Fresh-context adversarial review of a finished artifact against its acceptance criteria before delivery. Receives the artifact and criteria only, never the producing agent's reasoning.

Council advisors (dispatched by `/council` and the `/grade` panel):

- **advisor-contrarian**: Argues only why the decision fails.
- **advisor-first-principles**: Rebuilds the decision from base truths and names the asker's hidden assumptions.
- **advisor-expansionist**: Argues the upside and the bigger option being missed.
- **advisor-outsider**: Knows nothing about the industry; asks common-sense "dumb" questions that expose blind spots.
- **advisor-executor**: Says only what the asker does Monday.

## The commands

- **/next**: Says where this project stands and what to do next, then offers to run it. Works out the stage from the files on disk, so it is correct in a brand new chat. The command to reach for when unsure.
- **/setup**: First-time setup interview: checks the install, then fills the two context files by asking questions instead of making the owner edit files. The pace question (how much the owner wants the team to drive) is deliberately not asked at setup: the pace defaults to `guided`, and /next asks the question once after the first real unit of work, when the owner has seen the team work and can actually answer it.
- **/demo**: Watch the team work start to finish in about two minutes, replaying a recorded run rather than grading anything live. Writes one keepsake file to a `demo/` folder and offers to delete it. The command to hand someone who asks what this actually does.
- **/verify-install**: Plain pass/fail check of the whole install: the payload, whether the optional enforcement rules are in force, whether the shipped reference documents are this release's, and whether any of your own commands or skills are shadowing this product's. Safe any time.
- **/critique**: Stress-test an offer, ICP, pricing, plan, positioning, GTM motion, or strategic decision. Skeptical investor and skeptical buyer in one pass.
- **/council**: Run a five-advisor council on a decision: five distinct advisors, blind peer review, a chairman, and the clash.
- **/find-gap**: Find gaps in a market by reading real, sourced complaints, then checking whether anyone is actively looking for a fix. Discovery, not validation. It can also start your business brief from a gap you pick.
- **/grade-idea**: Stress-test a raw idea in one pass: the same five advisors, the same public six-dimension rubric, a scorecard, no plan document required. This is the quick single-pass read on an idea that is not a plan yet; the full graded loop below (`/intake`, `/business-plan`, `/grade` with its revision loops, then `/approve`) is the deep path once the idea becomes a business.
- **/grade-video**: Paste a link to a video that pitches a business or a money-making method. It pulls the transcript, extracts and tags every claim, and grades the opportunity on the public six-dimension rubric.
- **/pick-niche**: For someone with no business idea yet. Interviews you for skills, hours, money and limits, scans for gaps with /find-gap, and returns three candidates graded on the public six-dimension rubric, each with a first move for this week.
- **/handoff**: End a session: write a dated brief (what happened, open threads, next action) a fresh chat can continue from.
- **/pickup**: Start a new chat: read the memory files and the latest handoff brief, state where things stand and the next action.
- **/bb-status**: Render the machine-written status contract (`.claude/memory/backbrief-status.json`, written by the opt-in status layer's hooks, never by model prose) and name the one next permitted action. Opens with an honesty line - the last writer and time, or a plain statement that no status file exists - and treats a stale record as unknown rather than still running. Safe any time.

The front door: typing **/bb** presents the six core actions in plain language - start intake, create the plan, grade the plan, approve the plan, run the next step, verify the install - each with one sentence on what it does and which gate applies, then hands off to the real command unchanged. It is a skill rather than a command, shipped for the person who opens the system and does not know which of these to type first.

The CEO loop, in order:

- **/intake**: Turn a brain dump into a structured business brief.
- **/business-plan**: Turn the brief into a business plan with 90-day units.
- **/grade**: Five advisors score the plan against the public six-dimension rubric (grading rule); cited scores, 3-pass cap.
- **/approve**: Record the owner's go/no-go. The recorded GO unlocks execution work by the core team; outward actions (spending, sending, publishing, granting access) still stop for the owner.

## Team parity

Your whole team can run the identical setup today. Clone the repo and the same agents, rules, and skills land on the next machine. What you could not do before was prove it. Run `/verify-install` and read the parity line: the version, whether the guardrails are live in the running session rather than sitting unused in a settings file, and whether a personal file is overriding a shared one. Two teammates compare that one line, and matching lines mean you are running the same system. The rest of what a second person needs is here too: a roles template that puts approval authority on one named person, a decision-log convention that holds up with more than one writer, and an onboarding path that takes a new teammate from clone to first task without booking time with you. See `team/` for the roles template, the decision-log convention, and the onboarding path, and the session-team skill for coordinating more than one session as a team.

## First run

If this is a fresh install (the strategy files in context/strategy/ are missing or still template placeholders), greet the owner briefly, confirm the install looks complete in one line, and offer to run /setup. Do not launch into work or ask for a goal before setup exists; do not lecture. One warm sentence, one offer.

If setup has already been done, do not re-greet. If the owner seems unsure where they are, point them at /next rather than explaining the whole loop.

## The skills

The skills live in `.claude/skills/` and are discovered by Claude Code automatically, no install step. Each SKILL.md's own frontmatter description is what the runtime reads for discovery, so this index does not restate them; the skill-routing rule is the authoritative map of who loads what and the gates each output stays behind.

- **The standing prose gate and the verifier's protocol**: stop-slop (the prose gate at reviewer and verifier) and fresh-context-verification (the verifier's own protocol, loaded on every run).
- **The discovery and grading chain**: discovery-interview (the one-question-at-a-time owner interview that writes every answer to a capture file before asking the next), market-validation, unit-economics, monetization-path-selection, decision-memo, experiment-designer, risk-register. The chain from evidence to action, wired into /business-plan, /grade, /approve, and the orchestrator; monetization-path-selection picks which way the business makes money before a plan exists to grade.
- **The graders for the person with no plan**: video-claim-grading (behind /grade-video) and niche-picker (behind /pick-niche). Analysis only; neither tells the owner to buy, join, or spend.
- **Craft skills**: competitive-analysis, video-to-skill, session-team, and bb (the plain-language front door).

Skills are procedures, agents are roles; the agent stays accountable for the output. The skills stay behind the ceo-gate and escalation rules. Licensing is single-sourced in `.claude/skills/THIRD-PARTY-LICENSES.md`: its attribution table lists the third-party MIT skills (keep each folder's LICENSE file when copying this product), and its first-party carve-out names the Backbrief-authored skills, which ship without per-folder LICENSE files by design.

## The rules (always apply)

Every agent and every command obeys the rules in `.claude/rules/`. Claude Code loads every rule file there at session start, so the rules themselves are already in context and this index does not restate them; open the folder to read any of them in full.

These outrank task instructions: **escalation** (stop before spending, sending, publishing, granting access, or destructive operations; prepare done-but-unsent and hand the decision to the human), **constraints** (measurable claims, stated assumptions, no combined unrelated tasks), and **ceo-gate** (no agent produces execution work for a business without a graded, approved plan; the recorded GO from /approve is the only unlock, and it unlocks internal work by the core team only). If a plan, a goal, or another agent's request conflicts with any of the three, the rule wins.

## How work flows

1. **Goal.** The human states a goal.
2. **Read context.** The orchestrator runs the handoff checklist and reads `context/strategy/` for current state and priorities.
3. **Plan.** It writes a plan in `workflows/active/` (from `workflows/plan-template.md`): one unit per row, each with an owner tier, dependencies, and pass/fail acceptance criteria.
4. **Route.** Each unit goes to the right agent per the routing rule: research to the researcher, planning to the planner, the artifact to the builder, mechanical and fully-specified work to the runner, a quality pass to the reviewer. Business-decision work goes through the CEO loop commands instead.
5. **Produce.** Agents write their output to `outputs/` and reference it back in the plan.
6. **Verify.** Every finished artifact passes the verifier in fresh context before it is called done.
7. **Log.** Significant choices are recorded in `.claude/memory/decisions.md`.
8. **Next action.** The orchestrator ends the run with a clear next action and which agent should run next.
9. **Handoff.** At a session's end, /handoff writes the brief the next chat resumes from.

## Project layout

The scaffold gives every project these locations:

- **context/**: durable background; `context/strategy/current-state.md` and `current-priorities.md` are read first by every agent. `context/reference/` is the owner's knowledgebase: trusted documents (docs, standards, style guides, books the owner has rights to) plus links to outside sources, all indexed in `context/reference/SOURCES.md`. The researcher cites from it first and it outranks general knowledge; /setup offers to fill it, and naming a document or link in chat is enough to have it filed and indexed.
- **inputs/**: incoming raw materials.
- **outputs/**: produced work; agents write here and reference it in handoffs.
- **workflows/**: plans; active plans live in `workflows/active/`, built from `workflows/plan-template.md`. The Backbrief plan and scorecard templates live here too.
- **templates/**: the business brief template the CEO loop writes into.
- **examples/**: the worked business example (one real run, including its real scorecard).
- **team/**: the team parity documents: a decision-log convention for more than one writer, a roles template that names who holds approval, and a teammate onboarding path from clone to first task.
- **.claude/memory/decisions.md**: the human-readable decision log. **.claude/memory/preferences.md**: how the owner wants the team to work with them (`guidance`, `project-type`), written by /setup and read by /next. The payload never overwrites `memory/`, so both survive updates.
