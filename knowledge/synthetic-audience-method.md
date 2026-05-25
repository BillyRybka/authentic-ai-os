---
type: reference
doc: synthetic-audience-method
project: authentic-ai-os
status: active
tags: [reference, audience, synthetic, method]
---

# Synthetic Audience Method

The load-bearing reference for the `aud-*` skill family. Every audience skill loads this file at session start. If you are reading this as a skill, treat the checklists as literal instructions, not suggestions.

## What this system is and isn't

The system builds 4-6 synthetic avatars from real call transcripts and YouTube comments, then runs those avatars as a pre-publish panel over scripts, emails, titles, thumbnails, hooks, and CTAs. The panel produces a verdict, top-3 fixes, dimension scores, and a verbatim dissent block.

**It is** a fast critic that surfaces vocabulary mismatches, missed objections, and friction points using real audience language.

**It is not** an oracle. It does not predict CTR, conversion, or watch time. It does not replace customer interviews. It degrades fast without ongoing real human input.

## Research grounding (the short version)

The mechanism comes from Toubia, Gui, Peng, Merlau, Li, Chen, *Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions* (Marketing Science, Columbia Business School, 2025). 2,058 US participants, 500+ questions, ~2.4 hours per person across 4 waves. Twins built by narrative synthesis of survey answers reached ~88% of the test-retest reliability ceiling on held-out questions.

Two corrections people get wrong:

