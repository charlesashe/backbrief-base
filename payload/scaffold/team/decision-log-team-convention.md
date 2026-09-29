# The Decision Log, With More Than One Writer

**Applies to:** any Backbrief project where `.claude/memory/decisions.md` gets written by more than one person, or by one person running more than one concurrent session against the same repo.
**Owner:** whoever is currently working the project. Nobody owns the file; everyone who touches the project writes to it.
**Trigger:** you complete a significant unit, adopt or retire a workflow or tool, or discover a constraint that should change future decisions - the same trigger as the single-writer log, unchanged.
**Last updated:** ship date of this convention.

## The failure this prevents

Two sessions worked the same repo at the same time. One reported an action as blocked and spent the rest of its length working around that. The other completed the same action and pushed. Neither session was wrong about what it saw; neither one checked whether the other had also been busy.

The only reason anyone noticed was that both sessions happened to append to the same decision log file in the same sitting. Git refused to merge two edits to one file without a look, so a person opened it, read both entries, and caught the divergence before a stale status became the record anyone acted on.

Had the two sessions touched different files instead, both edits would have merged cleanly and the stale entry would have stood as fact. The log did not prevent the collision. It made the collision visible, which is the only thing that saved this from becoming a real defect that nobody caught for a proper while.

That is the case for the convention below: not to prevent every collision, since some are unavoidable when more than one hand is on the same file, but to make sure a collision fails loud instead of failing silent.

## Who writes

Anyone working the project writes to `.claude/memory/decisions.md`. No gatekeeper, no review step before an entry lands. This is append-only: nobody edits or removes another person's entry, and nobody edits or removes an entry from another session. Correct a stale entry with a new one that supersedes it, dated, never by rewriting the old line.

## Entry format

Keep the shipped format. Every entry starts with a date, states the decision in one sentence, and may add two or three rationale bullets:

```
2026-08-21: Switched the deploy check from a manual pull to `git fetch` before every status claim.
- Two sessions diverged on the same repo; the stale one wrote a handoff naming finished work as still pending.
- The fix cost one command. The miss cost a wrong handoff and a wasted read.
```

Add one field for a multi-writer project: an author tag on the same line as the date, naming the person or session that wrote the entry.

```
2026-08-21 (author: reviewer-session): Switched the deploy check from a manual pull to `git fetch` before every status claim.
```

Pick any author label that is stable and distinguishes writers from each other: a person's name, a role name, a session name. The requirement is that two different writers never share a label, not that the label follow any particular scheme. Without it, a multi-writer log accumulates entries nobody can trace back to a source, and the first question anyone asks when two entries conflict - "who wrote this, and were they looking at the same state I was?" - has no answer.

## Fetch-first discipline

Before writing an entry, pull. Specifically:

```
git pull --rebase
```

This is not a formality. A decision log entry is a claim about project state at the moment you wrote it. If you write it against a local copy that is behind the remote, the entry can already be wrong the moment it lands - describing a "current" constraint that a different writer already resolved, or proposing a decision that contradicts one already made and pushed five minutes earlier. Pulling first does not guarantee your entry stays correct, but writing without pulling first guarantees you are guessing at your own currency.

If your working copy is a live long-running session rather than a fresh git operation each time, fetch before any turn in which you are about to assert what the project's state is or write a decision-log entry, not once at session start and never again.

## The merge-conflict path

Two writers append to the log inside the same window and one has to rebase onto the other's push. When that happens:

1. **Keep both entries.** Neither writer is wrong for having written theirs. A conflict on this file is not an error to resolve by picking a winner - it is the log doing its job by refusing to let two claims merge invisibly.
2. **Order by timestamp**, not by whichever entry happens to resolve first in the merge tool. The log is a timeline; an entry from 9:57 that lands below one from 10:15 because of merge mechanics reads as confusing at best and misleading at worst.
3. **If the two entries actually contradict each other** - not just two unrelated decisions landing close together, but one saying a thing is blocked and the other saying it shipped - do not silently keep both as if they agree. Add a third entry, dated after both, that names the contradiction and states which one reflects reality. That third entry is what turns a caught collision into a resolved one.
4. **Do not resolve a decision-log conflict by discarding the older entry.** Even a superseded entry is part of the record of what someone believed and when; the record is more useful with the correction visible than with the mistake erased.

## Quality checklist

- [ ] Entry starts with a date.
- [ ] Author field present if this project has more than one regular writer.
- [ ] One sentence states the decision; rationale bullets stay to two or three.
- [ ] You pulled (or fetched, for a live session) before writing.
- [ ] If this entry corrects an earlier one, it says so and points at what it supersedes, rather than editing the old line.

## Troubleshooting

| Problem | Cause | Solution |
|---|---|---|
| Git refuses to merge on `decisions.md` | Two writers appended in the same window | Keep both entries, order by timestamp (see above). This is the log working as designed, not a bug to route around. |
| Two entries describe the same event differently | The writers were looking at different, stale views of project state | Add a dated third entry naming which account is correct and why; leave both originals in place. |
| An entry looks stale within hours of being written | It was written without pulling first | Add a correcting entry rather than editing the stale one; adopt fetch-first discipline going forward. |
| Nobody knows who wrote an old entry | The project skipped the author field | Add author tags going forward; do not attempt to retroactively attribute old unlabeled entries - a guess recorded as fact is worse than an acknowledged gap. |

## Escalation

If the same contradiction keeps recurring between the same two writers or sessions, that is a coordination problem the log cannot fix by itself - it can only surface it. Raise it as a decision of its own: are these two writers duplicating work that should be split, or working from different copies of the project that need to be reconciled first.
