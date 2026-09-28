---
name: niche-picker
description: For someone with no business idea yet. Interviews the operator for skills, weekly hours, money available to risk, hard constraints and the work they refuse, scans for market gaps with /find-gap, then returns three candidate niches, each graded on the public six-dimension rubric with a named first move for this week. Use for "what business should I start", "help me pick a niche", "I have some skills and a few hours a week, what can I do", "I do not have an idea yet", "find me something to build". Analysis only; it recommends nothing to buy, join or spend on, and it never picks for the operator.
---

# Niche picker: three graded candidates for someone with no plan yet

A grader needs something to grade, and a buyer with no idea has nothing to hand it. This skill
makes the three things worth grading. It takes the operator's own limits from an interview,
scans public complaints for gaps that fit inside those limits, builds three candidates, and
grades each on the same six-dimension rubric `/grade-idea` uses. The output is three
scorecards and three first moves. The operator chooses.

## What it is not

- **Not a pick.** It returns three candidates and orders none of them. The operator picks one,
  picks none, or changes a constraint and runs it again. No line in the output says "start
  with this one".
- **Not a prediction.** A grade is a stress-test. A high grade means no confident weakness was
  left un-named against the rubric. A low grade names the weakness, which is the useful result.
  Neither predicts what the business will earn.
- **Not a shopping list.** It recommends nothing to buy, join or spend on: no course, tool,
  community, list, domain, ad or subscription. The operator's money figure sizes the box the
  candidates must fit. Nothing here spends it or suggests spending it.
- **Not an outreach run.** It sends nothing and contacts no one, including anyone quoted in the
  scan.

## 1. Set up

Read `context/strategy/current-state.md` and `context/strategy/current-priorities.md` when
they exist, and `outputs/business-brief.md` when it exists. Whatever they already answer, the
interview does not ask again.

Open the capture file `context/discovery/YYYY-MM-DD-niche-picker.md` (date from the system
clock, folder created on first use) with three sections in this order: Settled, Open, and
Answers in the order given. Name the path to the operator once. If the `discovery-interview`
skill is installed, load it and follow its cycle; if not, the cycle below stands alone.

## 2. Interview

One question per turn. Each turn has four beats: ask one thing and offer the answer you would
infer, marked as an inference; take the answer as given; write it to the capture file before
asking again; choose the next question from the answer. An answer the operator cannot give
becomes an Open row with the name of who can answer it. Never supply the missing fact.

Fields to collect, in this order, because the early answers prune what the later ones can use:

| # | Field | What to collect |
|---|---|---|
| 1 | Hard constraints | Where the operator lives (city, state, country). Licenses held or lacking. Work they will not do: cold outreach, phone calls, appearing on camera, holding inventory, handling other people's personal or financial data, or anything else they name. Limits from an employer or a contract. Record each as stated. A location or license answer is the operator's statement, flagged for the researcher; the interview does not settle it. |
| 2 | Weekly hours | The hours per week the operator can commit, and whether they come as fixed blocks or scattered. A range is recorded as the low end, and the card says so. |
| 3 | Money to risk | The amount the operator can lose without harm to rent, debts or savings. Zero is a valid answer. The interviewer never proposes a figure. If the operator cannot say, the row goes to Open and grading treats it as zero. |
| 4 | Skills | What the operator has done that a stranger would pay for, each with its proof: the job, the project, the result. Ask for what they did, not what they would like to learn. A skill they would have to learn is graded as a gap under execution feasibility. |
| 5 | The pain they would rather not solve | The problems, customers, tasks or industries the operator refuses: burnout, dread, ethics, history. This is an exclusion filter. A candidate that lands on it is dropped, not softened. |
| 6 | Numbers and reach already held (optional) | A price the operator has charged before, past customers, an audience, a network. Feeds the reachability trial line and financial viability. Skip when there are none. |

