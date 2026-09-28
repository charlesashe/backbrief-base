---
description: Find gaps in a market by reading real complaints, then checking whether anyone is actively looking for a fix. Discovery, not validation.
---

Run FIND-GAP MODE on the industry, product type, or audience the user named.

If the invocation carries no subject, ask exactly one question and wait: "What should I look into? An industry, a product type, or an audience all work, as specific as you can make it. For example 'commercial HVAC contractors' or 'home espresso machines'." Ask it once. No menu, no interview, and never guess a subject.

If the subject is very broad, run it anyway and say in the limits paragraph that a broad subject returns shallow evidence. Narrowing is the user's call, not a second question.

This command needs nothing but that subject. No plan document, no prior run, no other file in this project.

1. SCOPE: write one line naming what is being searched: the subject in the user's words, and the group whose complaints count. Show it before dispatching, so a wrong reading costs one correction instead of a whole run.

2. DISPATCH THE RESEARCHER, ONCE: one subagent, the researcher, on its pinned mid-tier model (token-discipline rule). It runs both halves and returns one structured block. Do not widen with a second dispatch, and do not run searches alongside it. Re-dispatch at most once, and only when the return is malformed or carries fewer than three candidates; if the second return is no better, report what came back and say plainly that the scan was thin. Use this dispatch prompt, brackets filled:

   > You are running a two-part market scan on: [scope line from step 1].
   >
   > PART ONE, COMPLAINTS. Search public places where this group talks: community forums and threads, product and app reviews, question-and-answer sites, trade and association boards, comment sections under relevant videos and articles, and the support forums of products they already use. Collect real, posted complaints. For each one you keep, record the complaint in the poster's own words as a direct quote, the venue it came from with a URL where one exists, and the date of the post where one is visible. Drop any quote you cannot source that way rather than paraphrasing it into the output. Never attribute a quote to a named individual: name the venue, never the person. Group what you find into three to five distinct recurring problems.
   >
   > PART TWO, DEMAND, run once per problem. Search for whether people are actively trying to solve it: requests for recommendations, comparison and roundup threads, "has anyone found", "what do you use for", and people describing what they already tried. Then find what exists for it now, name those products or services, and quote what people say is wrong with them. Return exactly one of three states per problem: NO SEEKERS (nobody is looking, which points at no demand rather than at a gap), SEEKERS SATISFIED (people are looking and finding something that works), SEEKERS FRUSTRATED (people are looking and what they find disappoints them).
   >
   > Keep the whole search bounded: roughly two to four searches for part one, and one to two per problem in part two. Stop when the same complaints start repeating. Repetition across independent sources is the signal, and searching past it buys nothing.
   >
   > Return only this, per problem: the problem in one line; two to four sourced complaint quotes, each with venue, URL, and date; the demand state; the existing options by name with one sourced quote on why they disappoint; and the number of independent venues the complaint appeared in. Tag every item as verified (you have the source and can quote it), unverified (plausible, you could not source it), or vendor claim (the source sells something). Add nothing else. Do not rank, do not recommend, and never invent a quote, a URL, or a date. If a part came back empty, say it came back empty.

3. RANK: order the problems into three to five candidate gaps, on three things in this order: the demand state (SEEKERS FRUSTRATED outranks SEEKERS SATISFIED, which outranks NO SEEKERS), the number of independent venues the complaint appeared in, and how recent the sourced posts are. State the basis in one line. Drop nothing the researcher returned. A NO SEEKERS candidate ranked last is a finding, not a failure: it is the demand test doing its job.

4. TAG THE EVIDENCE: use these three tags and no others, because they are the grading rule's and reusing them keeps one vocabulary across the ladder:

   - verified: checked against a named source. Quote, venue, and date are all present, so it is established that somebody posted this.
   - unverified: plausible, unchecked. No source was produced.
   - vendor claim: the source sells something. A complaint quoted on a competitor's own comparison page is tagged this way.

   The tag applies to the claim the evidence is being used for. A quote with a URL and a date is verified evidence that one person said this. It is never verified evidence that the complaint is widespread, and nothing in a run may be tagged that way.

5. CONFIDENCE: one line per gap, from exactly these three values, each with its basis stated: strong signal (the same complaint sourced in three or more independent venues, at least one post inside the last year, demand state SEEKERS FRUSTRATED); mixed signal (sourced, but thin on venues, dated, or the demand state is unclear); weak signal (one venue, or no seekers found). No percentages and no scores.

6. REGULATED ACTIVITY: if serving a candidate plainly requires a licence, a registration, or a regulated disclosure (money, health, law, insurance, food, childcare, transport), add one line naming the regulated activity and labelling it an unverified local-law assumption. Do not state what the law requires. Nobody retrieved it.

