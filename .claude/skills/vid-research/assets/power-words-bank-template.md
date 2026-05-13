---
type: bank
kind: power-words
project: youtube-content-os
status: active
last_refreshed: {YYYY-MM-DD}
total_words_global: {N}
total_words_audience: {N}
---

# Power Words Bank

Words that carry above-average emotional or curiosity weight, repeating across high-performing titles. Two categories: Global (work everywhere) and Audience-Specific (work for THIS audience).

Loaded by `vid-title` for headline candidate generation, `vid-intro` for hook construction, and `vid-thumbnail` for thumbnail text. Each entry includes confidence + frequency + worked example titles.

## How to read this bank

- **Frequency** = number of outliers in the research session that used this word
- **Channels** = how many distinct channels in the research used this word
- **Confidence** = HIGH (4+ channels) / MEDIUM (2-3 channels) / LOW (1 channel)
- **Status** = curated (creator approved) / draft-pending-curation / dropped
- Worked examples come from the actual research data, never invented

## Global power words

Words that pull on virtually any audience. These transcend niches.

### "STOP"
- Frequency: {N}
- Channels: {M}
- Confidence: HIGH
- Status: curated
- Worked examples:
  - "STOP Following This Outdated Programming Advice" — @CoachX, 145k views
  - "STOP Resting 3 Minutes Between Sets (Do This)" — @CoachY, 88k views
- When this lands: contrarian command framing where the audience is doing something the creator has authority to push back on
- When this fails: when used without a credible "do this instead" replacement; reads as scolding

### "FAST"
- Frequency: {N}
- Confidence: HIGH
- Worked examples: {populated}

### "EASY"
{populated}

### "REAL" / "TRUTH"
{populated}

### "MISTAKE"
{populated}

### "NEVER"
{populated}

### "FIX"
{populated}

### "NEW"
{populated}

## Audience-specific power words

Words that resonate uniquely for THIS creator's audience based on their domain expertise or jargon. Pull these only when the audience is sophisticated enough to recognize them.

### "{audience-specific word 1}"
- Frequency: {N}
- Channels: {M}
- Confidence: {HIGH | MEDIUM | LOW}
- Status: curated
- Audience context: {why this word lands for this audience specifically}
- Worked examples:
  - "{title}" — @channel, {views}
- Caution: this word may not register for general audiences. Use when the title-thumbnail combo signals niche-credibility from frame one.

### "{audience-specific word 2}"
{...}

## Words avoided (flop signals)

Words that surfaced in flops or were rejected by the creator during curation. Skill should AVOID generating titles containing these.

### "{word}"
- Reason avoided: {one-line rationale}
- Bucket: {tone-mismatch | audience-sophistication | brand-off-axis | etc}
- Source: {flop analysis | creator drop | etc}

## Considered + dropped

Power words AI proposed that the creator dropped. Captured rationale prevents re-surfacing.

> [!quote] Dropped: "{word}"
> Rationale: {one-liner}
> Date: {YYYY-MM-DD}

