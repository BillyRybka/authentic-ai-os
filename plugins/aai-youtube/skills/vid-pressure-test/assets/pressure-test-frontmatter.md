---
type: asset
skill: vid-pressure-test
phase: 6
tags: [piece-md-schema, frontmatter]
---

# piece.md Frontmatter Block: Pressure Test Audit

Phase 6 appends this YAML block to piece.md frontmatter. Append, do not overwrite other fields. Other skills (vid-framing, vid-intro, vid-segment, vid-ending) own their own fields per the piece.md schema matrix.

## The block

```yaml
pressure_test_audit:
  ran_at: 2026-05-14
  mode: multi-agent
  hard_issues_caught: 3
  hard_issues_resolved: 3
  soft_issues: 2
  verdict: ready-to-film
  read_aloud_passed: true
  claims_to_source_before_filming: []
  soft_issues_list:
    - reviewer: voice-authenticity
      location: Segment 3 line 4
      quote: "You might want to consider this approach."
      diagnosis: "Hedge stack; accepted by creator as deliberate softness."
    - reviewer: ai-slop
      location: Segment 5 close
      quote: "Stronger, faster, more durable."
      diagnosis: "Three-item-list rhythm; creator kept for emphasis."
pressure_test_status: passed
pressure_tested_at: 2026-05-14
status: filming-ready
last_updated: 2026-05-14
```

## Field definitions

### `pressure_test_audit`

**`ran_at`** (date, YYYY-MM-DD)
The date the audit ran. Updates on every fresh run.

**`mode`** (string, always `multi-agent` in v1)
Reserved for future single-agent mode if added.

**`hard_issues_caught`** (integer)
Total hard issues surfaced by all 4 reviewers after dedup. Max 12 before consolidation; usually 6-9 after dedup.

**`hard_issues_resolved`** (integer)
Hard issues the creator handled (approve / deny+rewrite / mark-as-gap). If `hard_issues_resolved < hard_issues_caught`, some were left open mid-session.

**`soft_issues`** (integer)
Count of soft issues logged (not walked interactively).

**`verdict`** (enum)
- `ready-to-film`: all hard issues resolved AND read-aloud passed AND no open `claims_to_source_before_filming`
- `needs-revision`: at least one hard issue left as mark-as-gap OR read-aloud surfaced a rework
- `read-aloud-pending`: hard issues resolved but creator wants to think on read-aloud overnight

**`read_aloud_passed`** (bool)
True only if creator read aloud and reported no rewording needed. False if read-aloud surfaced edits OR was deferred.

**`claims_to_source_before_filming`** (array of strings, default `[]`)
Each entry is one line: `"{location}: {quote excerpt}: {why it needs sourcing}"`. Verdict cannot be `ready-to-film` while this array is non-empty.

**`soft_issues_list`** (array of objects)
Each object has `reviewer`, `location`, `quote`, `diagnosis`. Used by future re-audit mode to surface previously-deferred soft issues. Capped at the actual soft issue count (no padding).

### Top-level fields

**`pressure_test_status`** (enum, skill-namespaced audit result, NOT the piece lifecycle)
Records this audit's outcome for quick cross-skill reads: `passed` (verdict ready-to-film), `issues-flagged` (needs-revision), `resolved` (creator manually re-ran and closed gaps). It is deliberately prefixed so it never reads as a competing lifecycle status. The piece lifecycle is solely `status`; the orchestrator routes on `status: filming-ready`, never on this field. This field carries the finer detail `status` cannot: a piece can sit at `status: drafting` with `pressure_test_status: issues-flagged` (audited, found problems, not yet resolved).

**`pressure_tested_at`** (date)
Same as `ran_at`. Top-level for easy querying via Dataview or cross-skill reads.

**`status`** (enum, the piece lifecycle field)
Set to `filming-ready` ONLY when the verdict is `ready-to-film`. For `needs-revision` or `read-aloud-pending`, leave the existing `status: drafting`. This is the field vid-pipeline reads to know the piece is done. It is the one lifecycle field; there is no `piece_status`.

