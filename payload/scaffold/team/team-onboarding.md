# Teammate Onboarding

The setup is the repo. Cloning it is the transfer. Months of teaching an AI assistant how your business works, every convention, every decision, every dead end you already ruled out, live in this project's files rather than in one person's head, and handing a new teammate the repo hands them all of it at once.

That is the whole point of this document: the path from "just joined" to "running the identical setup everyone else on this team runs," with nothing left for the team lead to explain by hand.

## Step 1: Clone the repo

Get the project onto your machine the way your team already shares code or files. If your team lead has not told you how, ask them now. Nothing after this step works without a full, current copy of the project.

## Step 2: Confirm the team is on your machine

If your team commits its `.claude/` folder to the repo (most teams using this capability do, and it is the recommended setup), the clone you just made already contains the whole team: agents, commands, rules, and skills. There is nothing to install. Skip to Step 3.

One licensing note before you go further: this clone is covered by the product's own license file at the download root. Read it before you rely on the clone, and if your team bought the product, ask your team lead how it was licensed for the team.

If your team does not commit `.claude/`, ask your team lead for the install source they used (the product download or the plugin), open Claude Code inside the cloned folder, and say:

> **install this**

The installer carries the instructions Claude reads on open, so it knows what to check for, what to ask you, and what to copy. It will ask where the team should live (this project only, or everywhere on your machine) and whether you want the optional layer that has Claude Code itself pause and ask before any outward action, like publishing or sending. Answer honestly; there is no wrong answer, and it can be changed later.

If the project already shows a completed install (you can see agents and commands in place), skip this step. Installing twice does no harm, but there is nothing to gain from it.

## Step 3: Run the install check

Type:

> **/verify-install**

This runs a plain pass-or-fail check of everything: is the install intact, are the optional guardrails actually running rather than just sitting in a settings file, and is anything on your machine quietly running an older or personal copy instead of the team's shared one. Read the result. If it flags anything, it also tells you the fix, and it will offer to apply that fix for you rather than leaving you to figure it out.

Do not skip this step because the install "looked fine." A copy that looks complete and a copy that actually runs identically to your teammates' are not the same claim, and this is the only step that checks the second one.

## Step 4: Read the two files that tell you where things stand

Before you touch anything, read:

- `context/strategy/current-state.md`
- `context/strategy/current-priorities.md`

These two files are what every agent on the team reads first, before doing any work. They are short by design. Reading them now means you start from the same picture everyone else on the team is working from, instead of guessing at it from old conversations you were never part of.

## Step 5: Read the team roles template

If your team has filled in a roles template, read it next. It tells you who typically drives which kind of work, who runs the check on finished work before it ships, who owns the weekly review of the project's decision log, and who holds final approval on business decisions. That last one is worth reading twice: approval belongs to exactly one person on the team, and it does not transfer to whoever happens to be doing the day-to-day work, including you, once you are up and running.

If no roles template exists yet, say so to your team lead. It takes ten minutes to fill in and it is the reason a new teammate does not have to ask "wait, whose call is this?" partway through their first week.

## Step 6: Your first task

Open a fresh session in the project and type:

> **/pickup**

This reads the project's own memory: the decisions already made, the most recent handoff from whoever worked on it last, and where things currently stand. It will tell you what has happened and what the next action is. Do that next action. You are now running the same setup, from the same starting point, as everyone else on the team.

## What "done" looks like

You have reached a working, parity-checked install when all of the following are true, and none of them required asking your team lead a question this document could have answered:

- [ ] The repo is cloned and up to date.
- [ ] The install check in Step 3 reports a clean pass.
- [ ] You have read both strategy files in Step 4.
- [ ] You know who runs the pre-release check, who owns the weekly review, and who holds approval authority.
- [ ] `/pickup` has told you where the project stands, and you have started on the action it named.

If any of those is not true, that is the gap to close, not a reason to start guessing.
