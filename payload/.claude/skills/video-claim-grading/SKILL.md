---
name: video-claim-grading
description: Take a link to a video that pitches a business, a money-making method, a tool or an opportunity, pull its transcript, extract every claim it makes, tag each claim verified, unverified or vendor claim, then grade the opportunity on the public six-dimension rubric. Use for "is this video legit", "grade this YouTube pitch", "fact-check this reel", "should I do what this video says", or any link to a video that promises income, a business model, or a result. Analysis only; it never tells the owner to buy, join, or spend.
---

# Video claim grading: what the video alleges, checked and graded

A video that promises income is a business plan with the numbers left out and the camera left
on. This skill treats it as one. The transcript is the brief, every sentence that asserts a
fact or a result is a claim, each claim is tagged by what backs it, and the opportunity the
video describes is graded on the same rubric the base product uses for the owner's own plans.
The output is a scorecard plus a claim ledger, so the owner can see not just the grade but
which claims carried it and which were the presenter's word alone.

Two things it is not. It is not a verdict on the presenter's honesty: a claim tagged
unverified is a claim nobody checked, not a lie. And it is not advice: the last line is a
stress-test result, and the decision to act stays the owner's.

## 1. Get the transcript in

Load `video-to-skill` first: its section 1 carries the three routes (a `/watch` plugin when
installed, captions through `yt-dlp`, or a local file through `ffmpeg` and a local Whisper),
the update-first rule when a download is refused, and the frames discipline. Use the route
that works on this machine, in that order. Record which route produced the transcript and
whether the transcript is native captions, auto-generated captions, or a local transcription,
because the tag on a quoted claim depends on it: auto-generated captions mishear numbers.

Platform note. Public YouTube is the reliable case. Other platforms (Facebook, TikTok,
Instagram, X) vary in what a downloader can reach and in what their terms allow; when a
link is not YouTube, say so before starting, attempt the download once, and if it is refused
ask the owner for a local file rather than trying workarounds. Never log in to a platform
to fetch a video.

Rights. The transcript is read for analysis and quoted in short excerpts in the ledger. It
is not republished, and the skill never writes a derivative product from someone else's
video.

## 2. Build the brief the rubric can grade

From the transcript, write a brief of at most 300 words in the same shape `/grade-idea`
uses: what the video says the business or method is, who pays whom for what, the numbers
the video states (revenue, cost, time, conversion, price of any product being sold), what
the presenter says the operator needs (skills, hours, money), and what the presenter is
selling, if anything. Every sentence in the brief cites a timestamp. Nothing enters the
brief that the video did not say.

## 3. Extract the claims into a ledger

List every claim that would move a rubric score. For each row:

| # | Timestamp | Claim, quoted or closely paraphrased | Type | Tag | Basis |
|---|---|---|---|---|---|

Types: **result** (an income, a growth figure, a conversion), **cost** (what it takes),
**market** (demand, competition, who buys), **mechanism** (how the method works),
**operator** (what you need to be or have), **offer** (what the presenter sells you).

Tags, from the grading rule, applied the same way to every row:

- **verified**: checked this run against a named outside source, with that source in Basis.
  A video's own screenshot of a dashboard is not verification.
- **unverified**: plausible, unchecked. The default for almost everything a video says.
- **vendor claim**: the presenter, the platform, or the product being pitched is the source
  of the number, and that source profits if the claim is believed. A presenter's own income
  figure in a video that sells a course is a vendor claim. So is a tool's own case study.

Then the three tells, each answered yes or no with the timestamp: does the video sell
something (a course, a community, an affiliate link, a tool), does it show the costs beside
the results, and does it state a time frame for the results it shows. These are not scores.
They are context the advisors receive with the brief.

Verification budget. Check the claims that carry the grade, not all of them: the headline
result, the cost of entry, and whether the market exists. Use the researcher for anything
that needs retrieval; WebSearch and WebFetch for public facts; never the in-app browser
pane. If a claim cannot be checked in the time available, it stays unverified and the
ledger says so. Jurisdiction-specific claims (what is legal, licensed, taxed, or requires
disclosure in a named place) go through the researcher before they count for anything, and
until then are labeled unverified local-law assumptions naming the place.

## 4. Grade it

Run the `/grade-idea` procedure on the brief from step 2, with one addition to the advisor
dispatch: the claim ledger's tag counts and the three tells go in with the brief, and the
dispatch says "every number in this brief is from a video; its tag is in the ledger; a
vendor-claim number cannot raise a score above what an unverified one would." The five
advisors run on their pinned mid-tier model; consolidation stays here. The scorecard block
is the `/grade-idea` block with one extra line under the idea:

```
Source: <video title>, <channel>, <URL>, <duration>, transcript via <route>
Claims: <n> total, <n> verified, <n> unverified, <n> vendor claim
```

Save the scorecard to `outputs/video-scorecard-<slug>.md` and the ledger beside it as
`outputs/video-claims-<slug>.md`.

## 5. Close

End with the `/grade-idea` closing lines and one more before them, fixed: "This graded what
the video alleges, not what the presenter earns. A claim tagged unverified is unchecked, not
false." Then stop. Never recommend buying what the video sells, never recommend against the
presenter by name, and never invent a fact to fill a gap the video left.

## Composes with

- `video-to-skill` for the ingestion routes and the frames discipline (load first).
- `/grade-idea` for the rubric, the advisor dispatch, and the scorecard.
- `stop-slop` on the ledger prose and the scorecard notes before they are called done.
- `fresh-context-verification` when the owner asks for the ledger to be checked.
