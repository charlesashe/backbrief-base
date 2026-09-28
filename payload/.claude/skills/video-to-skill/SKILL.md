---
name: video-to-skill
description: Watch a video and turn what it teaches into something the team can reuse - a new skill when the video carries a method, or a knowledgebase entry when it carries facts. Covers getting the content in (the claude-video /watch plugin, YouTube captions, or a local ffmpeg-plus-Whisper pipeline), the watching discipline (frames carry what audio does not; transcripts mishear), and the gates that keep a distilled skill honest (source attribution, claim tagging, rights, and verification). Trigger on watch this video, /watch, turn this video into a skill, learn this from YouTube, "make a skill from this tutorial", or any request to extract reusable knowledge from video.
---

# Video to skill: watch once, reuse forever

A video someone found useful usually carries one of two things: a METHOD (how to run a
budget, how to structure outreach, how to set up a tool) or FACTS (what something costs,
what a product does, what changed in an ecosystem). This skill turns either into a durable
asset: a method becomes a new skill the team invokes again; facts become a knowledgebase
entry the researcher cites. The watching is the easy half. The discipline that keeps the
distilled artifact honest is the product.

Every claim below about the claude-video plugin was verified against its repository on
2026-08-29 (license, install commands, dependencies, what it hands over). Ecosystem facts
like caption availability were true then too. Re-verify against the source before quoting
any of them in outward copy; tool facts age fast.

## 1. Get the content in (three routes, in order of preference)

**Route A - the claude-video plugin, when installed.** The open-source `/watch` plugin
(`github.com/bradautomates/claude-video`, MIT at verification 2026-08-29) downloads a video
from a URL, extracts scene-aware frames, produces a timestamped transcript, and hands both
over. Install is two commands in Claude Code, verbatim from its README:

```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

It depends on `yt-dlp` and `ffmpeg` (it prints the install commands per platform), prefers
a video's native captions, and needs an API key only as a transcription fallback for
videos without captions. Installing the plugin, its dependencies, or any API key is the
owner's action; verify it works by watching something short, not by reading the README.

**Route B - captions without a plugin.** Many public YouTube videos carry captions
(auto-generated where the creator added none);
`yt-dlp` can fetch them as text. Captions plus a handful of frames is often enough.

**Route C - a local file.** Strip the audio and transcribe locally, and pull frames at
intervals:

```
ffmpeg -y -i input.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav
ffmpeg -y -i input.mp4 -vf "fps=1/3,scale=304:-1" frame_%02d.png
```

A local Whisper implementation transcribes the wav (use one already present, or ask the
owner before installing). Read the frames as images alongside the transcript.

**When the download is refused, suspect your tool's age before the site's wall.** A
YouTube 403, a "requested format is not available", or an offer of storyboard images only
often means the installed `yt-dlp` is months old - updating first is that project's own
standing advice, because the site changes faster than any pinned version. Updating it (owner-approved, like any install) is the first fix, and in
the measured case it was the whole fix. Two more findings from that case: classic muxed
formats can be gone entirely, and a video-only stream is all frames need - list formats
and take one; and captions (Route B) had already delivered the full substance before the
download worked - so when captions exist, a refused download degrades the analysis
rather than blocking it (a caption-less video with a refused download IS blocked, and
the output says so). Say plainly in the output when frames were unavailable, and what
that leaves uncorroborated.

**For a long video, tile before you crop.** A contact sheet locates the screens worth
reading at full resolution, without viewing hundreds of frames:

```
ffmpeg -y -i video.mp4 -vf "fps=1/10,scale=192:-1,tile=8x10" -frames:v 1 contact.png
```

(`-frames:v 1` matters: past one sheet's worth of video, ffmpeg emits a second image and
errors on the plain filename. Size the tile grid to the duration, or make more sheets.)
Read the sheet once, note which tiles carry on-screen text (counting from 1, tile n sits
near t = (n - 1) x 10 seconds - the first tile is the start of the video), then extract
those moments full-size. On-screen prompt and code text a video
shows for a few seconds is exactly what this finds and the audio never carries.

## 2. Watch properly - the part a transcript alone gets wrong

- **The frames carry what the audio does not.** On-screen text, UI walkthroughs, README
  screenshots, the name of the thing being demonstrated - these are routinely shown and
  never spoken. Extract a full-resolution crop of any frame that matters and read it.
- **The transcript has an error rate.** Automatic transcription mishears names and
  homophones with full confidence. Never carry a proper noun, number, or quote from a
  transcript into the distilled artifact without corroborating it against the frames or a
  primary source.
- **Identify the subject independently.** Social videos routinely gate their subject
  ("comment X and I'll send it") or show it only as a blurry screenshot. Find the actual
  repository, product, or source yourself and verify against IT, not against the video.
  What the video claims about its subject is marketing; what the source says is evidence.

## 3. Choose the output shape before writing anything

- **The video teaches a repeatable procedure** (a workflow, a setup, an analysis method)
  → distill a new skill into `.claude/skills/<name>/SKILL.md`, and it becomes part of the
  team's roster.
- **The video carries facts, positions, or reference knowledge** → write a source document
  into `context/reference/` and add its row to `context/reference/SOURCES.md`. The
  researcher cites the knowledgebase first, so this is how video content starts outranking
  general knowledge.
- Do not make a skill out of facts. A skill nobody will invoke twice is a filing error;
  the knowledgebase is where one-time knowledge belongs.

## 4. Distill the skill right

- **Frontmatter that discovery can read**: exactly `name` and a single-line `description`
  that says when to trigger it. No unquoted colon-space inside the description - that
  breaks the YAML parse and the skill silently vanishes from discovery.
- **Attribute and date the source.** The skill names the video (creator, platform, date
  watched) and any repository or product it verified against, with the verification date.
  A distilled skill with no provenance cannot be re-checked when it goes stale.
- **Tag the claims.** Anything the video asserts is an unverified claim - and when the
  speaker sells the thing being praised, a vendor claim - until checked against a primary
  source. Verify every load-bearing fact (a price, a license, a command, a legal
  assertion) before baking it in; hedge or drop what you cannot verify. A skill is the
  worst place to launder a video's confidence into the team's.
- **Wrap the method in this system's gates.** The video's method arrives with none. If it
  touches money, pricing, legal exposure, sending, or publishing, the distilled skill
  restates the escalation boundary in its own text. If it produces financial, legal, or
  health guidance (the "budget my finances" case), the skill carries the same
  analysis-not-advice framing the cfo carries. Jurisdiction-specific claims route to the
  researcher, per agent-routing.
- **Verify before it joins the roster.** The generated skill is a non-trivial artifact:
  pass it to the verifier in fresh context with its acceptance criteria (frontmatter
  parses; every factual claim verified, hedged, or attributed; gates present; stop-slop),
  per verify-before-delivery.

## 5. The rights gate

Learning a method from a public video and writing your own procedure is fine. What is not:
reproducing the video's script, wording, or structure verbatim (quote at most a line, with
attribution); extracting content from paid courses, gated material, or anything the
creator sells access to; and shipping a distilled skill in a PAID product without an owner
license call - a skill derived from someone else's licensed material can carry that
license's obligations with it. When in doubt, the derived artifact stays internal and the
owner decides.

## 6. The honesty bound

A distilled skill inherits every error the video made and then speaks with the calm
authority of documentation. Two controls keep that survivable: the provenance block (so a
future reader knows exactly what this knowledge is and when it was true), and treating the
skill's first real use as a test of the method rather than proof it works. A video with
strong production values is not evidence its method survives contact with your numbers.
