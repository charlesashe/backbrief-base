---
description: CEO intake. Turn a brain dump (text, prompts, files) into a structured business brief the team can plan from.
---

Run INTAKE on whatever the owner provides: freeform text, a conversation, and/or files placed in inputs/.

1. Read everything provided. Read context/strategy/ if it exists (context-first rule).
2. Draft outputs/business-brief.md from templates/business-brief-template.md, filling every section you can from the owner's material. Use the owner's own words where they are clear.
3. Ask ONLY for genuinely missing essentials (constraints rule), in plain language, maximum 5 questions, one batch, presented together with the draft brief. If the owner answers, fold the answers in; if the owner is not available, proceed: sections that remain unknown go under Open unknowns. Never invent numbers or facts.
4. Mark every estimate as an estimate. Do not upgrade the owner's guesses into facts.
5. Finish by showing the owner the brief and one line: "If this reads right, the next step is /business-plan, which turns it into a 90-day plan." Then honor `guidance` in `.claude/memory/preferences.md`: on `manual`, stop there; on `guided`, offer to run /business-plan now and wait for a yes; on `auto-prep`, run /business-plan and say you are doing it. Correcting the brief always comes first if the owner says anything is wrong: the plan is built on it, so a wrong brief is the expensive mistake.

Plain-language note: with a non-technical owner, say "your business brief," not "the intake artifact." No jargon in questions.
