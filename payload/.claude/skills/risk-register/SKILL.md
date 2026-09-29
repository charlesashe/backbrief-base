---
name: risk-register
description: Turn a graded plan's weaknesses into an owned, monitorable risk register after the owner's GO. Each row carries risk, likelihood, impact, a checkable leading indicator, mitigation or explicit acceptance, owner, review date, and a pre-committed kill or pivot trigger. Use after /approve, when asked to track risks, set kill criteria, or turn scorecard weaknesses into monitored items.
version: 1.0.0
category: Decision Quality & Governance
domain: risk-management
author: Backbrief (first-party)
status: draft
updated: 2026-08-26
activation_triggers:
  - "risk register"
  - "graded weaknesses"
  - "kill trigger"
  - "pivot trigger"
  - "after GO"
  - "monitor this risk"
  - "who owns this risk"
  - "leading indicator"
---

# Risk Register

Turn the plan's graded weaknesses into rows a named person owns and actually rereads. The grading rubric's risk-coverage dimension names weaknesses inside a scorecard; this skill is what happens to those weaknesses after the owner says GO, so they become tracked items instead of a paragraph nobody opens again.

## Before anything: the ceo-gate

This skill is loaded by the orchestrator after /approve and stays behind the ceo-gate rule. Confirm a recorded GO in `.claude/memory/decisions.md`, referencing the plan and its final scorecard, before building or updating a register. If there is no recorded GO, decline and point to `/intake`. Do not draft rows, do not ask clarifying questions first. The gate check comes before Step 1.

## Step 1: Pull the source material

Read the approved plan and its final scorecard (the /approve record and the grading pass it references). Pull candidate risks from two places, not one:

- Every risk named in the risk-coverage dimension's justification text, whether it already carries a mitigation or was scored down for lacking one.
- Any weakness cited in another dimension's justification that is really a risk in disguise: a financial-viability score citing an unverified cost assumption, a market-realism score citing an unconfirmed buyer signal, an execution-feasibility score citing a skill or time gap. A weakness does not stop being a risk because it was scored under a different heading.

Do not invent risks the scorecard never named. This skill converts graded weaknesses into owned items; it does not go looking for new ones. If the owner or the orchestrator wants to add a risk the grade never surfaced, add it, but label the row's source as "added post-grade," not "from scorecard," so the register does not overstate what the grade actually covered.

## Step 2: One row per risk

Every row carries all eight fields. A blank field is not a shorter row; it is an unfinished one, and the register is not done until each row has all eight.

- **Risk**: one sentence, specific to this plan. "Market risk" is not a risk; "the ICP defined in the brief has fewer than 200 reachable buyers on the channel the plan depends on" is.
- **Likelihood**: low, medium, or high, plus the one clause that justifies it, cited against the plan's own text or a named outside source. A likelihood with no justification clause is a guess wearing a label.
- **Impact**: low, medium, or high, and impact on what: revenue, timeline, viability, or reputation. Name the dimension, not just the size.
- **Leading indicator**: the thing you would see FIRST, stated so it can be checked against a number or a date, never a feeling. "Cost per lead exceeds $40 for two consecutive weeks" is an indicator. "Leads start feeling harder to close" is not, and a row with a feeling in this field is not finished.
- **Mitigation or explicit owner acceptance**: a concrete action with its own owner and date, OR the owner's explicit sentence accepting the risk as-is, dated. "Monitor closely" is neither: it names no action and no threshold. If the plan's own text already states an acceptance, quote it; if not, ask the owner for one rather than inventing a mitigation that sounds sturdier than what was actually decided.
- **Owner**: a named person. "The team" owns nothing; a person does.
- **Review date**: an actual date on a calendar, not "ongoing" or "regularly." Tie it to the plan's own review cadence if one exists; otherwise ask the owner to set one.
- **Kill/pivot trigger**: the pre-committed, testable condition under which this risk ends the plan or forces a pivot, written now, calm, not left for the moment the risk actually fires. State it as a threshold the leading indicator can cross, not as a mood. A register with no kill/pivot trigger on a high-impact row is incomplete, not conservative.

## Step 3: Jurisdiction-specific rows get the researcher discipline

Any risk row that touches what is legal, required, licensed, disclosed, or taxed in a named place cannot be marked mitigated on general knowledge alone (agent-routing rule: an unretrieved statute is an assumption, not a mitigation). Before such a row's mitigation field is written as fact:

- Route the claim to the researcher for retrieval against a named, current source.
- Until that retrieval has run, write the mitigation field as "unverified local-law assumption, jurisdiction: [name]" rather than a confident sentence. A row that reads as mitigated but rests on general training knowledge of a law that may have changed is worse than an honest blank.
- Once the researcher returns a sourced answer, update the row and cite the source in the register's notes.

## Step 4: State the cadence, out loud

A register nobody re-reads is theater, not risk management. The register is not complete on delivery; it is complete on its first scheduled reread. Write the review cadence into the register itself (weekly, monthly, or whatever the plan's own operating rhythm supports) and log the next review date. If the owner has no standing cadence for this plan, ask for one before calling the register done rather than defaulting to a date nobody agreed to.

When a review happens, update each row's likelihood, impact, and leading-indicator status in place, and add a dated line to the row's notes rather than silently overwriting what the last review found. A register that only ever shows the current read is not distinguishable from one that was never reviewed at all.

## Step 5: What this skill does not do

If a leading indicator crosses its stated threshold, this skill's job is to say so plainly and point at the pre-committed kill/pivot trigger, not to act on it. Pulling the plan, cutting spend, or changing direction is the owner's decision under the escalation rule, made in the moment with current facts, even when the trigger was written calmly in advance for exactly this moment. State what the register shows, state which trigger it matches, and stop.

## Step 6: Deliver

Write the register to `outputs/` using `assets/register-template.md`, one file per plan, named for the plan it tracks. Reference it back in the plan document and in `.claude/memory/decisions.md` with the date it was created and its first review date. Non-trivial registers (anything the owner will act on) go through the verifier before being called done, per verify-before-delivery.

## Constraints

No em dashes. No invented risks beyond what Step 1 permits. No mitigation language stronger than what the plan or the owner actually committed to.
