---
name: aud-review
description: Run a panel of validated synthetic avatars against a script, email, title+thumbnail, hook, or CTA. Subagent-isolated avatar responses, median-plus-dissent synthesis, verdict-first output. Final skill in the synthetic-audience pipeline. Triggers on "review my script", "test my email with avatars", "run the panel", "review my hook", "review my title and thumbnail", "review my CTA", "aud-review", or whenever the creator has a piece they want pre-publish feedback on from the synthetic audience.
---

# Avatar Review

Run validated avatars against a piece of content. Each avatar reviews in isolation. Median scores with verbatim dissent. Synthesis built so the creator reads the first screen and acts.

This is the final skill in the `aud-*` pipeline. It only uses avatars whose `status` is `validated-vocabulary` or `validated-full`.

## Load at session start

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

1. `knowledge/synthetic-audience-method.md`. Scoring dimensions, trigger rules, rotating disclaimers, banned vocabulary, calibration check trigger. Non-negotiable.
2. `knowledge/vault-integration.md`. Avatar-review and panel-synthesis frontmatter schemas.

## Contract

**Inputs (required):**
- A piece of content. The creator can supply it as:
  - A wikilink to a piece in `Content/pieces/{slug}/` (preferred)
  - A wikilink to a specific file inside a piece (e.g., `[[Content/pieces/x/email-draft.md]]`)
  - A file path
- The content type (script | email | title-thumb | hook | cta). If not stated, infer from the file name or ask once.

**Validated avatars in `audience/avatars/` with status `validated-vocabulary` or `validated-full`.** If none exist, stop and route the creator to `aud-validate`.

**Outputs:**
- Per-avatar review files at `Content/pieces/{piece-slug}/reviews/{N}/{avatar-slug}.md`
- Panel synthesis at `Content/pieces/{piece-slug}/reviews/{N}/synthesis.md`
- Updated panel-synthesis frontmatter (verdict, median scores)

Where `{N}` is the next available iteration number (1, 2, 3...). Re-running on the same piece creates a new iteration folder, never overwrites.

## Pre-check (silent)

1. Resolve the piece. If ambiguous, ask once. Don't proceed with guesses.
2. List `audience/avatars/` filtered to `status: validated-vocabulary` OR `validated-full`.
3. List existing review iterations for this piece. Compute next `{N}`.
4. Check the last-modified date on the most recent file in `banks/audience-data/calls/` (or comments/). If > 60 days ago, set a flag to surface the calibration check in the synthesis output regardless of iteration count.

If zero validated avatars exist → tell the creator: "No validated avatars yet. Run `aud-validate` first." Stop.

If only validated-vocabulary avatars exist AND the content type is one where behavioral prediction matters (e.g., CTA): proceed with what's available, but flag in the synthesis: "Only vocabulary-validated avatars used. CTA strength scores are directional only."

## Filter avatars by content type

Not every avatar reviews every content type. Quick rules:

- **Script**: all validated avatars
- **Email**: all validated avatars
- **Title + thumbnail**: all validated avatars (treat as a paired artifact, NEVER review separately)
- **Hook**: all validated avatars
- **CTA**: validated-full only. Vocabulary-only avatars cannot reliably predict action intent.

If the filter leaves fewer than 2 avatars usable for this content type, warn the creator: "Only {N} avatar(s) qualify for this content type. Panel won't have meaningful dissent. Proceed?" Wait for go.

## Phase 1: Run avatars in isolated subagent calls

For each qualifying avatar, in RANDOMIZED order:

### Step 1: Build the subagent prompt
Each subagent gets ONLY:
- The avatar profile (full file from `audience/avatars/{slug}.md`)
- The piece content (full file or files)
- The content-type-specific review questions (see Phase 1.5 below)
- The scoring instructions (5 dimensions, 0-10 each)

The subagent does NOT see:
- Other avatars' profiles
- Other avatars' responses
- The panel synthesis instructions
- Any prior iteration's reviews

### Step 2: Invoke the subagent
Use the Agent tool (or whatever subagent mechanism is available). The prompt template:

> You are {avatar-slug}, a synthetic representation of a real audience segment. Your full profile is below. Read it before answering.
>
> {full avatar profile}
>
> You have been asked to review a piece of {content type} content. You have not seen any other reviewer's response. You will answer as this person, in their vocabulary and with their objections.
>
> The content:
>
> {full piece content}
>
> Answer the questions below. Use this person's language, NOT polished prose. Score the 5 dimensions at the end. Reply in this exact markdown format:
>
> {content-type-specific question block, see Phase 1.5}
>
> ## Scores (0-10)
> - Clarity: {score} - {1-line reason}
> - Resonance: {score} - {1-line reason}
> - Believability: {score} - {1-line reason}
> - Friction: {score} - {1-line reason. Lower is better. 10 = no friction, 0 = bailed immediately.}
> - CTA strength: {score or N/A} - {1-line reason}