**`last_updated`** (date)
Bumped to today on every pressure-test run, per the vault-wide date rule.

## Append protocol

1. Read piece.md
2. Parse existing frontmatter
3. Add or update ONLY these fields:
   - `pressure_test_audit` (full block)
   - `pressure_test_status`
   - `pressure_tested_at`
   - `status` (set to `filming-ready` ONLY when verdict is ready-to-film)
   - `last_updated` (today)
4. Preserve every other field exactly as-is (do not touch `frame`, `core_payoff`, `format`, `goal`, `segment_purposes`, `segments_completed`, etc.)
5. Write piece.md back

## Re-audit overwrites previous block

When pressure-test re-runs on a piece, the `pressure_test_audit` block is fully replaced with the fresh run's data. Previous run's data is gone (the script changes are the historical record; the audit block reflects the current state).

If a creator wants to preserve audit history across runs, they can manually copy the block to a `pressure_test_audit_history` array before re-running. Not built-in to v1.

## Worked example (full piece.md frontmatter after pressure-test)

```yaml
---
type: content-piece
slug: why-i-quit-posting-daily
status: filming-ready
created: 2026-05-10
last_updated: 2026-05-14
published: null

# Written by vid-framing
frame: "Daily posting destroyed my quality and tanked retention"
core_payoff: "A schedule that doubles quality without losing growth"
format: short-process
voice_context: youtube-script
goal: views
outlier_anchor: "..."
anchor_confidence: high

# Written by vid-title
title: "Why I Quit Posting Daily And Grew 10x"

# Written by vid-thumbnail
thumbnail_text: ["STOP HIRING"]
thumbnail_shape: [imperative]

# Written by vid-structure (advanced status to drafting)
segment_purposes:
  - "The breaking point (when daily posting started costing me)"
  - "..."
segments_completed:
  - "The breaking point (when daily posting started costing me)"
  - "..."
tension_plan:
  central_question: "..."
  title_promise_segment: 4

# Written by vid-intro
intro_locked: true

# Written by vid-segment (per segment)
stories_used:
  - "[[banks/story-bank/breaking-point]]"
proofs_used: []
metaphors_used: []
testimonials_used: []
frameworks_used: []

# Written by vid-ending
ending_locked: true
next_video: "[[the-twice-weekly-system]]"

# Written by vid-pressure-test (this block; advanced status to filming-ready)
pressure_test_audit:
  ran_at: 2026-05-14
  mode: multi-agent
  hard_issues_caught: 4
  hard_issues_resolved: 4
  soft_issues: 3
  verdict: ready-to-film
  read_aloud_passed: true
  claims_to_source_before_filming: []
  soft_issues_list:
    - reviewer: voice-authenticity
      location: Segment 3 line 4
      quote: "You might want to consider this approach."
      diagnosis: "Hedge accepted as deliberate softness."
    - reviewer: ai-slop
      location: Intro line 8
      quote: "..."
      diagnosis: "..."
    - reviewer: retention-logic
      location: Segment 4 to 5 handoff
      quote: "..."
      diagnosis: "Cold handoff; creator chose to keep the breath."
pressure_test_status: passed
pressure_tested_at: 2026-05-14
---
```

## Anti-pattern

Do NOT write the pressure-test audit results to a separate `pressure-test.md` file. The script.md IS the deliverable. piece.md's frontmatter IS the receipt. Creating a third file just to log what happened reads as ceremony and the creator never opens it.

## Chat summary at end (paired with frontmatter write)

After writing the frontmatter, surface a clean chat summary:

```
Pressure test complete.

Hard issues: 4 caught, 4 resolved.
Soft issues: 3 logged in piece.md (non-blocking).
Read-aloud: passed.

Verdict: Script ready to film.
```

The chat summary IS the visible receipt for the creator. The frontmatter block is the structured data for cross-skill consumption.
