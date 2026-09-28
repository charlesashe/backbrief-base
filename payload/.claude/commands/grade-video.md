---
description: Paste a link to a video that pitches a business or a money-making method. The transcript is pulled, every claim is extracted and tagged, and the opportunity is graded on the public six-dimension rubric.
---

Run VIDEO CLAIM GRADING on the link the user gave. Load `.claude/skills/video-claim-grading/SKILL.md` and `.claude/skills/video-to-skill/SKILL.md` first and follow them exactly.

If the invocation carries no link, ask exactly one question and wait: "Paste the link to the video (or the path to a local file), and in one line say what you want to know: whether to do what it says, whether its numbers hold, or something else." Do not run a multi-question interview.

Order of work, no step skipped:

0. STATE THE ROUTE: say which ingestion route will be tried first on this machine and whether the platform is YouTube. If it is not, say the platform's reach is uncertain, attempt once, and on refusal ask for a local file.
1. TRANSCRIPT: get it in, record the route and the caption type, and never log in to a platform.
2. BRIEF: at most 300 words, every sentence with a timestamp, nothing the video did not say.
3. LEDGER: every claim that moves a score, typed and tagged verified, unverified or vendor claim per the grading rule, with the three tells answered. Check the headline result, the cost of entry and the market claim; leave the rest unverified and say so. Jurisdiction-specific claims go through the researcher or are labeled unverified local-law assumptions naming the place.
4. GRADE: the `/grade-idea` procedure on the brief, with the ledger and tells in the advisor dispatch and the instruction that a vendor-claim number cannot raise a score above an unverified one.
5. SAVE: `outputs/video-scorecard-<slug>.md` and `outputs/video-claims-<slug>.md`.
6. CLOSE: the fixed line "This graded what the video alleges, not what the presenter earns. A claim tagged unverified is unchecked, not false." then the `/grade-idea` closing lines, once.

Bans, all absolute: never recommend buying what the video sells; never accuse the presenter; never call a claim false because it is unchecked; never invent a number, a cost, or a mitigation the video did not state; never present a passing grade as a prediction of income.

Obey the constraints rule: make claims measurable; mark every unverified assumption as one.
