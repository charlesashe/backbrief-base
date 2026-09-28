# Backbrief: product definition

Created 2026-09-27 from Charles Ashe's restructure of Backbrief into a product line. Status: scaffold.
Nothing here has shipped. Version 0.1.0 is reserved for the first release.

**One line:** The base product: grade the plan before you build it.

## In scope

- The Council framework: five advisors, blind peer review, a chairman, the clash (/council).
- The CEO loop: /intake a plan or a money-making idea, /business-plan, /grade against the public six-dimension rubric, /approve. /grade-idea and /critique for the quick pass.
- Video claim grader (NEW): paste a link to a video that pitches a business or money-making opportunity; the transcript is pulled, every claim is extracted and tagged verified, unverified or vendor claim, and the opportunity is graded on the same rubric.
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
| orchestrator | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\orchestrator.md` |
| planner | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\planner.md` |
| builder | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\builder.md` |
| reviewer | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\reviewer.md` |
| runner | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\runner.md` |
| verifier | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\verifier.md` |
| researcher | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\researcher.md` |
| advisor-contrarian | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-contrarian.md` |
| advisor-first-principles | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-first-principles.md` |
| advisor-expansionist | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-expansionist.md` |
| advisor-outsider | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-outsider.md` |
| advisor-executor | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\agents\advisor-executor.md` |

### Commands

| Command | Status | Source |
|---|---|---|
| handoff | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\handoff.md` |
| pickup | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\pickup.md` |
| next | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\next.md` |
| setup | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\setup.md` |
| verify-install | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\verify-install.md` |
| bb-status | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\bb-status.md` |
| demo | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\demo.md` |
| intake | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\intake.md` |
| business-plan | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\business-plan.md` |
| grade | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\grade.md` |
| approve | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\approve.md` |
| council | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\council.md` |
| critique | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\critique.md` |
| grade-idea | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\grade-idea.md` |
| find-gap | LIFTED 2026-09-28 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\commands\find-gap.md` |
| grade-video | BUILT 2026-09-27 in payload/.claude | |
| pick-niche | BUILT 2026-09-28 in payload/.claude | |

### Skills

| Skill | Status | Source |
|---|---|---|
| stop-slop | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\stop-slop` |
| fresh-context-verification | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\fresh-context-verification` |
| bb | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\bb` |
| session-team | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\session-team` |
| discovery-interview | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\discovery-interview` |
| market-validation | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\market-validation` |
| unit-economics | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\unit-economics` |
| monetization-path-selection | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\monetization-path-selection` |
| decision-memo | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\decision-memo` |
| experiment-designer | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\experiment-designer` |
| risk-register | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\risk-register` |
| competitive-analysis | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\competitive-analysis` |
| video-to-skill | LIFTED 2026-09-27 into payload/.claude | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\skills\video-to-skill` |
| video-claim-grading | BUILT 2026-09-27 in payload/.claude | |
| niche-picker | BUILT 2026-09-28 in payload/.claude | |

### Rules

| Rule | Status | Source |
|---|---|---|
| escalation | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\escalation.md` |
| constraints | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\constraints.md` |
| verify-before-delivery | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\verify-before-delivery.md` |
| token-discipline | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\token-discipline.md` |
| handoff-checklist | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\handoff-checklist.md` |
| session-hygiene | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\session-hygiene.md` |
| context-first | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\context-first.md` |
| decision-log | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\decision-log.md` |
| agent-routing | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\agent-routing.md` |
| skill-routing | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\skill-routing.md` |
| grading | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\grading.md` |
| ceo-gate | lift from archived payload | `C:\business\vault\_archived\backbrief-2026-09-27\business-os\kit\.claude\rules\ceo-gate.md` |

## Open questions for this product

- Standalone or add-on: does this product ship its own core team (orchestrator, builder, runner,
  verifier, reviewer, researcher) so it works alone, or does it require the base product? The
  scaffold assumes standalone with a shared core, so a buyer of one product gets a working system.
- Price: owner's decision. No number appears here until Charles names it.
- Third-party skills keep their per-folder LICENSE file when lifted (THIRD-PARTY-LICENSES.md in the payload).
