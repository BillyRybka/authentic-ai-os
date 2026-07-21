---
type: reference
doc: packaging-bank-schema
project: authentic-ai-os
status: active
tags: [reference, packaging-bank, schema, contract]
---

# Packaging bank schema

The contract for writing packaging entries to `banks/packaging-bank/`. Any packaging reference that works: the creator's own winning title and thumbnail combos plus outliers from other creators worth studying. One bank, one place to look when the planner or generator needs proven packaging to reference.

Title and thumbnail get treated together because they ARE one unit. The title sells the click, the thumbnail sells the click, and the combo is what the algorithm tests. A winning title without its thumbnail context is half the story. A winning thumbnail without its title is half the story.

This bank is written by `vid-measurement` (own winners) and `vid-research` (outliers) when those skills ship. Until then, this schema documents the intended contract.

## Two sources, one bank

Every entry has a `source` field distinguishing where it came from:

- **`source: own`**: the creator's own videos that proved out. Real performance data (CTR vs channel baseline, retention through hook, views).
- **`source: outlier`**: other creators' videos performing significantly above their channel average (2x+ is the rule of thumb). Per standard outlier analysis, study what is working in your niche AND adjacent niches, then extract the packaging pattern.

Both feed the same use case. When `vid-thumbnail` generates concept briefs, it pulls reference packages from here. Over time, own-winners crowd out outliers as the creator builds their own proven style.

## What qualifies as an entry

One file per packaging combo that won. Entry captures:

- The exact title (as published)
- The thumbnail asset (image path)
- The strategy used (Cognitive Dissonance, Before-After, Curiosity, Social Hacking, Result, Minimal)
- The BENS letters it hit (Big, Easy, New, Safe)
- The performance signal (click-through rate, retention through hook, comparison to channel baseline)
- Link to the video it packaged: `[[content/pieces/{slug}]]`

**Add an entry when** a packaging combo clearly outperformed. Do not log every attempt. Only winners. Swipe files are winners only.

## What does NOT qualify

- Third-party frameworks or examples belong in `knowledge/`.
- Title patterns and fill-in-the-blank formulas belong in `banks/title-bank.md`.
- Hook patterns belong in the vid-intro skill's `references/hook-patterns.md` (system reference, not a creator bank).
- Transition patterns belong in `knowledge/transition-patterns.md` (system reference, not a creator bank).
- Losing A/B variants. Winners only.
- Untested concepts. Packages that never got measured against a real audience do not belong.
- Title-only wins without thumbnail context. If the thumbnail data is missing, the entry is incomplete.

## Difference from title-bank.md

- `banks/title-bank.md`: **patterns** (reusable mad-libs like "[Number] Ways to [Outcome] Without [Pain]")
- `banks/packaging-bank/`: **specific wins** (this exact title plus this exact thumbnail plus this exact strategy)

Both exist for different reasons. Patterns give you starting scaffolds, wins give you proven style references.

## Schema

```yaml
---
type: packaging
project: authentic-ai-os
source: own                          # own | outlier
title: "The exact published title"
thumbnail_asset: "banks/packaging-bank/assets/{slug}.png"   # path to the thumbnail image
strategy: cognitive-dissonance       # cognitive-dissonance | before-after | curiosity | social-hacking | result | minimal
bens_letters: [B, N]                 # which BENS letters this package hits
format: deep-dive                    # short-process | case-study | roast | deep-dive | interview | news | listicle

# Only if source: own
piece: "[[piece-slug]]"              # wikilink to content/pieces/ entry
performance:
  ctr: 9.2                            # thumbnail click-through rate %
  vs_baseline: "+3.1%"                # vs creator's channel average
  retention_through_hook: 68          # % of viewers past the 30s mark
  views_30d: 42000

# Only if source: outlier
outlier_source:
  channel: "Channel Name"
  video_url: "https://youtube.com/watch?v=..."
  channel_baseline: 50000             # channel's typical views
  this_video_views: 450000            # how far above baseline
  multiplier: "9x"                    # rough outlier magnitude
  niche_relationship: niche           # niche | adjacent | unrelated

captured: YYYY-MM-DD
status: captured                      # captured | retired
tags: [packaging, source-{own|outlier}, strategy-{slug}, {domain-slug}]
---
```

## Naming

`{short-slug}.md`. Kebab-case.

- Own winners: match the video slug. `first-hire-broke-everything.md`, `quit-my-day-job-2022.md`
- Outliers: prefix with channel or descriptor. `healthygamergg-self-loathing-man.md`
- Bad: `packaging-1.md`, `thumbnail-winner.md`

## Body template

```markdown
# {Exact title as published}

## Thumbnail
![[assets/{slug}.png]]

## The strategy
[One paragraph on WHY this package worked. What tension did the title create that the thumbnail resolved? What BENS letter did each piece hit?]

## Performance
- CTR: {%} (channel baseline: {%})
- Retention through hook: {%}
- Views in first 30 days: {#}
- What told you it was a winner: [the signal. Often a spike relative to recent uploads]

## What to copy going forward
- [1-3 things that made this work. Style elements, tension-pattern, text placement, expression choice]

## Related
- Video: [[content/pieces/{slug}]]
- Similar past winners: [[banks/packaging-bank/other-winner]]
```

## How entries get used

1. **Own winners:** creator publishes video, `vid-measurement` flags a winner, entry logged with full performance data.
2. **Outliers:** creator studies above-baseline videos in their niche or adjacent niches, then logs the ones worth copying with the outlier multiplier noted.
3. `vid-thumbnail` (planner) reads from this bank when generating concept briefs. Pulls both own winners and studied outliers as style anchors, weighting own winners higher once they exist.
4. Over time, own-winners dominate the bank and outliers serve as aspirational references. Retired outliers move to `status: retired` rather than being deleted.

## Assets folder

Thumbnail image files live in `banks/packaging-bank/assets/{slug}.png`. Reference them via Obsidian embed `![[assets/{slug}.png]]` in the entry body.
