---
type: reference
scope: vid-segment
loaded_by: [vid-segment]
status: active
tags: [reference, visual-demo, parable]
---

# Visual Demo Builder

A visual demo turns a problem you can't see into something you can. Pure facts retain about 10% of viewer attention. A strong visual demo can push retention on that point to 65% or higher because the viewer's brain does the work itself: it sees the visual, draws the connection, and forms the memory in one stroke.

This guide teaches how visual demos work. vid-segment loads it inline during writing when the segment's parable is a Visual Demo. There is **no Visual Demo bank**. Demos are created in-the-moment for each segment because the patterns transfer across videos, but specific demos don't.

## Why no bank

A "16 sugar cubes next to a Coke can" demo lands because the visual IS the sugar in the soda. The next video about retention strategies or framework selection won't reuse those sugar cubes. It will use a different demo built from the same SUB-TYPE pattern (Show the Problem). The pattern is reusable; the instance is not.

What transfers:
- The 3 sub-types (Show the Problem, Contrast, Breakdown)
- The planning filters per sub-type
- The anti-patterns

What does NOT transfer:
- Specific props, splits, frozen frames, or annotations
- Per-segment demo wording

The creator's signature visual style (icon charts, color-coded thumbnails) lives in `foundation/packaging-system.md` as committed thumbnail strategies and design guardrails. That's a different artifact than a one-shot in-script demo.

## When this fires

vid-segment loads this file inline when:
- The segment's parable is Visual Demo (per `references/parable-decision-matrix.md`)
- The creator wants help generating a demo for a specific point mid-write

The creator never invokes a "vid-visual-demo-craft" sub-skill. The 3-step brainstorm runs inline in vid-segment's structure pass.

## Real examples (read these first)

### Example 1: Show the Problem (Sugar Cubes) (weight loss niche)

**Point being demoed:** soda is why the viewer isn't losing weight.

**The demo:** stack 16 sugar cubes next to a Coke can. Say: "Would you lose weight if you consumed this much sugar a day? That's how much is in one can. Combined with average daily intake, you get 26 sugar cubes a day."

**Why it lands:**
- The problem (hidden sugar) was invisible. Now it's visible.
- Emotionally shocking. Easy to picture. Inspires action (skip the soda).
- Two visual elements maximum (sugar cubes + can). Complexity would kill it.

**Why this sub-type:** the viewer would struggle to picture "30 grams of sugar." A single image makes it obvious.

### Example 2: Contrast (Sales Page Headlines) (creator coaching niche)

**Point being demoed:** swapping a vague headline for a benefit-driven one drives conversions.

**The demo:** show two sales page mockups side-by-side. Left side: generic "Final Cut Pro Color Grading Masterclass" with a neon adjustment-rings hero image. Right side: "Stick out faster on social media with HBO-quality video" with a before/after split-screen showing dull-flat-video on top and cinematic-color-graded video below.

**Why it lands:**
- The "Version A vs Version B" moment is instant. The viewer sees themselves on the left side and wants the right.
- The contrast removes doubt better than explanation. Words about "improving conversions" don't have the same punch.

**Why this sub-type:** the improvement is visible, and the before/after split removes any ambiguity about what "better" means.

### Example 3: Breakdown (Frozen Late-Night Clip) (charisma niche)

**Point being demoed:** charismatic hosts open conversations on a positive note, every time.

**The demo:** freeze a clip from a late-night show. Annotate with a text overlay: "1. STARTS ALMOST EVERY CONVERSATION IN A FUN POSITIVE WAY." Point an arrow at the host's expression.

