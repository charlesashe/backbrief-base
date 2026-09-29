# The memory layer (opt-in)

This folder holds the optional automatic-memory layer for Backbrief. It is NOT copied
automatically: the installer asks whether you want it, and merges the hook entry from
`settings-memory-template.json` into your project's `.claude/settings.json` when you accept.
On a setup you already run it stays off unless you say yes.
Your existing settings file is never replaced, the hook entry is appended alongside
whatever else is already in your `hooks` key, and nothing else is touched. Before any write
the installer backs your file up (`settings.json.backbrief-backup-<date>`), re-reads and
parses the result before calling the merge done, and restores the backup if it does not
parse, then proves the install with `/verify-install` rather than assuming it.

## What it does

Without this layer, every new session starts blank: the team only knows where the project
stands once someone runs `/pickup` or reads a file. With it, a small hook fires at the start
of every session and prints a compact digest of this project's own memory, the newest
handoff brief and the tail of the decision log, into the model's context automatically.
The team starts each chat already knowing roughly where things left off. `/pickup` is still
the deliberate, complete read; this is the ambient floor underneath it.

The hook fires on session start, on `/clear`, and after auto-compaction, so the digest also
comes back after context compaction wipes it out, which softens the compaction wall the
session-hygiene rule warns about. It does not fire on `--resume`, on purpose: a resumed
session still has its earlier injection in context, and re-injecting would just spend tokens
on a repeat.

## What it costs

Measured against sixty one real handoff briefs from one working project: the digest form,
which covered fifty nine of them, costs roughly three hundred fifty to five hundred tokens
of context, with a median near four hundred twenty. That range already includes the last
five decision-log headings the hook appends to every injection, which account for about two
hundred twenty five tokens on their own and grow as a decision log accumulates longer
headings.

A brief injected whole (which only happens under the 4,000-byte threshold this layer uses
as its cutoff) costs more: about nine hundred tokens in that sample, and an estimated
thirteen hundred for a brief sitting right at the threshold. Past the threshold the hook
always switches to the digest, the brief's title line and its "Next action" section only,
plus a note pointing at the full file. A brand-new project with no handoff briefs yet costs
nothing at all: the hook has nothing to recall and prints nothing.

These are measured numbers from real briefs, not a hard cap, and they were counted with a
public tokenizer rather than Claude's own, so read them as approximate. The digest has no
internal length cap of its own: a brief whose "Next action" section runs long produces a
correspondingly long digest, and the largest in that sample passed a thousand tokens. The
4,000-byte threshold bounds the whole-file path, not the digest.

## Boundaries

- **Per-project only**, even on a global team install. The memory being recalled is this
  project's own `.claude/memory/`, so the hook lives in this project's settings, not in
  `~/.claude/`.
- **Fail-silent, always.** A missing memory folder, no handoff briefs yet, a missing
  decision log, or any internal error all resolve the same way: the hook prints nothing and
  exits clean. You will never see a hook-error notice from this layer, and a brand-new
  project experiences nothing at all until its first `/handoff`.
- **A moved project breaks the hook silently.** The Windows form writes an absolute path to
  this project at install time (needed so the same command works whichever shell ends up
  running it). Move or rename the project folder afterward and that path stops resolving -
  the hook simply prints nothing again, same as any other failure. `/verify-install` catches
  this: it checks that the hook entry exists and that the script it points at is actually
  there, and separately checks that the current session actually saw the recall marker. When
  those two disagree, that mismatch is the signal something moved.
- **No new runtime dependency.** The layer ships a POSIX `sh` script and a PowerShell script.
  Whichever shell your hooks already run under, one of the two is already there.

## Removal in one edit

Delete the `SessionStart` hook entry that runs `backbrief-memory-recall` from your
`.claude/settings.json` (it matches this folder's `settings-memory-template.json`), or ask
Claude to do it. You can also set `disableAllHooks` to silence it temporarily without
removing anything. Nothing else in your setup depends on it.
