---
type: research-log
project: authentic-ai-os
status: active
last_full_rebuild: {YYYY-MM-DD}
last_refresh: {YYYY-MM-DD}
last_phase_completed: {1-7}
research_window: "{calibrated window, default last 12 months}"
outlier_rule: "raw-view floor scaled per channel (start at 2x median; ~3-4x for normal cadence; higher for hyper-cadence; mega-hits only for giant style channels). 2x is the floor, not the bar."
outlier_count: {N}
channels:
  own: ["@channel-handle"]
  direct: ["@chan1", "@chan2", "@chan3"]
  adjacent: ["@adj1", "@adj2", "@adj3"]
---

# Research Log

What `vid-research` ran and what it found. Not a bank; nothing writing a video reads this. It exists so a refresh can rerun the same channel set, recompute multipliers against each channel's median, and run the fluke filter without asking the creator again.

The evidence itself is [[outliers.base]]. The usable patterns are [[title-bank]] and [[power-words-bank]].

## Channels

| Channel | Bucket | Subs | Median | Floor | Outliers |
|---|---|---|---|---|---|
| [@channel-handle](https://www.youtube.com/@channel-handle) | own | {N} | {N} | {N} | {N} |
| [@chan1](https://www.youtube.com/@chan1) | direct | {N} | {N} | {N} | {N} |
| [@adj1](https://www.youtube.com/@adj1) | adjacent | {N} | {N} | {N} | {N} |

**Channel themes** (from the fluke filter's read of each channel's last 30 titles):

- [[@chan1]]: {primary themes, one line}

## Findings

### Thumbnail strategy distribution

Counts of primary strategy across the outlier notes. Feeds the packaging-system thumbnail bet.

- {Strategy}: {N} outliers across {M} channels

### Visual patterns worth stealing

Cross-channel thumbnail observations. These are the one thing here that cannot be derived from a single outlier note; someone had to look across the whole set to see them.

> [!tip] {pattern name}
> {which channels, how dominant within each, one line on what it breaks or proves}

### Topic clusters (own + niche only, NEVER adjacent)

> [!note] Cluster: {label}
> Topic substance: {what subject matter}
> Members: {wikilinks to outlier notes}
> Why this pulls: {one-sentence hypothesis}

---

**Not part of the file. Build rules, delete this section when writing the creator's log.**

- Store the channel URL, not just the handle. A refresh needs to fetch it again.
- Store each channel's median and floor. The median cannot be rebuilt later from the outlier notes alone, because outliers are only the top slice.
- Store the themes. The fluke filter needs them on the next run and the creator should not be re-interviewed for them.
- Do not put title shapes or power words here. They live in [[title-bank]] and [[power-words-bank]], which are the files writing skills actually read.
- When `packaging-system.md` exists, the visual patterns and strategy distribution inform its thumbnail bet; this file stays the raw record.
