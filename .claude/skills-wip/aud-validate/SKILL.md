---
name: aud-validate
description: Run the three-test validation gate on each draft avatar. Quote attribution, objection prediction, vocabulary leak. Sets tiered status (validated-vocabulary or validated-full). Third skill in the synthetic-audience pipeline, gates avatars from being used by aud-review. Triggers on "validate my avatars", "test my avatars", "run validation", "aud-validate", or whenever the creator has draft avatars in audience/avatars/ that need to be tested before use.
---

# Avatar Validate

The gate. Three tests per avatar. Tiered outcome. Without this gate, the rest of the system is theater.

This runs after `aud-avatar-build`. It is the ONLY skill allowed to read from `audience/held-out/`.

## Load at session start

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

1. `.claude/skills-wip/synthetic-audience-method.md`. Validation thresholds, novel-word definition, banned Billy-facing vocabulary. Non-negotiable.
2. `references/common-english.txt`. Used by test 3. ~1,000 most-common English words; grows over time as needed.
3. `.claude/skills-wip/vault-integration-aud-schemas.md`. Avatar and avatar-validation frontmatter schemas.

## Contract

**Inputs (required):**
- One or more avatars in `audience/avatars/{slug}.md` with `status: draft`
- Matching held-out files in `audience/held-out/{segment-slug}.md` for each draft avatar

**Outputs:**
- Validation reports at `audience/avatars/{avatar-slug}-validation-{date}.md`
- Updated avatar frontmatter: `status` flipped to `validated-vocabulary`, `validated-full`, or kept at `draft`
- `validation_date` updated on each avatar

**Downstream consumers:** `aud-review` reads ONLY `status: validated-vocabulary` or `validated-full` avatars. Draft avatars are unusable until passed through this skill.

## Pre-check (silent)

1. List `audience/avatars/` for files with `status: draft`.
2. For each draft avatar, check the matching held-out file exists at `audience/held-out/{segment-slug}.md`.
3. If no drafts → tell the creator: "No draft avatars to validate. Run `aud-avatar-build` first." Stop.
4. If a draft has no matching held-out file → tell the creator the segment is missing held-out quotes. Skip that avatar with a clear message.

## How the tests work (read-aloud version for the creator)

Before running, show this once:

> Three tests per avatar. Each is small, deterministic, and the avatar either passes or doesn't. The point is not to grade your data, it's to confirm the avatar can reliably represent its own segment instead of getting confused with other avatars or making up vocabulary.
>
> - Test 1: Can the avatar tell its own held-out quotes apart from another avatar's? (10 mixed quotes, needs 7 right.)
> - Test 2: When given a generic offer, does it surface objections that match its real held-out objections? (Top 3, needs 2 to substance-match.)
> - Test 3: When asked to describe its own top problem in 100 words, does it stay in its own vocabulary? (Needs to keep novel words under 15%.)
>
> Outcomes:
> - Passes test 1 AND test 3 → validated-vocabulary. Usable for vocabulary checks, objection surfacing, friction detection. Not trusted for behavioral predictions.
> - Passes all three → validated-full. Usable for any review type.
> - Anything less → stays draft. We rebuild or drop.

## For each draft avatar

Run the tests in order. Stop and skip remaining tests if a test result conclusively rules out the higher tier.

### Test 1: Quote attribution

**Setup:**
- Read this avatar's held-out file. Pick 5 random quotes from it.
- Pick another avatar's held-out file (any other validated or draft avatar with held-out quotes). Pick 5 random quotes from it.
- Shuffle the 10 quotes into a random order.

**Test (in an isolated subagent if possible, or in a focused prompt):**
- Load this avatar's profile only (Identity, Top Problems, Top Objections, Vocabulary Bank).
- Show the 10 quotes one at a time.
- Ask: "Would you say this? Yes or no."
- Score: own held-out quotes should get "yes". Other avatar's quotes should get "no".

**Pass threshold:** >= 7/10 correct (defined in `.claude/skills-wip/synthetic-audience-method.md`).

Save score to validation report.

### Test 2: Objection prediction

**Setup:**
- Construct a generic offer description in the avatar's niche. Not the creator's specific offer. Something like: "A 12-week online course teaching {niche topic} with weekly live calls and a community Slack."
- From the held-out file, pull the avatar's actual I-pushed-back quotes (the objections they raised in real life).

**Test:**
- Load this avatar's profile.
- Show the generic offer.
- Ask: "What are your top 3 objections to this offer? Reply with one sentence each."
- Compare the avatar's 3 predicted objections to the held-out actual objections.

**Pass threshold:** at least 2 of the avatar's 3 predictions substance-match held-out actuals. "Substance match" means the objection points at the same concern, not the same exact words. Example: held-out says "I already bought 4 courses, will this be different?" The avatar predicting "How is this different from other courses I've tried?" is a substance match. A prediction about pricing when the held-out is about differentiation is NOT a match.

This test is the most judgment-heavy. Err strict. If unsure, count as no match.

### Test 3: Vocabulary leak

**Setup:**
- From the avatar's source quotes (cited in the profile, NOT from held-out), build a vocabulary set: every word used in those quotes, lowercased, with stems collapsed (first 4 letters or root form).
- Load `references/common-english.txt` as the common-words allowlist.

