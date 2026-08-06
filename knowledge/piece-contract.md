---
type: reference
doc: piece-contract
project: authentic-ai-os
status: active
tags: [reference, piece, schema, contract]
---

# piece.md contract

The per-piece identity ledger at `content/pieces/{slug}/piece.md`. Every locked decision for one video, in one file, so any skill can read true state without re-deriving it.

Load this if you write to `piece.md` or route on it. Shared vault rules (folder map, wikilink form, tags, naming) are in [[vault-integration]].

## Full schema

```yaml
---
type: content-piece
project: authentic-ai-os
slug: video-slug
pillar: {pillar-slug}           # creator's content pillar
frame: "..."                    # the chosen video described in third person, in the grammar of its want ("A video that shows {who} how to {the change}" is one shape, not the shape). Never a spoken line, never a headline, never a description of the contents. Set by vid-framing.
core_payoff: "..."              # the reason the viewer stays to the end, almost always the answer to a question already in their head. Second person, one thing, 1-2 sentences. Locked with the frame. Set by vid-framing. vid-structure orders the points so this lands late.
format: short-process           # from the 7 formats: short-process | case-study | roast | deep-dive | interview | news | listicle. Set by vid-framing.
voice_context: youtube-script   # delivery medium for voice: youtube-script (default) | tutorial | shorts | newsletter | linkedin | twitter | instagram | podcast | casual | talk. Orthogonal to format. Set by vid-framing (videos) or post-write (posts). Drives which foundation/reference-pieces/{voice_context}.md a writing skill loads.
goal: sales                     # sales | emails | views (ONE only). Set by vid-framing.
status: ideating                # ideating | drafting | filming-ready | filmed | editing | published. The one lifecycle field. See "Lifecycle" below.
created: YYYY-MM-DD             # stamped once by vid-intake at piece creation, never changed
last_updated: YYYY-MM-DD        # bumped to today by EVERY skill that writes this file
published: null                 # YYYY-MM-DD when published
segment_purposes: []            # set by vid-structure: the planned body segments
segments_completed: []          # appended by vid-segment, one label per locked body segment. The pipeline compares its length to segment_purposes to know when the body is done.
stories_used: []                # [[story-bank/slug]] wikilinks added when writing skills use them
metaphors_used: []
proofs_used: []
testimonials_used: []           # added when a writing skill weaves a testimonial
frameworks_used: []             # added when a segment teaches a creator framework
tags: [piece, format-{slug}, pillar-{slug}, {other-tags}]
---
```

## Creation subset (vid-intake)

`vid-intake` creates the file the moment the topic is known, with only what is true that early. It writes exactly these fields and no others:

```yaml
---
type: content-piece
project: authentic-ai-os
slug: {kebab-case-slug}
pillar: {pillar-slug or null}
status: ideating
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
anchor: "{Only when vid-ideas handed a picked seed: the full outlier receipt, source title + @channel + views + xMed. Omit otherwise.}"
tags: [piece, pillar-{slug}]
---
```

`format-{slug}` joins `tags` when `vid-framing` sets `format`. Everything else in the full schema is absent until its owning skill writes it. Absent is the correct state; do not pre-stub fields with empty values that no skill has decided yet.

## Field ownership

Skills append their own fields and never overwrite another skill's.

| Skill | Writes |
|---|---|
| vid-intake | `type`, `project`, `slug`, `pillar`, `status: ideating`, `created`, `last_updated`, `anchor`, `tags` |
| vid-framing | `frame`, `core_payoff`, `format`, `voice_context`, `goal`, plus the `## The Read` body section |
| vid-title | `title` |
| vid-thumbnail | `thumbnail_text`, `thumbnail_shape` |
| vid-structure | `segment_purposes`, `tension_plan`, `status: drafting` |
| vid-intro | `intro_locked`, plus bank-use arrays it pulled into |
| vid-segment | `segments_completed`, plus bank-use arrays it pulled into |
| vid-ending | `ending_locked`, `next_video`, plus bank-use arrays it pulled into |
| vid-pressure-test | the `pressure_test_audit` block, `claims_to_source_before_filming`, `soft_issues_list`, `status: filming-ready` |

The bank-use arrays (`stories_used`, `metaphors_used`, `proofs_used`, `testimonials_used`, `frameworks_used`) are shared: any writing skill that pulls a bank entry appends to the matching array. Append, never replace. The reciprocal write on the bank side is in [[bank-contract]].

Every skill that writes this file bumps `last_updated` to today. `created` never changes.

## Body sections

piece.md carries body sections as well as frontmatter, and they are contracted here for the same reason the fields are: `## The Read` silently changed shape twice because nothing outside the owning skill specified it.

| Section | Owner | Shape | Re-run behavior |
|---|---|---|---|
| `## The Read` | vid-framing | Three fields in this order, third person, all pointed at the locked frame: **Target** (who this is for and the situation, as one causal chain ending on a cost), **Transformation** (they stop doing X and do Y instead, plus what that gets them), **Stakes** (each consequence causing the next, the misattribution named near the end, landing back where Target started) | Replaced on a re-frame. It describes the current frame, not a history. |

`core_payoff` is frontmatter only. It is locked with the frame, before the read exists, so there is no second copy in the body to drift against.

Readers are soft: a piece written before a section existed must not block a downstream skill. vid-title presses on the Stakes, vid-intro mines them for hooks, and vid-structure builds toward the Transformation. All three degrade to their prior behavior when the section is absent.

Changing the shape of a contracted section means updating this table, the owning skill, and every reader named above in the same pass.

## What does not go in piece.md

Decisions a later skill or the pipeline reads, not a diary of how each skill worked. No process-journal fields (hook type, credibility form, title lane, transition pattern, cta shape, and the like): those had no reader. A journal field returns only when a real consumer exists (for example a future vid-measurement correlating hook type against retention), added then with that reader on the other end.

## Lifecycle

`status` is the single lifecycle field. The pipeline advances it at three points:

- `ideating` set by vid-intake on creation
- `drafting` set by vid-structure once the outline locks (writing has begun)
- `filming-ready` set by vid-pressure-test when the script passes

`filmed | editing | published` are set manually after production. There is no second status field. The old `piece_status` written by early vid-framing / vid-structure drafts is retired: the orchestrator never reads it.

## How the pipeline routes

`vid-pipeline` decides the next writing step by reading which artifact already exists, not by a micro-status: `frame` present? `title` present? thumbnail picks present? `segments_completed` length vs `segment_purposes` length? `ending_locked` present? `status` at `filming-ready`?

Each skill therefore writes its own distinguishing field in BOTH standalone and pipeline (sub-skill) mode, so the orchestrator can always read true state from the file.

## Failure cases

- **piece.md does not exist** when a downstream skill expects it: create it from the creation subset above and proceed. Do not invent decisions the earlier skills never made.
- **A field you need is absent**: that means its owning skill has not run. Route to that skill, or ask the creator. Never fill in another skill's field to unblock yourself.
- **`foundation/iceberg.md` or `foundation/avatar.md` missing**: hard stop. Tell the creator to run `/foundation` first.
