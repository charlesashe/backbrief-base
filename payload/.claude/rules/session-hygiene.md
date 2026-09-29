# Session Hygiene

Chats degrade as they grow. The project's memory lives in files, not in the chat (context-first, decision-log, handoff-checklist). These habits keep it that way:

- End every work session with /handoff. Start every new chat with /pickup.
- Good breakpoints for a fresh chat: after an approval decision, after a build or major unit completes, when switching to an unrelated goal, or when a long chat starts responding slowly or repeating itself.
- At a phase boundary, the orchestrator ends its run by suggesting: "Good breakpoint. Run /handoff, then continue in a fresh chat with /pickup."
- A handoff brief must stand alone. If continuing from it requires remembering the previous chat, the brief is incomplete.
- Token hygiene (token-discipline rule): a long thread re-reads its own history on every turn. /clear between unrelated tasks, /compact only when mid-task context must survive, and never one thread for days: one per work session or sprint phase.

## Get ahead of the compaction wall (do not wait for it)

As a chat grows, the tool eventually auto-compacts: it summarizes older history to make room, and that summary silently drops detail the work may depend on. Treat auto-compaction as a failure mode to avoid, not a safety net to lean on.

- Act before the wall, not at it. When context is getting full (the harness signals it filling, or you are deep into a long session), proactively run /handoff and continue in a fresh chat with /pickup. Do not wait for replies to slow down, repeat, or for the tool to compact on its own. By the time you notice degradation, detail is already lost.
- A proactive handoff is cheap and lossless: state lives in files, so a fresh chat with /pickup loses nothing. An auto-compaction is lossy and silent. Always prefer the handoff.
- The orchestrator watches for this. When a session runs long or nears compaction, it stops at the next clean breakpoint and says: "Context is filling. Good moment to /handoff and continue fresh with /pickup," instead of pushing on into a compaction.
