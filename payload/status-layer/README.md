# The status layer (opt-in)

This folder holds the optional status contract for Backbrief. It is NOT copied
automatically: the installer asks whether you want it, copies the hook scripts into your
project's `.claude/hooks/`, and merges the hook entries from `settings-status-template.json`
into your project's `.claude/settings.json` when you accept. On a setup you already run it
stays off unless you say yes. The same merge guards as the memory layer apply: your settings
file is backed up first, the merged result is re-read and parsed before the install is called
done, and the backup is restored if it does not parse.

## What it does

A small hook watches for the moment you launch a Backbrief command (`/intake`,
`/business-plan`, `/grade`, `/approve`, `/next`, and the rest) and writes a deterministic
status record to `.claude/memory/backbrief-status.json`, with an append-only event log
beside it at `.claude/memory/backbrief-events.jsonl`. The `/bb-status` command reads that file
back and tells you where things stand.

The point of a hook-written file is that it is machine-written state, not model prose. A
session describing its own progress can be wrong in ways it cannot see; a hook fires
deterministically whether or not the session remembered. The record carries: the operation
last launched, its phase, the gate that applies to it, whether an owner approval is required,
when it started, when the file was last touched, and which session wrote it.

Both files live in `.claude/memory/` on purpose: that folder sits under the payload's
never-overwrite guarantee, beside the decision log the gates already read, so no product
update ever touches your status history.

## What it does NOT record, stated plainly

- **Completion.** A hook can observe that an operation was launched and that turns keep
  ending; it cannot observe that the operation succeeded or failed. `exit_status` reads
  `"unknown"` always, by design. The ground truth for "did it finish" is the decision log
  and the files the operation was supposed to produce - `/bb-status` points there rather than
  guessing.
- **Anything on a surface where hooks do not fire.** A surface that loads no settings file
  (Claude Cowork today) never runs this hook, so the status file there is stale or absent,
  not wrong. `/bb-status` opens with the honesty line for exactly this case: it names the last
  writer and time, or says plainly that there is no status file. Treat a `running` phase
  older than the last event as `unknown`, never as still running.

## What it costs

Nothing visible at session time. The hook prints nothing to your context (a status hook that
spent tokens would be paying for its own bookkeeping), writes a file only when a tracked
command is launched or a turn ends, and exits silently on everything else. The event log
grows by one short line per tracked launch and, once a status record exists, per turn end
(before the first tracked launch, turn ends write nothing); it is plain JSONL and safe to
truncate or delete whenever you like - the hook recreates it on the next event.

## Boundaries

- **Per-project only**, even on a global team install. The state being recorded is this
  project's own, so the hook lives in this project's settings, not in `~/.claude/`.
- **Fail-silent, always.** A missing memory folder, unparseable input, or any internal error
  resolves the same way: the hook writes nothing and exits clean. The scripts themselves
  never error and never print.
- **A moved project breaks the Windows hook.** The Windows form writes an absolute path to
  this project at install time; if the project is later moved or renamed, the shell can no
  longer find the script at all - that failure happens before the script's own fail-silence
  exists to swallow it, so whether anything is shown depends on Claude Code, not this layer.
  Either way no status is written, and `/bb-status` reporting a stale `updated_at` is what
  surfaces it.
- **Never hand-edit `backbrief-status.json`.** The contract's value is that only hooks write
  it. If it is wrong, delete it; the next tracked command rewrites it.

## Removing it

Delete the two hook entries (`UserPromptSubmit` and `Stop`, the ones naming
`backbrief-status`) from your project's `.claude/settings.json`, and delete
`.claude/hooks/backbrief-status.sh` and `.claude/hooks/backbrief-status.ps1`. The status and
events files under `.claude/memory/` are yours to keep or delete; nothing reads them but
`/bb-status`.
