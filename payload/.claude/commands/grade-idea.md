---
description: Stress-test a raw business idea against the public six-dimension rubric. Five advisors, cited scores, no plan document required.
---

Run GRADE-IDEA MODE on the idea the user gave. If the invocation carries no idea text, ask exactly one question and wait: "Describe your business idea in a sentence or two: what it is, who pays, and any numbers you already have." Do not run a multi-question interview. Whatever comes back, thin or rich, is what gets graded.

This command needs nothing but the description in front of you. No plan document, no prior scorecard, no other file in this project.

0. LOCAL LAW CHECK: if the idea turns on what is legal, licensed, required, disclosed, or taxed in a named place, dispatch the researcher on that point before the advisors run, and carry the retrieved answer and its citation into the brief you build in step 1. If the check has not been run, every advisor touching the point labels it an unverified local-law assumption and never scores it as risk coverage (agent-routing rule). A vague idea with no named jurisdiction skips this step; a specific one ("a food truck in Austin") does not.

1. COMPRESS: turn the description into a brief of at most 300 words: the idea, who pays, and any numbers the user already gave. Do not add facts the user did not state. If the description is thin, the brief stays thin. That is the input, not a defect to paper over.

2. FIVE ADVISORS: dispatch five subagents in parallel, one each: advisor-contrarian, advisor-first-principles, advisor-expansionist, advisor-outsider, advisor-executor. Each receives ONLY the brief and the rubric below, nothing else: no chat history, no other file, no prior run. Advisors run on their pinned mid-tier model; the consolidation in step 4 stays here on the strong model.

   Use this dispatch prompt for every advisor, brackets filled. The format instruction is not optional: several advisors' own definitions prefer open-ended output (the outsider, for one, answers in questions), and without it an advisor will return no scores at all.

   > You are grading a raw business idea through your own lens. THE BRIEF: [brief from step 1, including any step-0 local-law finding]. THE RUBRIC: [the six dimensions and scoring discipline below, verbatim]. Output exactly seven lines: one per rubric dimension in order, then the reachability trial line, each formatted "[dimension name]: X.X/10 - [roughly 60 words citing the brief's own words or naming what the brief does not say]". Keep your lens inside the justifications: your questions, your attacks, your Monday steps all live there. Do not switch to your usual open-ended format. Do not add anything before or after the seven lines.

   Rubric, six dimensions, 1-10 each:
   1. Clarity of offer: who pays, for what, stated so a stranger understands it in one sentence.
   2. Market realism: evidence demand exists (named buyers, comparable products, real signals, not "everyone needs this").
   3. Financial viability: the unit economics close using the numbers the user actually gave.
   4. Execution feasibility: for this operator, the time, money, and skills stated in the description, not a hypothetical team.
   5. Risk coverage: the top risks are named, each with a mitigation or an explicit acceptance.
   6. Differentiation: a concrete reason to pick this over the obvious alternative, including doing nothing.

   Trial line, scored beside the rubric and never averaged into the grade:
   7. Reachability (trial): a named, plausible way a stranger first finds this, using only the channels, budget, and audience the user actually stated. No channel stated is a low score, and the justification says so.

   Scoring discipline: every score cites the user's own words. No citation, no score. What the description does not say is scored as a gap and named as a gap in the justification, not invented to fill the space. Tag every number the user supplied as unverified (plausible, unchecked) or vendor claim (the source of the number sells something); nothing in a raw idea description has been independently checked, so nothing gets called verified here. A thin description will not support confident scores on every line, and low scores from missing information are the correct, expected result, not a bug in the run.

3. CONSOLIDATE: average the six rubric dimension scores. Pass line is 8.5. Letter map: 9.0+ is A, 8.5-8.9 is A-, 8.0-8.4 is B+, 7.0-7.9 is B, below 7.0 is C. Reachability is consolidated the same way but reported beside the rubric: it never enters the average, the letter, or the pass line, because the public rubric is six dimensions and this line is a trial. Report divergent advisor scores on a dimension rather than quietly averaging them away. If an advisor returned anything beyond its scored lines, use the scored lines and ignore the extra; if an advisor returned no scores at all, re-dispatch it once with the format instruction repeated, and if it still returns none, say so in the scorecard notes rather than inventing its scores. Identify the lowest-scoring dimension and state plainly what the panel flagged there. Thin ideas often tie several dimensions at the floor: when two or more tie for lowest, name them all on the Lowest line and cover the tie in one sentence instead of picking one arbitrarily.

4. SCORECARD: render the result in the block below, fixed-width so it reads cleanly as a screenshot. Fill every bracket; keep the row order and labels exactly as shown. The panel's read is the panel's recommendation, drawn from what the advisors argued, never invented past it; the decision stays the user's, and the read never overrides the closing stress-test line.

```
IDEA SCORECARD
Idea: <one-line summary of what the user described>

Clarity of offer         X.X/10
Market realism           X.X/10
Financial viability      X.X/10
Execution feasibility    X.X/10
Risk coverage            X.X/10
Differentiation          X.X/10

Reachability (trial)     X.X/10   beside the rubric, not in the average

Average: X.X/10   Pass line: 8.5   Grade: <letter>

Lowest: <dimension name, or the tied dimensions listed> (X.X)
What the panel caught: <one sentence, cites the description or names the gap>

The panel's read: <pursue as-is / close the gaps first / walk away> - <one sentence>
First move: <the single next action, taken from the executor's own answer>

[Input note, only when the description was too thin to support full scoring:]
A description this short caps what can be scored. The gaps above are the finding, not a failure to produce confident numbers on every line.

This is a stress-test, not a certification. A pass means no confident weakness was left un-named. A low score is the useful result.
```

Save the filled scorecard to `outputs/idea-scorecard-<slug>.md`, where `<slug>` is a short lowercase, hyphenated form of the idea (for example `idea-scorecard-dog-walking-app.md`). Create the `outputs/` folder if it does not exist.

5. NEXT STEP: end with exactly one line: adding detail to the description and running `/grade-idea` again is free, and the score will move as the gaps close. State it once and stop. Do not propose a revision loop, a follow-up plan, or another pass unless the user asks.

6. CLOSE: end the whole response with exactly one sentence offering the deep path this install already ships: if the idea is worth a real plan, /intake turns it into a structured brief, and /business-plan, /grade, and /approve take it the rest of the way. Say it once. Never repeat it, never expand it into a pitch.

Bans, all of them absolute: never mock the idea or its owner. Never imply a passing score predicts the business will succeed, or that a low score means it will fail. Never invent a fact, a number, or a mitigation the user did not state to make a dimension score higher. Never reference a plan document or scorecard the user does not actually have, or any command this install does not ship.

Obey the constraints rule: make claims measurable; do not combine unrelated tasks without section breaks.
