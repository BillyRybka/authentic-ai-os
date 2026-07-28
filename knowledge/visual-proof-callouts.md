---
type: reference
scope: shared
loaded_by: [vid-intro, vid-segment, vid-ending]
status: active
tags: [reference, visual-proof, callouts]
---

# Visual Proof Callouts

When a claim lands in a script, visual proof should appear on screen at the same moment. The script doesn't need to draw the visual. It needs to call out where the visual is required so the editor knows. This file tells writing skills (`vid-intro`, `vid-segment`) how to surface those callouts in the saved script without bloating the spoken content.

The visual-proof rule comes from [[intro-architecture]]: "A claim with no visual proof creates doubt. A claim with visual proof creates trust." This is a production note for the editor; the script-writing skill flags where the editor needs to put proof on screen.

## What counts as a claim that needs visual proof

In an intro, claims worth flagging are:

- **Numbers** (revenue, view counts, time durations, quantities)
- **Named outcomes** ("got my first three clients in 30 days")
- **Specific time-bounded results** ("in four months")
- **Before-and-after states** ("from 80 hours a week to 15")
- **Volume signals** ("over 200 reviews")
- **Specific named people** ("Steve hadn't landed a single client")

What does NOT need visual proof:

- General industry observations ("most creators struggle with this")
- Avatar problem-poke language ("do you hate making thumbnails?")
- The Setup contract ("So in this video, I'm going to show you...")
- Banned phrases (which shouldn't be there anyway)

The principle: any time the creator says a SPECIFIC thing that the viewer might doubt, the editor needs to put proof on screen. Generic claims don't need it because nobody doubts them.

## How to surface callouts in the saved script

Use Obsidian callout syntax inside the saved `## Intro` section. Format:

```markdown
> [!important] Visual proof needed
> {what the visual should show}
```

Place the callout immediately AFTER the line that contains the claim, in the script. Don't put it before. It disrupts the read.

## Worked: Big personal result Hook

**Spoken intro:**

> "Six months ago Steve hadn't landed a single client. Now he's doing $80k a month. Same niche, same offer, same skill level. Three things changed."

**Saved script:**

```markdown
## Intro

Six months ago Steve hadn't landed a single client. Now he's doing $80k a month.

> [!important] Visual proof needed
> Steve's revenue dashboard showing $80k monthly. Or a Stripe screenshot. Or a testimonial card with the same number from Steve.

Same niche, same offer, same skill level. Three things changed.
```

**Why this works:** the callout sits right after the spoken claim "$80k a month." The editor sees it AT THE EXACT MOMENT they're cutting that line, knows what to put on screen, and the cold viewer's doubt gets answered as the claim lands.

## Worked: Effort signal in Setup

**Spoken intro:**

> "So in this video, after analyzing 247 sales pages this month, I'm going to show you the three structural moves that separate the winners from the losers."

**Saved script:**

```markdown
## Intro

So in this video, after analyzing 247 sales pages this month,

> [!important] Visual proof needed
> Quick montage of sales-page screenshots flicking past, OR a Notion/Airtable database view with 247 rows visible.

I'm going to show you the three structural moves that separate the winners from the losers.
```

**Why this works:** the proof shows volume (247 pages) without stopping the verbal flow. The viewer's brain registers "OK, this isn't theory" and stays.

## Near-miss: Callout in the wrong place

**Wrong placement (callout BEFORE the claim):**

```markdown
## Intro

> [!important] Visual proof needed
> Show Steve's revenue dashboard at $80k.

Six months ago Steve hadn't landed a single client. Now he's doing $80k a month.
```

**Why this fails:** the editor sees the callout first, may put the visual on screen BEFORE the claim is spoken, and the viewer sees a number with no context. The setup matters: claim first, then proof on screen.

**The rule:** callout immediately AFTER the line that contains the claim. Not before. Not three lines later.

## Worked: Multiple proofs in one intro

**Spoken intro:**

> "Most coaches' sales pages convert at under 1%. Mine went from 0.8% to 6.2% after I changed three things. After analyzing 247 pages this month, I'm going to show you those three moves."

**Saved script:**

```markdown
## Intro

Most coaches' sales pages convert at under 1%. Mine went from 0.8% to 6.2% after I changed three things.

> [!important] Visual proof needed
> Before-and-after screenshot: old conversion rate (0.8%) and new conversion rate (6.2%). Side by side, with date labels.

After analyzing 247 sales pages this month,

> [!important] Visual proof needed
> Quick montage of sales-page screenshots OR a research database view showing 247 rows.

I'm going to show you those three moves.
```

**Why this works:** each claim gets its own callout. The editor handles them as separate visual beats. The viewer sees proof at every claim-moment, never doubts a number.

## What if the brain dump doesn't have a usable visual asset?

If the creator's claim is real (it's in the lock list) but no visual asset exists:

