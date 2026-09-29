---
description: End a work session deliberately. Capture what happened, decisions, open threads, and the exact next action into a dated handoff brief a fresh chat can continue from.
---

Run HANDOFF at the end of a work session, before the chat is closed.

1. Gather from this session: what was completed, decisions made, open threads, the single most important next action, and the files touched.
2. Confirm the decision log is current: any significant choice made this session should already be in .claude/memory/decisions.md (decision-log rule). Add what is missing before writing the brief.
3. Write .claude/memory/handoffs/YYYY-MM-DD-HHMM-<short-slug>.md (create the folder if missing) with exactly these sections: What happened; Decisions recorded; Open threads; Next action (one, concrete, starts with a verb); Files touched. **The HHMM is load-bearing.** More than one session a day is normal, and without it same-day briefs sort alphabetically by slug, so the next /pickup can read the wrong brief as the newest and act on a stale next action.
4. If the project's overall picture changed, refresh context/strategy/current-state.md (one-paragraph snapshot).
5. The brief must stand alone: a new chat with zero context should be able to continue from it. No "as discussed above."
6. End your reply with exactly: "Handoff saved. Start your next chat with /pickup."

Plain-language note: with a non-technical owner, call this "saving your progress note." No jargon.
