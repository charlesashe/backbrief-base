# Handoff Checklist

Applies whenever you are continuing previous work, switching agents, or resuming a paused thread: any "continue where we left off" session, before making claims about state or editing files.

Before asserting current state or proposing next steps:

1. Read the project's root CLAUDE.md for the overview and agent routing.
2. Read the .claude/rules/ files relevant to the area you are working on.
3. Read .claude/memory/decisions.md for the last major decisions and open questions.
4. If auto-memory is enabled, review the project memory notes, treating them as secondary to the files.
5. Only then summarize current state and propose next actions.

Guardrails:

- Never rely on recollection alone when claiming project state.
- On any discrepancy between memory and files, files win. Correct the memory afterwards.
- Do not skip this checklist for multi-step tasks or agent handoffs.
