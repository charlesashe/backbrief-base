# Backbrief: product definition

Created 2026-09-27 from Charles Ashe's restructure of Backbrief into a product line. Status: payload
assembled 2026-09-28 (plan unit 3), unreleased. Version 0.1.0 is reserved for the first release.

**One line:** The base product: grade the plan before you build it.

## In scope

- The Council framework: five advisors, blind peer review, a chairman, the clash (/council).
- The CEO loop: /intake a plan or a money-making idea, /business-plan, /grade against the public six-dimension rubric, /approve. /grade-idea and /critique for the quick pass.
- Video claim grader (NEW): paste a link to a video that pitches a business or money-making opportunity; it pulls the transcript, tags every claim verified, unverified or vendor claim, and grades the opportunity on the same rubric.
- Niche picker (NEW): for the buyer with no plan yet. Interviews for skills, hours, money and constraints, scans for gaps with /find-gap, and returns three graded candidates.
- The core team and the fresh-context verifier, so every artifact is checked before it is called done.

## Out of scope

- The operations tier (cmo, cfo, web, ops) and every execution skill. Those live in the specialized products.
- Publishing, sending, spending. The base grades and plans; it does not run the business.

## Source of components

Every component marked "lift" exists today in the archived Backbrief Business OS 3.22.0 payload at
`C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude` (or in the archived operating workspace where noted). Lifting means copying the file, then
editing its routing lines so it names only agents and skills this product ships. Components marked
NEW do not exist and are build units.

### Agents

| Agent | Status | Source |
|---|---|---|
| orchestrator | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\orchestrator.md` |
| planner | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\planner.md` |
| builder | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\builder.md` |
| reviewer | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\reviewer.md` |
| runner | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\runner.md` |
| verifier | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\verifier.md` |
| researcher | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\researcher.md` |
| advisor-contrarian | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-contrarian.md` |
| advisor-first-principles | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-first-principles.md` |
| advisor-expansionist | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-expansionist.md` |
| advisor-outsider | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-outsider.md` |
| advisor-executor | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-executor.md` |

### Commands

| Command | Status | Source |
|---|---|---|
| handoff | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\handoff.md` |
| pickup | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\pickup.md` |
| next | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\next.md` |
| setup | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\setup.md` |
| verify-install | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\verify-install.md` |
| bb-status | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\bb-status.md` |
| demo | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\demo.md` |
| intake | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\intake.md` |
| business-plan | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\business-plan.md` |
| grade | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\grade.md` |
| approve | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\approve.md` |
| council | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\council.md` |
| critique | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\critique.md` |
| grade-idea | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\grade-idea.md` |
| find-gap | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\find-gap.md` |
| grade-video | BUILT 2026-09-27 in payload/.claude | |
| pick-niche | BUILT 2026-09-28 in payload/.claude | |

### Skills

| Skill | Status | Source |
|---|---|---|
| stop-slop | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\stop-slop` |
| fresh-context-verification | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\fresh-context-verification` |
| bb | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\bb` |
| session-team | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\session-team` |
| discovery-interview | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\discovery-interview` |
| market-validation | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\market-validation` |
| unit-economics | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\unit-economics` |
| monetization-path-selection | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\monetization-path-selection` |
| decision-memo | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\decision-memo` |
| experiment-designer | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\experiment-designer` |
| risk-register | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\risk-register` |
| competitive-analysis | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\competitive-analysis` |
| video-to-skill | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\video-to-skill` |
| video-claim-grading | BUILT 2026-09-27 in payload/.claude | |
| niche-picker | BUILT 2026-09-28 in payload/.claude | |

### Rules

| Rule | Status | Source |
|---|---|---|
| escalation | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\escalation.md` |
| constraints | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\constraints.md` |
| verify-before-delivery | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\verify-before-delivery.md` |
| token-discipline | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\token-discipline.md` |
| handoff-checklist | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\handoff-checklist.md` |
| session-hygiene | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\session-hygiene.md` |
| context-first | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\context-first.md` |
| decision-log | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\decision-log.md` |
| agent-routing | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\agent-routing.md` |
| skill-routing | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\skill-routing.md` |
| grading | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\grading.md` |
| ceo-gate | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\ceo-gate.md` |

### Scaffold, opt-in layers, and the install guide

Lifted 2026-09-28 with the components above, byte-for-byte apart from product-name lines and one
routing line in the business plan template. Not rows in the tables above because they are not
agents, commands, skills or rules; they are what the commands read and write.

| Part | Status | Source |
|---|---|---|
| scaffold (context/, inputs/, outputs/, workflows/ with the plan, business plan and scorecard templates, templates/ with the business brief template, examples/ with the worked example, team/, .claude/memory/, project CLAUDE.md) | LIFTED 2026-09-28 into payload/scaffold | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\scaffold` |
| enforcement (opt-in permission rules) | LIFTED 2026-09-28 into payload/enforcement | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\enforcement` |
| memory-layer (opt-in session-recall hook) | LIFTED 2026-09-28 into payload/memory-layer | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\memory-layer` |
| status-layer (opt-in status contract that /bb-status reads) | LIFTED 2026-09-28 into payload/status-layer | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\status-layer` |
| INTEGRATION.md (merge into an existing setup) | LIFTED 2026-09-28 into payload/ | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\INTEGRATION.md` |
| .claude/VERSION (`Backbrief 0.1.0`) | WRITTEN 2026-09-28 | |
| .claude/reference-manifest.json (shipped names and hashes; /verify-install reads it) | GENERATED 2026-09-28 by `tools/manifest_build.py` | |
| .claude/skills/THIRD-PARTY-LICENSES.md (rewritten for the three MIT skills shipped) | LIFTED and edited 2026-09-28 | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\THIRD-PARTY-LICENSES.md` |

The `kit/` path references inside the payload's own text are kept on purpose: the release zip
(plan unit 5) places `payload/` contents under a `kit/` folder as the predecessor did.

## Open questions for this product

- Standalone: decided by Charles on 2026-09-27 (business brief, "Decided"). This product ships its
  own core team and works alone; the payload assembled on 2026-09-28 carries it.
- License: the predecessor shipped `LICENSE-BUSINESS-OS.md` at the download root. This product has
  no license file yet. A license is a legal commitment and is Charles's to name (escalation rule).
- Price: owner's decision. No number appears here until Charles names it.
- Third-party skills keep their per-folder LICENSE file when lifted (THIRD-PARTY-LICENSES.md in the payload).
