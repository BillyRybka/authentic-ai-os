---
name: vid-structure
description: Build the Tier 1 outline for one video. Mines the brain-dump against the locked angle, filters core lessons from tangents, maps surviving material to the format's body shape (segments, narrative arc, cycles), surfaces block candidates per segment (frameworks, stories, proofs, metaphors from brain-dump + banks), and plans the cross-segment tension graph (title-promise location, threads, handoffs). Writes script.md with material-anchored segment purposes and bullet-level outline notes ready for vid-segment to write the prose. Standalone OR invoked by vid-pipeline after framing + packaging lock. Phrases like "structure this video", "build the outline", "plan the body", "what segments should this have", "mine the brain dump into segments", "build the skeleton", "I'm ready to outline this", "lay out the script", or any pipeline that needs the body skeleton before per-segment writing should fire this skill.
---

# Video Structure Builder

Builds the Tier 1 outline for one video. Takes raw brain-dump material plus the locked framing decisions and produces a working rough draft: material-anchored segment purposes, block candidates per segment, cross-segment tension graph. Hands off to vid-segment for Tier 2 (word-for-word prose).

**Scope boundary:** this skill produces THE outline only. It does NOT write titles (`vid-title`), thumbnails (`vid-thumbnail`), intros (`vid-intro`), segments (`vid-segment`), or endings (`vid-ending`). It does not re-litigate the angle (`vid-framing`) or re-derive iceberg alignment (`vid-intake`).

## What this produces

`content/pieces/{slug}/script.md` with the outline skeleton: `## Intro` (empty, vid-intro fills), format-native body sections (each with one-line purpose anchored in brain-dump material + bullet outline + block candidates listed), `## Ending` (empty, vid-ending fills), and `## Blocks to capture` (the consolidated list of blocks the script needs that the banks do not have yet).

`content/pieces/{slug}/piece.md` frontmatter updates: `status: drafting` (the outline locks, writing begins), `segment_purposes` (material-anchored list), `segments_completed: []` (initialized empty; vid-segment appends to it as each body segment locks), `tension_plan` (title-promise location + active threads), `last_updated: {today}`.

## When to run this

