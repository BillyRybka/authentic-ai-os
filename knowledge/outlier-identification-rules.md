---
type: reference
scope: shared
loaded_by: [vid-research, vid-measurement]
status: active
tags: [reference, outliers, research, rules]
---

# Outlier Identification Rules

The rules for identifying which videos count as outliers in pattern research. Examples-first. Three layers: the 2x rule, the raw-count threshold, and the fluke filter.

## Why this exists

Pattern research only studies outliers — videos that significantly outperformed channel average. Studying underperformers teaches you what tanks, which is useful but separate. Studying average videos teaches you what's expected, which is unhelpful. Outliers signal what audiences want MORE of, which is the only signal worth scaling.

But "outlier" is fuzzy. A bigger view count alone isn't enough. Need three layers of filtering to separate real signal from noise.

## Layer 1: The 2x rule

**Rule:** A video qualifies as an outlier candidate if its view count is at least 2x the channel's recent average.

**How to compute channel average:**

- Pull the channel's videos from the last 2 years (older data is stale, channel may have evolved).
- Exclude shorts (60 seconds or less) — different content type, different ranking signals.
- Exclude live streams — different format, often performance-skewed by drop-in views.
- Compute median of remaining videos' view counts (median, not mean — outliers themselves would skew the mean).

**Why 2x:** below 2x is within normal channel variance. 1.5x performance is noise (any given video can hit that on a normal day). 2x signals something genuinely caught fire that other videos didn't.

**Worked example:** A channel's median over last 2 years is 80,000 views. Outlier threshold = 160,000 views. A video at 145k views: not an outlier (close but inside variance). A video at 220k views: outlier candidate (passes Layer 1, must clear Layer 2 next).

**Edge case — small channels:** if median is fewer than 1,000 views, the 2x rule is mathematically too easy to clear. Apply the raw-count threshold (Layer 2) more strictly.

## Layer 2: The raw-count threshold

**Rule:** The video's absolute view count must be meaningful for the niche, not just relative to the channel.

This is the "common sense over math" layer. A 600-view video on a 300-view-average channel passes Layer 1 (2x the average) but is NOT an outlier in the meaningful sense. 600 views is too small for nearly any niche to teach a real lesson — the data set is too thin and the audience may have come from one share, one search query, one accident. The pattern can't be trusted.

**The threshold is niche-relative.**

Compute the niche's typical view count:

1. Take all niche channels in the research session (Circle 2 — 5 channels).
2. Compute each channel's median view count (using Layer 1 method).
3. Take the median of those medians. Call this "niche-typical."
4. The raw-count threshold for outliers is **at least 50% of niche-typical**.

**Worked example:** Researching the YouTube growth niche. Five niche channels analyzed. Their medians: 80k, 120k, 200k, 60k, 180k. Niche-typical median = 120k. Raw-count threshold = 60k.

Now consider a candidate outlier on a small niche channel: channel median 30k, video pulled 90k. Layer 1: 3x the average, passes. Layer 2: 90k > 60k threshold, passes. Confirmed outlier.

Consider another candidate: channel median 5k, video pulled 18k. Layer 1: 3.6x average, passes. Layer 2: 18k < 60k threshold, FAILS. Not an outlier for this niche. Skip.

**Why this matters:** prevents the pattern bank from being polluted with patterns from videos that simply caught a friend share, a small subreddit boost, or a one-time algorithmic spike that doesn't represent what the niche audience really wants.

**Edge case — your own channel below niche-typical:** a creator's own channel may be smaller than the niche typical. Still apply the threshold for OWN-channel outliers but with creator confirmation: "Your channel's outlier at 18k views is small for the niche-typical 120k. Want to study it as your own data point, knowing the pattern may be small-channel-specific?" Creator decides.

## Layer 3: The fluke filter

**Rule:** The outlier must be on-niche for the channel's primary themes. Off-niche flukes don't represent what works for the audience.

This is the underwater-basket-weaving filter. A YouTube marketing channel with 99 videos about thumbnails, retention, and hooks — and one viral video about sewing — does not have 100 useful data points. It has 99 data points + 1 fluke. The sewing video's pattern doesn't transfer to the channel's actual audience because the audience that watches the sewing video probably isn't the channel's regular audience.

**How to apply the fluke filter:**

1. AI summarizes the channel's primary themes from the last 30 video titles.
2. For each candidate outlier (passed Layers 1 and 2), AI checks: is this video's topic on-niche for the channel?
3. Surface fluke flags to the creator with full context:

```
> [!warning] Possible fluke
> 
> Outlier: "I Tried Sewing for 30 Days" — 700k views
> Channel @YouTubeMarketingPro — primary themes: thumbnails, retention, hook writing, scripting
> 
> This outlier appears off-niche for the channel. Likely a fluke (algorithmic spike, 
> cross-promotion, or one-off curiosity hit). Pattern data from off-niche flukes 
> typically doesn't transfer to the channel's actual audience.
> 
> Skip / Study anyway / Flag for manual review
```

