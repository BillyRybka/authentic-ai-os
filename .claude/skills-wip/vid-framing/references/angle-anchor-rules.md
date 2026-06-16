---
name: Angle Anchor Rules
type: skill-local-reference
loaded_by: vid-framing
when_to_read: Phase 2 (angle generation) and Phase 3 (Theory of One filter)
---

# Angle Anchor Rules

Every angle vid-framing surfaces is either anchored to a real pattern-bank outlier OR flagged experimental. No third option. This file is the rule set for HOW to anchor, how anchor strength is derived from a pattern's spread, when to use the experimental slot, and how to avoid common mistakes.

## The 3 + 1 rule

Every framing session surfaces 4 angles:

- **Angles 1, 2, 3** anchor to real outliers from the creator's pattern banks (`banks/pattern-bank.md` + sub-banks). Strong or moderate anchors only (strength derived from spread; see below).
- **Angle 4** is experimental. No outlier anchor required. Flagged `anchor_confidence: experimental` so the creator picks it with eyes open.

The 3+1 split protects two things at once: discipline (75% of angles are evidence-anchored) and creativity (one slot for the creator's gut).

## What counts as a valid anchor

An anchor is a SPECIFIC outlier entry from one of the seven pattern banks. Not a "pattern" in the abstract. Not a "things that work in this niche." A named entry with:

- A real video title
- A real channel handle
- A real view count
- A documented "why this pulled" hypothesis in the bank entry

If the AI surfaces an angle with the rationale "outliers in your niche use curiosity hooks," that's not an anchor. That's hand-waving. The anchor must be: `"You Need This Camera Setting" (@SonyCreator, 480k views, title pattern imperative-hidden-move)`.

## Anchor strength (derived from spread)

Strength is NOT read from a stored label. vid-framing derives it at load time from the pattern's `spread` (how many channels used it) and `own_channel_proven`, both written by vid-research into `pattern-bank.md`. When writing piece.md, strong maps to `anchor_confidence: high`, moderate to `medium`, weak to `low`.

### STRONG

Anchor outlier's pattern matches ANY of:
- `own_channel_proven: true` (the creator has already proven it on THIS audience). The strongest signal, Repeat What Works.
- `spread` is 5+ of the analyzed channels (cross-channel convergence).
- Pattern has been validated post-publish on a real video (winner logged via vid-measurement, future).

And the creator's brain-dump material supports the angle without stretching. Strong anchors are surfaced first.

### MODERATE

Anchor outlier's pattern matches:
- `spread` is 3-4 of the analyzed channels (observed but not yet convergent), and `own_channel_proven: false`
- Creator's brain-dump material supports the angle but may require some drilling to flesh out

Moderate anchors are the "test this" candidates. Reasonable bet, not guaranteed.

### WEAK

`spread` of 1-2 channels and not own-channel-proven. Weak anchors should NOT be surfaced as one of the 3 anchored angles. If the only available anchors for a topic are weak, the creator probably has a pattern-bank gap, flag this in soft friction: "Limited anchors with real spread for this topic. Consider running vid-research to refresh banks before locking the angle."

### EXPERIMENTAL (no anchor)

Used only for the 4th angle slot. Reasons an experimental angle is worth surfacing:

1. The creator has a gut hunch the AI couldn't have proposed (different framing of an angle, surprising story, contrarian take)
2. The brain-dump contains a unique story or proof element that doesn't map to any existing pattern
3. The creator wants to test an adjacent-niche structural pattern applied to a topic NOT yet in their pattern bank (the yoga-niche example from research)

Experimental angles MUST be flagged: `anchor_confidence: experimental`, `outlier_anchor: null`. They are first-class citizens, the creator can pick them. But they're communicated transparently as the "no data behind this, your gut pick" slot.

## How to anchor an angle (worked example)

**Brain-dump topic:** the creator's framework for setting weekly priorities under ADHD.

**Pattern bank shows:** title pattern `stop-do-this` ("STOP [common practice]") with spread 8 of 11 niche channels, anchored to outliers like:
- "STOP Using These 5 Outdated Productivity Apps" (@CoachX, 1.4M views)
- "STOP Planning Your Week Like This" (@CoachY, 800k views)

**Anchored angle proposal:**

> **Angle 1 (strong, anchored):** "Stop Using Time-Blocking If You Have ADHD"
>
> Anchor: `stop-do-this` pattern. Worked outliers: "STOP Using These 5 Outdated Productivity Apps" (@CoachX, 1.4M), "STOP Planning Your Week Like This" (@CoachY, 800k).
>
> Why it could land: Brain-dump has the creator's specific story about abandoning time-blocking after burnout. The stop-do-this pattern lands consistently in this niche because the audience expects contrarian framing of common advice. Avatar's Top 3 problem #2 ("productivity systems made for neurotypical brains").
>
> Risk: Audience may push back if the alternative the video offers isn't strong. Brain-dump's alternative (energy-blocking) needs to be specific in execution.

This anchor cites a real entry, names the pattern, names the worked examples, and ties the brain-dump material to it. That's an anchor.

## What does NOT count as anchoring (near-miss)

**Bad anchor proposal:**

> **Angle 1:** "Stop Using Time-Blocking If You Have ADHD"
>
> Why: Curiosity-gap hooks work well in this niche. STOP titles tend to get high CTR. The audience has ADHD and would relate.

This is hand-waving. "Curiosity-gap hooks work well" is generic. No specific outlier. No view count. No hypothesis tied to the audience's specific bucket. This is the kind of angle creators have been getting from AI for years, feels confident, anchored in nothing.

The difference: the worked example cites BY NAME. The near-miss describes a category.

## The fluke filter (applied during anchoring)

Before surfacing an outlier as an anchor, run the fluke filter (`knowledge/outlier-identification-rules.md`).

A fluke is an outlier on a channel whose primary themes don't match the outlier's topic. Example: a dog training channel has one 700k-view video on van life. That's a fluke. The pattern that drove that video doesn't transfer to dog training content.

When the candidate anchor is a fluke:
- Skip it as an anchor
- Don't pretend it's evidence

Pattern banks built via vid-research should have flukes already filtered. But if the creator manually added an outlier or pattern, the fluke filter runs at framing time too.

## Repeat What Works, when to anchor to the creator's OWN past winners

The creator's own past winners are the strongest anchors. When a past winner exists for a topic similar to the brain-dump:

- Strong anchor by default (`own_channel_proven: true`, creator has already proven the pattern works for THIS audience)
- Surface affirmatively: "This angle repeats your past winner '[title]' which pulled [N] views and [DPV signal if known]. The Repeat What Works principle says copy the packaging."
- Note any planned variations, different story, different framework, so the creator sees what's changing

The creator's own winners are the highest-DPV anchors available. They beat any niche outlier of the same pattern.

## Adjacent-niche structural transfer (the experimental sweet spot)

The strongest experimental angles use adjacent-niche STRUCTURAL patterns applied to the creator's OWN topic. Pattern bank has these as `banks/pattern-bank.md` entries with `source: adjacent_niche, transfer_type: structural`.

Worked example (from the research process): a yoga creator stuck at 25k subs studied the mobility and weightlifting niches. Found short bingeable tip videos with simple before/after thumbnail composition. Applied that structural format to yoga content, first video in the new format pulled 2.4M views.

**Adjacent-niche transfer rule:** the TOPIC stays on-niche (yoga). The STRUCTURE comes from adjacent (before/after thumbnail, short bingeable format). Topics from adjacent niches NEVER enter the pattern bank, only structures, formats, and power words transfer.

When surfacing an adjacent-niche-anchored experimental angle:

- Flag it: `anchor_confidence: experimental` (because it's untested for THIS channel)
- Name the adjacent niche AND the structure being borrowed
- Surface the risk: "This pattern hasn't been tested on your audience. Adjacent transfer is the highest-upside experimental slot but has variance."

## Anchor count budget

Each session surfaces 3 anchored + 1 experimental. Don't surface 7 anchored angles "to give more options." Choice paralysis kills decisions. 3-4 is the magic number.

If the pattern bank surfaces 10 strong anchored candidates, vid-framing picks the TOP 3 by:

1. Widest spread (and own-channel-proven) first
2. Best alignment to brain-dump material second
3. Best fit to the Theory of One filter third

The other 7 candidates get noted internally but NOT surfaced. The creator doesn't see them unless they ask "are there other anchors I should consider?"

## When an anchored angle requires modification

The creator may say "I like the anchor but rewrite the angle." This is fine. The anchor stays in piece.md. The angle text changes. Example:

- Original: "Stop Using Time-Blocking If You Have ADHD"
- Creator's rewrite: "I Threw Out My Calendar. Here's What Replaced It"
- Same anchor (T-7 STOP pattern, but applied as a personal-story framing). Captures the creator's voice.

The anchor's strength stays the same (derived from spread). The selected_angle field captures the creator's rewrite. The outlier_anchor field captures the original pattern.

## Mode 2: anchoring during a refresh / re-frame

If the creator runs vid-framing on an existing piece (re-framing because the first angle didn't feel right), preserve the dropped angles in `## Considered + Dropped Angles` and surface a fresh 3+1 set. Don't re-surface previously dropped angles unless the creator explicitly asks.

## Hard "no" cases

Reject any anchor that is:

- Cited without a real bank entry (AI invented the outlier)
- A fluke (off-niche outlier on the source channel)
- Weak spread (1-2 channels, not own-channel-proven) and surfaced as one of the 3 anchored slots
- An adjacent-niche topic being borrowed AS a topic (only structures transfer)
- Anchored to a video the creator has already directly copied within the last 90 days (use Repeat What Works affirmatively, but don't propose the third-in-a-row clone, that's diminishing returns)