- The creator has run vid-intake + vid-framing on a brain-dump and is ready to outline the body
- The creator wants to re-structure an existing piece (the first outline didn't hold)
- vid-pipeline (future) invokes after framing + packaging (title + thumbnail) lock

## Prerequisites

Hard requirements:
- `content/pieces/{slug}/brain-dump.md` exists with raw material AND `iceberg_aligned: true`
- `content/pieces/{slug}/piece.md` exists with `selected_angle`, `core_payoff`, `format`, `goal`, `viewer_stage` (all written by vid-framing)
- `foundation/creator-foundation.md` exists (iceberg + avatar, for lane and voice context; alignment was already locked at intake)
- `knowledge/format-planners/{format}.md` exists for the locked format

Soft requirements (used when present, never blockers):
- `content/pieces/{slug}/thumbnail-brief.md` (informs which lessons need on-screen demos)
- `foundation/packaging-system.md` (informs default segment count by format)
- `banks/story-bank/`, `banks/proof-bank/`, `banks/metaphor-bank/`, `banks/framework-bank/`, `banks/testimonial-bank/` (queried for block candidates per segment)

## Invocation modes

**Standalone:** creator invokes directly with a slug ("structure the ADHD planning piece"). Skill loads inputs, mines brain-dump, surfaces outline proposal, locks, writes script.md.

**Sub-skill:** vid-pipeline invokes after vid-framing (and packaging) completes. Caller passes the slug; skill skips the "which piece?" prompt. Returns a status packet on completion (`{status: drafting, segment_count, threads}`).

**Re-structure mode:** detected when piece.md already has `segment_purposes`. Surface the prior segment purposes and ask: "Re-structure from scratch, or refine the existing outline?" Don't discard prior segment_purposes unless the creator says so. They may contain locked decisions worth preserving.

## The 2 phases

### Phase 1: Mine + propose outline

This is the conversation phase. The skill behaves as a creative sparring partner. It surfaces what's in the brain-dump, where it lands, what's missing, and what threads run across.

**Silent loads** (do NOT paste into chat):

1. `content/pieces/{slug}/brain-dump.md`, the raw material plus locked intake fields
2. `content/pieces/{slug}/piece.md`, locked framing (`selected_angle`, `core_payoff`, `format`, `voice_context`, `goal`, `viewer_stage`, `outlier_anchor`)
3. `foundation/creator-foundation.md`, iceberg statement, avatar, credibility brags (lane + voice context, not re-checked against the Top 3)
4. `foundation/voice-profile.md`, the thin guardrail (fingerprint and energy, for skeleton style orientation only, no prose written here). The reference pieces in `foundation/reference-pieces/{voice_context}.md` are loaded by the prose skills, not this one. Contract in `knowledge/voice-profile-schema.md`
5. `knowledge/format-planners/{format}.md`, the body shape for THIS format
6. `knowledge/script-tension-architecture.md`, cross-segment tension flow + thread planning + handoff rules
7. `content/pieces/{slug}/thumbnail-brief.md` if present, for visual-demo cues
8. The relevant bank folders by problem-tag, brain-dump theme match: `banks/story-bank/`, `banks/proof-bank/`, `banks/metaphor-bank/`, `banks/framework-bank/`, `banks/testimonial-bank/`

**Hard friction checks during load:**

- `brain-dump.md` missing or empty → "No brain-dump for this piece. Run vid-intake first to capture the raw material."
- `piece.md` missing framing fields (`selected_angle`, `format`) → "Piece isn't framed yet. Run vid-framing first to lock the angle."
- `creator-foundation.md` missing → "No foundation docs. Run /foundation first to lock iceberg + Top 3."
- Format planner missing for the locked format → show the format value and the list of available planners.

**Step 1.1: Mine the brain-dump against the angle.**

Read every lesson, story, proof, framework candidate, and tangent in the brain-dump. Tag each one mentally:

- **Core.** Directly serves the locked angle. The viewer needs this to get the core_payoff.
- **Tangent.** Interesting but doesn't serve the angle. Likely cut.
- **Support.** Provides context, proof, parable material for a core lesson. Lives inside a segment, not as a segment of its own.
- **Combine.** Overlaps with another lesson; should merge.

Do NOT surface this tagging as a separate review step. Apply it silently during outline proposal. The creator sees the OUTPUT (lessons that survived, mapped to segments), not the tagging worksheet.

**Step 1.2: Identify the title's central question + plan tension.**

Per `knowledge/script-tension-architecture.md`:

1. **Central question.** What is the title implicitly asking? (E.g., title "How I Added 50 Pounds To My Squat In 12 Weeks" → "how did you do that?")
2. **Title-promise location.** Which segment delivers the named answer? Push it LATE in the body, past the midpoint. Earlier segments deliver pieces, not the full answer. The exact spot depends on format (News compresses, Listicle saves the named lesson for late items, Case Study lands at the Outcome beat).
3. **Threads.** Pick 1-2 threads to run across the body (the protagonist's transformation, an open claim, a teased concept). Mark which segment opens, which closes. More loops are doable but harder to honor; default to 1-2 unless brain-dump supports more.

**Step 1.3: Map material to format-native body shape.**

Load the format planner. Use the format's prescribed shape, NOT a generic "N segments" template:

- **Case Study:** narrative arc. `## Setup` → `## Problem` → `## Action` → `## Outcome` → `## Lesson + Steps`. These are story beats, not 5 abstract segments. The whole body is one parable (the story); the principle lands at the Lesson beat.
- **Listicle:** N items, each its own segment. `## Item 1: {name}` ... `## Item N: {name}`. Big arc rising to "biggest" or "most surprising."
- **Short Process:** N steps. `## Step 1: {action}` ... `## Step N: {action}`. One big parable up front (in the intro), each step runs lean principle-only.
- **Deep Dive:** 3-5 major lessons. `## Lesson 1: {concept}` ... `## Lesson N: {concept}`. Each lesson its own parable + principle.
- **News:** tight 3-part. `## What Happened` → `## Why It Matters` → `## What To Do`.
- **Roast:** per-subject reviews. `## Subject 1: {name}` ... `## Subject N: {name}`. Same internal shape per subject.
- **Interview:** per-question. `## Q1: {question}` ... `## QN: {question}`. Host pulls a through-line.

If brain-dump material doesn't map cleanly to the format's shape, flag the mismatch. Don't silently force-fit. Surface: "Your brain-dump has 11 lessons but the locked format is case-study (narrative arc, not segmented). Want to re-frame as a deep-dive, or pick the one transformation story this becomes?"

**Step 1.4: Surface block candidates per segment.**

For each segment, query banks + brain-dump for candidate blocks. Surface, don't lock. vid-segment makes the final pick when writing prose.

Per segment, list (when available):
- **Brain-dump material:** the actual lessons, stories, moments, quotes from the brain-dump that land here
- **Story candidates:** `[[story-slug]]` matches from `banks/story-bank/` by `problem_illustrated` + theme
- **Proof candidates:** `[[proof-slug]]` matches from `banks/proof-bank/` by claim being made
- **Framework candidates:** `[[framework-slug]]` matches from `banks/framework-bank/` if a creator-owned system fits, OR flag "no framework yet, vid-segment may need to invent one inline" if a principle is needed
- **Metaphor candidates:** `[[metaphor-slug]]` if an abstract concept needs clarification
- **Visual demo flag:** if the segment's parable is likely visual (per the brain-dump's actual material or thumbnail brief)

**Anti-fabrication rule:** never invent bank entries. If banks are empty for a slot, say so. Don't guess at what might exist.

**Step 1.5: Plan cross-segment handoffs.**

Per `knowledge/script-tension-architecture.md`. For each segment boundary, propose the forward-hook: what question, name, or gap does the outbound transition raise that the next segment's setup lands?

Mark in the proposal: "Segments 2 → 3 handoff: open the retention-mistake question."

**Step 1.6: Surface the outline proposal.**

Format (Listicle example):

```
OUTLINE PROPOSAL (Listicle, 5 items)

Title's central question: "What are the mistakes killing my channel?"
Title-promise location: Item 5 (the most common one, named at peak)
Active thread: the protagonist's pattern (viewer recognizes themselves by Item 3)
Handoffs: each item ends with "but wait until you see #{N+1}..." style forward-hook

## Item 1: The thumbnail mistake (the visible one)
Material: brain-dump entry on Linus's first 6 thumbnails + the click-rate data
Blocks: [[story-linus-thumbnails]], [[proof-ctr-screenshot]]
Tension role: opens easy, hooks viewer into "what's worse than this?"

## Item 2: The pacing mistake (the felt one)
Material: brain-dump on 12-min vs 18-min retention split + your own analytics
Blocks: [[proof-retention-curve]], framework candidate: pace-tension-rule (no bank match, vid-segment may invent inline)
Tension role: deepens, viewer recognizes their own pattern starts here

## Item 3: The hook mistake (the structural one)
Material: brain-dump on title-hook gap + the 6 case studies
Blocks: [[story-tom-startup]], [[story-emma-coach]]
Tension role: MIDPOINT. Viewer thinks this is the answer; not yet
Handoff: "...but the next one is the one I made for two years before someone called me out"

## Item 4: The promise mistake (the trust one)
Material: brain-dump on viewer-betrayal patterns
Blocks: [[metaphor-broken-contract]], [[proof-subscriber-churn]]
Tension role: builds toward Item 5; the "real" answer is close

## Item 5: The retention mistake (the title-promise payoff)
Material: brain-dump on the named insight + the framework
Blocks: [[framework-retention-curve]], [[proof-9-week-arc]], [[story-steve-90k]]
Tension role: the named answer the title promised; full payoff

CUTS: brain-dump entries on "scheduling tools" (tangent), "studio setup" (tangent), 
      "lighting basics" (off-angle for this video)

COMBINES: brain-dump entries on "click-rate" and "thumbnail study" merge into Item 1
```

Then ask:

> "Outline check. Pick: lock outline, swap a segment for a different lesson, merge/split segments, re-order, change which segment carries the title-promise payoff, scrap and propose again."

Wait. Loop until outline locks.

**Soft friction during outline review:**
- Brain-dump material thin for a proposed segment → "Segment 3's material is light. Want to lock with a thinner segment, route back to vid-intake to capture more, or merge it into segment 2?"
- Title-promise payoff lands in segment 1 or 2 → "This puts the named answer in segment 2 of 5. That's early-payoff territory, and most viewers will leave after segment 2. Want to push the named answer to segment 4 or restructure earlier segments?"
- No threads identified → "I don't see a thread running across these segments. They read as disconnected lessons. Want me to propose a thread, or lock as-is?"
- Bank candidates empty for a needed block → "Segment 3 wants a story block but the bank has no match for problem-2 + theme:retention. Want to skip the block, use a metaphor instead, or pause to capture a story first?"

### Phase 2: Write script.md skeleton

Once the outline locks, write the file.

**Script.md shape (Listicle example):**

```markdown
---
type: script
piece: [[piece-slug]]
status: outlined
tier: 1
last_refreshed: {today}
---

# {title from piece.md}

> Tier 1 outline. vid-intro fills ## Intro. vid-segment fills each body section. 
> vid-ending fills ## Ending. Material anchors and block candidates are surfaced
> per section. vid-segment makes the final block picks at prose-writing time.

## Intro

*To be written by vid-intro after title + thumbnail lock.*

## Item 1: The thumbnail mistake (the visible one)

**Material:** brain-dump entries on Linus thumbnails + click-rate data  
**Block candidates:**
- Story: [[story-linus-thumbnails]]
- Proof: [[proof-ctr-screenshot]]

**Bullet outline:**
- Open on Linus's first 6 thumbnails (visual contrast)
- Setup: the gap between what creators THINK is good and what data shows
- Payoff: the one rule that fixes it (one-sentence lesson)

**Tension role:** opens easy, hooks into Item 2
**Outbound handoff:** "...but wait until you see what happens when the thumbnail works and the pacing doesn't."

## Item 2: ...

[etc per segment]

## Ending

*To be written by vid-ending. CTA shape per piece.md goal.*

## Blocks to capture

*Open blocks the script needs that the banks do not have yet. Every "no match" flag from the sections above lands here. Fill them in a batch now, or inline as each segment gets written. Delete a row once its block is captured and wikilinked into its section. An empty list means the script is fully sourced.*

- [ ] Item 2 / framework: pace-tension-rule (no bank match) needed for the pacing payoff
- [ ] Item 3 / story: hook-gap example (problem-2, theme:retention) bank empty
```

**Per body section, write:**
- Section header with one-line purpose (material-anchored, not abstract)
- **Material:** what brain-dump entries land here
- **Block candidates:** listed wikilinks per category, plus "no match" flags
- **Bullet outline:** 3-5 bullets covering the parable and principle for this segment (working draft, not prose)
- **Tension role:** where this segment sits in the cross-segment arc
- **Outbound handoff:** the forward-hook into the next segment (or to ending)

Every "no match" flag you write into a section must also get a row in the `## Blocks to capture` list at the bottom of the file, tagged with the segment and block type. That list is the single record of what still needs sourcing; do not flag a gap in a section without adding its row.

**Update piece.md frontmatter:**

```yaml
status: drafting
last_updated: {YYYY-MM-DD}

segment_purposes:
  - "Item 1: The thumbnail mistake (the visible one)"
  - "Item 2: The pacing mistake (the felt one)"
  - "Item 3: The hook mistake (the structural one)"
  - "Item 4: The promise mistake (the trust one)"
  - "Item 5: The retention mistake (the title-promise payoff)"

segments_completed: []   # vid-segment appends each locked segment's label here

tension_plan:
  central_question: "What are the mistakes killing my channel?"
  title_promise_segment: 5
  active_threads:
    - "Viewer's self-recognition pattern (Items 1-3, peaks at Item 3)"
```

After save, confirm:

```
Outline locked. script.md written, piece.md updated.
- Format: {format}, {segment_count} body sections
- Title-promise payoff: segment {N}
- Threads: {count}
- Cuts: {N} brain-dump entries (logged in comment, see script.md)

Next: fill any open blocks in the `## Blocks to capture` list (batch now, or inline as you write),
then vid-intro for the opening, then vid-segment per body section, then vid-ending.
```

Title and thumbnail are already locked (packaging runs before structure). Do not send the creator back to package here.

### Phase 3: Gap-fill decision

This is the seam between the outline and the prose. The script needs its blocks (stories, proofs, metaphors, frameworks) sourced before the writing skills can pull them without fabricating.

If the `## Blocks to capture` list is empty, the script is fully sourced. Skip this and hand off to vid-intro.

If the list has open blocks, surface it and let the creator choose when to fill it:

> "The script needs {N} blocks the banks don't have yet ({e.g. a framework for Item 2, a story for Item 3}). Capture them now in one batch, or grab each one inline when you write that segment? We're about to enter the writing phase."

- **Capture now (batch).** For each open block, invoke `vid-capture` in sub-skill mode (captures one item, returns the new `[[wikilink]]`). For a framework with no bank match, load `knowledge/framework-builder.md`, run the 5-step build inline (dump → result → top 3 → shape → name), then save via vid-capture Stage F. As each block is captured, replace the "no match" placeholder in its section with the real wikilink and delete that row from `## Blocks to capture`. When the list is empty, hand off to vid-intro. Prose then gets written against complete banks, uninterrupted.
- **Inline later.** Leave `## Blocks to capture` as-is. It is the resurfacing mechanism: vid-segment reads it when writing each section and captures the open block for that segment at that moment.

Either path is fine; it is the creator's call, not an enforced gate. The only rule is that no block is silently skipped. The manifest stays the single source of truth until every row is filled or the creator consciously cuts a block (note the cut in the section it would have served).

## Conversational discipline

- **Listen during dumps.** If the creator pushes back on the outline with 3+ sentences of "actually, what I want is...", hear it all before re-proposing.
- **Sparring partner, not NPC.** Make the call with reasoning. "I'd put the named answer in segment 4 because dropping it in segment 2 is early-payoff. Override if you want it earlier; it could work if segments 3-5 add new layers." Don't just tick through phases.
- **Material-anchored purposes always.** Never propose `## Segment 3: {abstract purpose}`. Always reference actual brain-dump material the segment carries.
- **Block candidates surfaced, not locked.** vid-segment makes the final pick at prose-writing time. vid-structure's job is to expose options, not to choose.
- **Tension graph is mandatory.** Every outline names the title-promise location, at least one thread, and the handoff style. No "five disconnected lessons stacked" outlines.
- **Bulk-keep mode for experienced creators.** If the creator says "this outline is obvious, skip the loop," surface ONCE with the full proposal, lock on confirm. Don't drag a multi-round dialogue through someone who already sees it.

## Hard friction (auto-flag, stop)

1. `brain-dump.md` missing → redirect to vid-intake
2. `piece.md` missing framing → redirect to vid-framing
3. `creator-foundation.md` missing → redirect to /foundation
4. Format planner missing for the locked format → show available formats
5. Fabricated bank entries surfaced (always cite real entries; if banks empty, say so)
6. Em-dashes in productized output (brand rule)
7. Attribution leaks in productized output (no named-source language; calibration examples use niche/category descriptors only)

## Reference index

| File | When to read it |
|---|---|
| `references/brain-dump-mining.md` | Phase 1.1, how to filter brain-dump material against the angle, what counts as core vs tangent, combine criteria |
| `references/structure-conversation-examples.md` | All phases, worked dialogues for clean session, re-structure mode, narrative-format outline, format-mismatch surface |
| `knowledge/script-tension-architecture.md` | Phase 1.2 + 1.5, cross-segment tension flow, title-promise location, threading, handoff rules (shared with vid-segment + vid-pressure-test) |
| `knowledge/format-planners/{format}.md` | Phase 1.3 + 1.4, format's prescribed shape and segment defaults |
| `assets/script-skeleton-template.md` | Phase 2, the exact script.md shape to write (frontmatter + section conventions) |

## Principles (the why)

- **Outline = mined material mapped to format shape.** Not abstract headers. Material-anchored purposes are what make vid-segment work later. The prose writer needs to know which lessons land where.
- **Two tiers of writing.** vid-structure produces Tier 1 (the rough outline with bullets). vid-segment produces Tier 2 (word-for-word prose). Different skills, different tasks, different review cadences.
- **Blocks surfaced early, locked late.** Surfacing block candidates at outline time lets the creator see what's available without forcing a choice they'll regret at prose-writing time.
- **The format dictates shape, not the segment count.** Case Study isn't 5 segments. It's a narrative arc. Forcing every format into "N segments" breaks the formats that don't segment.
- **Title-promise late or it dies.** Early-payoff is the most common retention killer. vid-structure's primary discipline is pushing the named answer to 60-80% through the body.
- **Threads make scripts feel woven.** One open loop running across the body separates "lessons stacked" from "one experience."
- **Cuts are sticky.** Lessons that get cut at outline time get logged (as a comment in script.md) so they don't re-surface in re-structure runs. The creator's "no" stays "no" unless they re-open it.

## Related skills

- The `/foundation` chain produces `creator-foundation.md` (iceberg, Top 3, avatar), this skill reads
- `vid-intake` produces `brain-dump.md`, this skill mines
- `vid-framing` produces `piece.md` framing fields (`selected_angle`, `format`, `goal`, `viewer_stage`), this skill reads
- `vid-thumbnail` produces `thumbnail-brief.md`, this skill reads (soft) for visual-demo cues
- `vid-title` locks the title in the packaging phase (after framing, before structure), NOT invoked from this skill
- `vid-intro` fills `## Intro` in the script.md this skill writes
- `vid-segment` fills each body section in the script.md this skill writes; reads `segment_purposes` + bullet outline + block candidates from this skill's output
- `vid-ending` fills `## Ending` in the script.md this skill writes
- `vid-pressure-test` audits the full script against `script-tension-architecture.md` (the same file this skill plans against)
- `vid-pipeline` (future) sequences this skill after framing + packaging
