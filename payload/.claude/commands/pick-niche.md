---
description: For someone with no business idea yet. Interviews you for skills, hours, money and limits, scans for gaps with /find-gap, and returns three candidates graded on the public six-dimension rubric, each with a first move for this week.
---

Run NICHE PICKER. Load `.claude/skills/niche-picker/SKILL.md` first and follow it in order, no step skipped. The skill holds the procedure; this command starts it.

If the invocation carries text about the operator (skills, hours, money, limits), treat it as the first answers, write it to the capture file, and interview only for the fields it leaves empty. If it carries nothing, open the interview with the first field, hard constraints, and ask one question per turn.

The scan step calls `/find-gap`, and each candidate is graded with the `/grade-idea` procedure. Both commands ship in this install; the researcher and advisor agents they dispatch arrive with the assembled base, and the skill says what to do when they are absent.

Bans, all absolute: never pick a candidate for the operator; never recommend buying, joining or spending on anything; never invent a number, a quote, a URL or a demand signal; never send or contact anyone. The run ends with the skill's closing lines, once.

Obey the constraints rule: make claims measurable; mark every unverified assumption as one, including anything about what is legal or licensed in a named place.
