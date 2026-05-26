---
name: aud-intake
description: Ingest call transcripts and YouTube comments into the audience-data bank. Runs the contamination scan, extracts the 5 moment types from calls, batches comments as vocabulary samples. First skill in the synthetic-audience pipeline. Triggers on "ingest audience data", "process call transcripts", "load my YouTube comments", "build my audience bank", "aud-intake", or whenever the creator wants to feed raw audience material into the system for later avatar building.
---

# Audience Intake

Ingest raw audience material into `banks/audience-data/`. Two paths: calls (high-trust, full processing) and comments (low-trust, vocabulary samples only). Contamination scan runs on both.

This is the first skill in the `aud-*` pipeline. Without it, `aud-avatar-build` has nothing to read.

## Load at session start

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

1. `knowledge/synthetic-audience-method.md`. The contamination checklist, the 5 moment types, the validation thresholds, the banned vocabulary list. Non-negotiable.
2. `knowledge/vault-integration.md`. Frontmatter schemas for audience-data, vocabulary-sample, and the People stub rule.

## Contract

**Inputs (required):**
- Raw call transcripts in `inbox/audience/calls/` (`.txt`, `.md`, or `.vtt` files)
- AND/OR YouTube comment exports in `inbox/audience/comments/{video-slug}.csv`

**Inputs (optional):**
- Existing `banks/audience-data/` entries (this skill is incremental, not destructive)

**Outputs:**
- Per-call summary files in `banks/audience-data/calls/{call-slug}.md` (one per call, with extracted moment-type quote units)
- Vocabulary-sample files in `banks/audience-data/comments/{video-slug}/{id}.md` (one per kept comment)
- People stubs in `people/{Full Name}.md` for any prospect identified in a call
- A single batched contamination report shown at end of run

**Downstream consumers:** `aud-avatar-build` reads ONLY the summary files in `banks/audience-data/calls/` and the vocabulary samples. It never reads raw transcripts.

**Caps per run:** 5 calls max, 100 comments max. If more, queue the rest and tell the creator to invoke again.

## Before you start (literal text to show the creator on first run)

Show this if `inbox/audience/calls/` or `inbox/audience/comments/` is empty, OR if the creator pasted content into chat.

> Before we start: put your raw files in the inbox folder, not in chat.
>
> - Call transcripts go in `inbox/audience/calls/` (any filename, .txt or .md or .vtt)
> - YouTube comment exports go in `inbox/audience/comments/{video-slug}.csv` (one CSV per video, comment text in a column called `comment` or `text`)
>
> I will not read content pasted into chat for this skill. I process up to 5 calls and 100 comments per run. If you have more, I queue the rest and ask you to invoke me again.

If the inbox folders don't exist, create them and tell the creator they're ready.

## Pre-check (silent)

