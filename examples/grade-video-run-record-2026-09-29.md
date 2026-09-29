# /grade-video run record, 2026-09-29

Real pitch videos graded in an installed copy of the base product, following `.claude/commands/grade-video.md` step by step.

## The videos

All on YouTube. Views, subscribers and length are vidIQ search-result figures (vendor claim, read 2026-09-29).

| Slug | Id | Channel | Published | Length | Views | Subscribers |
|---|---|---|---|---|---|---|
| erhart-ai-agency-blueprint | XGWSm03C6RQ | Adam Erhart | 2026-04-03 | 13:12 | 10,188 | 727,000 |
| kvk-boring-automations | g1kLhDwOB54 | KVK AI | 2026-09-24 | 5:19 | 115 | 1,220 |
| pavlo-10k-asap | sXBDL9bvyhE | Pavlo | 2026-08-09 | 11:47 | 10,864 | 131,000 |

## Route

The owner pulled each transcript through vidIQ, a licensed service: the skill's "pasted transcript the owner has the right to use" route. The `yt-dlp` download route was not run, because every platform checked restricts automated access and the skill says to offer a licensed or local route first. Nothing was fetched from a platform or logged in to. vidIQ returns plain text with no timestamps and does not say whether captions are native or automatic.

Local-file route: `ffmpeg` and Whisper ran end to end on a 22-second clip with no speech. Nothing was graded from it. No full-length pitch video exists on this machine.

## Grades

| Video | Average | Grade | Lowest | Reachability (trial) |
|---|---|---|---|---|
| Erhart | 3.8 | C | Risk coverage 2.6 | 4.0 |
| KVK AI | 3.2 | C | Risk coverage 1.8 | 1.5 |
| Pavlo | 3.2 | C | Risk coverage 2.2 | 4.3 |

## Findings for the product

Paths are in the installed copy. Nothing was changed.

1. **No timestamps.** `commands/grade-video.md` step 2 ("every sentence with a timestamp"); `skills/video-claim-grading/SKILL.md` section 2 ("Every sentence in the brief cites a timestamp") and the ledger's Timestamp column. This run cited quoted words plus a step or third of the video. The skill needs that form.
2. **Caption type unknown.** SKILL.md section 1 ("whether the transcript is native captions, auto-generated captions, or a local transcription") has no value for "the service does not say". One transcript renders likely $397 and $497 as "3.97" and "4.97".
3. **A refused fetch.** SKILL.md section 3 defines verified as "checked this run against a named outside source". The SBA page returned HTTP 403; the figure came from a search summary. The skill does not say what tag that earns.
4. **Dispatch contradicts the ledger.** `commands/grade-idea.md` step 2 says "nothing gets called verified here"; SKILL.md section 4 adds only the vendor-claim sentence. The run had to state that ledger tags govern and that "the user" means the operator the video describes.
5. **First move versus the ban.** `grade-idea.md` step 4 takes the first move "from the executor's own answer"; `grade-video.md` bans recommending what the video sells. The run added a dispatch line, and one executor still proposed "HighLevel's free materials".
6. **Tag rule gaps.** SKILL.md section 3: a presenter whose only offer is free (KVK AI) is not covered by "sells a course"; arithmetic that holds on unchecked inputs has no tag; risk and compliance statements have no type.
7. **Brief rule.** SKILL.md section 2 ("Nothing enters the brief that the video did not say") does not say whether a stated gap is allowed. The graded Erhart brief carried "the agency pays for software", which the video never says; the saved copy is corrected.
8. **Closing lines.** `grade-idea.md` steps 5 and 6 ("adding detail to the description", "if the idea is worth a real plan") assume the owner's own idea.
