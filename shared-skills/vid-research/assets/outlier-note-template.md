---
type: outlier
project: authentic-ai-os
channel: "@CoachX"
bucket: direct                  # own | direct | adjacent | style-only
video_id: abc123DEFgh
url: https://www.youtube.com/watch?v=abc123DEFgh
views: 480000
xmed: 6.2
published: 2025-08-12
strategy: Cognitive Dissonance  # one of the 6 in thumbnail-vision-classification
enhancers: [Social Hack]        # zero or more, layered on the primary
thumbnail_text: "I WAS WRONG"
thumbnail: "[[thumbnail-abc123DEFgh.jpg]]"
captured: YYYY-MM-DD
tags: [outlier]
---

# Why I Cut My Squat 20% After Coaching 100+ Lifters

![[thumbnail-abc123DEFgh.jpg]]

**Hero:** {one line, the primary visual element driving the thumbnail}

**Packaging read:** {one line: how title and thumbnail work as one unit; the gap or payoff between what the title says and what the thumbnail shows that pulls the click}

---

One note per outlier. The note IS the winning package: title (the H1), thumbnail (embedded), and the receipts (frontmatter numbers). File name: the video title, sanitized, trimmed to ~60 chars. Dedup by `video_id` in frontmatter, never by file name. Thumbnails save to `banks/outliers/thumbs/thumbnail-{video_id}.jpg`. Delete this trailing note-to-self section when writing real entries; everything above the divider is the entire entry.
