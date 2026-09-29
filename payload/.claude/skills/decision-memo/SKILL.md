---
name: decision-memo
description: Produce a one-page decision brief for a consequential choice, with options including doing nothing, a recommendation, tradeoffs, tagged evidence, risks, cost, reversibility, and an explicit GO or NO-GO request for the owner. Use when a choice needs the owner's decision, when weighing options with real cost or risk, or when someone asks for a decision memo or recommendation write-up.
version: 1.0.0
category: Decision & Control
domain: governance
author: Backbrief (first-party)
status: draft
updated: 2026-08-26
activation_triggers:
  - "decision memo"
  - "GO/NO-GO"
  - "go no-go"
  - "consequential choice"
  - "should we"
  - "before we commit to"
  - "before we spend on"
  - "owner decision needed"
---

# Decision Memo

Produce the standard one-page artifact for a consequential choice: what is proposed, what evidence supports it, and what the owner must explicitly decide. This skill requests a decision. It never records one as made.

## When to use

Use whenever a choice is real enough to commit money, time, reputation, or a relationship, and small enough to state on one page: adopting a tool or vendor, changing a price, entering a new channel, killing or keeping a workstream, committing a budget line, signing up for a service. Primary agent is the orchestrator; any agent may request a memo when its own work surfaces a choice the owner needs to make.

Not for business-plan approval. `/approve` is the recorded GO for a graded business plan under the CEO loop. A decision memo is the artifact for every other consequential choice, the ones that come up between plans or inside one. If the choice is "should we proceed with this whole business," route to `/approve`. If it is one decision inside an already-approved plan, or a decision the CEO loop does not cover at all, write a decision memo.

## What it produces

One filled copy of `assets/decision-memo-template.md`, saved to `outputs/` and named for the decision (for example `outputs/decisions/2026-08-26-vendor-x-adoption.md`). Every field in the template is required. Do not add fields. Do not remove fields because they feel inconvenient for this particular decision; if a field genuinely does not apply, write "not applicable" and one line of why, rather than deleting the row.

The template's fields, in order:

1. **Decision statement.** One sentence: what is being decided, stated so a stranger understands it.
2. **Options.** Every real option, including the do-nothing option. Do-nothing is never omitted, even when it is clearly the worst choice; naming it is what makes the recommendation a comparison instead of an assertion.
3. **Recommendation.** Which option, plus one line of reasoning. Not a paragraph. If the reasoning needs more than one line, the options above are underspecified.
4. **Tradeoffs.** What the recommended option gives up relative to the next-best option. Every recommendation costs something; name it.
5. **Evidence.** Every fact used to support the recommendation, each tagged **verified**, **unverified**, or **vendor claim** per the grading rule (`.claude/rules/grading.md`). Quoting a source's own claim about itself is not verification. Tag consistently even where the honest tag is unflattering to the recommendation.
6. **Risks.** The risks specific to this decision, not a generic list. Each risk gets a one-line mitigation or an explicit note that the owner is accepting it unmitigated.
7. **Cost.** What this costs in money, time, and anything irreplaceable (a relationship, a reputation, a slot). State the number or state plainly that no number exists yet and why.
8. **Reversibility.** Stated plainly: what it takes to undo this if it goes wrong. Name the mechanism (cancel a subscription, revert a commit, unwind a contract) and roughly how long it takes. "Reversible" and "irreversible" without a mechanism are not answers.
9. **GO/NO-GO request.** The explicit question to the owner, and nothing else. Never a decision already made, never a default that takes effect on silence.

## The one-page constraint

One page is enforced, not aspirational. If a completed memo runs past roughly 500 words or forces a second page to hold its content, that is a signal the choice in front of the owner is actually several decisions bundled together, not one. Split it: write a separate memo per decision, and say so to whoever asked for the memo, rather than compressing a multi-decision choice into dense fine print to keep it on one page. Compression that makes the page still fit while losing the owner's ability to actually read it in one pass defeats the artifact.

## What this skill never does

- Never records a decision as made. The memo requests a GO/NO-GO; it does not contain one. The decision itself lands in `.claude/memory/decisions.md` only when the owner actually makes it, per the decision-log rule, and only the owner's own words in session count as that decision. Per the escalation rule, silence is not approval: an unanswered memo sitting in `outputs/` is a pending request, not a NO-GO and not a GO.
- Never proceeds on the recommended option before the owner answers. Drafting the memo is preparation, not authorization; this mirrors the escalation rule's "done-but-unsent" standard applied to a decision rather than an outward action.
- Never substitutes for `/approve` on a full business plan, and never substitutes for the researcher on a jurisdiction-specific legal, tax, or licensing claim inside the evidence section: that claim goes through the researcher first, tagged per the agent-routing rule, before it can appear as evidence here.

## Delivery

Write the filled memo to `outputs/decisions/` and hand it to the owner with a one-line summary of what is being asked. Log nothing in the decision log until the owner responds; when they do, the decision-log entry references the memo's file path so the two stay linked.

No em dashes anywhere in this skill's output.
