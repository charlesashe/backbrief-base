# The enforcement layer (opt-in)

This folder holds the optional enforcement profile for Backbrief. It is NOT
copied automatically: the installer asks whether you want it, and merges
`settings-enforcement.json` into your project's `.claude/settings.json` when you accept.
On a setup you already run it stays off unless you say yes; on a fresh install it is
recommended, and goes on if you state no preference.
Your existing settings file is never replaced: our entries are appended into its
permission arrays and nothing else is touched. Before any write the installer backs
your file up (`settings.json.backbrief-backup-<date>`), re-reads and parses the result
before calling the merge done, and restores the backup if it does not parse, then
proves the install with `/verify-install`'s self-test rather than assuming it.

## What it does

The escalation rule says outward actions (sending, publishing, deploying, spending)
stop for you. Without this profile, that is an instruction the team follows. With it,
Claude Code's own permission engine enforces the stop on the command path: when any
agent tries a matching shell command, the engine interrupts and asks you first, even if
the model forgot the rule. In non-interactive (headless) runs there is nobody to ask, so
a matching command is simply blocked: fail closed.

A useful way to hold the whole layer in your head is three buckets. **Always do** -
everyday work (file edits, builds, `git commit`): no rules match it and nothing changes.
**Ask first** - outward moves (push, deploy, web requests, mail, payments) and edits to
the files that govern the team (the settings files, the rules, the agent definitions,
the decision log): the engine interrupts and hands you the
decision. Nearly this whole profile lives here. **Never do** - refused outright by
`deny` rules: the profile deliberately ships only the verification canaries in this
bucket, because absolute lines are yours to draw, not ours - when you have an action
that must never happen even with you in the room, a `deny` rule on it is how you say so.

These rules apply in the default permission mode and inside every subagent. The mode
story has two halves, both measured rather than assumed, and the split matters:

- **Headless runs (the `-p` path, CI, unattended agents): matching commands fail closed
  in every permission mode, including bypass.** Probed with a control: a command with no
  matching rule executed under the skip-permissions flag while the matching one was
  blocked in the same configuration.
- **Interactive bypass-mode sessions: ask prompts are off, and this profile is almost
  entirely `ask` rules, so the outward stops are off with them.** That mode is the
  owner's own switch, not something an agent can flip. The deny canary still answers in
  that mode, so a LIVE canary alone is not proof the outward asks are active - which is
  exactly why the profile also ships `backbrief-enforcement-askcanary`, an `ask` rule on
  a command that exists nowhere: `/verify-install` probes it and reports the ask layer
  separately (active, or inert in this session), so the verifier cannot overstate what
  is protecting you.

## Two shells, two rule namespaces

Claude Code runs shell commands through one of two tools, and each has its own
permission namespace: `Bash(...)` rules match only commands sent through the Bash tool,
and `PowerShell(...)` rules match only commands sent through the PowerShell tool. A rule
in one namespace does nothing for the other. Which tool a session uses depends on the
machine: on Windows without Git Bash, PowerShell is the shell; on Mac and Linux it is
Bash; Windows machines with Git Bash may use either.

So every outward pattern in this profile ships twice (once per namespace) and the
whole profile protects you whichever shell your sessions run. Do not trim one side
because your machine uses the other today: the point of the pair is that it keeps
working when that changes.

Two namespace-specific notes:

- `Invoke-WebRequest` and `Invoke-RestMethod` are PowerShell cmdlets, so their rules
  exist only on the PowerShell side: a cmdlet cannot arrive through the Bash tool.
  PowerShell rules match aliases automatically, so the `Invoke-WebRequest` rule also
  covers `iwr` (and, on Windows PowerShell 5.1, the `curl`/`wget` alias spellings).
  Explicit `curl` and `wget` rules ship anyway, because PowerShell 7 drops those
  aliases and runs the real binaries.
- The two namespaces pattern-match slightly differently. The rule forms in this file
  are each empirically tested in their own namespace; when adding your own rules,
  mirror the forms you see here rather than assuming one namespace's shape works in
  the other.

## What is in the profile

Mostly `ask` rules. A few guard the layer itself: the settings files, the agent
definitions, and the rules (see the next section); the rest cover outward shell commands in both shell namespaces: every pattern
ships once for `Bash(...)` and once for `PowerShell(...)`, because a rule in one namespace
does nothing for the other: in six groups, each in bare form AND runner-prefixed forms AND the alternate
package managers, because Claude Code does not unwrap runners like `npx` when matching
patterns. Each runner-prefixed tool carries three rule forms per namespace, all
empirically required (a word-boundary pattern does not match flag variants such as
`npx -y vercel`, and a middle wildcard needs at least one word):

- publish/deploy: `git push` (including `git -C <path> push`), `vercel`, `netlify`,
  `wrangler`, `gh`, `npm/pnpm/yarn/bun publish`
- network send: `curl`, `wget`, `Invoke-WebRequest`/`iwr`, `Invoke-RestMethod`/`irm`,
  `mail`, `sendmail`, `ssh`, `scp`, `rsync`, `stripe`
- run-anything runners: `pnpm dlx` and `yarn dlx` ask on ANY use, not per-tool: they
  exist to fetch and run arbitrary packages, they are rare in normal work, and a
  per-tool list would miss whatever tool ships next. (`npx`/`bunx` are per-tool
  because they are common in everyday scaffolding; asking on every `npx` would teach
  you to click through the prompt, which is worse than narrower coverage.)
- execution wrappers that could carry any of the above: `docker exec`, `direnv exec`,
  `devbox run`, `mise exec`
