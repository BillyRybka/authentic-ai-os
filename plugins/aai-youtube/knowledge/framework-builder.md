---
type: reference
scope: shared
loaded_by: [vid-bank, vid-segment]
status: active
tags: [reference, framework-capture, framework-bank]
---

# Framework Builder

A framework is a container for the viewer's brain. It turns a scattered topic into a named structure they can hold, repeat, and act on. The #1 mistake in a principle is including too much. A framework's job is to give the viewer the 20% of the material that creates 80% of the result, and to give that 20% a memorable shape and name.

This guide teaches how frameworks work. vid-bank's Stage F uses it to walk creators through naming an existing system. vid-segment loads it whenever a segment's principle is a framework: to pick the teaching shape for an existing bank entry, or to walk the 5-step build when no entry exists.

## When this fires

- vid-bank Stage F (standalone): creator says "I have a system called X, save it."
- vid-segment (write time): the segment's principle pulls a framework from `banks/framework-bank/`; this file decides the shape it's taught in.
- vid-segment (inline, mid-write): creator is writing a segment whose principle is a framework, no bank match exists, walks the 5-step build then optionally saves via Stage F.
- vid-segment (inline, mid-write): creator wants help naming a framework that already exists in their brain-dump but isn't banked yet.

## Frameworks in the principle context