**Test:**
- Load this avatar's profile.
- Ask: "Describe your top problem in your own words. 100 words."
- Take the response. Tokenize into individual words.
- For each word in the response: a word is **novel** if BOTH (a) it does NOT stem-match anything in the source vocabulary set AND (b) it does NOT appear in `common-english.txt`.
- Calculate: `novel_percent = (novel_words / total_words_in_response) * 100`

**Pass threshold:** novel_percent <= 15 (defined in `.claude/skills-wip/synthetic-audience-method.md`).

This catches avatars that invent vocabulary they have no source basis for.

### Compute outcome

Apply the tier rules:

- Tests 1 + 3 passed → `status: validated-vocabulary`
- All three passed → `status: validated-full`
- Anything less → `status: draft` (no change)

### Write the validation report

Save to `audience/avatars/{avatar-slug}-validation-{date}.md` using the avatar-validation schema. Body uses plain English. Banned: "test-retest reliability," "p-value," "confidence interval," "statistical significance," "Bayesian," "cosine similarity." Translate to actions.

**Validation report body template:**

```markdown
# Validation report: {avatar-slug}, {date}

## Outcome
{validated-full | validated-vocabulary | draft}

## What this means
{Plain-English sentence. Examples below.}

## Test results

### Test 1: Quote attribution
{Score}/10. {1-line note on which quotes confused the avatar, if any.}

### Test 2: Objection prediction
{Pass | Fail}. {1-line note on which predictions substance-matched, which missed.}

### Test 3: Vocabulary stayed in lane
{Novel percent}%. {1-line note. If failed, list 3-5 novel words that leaked.}

## How to use this avatar
{Plain English. See examples below.}
```

**Examples of plain-English "what this means" lines:**

- validated-full: "{Slug} can be used for any review type. Reviews of scripts, emails, titles, thumbnails, hooks, and CTAs. Trust the panel feedback."
- validated-vocabulary: "{Slug} can be used to check vocabulary fit and surface objections. Don't trust this avatar for tone or behavioral predictions. Useful but limited."
- draft (failed): "{Slug} confused its own quotes with another avatar's twice. We're not confident this avatar represents its segment cleanly. Either rebuild with more data or drop it."

### Update the avatar frontmatter

In `audience/avatars/{avatar-slug}.md`:
- `status: {new tier}`
- `validation_date: {today}`

Leave the rest of the avatar file alone.

## After all avatars are tested

Surface the summary:

```
Validation complete.

Validated-full ({N}):
- {slug-1}
- {slug-2}

Validated-vocabulary ({M}):
- {slug-3}

Draft / failed ({K}):
- {slug-4} (failed test 1: confused own quotes 4 times in 10)
- {slug-5} (failed test 3: 22% novel vocabulary)

Next:
- Validated-full and validated-vocabulary avatars are now usable by aud-review.
- Draft avatars need rebuild (more data via aud-intake) or drop.
```

If everything stayed draft, push back gently: "No avatars passed. This usually means the audience-data bank is too thin to support distinct segments. Add more calls via aud-intake before retrying."

Do NOT auto-invoke `aud-review`. The creator decides.

## Edge cases

**Only one draft avatar exists.** Test 1 needs another avatar's held-out for the mixed quote pool. Tell the creator: "Test 1 needs at least 2 avatars to compare. With only one avatar, we can only run tests 2 and 3. Best possible outcome is validated-vocabulary." Then run tests 2 and 3 only. If both pass, set status to `validated-vocabulary`.

**Held-out file has too few quotes (< 5).** Skip test 1 for that avatar (not enough quotes for the 5+5 split). Tell the creator. Best possible outcome becomes validated-vocabulary if tests 2 and 3 pass.

**Test 2 is ambiguous (creator judgment needed).** When in doubt, count as no match. Strict. The creator can manually override later by editing the validation report and avatar frontmatter.

**An avatar passes test 1 and 2 but fails test 3.** Stays draft. Test 3 catches invented vocabulary, which is the most dangerous failure mode for a copy review system. No exception.

**An avatar passes test 1 and 3 but not test 2.** Becomes validated-vocabulary. Still useful for the vocabulary use cases.

**A draft has no held-out file.** Skip. Tell the creator: "{slug} has no held-out quotes. Re-run aud-avatar-build for this segment to regenerate the held-out file."

**Banned vocabulary appears in Billy-facing output.** Strip and rewrite. Example: "Mike scored 8/10 with 95% confidence interval" becomes "Mike got 8 of 10 right."

## Anti-patterns

- Skipping the held-out separation. Test 1 requires the held-out file. No shortcuts.
- Using mean scores instead of pass/fail thresholds. Each test is binary.
- Counting near-misses in test 2 as substance matches. Err strict.
- Using statistics jargon in the report. Translate to actions.
- Auto-promoting failed avatars to validated. The status tier is strict.
- Auto-invoking `aud-review`. The creator decides.
- Running tests on the same avatar multiple times to game the result. One run per validation date. The creator can re-validate after rebuilding the avatar via `aud-avatar-build`.
