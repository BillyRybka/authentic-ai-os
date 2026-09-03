---
type: reference
scope: shared
loaded_by: [vid-intro, vid-segment, vid-ending]
status: active
tags: [reference, story-pulling, banks]
---

# Story Pulling Criteria

How to pick the right story from N candidates the bank surfaces. Examples-first. Each criterion pairs a worked example (the story that landed) with a near-miss (the story that looked plausible but missed) so the boundary is clear.

This file is reference material for Claude to think with at structure-pass time when querying `banks/story-bank/*.md`. It's NOT the story capture guide. That's `knowledge/story-capture-guide.md` and lives upstream of this file.

## Why pulling matters more than capture

A bank with 30 stories is useful only if the right one gets pulled. Pull the wrong story and the segment lands flat, even if the story is technically a good story. The pulling job is matching: matching the story's emotional shape, the avatar's stage, the segment's job, and the format's tolerance.

Five criteria. They compound. A candidate that passes all five is a strong pull. One that fails 2+ should be dropped even if it's the most polished entry in the bank.

---

## Criterion 1: Stage match

The story's protagonist must be at a stage similar to the avatar's CURRENT stage, not where the avatar wants to end up.

**Worked (avatar = $10k/mo coach):**

Pulled: a story about a $12k/mo coach who lost 2 clients and kept his pricing the same instead of dropping it. Outcome: replaced both clients within 6 weeks at original rates.

Why it lands: avatar sees themselves in the protagonist. The before-state ($12k/mo) is achievable now. The after-state (replaced clients) is the next visible win.

**Near-miss (same avatar):**

Pulled: a story about a $1M/yr agency owner who restructured his delivery and 10x'd profit margins.

Why it misses: avatar can't see themselves in the protagonist. The before-state ($1M/yr) is foreign. The story might be true, dramatic, and well-told, and still fail because the stage gap is too wide. Save this one for an avatar making $250k+.

**The principle:** the protagonist's BEFORE state must be where the avatar lives RIGHT NOW. A jump of one stage forward is fine. Two stages forward and the avatar disconnects.

---

## Criterion 2: Point match

The story must illustrate the point this segment is making. Match the story's `illustrates` line and `themes` to the pain in the segment's emotional opening, by meaning, not by a fixed problem number.

**Worked (segment is teaching "you can't grow while you're buried in client work"):**

Pulled: a story whose `illustrates` line is "doing all the client work yourself is what caps your growth", where a coach was working 60-hour weeks, pulled in a contractor on one engagement, and freed 15 hours a week without dropping quality.

Why it lands: direct match. The story's lesson IS the segment's point.

**Near-miss (same segment):**

Pulled: a story whose `illustrates` line is about figuring out a pricing model. Story is great. Just doesn't make this segment's point.

Why it misses: the viewer is here for the time-and-delegation point, not the pricing one. Right story, wrong segment. Save it for the pricing segment.

**Reuse, not buckets:** the same story can pull for any segment whose point it fits. A story is not owned by one category. Match on what it illustrates and let a strong entry surface across many videos.

---

## Criterion 3: Outcome specificity

The outcome must be specific (numbers, named timeframes, named results). Vague outcomes kill the block.

**Worked:**

Outcome line in bank entry: "9 weeks later, MRR went from $42k to $74k. Steve took his first two-week vacation in 4 years."

Why it lands: two specific numbers, one specific timeframe, one specific human outcome (the vacation). Viewer can mentally model the receipt.

**Near-miss:**

Outcome line in bank entry: "Things got way better and Steve was much happier."

Why it misses: no number, no timeframe, no concrete change. Viewer has nothing to anchor belief on. Even if the segment's job allows for an emotional outcome, "much happier" is too generic. Push for the specific behavior change.

**The principle:** if the bank entry's outcome is thin, EITHER route to `vid-bank` to dig deeper before pulling, OR pick a different candidate. Do NOT make up specifics. Anti-fabrication is the gate.

---

## Criterion 4: Type match for sales-power

The story's `story_type` (client / own / viewer) should match the segment's persuasion job.

- **Client stories** carry the highest sales weight. Use when the segment's job is convincing the viewer the methodology works for someone like them.
- **Own stories** carry strong credibility weight. Use when the segment's job is establishing the creator's expertise OR when admitting the creator's failure makes the lesson land harder.
- **Viewer stories** carry the lowest weight. Use only when neither client nor own exists and the segment can't run without a story.

