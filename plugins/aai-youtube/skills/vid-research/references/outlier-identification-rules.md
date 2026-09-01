---
type: reference
scope: shared
loaded_by: [vid-research, vid-measurement]
status: active
tags: [reference, outliers, research, rules]
---

# Outlier Identification Rules

The rules for deciding which videos count as outliers in pattern research. Examples-first. The core move: a video is an outlier when it clearly beat what is normal for THAT channel's size. 2x the median is the floor you start from, not the bar you stop at. The bar scales per channel.

All examples here are generic placeholders (`@CoachX`, fitness niche). They illustrate the method. Real channel data lives only in the creator's `banks/research-log.md` and their outlier notes, never in this file.

## Why this exists

Pattern research only studies outliers, videos that significantly outperformed what the channel normally does. Studying average videos teaches you what is expected. Studying underperformers teaches you what tanks. Outliers signal what audiences want MORE of, which is the only signal worth scaling.

But "outlier" is fuzzy. A bigger view count alone is not enough, and a flat 2x rule breaks at the edges (it floods on channels that post daily and starves on giants). So the floor scales to the channel.

## The window (calibrated, ask first)

Pull each channel's videos from a set window. **Default is the last 12 months.** Offer to expand to 24 if a channel posts rarely and 12 months is too thin to read. This is a calibration question at the start of a run, not a hardcoded number. Older data is staler (the channel and the platform have moved on), so recent wins weigh more (see Recency below).

When computing the median, exclude shorts (60 seconds or less) and live streams. They have different view dynamics and would skew the picture.

Note on Shorts. The fetch already excludes videos of 60 seconds or less, but platforms now allow longer short-form. So a video that runs far shorter than the channel's normal length should be surfaced as a possible Short rather than silently counted as an outlier, because short-form has different view dynamics.

## The rule: scale the floor to the channel

For each channel, compute the **median** view count over the window (median, not mean, so the outliers do not inflate their own bar). Then set a raw-view floor that represents a genuine breakout for a channel THAT size. Three things move the floor:

1. **Start at 2x the median.** This is the floor of the floor. Below 2x is normal channel variance (a 1.5x video is just a good day). 2x is the minimum to even be a candidate.
2. **For a normal-cadence channel, the real bar is closer to 3 to 4x the median.** A video that did 3 to 4x what the channel usually does clearly caught fire. That is the breakout, not a video that squeaked past 2x.
3. **Push the floor higher when the channel posts constantly.** A channel that uploads near-daily drags its own median down with a pile of low-view videos, which makes 2x trivial to clear. For those, the floor climbs to 8x, 10x, more, until only the real breakouts survive.
4. **For giant, fame-driven channels, only the mega-hits count.** A huge channel's median is already enormous, so 2x is a big number on its own. Keep the floor high (their biggest videos only). Channels are channels: you still study a giant's packaging, the same as any other channel. The only adjustments are two. Do not expect or benchmark its view counts (a chunk of its reach is the name on the channel, not the packaging). And for each spike, check whether it is packaging-driven (a title and thumbnail you can learn from) or fame-driven (it would have spiked no matter the packaging). You are mining these for packaging shape, not benchmarking your reach against theirs.

The AI proposes a floor per channel from the median plus the posting cadence (videos per window) and explains the reasoning. The creator confirms or adjusts. The creator's eye on "is that a real breakout for a channel that size" is the final call.

A second sanity check after the multiple: the raw view count has to be meaningful for the niche. A 600-view video on a 300-view channel is 2x but means nothing; the audience could be one share or one search fluke. If the raw number is too small to trust, it is not an outlier no matter the multiple.

## Worked examples (generic)

**Normal-cadence mid channel.** `@CoachX`, fitness programming, posts weekly, ~50 videos in the window, median 20k. Start: 2x = 40k. Real bar: 3 to 4x = 60k to 80k. A 145k video (7x) is a clear outlier. A 52k video (2.6x) is a solid breakout worth keeping. A 41k video (2x exactly) is borderline, probably just a good week, lean skip.