Frameworks are one of three principle tools. The other two are Proof (builds trust after the framework lands) and Checklists / On-Screen Steps (anchor attention through the framework's components, give the viewer a sense of progress). When using a framework in a video, all three usually appear together: the framework names the structure, proof backs each component, on-screen step markers ("STEP 1," "STEP 2") track progress for the viewer.

For Proof, see `knowledge/proof-placement-rules.md`. For Checklists / On-Screen Steps, see `knowledge/visual-proof-callouts.md` (the editor convention for surfacing step markers in saved scripts).

## Real examples (read these first)

### Example 1: NEI Triangle (pyramid shape, named system)

**Problem it solves:** creators are overwhelmed by how many factors drive video performance and don't know where to put their energy.

**Components:**
1. **New**, the topic, angle, or framing feels fresh to the viewer
2. **Easy**, the viewer can absorb it without straining
3. **Inspiring**, the viewer leaves believing they can act on it

**Shape:** pyramid. Three ingredients that all matter equally, with "FEEL" labeled in the center.

**Why it lands:** three is the comfortable max the viewer can hold. Calling out the center makes the principle stick.

### Example 2: Fail As Fast As You Can (cycle shape)

**Problem it solves:** creators overthink their first videos and burn months building something that doesn't get tested against viewers.

**Components:**
1. MVP (build the minimum version)
2. Test (ship it)
3. Measure (gather signal)
4. Adjust (change one thing)
5. Loop back to MVP

**Shape:** cycle. The process improves as it repeats. Drawn as a circular flow chart with arrows.

**Why it lands:** the loop visual sets the right expectation. The viewer doesn't expect a single attempt to work; they expect to iterate.

### Example 3: BENS (acronym shape)

**Problem it solves:** creators draft titles and thumbnails without a clear test, then wonder why CTR underperforms.

**Components:**
- **B**ig, does the promise land at a meaningful size?
- **E**asy, would the average viewer expect to absorb this without strain?
- **N**ew, is there enough freshness to pull the click?
- **S**afe, does the package signal "this won't waste my time"?

**Shape:** acronym. Four letters spell a memorable word that doubles as a checklist.

**Why it lands:** viewers remember the word first, then recall what each letter means. Strong recall, simple recall, the framework becomes shorthand.

## The 6 framework shapes

Pick the shape AFTER the components are clear, not before. The shape's job is to make the relationship between components visible at a glance.

### Arrows

**Use when:** the components happen in a strict order, one feeding the next.

**Example:** Title → Thumbnail → Intro. Each step builds on the last. The arrow promises a finish line.

**Visual:** sequential boxes connected by arrows, left-to-right.

**Anti-pattern:** forcing arrows on components that don't actually require sequence. If the order is interchangeable, this is the wrong shape.

### Pyramid (or Triangle)

**Use when:** three ingredients all matter equally and stack to produce one outcome.

**Example:** NEI triangle with "FEEL" in the center.

**Visual:** triangle with one component per side, the principle they produce in the middle.

**Anti-pattern:** forcing a pyramid when there are 4+ components. The shape lies about the count.

### Cycle

**Use when:** the process loops and improves with each repetition.

**Example:** Fail As Fast As You Can (MVP → Test → Measure → Adjust → repeat).

**Visual:** circular flow chart with arrows around the loop.

**Anti-pattern:** forcing a cycle on a one-and-done process. Cycles imply repeated improvement; one-shot work doesn't fit.

### Venn Diagram

**Use when:** two or three concepts overlap and the magic happens in the overlap.

**Example:** Passion + Outcomes + Paid, with the center labeled "Entrepreneurial Sweet Spot." The outer regions get names too (Unethical, Unfulfilling, Unrewarding).

**Visual:** overlapping circles with named regions.

**Anti-pattern:** forcing a Venn when the concepts don't actually overlap. If they're sequential, use arrows.

### Funnel

**Use when:** the structure narrows from broad to specific, filtering attention into action.

**Example:** Awareness → Consideration → Conversion → Loyalty.

**Visual:** classic funnel shape, wide at the top, narrow at the bottom.

**Anti-pattern:** forcing a funnel when the relationship is parallel, not sequential narrowing.

### Acronym

**Use when:** the components share a clean alphabetical relationship that spells a memorable word.

**Example:** BENS (Big / Easy / New / Safe).

**Visual:** the four letters, each one a section header.

**Anti-pattern:** forcing an acronym by twisting words to fit letters ("S" stands for "Strongifying"). If the acronym is strained, the framework loses credibility.

## Selection matrix

| Component relationship | Shape |
|---|---|
| Happen in strict order | Arrows |
| Three (or four) equal ingredients stacking to one outcome | Pyramid |
| Loop and improve over time | Cycle |
| Overlap, magic in the intersection | Venn |
| Broad to narrow | Funnel |
| Share a clean alphabetical relationship | Acronym |

If two shapes seem to fit, default to the simpler one. The shape exists to make the relationship visible, not to demonstrate cleverness.

If NO row fits, the "framework" is probably a list, not a framework. If the components are a flat list with no logic between them, it's a checklist: teach it with on-screen step markers, don't dress it as a framework.

## Using a framework at write time (vid-segment)

When the segment's principle pulls an existing framework from the bank:

1. Open the entry, read `framework_type` and `components:`
2. If the entry has a `shape:` field, respect it; otherwise apply the selection matrix
3. Note the shape in the structure draft (e.g. "Principle: framework [[3-part-onboarding-system]], arrows shape")
4. At prose time, name the framework, walk the components in shape order, and place a `> [!note] visual:` callout suggesting the on-screen graphic if the format supports it

Cross-shape rules, either path:

- **Three is the default count.** More than 5 components rarely lands. An 8-component framework should be split, or some components are sub-items under a parent.
- **Name the shape on screen.** Arrows drawn as steps, pyramid stacked, acronym letters bold. Make the shape visible.
- **One framework per segment.** Two frameworks in one segment dilute both; that's two segments.
- **The shape doesn't replace the lesson.** The shape is the scaffold; the words do the teaching.

## The 5-step build process

This is the spine of inline framework crafting in vid-segment. Walk the creator through these steps. They produce a named system the creator can either lock into the script directly, or save via vid-bank Stage F for reuse across future videos.

### Step 1: Dump every point

Ask the creator to dump every point they could make on this topic, in any order. If the segment has a brain-dump already, pull from there; otherwise probe: "Imagine you're explaining this to a smart friend over coffee, and they keep asking why. What are all the things you'd want to land?"

**Visual to invoke if the creator is stuck:** imagine a table covered in scattered sticky notes, each one a different point (Hooks, Editing, Titles, Watch Time, CTR, etc.). You're going to look at the whole table, then group them into 3 clean blocks. The viewer can hold 3 blocks; they can't hold 12 sticky notes.

**Worked:** creator names 8-12 scattered points covering tactics, principles, examples, edge cases.

**Near-miss:** creator names only 2-3 polished bullets. That's too few. Push for 8+ to find the right 3. "Dump everything, even the ones that feel obvious."

### Step 2: Ask the result

"What's the result you're helping the viewer get from this point?" Force a SPECIFIC viewer outcome, not a vague "they'll understand more."

**Worked:** "They'll know how to draft a YouTube title that hits BENS without overthinking."

**Near-miss:** "They'll learn more about titles." Push: "Learn what specifically? What can they DO after?"

### Step 3: Circle the top 3

From the dumped points, circle the 3 that drive the result most directly. Push hard against keeping 4+. The viewer can hold 3 easily; 4+ becomes a list, not a framework.

**Worked:** drops 9 points, keeps 3 that compound. Creator might protest. Push: "Which 3 produce the result fastest? The others are bonus, not core."

**Near-miss:** keeping 6 because "they all matter." They all matter, but they're not all CORE. A framework is the 20% that creates 80%, not everything that's relevant.

### Step 4: Pick the shape

Use the selection matrix. Propose 1-2 shapes based on how the 3 components relate, with a one-line "why this shape" each. Creator picks.

**Worked:** components are "Find the topic → Build the block → Polish the wording." Order matters and one feeds the next. Arrows.

**Near-miss:** components are "Hook strength, Retention, CTA" but creator wants a pyramid. Push: do they actually stack equally to produce one outcome, or are they sequential? If sequential, arrows fit better.

### Step 5: Name it

Propose 3-5 names. Mix descriptive ("The 3-Part Onboarding System") and acronym ("BENS-style if the letters land"). Creator picks or rewrites. **Apply the read-aloud test to the NAME**: would the creator say this on camera without rewording?

**Worked:** "The 3-Part Onboarding System." Clean, descriptive, the creator will repeat this on camera.

**Near-miss:** "S.C.A.L.E. (Strongify Communication And Lead Engagement)." Strained acronym, strained words. Pick a clean descriptive name instead.

## Naming rules

- **Three is an example, not a rule.** Default to 3 components because the viewer can hold 3 easily, and more becomes overwhelming. But the rule is flexible. A 4-letter acronym like BENS works because the letters spell a memorable word. If 4 components compound to one outcome and lose meaning when reduced to 3, keep 4. Just be honest about whether the 4th component is core or padding.
- **Use the creator's voice.** If the creator uses "Block" everywhere, "The 3-Block Stack" sounds natural; "The Triangulated Decision Architecture" does not.
- **Avoid AI-invented compound nouns.** "Engagement Crystallization Loop" reads as AI. Real names sound like real people would say them at a dinner party.
- **Test acronyms ruthlessly.** Read the acronym aloud. Does it sound like a word the creator would use, or a forced label? If forced, go descriptive.
- **Allow descriptive names.** Not everything needs an acronym. "The 3-Part Onboarding System" is fine.
- **Test repetition.** "Would you say this name 3 times in a video without it sounding clunky?"

## What NOT to bank

- **Frameworks other people created.** BENS, Eisenhower Matrix, the marketing funnel. Those are universal references, not creator IP. Reference them inline in scripts; don't put them in framework-bank.
- **AI-invented acronyms.** Names come from the creator's actual practice and language, not AI-generated branding.
- **Half-baked ideas.** A framework needs (a) a name the creator actually uses, (b) named components, (c) a clear problem it solves. Missing any of these means it's not ready to bank.
- **Single tactics.** "Use a Calendly link" is a tactic, not a framework. Frameworks have multiple components.
- **One-time frameworks invented for one video.** If the framework is genuinely point-specific and won't compound across videos, build it in the script, don't bank it. The bank captures frameworks that will be repeated.

## Entry schema + worked body example

When the creator wants to save a framework (either standalone via vid-bank Stage F or after inline crafting in vid-segment), the entry follows this shape. Stage F handles the actual save.

```yaml
---
type: framework
project: youtube-content-os
name: "The 3-Part Onboarding System"
framework_type: process
shape: arrows
components: ["welcome-call", "first-win-week", "30-day-rhythm"]
problem_it_solves: "new clients drift in their first month if there's no rhythm"
themes: [onboarding, delegation]
maturity: active
captured: 2026-05-11
status: captured
tags: [framework, arrows, onboarding]
used_in: []
---

# The 3-Part Onboarding System

## What problem does this solve?

New clients drift in their first month because nothing forces them into a rhythm. They forget what they signed up for, miss the first action steps, and quietly leave by month two. The system gives the first 30 days a backbone.

## The components

1. **Welcome call (week 1):** 30-minute kickoff where we name the one biggest result they want and the one biggest blocker. No tactics yet. Just clarity.
2. **First-win week (week 2):** they ship one small thing tied to the result. The win is the proof point. Without it, the rest doesn't compound.
3. **30-day rhythm (week 3-4):** weekly check-ins go on the calendar. The cadence becomes the system, not me.

## The shape

Arrows. Each step depends on the prior one. You can't run the 30-day rhythm without a first win, and you can't pick a first win without the welcome call.

## When to use it

- Videos teaching client retention or onboarding systems
- The "scale" segment of a sales video where the methodology becomes visible
- Sales-page copy that needs to show what the first month looks like

## Related assets

- Stories: [[story-bank/steve-9-weeks-to-2-week-vacation]]
- Proofs: [[proof-bank/30-day-retention-rate]]
- Metaphors: [[metaphor-bank/training-wheels-vs-bike-lanes]]

## Origin

Came from running this with 14 clients over 6 months. Started as "I should do a welcome call," became a documented system after the third time I forgot what we agreed on in week 1.
```

## Dig deeper probes (when the first attempt is weak)

When the creator's components feel like a list:
- "Are these actually a system, or are they 5 tips that don't depend on each other?"
- "If you removed component 2, would 1 and 3 still produce the result?"

When the shape doesn't feel right:
- "Walk me through using component 1, then 2, then 3. Does order matter? If yes, arrows. If no, try pyramid."
- "Could a viewer skip a component? If yes, it's a list. If no, it's a real framework."

When the name feels forced:
- "Read it aloud three times. Does it stay natural?"
- "Would you say this in a sales call without explaining the acronym? If no, simplify."

When the creator wants to bank something half-baked:
- "Have you used this framework in 3+ videos? If no, it's still an idea. Put it in `content/ideas/content-ideas.md` and bank it when it crystallizes."

## Pivot phrases (the bridge into the framework)

When transitioning from the parable (story/metaphor/demo) into the framework as the principle, three patterns work:

- "So here's what I learned from that. I call it the [framework name]."
- "Here's the system I built to fix this. Three parts: [component 1], [component 2], [component 3]."
- "If I had to break it down into the smallest set of moves, it's [framework name]."

These belong as the transition between the segment's parable and its principle.

## Source note

Frameworks the creator invents are the creator's IP. Frameworks the creator references but didn't invent (BENS, the marketing funnel) stay as inline references, not bank entries. The bank is for compounding creator-owned material.
