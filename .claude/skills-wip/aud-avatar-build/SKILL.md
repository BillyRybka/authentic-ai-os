---
name: aud-avatar-build
description: Cluster audience-data into 4-6 segments and draft a synthetic avatar profile per segment. Bounded interview pattern, file-system-enforced held-out separation, 4-section avatar schema (Identity, Top Problems, Top Objections, Vocabulary Bank). Second skill in the synthetic-audience pipeline. Triggers on "build my avatars", "cluster my audience data", "draft my synthetic audience", "aud-avatar-build", or whenever the creator has audience-data in the bank and is ready to build the avatars that aud-review will run as a panel.
---

# Avatar Build

Cluster the audience-data bank into 4-6 segments. Set aside held-out quotes for validation. Draft one avatar per segment using the 4-section schema. Every claim cites 2+ source entries.

This runs after `aud-intake`. Without intake, this skill has nothing to read.

## Load at session start

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

1. `.claude/skills-wip/synthetic-audience-method.md`. Held-out protocol, the 5 moment types, banned vocabulary list. Non-negotiable.
2. `.claude/skills-wip/vault-integration-aud-schemas.md`. Frontmatter schemas for audience-segment, avatar, held-out.
3. `audience/state.md` if it exists. Resume-from-where-we-left-off state for bounded interviews.

## Contract

**Inputs (required):**
- `banks/audience-data/calls/{call-slug}.md` files with extracted moment-type quote units
- AND/OR `banks/audience-data/comments/{video-slug}/{id}.md` vocabulary samples

**Inputs (optional):**
- Existing `audience/segments/` and `audience/avatars/` for refresh runs

**Outputs:**
- `audience/segments/{segment-slug}.md` (one per cluster, named by the creator)
- `audience/held-out/{segment-slug}.md` (25-30% of each segment's strongest quotes, written BEFORE avatar drafts)
- `audience/avatars/{avatar-slug}.md` (one per segment, 4-section schema, `status: draft`)
- `audience/state.md` (resumable session state)

**Downstream consumers:** `aud-validate` reads avatars AND held-out files. `aud-review` reads only `status: validated-*` avatars.

**Target:** 4-6 avatars total. NOT 8-12. Fewer, deeper avatars beat more shallow ones at MVP scale.

**Hard caps per session (the bounded-interview rule):**
- Max 3 clustering questions asked of the creator per session
- Max 5 quotes shown per question
- Max 8 candidate clusters surfaced

If more input is needed, save state and tell the creator to resume tomorrow. Do NOT push through.

## Pre-check (silent)

1. List `banks/audience-data/calls/` and `banks/audience-data/comments/`.
2. List `audience/segments/`, `audience/avatars/`, `audience/held-out/`.
3. Read `audience/state.md` if it exists.

Decide what state we're in:

- **Bank empty** → tell the creator: "No audience data in the bank yet. Run `aud-intake` first." Stop.
- **Bank has < 3 calls** → warn the creator: "Only {N} calls in the bank. Avatars built on this little data will be thin. I can proceed if you want, or you can add more calls first." Wait for their call.
- **Bank populated, no segments yet** → fresh run. Start at Phase 1 (clustering).
- **Segments exist, no avatars yet** → resume at Phase 2 (avatar drafting).
- **Avatars exist** → ask refresh / keep / replace. Show the creator the existing avatars (slug + status) before they decide.
- **state.md says resume mid-interview** → pick up exactly where the last session stopped. Read the resume point from state.

## Phase 1: Clustering (bounded)

The goal is to find 4-6 natural segments in the audience-data, named by the creator, not by Claude.

### Step 1: Pre-cluster silently
Read every per-call summary file. Pull out the moment-type quotes. Group them by language similarity (shared problem framing, shared vocabulary, shared objection patterns). Cap at 8 candidate clusters even if the data wants more.

Demographics are a tiebreaker, not the grouping axis. People with the same pain pattern buy similarly even when they look different on paper.

### Step 2: Run the bounded interview
Present each cluster to the creator with this exact pattern. Stop after 3 clusters in one session if more would push past the cap.

> Cluster {N} of {total}: I'm seeing a pattern around {Claude's proposed theme}. Three representative quotes:
>
> 1. "{quote 1}" ({source slug})
> 2. "{quote 2}" ({source slug})
> 3. "{quote 3}" ({source slug})
>
> Does this feel like one type of person, or two?
>
> Two name candidates: {candidate 1} / {candidate 2}. Pick one, override, or split.

Accept: yes/no/split/pick one name/override with their own name.

**Do NOT show all the quotes in a cluster.** Max 3-5 representative quotes per question. If the creator wants to see more, they can open the segment file later.

