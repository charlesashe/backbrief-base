---
name: experiment-designer
description: Design the smallest decisive test before committing work or money to an uncertain plan. Produces an experiment brief with hypothesis, smallest test, budget and time cap, success metric, minimum sample or decision threshold, a mandatory stop rule, and next action by outcome. Use when asked to design an experiment, find the cheapest test, validate an assumption, pilot something, or prove demand before spending.
version: 1.0.0
category: Decision & Evidence
domain: experimentation
author: Backbrief (first-party)
status: draft
updated: 2026-08-26
activation_triggers:
  - "design an experiment"
  - "smallest test"
  - "test this before we build it"
  - "cheap test"
  - "validate this assumption"
  - "pilot"
  - "should we test this first"
  - "run a small test"
  - "MVP test"
  - "prove the demand before we spend"
---

# Experiment Designer

Turn an uncertain plan item into the smallest test that can safely tell the owner whether to proceed, change course, or stop. This skill is the bridge between a plan that still carries open assumptions and any resourced action taken on those assumptions. It operationalizes one rule: do not move work or money on an idea nobody has tested.

The skill produces one artifact: an experiment brief. It never runs the experiment, spends the budget, or launches anything itself.

## Before anything: two gates

Check both before designing a single test. Neither is optional and neither is satisfied by the requester's confidence that it will be fine.

**Gate 1, the ceo-gate.** This skill is loaded by the orchestrator or builder as planning support for /business-plan and /grade, and for a business with a graded, approved plan and a recorded owner GO. If there is no recorded GO, the request is planning support only: an experiment brief may still be drafted (typically requested by the business-plan or grading step to strengthen a weak dimension with a proposed test rather than an unexamined assumption), but the brief is labeled "planning support, not authorized to run" and nothing in it may be executed, scheduled, or resourced. Producing a design is not the same as clearing it to happen. If asked to run, schedule, or spend against a brief that carries this label, decline and point back to the approval step.

**Gate 2, the spend gate.** Any experiment that spends money, in any amount, stops for the owner before it runs, regardless of GO status. A recorded GO approves the plan; it does not pre-authorize a specific spend. Prepare the experiment to done-but-unsent: hypothesis, test design, budget cap, and stop rule fully written, ready to execute the moment the owner says go. Then stop and hand over the decision, stating what is ready, what decision is needed, and the recommended choice with one line of reasoning. Do not treat silence as approval. This applies even to trivially small amounts; the gate is about the category of action, not the size of the number. A zero-spend test (a survey, a manual concierge pilot, a landing page with no ad traffic behind it, a conversation with five prospects) does not trigger this gate and can move directly to done-but-unsent readiness for the owner to greenlight on schedule, but never assume zero spend without checking: ad tests, paid tools, contractor time, and paid list access all count.

## Step 1: Form the hypothesis

State the belief being tested as a single falsifiable sentence: "If we [do X], then [segment] will [measurable behavior], because [reason]." Reject a hypothesis that cannot fail. "People want a better version of this" is not testable. "At least 10 of 50 contacted small-business owners will book a paid consultation within two weeks of a direct outreach message" is.

Pull the hypothesis from the plan unit or plan dimension that prompted the request, not from a restated version of the whole business idea. One experiment tests one belief. A plan with three shaky assumptions needs three briefs, not one brief trying to cover all three.

## Step 2: Design the smallest decisive test

This is the core judgment call the skill exists to make well. A test is decisive when its result can actually change the decision; it is smallest when it costs the least time and money that still produces a decisive result. Optimizing for either alone produces a bad test: the cheapest possible action (posting a tweet) is rarely decisive, and the most rigorous possible action (a full build and launch) is rarely small.

Ask, in order:

1. What is the cheapest thing a real prospect could do that would only happen if the hypothesis is true? Prefer a real commitment (money, a signed order, a scheduled call, a submitted application) over a proxy (a survey answer, a like, a stated intention). Stated intent is the weakest evidence available and should be the fallback, not the default.
2. Can this be tested without building the thing at all? A landing page with a real order button, a concierge process done by hand behind an automated-looking front end, a pre-sell, a single manual delivery to one real customer, and a direct outreach message to a qualified list are all smaller than a build. Reach for `references/smallest-decisive-test-patterns.md` for a working list of these patterns matched to common plan situations, before defaulting to "build a prototype."
3. What population and channel actually resembles the real buyer? A test run on the wrong audience produces a result that answers nothing.

Write the test as: what happens, to whom, over what channel, for how long.

## Step 3: Set the caps and thresholds

Every brief carries four numbers, stated before the test starts, never adjusted afterward to fit the result:

- **Budget cap.** The maximum spend, in the owner's currency, that this test will use. Zero is a valid and common answer; state it explicitly rather than leaving it blank.
- **Time cap.** The calendar date or elapsed duration after which the test ends regardless of how it is going. An experiment with no end date is not an experiment; it is a new ongoing activity wearing an experiment's name.
- **Success metric.** The single measurable outcome that will be checked, stated as a number or a rate, not a feeling. "Good engagement" is not a metric. "12% of landing page visitors submit an email" is.
- **Minimum sample or decision threshold.** How much evidence is enough to act on. Name the count (number of visitors, number of outreach replies, number of orders) below which the result is inconclusive rather than negative, and say what happens if the cap is hit before that count is reached: usually, extend once at the same budget or call it inconclusive and stop, never silently keep spending until a result appears.

When the plan spans materially different segments, price bands, or channels, do not blend them into one threshold. Either set a threshold per segment or state plainly that one number is being used and name where it is likely to be wrong.

## Step 4: Write the stop rule

Mandatory. A brief with every other field filled and no stop rule is not complete and does not go to the owner. The stop rule is the answer to one question, asked before the test starts, in the requester's own words: **what result kills this?**

A good stop rule is symmetric with the success metric and just as specific: "If fewer than 3 of the 50 contacted owners reply within two weeks, the direct-outreach channel is dead for this offer at this price; do not repeat it, revise the price, or find a warmer list before testing this channel again." A stop rule that only describes success, or that says "we'll reassess," is not a stop rule; it is a way to keep going regardless of the result. Write it so that a different, less invested person reading only the stop rule could correctly call the outcome without asking the requester what they meant.

## Step 5: Name the next action

State, for both outcomes (the hypothesis holds, the hypothesis fails), what happens next and who does it: proceed to the next plan unit, revise the offer and retest, escalate a different assumption, or stop the initiative. A brief that stops at the metric without naming the next action for each branch hands the owner a report, not a decision aid.

## Step 6: Deliver

Fill `references/experiment-brief-template.md` and write the completed brief to `outputs/`. Every brief carries all of these, in this order, with none left as a placeholder: hypothesis, smallest test, budget cap, time cap, success metric, minimum sample or decision threshold, stop rule, next action for each outcome, and the gate status (cleared to run, or planning support only, per the gates above).

Keep the brief to what is needed to run and judge the test. It is a working document for the owner to approve, not a narrative.

## Escalation restatement

Every experiment this skill designs stops before it spends, publishes, or commits to anything external, exactly the same way any other outward action in this system stops for the owner: prepare the work to done-but-unsent, state what is ready and what decision is needed, and wait. A recorded plan approval clears the initiative; it never pre-clears a specific spend, message, or publish action produced under it. Designing the test is this skill's job. Deciding to run it stays the owner's, every time.

## Scope

This skill designs experiments; it does not execute them, does not analyze results after the fact (that belongs to a postmortem or learning-loop pass once data exists), and does not replace the grading rubric's own market-realism or risk-coverage checks, it feeds them. No em dashes anywhere in this skill's output.
