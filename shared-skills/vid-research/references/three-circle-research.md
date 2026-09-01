---
type: reference
scope: shared
loaded_by: [vid-research, vid-channel-audit, vid-measurement]
status: active
tags: [reference, research, methodology, outliers]
---

# Three-Circle Research

The methodology for finding patterns that grow channels. Examples-first. Three circles intersect to produce differentiation: your own channel, your niche, and your adjacent niches. Most creators only mine the niche circle and end up copying each other. The breakthroughs come from the intersection.

## Why this exists

Making videos based on what you THINK is a good idea is the dominant failure mode for business channels. Pattern research replaces guesses with hypotheses backed by real data. Three-Circle Research is the structured way to gather that data, never random, never just what's trending, always anchored to channels that share your audience.

## The three circles

```
       ┌──────────────────┐
       │ Your channel     │
       │ (already worked) │
       └────────┬─────────┘
                │
        ┌───────┴───────┐
        │   Your niche  │
        │  (5 channels) │
        │  proven       │
        │  insights     │
        └───────┬───────┘
                │
        ┌───────┴───────┐
        │   Adjacent    │
        │  niches       │
        │  (3-5 chans)  │
        │  differentia- │
        │  tion gold    │
        └───────────────┘
```

Each circle answers a different question. Together they triangulate the patterns most likely to grow YOUR channel.

### Circle 1: Your own channel

**Question:** "What's already worked for me?"

