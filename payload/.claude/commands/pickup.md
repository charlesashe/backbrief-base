---
description: Pick up where the last session left off. Reads the project's memory files, says where things stand, names the next action, then waits.
---

Run PICKUP as the first command in a new chat on an existing project.

**Why this command is not called `/resume`.** Claude Code ships a built-in `/resume` that opens a
session picker, and the built-in wins the name. A command file called `resume.md` is never reached
by typing `/resume`, so this command is called `/pickup` instead. Nothing about what it does
changed with the name.

1. Read, in order: the root `CLAUDE.md`; `context/strategy/current-state.md` and
   `current-priorities.md`; the last 5 entries of `.claude/memory/decisions.md`; the most recent
   file in `.claude/memory/handoffs/` (if the folder exists); any plan in `workflows/active/`
   (if it exists).

2. **Read the append-only files by their tail, never whole.** A decision log grows without bound,
   and a plain read returns the TOP of a file. So "the last 5 entries" silently becomes the OLDEST
   five, and the session carries on believing it holds current context. The failure is silent
   rather than loud, which is what makes it worth spending a step on. Read these by target:
   - **Decision log:** list the entry headings and keep the last five
     (`grep -n '^## ' .claude/memory/decisions.md | tail -5`), then read from the first of those
     line numbers to the end of the file. If the project keeps `decisions-archive-*.md` files,
     leave them alone unless a specific question needs them.
   - **Latest handoff:** take the newest file in `.claude/memory/handoffs/` and read that one in
     full. It is written to stand alone and is the highest-value read here.
   - **`workflows/active/`** can hold plans for work that already shipped. Check each plan's own
     status before treating it as current work.

3. Summarize in under 200 words: where the project stands, what changed most recently, and the
   single next action (taken from the latest handoff brief when one exists).

4. Files win over recollection (handoff-checklist rule). If two files disagree, say so plainly and
   ask one question instead of guessing.

5. Do not start work until the owner confirms the next action or redirects.