7. RENDER the block below, fixed width so it screenshots. Fill every bracket, keep the labels and the row order, repeat the gap block once per candidate, and reproduce the closing paragraph verbatim, every run, never shortened, never softened, never moved above the gaps, and never dropped because a run went well.

```
GAP SCAN
Subject: <the subject in the user's words>
Searched: <one line naming the kinds of places that were read>
Ranked on: <the ranking basis>

GAP 1  <short name>
  The complaint      <one line>
  Heard in           <venues>, <N> independent venues
  Evidence           "<verbatim quote>"
                     <venue> | <URL> | <date> | <tag>
                     "<verbatim quote>"
                     <venue> | <URL> | <date> | <tag>
  Demand             <NO SEEKERS | SEEKERS SATISFIED | SEEKERS FRUSTRATED>
  What exists now    <named options>
                     why it disappoints: "<quote>" <venue> | <tag>
  Confidence         <strong | mixed | weak> signal, because <basis>
  [Regulated         <activity>. Unverified local-law assumption; nobody checked it.]

GAP 2  <short name>
  ...

WHAT THIS IS AND IS NOT
Complaint mining reads what people chose to post in public. That over-represents the
people who were angry enough to write and comfortable enough online to post it, and it
says nothing at all about the people who had the same problem and never posted. The
demand check is a judgment made from a handful of threads, not a measurement of demand.
Nothing here establishes that anyone will pay for a fix, only that some people said
something was broken.
```

8. SAVE to `outputs/gap-scan-<slug>.md`, slug being a short lowercase hyphenated form of the subject. Create `outputs/` if absent. If the name is taken, add a numeric suffix instead of overwriting: a previous scan of the same subject is what a new scan is worth comparing against.

9. CLOSE. Exactly the first line below, then two offers, then wait:

   - What this run did not do: "This scan found complaints and sourced them. It did not grade anything, and a complaint is not evidence that anyone will pay."
   - "Running `/grade-idea` on the top gap scores it against the public six-dimension rubric."
   - "Or I can write a gap into your business brief, so `/intake`, `/business-plan`, and `/grade` run off it without you retyping any of this. Tell me which gap." Do not pick one for them.

10. BRIEF PRE-FILL, only after the user names a gap in response to step 9.

    Copy `templates/business-brief-template.md` to `outputs/business-brief.md` and fill exactly the parts in the table below, leaving every other placeholder untouched so `/intake` still asks for it.

    | Template part | Filled by `/find-gap` | With what |
    |---|---|---|
    | `# Business Brief: <name>` | YES | a short name for the gap |
    | the date line | YES | today's date, and `Produced by /intake.` is replaced by `Started by /find-gap from a complaint scan. Complete it with /intake.` The file never claims an intake that has not happened. |
    | `## The idea in one paragraph` | YES | the gap, who has it, what they use now and why it disappoints them, ending with a pointer line naming `outputs/gap-scan-<slug>.md` as where the evidence sits |
    | `## Who pays, and for what` | PARTIAL | the group the complaints came from, and the thing they are failing to get. The price is left out: none was found, and inventing one poisons the financial dimension of every later grade. |
    | `## What exists today` | NO | the template means the owner's own assets. A scan knows none of them. |
    | `## The operator` | NO | same reason. |
    | `## Numbers you know` | NO | same reason, and this is the section a grade leans on hardest. |
    | `## 90 days from now, done looks like` | NO | the owner's definition, nobody else's. |
    | `## Open unknowns` | YES | every question the scan could not answer. At minimum: whether these complainers would pay and how much; how many people have the problem; the mechanism behind why existing options disappoint rather than the sentiment; and the self-selected-sample limit from the closing paragraph. |

    If `outputs/business-brief.md` already exists, do not overwrite it. Say it exists, say what it is about, and ask. On a yes, copy it beside itself as `business-brief.backbrief-backup-<date>.md` first, and say where the backup is. Finish with one line: the brief is started, and `/intake` completes it. Never run `/intake`, `/business-plan`, or `/grade` from this command. Offer and wait.

Bans, all absolute: never invent, complete, or adjust a quote, a URL, a date, or a venue. Never present a paraphrase as a quotation. Never name or describe an identifiable person from a thread, and never reproduce contact details. Never contact anyone found in a source, never post, never sign up for anything, and never spend money: this command reads public pages and writes local files, and nothing else (escalation rule). Never call the result validated, validated demand, or market research. Never claim a complaint is common, widespread, or growing beyond the venues actually cited. Never reference a command this kit does not ship.

Obey the constraints rule: make claims measurable, and state assumptions rather than smoothing over them.
