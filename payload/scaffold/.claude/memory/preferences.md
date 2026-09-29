# Preferences

How you want the team to work with you. Edit any line by hand, or just say what you want changed and it will be updated for you.

guidance: guided
guidance-confirmed: no
project-type: business

## What these mean

**guidance** is how much the team drives.

- `manual`: it names the next step and runs nothing. For when you know the loop.
- `guided`: after each step it says what is next and offers to run it. One word to continue. This is the default.
- `auto-prep`: it runs the cheap preparation steps (`/setup`, `/intake`, `/business-plan`) without asking, then stops before `/grade` because that one is expensive, and always stops at `/approve` because that decision is yours.

No setting ever skips an approval, an outward action (sending, publishing, spending, granting access), or a new grading loop. Those always stop for you. Type `/next` any time to see where you stand.

**guidance-confirmed** is whether you have actually been asked. Setup starts everyone on `guided` without asking, because the question only makes sense once you have seen the team work. While this reads `no`, /next asks you the pace question once after your first real unit of work, records your answer, and flips this to `yes`.

**project-type** is `business` (run through the CEO loop: /intake, /business-plan, /grade, /approve) or `build` (state a goal and the team plans, builds, and verifies it).