**Worked (sales-segment in success-story format):**

Pulled: a `client` story where the protagonist's transformation directly mirrors the avatar's desired outcome.

Why it lands: client stories remove the "of course YOU could do it" objection. Sales conversion improves measurably with client stories.

**Worked (credibility segment in deep-dive format):**

Pulled: an `own` story about the creator's costly rookie mistake from year one, the one where they tried the wrong path before finding the right one.

Why it lands: own-story-with-failure-admission builds trust. Viewer thinks "they've been where I am, and they figured it out."

**Near-miss (sales segment, viewer story pulled when client story exists):**

Pulled: a viewer story (fairy-tale framing) when a client story is in the bank.

Why it misses: viewer stories are weakest. If a client story exists for this problem, it should win. The exception: the client story has a stage mismatch. Then drop to own-story or viewer-story rather than mismatching stage.

---

## Criterion 5: Reuse hygiene

If the bank entry's `used_in:` already lists multiple recent pieces, consider whether the audience has heard this story too recently.

**Worked:**

Bank entry has `used_in: ["[[piece-from-2025-09]]"]`: one use, 8 months ago. Pulling again is fine.

Why it lands: viewers don't audit overlap. One use 8 months ago is forgotten. The story can land again.

**Worked (reuse-aware framing):**

Bank entry has `used_in: ["[[piece-1]]", "[[piece-2]]"]`: both recent. The segment pulls it ANYWAY because the segment's job specifically requires THIS story, but the prose acknowledges the reuse: "Some of you saw me tell this story last week. Here's what I didn't include then."

Why it lands: acknowledging the reuse and adding new context turns the reuse into a feature.

**Near-miss:**

Bank entry has `used_in:` with 4 recent pieces. Skill pulls it without acknowledgment.

Why it misses: regular viewers tag the repetition. Trust drops. Pull a different candidate, or acknowledge the reuse and add new framing.

**The principle:** stories CAN be reused. That's part of their bank value. But the cadence matters. If used 3+ times in the past 90 days, default to a different candidate or surface the reuse to the creator.

---

## What to do when criteria conflict

You'll often have N candidates and no single one passes all five criteria. Resolution order:

1. **Stage match wins.** A criterion-1 mismatch breaks the segment harder than any other miss.
2. **Point match second.** A story that makes a different point is a wrong-segment story.
3. **Outcome specificity third.** If the bank entry is thin, route to vid-bank or skip the block.
4. **Type and reuse are tiebreakers.** When two candidates pass 1-3, type and reuse pick the winner.

If NO candidate passes 1-3, the bank doesn't have what the segment needs. Two options:

- **Route to vid-bank** mid-skill to capture a fitting story (sub-skill mode of vid-bank). Resume the segment with the new entry.
- **Switch the block type.** Use Visual Demo (Show-the-Problem or Contrast) or Metaphor instead. The segment can still work without a story.

---

## Surfacing candidates to the creator

The skill picks the top 1-3 candidates after applying the criteria. Surface them with one-line rationale each:

```
Story candidates for this segment (the point: you can't grow while buried in client work):

1. [[steve-9-weeks-to-2-week-vacation]]: client win, MRR $42k→$74k, stage match (avatar at $50k)
2. [[anonymous-client-15-hour-week-cut]]: client win, freed 15hr/wk via contractor, stage match (avatar at 60hr/wk)
3. [[my-first-burnout-2021]]: own story, admits failure mid-arc, credibility framing

Pick one, swap the block type, or want me to pull more?
```

Three is the cap. More than three causes choice paralysis. If only one passes the criteria, surface only one and explain why the others didn't fit. If zero pass, surface the gap and offer the two fallback routes (capture or swap block).

---

## How vid-segment uses this file

At Phase 2 (structure pass):

1. Read the segment's point from its job and emotional opening (in `piece.md` and the locked skeleton), in the creator's words
2. Query `banks/story-bank/*.md`, matching each entry's `illustrates` line and theme tags to that point by meaning
3. Apply criteria 1-3 to filter to viable candidates (stage match, point match, outcome specificity)
4. Apply criteria 4-5 to rank
5. Surface top 1-3 to creator
6. On creator pick, lock the candidate
7. At Phase 4 (save), update the entry's `used_in:` and flip `status:` to `used`

If criteria 1-3 produce zero viable candidates, route to capture or swap the block before writing prose.