4. Default = Skip. Creator can override only with rationale ("this fluke shows my audience is broader than I thought, want to study it").

**Why default skip:** off-niche flukes pollute patterns. A channel that gets 700k on a sewing video, applied to thumbnail strategy research, would suggest "show your hands doing a craft" as a thumbnail pattern that pulls. But the channel's regular audience came for thumbnail teaching, not crafts. The pattern is a misattribution.

**When to override:** when the fluke reveals something genuine about the audience the creator didn't realize. "My YouTube marketing audience apparently also responds to creator-process content — interesting." Capture the insight, not the topic.

## Layer 4 (optional): Recency check

For any outlier candidate that passes Layers 1-3, also check recency:

- If the outlier was published 24+ months ago, the platform context has shifted enough that the pattern may be stale. Flag with `published: {date}, age: {months}` in the bank.
- Outliers from the last 12 months are highest signal.
- Outliers from 12-24 months ago are useful but should be marked.
- Outliers older than 24 months can be excluded entirely from primary pattern bank (live in archived section if creator wants the historical record).

This isn't a hard filter — recency is more of a confidence weight than a yes/no. Patterns that converge across recent AND older outliers are highest confidence (proven across multiple platform iterations).

## Threshold confirmation summary

A video qualifies as a confirmed outlier when ALL of the following are true:

- View count ≥ 2x channel median (Layer 1)
- View count ≥ 50% of niche-typical median (Layer 2)
- Topic is on-niche for the channel's primary themes (Layer 3)
- Published within last 24 months for primary bank (Layer 4 — soft preference, not hard filter)

Anything that fails any layer is either skipped (default), flagged for creator override, or moved to an archived/considered-and-dropped section.

## Worked end-to-end example

**Scenario:** researching a fitness-coaching channel for the creator's pattern bank. Channel @CoachX has been active 3 years.

**Pull last 2 years of @CoachX videos (excluding shorts and live streams):**

- 47 videos found
- View counts: 12k, 8k, 22k, 15k, 9k, 14k, 145k, 11k, 18k, ... (sorted)
- Median: 18k

**Identify Layer 1 candidates (≥ 2x median = ≥ 36k):**

- Video A: 145k — passes
- Video B: 80k — passes
- Video C: 52k — passes
- Video D: 38k — passes (just over threshold)
- 4 candidates total

**Compute Layer 2 threshold:**

- Niche-typical (from 5 niche channels' medians): 80k
- Layer 2 threshold = 40k

**Apply Layer 2:**

- Video A: 145k > 40k — passes
- Video B: 80k > 40k — passes
- Video C: 52k > 40k — passes
- Video D: 38k < 40k — FAILS Layer 2. Skip from primary bank, capture in considered-but-too-small section.

**Apply Layer 3 fluke filter on remaining 3:**

- Video A: "5 Lifts I Wish I Started With" — on-niche (fitness, lift programming) — passes
- Video B: "Why I Quit My 9-to-5 to Coach" — on-niche but personal/business — borderline, surface to creator: "this is on-niche-adjacent (your story, not lift programming), worth studying as a different content type or fluke?" Creator says: "study it, this is the personal-brand thread my audience also engages with." Confirmed outlier.
- Video C: "How My Wife Reorganized Our Pantry" — off-niche (channel is fitness, not home org) — FLAGGED FLUKE. Default skip. Creator confirms skip.

**Final outlier set: Videos A and B.** These get full pattern extraction (vision-classify thumbnails, extract title patterns, identify formats, log power words). Video C is captured in `## Considered + dropped` appendix with rationale "off-niche fluke per Layer 3."

**Time spent on filtering:** roughly 3-5 minutes per channel. Done.

## Common mistakes

- **Using mean instead of median for channel average.** Outliers themselves skew the mean upward, making the threshold artificially high and missing real outliers. Always median.
- **Including shorts in the average computation.** Shorts have different view dynamics. Including them either inflates the average (channels that ride shorts) or makes outliers easier to clear artificially. Exclude shorts and live streams.
- **Skipping Layer 2 for small channels.** Producing pattern data from 600-view videos on 300-view channels gives the creator confidence in patterns that haven't actually been tested at meaningful scale. Always apply niche-typical threshold.
- **Auto-skipping fluke flags without creator review.** Sometimes the "fluke" reveals genuine audience insight. Surface with context, let creator decide. Don't silently drop.
- **Treating 2-year-old outliers as fresh signal.** Platform changes shift what works. Mark recency on every captured outlier so future runs can re-validate.