1. **"88% accuracy" is sloppy.** It is 88% of the ceiling set by humans re-answering their own questions 2 weeks later. That ceiling sits around 0.7-0.8 absolute. So absolute predictive accuracy on well-built twins is closer to 0.6-0.7. At small-business scale (one creator's calls + comments) we are well below this. Treat outputs as directional, never predictive.

2. **The Funhouse Mirror paper matters.** Hewitt et al., *Digital Twins are Funhouse Mirrors: Five Systematic Distortions* (arxiv 2509.19088, 2025) names five distortions that hit LLM personas: majority overweighting, exaggerated agreement, demographic stereotyping, position bias inside the prompt, and sycophancy toward the asker. Half the guards in this method exist to fight these distortions.

## The contamination checklist

Used by `aud-intake` to flag entries that may be LLM-generated, not human. Flag any entry that hits **2 or more** of the following. One match is not enough.

### Surface tells (lexical)
1. Em-dashes (`—`) used as punctuation, especially more than once per entry
2. Filler words common in LLM output: `delve`, `delving`, `tapestry`, `navigating`, `treasure trove`, `robust`, `seamless`, `elevate`, `cultivate`, `harness`, `unlock`, `landscape` (as metaphor), `realm`, `intricate`, `multifaceted`
3. Hedging phrases: `it's important to note`, `it's worth noting`, `in conclusion`, `in summary`, `furthermore`, `moreover`, `that said`, `it's crucial to`
4. Suspiciously formal contractions or no contractions at all in casual contexts (a comment that says "do not" instead of "don't" is suspect; an email that says neither over 500 words is suspect)

### Structural tells
5. Suspiciously uniform sentence length across an entire entry (no short bursts, no run-ons, mean length within ±2 words across paragraphs)
6. Parallel construction with no broken thoughts. Three or more lists/paragraphs that match each other's exact shape, no asymmetry
7. Zero typos, zero abbreviations, zero ALL CAPS, zero exclamation marks in a 500+ word entry from a presumed casual source (comment, DM, forum)
8. A perfect open-middle-close arc on what should be a short comment (12-word comments don't need conclusions)

### Worked examples

**Contaminated example A** (do flag):
> "The journey of mastering guitar is multifaceted — it requires navigating the intricate landscape of music theory while cultivating the muscle memory needed to truly elevate one's playing. It's worth noting that consistent practice unlocks the door to mastery."
>
> Hits: em-dash, "multifaceted", "navigating", "intricate landscape", "cultivating", "elevate", "it's worth noting", "unlocks the door". 8 tells. Strip.

**Contaminated example B** (do flag):
> "I think there are three main reasons people stop playing guitar. First, they lack a structured practice routine. Second, they don't see immediate progress. Third, they don't have a community of fellow players. Each of these can be addressed with the right approach."
>
> Hits: zero typos, perfect parallel construction, zero contractions, three balanced points with a clean wrap. 4 tells. Strip.

**Clean example A** (do NOT flag):
> "honestly i bought 4 courses already and im stuck. like i can play chords ok but improvising over a 12 bar makes my brain melt. dunno if more courses is the answer"
>
> Lowercase, typos, "dunno", real frustration, casual structure. Clean human. Keep.

**Clean example B** (do NOT flag):
> "Been playing 15 years. The thing nobody tells you is your ear gets ahead of your hands. You hear what you want to play, fingers won't catch up. Maddening."
>
> Specific lived detail, asymmetric sentences, opinion that's not balanced. Clean human. Keep.

### Action when flagged
- Mark `verified_human: needs_review`
- Surface in a single batched table at end of intake
- Default: keep with the flag. Billy can strip in bulk.
- Do NOT block on per-entry confirmation.

## The 5 moment types for call extraction

Used by `aud-intake` when processing call transcripts. Extract quote-level units ONLY when they match one of these. Everything else is small talk and gets dropped.

1. **I-am moment.** The speaker describes themselves. Identity, situation, role, life stage. Example: *"I've been playing on and off for 15 years but I'm not really a player, you know."*
2. **I-tried moment.** What they did before. Other products, courses, DIY attempts, free content. Example: *"I bought the Teachable course, did maybe half of it, then drifted."*
3. **I-fear moment.** What they're avoiding, anxious about, embarrassed by. Often the loudest signal. Example: *"I don't want to be the guy who's still playing the same five chords in five years."*
4. **I-want moment.** The outcome they describe, in their words. Often a paraphrase of a problem in positive form. Example: *"I want to walk into a jam and actually contribute, not just nod."*
5. **I-pushed-back moment.** Objections, hesitations, "yeah but..." statements. The most useful for objection prediction. Example: *"How is this different from the four other things I already paid for?"*

Extract each unit as a verbatim quote with: speaker, source line ref, moment type, segment guess (one-word label, can be refined later).

## Held-out protocol

Used by `aud-avatar-build`. Non-negotiable.

1. After clustering, identify each segment's strongest 25-30% of quotes (most distinctive, most representative).
2. Write these to `audience/held-out/{segment-slug}.md` BEFORE drafting any avatar prose.
3. The avatar drafting step runs in a separate skill invocation with explicit instruction: "Do not read from `audience/held-out/`. The held-out file is reserved for validation."
4. `aud-validate` is the only skill that reads from `audience/held-out/`.

This separation has to live on disk. Working-memory promises don't survive context windows.

## Novel-word definition

Used by `aud-validate` test 3 (vocabulary leak). Deterministic.

A word is **novel** to an avatar if BOTH conditions hold:
- (a) The word does NOT appear as a stem-match in any source quote cited by that avatar (stem-match: same first 4 letters or same root, e.g., "playing" matches "play", "improvise" matches "improvising")
- (b) The word does NOT appear in `knowledge/common-english.txt`

Stop words, articles, prepositions, and connectives are never novel.

**Pass threshold:** <= 15% novel words across a 100-word self-description.

## Validation thresholds

Used by `aud-validate`. All thresholds are encoded here, not in the skill. Skill reads from this file.

| Test | Pass threshold |
|---|---|
| Test 1: Quote attribution (10 mixed quotes, 5 own + 5 from another avatar's held-out) | >= 7/10 correct |
| Test 2: Objection prediction (top 3 vs held-out actual) | >= 2/3 match in substance |
| Test 3: Vocabulary leak (100-word self-description) | <= 15% novel |

**Tiered outcomes:**

- Pass test 1 + test 3 only → `status: validated-vocabulary`. Usable for vocabulary checks, objection surfacing, friction detection. Not trusted for behavioral predictions.
- Pass all three → `status: validated-full`. Usable for any review type.
- Anything less → `status: draft`. Cannot be invoked by `aud-review`.

## Scoring dimensions and trigger rules

Used by `aud-review` synthesis. Five dimensions, scored 0-10 by each avatar:

1. **Clarity.** Did the avatar correctly describe the offer/idea after reading the piece?
2. **Resonance.** Did the language match the avatar's vocabulary?
3. **Believability.** Did skeptic-flavored avatars get triggered? Did claims feel earned?
4. **Friction.** Where did the avatar want to leave? Lower is better (10 = no friction, 0 = bailed immediately).
5. **CTA strength.** Would the avatar take the action asked? Only scored when the piece has a CTA.

**Consensus rule: median, never mean.** A single skeptic should not get averaged out.

**Trigger rules:**
- Median < 7 on any dimension → REWRITE
- Any avatar's min on any dimension < 4 → REWRITE
- Median >= 7 across all + no min < 4 → SHIP
- Anything between → FIX-THEN-SHIP

**Dissent capture:** any avatar review scoring 3+ points below the median on any dimension gets a dissent block in the synthesis with the avatar's reasoning quoted verbatim. Dissent is read FROM the per-avatar response files, not from working memory.

## Banned vocabulary in Billy-facing output

Never use in any skill output Billy reads:
- `test-retest reliability`
- `p-value`
- `confidence interval`
- `statistical significance`
- `Bayesian` or `prior`
- `cosine similarity`

These are jargon Billy does not have a model for. Translate to plain-English actionable statements. Example: instead of "low test-retest reliability on Mike," write "Mike confused his own quotes with another avatar's twice. Use him for vocabulary, not tone."

## Rotating disclaimers

Three variants. `aud-review` picks one per run randomly. Every 10th run, append the calibration check regardless.

**Variant 1 (under verdict):**
> Heads up: this synthesis comes from 4-6 synthetic avatars built from your calls and comments. Useful for vocabulary fit and missed objections. Not a CTR predictor. Real customer calls remain the source of truth.

**Variant 2 (callout mid-report):**
> [!warning] Read this before acting
> The avatars are language mirrors, not behavior predictors. If a fix below feels wrong, your gut beats the panel. Run the change past one real customer before publishing.

**Variant 3 (above the rewrite brief):**
> The rewrite brief below is grounded in real audience language but built from a small sample. Use it as a starting point, not a final draft.

**Calibration check (every 10th run, mandatory):**
> When did you last add real call transcripts to `inbox/audience/calls/`? If it has been more than 60 days, these avatars are drifting from your real audience. Run `aud-intake` before you trust this review.

## What this method does and doesn't do

**Does:** surface objections Billy forgot, flag vocabulary mismatches, score friction points, identify tone-deaf framing, generate evidence-grounded rewrite briefs.

**Doesn't:** predict view counts, replace customer interviews, score independently of source data depth, stay accurate without ongoing real human input.

If a skill output ever crosses into "this will get X views" or "this will convert at Y%", that output is wrong and should be flagged.

## References

- Toubia, O., Gui, G., Peng, T., Merlau, D., Li, A., Chen, H. (2025). *Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions.* Marketing Science. Columbia Business School Digital Twins Lab.
- Hewitt et al. (2025). *Digital Twins are Funhouse Mirrors: Five Systematic Distortions.* arxiv 2509.19088.
- Crowd Copy approach: Justin Book demo (Greg Eisenberg event, January 2026) on Mind Studio. Rebuilt on Claude Code by the YouTuber referenced in soptxNjjBVI.