**Do NOT ask the creator to invent the name from scratch.** Offer 2 candidates. They pick or override.

### Step 3: Save state if pausing
After 3 questions OR if the creator says "stop here", write `audience/state.md`:

```yaml
---
type: state
skill: aud-avatar-build
phase: clustering
clusters_confirmed: 3
clusters_pending: 2
session_date: YYYY-MM-DD
---
```

Then say: "Stopping for now. We've named {N} segments. {M} more to go. Run `aud-avatar-build` again tomorrow and we'll resume."

### Step 4: Write each confirmed segment file
For each segment the creator confirms (named, split or kept as one), write `audience/segments/{segment-slug}.md` using the audience-segment schema. Body lists which audience-data entries belong to this segment (wikilinks).

### Step 5: Decide segment count
Continue clustering across sessions until segments stabilize at 4-6. If the data wants fewer (3 or less), the creator's audience is more homogeneous than expected. That's fine. Note it and proceed with fewer avatars.

If clustering wants more (7-8), force-merge similar segments. Tell the creator: "Two of these are close. I'm merging {A} and {B} into {C}. We don't have enough data at MVP scale to keep them apart."

## Phase 2: Held-out segregation (file-system enforced)

This phase MUST run before Phase 3. Non-negotiable.

For each confirmed segment:

### Step 1: Identify the strongest 25-30% of quotes
"Strongest" means: most distinctive language, most specific to this segment, hardest to confuse with another segment's quotes. Prefer I-fear and I-pushed-back quotes for held-out (they're hardest to mimic).

### Step 2: Write the held-out file BEFORE any avatar drafting
Save to `audience/held-out/{segment-slug}.md` using the held-out schema. Body:

```markdown
# Held-out quotes: {segment slug}

These quotes are reserved for aud-validate. Do NOT read this file during avatar drafting.

## Quotes

> "verbatim quote 1" (source: [[call-slug]], line X)
> "verbatim quote 2" (source: [[call-slug]], line Y)
> ...
```

Update the parent segment file's frontmatter: `held_out_count: {count}`.

### Step 3: Verify the held-out is written before proceeding
Read `audience/held-out/{segment-slug}.md` back to confirm the write succeeded. If the file doesn't exist on disk, DO NOT proceed to avatar drafting. Retry the write. If retry fails, stop and report to the creator.

This file-system separation is the actual guardrail. Working memory can't be trusted across context window boundaries.

## Phase 3: Avatar drafting (one segment at a time)

For each segment with a held-out file already written:

### Hard rule (literal)
> Do not read from `audience/held-out/`. The held-out file is reserved for aud-validate. If you accidentally surface a held-out quote in an avatar, that avatar must be redrafted.

This is the most important instruction in the skill. Honor it.

### Step 1: Gather evidence (from NON-held-out quotes only)
Read the segment file. Read the audience-data entries it points to. Filter out any quote already in the segment's held-out list. The remaining quotes are the evidence pool.

### Step 2: Draft the 4-section avatar profile
Use ONLY the 4 sections. No others. Every claim needs 2+ citations from the evidence pool (or 0 in the Vocabulary Bank for word lists).

```markdown
# {Avatar slug, descriptive name like "Weekend Warrior Mike"}

## 1. Identity sketch
{2-3 sentences. Situation-led, NOT demographic-led. What are they doing in their life, what's the friction, why are they here.}

Cited evidence:
- [[call-slug-1]] line X: "quote"
- [[call-slug-2]] line Y: "quote"

## 2. Top problems in their vocabulary
{1-3 problems, verbatim quotes preserved. The creator's avatar uses THESE words when they vent.}

### Problem 1: {short label in their vocabulary}
> "verbatim quote" ([[call-slug-1]])
> "verbatim quote" ([[call-slug-2]])

### Problem 2: {short label}
> "verbatim quote" ([[call-slug-3]])
> "verbatim quote" ([[call-slug-4]])

## 3. Top objections
{1-3 objections, with verbatim quotes. The "yeah but..." patterns. CALLS ONLY for this section, not comments.}

### Objection 1: {1-line summary}
> "verbatim quote" ([[call-slug-1]])
> "verbatim quote" ([[call-slug-5]])

### Objection 2: {1-line summary}
> "verbatim quote" ([[call-slug-2]])
> "verbatim quote" ([[call-slug-3]])

## 4. Vocabulary bank
{Words they USE. Words they REJECT. Calls AND comments are both valid sources here.}

### Words they use
- "word/phrase" (frequent in [[call-slug-1]], [[c-0042]])
- "word/phrase" (across [[call-slug-2]], [[c-0078]])

### Words they reject or never use
{Inferable from contrast. If they say "I'm not a real player," they reject "player". If they say "I just want to noodle," they reject "performer".}

- "word/phrase" (they reject because: [[evidence]])
```