**Hyper-cadence channel.** `@DailyFitTips`, posts near-daily, ~500 videos in the window, median 4k (dragged down by volume). Start: 2x = 8k, which dozens of videos clear, that is noise. Push the floor up: at ~12x median (48k) only the genuine breakouts remain. Set the floor where the real hits separate from the daily churn, then confirm with the creator.

**Giant fame-driven channel.** `@MegaCreator`, 5M subs, median 300k. 2x = 600k. Keep the floor at the mega-hits only (say 1M+), so you are studying the shape of their biggest packaging. You still learn from this channel, you just do not benchmark a smaller creator's reach against it, and for each mega-hit you check whether it spiked on packaging or on the name. Mark this channel style-only, meaning structure and packaging transfer but view counts do not: take title and thumbnail structure, never view benchmarks.

**Tiny channel below the niche.** `@NewCoach`, median 1.5k. The multiples look huge (a 10k video is 6.7x), but 10k may still be too small to trust for the niche. Surface it to the creator: "this is 6.7x your normal but small for the niche, study it as your own data point knowing the pattern may be small-channel-specific?" The creator decides.

## The fluke filter (always run it)

A high multiple does not make a pattern if the topic is off-niche. A YouTube-marketing channel with 99 videos about thumbnails and one viral video about sewing does not have 100 useful data points. It has 99 plus a fluke.

How to apply it:

1. Summarize the channel's primary themes from its recent video titles.
2. For each candidate outlier, check: is this topic on-niche for the channel?
3. Surface flukes to the creator with context:

```
> [!warning] Possible fluke
>
> Outlier: "I Tried Sewing for 30 Days", 700k views (14x median)
> Channel @CoachX, primary themes: thumbnails, retention, hook writing
>
> This looks off-niche. Likely a one-off spike (cross-promotion, algorithmic luck) that
> will not transfer to the channel's actual audience.
>
> Skip / Study anyway / Flag for manual review
```

Default is skip. The creator can override only with a reason ("this fluke shows my audience is broader than I thought, worth studying"). When they override, capture the audience insight, not the off-niche topic.

## Recency (a weight, not a gate)

Within the window, newer wins weigh more, because the platform shifts.

- Outliers from the last 6 months are the strongest signal.
- Older outliers in the window are useful but mark the date.
- A pattern that shows up in both recent AND older outliers is the most trustworthy, it has held across platform changes.

## Spread, not confidence

When a pattern repeats across multiple channels, that is the real strength signal: it is repeatable, not a one-channel quirk. Record the spread (how many channels, and which ones) on the synthesized pattern. Do not stamp a HIGH/MEDIUM/LOW confidence label; the channel count is the honest signal and a label only skews how the next decision gets made. A pattern proven on the creator's OWN channel is the strongest of all (mark `own_channel_proven: true`).

## Summary

A video is a confirmed outlier when ALL of these hold:

- It clears the channel's scaled floor (start at 2x median, real bar ~3 to 4x for normal cadence, higher for hyper-cadence, mega-only for giants).
- Its raw view count is meaningful for the niche (not a tiny-channel math trick).
- Its topic is on-niche for the channel (passes the fluke filter).
- It falls inside the calibrated window (default 12 months), with recency as a weight.

Anything that fails is skipped (default), surfaced for creator override, or moved to a considered-and-dropped note.

## Common mistakes

- **Treating 2x as the bar.** 2x is the floor. The real breakout for a normal channel is 3 to 4x its median. Stopping at 2x fills the bank with good-week videos.
- **Using mean instead of median.** Outliers inflate the mean and hide themselves. Always median.
- **Including shorts or live streams in the median.** Different view dynamics. Exclude them.
- **Letting hyper-cadence channels flood the bank.** A daily-posting channel clears 2x dozens of times. Raise its floor until only the real breakouts remain.
- **Benchmarking a small creator against a giant.** Giant channels are style-only references, which means their structure and packaging transfer but their view counts do not. Study their packaging shape like any channel. Just do not benchmark your reach against theirs, and check whether each spike was packaging-driven or fame-driven.
- **Auto-skipping flukes without surfacing them.** Sometimes the fluke reveals a real audience insight. Surface with context, let the creator decide.
- **Stamping confidence labels.** Record spread (which channels, how many) instead. The count is the signal; the label skews.
