# <PROJECT NAME>

<One paragraph: what this project is and what "done" looks like. The orchestrator reads this first.>

This project runs on Backbrief. Agents, commands, and rules are installed under .claude/ (globally or here). Durable background lives in context/, incoming materials in inputs/, produced work in outputs/, plans in workflows/active/, and the decision log at .claude/memory/decisions.md.

## How work flows here
- State a goal. The orchestrator reads context/strategy/, writes a plan in workflows/active/, routes each unit to a specialist agent (or the runner for mechanical work), and gates finished work through the verifier before it is called done.
- Significant choices are recorded in .claude/memory/decisions.md.
- Outward or irreversible actions (spending, sending, publishing, deleting) stop for human approval per the escalation rule.
