---
type: outlier
project: authentic-ai-os
channel: "@CoachX"
channel_name: "Coach X"
bucket: direct                  # own | direct | adjacent | style-only
video_id: abc123DEFgh
url: https://www.youtube.com/watch?v=abc123DEFgh
views: 480000
xmed: 6.2
published: 2025-08-12
strategy: "Cognitive Dissonance"  # one of the 6 in thumbnail-vision-classification
thumbnail_text: "I WAS WRONG"
thumbnail: "[[thumbnail-abc123DEFgh.jpg]]"
hero: face                      # face | screenshot | object | whiteboard | logo | text
face: big                       # none | small | medium | big
expression: neutral             # neutral | shocked | smile | smirk | excited | defeated
gesture: none                   # none | pointing | presenting | shushing | open-hands | thumbs
layout: single                  # single | split | collage | text-dominant
text_amount: few                # none | few | phrase
text_style: [caps, highlighted] # caps | handwritten | highlighted | boxed | outlined
background: solid               # solid | gradient | real | screenshot
bg_tone: dark                   # dark | light
devices: []                     # arrow | circle | check-x | number | logo | mockup | money | glow
promise: [contrarian, S]        # B | E | N | S | fear | status | contrarian
captured: YYYY-MM-DD
tags: [outlier]
---

# Why I Cut My Squat 20% After Coaching 100+ Lifters

![[thumbnail-abc123DEFgh.jpg]]

**Hero:** {one line, the primary visual element driving the thumbnail}

**Packaging read:** {one line: how title and thumbnail work as one unit; the gap or payoff between what the title says and what the thumbnail shows that pulls the click}

---

One note per outlier. The note IS the winning package: title (the H1), thumbnail (embedded), and the receipts (frontmatter numbers). File name: the video title, sanitized, trimmed to ~60 chars. Dedup by `video_id` in frontmatter, never by file name. Thumbnails save to `banks/outliers/thumbs/thumbnail-{video_id}.jpg`.

Three tag layers, all filterable in `outliers.base`: `strategy` is the lever (Layer 2, from `references/thumbnail-vision-classification.md`). `hero` through `devices` are visual facts read off the image alone (Layer 1, vocabularies and per-tag tests in the same reference). `promise` is the emotional promise of title plus thumbnail together (Layer 3, Prompt 6 in `references/pattern-extraction-prompts.md`). Every tag comes from a fixed vocabulary; never invent a value. `expression` and `gesture` are omitted when `face` is `none`. Delete this trailing note-to-self section when writing real entries; everything above the divider is the entire entry.
