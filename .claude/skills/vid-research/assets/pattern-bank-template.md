---
type: pattern-bank
project: authentic-ai-os
status: active
last_full_rebuild: {YYYY-MM-DD}
last_refresh: {YYYY-MM-DD}
last_phase_completed: {1-6}
channels_analyzed:
  own: "@channel-handle"
  niche: ["@chan1", "@chan2", "@chan3", "@chan4", "@chan5"]
  adjacent: ["@adj1", "@adj2", "@adj3", "@adj4", "@adj5"]
pattern_count_total: {N}
---

# Pattern Bank

The synthesis + outlier evidence the creator's pattern research produced. The entry point for vid-framing when picking an angle. Sub-banks for power words and title patterns live in their own files (loaded by vid-title). Thumbnail strategy and visual data live IN the outlier rows below (vid-thumbnail-gen, when built, queries this file by strategy match).

## Sub-banks (focused, loaded by writing skills)

- [[title-bank]]: fill-in-the-blank title shapes with worked examples, loaded by vid-title
- [[power-words-bank]]: global + audience-specific power words, loaded by vid-title

## Synthesis (cross-channel insights)

The "what we learned" layer. Patterns that hold across the research set, not individual outliers. vid-framing reads this first when picking angles; outlier rows below are the evidence cited.

> [!important] Convergent patterns (highest confidence)
> Patterns that appear across multiple channels in the niche set, OR convergent between niche and adjacent niches. These are the patterns worth testing first.
>
> {populated by Phase 4 synthesis pass}

> [!note] Niche-specific patterns
> Patterns that appear in 3+ niche channels but not in adjacent. Strong for this audience specifically.
>
> {populated}

> [!tip] Adjacent translations (differentiation gold)
> Structural patterns from adjacent niches that haven't been adopted in the niche yet. Highest differentiation potential.
>
> {populated}

> [!warning] Channel-unique signals (low confidence)
> Patterns from one channel only. May or may not transfer. Tag and revisit if testing.
>
> {populated}

## Per-channel raw research

Each section below shows the WHOLE PACKAGING for studied outliers: title, thumbnail text, thumbnail image, view count, outlier multiplier, extracted patterns. Visual coherence so the creator can see complete title-thumbnail combos in one view. Future vid-thumbnail-gen queries these rows by `thumbnail strategy` to find visual references for novel angles.

### Own channel: @channel-handle

**Channel themes:** {primary themes from Prompt 1}
**Channel median views (last 2 years):** {N}
**Outlier threshold (2x):** {N}
**Outliers studied:** {count}

#### Outlier 1: "{title}"

- [Watch on YouTube]({video_url}) | video_id: {11-char id} | @{channel} | {view_count} views ({multiplier}x channel avg) | published {YYYY-MM-DD}
- ![thumbnail]({local_path or url})
- thumbnail strategy: {one of 6} | thumbnail text: "{verbatim text}" | hero: {one-line description of primary visual element}
- patterns: [[title-bank#T-{N}]], [[power-words-bank#{word}]]

#### Outlier 2: "{title}"

{same shape}

### Niche channel: @niche-channel-1

{same structure}

### Adjacent channel: @adjacent-channel-1

{same structure, but extract structural patterns only, not topic patterns}

## Considered + dropped

Patterns the creator considered and dropped during Theory of One curation. Rationale captured so future quarterly refreshes don't re-surface them.

> [!quote] Dropped: {pattern label}
> Rationale: {one-liner}
> Bucket: {tone-mismatch | audience-sophistication | brand-off-axis | tested-flopped | authority-conflict | trend-chasing | other}
> Date dropped: {YYYY-MM-DD}

## Confirmed winners (vid-measurement feedback)

Patterns proven by the creator's own published videos. Future vid-measurement skill appends here when a video's performance confirms a pattern actually worked for this creator.

> [!success] Confirmed: {pattern label}
> Validated by: [[content/pieces/{slug}]]
> Performance: {view count, CTR, retention}
> Confidence: proven
> Date validated: {YYYY-MM-DD}

## Field reference

Per-outlier fields and why each is captured:

- **video_url / video_id**: stable identifier, clickable back to source for re-verification
- **view_count**: citation evidence ("@channel pulled 145k") for anchor strength sanity-check in vid-framing
- **outlier_multiplier**: the real signal-strength field ("3.5x channel avg"). vid-framing ranks anchors by this, not raw views, to avoid bias toward MrBeast-scale channels
- **published**: recency context. A pattern from 2022 reads differently than from 2025
- **thumbnail image**: visual evidence plus future vid-thumbnail-gen design reference
- **thumbnail strategy**: categorization (one of 6). vid-thumbnail-gen queries by this to find visual matches
- **thumbnail text**: verbatim words on the thumbnail
- **hero element**: primary visual driver. Future vid-thumbnail-gen uses this when the angle does not match top examples in worked references
- **patterns**: wikilinks to title-bank and power-words-bank entries. The cross-reference glue

Fields deliberately not captured: `format` (cannot reliably be inferred from title + thumbnail + metadata; source-fidelity established 2026-05-19 work log).