1. List `inbox/audience/calls/` and `inbox/audience/comments/`.
2. List `banks/audience-data/calls/` and `banks/audience-data/comments/` (so we don't re-process).
3. If both inboxes empty AND `banks/audience-data/` empty → show the Before-you-start block, then stop.
4. If inboxes have files but exceed caps → process the first 5 calls and first 100 comments, queue the rest with a clear message.
5. If inboxes empty but bank has entries → tell the creator the bank already has N entries and ask if they want to add more or run `aud-avatar-build` next.

## Path A: Process calls (one at a time)

For each call file in `inbox/audience/calls/` (up to 5 per run):

### Step 1: Speaker detection
Read the file. If speaker labels are generic (`Speaker 1`, `Speaker 2`, `00:01:23 -`), ask the creator ONCE per session:

> Your transcripts use generic speaker labels. Are you always the host? If yes, I'll treat Speaker 1 / the first named speaker as you across all calls in this run.

Save the answer to `audience/state.md` so we don't ask again. Default: first speaker is the host (creator).

### Step 2: Identify the prospect
Find the prospect's name in the transcript opening if present. If found:
- Create `people/{Full Name}.md` stub if it doesn't exist (per the People stub rule in `knowledge/vault-integration.md`)
- Use the name for the call-slug: `{first-name}-{date-or-topic}.md`

If no name in the transcript:
- Slug becomes `discovery-{date}.md` or similar
- No People wikilink in frontmatter (leave `person: ""`)

### Step 3: Extract the 5 moment types
Scan the prospect's lines ONLY (skip the host's lines, except where the host's question is needed to interpret the response). Extract quote-level units matching one of:

- **I-am moment** (how they describe themselves)
- **I-tried moment** (what they did before)
- **I-fear moment** (what they're avoiding)
- **I-want moment** (the outcome they describe)
- **I-pushed-back moment** (objections, hesitations)

Each extracted unit needs: verbatim quote (keep the prospect's exact words, no polishing), source line reference (line number or timestamp), moment type, one-word segment guess.

Skip everything else. Small talk, scheduling, host's leading questions are dropped.

**Cap on extracts per call:** ~15 quote units. If a call yields more, keep the strongest 15 (most specific, most emotional, most distinctive language). Quality over quantity.

### Step 4: Run contamination scan on the extracted units
For each extracted quote, apply the checklist in `knowledge/synthetic-audience-method.md` (em-dashes used as punctuation, LLM filler words, hedging phrases, suspiciously uniform sentence length, etc.). A quote needs 2+ tells to flag.

Calls are usually clean (spoken language is messy), so flagging is rare. If a "transcript" comes back perfectly polished and free of filler ("um", "like", "you know"), flag the whole call as `verified_human: needs_review`.

### Step 5: Write the per-call summary file
Save to `banks/audience-data/calls/{call-slug}.md` using the audience-data (call) schema from `knowledge/vault-integration.md`.

Body structure:

```markdown
# {Call slug, descriptive}

## Source
- File: `inbox/audience/calls/{original-filename}`
- Prospect: [[people/Full Name]] (if identified)
- Captured: {date}

## Extracted quote units

### I-am moments
> "verbatim quote 1" (line 47)
> "verbatim quote 2" (line 89)

### I-tried moments
> "verbatim quote 3" (line 112)

### I-fear moments
> "verbatim quote 4" (line 134)

### I-want moments
> "verbatim quote 5" (line 156)

### I-pushed-back moments
> "verbatim quote 6" (line 189)
> "verbatim quote 7" (line 201)

## Segment guesses
- {one-word segment label}: {1-line reasoning}
```

### Step 6: Move the raw file
After successful write, move the original transcript from `inbox/audience/calls/` to `raw/audience/calls/{call-slug}.txt` (create the folder if needed). This prevents reprocessing on the next run and preserves the raw for audit.

Do NOT delete. The raw stays as an audit trail.

### Step 7: Report and move on
Brief line back to the creator: `Processed {call-slug}. {N} quotes across {M} moment types.` Move to the next call. Do not stop for confirmation between calls.

## Path B: Process comments (batched)

For each CSV file in `inbox/audience/comments/` (combine to cap at 100 comments total per run):

### Step 1: Parse the CSV
Read each CSV. Expect a column named `comment`, `text`, `comment_text`, or `body`. If none match, ask the creator once which column holds the comment text. Save the answer to `audience/state.md`.

Other useful columns if present: `author`, `id`, `published_at`, `like_count`.

### Step 2: Drop bot-style noise
Filter out any comment that hits ALL of:
- Length < 5 words
- No problem language (no first-person verbs, no emotional charge, no question)

Also drop:
- Pure link spam (only a URL, or "check out my channel")
- Emoji-only (no words)
- Exact-duplicate comments (same text across multiple rows)

### Step 3: Run contamination scan
Apply the checklist in `knowledge/synthetic-audience-method.md`. Flag any comment with 2+ tells.

Comments are more often clean (short, casual, typo-prone). LLM-generated comments are typically too long, too balanced, and too polite for the platform. Flag those.

### Step 4: Score emotional valence (one-word label)
For each kept comment, pick ONE label:
- `frustration` (complaint, anger, exhaustion)
- `excitement` (positive surprise, enthusiasm)
- `contempt` (dismissive, hostile, troll-adjacent)
- `curious` (asking, exploring, open)
- `neutral` (factual, observational, no charge)

### Step 5: Extract surface objection if present
If the comment contains a "yeah but...", "but what about...", "doesn't this assume...", or similar pushback in 1 line, capture it as `surface_objection`. Otherwise leave empty.

### Step 6: Write the vocabulary-sample files
For each kept comment, write `banks/audience-data/comments/{video-slug}/{id}.md` using the vocabulary-sample schema.

Body structure (minimal, this is a low-trust entry):

```markdown
# Comment {id}

> {verbatim comment text}

- Source video: {video-slug}
- Author: {author or "anonymous"}
- Valence: {label}
- Objection: {1-line or "none"}
```

Cap on file count: 100 per run. If the CSV has more kept comments, take the 100 most language-rich (longest non-trivial entries, highest emotional charge) and tell the creator how many were queued.

### Step 7: Move processed CSVs
Move each processed CSV from `inbox/audience/comments/` to `raw/audience/comments/{video-slug}.csv`. Preserves audit trail.

## Final step: The batched contamination report

After all calls and comments are processed, surface flagged entries in a single table.

**Do NOT block on per-entry confirmation.** Default action: keep all flagged entries with `verified_human: needs_review` already set in their frontmatter.

Show the table to the creator:

```
Flagged entries (default: kept with needs_review flag)

| Type    | Slug                    | Tells matched              |
|---------|-------------------------|----------------------------|
| Comment | c-0042                  | em-dash, "navigating"      |
| Call    | discovery-2026-05-12    | uniform sentence length    |
| Comment | c-0178                  | parallel construction      |

These look possibly AI-generated. They are kept by default but marked for review. To strip any, edit the file and delete it from banks/audience-data/. To approve as human, change verified_human to true in the frontmatter. Either way, your call.
```

If zero entries were flagged, skip the table and just say: `No contamination flags. {N} calls and {M} comments ingested cleanly.`

## Closing the skill

Summarize the run:

```
Intake complete.
- Calls processed: {N} ({banks/audience-data/calls/})
- Comments kept: {M} ({banks/audience-data/comments/})
- Comments dropped as noise: {dropped}
- Flagged for review: {flagged}
- Raw files moved to: raw/audience/

Next: run aud-avatar-build to cluster these into segments and draft avatars.
```

If there's a queue (calls > 5 or kept comments > 100), name what's queued:

```
Queued for next run:
- {N more calls in inbox/audience/calls/}
- {M more comments in inbox/audience/comments/}

Invoke aud-intake again when you're ready.
```

Do NOT auto-invoke `aud-avatar-build`. The creator decides when to move on.

## Edge cases

**Inbox empty, bank non-empty.** Tell the creator the bank already has N call summaries and M vocabulary samples. Ask if they want to add more data (drop files in inbox), proceed to clustering (run `aud-avatar-build`), or stop.

**Pasted content in chat.** Show the Before-you-start block. Do not process pasted content. The skill is file-based for a reason: pasted content gets lost across sessions.

**CSV missing the expected column.** Ask the creator once which column has the comment text. Save the answer in `audience/state.md` so we don't ask again across files in the same run.

**Same prospect across multiple calls.** Create the People stub on first encounter. Subsequent calls add to the bank but link to the same People profile. Don't deduplicate the calls themselves. Each call is its own evidence.

**Transcript without timestamps or line numbers.** Use paragraph numbers or quote position as the source ref. The goal is "Billy could find this quote in the raw file" not formal citation.

**Very short call (< 10 minutes).** Process anyway. May yield only 3-5 quote units. That's fine.

**Very long call (> 90 minutes).** Process the prospect's lines only. If the file is too large to process in one read, summarize in chunks and combine. Cap extracted quotes at 15 regardless of call length.

## Anti-patterns

- Reading raw transcripts into avatar building. Avatar building reads summaries only.
- Per-entry confirmation prompts during contamination review. Batch it, default to keep, surface once at the end.
- Polishing the prospect's quotes. Verbatim, including filler and grammar quirks. The voice is the data.
- Extracting quotes from the host's lines. Only the prospect.
- Auto-invoking `aud-avatar-build`. The creator decides.
- Processing more than 5 calls or 100 comments per run. Cap it, queue the rest.
- Citing a comment for anything other than vocabulary. That's a downstream rule, but if you see it happening here flag it.