- shell-in-shell forms that carry a whole command as a string argument, where the
  patterns cannot see inside: `bash/sh/zsh -c` (including the combined `-lc` spelling
  and flag-inserted forms like `sh -eu -c`), `eval` and `Invoke-Expression`/`iex`,
  `pwsh`/`powershell` with `-Command`, `-c`, or `-EncodedCommand` (a base64 command
  payload): each also covered with flags in between, because
  `pwsh -NoProfile -Command` is the canonical documented spelling, and `cmd /c` /
  `cmd /k` in both cases on the Bash side (`/C`, `/K`); the PowerShell namespace
  matches case-insensitively, verified by probe. These ask on the wrapper itself.
  Running a script file (`pwsh script.ps1`) is deliberately not matched: the rules
  target the shape that smuggles a command as a string, not the interpreter.
- wrapper commands the engine cannot see through: `xargs` with flags (bare `xargs cmd`
  is unwrapped and the inner command's rule applies, but `xargs -n1 cmd` is matched as
  an xargs command), `watch`, `setsid`, `ionice`, `flock`, and `find` with `-exec` or
  `-delete`.

## The rules also guard themselves, and the decision log

Three `ask` rules cover the settings files where these rules live: this project's
`.claude/settings.json` and `.claude/settings.local.json`, and your user-level
`~/.claude/settings.json`.

Two more cover the decision log (`.claude/memory/decisions.md`, and a root `decisions.md`
where a project keeps it there). This reverses an earlier call that left all of
`.claude/memory/` uncovered, and the reversal is measured, not guessed: benchmark runs
found the decision log is where a pressured session records the entry that legitimizes
everything downstream - a standing "anything under $X is pre-approved" waiver, a
governance change framed as an owner decision. The gate cannot see an *offer* (offers are
language; the decision-log rule governs those), but it converts offer-*acceptance* from a
silent write into a loud permission prompt. The trade-off, plainly: a legitimate decision
entry prompts once when written interactively, and in headless runs the write fails
closed - the entry belongs in the session's report instead. Preferences and handoff
briefs stay uncovered; they are written constantly and prompting on them would train you
to click through.

They are here because of how the permission engine loads settings. It registers settings
files when a session starts, but it re-reads a registered file's rules live, so a rule
removed mid-session stops applying immediately, on the very next command. Without these
three, any agent holding file-editing tools could delete the rules above and then take
the outward action itself, in the same session, with nothing to prompt you. That is not
a hypothetical about a badly-behaved model: an agent asked to fix a settings problem, or
one that reasons a prompt is blocking the job it was told to finish, arrives there by
ordinary helpfulness.

They are `ask` rather than a hard block for a reason that is the whole posture of this
product in one line: changing your own settings is legitimate, and you may well want to.
What should never happen silently is the team changing the rules that govern the team.
So it stops and asks you, exactly as the escalation rule says. When you say yes, the
edit goes through.

Three mechanical notes, each verified rather than assumed:

- `Edit(...)` rules cover every file-editing tool, Write included. A `Write(...)` rule
  is not matched by file permission checks at all, so shipping one would look like
  protection and do nothing.
- `Edit(...)` rules govern the file-editing tools only. A shell command that rewrites
  the same file (a `sed`, a Python one-liner, a redirect) is matched by the command
  rules only if it takes one of the enumerated wrapped forms above, and most direct
  file-writing one-liners do not. This has been observed in practice, not just
  reasoned about: a session asked to remove these rules, blocked on the Edit path,
  reached the same file through a shell write. The guard makes the quiet path loud;
  it does not close every path. That is what the escalation rule's own words are for.
- Being `ask` rules, these self-guards share the mode bound above: in
  `bypassPermissions` they are off, along with the rest of the profile.

Plus two probe commands that exist nowhere and never fire in normal work, one per rule
type, each shipped in both shell namespaces. `backbrief-enforcement-canary` (`deny`): a
BLOCKED response proves the profile is loaded and live in the namespace your session
actually uses. `backbrief-enforcement-askcanary` (`ask`): proves the ask layer itself is
active in THIS session - it prompts (or fails closed headless) where the layer is on,
and executes harmlessly where an interactive bypass-mode session has turned ask prompts
off, which `/verify-install` reports plainly instead of letting a LIVE deny canary imply
more than it proves.

Your own everyday commands (`git commit`, local builds, file edits, tests) match
nothing here and are untouched.

## What it does not cover

This profile covers **direct and wrapped shell invocations on the command path**: the
enumerated forms above, in both shell namespaces, and nothing else. Coverage is
enumerated, not categorical: a session that reaches an outward outcome through a
command shape the list does not name is governed by the escalation rule, not by the
engine, and benchmark measurement of real sessions shows that happens. It does not
cover script interiors either: an outward call made from inside a script file the
model writes and then runs is not a shell command the patterns can see. Indirection is
unbounded in principle, so the profile does not claim completeness; it names its list
and says plainly where the list stops. The stronger answer for script interiors is
OS-level sandboxing, which Claude Code offers on macOS and Linux only: there is no
Windows equivalent, so no copy anywhere promises it.

It also does not cover MCP server tools: if you have connected a server that can send
(Slack, email, social posting), add one line per server to the `ask` array in your
`.claude/settings.json`, for example:

    "ask": ["mcp__slack__*"]

The escalation rule itself still applies everywhere: this profile is the mechanical
backstop for the shell path, not a replacement for the rule.

## Removing it

Delete the entries this file added from your `.claude/settings.json` (they match this
folder's `settings-enforcement.json` exactly), or ask Claude to do it. Nothing else in
your setup depends on them.
