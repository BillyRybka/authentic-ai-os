---
type: bank
kind: power-words
project: authentic-ai-os
status: active
last_refreshed: {YYYY-MM-DD}
total_words_global: {N}
total_words_audience: {N}
---

# Power Words Bank

Words that carry above-average emotional or curiosity weight in the research outlier set. Two categories: Global (pull on virtually any audience) and Audience-Specific (resonate uniquely for this creator's audience because of domain expertise or jargon).

Loaded by `vid-title` for headline candidate generation, `vid-intro` for hook construction, and `vid-thumbnail` for thumbnail text.

## How to read this bank

This bank is comprehensive: mine every recurring power word from the FULL outlier title set, not a token few. A 100-plus-title set should produce a couple dozen words. "Lean" means no frequency junk, not a short list. Each entry is a word + when it lands + when it fails + a real worked example. No frequency counts, no raw channel counts: those numbers anchor the AI on "this appeared most" rather than "this fits the line being written." The decision is fit-by-context, not popularity. The creator edits this file in place, deleting words they would not use and adding words they prefer.

One word or short phrase per entry. Never combine two distinct words with a slash (for example "REAL" / "TRUTH"). Distinct words land and fail under different conditions, so each needs its own when-it-lands and when-it-fails lines. Downstream title generation also pulls a single word per slot, so a slashed pair gives it nothing clean to select.

## Global power words

Words that pull on virtually any audience. These transcend niches.

### "STOP"

- When this lands: contrarian command framing where the audience is doing something the creator has authority to push back on.
- When this fails: used without a credible "do this instead" replacement; reads as scolding.
- Worked example: "STOP Following This Outdated Programming Advice" → [[pattern-bank#outlier-row]]

### "FAST"

- When this lands: result-oriented payoff for an audience under time pressure.
- When this fails: when the actual content is slow or layered; raises a promise the body cannot keep.
- Worked example: {populated by research}

### "EASY"

- When this lands: relief framing for an audience that has tried complicated solutions.
- When this fails: for sophisticated audiences who read "easy" as oversimplified.
- Worked example: {populated}

### "REAL"

{when this lands / when this fails / worked example}

### "TRUTH"

{when this lands / when this fails / worked example}

### "MISTAKE"

{populated}

### "NEVER"

{populated}

### "FIX"

{populated}

### "NEW"

{populated}

## Audience-specific power words

Words that resonate uniquely for THIS creator's audience because of domain expertise or jargon. Pull only when the audience is sophisticated enough to recognize them; the title-thumbnail combo should signal niche-credibility from the first frame.

### "{audience-specific word 1}"

- When this lands: {why this word resonates uniquely for this audience}
- When this fails: {when this word does not register or backfires}
- Worked example: "{title}" → [[pattern-bank#outlier-row]]
- Caution: may not register for general audiences. Use only when the title-thumbnail combo signals niche-credibility.

### "{audience-specific word 2}"

{...}

## Words avoided (flop signals)

Words that surfaced in flops or that the creator rejected during curation. The skill should AVOID generating titles containing these.

### "{word}"

- Reason avoided: {one-line rationale}
- Bucket: {tone-mismatch | audience-sophistication | brand-off-axis | hype | other}
- Source: {flop analysis | creator drop}

## Considered + dropped

Power words AI proposed that the creator dropped. Rationale captured.

> [!quote] Dropped: "{word}"
> Rationale: {one-liner}
> Date: {YYYY-MM-DD}

## Field reference

- **When this lands**: the conditions under which this word strengthens a title. The fit criterion.
- **When this fails**: the conditions under which this word weakens a title. The guard.
- **Worked example**: a real title from the research, linked back to its full outlier row in `pattern-bank.md` for context.
- **Audience context** (audience-specific words only): why this word resonates uniquely for this creator's audience.

Fields deliberately not captured: `frequency`, `channels_used`, `confidence` rank. The popularity of a word in the research set does not equal its fit for the next title. Fit is judged by the when-it-lands / when-it-fails criteria, not the count.
