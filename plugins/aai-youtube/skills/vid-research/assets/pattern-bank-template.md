---
type: pattern-bank
project: authentic-ai-os
status: active
last_full_rebuild: {YYYY-MM-DD}
last_refresh: {YYYY-MM-DD}
last_phase_completed: {1-7}
research_window: "{calibrated window, default last 12 months}"
outlier_rule: "raw-view floor scaled per channel (start at 2x median; ~3-4x for normal cadence; higher for hyper-cadence; mega-hits only for giant style channels). 2x is the floor, not the bar."
channels_analyzed:
  own: "@channel-handle"
  direct: ["@chan1", "@chan2", "@chan3"]
  adjacent: ["@adj1", "@adj2", "@adj3", "@adj4", "@adj5"]
  style_only: ["@giant1", "@giant2", "@giant3"]
pattern_count_total: {N}
---

# Pattern Bank

The synthesis + outlier evidence the creator's pattern research produced. The creator's entry point for browsing what works in their space, and the evidence layer behind the sub-banks. Sub-banks for power words and title shapes live in their own files (loaded by vid-title). Thumbnail strategy and visual data live IN the outlier rows below.

## Sub-banks (focused, loaded by writing skills)

- [[title-bank]]: fill-in-the-blank title shapes with worked examples, loaded by vid-title
- [[power-words-bank]]: global + audience-specific power words, loaded by vid-title

## Synthesis (cross-channel insights)

The "what we learned" layer; the outlier rows below are the evidence. Each synthesized pattern carries its spread and attribution so downstream reads derive strength from the data, not a stored label.

Per-pattern shape:

```
> Pattern: titles opening with "STOP [common practice]"
> spread: 6 of 11 channels
> channels: [[@CoachX]], [[@CoachY]], [[@CoachZ]], [[@CoachW]], [[@CoachV]], [[@CoachU]]
> own_channel_proven: false
```

> [!important] Convergent patterns (proven across the most channels)
> Patterns that appear across multiple channels in the niche set, OR convergent between niche and adjacent niches. Widest spread, the strongest signal. Worth testing first.
>
> {populated by Phase 4 synthesis pass, each with spread + channels + own_channel_proven}

> [!note] Niche-specific patterns
> Patterns that appear in 3+ niche channels but not in adjacent. Strong spread for this audience specifically.
>
> {populated}

> [!tip] Adjacent translations (differentiation gold)
> Structural patterns from adjacent niches that haven't been adopted in the niche yet. Highest differentiation potential, thinner spread in this audience.
>
> {populated}

> [!warning] Channel-unique signals (one channel only)
> Patterns from one channel. Spread of one, may or may not transfer. Tag and revisit if testing.
>
> {populated}

## Per-channel raw research

Every qualifying outlier from the window is listed below as a full inventory (the whole set, nothing dropped). The top performers per channel are tagged **[studied]** and get thumbnail-vision classification; lower-tier outliers are URL-saved without vision per the method.

### Own channel: @channel-handle

**Subs:** {N} | **Median ({window}):** {N} | **Outlier floor (per channel):** {N} | **Qualifying outliers:** {count}
**Channel themes:** {primary themes from Prompt 1}

| Views | xMed | Published | Title | Studied |
|---|---|---|---|---|
| {views} | {mult}x | {YYYY-MM-DD} | [{title}]({video_url}) | **[studied]** |
| {views} | {mult}x | {YYYY-MM-DD} | [{title}]({video_url}) |  |

#### Studied outlier: "{title}"

- [Watch on YouTube]({video_url}) | video_id: {11-char id} | @{channel} | {view_count} views ({multiplier}x median) | published {YYYY-MM-DD}
- ![[thumbnail-{video_id}.jpg]]
- thumbnail strategy: {primary, one of 6} (+ enhancers: {0 or more of the 6 layered on top}) | thumbnail text: "{verbatim text}" | hero: {one-line description of primary visual element}
- packaging read: {one line on how the title and thumbnail work together as one unit (what the title says vs. what the thumbnail shows, and the gap or payoff that pulls the click)}

### Direct competitor: @chan1

{same structure: inventory table of ALL outliers, then a studied block per top-N}

### Adjacent: @adj1

{same structure, but extract structural patterns only, never topic patterns}

### Style-only (giant): @giant1

{same structure; mine packaging shape only, never topics, never a view benchmark}

## Considered + dropped

Patterns the creator considered and dropped during Theory of One curation. Rationale captured so future refreshes don't re-surface them.

> [!quote] Dropped: {pattern label}
> Rationale: {one-liner}
> Bucket: {tone-mismatch | audience-sophistication | off-positioning | tested-flopped | authority-conflict | trend-chasing | other}
> Date dropped: {YYYY-MM-DD}

