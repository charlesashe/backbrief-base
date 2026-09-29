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
whether the transcript is native captions, auto-generated captions, a local transcription, or
unknown (the route did not say), because the tag on a quoted claim depends on it:
auto-generated captions mishear numbers. Quote numbers from an unknown or auto-generated track
as rendered, and flag any that look misheard (one run saw "3.97" and "4.97" for likely $397
and $497).

Platform note. Each of the four platforms checked restricts automated access in its terms,
and YouTube's are not an exception. As read on 2026-09-28: YouTube's Terms of Service bar
downloading content except as the Service expressly authorizes or with prior written
permission from YouTube and, if applicable, the respective rights holders, and bar access by
automated means (robots, botnets or scrapers) except for public search engines under
robots.txt or with YouTube's prior written permission; Facebook's Terms bar accessing or
collecting data by automated means without Meta's prior permission; Instagram's Terms of Use
bar collecting information in an automated way without express permission; TikTok's U.S.
Terms bar scraping, crawling, exporting or extracting content with any automated system or
software except as approved in writing. Public YouTube is the technically reliable case, not
the permitted one, and X was not checked. For any link, tell the owner before starting that
the platform's terms restrict automated download, and offer a local file or a pasted
transcript the owner has the right to use as the first route. Attempt a download only after
the owner has heard that and says to go ahead; if it is refused, ask for a local file rather
than trying workarounds. Never log in to a platform to fetch a video. This note reports what
the terms say, not whether a particular use breaches them; terms change, so re-read a
platform's terms before relying on this line.

Rights. The transcript is read for analysis and quoted in short excerpts in the ledger. It
is not republished, and the skill never writes a derivative product from someone else's
video.

## 2. Build the brief the rubric can grade

From the transcript, write a brief of at most 300 words in the same shape `/grade-idea`
uses: what the video says the business or method is, who pays whom for what, the numbers
the video states (revenue, cost, time, conversion, price of any product being sold), what
the presenter says the operator needs (skills, hours, money), and what the presenter is
selling, if anything. Every sentence in the brief and every ledger row cites a timestamp.
When the transcript route carries no timestamps (a pasted transcript, a service that returns
plain text), cite the quoted words plus the position the presenter announces (a step, a
chapter) or an approximate position, and record in the run that timestamps were unavailable.
Never invent a timestamp. Nothing enters the brief that the video did not say. The brief may
state a gap in one sentence when the video omits something the rubric needs (a cost, a
market, a mechanism), phrased "the video does not state ...", and never fills the gap in.

## 3. Extract the claims into a ledger

List every claim that would move a rubric score. For each row:

| # | Timestamp | Claim, quoted or closely paraphrased | Type | Tag | Basis |
|---|---|---|---|---|---|

Types: **result** (an income, a growth figure, a conversion), **cost** (what it takes),
**market** (demand, competition, who buys), **mechanism** (how the method works),
**operator** (what you need to be or have), **offer** (what the presenter sells you).

Tags, from the grading rule, applied the same way to every row:

- **verified**: checked this run against a named outside source, with that source in Basis.
  A video's own screenshot of a dashboard is not verification. Verified requires the source
  itself to have been read: a figure taken only from a search-result summary, because the
  source page returned an error, stays unverified, and Basis says the page was not reached.
- **unverified**: plausible, unchecked. The default for almost everything a video says.
- **vendor claim**: the presenter, the platform, or the product being pitched is the source
  of the number, and that source profits if the claim is believed. A presenter's own income
  figure in a video that sells a course is a vendor claim. So is a tool's own case study.

Three cases the tags do not name, typed and tagged within the same three. A free funnel (a
free community, course or trial the presenter directs the viewer to, whether or not a paid
step is shown) is an offer row tagged vendor claim, and the first tell below answers yes. Arithmetic the presenter performs on unchecked
inputs takes the tag of its weakest input (vendor claim is weaker than unverified, which is
weaker than verified). A risk or compliance statement the presenter makes is a mechanism or
operator row tagged unverified unless it was retrieved; a jurisdiction-specific one goes to
the researcher per the agent-routing rule.

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
vendor-claim number cannot raise a score above what an unverified one would." The ledger
carries verified rows, so the dispatch also says that advisors take each row's tag as given
and may not raise a tag. The five advisors run on their pinned mid-tier model; consolidation stays here. The scorecard block
is the `/grade-idea` block with one extra line under the idea:

```
Source: <video title>, <channel>, <URL>, <duration>, transcript via <route>
Claims: <n> total, <n> verified, <n> unverified, <n> vendor claim
```

The scorecard's First move may not be to buy, join, sign up for, or trial anything the video
sells or links to. If the executor proposes that, replace it with the cheapest independent
check of the video's headline claim, and say on that line that you replaced it.

Save the scorecard to `outputs/video-scorecard-<slug>.md` and the ledger beside it as
`outputs/video-claims-<slug>.md`.

## 5. Close

End with three lines, not the `/grade-idea` closing, which assumes the owner's own idea. The
first is fixed: "This graded what the video alleges, not what the presenter earns. A claim
tagged unverified is unchecked, not false." The second: "The decision to act stays yours."
The third: "The presenter was not accused of anything." Then stop. Never recommend buying what the video sells, never recommend against the
presenter by name, and never invent a fact to fill a gap the video left.

## Composes with

- `video-to-skill` for the ingestion routes and the frames discipline (load first).
- `/grade-idea` for the rubric, the advisor dispatch, and the scorecard.
- `stop-slop` on the ledger prose and the scorecard notes before they are called done.
- `fresh-context-verification` when the owner asks for the ledger to be checked.