The interview ends when fields 1 to 5 each have a Settled row or an Open row. If field 4 is
Open, stop and say so: a scan run on an invented skill set produces a guess. Any other Open
field lowers the scores it touches and shows up on the card.

Then read the box back in one block (hours, money, hard constraints, refused work, skills) and
ask the operator to confirm or correct it. After the confirmation, ask nothing further.

## 3. Gap scan

Choose one subject: an audience the operator's skills serve and the box allows. Build it from
fields 4 and 6, and screen it against fields 1 and 5, so a subject that needs refused work is
never scanned. Show the scope line to the operator (`/find-gap` step 1) and continue unless
they correct it.

Run `/find-gap` on that subject through its step 8: scope, one researcher dispatch, rank, tag,
confidence, regulated-activity line, render, save. Hold its step 9 offers and its step 10 brief
pre-fill. The picker's own close in section 7 replaces them. Run a second scan, on a different
subject, only when the first leaves fewer than three usable gaps after the section 4 filter.
Two scans is the cap.

Keep from each gap: the name, the complaint line, the demand state, the existing options, the
confidence line, the regulated-activity line, and the evidence lines with their tags as
the scan returned them. A gap with NO SEEKERS stays in the saved scan and becomes a candidate
only when fewer than three other gaps survive; its card then says no seekers were found.

If the scan fails or comes back thin, say so. The candidates then come from the interview
alone, and every card says "interview only".

## 4. Three candidates

**Filter first.** Drop any gap whose fix needs work the operator refuses (field 5) or breaks a
hard constraint (field 1). Skill gaps and money gaps are graded, not filtered. A regulated
activity is flagged and graded, and dropped only when the operator said they lack the license.

**Build three.** Each candidate carries:

- a short name;
- the offer in one sentence a stranger understands: who pays, for what;
- its origin: the gap it came from, or "interview only";
- a fit line in the operator's own numbers: hours, money to risk, constraints.

The three differ by buyer or by mechanism. Three price tiers of one offer count as one
candidate. Choose among the surviving gaps by fit to the box first, then by scan confidence.
Present the candidates in the order you built them, lettered A, B and C.

No price appears in any candidate. Price is the operator's decision. The brief says "price not
stated" unless the operator gave one in field 6.

If fewer than three fit the constraints, build the rest from the interview alone and label
them. If the hard constraints leave fewer than three that can exist, say which constraint
blocks the rest and return the ones you have. Never invent a gap, a quote or a demand signal,
and never breach a hard constraint to reach three.

## 5. Grade each candidate

Run the `/grade-idea` procedure on each candidate as its own idea. Steps 0 to 3 run as
written: the local-law check, a brief of at most 300 words, five advisors in parallel that
receive only the brief and the rubric, and consolidation on the strong model. Step 4's
scorecard block is filled as written and rendered into the picker's output file instead of a
separate one. Steps 5 and 6 are held for the picker's close.

The researcher and the five advisors that these steps dispatch are agents the base product
lifts in at assembly. If `.claude/agents/` in this install holds none of them, say so at the
start of the run and grade by hand on the same rubric, labeling every scorecard as a
hand-applied grade, not a panel result.

Each candidate is a separate dispatch. One candidate's advisors never see another's brief.

The consolidated justification for each dimension goes into the output as one sentence under the
block ("Why these scores"). Each sentence cites the operator's words or the scan line it rests
on, or names the gap where the brief is silent, and carries the tag of any figure it uses.