If the channel has any history, this is the fastest, highest-signal research. Find your own outliers (videos that cleared the channel's scaled floor, see `references/outlier-identification-rules.md`). Repeat what worked. The audience that came back already told you what they want.

**Worked example:** A channel averages 200k views per video. One video pulled 700k. That's the channel's most reliable data point, those 700k viewers came back for that specific topic, in that specific frame, with that specific thumbnail style. The next move: repeat it with minimal variation. Change the outfit color. Swap the specific stat. Don't redesign from scratch.

**Worked example (creator's own quote):** "Just use one that already worked and change the color of your outfit, and change the days. And hey presto, 300,000 views."

**When this circle is empty:** brand new channel, fewer than 10 videos, or pivoting from a different niche. Skip Circle 1, start with Circle 2. Build Circle 1 over time as the channel publishes.

### Circle 2: Your niche (5 channels)

**Question:** "What works for audiences just like mine?"

Niche channels share your audience and your problem space. Their outliers tell you what topics, title structures, thumbnail strategies, and formats land for the people you're trying to reach.

**Channel selection criteria:**

- Channel covers the same problem space your channel covers
- Channel has actual outliers to study (not just consistent averages, outliers are the signal)
- Channel has been active in the last 6 months (stale channels = stale patterns)
- Channel size doesn't matter as long as outliers exist (a 50k-sub channel with a real 5x outlier teaches more than a 1M-sub channel with consistent flat performance)

**Reading large channels:** big channels are fine to study. Their outliers still teach packaging shape (title structure, thumbnail composition, format, power words), and that shape is what transfers. The one caution: you cannot expect their view counts. A massive channel with a giant audience can spike on a topic purely because the audience already knows the name, so separate a fame-driven spike from a packaging-driven win. When a large channel's outlier wins on shape rather than name recognition, that's the signal worth extracting. The pattern bank wants what works for cold viewers who don't know you.

**Worked example:** A YouTube growth coach researches 5 niche channels. Channel A's outlier: "Stop Making Boring Thumbnails" (1.4M views), pattern: contrarian command + specific subject. Channel B's outlier: "I Studied 100 Outliers, Here's What Worked" (900k views), pattern: study volume + result tease. Channel C: "5 Hooks That Actually Work in 2026" (700k views), pattern: list + dated specificity + power word "actually." Three different angles, three different hook patterns. The synthesis: the niche audience responds to specificity + contrarian framing.

### Circle 3: Adjacent niches (3-5 channels)

**Question:** "What works for audiences ADJACENT to mine that I can translate?"

This is where most creators fail to look. Adjacent niches share STRUCTURAL patterns with yours, the shape of titles, the thumbnail composition, the format choice, the power word toolkit, without sharing topics. Most differentiation comes from here.

**The translation rule:** adjacent niches give you SHAPES, not subjects. Extract title structures, power words, thumbnail patterns, formats. Never extract topics. If the adjacent channel is about guitar and yours is about drums, the topic doesn't transfer. The "STOP doing this with your hands" thumbnail composition does.

**Worked example (the canonical case):** A yoga channel was stuck at 25k subs. The yoga niche had no usable patterns, every channel copied the same top creator with bad thumbnails and sporadic views. The creator looked at adjacent niches: mobility content and weightlifting content. Both used "before/after" thumbnail compositions and short bingeable tip videos with short clickbait titles, completely different from the 25-minute yoga tutorials that dominated yoga. The creator extracted the structural patterns (before/after composition, scientific dot overlays, shorter bingeable format), applied them to yoga content. First video in the new format: 2.4M views. Second: 8.2M views. Channel went from 25k to 450k subs in 18 months.

**Adjacent niche identification:**

For each niche, several adjacent niches typically exist. Examples:

- Yoga → Mobility, Weightlifting, Athletic Performance
- Drums → Guitar, Piano, Music Theory
- Tax accounting → Bookkeeping, Small Business Finance, Wealth Management
- YouTube growth → Copywriting, Email Marketing, Content Strategy, Personal Branding
- Fitness coaching → Mobility, Athletic Performance, Longevity, Nutrition Science

The adjacent niche either shares the audience problem at a different angle, OR shares the audience type with a different problem. Either pulls structural patterns worth studying.

## Channel selection workflow

Ask the creator first. They know their competitors and the channels they watch better than any guess. The skill's job is to make it easy for them to name those channels, then quietly turn the names into real data. Never open with a generated list.

**Order:**

1. **Ask.** For the niche circle, ask who their direct competitors are. For the adjacent circle, explain adjacent in one plain line and ask if any come to mind. Give them the simple test for a good pick, in plain words:
   - Makes the kind of content they want to be known for (niche), or a similar type of content on a different topic or industry (adjacent).
   - Serves the same kind of viewer, or one their viewer overlaps with.
   - Has a few videos that clearly beat that channel's own normal, ideally within the last couple of years.
2. **Take their list.** Hear all of it. If they come up short of the target, nudge once for more, then move on.
3. **Suggest only to fill gaps.** If the creator is genuinely stuck, offer a couple of channels you believe fit, built from the ones they already named plus the known players in that space. A couple at a time, never a long list.
4. **Enrich and confirm.** Resolve every named or suggested channel through the API and reflect back the real data so the creator confirms on facts, not blind trust. For each channel you surface:
   - Channel handle and recent themes (from recent video titles)
   - Subscriber count and a recent standout video or two
   - Why it fits the circle (one plain line)

Final set: about 5 niche, plus 3 to 5 adjacent, plus the creator's own = roughly 9 to 11 channels per session.

## Outlier identification within each circle

Same method applies in all three circles:

1. Compute the channel's median views over the calibrated window (default 12 months), excluding shorts and live streams.
2. Set a floor scaled to the channel: start at 2x median, real bar ~3 to 4x for normal cadence, higher for hyper-cadence channels, mega-hits only for giants. The raw count still has to be meaningful for the niche.
3. Identify every video that clears the floor (the full set, not just the top one).
4. Run the fluke filter: is the outlier on-niche for the channel's primary themes? Off-niche flukes don't transfer to the audience and shouldn't be studied.

See `references/outlier-identification-rules.md` for full implementation.

## What gets extracted per circle

Different circles produce different pattern types. The extraction rules:

| Pattern type | Own channel | Niche | Adjacent |
|---|---|---|---|
| Topics | YES | YES | NO |
| Title structures | YES | YES | YES |
| Power words | YES | YES | YES |
| Thumbnail patterns | YES | YES | YES |
| Formats | YES | YES | YES |
| Things-viewers-hate (flops) | YES | YES | NO |
| Production style | YES | YES | LIGHT |

The "topics from adjacent NO" rule is non-negotiable. Adjacent niches translate structural patterns, not subject matter.

## Cross-channel synthesis

After all 3 circles are researched, synthesize:

- **Convergent patterns:** appear across multiple channels and across multiple circles. Widest spread, the strongest signal. Worth testing first.
- **Niche-specific patterns:** appear in 3+ niche channels. Strong spread for this audience.
- **Adjacent translations:** structural patterns from adjacent niches not yet used in the niche. Highest differentiation potential, thinner spread in this audience (untested here).
- **Channel-unique signals:** patterns from one channel only. Spread of one, may or may not transfer. Tag and revisit if testing.

The synthesis output drives Theory of One curation: which patterns DOES the creator's audience already expect from them? Which would feel surprising but earned? Which are too far?

## The Theory of One filter

The most important rule: **just because a pattern worked for another channel does not mean it will work for yours.**

Filter every pattern through:

- Does this fit my audience's expectations of me?
- Would this feel earned, or would it feel like I'm chasing a trend?
- What's my credibility for this angle? Can I deliver on it?
- Has my audience already given me permission to do this kind of video?

A pattern that showed wide spread across channels can still be a wrong fit for the creator's specific audience. The creator's call, always. The pattern bank captures the data; the creator decides what to test.

## Cadence

- **First build:** 1.5-3 hours for the full Three-Circle session. Captures the initial bank.
- **Quarterly refresh:** 30-45 minutes. Pulls new outliers since last refresh. Sticky-curated patterns persist.
- **Single outlier add:** 5-10 minutes between full sessions. Creator captures one outlier they spotted.
- **Full rebuild:** every 6-12 months. Refreshes adjacent niches (which shift faster than your own niche).

The pattern-spotting muscle improves with reps. Early sessions feel slow as the creator builds intuition for what's a real pattern vs noise. Later sessions feel fast because the creator's own taste is calibrated.

## Common mistakes

- **Researching only your niche.** The dominant mistake. Produces convergent copycat output. Always include adjacent niches.
- **Extracting topics from adjacent niches.** Topics don't transfer. The yoga channel doesn't make weightlifting videos. It applies weightlifting THUMBNAIL composition to yoga topics.
- **Studying flukes as if they were patterns.** A 700k-view video on a channel with 50k average is interesting only if it's on-niche. If it's a one-off off-topic spike, the pattern data is noise.
- **Skipping the Theory of One filter.** AI gives you 30 patterns. The creator says "all keep" without considering audience fit. Result: pattern bank polluted with patterns the audience won't engage with. Always filter.
- **Mistaking a fame-driven spike for a packaging-driven win.** Large channels are worth studying, but some of their outliers win on name recognition, not packaging. Don't expect their view counts on your own channel, and check whether a large channel's outlier is carried by the shape (title, thumbnail, format) or just the brand. Extract the shape; ignore the fame.
- **Treating the pattern bank as static.** The bank decays. Adjacent niches shift fastest (a 6-month-old adjacent niche pattern may already be exhausted). Quarterly refresh keeps signal fresh.
