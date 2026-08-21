---
type: skill-reference
skill: vid-structure
step: all
last_updated: 2026-07-28
---

# Structure Conversation Examples

How vid-structure runs in real sessions. The creator sees two proposals (the rough spine, then the built-out plan) and one confirmation. The steps are internal, never announced.

## Example 1: Clean run, Listicle

**Locked at framing (piece.md):** frame "A video that shows creators which widely repeated best practices are quietly costing them retention", core payoff "spot the advice tanking your retention and what to do instead", format listicle, goal views.
**Brain-dump:** thumbnail-copying flops, a year of daily posting tanked, the 12-minute retention cliff, Linus's bad first thumbnails, best mic under $200, the "5-second hook" myth, a lighting setup, "post consistently" trains the algorithm wrong, titles that overpromise killed Tom's channel.

### The spine (step 1)

> **AI:** "Rough spine, listicle, 4 items.
>
> 1. Copying the big channels' thumbnails
>    - You copy the look, but the thing that makes theirs work is that people already know their face.
>    - Linus's first 6 thumbnails were cluttered copies. The redesign that worked ignored them.
>    - Design like the viewer has never seen your face.
> 2. The '5-second hook' myth
>    - Viewers don't leave at 5 seconds, they leave when the promise runs out.
>    - The real hook is the first 30 seconds of promise-building.
> 3. Titles that overpromise
>    - Promise more than you deliver and viewers feel lied to, so they bounce, and the algorithm reads it.
>    - Tom's channel did this for two years.
>    - Write the title after you know what you delivered.
> 4. 'Just post consistently'
>    - The most-repeated advice is the one that tanked my channel.
>    - Daily posting trains the algorithm for volume, not quality.
>    - The 12-minute cliff: 30% dropped at minute 12, across 8 videos.
>    - Cut to one strong video a week, retention climbed.
>
> Cuts logged: best mic under $200, lighting setup.
>
> Add, cut, merge, reorder?"

> **Creator:** "That's it. Lock."

### The built plan (step 2)

> **AI:** "Built plan. I moved 'post consistently' to item 4 so the most-preached advice is the late payoff. Title pays off at item 4. One thread: the viewer recognizing themselves, building to item 4.
>
> ## Item 1: Copying the big channels' thumbnails
> Parable: Visual Demo + story, Linus's first 6 on screen. [[story-linus-thumbnails]]
> Principle: a big channel's thumbnail works on recognition you don't have yet. Design for a stranger. Proof: [[proof-ctr-screenshot]]
>
> ## Item 2: The '5-second hook' myth
> Parable: Contrast, old way (nail 5 seconds) vs new way (keep a promise alive for 30). No bank block, built from the dump.
> Principle: viewers leave when the promise runs dry, not on a stopwatch. Proof: early-drop retention data -> to build.
>
> ## Item 3: Titles that overpromise
> Parable: Story, Tom's channel. [[story-tom-startup]]
> Principle: the title is a contract, break it and the bounce tells the algorithm to stop. [[metaphor-broken-contract]]
>
> ## Item 4: 'Just post consistently' (title-promise payoff)
> Parable: Story, personal, my year of daily posting and the month it tanked.
> Principle: the algorithm rewards retention, not frequency. Cut the schedule, one strong video a week. Proof: the 12-minute cliff -> to build.
>
> To build: item 2 retention data, item 4 the 12-minute cliff. Lock, or adjust an item?"

> **Creator:** "Lock."

[Step 3: script.md written with the 4 items (parable + principle each), intro and ending stubbed, a ## To build list with the two proofs. piece.md gets status: drafting, segment_purposes, segments_completed: [], the setup/payoff plan (payoff at item 4, one thread), last_updated.]

**Why this worked:** the spine got agreed before anything was built out, so the detailed proposal was fast to review. The order changed for a reason (payoff late) and the AI said why. Blocks were picked, not offered as menus. The writer picks this up and writes, no re-planning.

## Example 2: Re-structure mode

The piece already has `segment_purposes`. The creator wants to refine, not rebuild.

> **Creator:** "Re-structure the retention-mistakes piece."

> **AI:** "This one's already outlined (4 items, payoff at item 4). Refine it, or rebuild from the brain-dump?"

> **Creator:** "Refine. Item 3 doesn't have material that fits. I don't actually have a story there."

> **AI:** "Item 3's material is thin, two lines with no specifics. Options:
> 1. Cut it, item 4 becomes item 3, payoff still lands last.
> 2. Merge it into item 2 (the hook and the promise are the same problem).
> 3. Pause and capture a story for it.
> Which?"

> **Creator:** "Merge into item 2. The hook is the promise."

> **AI:** "Merged. Now 3 items, item 2 combines the hook and the promise, item 3 is the payoff. Locked?"

> **Creator:** "Locked."

[script.md merges the sections, renumbers, logs the merge in the cuts comment so a future re-structure keeps it. piece.md segment_purposes updated.]

**Why this worked:** the AI surfaced the existing spine and took the creator's diagnosis without re-mining from scratch. Prior points were preserved unless the creator cut them.

## Example 3: Format mismatch surfaced

Eleven separate lessons in the brain-dump, but the format is locked to case study (one story arc).

> **AI:** "Before I rough the spine, a mismatch. Your brain-dump has 11 separate lessons. The locked format is case study, which is one transformation story, not a list. Two routes:
> 1. Re-frame to deep-dive or listicle. Your 11 lessons group cleanly into either. That's a trip back to vid-framing.
> 2. Pick the one transformation this is really about. The other lessons become support or cuts.
> Which?"

> **Creator:** "Pick the one. The Steve story is the case study."

> **AI:** "Pulling Steve's story. The other lessons get tagged support-for-Steve or logged as cuts. Roughing the spine on the story now..."

**Why this worked:** the AI caught the mismatch before proposing a spine that would force-fit. It never silently jammed 11 lessons into a story arc, and it never re-asked the format from scratch (it proposed a switch and let the creator decide).

## Anti-patterns

- **NPC ticking.** "Mining complete, moving to the build." The steps are internal. The creator sees the spine, then the plan, then the confirm.
- **Abstract points.** `## Item 3: {second main point}`. Always name the actual lesson from the brain-dump.
- **Silent cuts.** Proposing a spine without saying what got cut. Always log cuts; the creator may know a cut is the real gold.
- **Surfacing block menus instead of picking.** The build step locks the parable and principle. It does not hand the writer three candidates to choose from later.
- **Writing prose.** This skill outlines. Full sentences belong to vid-segment.
