---
type: reference
doc: vault-integration-aud-schemas
project: authentic-ai-os
status: parked
tags: [reference, vault-integration, audience, schemas]
---

# Vault Integration: Audience-Family Schemas (parked)

Parked out of `knowledge/vault-integration.md` on 2026-07-21 during the knowledge-layer cleanup (branch dag). These frontmatter schemas serve only the WIP aud-* pipeline (aud-intake, aud-avatar-build, aud-validate, aud-review). No shipped skill uses them. When the aud-* skills graduate, this becomes `knowledge/audience-contract.md`, a per-artifact contract alongside `piece-contract.md` and `bank-contract.md`, indexed from `knowledge/vault-integration.md`. It does not go back into vault-integration itself; that file is the shared core only.

### Audience-data entries (calls)

Location: `banks/audience-data/calls/{call-slug}.md`

Per-call summary written by `aud-intake`. Contains extracted quote units (the 5 moment types: I-am, I-tried, I-fear, I-want, I-pushed-back) with source line refs. This is the source of truth that `aud-avatar-build` reads. Raw transcripts are NOT read by avatar building.

```yaml
---
type: audience-data
source: call
project: authentic-ai-os
call_slug: discovery-call-2026-04-12
collected: YYYY-MM-DD
verified_human: true                  # true | false | needs_review
evidence_weight: high
contamination_flags: []               # list of flag tags if any
person: "[[people/Full Name]]"        # wikilink if prospect identified
segment_guesses: [returning-hobbyist] # one-word labels, refined by aud-avatar-build
quote_count: 12
tags: [audience-data, call, source-call]
---
```

### Audience-data entries (comment vocabulary samples)

Location: `banks/audience-data/comments/{video-slug}/{id}.md`

YouTube comment vocabulary samples written by `aud-intake`. Low-trust evidence. May ONLY be cited in an avatar's Vocabulary Bank section, never in Identity, Problems, or Objections.

```yaml
---
type: vocabulary-sample
source: comment
project: authentic-ai-os
video_slug: why-most-guitarists-quit
comment_id: c-0042                    # YouTube comment id or local sequence id
collected: YYYY-MM-DD
verified_human: true                  # true | false | needs_review
evidence_weight: low
contamination_flags: []
language_used: "verbatim comment text, single line"
emotional_valence: frustration        # frustration | excitement | contempt | curious | neutral
surface_objection: ""                 # 1-line objection if present, empty otherwise
person: ""                            # wikilink only if commenter is also a known caller
tags: [vocabulary-sample, comment, source-comment]
---
```

### Audience segments

Location: `audience/segments/{segment-slug}.md`

Rough cluster of related quote units, named by the creator during `aud-avatar-build` clustering interview. One segment becomes one avatar.

```yaml
---
type: audience-segment
project: authentic-ai-os
segment_slug: returning-hobbyist
captured: YYYY-MM-DD
quote_count: 18
held_out_count: 5                     # 25-30% of strongest quotes set aside for validation
source_calls: ["[[discovery-call-2026-04-12]]"]
source_comments: ["[[c-0042]]"]
status: clustered                     # clustered | avatar-drafted | retired
tags: [audience-segment]
---
```

### Synthetic avatars

Location: `audience/avatars/{avatar-slug}.md`

One avatar per segment. Four-section profile: Identity, Top Problems, Top Objections, Vocabulary Bank. Every claim cites 2+ source entries from `banks/audience-data/`. Comments may only be cited in the Vocabulary Bank section.

```yaml
---
type: avatar
project: authentic-ai-os
slug: weekend-warrior-mike
segment: "[[audience/segments/returning-hobbyist]]"
status: draft                         # draft | validated-vocabulary | validated-full | retired
evidence_count: 23                    # count of cited audience-data entries
held_out_path: "audience/held-out/returning-hobbyist.md"
validation_date: null                 # YYYY-MM-DD when last validated
last_calibrated: YYYY-MM-DD
tags: [avatar, segment-{slug}]
---
```

### Held-out quote sets

Location: `audience/held-out/{segment-slug}.md`

Reserved quotes per segment. Written by `aud-avatar-build` BEFORE avatar drafting. Read ONLY by `aud-validate`. The avatar drafting step explicitly does not read from this folder.

```yaml
---
type: held-out
project: authentic-ai-os
segment_slug: returning-hobbyist
written: YYYY-MM-DD
quote_count: 5
read_by: aud-validate                 # documents the only allowed consumer
tags: [held-out]
---
```

### Avatar validation reports

Location: `audience/avatars/{avatar-slug}-validation-{date}.md`

Result of the three-test validation gate. Outcome determines avatar `status` tier.

```yaml
---
type: avatar-validation
project: authentic-ai-os
avatar: "[[audience/avatars/weekend-warrior-mike]]"
run_date: YYYY-MM-DD
test_1_attribution: 8                 # 0-10, pass = >= 7
test_2_objection: pass                # pass | fail (>= 2/3 substance match)
test_3_vocabulary: 12                 # percent novel, pass = <= 15
outcome: validated-full               # validated-full | validated-vocabulary | draft
tags: [avatar-validation]
---
```

### Avatar reviews of a piece

Location: `content/pieces/{piece-slug}/reviews/{N}/{avatar-slug}.md`

One per avatar per review iteration. Written by `aud-review` via subagent invocation, isolated from other avatars' responses. Read in a second pass by the synthesis step.

```yaml
---
type: avatar-review
project: authentic-ai-os
piece: "[[content/pieces/why-most-guitarists-quit]]"
avatar: "[[audience/avatars/weekend-warrior-mike]]"
iteration: 1
content_type: script                  # script | email | title-thumb | hook | cta
run_date: YYYY-MM-DD
scores:
  clarity: 7
  resonance: 6
  believability: 5
  friction: 4
  cta_strength: null                  # null when not applicable
tags: [avatar-review, content-{type}]
---
```

### Panel synthesis for a piece

Location: `content/pieces/{piece-slug}/reviews/{N}/synthesis.md`

The Billy-facing output of one review iteration. Verdict, top 3 fixes, median scores, dissent block, links to per-avatar reviews, disclaimer. Read-on-the-first-screen design.

```yaml
---
type: panel-synthesis
project: authentic-ai-os
piece: "[[content/pieces/why-most-guitarists-quit]]"
iteration: 1
content_type: script
run_date: YYYY-MM-DD
verdict: fix-then-ship                # ship | fix-then-ship | rewrite
median_scores:
  clarity: 7
  resonance: 6
  believability: 6
  friction: 5
  cta_strength: 6
dissent_count: 1                      # avatars scoring 3+ below median on any dimension
avatars_used: ["[[audience/avatars/weekend-warrior-mike]]"]
tags: [panel-synthesis]
---
```