The brief holds: the offer; who pays; the operator's own numbers and constraints, each tagged
unverified (the operator's own, unchecked); the scan evidence for that gap with its tags and
confidence line, or "no scan evidence, interview only"; and the regulated-activity line if
there is one. Nothing else goes in. The brief adds no fact the operator or the scan did not
supply.

**Number discipline.** Any figure in a scorecard, a first move or a candidate line is one of
three things:

1. the operator's own stated number, quoted as stated and tagged unverified;
2. an outside figure with its URL, its accessed date and a tag: verified, unverified or vendor
   claim;
3. arithmetic on type 1 numbers, with the arithmetic shown.

A figure that cannot be retrieved is written without the number, or marked unverified. This
skill never estimates a price, an income, a market size, a conversion rate or a cost.

**Jurisdiction.** A claim about what is legal, licensed, required, disclosed or taxed in a
named place goes to the researcher before it can raise a score. Until then it reads "unverified
local-law assumption, <place>" and never counts as risk coverage.

**Expect low financial viability.** No price means the unit economics do not close on the
operator's numbers, and the card says so. The first move often closes the gap.

## 6. The first move

Each candidate gets a named first move on the `First move:` line of its block, in the form
`<short name> - <what the operator does>`. Take it from the executor advisor's answer and edit
it until it passes all five tests. If the answer cannot pass, replace it and say the card's line
is a rewrite.

1. The operator finishes it inside one week and inside the weekly hours they stated.
2. It spends nothing and buys nothing.
3. The operator does it themselves. It involves no cold outreach if field 1 excludes it, and no
   contact with anyone found in the scan.
4. It is a concrete act: write down, count, draft, list, price a job on paper. "Research the
   market" fails.
5. Its result would move a named rubric dimension on the next `/grade-idea` run, and the line
   names that dimension.

## 7. Output

Save the run to `outputs/niche-picker-YYYY-MM-DD.md` (create `outputs/` if absent; add a
numeric suffix rather than overwrite). Layout, fixed width so it screenshots:

```
NICHE PICKER
Operator: <one line: who, and what they can do>
The box: <hours> hours a week | <money to risk> | Hard constraints: <list> | Will not do: <list>
Gap scan: <path to the saved scan, or "none: interview only"> | <one line on its confidence>

CANDIDATE A  <name>
Offer: <one sentence: who pays, for what>
Came from: <gap name | interview only>
<the /grade-idea scorecard block, filled>
Why these scores:
  <one line per rubric dimension, in rubric order, then the reachability line>

CANDIDATE B  <name>
...

CANDIDATE C  <name>
...

SIDE BY SIDE
                         A      B      C
Clarity of offer
Market realism
Financial viability
Execution feasibility
Risk coverage
Differentiation
Average
Where they differ: <one sentence>. The table shows differences. It does not choose.
```

When all three land below the pass line, say so in one sentence and name the one interview
answer that would move the most scores. A thin interview capping the scores is the finding.

Close with these lines, once, then stop:

- "This is a stress-test of three candidates, not a prediction that any of them will work. A
  complaint in the scan is not evidence that anyone will pay."
- "Nothing here recommends buying, joining or spending on anything. The choice among the three,
  or none of them, is yours."
- "Do the first move for the one you pick, add what you learn, and `/grade-idea` scores it
  again for free. If one is worth a real plan, `/intake` turns it into a brief, and
  `/business-plan`, `/grade` and `/approve` take it the rest of the way. To change the box,
  tell me what changes and I run the picker again from the scan."

## Bans, all absolute

- Never say which candidate to choose, rank them, or hint at a favorite.
- Never recommend a purchase, a membership, a tool, a course or a spend of any size.
- Never state a price, an income, a market size or a cost that the operator or a cited source
  did not supply.
- Never invent, complete or adjust a quote, a URL, a date or a venue from the scan. The one
  permitted change is a correction toward the source page after re-opening it, recorded in
  the run notes with the before and after.
- Never state what a license or law requires in a named place as fact.
- Never breach a hard constraint or land on the refused-work list to reach three candidates.
- Never present a passing grade as a prediction or a low grade as a verdict on the operator.
- Never contact anyone, send anything or sign up for anything.

## Composes with

- `/find-gap` for the scan (section 3) and `/grade-idea` for the rubric, the advisors and the
  scorecard (section 5).
- `discovery-interview` for the interview cycle when installed.
- `stop-slop` on every line of prose before the run is called done.
- `fresh-context-verification` when the operator asks for the output to be checked.
