---
type: spec
doc: thumbnail-metadata
project: authentic-ai-os
status: approved-not-built
date: 2026-09-04
tags: [spec, vid-research, vid-thumbnail, outliers, metadata]
---

# Thumbnail and package metadata spec

Three layers of tags on every outlier note, so a thumbnail session can filter the 143 packages down to design references without opening every image. Approved by Billy 2026-09-04. Not built yet; see [[handoff-thumbnail-metadata]].

## The one rule

Every tag must be something two people would label the same way. Layer 1 and 2 are judged from the image alone. Layer 3 is judged from title plus thumbnail together, against a one-line test. "Whiteboard" passes. "Confident energy" fails and does not exist.

## Layer 1: visual facts (thumbnail only)

What is physically in the frame. Six buckets, fixed vocabularies, no free text.

### hero (single value)

The main thing in the frame. If two compete, the larger one.

| Value | Test |
|---|---|
| `face` | A person is the largest element |
| `screenshot` | A UI, app, browser, terminal, or device screen is the largest element |
| `object` | A physical prop or product is the largest element (a logo held in a hand counts here) |
| `whiteboard` | A diagram, list, or drawing on a board or board-like surface |
| `logo` | A brand mark with no face and no scene around it |
| `text` | Words are the largest element |

### face (single value)

`none` | `small` (under a quarter of the frame) | `medium` (a quarter to a half) | `big` (over half)

### expression (single value, only when face is not none)

| Value | Test |
|---|---|
| `neutral` | Closed or relaxed mouth, level eyes |
| `shocked` | Wide eyes, open mouth, or raised brows |
| `smile` | Teeth or a clear upturn |
| `smirk` | One-sided, knowing |
| `excited` | Big open-mouth grin, often with a gesture |
| `defeated` | Head down, hand on face, eyes closed |

### gesture (single value, only when face is not none)

| Value | Test |
|---|---|
| `none` | Hands not in frame or at rest |
| `pointing` | A finger aimed at something, including up or at the viewer |
| `presenting` | An open palm holding or showing an object |
| `shushing` | Finger to lips |
| `open-hands` | Both hands open, palms up or out |
| `thumbs` | Thumbs up or down |

### layout (single value)

| Value | Test |
|---|---|
| `single` | One subject, one zone |
| `split` | Two zones side by side or stacked, each with its own subject |
| `collage` | Three or more panels or a grid |
| `text-dominant` | The text block takes more area than any image element |

### text_amount (single value)

`none` | `few` (one to three words) | `phrase` (four or more)

### text_style (list, zero or more)

`caps` | `handwritten` | `highlighted` (a colored box behind a word) | `boxed` (a border around the text) | `outlined` (stroke around letters)

### background (single value)

`solid` | `gradient` | `real` (a room, outdoors, any photographed environment) | `screenshot`

### bg_tone (single value)

`dark` | `light`. Judge the majority of the frame.

### devices (list, zero or more)

| Value | Test |
|---|---|
| `arrow` | Any arrow |
| `circle` | A ring or highlight circle drawn on |
| `check-x` | A check mark or an X, including green check beside red X |
| `number` | A standalone figure: a count, a dollar amount, a percentage, a multiplier |
| `logo` | A recognizable brand mark anywhere in frame |
| `mockup` | A phone, browser, or device frame around content |
| `money` | Cash, bills, coins |
| `glow` | A deliberate glow or light effect on an element |

## Layer 2: strategy (thumbnail lever)

Already in place. One primary from `references/thumbnail-vision-classification.md`: Cognitive Dissonance, Result, Curiosity, Before/After, Minimal. Social Hack is an enhancer, never a primary. Plus the two anti-pattern flags. No change.

The existing `enhancers` prose field is retired once Layer 1 lands; `devices` and `gesture` carry that information as filterable tags.

## Layer 3: emotional promise (the package)

What the viewer is made to feel, judged from title plus thumbnail together. Multi-select. Stored on the outlier note because the feeling often lives in the title ("You're not behind (yet)") while the image is just a face.

Uses the BENS letters vid-title already scores on, so the title skill and the thumbnail skill speak one vocabulary, plus three the letters miss.

| Tag | Test |
|---|---|
| `B` (Big) | The result claimed is larger than the niche normally hears. A number or outcome that makes you ask "that much?" |
| `E` (Easy) | The path feels short or the bar low: minutes, hack, simple, for beginners, for dummies |
| `N` (New) | Something feels novel or previously hidden: just dropped, nobody tells you, a withheld mechanism |
| `S` (Safe) | Trust is borrowed or earned: a known name or tool, a completed past-tense result, a calm authoritative face |
| `fear` | The viewer is doing something wrong or stands to lose: STOP, DON'T, SUCKS, wrong, the hard way |
| `status` | The viewer ends up ahead of others: 99%, get ahead, winners and losers, better than |
| `contrarian` | The package contradicts what the niche believes: awful idea, sucks actually, why X is bad |

Most packages carry two. Tag every one that passes its test; do not pick a favorite.

## Note schema

Frontmatter on `banks/outliers/{title}.md`. Existing fields unchanged, new fields added.

```yaml
---
type: outlier
project: authentic-ai-os
channel: "@handle"
channel_name: "Name"
bucket: direct                    # own | direct | adjacent | style-only
video_id: abc123DEFgh
url: https://www.youtube.com/watch?v=abc123DEFgh
views: 480000
xmed: 6.2
published: 2025-08-12
strategy: "Result"                # layer 2, unchanged
thumbnail_text: "IT MADE THIS"
thumbnail: "[[thumbnail-abc123DEFgh.jpg]]"
hero: face                        # layer 1 from here down
face: big
expression: shocked
gesture: presenting
layout: single
text_amount: few
text_style: [caps, highlighted]
background: solid
bg_tone: dark
devices: [logo, glow]
promise: [B, N]                   # layer 3
captured: YYYY-MM-DD
tags: [outlier]
---
```

Body keeps the H1 title, the embedded thumbnail, the one-line `**Hero:**` detail (prose stays, it is the description behind the tag), and the `**Packaging read:**` line.

## What this makes filterable

Any Base view or skill query becomes a property match. Examples that were impossible before:

- `hero == "whiteboard"`
- `face == "none"` and `bg_tone == "dark"` and `text_amount == "few"`
- `devices.contains("arrow")`
- `promise.contains("status")` and `strategy == "Result"`
- `expression == "shocked"` grouped by channel, to see who leans on it

The By strategy view in `outliers.base` gets siblings: By hero, No face, Dark and big text, By promise. Exact views to be picked when built, from what the tagged data actually supports.

## What is deliberately not a tag

- Color palette. Nobody filters for "the orange ones." `bg_tone` covers the real decision.
- Motifs like "OLD vs NEW split." Those are combinations of atomic tags (layout split, two text labels), not their own axis. Keep tags atomic and let combinations emerge.
- Anything interpretive about the image alone ("confident," "premium," "authentic"). If it fails the two-people test it does not exist.
