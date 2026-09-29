# Backbrief

Grade the plan before you build it.

## What this is

Backbrief is the base of a line of products. The others are sold separately.

It is for a person about to spend money, time or reputation on a business idea, a plan, or a video pitching one. It gives you:

- A council of advisors and a CEO loop that stress-test a plan against a public six-dimension rubric.
- A quick pass for a raw idea.
- A grader for a video that pitches a money-making method.
- A picker for someone with no idea yet.

Two honesty lines. The grade is a stress-test. It does not predict results or certify a plan. Backbrief produces analysis, not advice, and never tells you to buy what a video sells.

## What you need

- Claude Code, installed and signed in. It runs in a terminal or in the desktop app.
- A project folder.

You need no other accounts and no keys. Backbrief runs on your own Claude Code access, whatever plan or billing it uses. It has no server and collects nothing.

Grading a video from a link or file can use free local tools (`yt-dlp`, `ffmpeg`). Claude asks before it installs any. A pasted transcript needs none.

## Install (Claude does it, about two minutes)

1. Unzip the download.
2. Open Claude Code in the unzipped folder.
3. Type: `read the README.md in this folder and install this for me`

Claude asks for your project folder and whether Backbrief goes in every project or only that one, copies the pieces, runs `/verify-install`, and offers `/setup`.

If that is unclear, paste this instead:

> Install Backbrief from this folder. Copy the contents of `kit/.claude/` into my global `~/.claude/` (or my project's `.claude/` if I say per project). Then copy the contents of `kit/scaffold/` into my project root without overwriting any existing file. Ask me for my project folder first. When done, run `/verify-install` by file path, show me the result, and offer `/setup`.

Already have your own Claude Code setup? Say so, and Claude merges without overwriting anything. `kit/INTEGRATION.md` covers each decision.

Upgrading from Backbrief Business OS or the free Backbrief Kit? Say "this is an upgrade from an earlier Backbrief product." The plain copy skips same-name files and would leave you on the old version. Case A3 in `kit/INTEGRATION.md` lists what is replaced, added and left in place.

## Install by hand

Two copies: the team (`kit/.claude/`) and the scaffold (`kit/scaffold/`). Run them from the unzipped folder. Neither overwrites a file you already have.

Team, global or per project (pick one):

```bash
# macOS / Linux
mkdir -p ~/.claude
cp -Rn kit/.claude/. ~/.claude/
# or per project
mkdir -p /path/to/your-project/.claude
cp -Rn kit/.claude/. /path/to/your-project/.claude/
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force "$HOME\.claude" | Out-Null
robocopy "kit\.claude" "$HOME\.claude" /E /XC /XN /XO
# or per project
New-Item -ItemType Directory -Force "C:\path\to\your-project\.claude" | Out-Null
robocopy "kit\.claude" "C:\path\to\your-project\.claude" /E /XC /XN /XO
```

Scaffold, into the project root, even if the team is global:

```bash
cp -Rn kit/scaffold/. /path/to/your-project/
```

```powershell
robocopy "kit\scaffold" "C:\path\to\your-project" /E /XC /XN /XO
```

Robocopy prints a summary table. That is normal.

## What's in the box

`kit/.claude/` is the team: agents, commands, rules and skills. Its `CLAUDE.md` holds the roster. `kit/scaffold/` holds the folders and templates the team works in. Opt-in layers sit beside them: `kit/enforcement/` adds permission rules that stop outward shell commands, `kit/memory-layer/` recalls your latest handoff at session start, and `kit/status-layer/` writes a small status file that `/bb-status` reads back. The installer asks about each one. On a fresh install, enforcement is recommended and goes on unless you say no; the other two stay off unless you say yes. `kit/INTEGRATION.md` merges Backbrief into an existing setup. `LICENSE.md` holds the terms.

## First run

1. Run `/verify-install`. It reports plain pass or fail.
2. Run `/setup`. A short interview writes your context files.
3. Run `/next`. It says where the project stands and offers the next step.

Lost? Type `/bb`.

To grade a video, run `/grade-video` with a link or a local file. Before any fetch, it tells you that the platform's terms may restrict automated download, and it offers a local file or a transcript you have the right to use first.

## Try the commands

- `/grade-idea`: stress-test a raw idea against the rubric in one pass. No plan document needed.
- `/grade-video`: paste a link to a video that pitches a business. It extracts and tags every claim and grades the opportunity.
- `/pick-niche`: for someone with no idea yet. It interviews you, then returns three graded candidates, each with a first move for this week.
- `/find-gap`: find market gaps from real complaints, then check whether anyone looks for a fix.
- `/critique`: a skeptical investor and buyer in one pass.
- `/council`: distinct advisors, blind peer review, a chairman, and the clash.

The CEO loop, in order:

- `/intake`: turn a brain dump into a business brief.
- `/business-plan`: turn the brief into a plan with 90-day units.
- `/grade`: advisors score the plan against the rubric, with a capped revise loop.
- `/approve`: your recorded go or no-go. Spending, sending and publishing still stop for you.

## Global vs per project

Install globally to have Backbrief in every project. Install per project to keep it in one project, or to keep that project on one version while others move. Either way, each project needs its own scaffold.

## License, support, updates

`LICENSE.md` holds the terms. For support, write to contact@ashecorp.com from the address you bought with. Updates are free through your download link for as long as the product is offered.