### Step 3: Write the subagent response to disk
Save to `Content/pieces/{piece-slug}/reviews/{N}/{avatar-slug}.md` using the avatar-review schema. Frontmatter populated, body is the subagent response.

CRITICAL: write this file BEFORE invoking the next subagent. The parent context will need to read these files back in Phase 2. Working memory is not the source of truth.

### Step 4: Move to next avatar
Do not summarize, do not cross-reference. Move on. Continue in randomized order until all qualifying avatars have run.

## Phase 1.5: Per-content-type question sets

Each subagent invocation injects ONE of these question blocks based on `content_type`.

### Script

```markdown
## Reactions

### At 0:15 (~first 60 words)
Are you still here? Why or why not?

### At 1:00 (~first 250 words)
What do you think this is about? What did you not believe?

### At 3:00 (~first 700 words)
Did you tune out? Where? What pulled you back, if anything?

## Friction points
List the exact moments you wanted to leave. Quote the line that made you bounce.

## Belief breakdowns
List any claim that lost you. Quote it. Say why.

## Number one remaining question
What would you still want answered after watching?
```

### Email

```markdown
## Subject line
Would you open this? Yes or no. What did the subject line tell you?

## After paragraph 1
Still reading? Why or why not?

## The ask
What is this email asking you to do? In your own words.

## Action intent
Would you do it? Yes / no / maybe. Why?

## Friction points
List the lines that made you want to delete. Quote them.

## Number one remaining question
What's missing that would change your mind?
```

### Title + thumbnail

```markdown
## Click intent
1-10. Would you click? Why?

## What you expect the video to be about
In one sentence.

## What would disappoint you
If you clicked and the video did NOT deliver this, what would that be?

## Trust signal
Does anything in the title or thumbnail make you trust the creator less? Quote it.
```

### Hook

```markdown
## At 0:05
Stay or leave? Why?

## At 0:15
Stay or leave? Why?

## At 0:30
Stay or leave? Why?

## The promise
What did the creator promise you'd get from this video? In your own words.

## Believability
Do you believe they can deliver on that promise? Why or why not?
```

### CTA

```markdown
## What is being asked
In your own words.

## Perceived cost
What does this cost you? Time, money, risk, identity. List everything.

## Perceived value
What do you get? In your own words.

## Action intent
Would you do it? Yes / no / maybe. Why?

## What stops you
What's the single biggest thing keeping you from acting right now?
```

## Phase 2: Synthesis (read avatar files from disk)

After ALL subagents have written their files:

### Step 1: Read each avatar-review file
Iterate through `Content/pieces/{piece-slug}/reviews/{N}/*.md` (excluding `synthesis.md`). For each:
- Extract the 5 scores
- Extract any 1-line reasons for outlier scores

### Step 2: Compute median per dimension
Median, not mean. A single skeptic should not get averaged out.

For each dimension (clarity, resonance, believability, friction, CTA strength): sort the per-avatar scores, take the middle value (or average of two middles if even count).

### Step 3: Identify dissent
For each dimension:
- For each avatar's score on that dimension
- If `(median - score) >= 3` → flag as dissent

For each dissent flag, read the avatar's reason for that dimension verbatim from the avatar-review file. The dissent quote in the synthesis MUST come from the file on disk, not from working memory.

### Step 4: Compute verdict
Per `knowledge/synthetic-audience-method.md`:
- Median < 7 on any dimension → REWRITE
- Any avatar's min on any dimension < 4 → REWRITE
- Median >= 7 across all + no min < 4 → SHIP
- Anything between → FIX-THEN-SHIP

CTA strength is skipped from the verdict computation if the piece doesn't have a CTA (e.g., a hook in isolation).

### Step 5: Build the top 3 fixes
Read all avatar-review files. Pull out:
- Friction points (most-quoted moments)
- Vocabulary swaps (words avatars rejected, words they would have used)
- Missing objection handlers (questions avatars said remained)

Rank by frequency (mentioned by 2+ avatars beats mentioned by 1) and severity (verdict-changing matters more than nice-to-have). Pick the top 3.

Each fix must be actionable in 60 seconds. Examples of good fixes:
- "Replace 'mastery' with 'getting unstuck' (used 5 times in script, 4 avatars flagged it as expert-framed)"
- "Cut paragraph 3 of email. 3 of 4 avatars said they bailed there."
- "Add a 1-sentence answer to 'how is this different from other courses' before the CTA. 4 of 5 avatars listed this as remaining question."

Bad fixes (do NOT write):
- "Make it better"
- "Improve the hook"
- "Rewrite the script with more clarity"

### Step 6: Pick the disclaimer variant
Pick ONE of the three variants from `knowledge/synthetic-audience-method.md` randomly per run. If this run hits the every-10th-run trigger OR the 60-day-stale-data flag was set in pre-check, append the calibration check at the bottom regardless.

