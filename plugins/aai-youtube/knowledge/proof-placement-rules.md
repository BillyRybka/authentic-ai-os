---
type: reference
scope: shared
loaded_by: [vid-intro, vid-segment, vid-ending]
status: active
tags: [reference, proof-placement, banks]
---

# Proof Placement Rules

Where proof goes inside a segment, how to handle the multiple presentation formats one entry can carry, and how to keep proof from contradicting the framework or breaking trust. Examples-first.

This file is reference material for Claude to think with when querying `banks/proof-bank/*.md` and `banks/testimonial-bank/*.md`. The capture guides (vid-bank's `references/proof-capture-guide.md`, `references/testimonial-capture.md`) live upstream and define what proof IS. This file decides where it goes once pulled.

## The placement rule

Proof goes RIGHT AFTER a framework, claim, or lesson lands. Not before. Not at the start of the segment. Not at the end.

**Worked (deep-dive segment, Step 5 of a system):**

> [Principle teaches the framework: "the Re-engagement Trigger", three components walked through in 90 seconds]
>
> "Here's what this looked like when Steve installed it." [Loom screenshot: Steve's calendar going from 4 calls/month to 4 calls/week over 8 weeks]
>
> "Same email list. Same offer. One trigger built. The math changes."

Why it lands: framework is taught FIRST, viewer is now asking "has this actually worked?", proof answers in the same breath. Trust is preserved at the exact moment it would otherwise break.

**Near-miss (proof placed before the framework):**

> "Here's Steve's calendar going from 4/month to 4/week." [shows screenshot]
>
> "Now let me show you the Re-engagement Trigger framework."

Why it misses: viewer doesn't know what's being proved. The screenshot lands as a brag instead of evidence. By the time the framework arrives, the proof's emotional charge is spent.

**Near-miss (proof placed at the end of the segment, after the payoff):**

> [Framework taught. Principle walked. Payoff delivered.]
>
> "Oh, and here's a screenshot from a client who did this." [shows after the payoff has landed]

Why it misses: the viewer's already moved on. Proof at the end reads as afterthought. The trust window opens right after the framework. That's the placement.

---

## Why the placement rule holds

Cold viewers don't trust the creator on the framework. The moment the framework lands, they ask "has this actually worked for anyone?" If the answer is shown immediately and visually, trust is preserved. If the answer is delayed (or never delivered), the viewer decides "this is theory" and disengages.

The same logic holds for testimonials: drop the verbatim quote right after the claim it backs up, not at the start of the segment, not at the end.

---

## Multi-format presentation

A single proof entry can carry multiple presentation formats (`static-screenshot`, `before-after-pairing`, `live-clip`, `inline-stat`). The segment's job decides which format to use.

**Worked (deep-dive segment, format = before-after pairing):**

Bank entry's `proof_type: client-win`. Body has all four presentation formats listed. Segment pulls `before-after-pairing`:

> [Principle lands]
>
> "Here's the before and the after." [split screen: left side = client's old sales page screenshot, right side = redesigned page screenshot, labeled "Before, 0.7% conversion" and "After, 4.2% conversion"]

Why it lands: before-after format works in a deep-dive because the segment can carry the time to present both visuals. The transformation is visually obvious.

**Worked (news segment, same proof entry, format = inline-stat):**

> "And here's how big the gap is. Agencies running this trigger book 4x more calls per month than agencies that don't." [no visual, just the stat spoken]

Why it lands: news segment compresses. Inline stat is the right format for the speed of the format. The before-after visual would slow the news segment down.

**The principle:** match the presentation format to the segment's pacing. Static screenshots work everywhere. Before-after needs time. Live clip needs even more time. Inline stat is the lean default.

---

## Proof asset visibility

If the proof entry has an `asset_path:` in frontmatter, the asset should appear ON SCREEN at the placement moment. The script signals this with a Visual Proof callout.

**Callout convention is canonical in `knowledge/visual-proof-callouts.md`** (the `> [!important] Visual proof needed` form, the `visual_proofs_called_out:` piece.md schema, and worked examples). Load that file when writing claim-proof callouts. This file (proof-placement-rules.md) owns the placement decision (where in the segment), bank-pulling logic, and presentation-format selection. It does not own the callout syntax.

The examples below use a separate `> [!note] visual:` form because they describe production instructions for visual demo blocks and metaphor props (prop setup, camera angle, hold time, on-screen text), not claim-proof pairings. When the segment makes a CLAIM, use the canonical form per `knowledge/visual-proof-callouts.md` so vid-pressure-test can audit.

**Worked:**

Segment prose:

> [framework lands]
>
> "Here's what Steve's calendar looked like."
>
> > [!note] visual: insert `banks/proof-bank/assets/steve-calendar-9-weeks.png` (full-screen, 4-second hold, no zoom needed). Caption: "Steve's calendar, weeks 1-9."

Why it lands: the editor knows exactly what to insert and how to time it. The proof has a visual anchor.

**Near-miss:**

Segment prose:

> "Steve had a great result."

Why it misses: no visual instruction, no specific stat, no asset reference. Even if the bank entry has the asset, the segment's prose doesn't trigger its use. Editor edits the segment without the proof, and the trust gap reopens.

---

## Stacking proof: the wall-of-wins technique

Sometimes one proof isn't enough. The wall-of-wins (multiple screenshots scrolled at speed) lets the viewer see VOLUME, which proves "this isn't just one lucky case."

**Worked (success-story takeaway segment):**

> "And Steve's not the only one. Here are about 40 client wins from the past 6 months."
>
> > [!note] visual: scroll through `banks/proof-bank/assets/client-wins/` folder at ~2 seconds per screenshot. Total runtime: ~80 seconds.

Why it lands: volume proof. Viewer sees the method works for many, not one. Defends against the "one-off luck" objection.

**Near-miss (wall of wins replacing individual proof):**

A segment where the wall-of-wins is the ONLY proof and there's no specific case shown.

Why it misses: volume without specificity is weaker than one specific case. Pair the wall with one individual success story, not as a replacement.

**When NOT to use wall-of-wins:**

- The bank doesn't have ~20+ client-win entries with assets. A wall of 4 looks thin.
- The format is news, step-by-step, or review. These don't carry the runtime for an 80-second scroll.
- The segment's job is teaching the method, not establishing volume credibility.

---

## Testimonial placement

Testimonials are verbatim client quotes. They drop in as social proof inside the principle, in addition to (not instead of) numerical/visual proof.

**Worked:**

> [Framework taught. Numerical proof shown.]
>
> "Here's how [Client] said it after we ran this for the second month." 
>
> > [!quote] [Client], email 2026-02-14
> > "I haven't had to pitch in 6 weeks. Calls just keep coming. I don't even know how to explain it to my wife when she asks how the business is going."

Why it lands: testimonial drops in AFTER the framework AND the numerical proof. The verbatim quote (with the human detail of "explaining to my wife") humanizes the proof without replacing it.

**Near-miss (testimonial as the only proof):**

A segment where the only proof is a testimonial. No numbers. No screenshot.

Why it misses: testimonials carry social proof but not analytical proof. Cold viewers want both. Pair them.

**Verbatim rule:** testimonials are NEVER paraphrased, polished, or "improved." The exact wording is the testimonial. If the bank entry's quote has a typo or odd phrasing, that's the testimonial. Preserve it. If the creator wants a "cleaner" quote, the answer is to capture a different testimonial, not edit the existing one.

**Anonymization rule:** if the bank entry is `anonymized: true`, the segment uses "a client" or the anonymized identifier. Never reveal a name marked anonymized.

---

## Proof per segment: count rule

Default: ONE specific proof per principle. Stacking multiple proofs in one segment dilutes both.

**Worked (one proof, one principle):**

> [Framework]
> [One proof, Steve's calendar]
> [Lesson: "the framework is the lever, not the work harder"]

Why it lands: one proof, one belief shift. The viewer integrates one piece of evidence per beat.

**Near-miss (three proofs in one segment):**

> [Framework]
> [Steve's calendar] [Sarah's revenue jump] [Marco's testimonial] [Wall of wins]
> [Lesson]

Why it misses: 4 proofs in one segment overwhelms. The viewer can't integrate all four; they remember none of them. Save the additional proofs for other segments OR use the wall-of-wins technique to consolidate.

**Exception:** the wall-of-wins itself is one proof unit even if it contains 40 screenshots, because the viewer processes it as "many" not as 40 individual proofs.

---

## When proof contradicts the framework

If the bank entry's actual numbers don't quite match the framework's claim, surface the gap to the creator. Don't shave the data to fit.

**Worked:**

Framework claims: "consistent inbound leads within 8 weeks."

Bank entry says: 9 weeks for Steve.

Skill action: surface to creator. "Bank entry shows 9 weeks for Steve, framework claims 8. Pick: adjust the framework's claim to '8-12 weeks', use Steve's actual 9 weeks, or pull a different proof candidate that landed in 8 weeks."

Why it lands: the gap surfaces, the creator decides. The integrity stays intact.

**Near-miss:**

Skill rounds Steve's 9 weeks down to 8 weeks to match the framework.

Why it misses: fabrication. Even rounding by 1 is fabrication when the bank entry is specific. Anti-fabrication discipline applies to numbers as much as it applies to invented client names.

---

## How vid-segment uses this file

At Phase 2 (structure pass), when the segment pulls proof:

1. Query `banks/proof-bank/*.md` and `banks/testimonial-bank/*.md` by tag and theme matching the segment's claim
2. Filter candidates by stage match (does this proof support a claim at the avatar's current stage?)
3. Surface 0-2 proof candidates and 0-1 testimonial candidates with one-line rationale each
4. Note the placement: AFTER the framework, BEFORE the payoff

At Phase 3 (prose pass):

1. Drop proof immediately after the framework's components are walked
2. Use a `> [!note] visual:` callout for the asset path
3. Use a `> [!quote]` callout for verbatim testimonials
4. Verify every number traces to the bank entry. No rounding, no inflation.

At Phase 4 (save):

1. Update each pulled proof's and testimonial's `used_in:` array with `[[piece-slug]]`
2. Flip `status:` to `used` if it was still `captured`