### Step 3: Citation enforcement
Before saving, verify:
- Identity sketch: 2+ citations from call entries only
- Each problem: 2+ citations from call entries only
- Each objection: 2+ citations from call entries only
- Vocabulary bank: calls AND comments both valid

If any section has < 2 citations, either find more evidence in the bank or DROP the claim. Single-citation claims leak in as stereotype. Strip them.

**Hard structural rule (per `.claude/skills-wip/synthetic-audience-method.md`):** comments may ONLY be cited in section 4 (Vocabulary Bank). Never in Identity, Problems, or Objections. Comments don't carry enough context for those claims.

If you find yourself wanting to cite a comment in section 1-3, the avatar is reaching. Strip the claim or find call evidence.

### Step 4: Write the avatar file
Save to `audience/avatars/{avatar-slug}.md` using the avatar schema. Set `status: draft`. Avatar is unusable until `aud-validate` flips it.

### Step 5: Show the avatar to the creator (briefly)
Don't dump the whole file in chat. Show:

```
Avatar drafted: {slug}

Identity: {1-line paraphrase}
Top problem: "{quote}"
Top objection: "{quote}"
Vocab: {3-5 example words from the bank}

Full file: audience/avatars/{slug}.md (status: draft)
```

Move on. Do not iterate on the avatar with the creator here. Validation is the next step.

## Phase 4: Wrap

Once all segments have avatars:

```
Avatars drafted: {N}
{slug-1} (draft)
{slug-2} (draft)
{slug-3} (draft)
{slug-4} (draft)

Held-out files written for each segment.

Next: run aud-validate to test each avatar against held-out quotes. Avatars stay in draft status until validation passes.
```

Do NOT auto-invoke `aud-validate`. The creator decides.

## State file schema

`audience/state.md` tracks bounded-interview resumption.

```yaml
---
type: state
skill: aud-avatar-build
project: authentic-ai-os
phase: clustering | held-out | drafting | done
clusters_confirmed: 0
clusters_pending: 0
avatars_drafted: 0
last_session_date: YYYY-MM-DD
resume_point: "name a thing the next session should read first"
---
```

When a fresh session loads, read this first. If the file exists and phase != done, resume at the documented point.

## Edge cases

**Creator wants > 6 avatars.** Push back once: "MVP scale supports 4-6 avatars well. More gets thin per avatar. Want to merge some, or proceed with more knowing each will be weaker?" Accept their call.

**Creator wants < 3 avatars.** Probably fine. Single-segment audiences exist. Note it: "Your data clustered into {N} natural segments. That's a homogeneous audience. We'll build {N} avatars."

**One cluster has only 2-3 quotes total.** Force-merge with the nearest cluster. Tell the creator. Single-cluster-of-three avatars are stereotypes waiting to happen.

**Creator names a segment after a real client.** Push back: "{Client Name} is a person, not a segment. Pick a descriptor that captures the type. {Client Name}'s quotes can still feed this segment." Offer 2 alternative names.

**Creator wants to refresh existing avatars.** Show them the current avatars. Ask: refresh which ones? Treat refresh as a fresh draft for those specific avatars only. Re-write the held-out file too (held-out should reflect the most current bank).

**Held-out file write fails.** Retry once. If still fails, stop and report. Do NOT proceed to avatar drafting without the held-out file on disk. This is the load-bearing guardrail.

**Avatar drafting accidentally surfaces a held-out quote.** Strip the quote from the avatar. Find a different citation from the non-held-out pool. If no alternative exists, drop the claim entirely.

**Banned vocabulary appears in Billy-facing output.** Per `.claude/skills-wip/synthetic-audience-method.md`, never use "test-retest reliability," "p-value," "confidence interval," "statistical significance," "Bayesian," "cosine similarity" in Billy-facing output. Translate to plain English.

## Anti-patterns

- Showing more than 5 quotes per clustering question. Bounded interview is the UX investment.
- Asking the creator to invent segment names from scratch. Offer 2 candidates.
- Building more than 6 avatars at MVP scale. Quality over quantity.
- Reading from `audience/held-out/` during avatar drafting. That folder is reserved for `aud-validate`.
- Single-citation claims. 2+ minimum or strip the claim.
- Comments cited in Identity, Problems, or Objections sections. Vocabulary Bank only.
- 5-section, 6-section, 8-section avatars. Stick to 4.
- Demographic-led identity sketches ("a 45-year-old male"). Situation-led only.
- Auto-invoking `aud-validate`. The creator decides.
- Pushing past the 3-question-per-session cap. Save state and tell them to resume tomorrow.