### Step 7: Write `synthesis.md`
Top-to-bottom, designed for first-screen reading.

```markdown
---
{panel-synthesis frontmatter}
---

# Panel synthesis: {piece-slug}, iteration {N}, {date}

## Verdict: {SHIP | FIX-THEN-SHIP | REWRITE}

## Top 3 fixes

1. {actionable fix}
2. {actionable fix}
3. {actionable fix}

## Median scores

| Dimension | Median | Range |
|---|---|---|
| Clarity | {n} | {min}-{max} |
| Resonance | {n} | {min}-{max} |
| Believability | {n} | {min}-{max} |
| Friction | {n} | {min}-{max} |
| CTA strength | {n or N/A} | {min}-{max} |

## Dissent

{For each dimension with dissent: quote the avatar's verbatim reason.}

### {dimension}: {avatar-slug} scored {n}, median was {m}
> {verbatim quote from the avatar-review file}

{If no dissent across all dimensions:}
> No dissent. All avatars within 2 points of median on every dimension. Either the piece is genuinely tight or the panel is in agreement (which sometimes means the panel is missing a viewpoint).

## Per-avatar full reviews

- [[{avatar-slug-1}]]
- [[{avatar-slug-2}]]
- ...

## {Disclaimer variant chosen for this run}

{If calibration check is triggered:}

> When did you last add real call transcripts to `inbox/audience/calls/`? If it has been more than 60 days, these avatars are drifting from your real audience. Run `aud-intake` before you trust this review.
```

## Phase 3: Show the creator

Brief surface in chat. Do NOT dump the whole synthesis. The synthesis file is the deliverable.

```
Panel review complete: iteration {N}.

Verdict: {SHIP | FIX-THEN-SHIP | REWRITE}

Top 3 fixes:
1. {one-line}
2. {one-line}
3. {one-line}

Median scores: clarity {n}, resonance {n}, believability {n}, friction {n}, CTA {n or N/A}.

Full synthesis: Content/pieces/{piece-slug}/reviews/{N}/synthesis.md
Per-avatar reviews: same folder, one file per avatar.
```

Do NOT auto-trigger a rewrite. The creator decides what to do.

## Edge cases

**Piece not found at the supplied path.** Stop. Ask the creator for the correct path. Don't guess.

**Content type not stated and unclear from the file.** Ask once: "Is this a script, email, title+thumbnail, hook, or CTA?" Save the answer to the file's frontmatter if it's a piece-level file, otherwise just use it for this run.

**Only one validated avatar.** Run anyway. Tell the creator: "One avatar review. No dissent possible. This is a single perspective, not a panel." Verdict logic still applies but is much weaker.

**Title and thumbnail supplied separately.** Stop. Tell the creator: "Title and thumbnail must be reviewed as a pair. They're a single click-decision artifact." Wait for both.

**The piece is empty or trivial (< 30 words for a script, < 50 words for an email, etc.).** Tell the creator the piece is too thin to review. Don't run the panel.

**Subagent invocation isn't available in this environment.** Fall back to sequential focused prompts: for each avatar, build a focused prompt that loads only the avatar profile and the piece, run it, write the response file, then proceed to the next avatar. Tell the creator: "Subagent isolation not available in this environment. Running sequential focused prompts instead. Cross-avatar contamination is minimized but not eliminated."

**A subagent's response is missing scores or malformed.** Re-run that avatar once. If still malformed, skip that avatar and note in the synthesis: "Avatar {slug} failed to return a parseable response. Excluded from this iteration." Continue with the rest.

**The piece has been reviewed before (iteration N exists).** Create iteration N+1. Never overwrite. The history of iterations is a feature.

**The creator wants to re-run on the same iteration.** Push back: "Iteration {N} already has a synthesis. Running again creates iteration {N+1}. That's the audit trail. Proceed?"

**Banned vocabulary appears in synthesis output.** Strip. Per `knowledge/synthetic-audience-method.md`, never use "test-retest reliability," "p-value," "confidence interval," "statistical significance," "Bayesian," or "cosine similarity" in synthesis output.

## Anti-patterns

- Cross-referencing avatars in their subagent prompts ("the other reviewers thought..."). Each avatar runs blind.
- Computing dissent from working memory instead of from the avatar-review files on disk. The "verbatim" quote must be from the file.
- Mean instead of median. Outliers carry information. Don't average them away.
- "Make it better" as a fix. Every fix must be actionable in 60 seconds.
- Showing the whole synthesis in chat. The file is the deliverable. Surface the first screen.
- Auto-triggering a rewrite skill. The creator decides what to do with the verdict.
- Skipping the calibration check on stale data. If data is > 60 days old, the check appears regardless of iteration count.
- Reviewing title and thumbnail separately. Always paired.
- Running CTA review on vocabulary-only avatars. CTA needs validated-full. Filter strictly.
- Treating the verdict as a prediction. It's a panel reading, not a prophecy.