1. **Surface to the creator at save time:** "Spotted: '$80k a month' is in the intro. The brain dump doesn't link to a screenshot or dashboard. Want to grab one before filming, or remove the claim?"
2. **Don't auto-remove the claim.** The creator decides whether to capture the proof or rephrase.
3. **Don't fabricate a visual** ("imagine a dashboard here"). Anti-fabrication applies to visual proof too. The proof is real or the claim doesn't ship.

This connects to [[banks/proof-bank]]: if the proof exists in the bank but isn't linked to the brain dump, ask the creator if they want to wikilink it. Update both sides per [[knowledge/bank-contract]].

## How callouts feed downstream skills

`vid-segment` uses the same callout convention for body claims. `vid-pressure-test` (future) reads callouts during review and flags any claim that's missing one. The convention stays consistent across the writing skills.

When `vid-intro` saves the intro, it also updates `content/pieces/{slug}/piece.md`:

```yaml
visual_proofs_called_out:
  - line: "Now he's doing $80k a month."
    proof_needed: "Steve's revenue dashboard or Stripe screenshot"
    bank_link: "[[steve-80k-monthly]]"   # if proof exists in bank, otherwise null
  - line: "after analyzing 247 sales pages this month"
    proof_needed: "Montage or database view of 247 sales pages"
    bank_link: null
```

The `bank_link: null` cases get surfaced at save time so the creator can capture missing proofs before filming.

## On-screen step markers (checklists as the third principle tool)

Step markers are the third principle tool (alongside Frameworks and Proof). When a segment teaches a framework with named components, on-screen step markers ("STEP 1," "STEP 2," "STEP 3") track progress for the viewer. They reduce cognitive load and prevent the "should I stop here?" feeling by giving viewers chapter-marker-style orientation.

Step markers are an editor-facing convention, just like visual proof callouts. The script flags them; the editor places them on screen.

### When to flag step markers

- The segment's principle is a framework with 3+ named components
- The framework's shape is sequential (Arrows) or staged (Funnel)
- The viewer needs a sense of progress through a list of actions
- A long segment (>2 minutes) benefits from chapter-style orientation

### How to surface step markers in the saved script

Use the same Obsidian callout convention. Place the callout immediately after the line that introduces each numbered component:

```markdown
> [!important] On-screen step marker
> STEP 1 / Welcome Call
```

The editor adds the visual chyron / slide at the corresponding moment in the video.

### What does NOT need step markers

- Single-point segments (no list to track)
- Cycles, Venns, Pyramids: non-sequential shapes don't read as steps; use a labeled diagram instead
- Listicle videos: the format planner already includes counted titles per point, which double as step markers without needing callouts

### Tracking in piece.md

When `vid-segment` writes a segment with step markers, also update piece.md:

```yaml
on_screen_steps:
  - segment: 2
    framework: "The 3-Part Onboarding System"
    steps: ["Welcome Call", "First-Win Week", "30-Day Rhythm"]
```

`vid-pressure-test` (future) reads this to verify the framework's component names appear consistently on screen and in the script.

## What this file does NOT do

- It does not generate the visual itself. That's the editor's job.
- It does not enforce that every claim has a bank-linked proof at save time. It surfaces gaps; the creator decides.
- It does not apply outside the intro. `vid-segment` and `vid-ending` use the same convention but flag their own callouts.
