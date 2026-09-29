---
name: market-validation
description: Collect and structure evidence for a plan's market claims before grading. This skill should be used before /grade evaluates dimension 2 (market realism), whenever a plan, brief, or idea rests on claims about buyer demand, a customer problem, or market size that have not been checked against evidence yet. Trigger on requests to validate a market, stress-test demand claims, build an evidence base before grading, check whether a claimed customer problem is real, or when /business-plan or /grade needs supporting evidence for the market realism dimension.
---

# Market Validation

Turn a plan's market claims into a structured evidence base before the plan is graded. This is
evidence collection, not a verdict: it produces the material dimension 2 of the grading rubric
(market realism) needs, and it stops there.

## Primary agent

researcher. This is planning support under the ceo-gate rule: gathering evidence for a plan that
has not been approved yet, never execution for an approved business.

## What this skill is not

It does not grade the plan, does not score market realism, and does not recommend proceed, pivot,
or kill. Evidence that a problem exists is not a prediction that a business built around it will
succeed. The output template ends with a fixed line stating this, and that line is not optional.

## Step 1: Build the claim ledger

Read the plan or brief and pull out every sentence that asserts something about the market: who
the buyer is, that a problem exists, that people will pay, that a segment is large or growing, that
a channel works. Quote the claim verbatim and note where it appears. A claim that cannot be quoted
from the plan's own text does not belong in the ledger; if a claim was implied rather than stated
outright, say so and quote the nearest text that implies it.

## Step 2: Gather evidence per claim

For each claim, look for material that supports, contradicts, or is silent on it: named buyers who
have said something on the record, comparable products already selling into this market, review
threads, forum posts, search or trend data, industry reports, direct outreach the owner has already
run. Prefer sources close to the buyer's own words over aggregated or paraphrased ones.

Two additional evidence blocks are mandatory outputs, not optional extras:

- **Customer and problem signals**: direct evidence the underlying problem is real and felt, in the
  words of someone who has it. A quote, a support ticket, a forum complaint, a review. Source and
  date every one.
- **Competitor alternatives**: what a buyer does today instead, including doing nothing. Named
  products, their price point, and the concrete reason a buyer might already be satisfied with the
  alternative. A plan with no named alternative has not looked hard enough; it has not found a
  market with no competition.

## Step 3: Tag every piece of evidence

Use the grading rubric's own evidence taxonomy, unchanged:

- **verified**: checked against a named source.
- **unverified**: plausible, unchecked.
- **vendor claim**: the source sells something.

Quoting the plan's own text about itself is never verification. A plan citing its own market-share
or membership number is an unverified figure until it is checked against something outside the
plan, and the evidence table has to say so. Apply the tag consistently across every claim, not only
where a figure happens to look suspicious.

## Step 4: Rate confidence per claim

For each claim in the ledger, roll its evidence up into one confidence rating:

- **Strong**: multiple verified sources, no material contradiction.
- **Moderate**: one verified source, or multiple independent unverified sources pointing the same
  way.
- **Weak**: unverified or vendor-claim evidence only.
- **Unsupported**: no evidence found for or against the claim.

State the rating and cite the specific evidence table rows behind it. A rating with no citation is
not a rating.

## Step 5: Name unresolved assumptions

List every claim the search could not resolve, what would resolve it, and who or what could resolve
it (a specific search, a specific person to ask, a specific document to find). A jurisdiction-
specific legal, tax, or licensing claim buried inside a market claim (a licensing requirement that
gates who can even buy, for example) is not something this skill resolves on general knowledge; name
it as an unretrieved statute, flag the jurisdiction, and route it to the researcher for retrieval
rather than reasoning past it, per the agent-routing rule.

## Step 6: Deliver

Write the completed evidence base to `outputs/`, using the structure in
`assets/market-validation-template.md`: claim ledger, evidence table, customer and problem signals,
competitor alternatives, unresolved assumptions, and confidence rating per claim, ending with the
fixed statement of what this artifact did not do. Reference the file back to the plan or brief it
supports so the grading pass can find it.

## Escalation awareness

This skill sources evidence that already exists: public reviews, forum threads, published reports,
outreach the owner has already run. It does not contact a real customer, post anywhere, or send a
survey on its own. If closing a gap in the evidence genuinely needs new outreach (a direct question
to a prospect, a survey, a forum post asking for input), draft it and stop there: that draft goes to
`outputs/` done-but-unsent, and sending it is the owner's decision, per the escalation rule. Mark the
claim it would have resolved as unresolved in the meantime, not as pending.

## Style

No em dashes anywhere in this skill's output.
