---
name: discovery-interview
description: Interview the owner one question at a time about a business, a plan, a product or a decision, recording each answer on disk before the next question is asked, so a session that ends early still leaves a complete file in context/discovery/. Use when the owner wants to be questioned about something they know and have not written down ("grill me", "get this out of my head"), wants a plan or a design questioned until it holds, or before /intake or /business-plan when the brain dump would be thin. Never invents an answer; what the owner cannot answer is recorded with the name of who can.
---

# Discovery interview

Most of what a business knows about itself sits in the owner's head and in no file. A form
does not get it out, and a brain dump gets it out in the wrong order with the gaps hidden. An
interview does: the agent asks, the owner answers, the answer goes to disk, and the next question
is chosen from what the last answer settled. The file at the end is what the session was for. It
is the input `/intake` and `/business-plan` should have had all along.

## Provenance

The interview-and-checkpoint pattern is in general circulation among Claude Code users; at least
two public "grill me" skills describe it, neither under a license, and Nate Herk demonstrates it
in "Turn Claude Into a One Person Marketing Team in 38 Mins" (YouTube, published 2026-08-21,
watched in full 2026-09-02: captions and frames) as the step that fills a marketing project's
context before any asset is generated. What Backbrief takes from those sources is the idea: one
question at a time, written down as it is answered. The procedure below, its structure, its file
shape and its wiring into Backbrief's commands and gates are Backbrief's own, and the public
skills' sentences do not appear here. The set of context notes offered at the close is the set
Herk shows on screen, described in Backbrief's words.

## Where it sits in Backbrief

`/setup` asks a short set of questions to fill the two strategy files. `/intake` takes a brain
dump and asks at most five batched questions on the way to a business brief. Both start thin when
the owner has not yet said out loud what they know. This skill is the pass that goes before them:
run the interview, then hand its capture file to `/intake` as the brain dump it was waiting for.
For a plan that already exists, the interview feeds `/critique` or `/grade`; for a product or a
design, it feeds a spec in `outputs/`.

The context-first rule binds the interviewer as much as anyone. Read `context/strategy/`,
`context/reference/SOURCES.md` and whatever sits in `inputs/` before the first question. Where a
file in the project already holds an answer, the file is read and the owner is not asked; the
interview spends the owner's attention on what no file holds.

## The capture file

Path: `context/discovery/YYYY-MM-DD-<topic>.md`, folder created on first use. It sits beside the
strategy files because it is durable context, not a working note, and not an output: the briefs,
plans and specs built from it are written to `outputs/` by the commands that build them, and the
capture is the context those commands read.

Three parts, in this order, so a reader who opens it cold reads the conclusions first:

```
# <Topic>, discovery, <YYYY-MM-DD>
Purpose: <one line>

## Settled
| Topic | What the owner said | Settles |
|---|---|---|

## Open
| Question | Who can answer it | Why it matters |
|---|---|---|

## Answers, in the order given
<numbered entries: the question as asked, the inference offered, the answer>
```

"Settled" is rewritten as the session goes, so it always reads as the current synthesis. "Open"
holds what the owner could not answer, each line with a person and a reason. The third part is
the record the first two are built from, and it is never edited after the fact except to add a
note that a later answer changed it.

The file exists before the first question does. Opening the session means writing the header
(the date from the system clock, not from memory) and the three empty sections, and naming the
path once so the owner knows where to look while the interview runs.

## The cycle

Every question runs the same four beats, and the third beat is the one that cannot be skipped:

1. **Ask one thing.** Put a single question to the owner, and with it the answer the agent would
   infer from what it already knows, marked as an inference. The owner then spends a word
   agreeing or a sentence correcting instead of composing an essay.
2. **Take the answer as given.** A positioning line, a price, or a promise the owner is willing
   to make is copied verbatim, because in those the words are the decision. Other answers are
   recorded as their sense.
3. **Write before asking again.** One answer, one write: the ordered record gets its entry, the
   Settled table is rewritten, Open rows are added or cleared, and an earlier entry the answer
   overturns gets an annotation. The reason is the failure this beat prevents: an interview held
   only in the agent's context is lost the moment that context is summarized or the session
   closes, and the owner has to be asked everything again.
4. **Choose the next question from the answer**, not from a script.

An owner who cannot answer gets an Open row with a name in it and the next question. The agent
never supplies the missing fact itself, because a guess written into `context/` is read as a
fact by every agent that loads it later.

## Choosing the order

Questions have dependencies, and the interview follows them. A question whose answer depends on
something not yet settled is a question asked too early: who the buyer is comes before what the
offer costs, what hurts comes before what is promised, what the product is comes before what it
is called.

When the topic is a business or its marketing, the whole interview hangs from three answers, so
they come first:

- **The pain.** The problem the business solves, in the words the buyer would use on the day it
  hurts.
- **The person.** One describable human who has it: their situation, and what they do about the
  problem today.
- **The promise.** What the product does about that pain for that person, stated as an outcome
  they get, not a list of features.

The branches after that, in whatever order the answers open them: what the product is and is
not; the offer and its price, recorded in the owner's own words; the brand's voice and the words
it refuses to use; the proof the business already holds (numbers, quotes, screenshots, and where
each one lives); the channels that exist today and their state; the constraints on time, money,
skill, and law, and anything the owner will not do; and what a good ninety days would look like.

Two things end an interview: the owner calling time, or the agent finding no branch left
without a row in Settled or Open. In the second case the agent asks one further question anyway,
about whatever the interview's own framing may have excluded, since the branch nobody raised is
the one this method cannot find by itself.

## Closing

- The last write of the session adds a `Next:` line under the purpose naming where the file goes:
  `/intake` for a business topic, `/critique` or `/grade` for a plan, a spec in `outputs/` for a
  design. Before that line is written, each Settled row is re-read against the record it came
  from, and a row a later answer overturned is corrected there.
- The owner hears the `Next:` line and the Open table with its names. Nothing longer: the file
  is the report.
- Where the interview produced positioning the strategy files do not yet hold, offer to carry it
  into `context/strategy/current-state.md`. Offer only; a file the owner has not asked to change
  stays as it is.
- Offer to split the capture into the short context notes later agents load: positioning (the
  three answers above, the promise in a long and a short form, what the product is not), the
  customer (the person, the compromise they make today, a morning in their life, the objections
  and their answers), product facts with a claims gate (what may be said, what may not, and every
  number marked unconfirmed until the owner fills it), voice (how it sounds, the words it never
  uses), and a message bank with empty proven and retired sections for the copy that later earns
  a place. The Open table becomes the project's open-questions list, and a number on that list
  does not appear on a public asset until it leaves it.

## Bounds

The interview sends, publishes and spends nothing. An inferred answer stays labelled as an
inference until the owner confirms it. Pricing is written as the owner's decision in the owner's
words and is never proposed by the interviewer. A legal, tax or licensing answer for a named
place is recorded as the owner's statement and flagged for the researcher (agent-routing rule);
the interview does not settle it.
