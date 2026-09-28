---
name: fresh-context-verification
description: >
  The verification protocol for the verifier and any fresh-context review: entry/exit
  gates with BLOCKED and UNVERIFIED verdicts, three pause points, artifact-type
  adversarial passes, the claim ledger, anti-sycophancy controls, a judge protocol for
  rubric scoring, and the reproducible evidence envelope. Trigger on: verifying any
  finished artifact, verifier dispatches, acceptance-criteria review, "check this before
  it goes out". Sources: Fagan 1976, Bacchelli & Bird 2013, WHO/NASA checklist research,
  NIST AI 600-1, Zheng et al. 2023, Min et al. 2023, Huang et al. 2024, Anthropic
  sycophancy research - all accessed 2026-08-28.
---

# Fresh-Context Verification

The verifier is an independent inspection system, not a second generic reviewer. Fresh
context removes the producer's narrative; this protocol adds what fresh context alone
cannot: independent contract reconstruction, mechanical evidence, counterexample search,
exposed unverified scope, and a reproducible verdict.

**Regression harness (recommended):** keep one harness for measuring verification behavior
- seeded-defect suites, gold sets, and judge-bias tests all live there as scenarios.
Anything this protocol needs measured gets a scenario in that harness; never build a
second, parallel one, because two harnesses drift and neither stays trusted.

## 1. Entry gate - or the verdict is BLOCKED, never PASS

Before inspecting: artifact exists at a named path (hash it for anything contested);
authoritative acceptance criteria identified; environment and allowed tools known;
verification dependencies available. Missing any: return **BLOCKED** with what is missing.
Silence is not evidence, and a pass with no entry gate is worthless.

## 2. Independence controls (anti-sycophancy, all mandatory)

- Read the specification and the artifact BEFORE any producer summary. Producer claims are
  assertions to test, not context to trust. (Dispatchers: never tell the verifier the
  artifact is "finished", "approved", or expected to pass; never include the producer's
  confidence or desired verdict.)
- Write a provisional failure hypothesis before reading any producer notes that were
  provided.
- Pair every semantic judgment with external feedback where one exists: tests, parsers,
  schemas, source documents, independent recalculation, browser observation.
- Models do not reliably self-correct without external feedback and can degrade trying
  (Huang et al. 2024); sycophancy is a measured failure mode (Anthropic research). The
  same model response never both produces the artifact and serves as its sole acceptance
  evidence.
- High-severity findings get a REFUTATION pass: a fresh context tries to disprove each,
  from the artifact and sources, not from the first verifier's reasoning.

## 3. Three pause points (checklists are pause points, not paperwork)

1. **Before inspection:** artifact identity, version/hash, requested outcome, authoritative
   requirements, environment, risk class, prohibited actions.
2. **Before verdict:** every must-requirement has evidence; every executed command has
   captured output and exit status; adversarial cases ran where applicable; unsupported
   claims are marked.
3. **Before delivery:** the report names unresolved items, scope NOT checked, evidence age,
   artifact path, and exact rerun instructions.

Checklist rules: short universal spine + artifact-type modules; a checked box with no
evidence pointer is invalid; `not applicable` requires a reason; items that never change a
decision get removed; time pressure is a risk input, never a reason to skip silently.

## 4. Adversarial pass by artifact type (at least one, matched to the artifact)

- **Code/automations:** malformed, empty, extreme, duplicated, out-of-order, unauthorized,
  expired, replayed, concurrent inputs; dependency failure; timeout; partial write; retry;
  rollback; wrong timezone.
- **Revenue reports:** date-boundary errors, currency-unit confusion, test-mode mixed with
  live, refunds omitted, fees double-counted, duplicated events, zero denominators,
  one-sale percentages presented as trends.
- **Marketing/research prose:** unsupported numbers, testimonial consent, quote
  distortion, audience overgeneralization, cherry-picking, inconsistent offer terms, dead
  links, vendor-only citations. (Plus the standing stop-slop pass.)
- **CRM workflows:** duplicate entry, re-entry, stale tags, opt-out bypass, races, webhook
  replay, failed branches, manual overrides, contact-state corruption.
- **Documents/media:** wrong file, stale version, hidden metadata, broken exports, visual
  clipping, missing alt text, caption mismatch, spoken-vs-on-screen-vs-linked divergence.

Pre-mortem prompt (a tactic, not evidence): "Assume this passed review and harmed a
customer 30 days later. List the plausible causal chains; test the first observable link
in each."

## 5. The claim ledger

Every load-bearing claim, atomically: claim ID + exact location; one proposition; type
(internal fact / external fact / calculation / inference / forecast / testimonial / vendor
claim); source (primary URL or artifact path); access time; support (exact excerpt, field,
command output, calculation); independence (primary / independent secondary / same-party
repetition / circular); status (supported / contradicted / mixed / stale / unverifiable /
not checked); one-line confidence limit. Rules: primary sources for product behavior, law,
and account data; vendor marketing tagged even from the official site; circular sourcing
detected; calculations recomputed with units; verify the claim AS WRITTEN, not a nearby
weaker one. And for findings about files: a CONFIRMED finding carries path + line number +
the verbatim string, checked with a mechanical grep before it is accepted; a REFUTED
finding carries the artifact's hash and vintage, because a negative grep across a stale
copy is not absence from the record.

The ledger is not a filing exercise. For the load-bearing subset, open the cited source
and compare its exact excerpt against the artifact's claim before writing "supported": a
citation nobody opened is "not checked", however authoritative it looks. Where the source
cannot be reached from this role (a URL, with no web access in the verifier's toolset),
use an excerpt the dispatch supplied or record "unverifiable" - the citation's existence
is never evidence of its content. (A claim marked SOURCE UNREACHABLE in the report body
carries ledger status "unverifiable"; they are the same condition in two registers.)

## 6. Judge protocol (when scoring against a rubric)

Decompose into independently scored criteria (no holistic score first); blind the producer
identity and expected answer; randomize and REVERSE pairwise orders - if the winner
changes, record a tie or escalate; solve checkable problems independently before grading;
provide authoritative references for factual judgments; deterministic checks break ties;
high-impact verdicts get a second judge or human adjudication with disagreement reported;
abstention is permitted - forced certainty is a defect. Calibration gold sets belong in
the regression harness.

## 7. Verdict and evidence envelope

Verdicts: **PASS / FAIL / CONDITIONAL / BLOCKED**, with **UNVERIFIED** for any requirement
whose deciding tool, credential, or source was unavailable. A pass is valid only if every
mandatory requirement is `pass` or justified `not_applicable`, required commands produced
FRESH evidence, and no critical/high finding stands unresolved. "File exists", "looks
good", and "tests should pass" are never pass evidence. A changed artifact gets a fresh
run - never reuse a prior pass because the reported defects were fixed.

Findings carry: requirement, evidence, reproduction steps, consequence, severity,
confidence, scope limits. For high-stakes artifacts, emit the machine-readable envelope
alongside the report: artifact {path, hash, observed_at}, contract sources, verdict,
per-requirement status + evidence, executed commands with exit codes, findings, coverage
limits, unresolved items, rerun instructions.

## 8. Standing rules that outrank convenience

"No confirmed issues" is a valid, expected outcome - never invent changes to justify the
review (verify-before-delivery rule). CONFIRMED findings are fixes; PLAUSIBLE findings are
owner judgment calls. The verifier receives artifact + criteria only. Instruments are a
floor, not a verdict: for media artifacts, a person watches every cut - automated checks
have passed defects that a human caught in seconds.