**Why it lands:**
- The technique (charisma's opening move) was invisible inside the flow of conversation. Freezing it makes it visible.
- The viewer can now spot the same move in other interviews. Pattern recognition installs.

**Why this sub-type:** the move happened in real time and would be lost without slowing down. Freezing the moment is the only way to teach it.

## The 3 sub-types

### Show the Problem

Turn a problem you can't see into something you can. Use a physical prop, a simple diagram, or a single image that makes the invisible visible.

**Worked example:** 16 sugar cubes next to a Coke can. The hidden sugar is now visible.

**Planning filter:** use this sub-type when:
- Would the viewer struggle to picture the problem from words alone?
- Would a single image make the problem obvious?
- Would a 2-second visual beat 2 minutes of explanation?

If yes to any, this sub-type fits.

**Anti-pattern:** too many elements. The YouTube icon chart with 5 colors failed (too complex). The same chart with 2 colors worked. Limit to 2 core elements per demo.

### Contrast Demo

Show before/after, wrong/right, or low/high impact side-by-side so the viewer instantly "gets" which one is better.

**Worked example:** generic sales page on the left, benefit-driven sales page on the right. The improvement is visible without explanation.

**Planning filter:** use this sub-type when:
- Would a before/after clearly show the improvement?
- Would a wrong-vs-right split make the lesson obvious?
- Would a side-by-side remove doubt better than explanation?

If yes to any, this sub-type fits.

**Anti-pattern:** more than 3 contrasts in a row. Two is the sweet spot. Three is the max. After that, the viewer loses the thread.

### Breakdown Demo

Pause, freeze, or annotate a clip / image / page to make a specific point visible. Best for teaching subtle techniques that get lost in real-time flow.

**Worked example:** frozen late-night clip with an annotation pointing at the host's opening move.

**Planning filter:** use this sub-type when:
- Is there something visual that needs to be slowed down or zoomed in on?
- Would freezing the moment clarify the point?
- Would showing how it worked beat describing it?

If yes to any, this sub-type fits.

**Anti-pattern:** cluttered annotations. One thing at a time. If the demo points at 4 things in the same frame, the viewer loses focus.

## The 3-step brainstorm process

This is the spine of inline visual demo crafting in vid-segment. Walk the creator through these steps when the segment's parable is Visual Demo.

### Step 1: Name the point that needs the demo

What's the SPECIFIC point in this segment that would benefit from a visual? One sentence in the creator's voice.

**Worked:** "Most creators script titles by guessing instead of running them through BENS, and the difference shows up in CTR."

**Near-miss:** "Titles matter." Too vague. Push for specificity: "What's the specific failure mode you're showing?"

### Step 2: Pick the sub-type via the planning filter

Walk through the 3 sub-types' planning filters. Usually one fits clearly.

**Worked:** the point is about CTR difference between guessed titles and BENS-tested titles. Contrast Demo fits: show the two titles side-by-side with CTR numbers underneath. The viewer sees the gap instantly.

**Near-miss:** picking Breakdown Demo for a contrast point. Breakdown freezes ONE thing; Contrast compares two. Wrong sub-type means the demo doesn't land.

### Step 3: Generate 2-3 candidate demo concepts

Propose 2-3 specific demo concepts using the chosen sub-type. Creator picks one or modifies. Each candidate is one sentence describing what's on screen and what the creator says alongside it.

**Worked (Contrast example):**

Candidate A: "Left side: a guessed title ('My Best Productivity Tips'). Right side: a BENS-tested title ('I Stopped Time-Blocking. Here's What I Use Now'). CTR numbers below each."

Candidate B: "Two YouTube search results side by side. Left: a video with a guessed title that got 800 views in 30 days. Right: a video with a BENS title that got 84,000 views. Same creator, same topic."

Candidate C: "Split screen of the creator's own channel: top row, 4 videos with low CTR + guessed titles. Bottom row, 4 videos with strong CTR + BENS titles."

Creator picks the one with the strongest proof anchor (probably B or C if real data exists; A if it's a teaching example).

**Near-miss:** generating one option and assuming it lands. 2-3 candidates lets the creator see range and pick the strongest. Generating ONE rushes the decision.

## Anti-patterns (across all sub-types)

### Complexity kills

Two visual elements per demo is the safe ceiling. Three is the max if all three are tightly related. Four+ becomes a slide, not a demo. The icon chart with 5 colors failed; the same chart with 2 colors worked.

### Never assume viewers know where to look

If the demo has multiple elements on screen, use an arrow or callout. Crop tight to remove anything that isn't load-bearing. A messy screenshot with 20% relevant content reads as low-effort.

### Missing transition out of the demo

After a visual demo lands, the viewer doesn't know if the moment ended or what comes next. Always write the transition into the script. Without it, retention drops at the seam.

### Verbal demo without the visual

If the script says "imagine 16 sugar cubes next to a Coke can," the demo fails. Visual demos require ACTUAL VISUALS. If filming or editing can't produce the visual, swap to a different block type (story or metaphor).

### Forcing a sub-type that doesn't fit

If the point is genuinely "show how this works step-by-step over time," that's a Breakdown. Forcing Contrast on it ("before doing it / after doing it") is weaker than just slowing down the real moment. Pick the sub-type the point asks for, not the one that came to mind first.

## Transitions out of a visual demo

After the demo lands, transition into the principle. Three patterns work:

- "So now that you've seen the problem, here's how to fix it."
- "Let me show you the steps to get the same result."
- "Here's how to apply this for yourself."

The pattern signals the demo is done and the principle is starting. Without this signal, retention drops at the seam.

## Reusability notes

The bank pattern doesn't apply here. What gets reused across videos:

- **Sub-type patterns** (Show the Problem, Contrast, Breakdown), apply the same pattern to different points
- **Style preferences**, if the creator always uses icon charts for quantity comparisons, that's a packaging-system commitment, not a per-demo bank entry
- **Anti-patterns**, the same complexity-kills, where-to-look, transition rules apply every time

What does NOT get reused:
- Specific props (16 sugar cubes)
- Specific contrast pairs (one sales page vs another)
- Specific frozen frames

When the creator nails a demo and wants to remember the IDEA for inspiration, drop a `> [!todo]` callout under the relevant segment's heading in that piece's script.md, or just trust the script's record. The bank model is wrong for this material type.

## When to swap to a different block type

If 2-3 brainstorm rounds don't produce a demo concept the creator believes in, swap the parable to Story or Metaphor. The segment's job is to land the point with emotion before logic; the specific block type is replaceable.

Signals to swap:
- All 3 candidates feel forced
- The visual would require footage or props the creator can't produce
- The creator can't picture filming this without it feeling staged

## Dig deeper probes (when the first attempt is weak)

When the demo concept is too abstract:
- "What would actually be on screen? Describe it like you're directing a camera."
- "Could someone else recreate this from your description?"

When the visual would be hard to film:
- "Is there a simpler version that uses something on your desk right now?"
- "Could a screenshot or a diagram do the same work as a physical prop?"

When the contrast isn't sharp enough:
- "Make the two sides more extreme. What's the worst case on one side and the best case on the other?"
- "Are these two things genuinely different, or are they two flavors of the same thing?"

When the breakdown is cluttered:
- "Crop to ONE element. What's the single thing you want them to see?"
- "Could you split this into 2 sequential demos instead of one busy one?"
