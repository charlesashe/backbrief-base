# Decision Log

.claude/memory/decisions.md is the human-readable record of major choices.

Log an entry when you: complete a significant unit, adopt or retire a workflow/tool/agent, or discover a constraint that should influence future decisions.

Format: date (YYYY-MM-DD), the decision in one sentence, optional 2-3 rationale bullets.

Guardrails: no transient notes, only choices that change how the project should behave. When later work contradicts a logged decision, add a new entry that supersedes it.

Multi-writer projects: if this log has more than one regular writer (the team convention file `team/decision-log-team-convention.md` exists in the project, or entries already carry author tags), every entry carries an author tag and a `git fetch`/pull precedes writing, so two sessions cannot write past each other unseen. The full procedure - conflict handling, ordering, contradiction entries - lives in the convention file.

Integrity: the log records decisions at the time they are made, by the person who made them. Never backdate, pre-record, or fabricate an entry - and never offer wording that would. Do not offer to perform a refused action conditionally: "I can write it if you confirm" is performing the first half of the action, and a refusal is complete in itself. When the owner reports a decision made earlier, record it under today's date with the fact stated plainly: "approved verbally on <date>, logged retroactively." A GO is recorded only by the /approve flow with the owner present.
