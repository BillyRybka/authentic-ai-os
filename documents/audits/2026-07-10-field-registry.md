# Field registry, 2026-07-10

Map 3 of the Phase 1 sweep. Every frontmatter field: producer, consumers that ACT on it, verdict candidate. Built from CURRENT skill files (post framing/title/structure/intake rewrites), key contradictions hand-verified (viewer_stage cut rationale at vid-framing/WORKING-NOTES.md:26-40; goal enum drift at vid-framing/SKILL.md:57 vs vid-pressure-test/SKILL.md:74). "Verdict" here is a candidate for the D3 memo, not a decision.

Path shorthand: PIPE = vid-pipeline/SKILL.md, PT = vid-pressure-test/SKILL.md, PT-ASSET = vid-pressure-test/assets/pressure-test-frontmatter.md, VAULT = knowledge/vault-integration.md.

## piece.md (exhaustive)

### Keep: produced, consumed, load-bearing

| Field | Producer | Acted on by |
|---|---|---|
| type, slug | vid-intake:107-108 | identity + path key everywhere |
| status | vid-intake:111, vid-structure:62, PT:193 | PIPE:67,91-92,116 (the lifecycle the orchestrator routes on) |
| created / last_updated | intake once / every writer | resume list display (PIPE:70-71) |
| selected_angle | vid-framing:54 | PIPE:84 route, STRUCT:20 prereq, PT:26,64 |
| core_payoff | vid-framing:55 | STRUCT:20, SEG:75,78 |
| format | vid-framing:56 | planner selection in structure/intro/segment/ending/PT |
| goal | vid-framing:57 | vid-ending CTA (END:90-94), PT rubric (PT:73-75) |
| voice_context | vid-framing:58 | reference-piece selection in intro/segment/ending/PT |
| title | vid-title:157-159 | PIPE:85-86 route + thumbnail/intro/structure |
| segment_purposes / segments_completed | vid-structure:62 / vid-segment:199 | PIPE:87-90,108 count-compare route |
| tension_plan | vid-structure:62 | vid-segment reads, does not re-derive (SEG:93) |
| intro_locked / ending_locked | vid-intro:227 / vid-ending:187 | PIPE:88-91 routes |
| stories_used / proofs_used / metaphors_used | vid-segment:197, vid-intro:233 | reuse hygiene via story-pulling-criteria (SEG:104,257); schema-defined VAULT:401-403 |
| pressure_test_audit block | PT:174-190 | PT re-audit detection (PT:42) |
| claims_to_source_before_filming | PT:141,185 | non-empty blocks ready-to-film verdict (PT-ASSET:59,66-67) |
| soft_issues_list | PT:186 | PT re-audit surfaces priors (PT:42) |
| next_video | vid-ending:188 | the Bridge deliverable; future vid-measurement |
| pillar | vid-intake:116 | context load, weak consumption; keep |
| published | manual (VAULT:398) | post-publish record |

### Contradictions (the D3 core)

1. **viewer_stage: required, produced by nobody.** PT hard-requires it (PT:26) and weights rubrics on it (PT:80-81, rubric-conditioning.md:28,39, reviewer-retention-logic.md:43-50). vid-framing cut it 2026-06-28 (WORKING-NOTES:26,31) with the explicit note that PT "can derive temperature from the finished script"; that rederive was logged as out-of-scope later work (WORKING-NOTES:40) and never happened. Every real pipeline run now hits a missing hard prereq.
2. **goal enum drift.** Framing writes `sales | emails | views` (SKILL.md:57, asset:20); PT conditions on `goal: email` singular (PT:74). Billy's live piece carries `goal: email`. Three spellings of one enum.
3. **voice_pressure_test: two writers, object shape, last write clobbers.** vid-intro:231 and vid-segment:214 both write it as a single object per knowledge/voice-pressure-test.md:66; piece.md only ever reflects the LAST voice check. Needs array or sub-keys (intro / segments[] / ending).
4. **testimonials_used: written, undefined.** vid-intro:233 writes it; VAULT:401-403 does not define it; vid-segment never writes it. The graph promise for woven testimonials rests on an unschema'd field.
5. **frameworks_used: written, undefined, unread.** vid-segment:197; not in VAULT schema; no reader.
6. **iceberg_aligned: a gate nobody guards.** vid-intake claims leaving it unset "tells the pipeline the piece needs intake" (INTAKE:38), but PIPE routes on piece.md presence + selected_angle, never this flag. Also target-ambiguous (brain-dump template :59 vs "in piece.md" prose :36). Already named in skill-writing-lessons.md:66.

### Write-only (producer exists, nothing branches; cut or wire to vid-measurement)

| Field | Producer | Note |
|---|---|---|
| title_lane | vid-title:158 | no skill reads the lane |
| intro_strategy / intro_hook_type / intro_credibility_form | vid-intro:228-230 | appear only in PT-ASSET worked examples |
| ending_be_pattern | vid-ending:190 | same |
| cta_shape | vid-ending:189 | mirrors `goal`; redundant |
| visual_proofs_called_out | vid-intro:200, vid-segment:203-210 | surfaced to creator at save, never read after |
| pressure_test_status | PT:191 | orchestrator explicitly routes on `status`, not this (PT-ASSET:75,81) |
| pressure_tested_at | PT:192 | admitted duplicate of pressure_test_audit.ran_at (PT-ASSET:77) |
| alignment_note | vid-intake:60 | narrative note, unconsumed |

### Fully dead (no producer, no consumer)

- **outlier_anchor / anchor_confidence**: cut from framing (WORKING-NOTES:32, "write-only fields no skill read"); survive only in PT-ASSET:124-125 worked-example frontmatter, which still attributes them to vid-framing.
- **problem_addressed**: written by no current skill; present in 3 live-vault pieces. Residue.
- **Stale spec risk**: PT-ASSET:96,123-125 still instructs preserving viewer_stage/outlier_anchor/anchor_confidence "written by vid-framing." That asset re-teaches the dead schema to anyone who loads it.

## script.md

| Field | Verdict | Reason |
|---|---|---|
| type, piece wikilink | keep | identity + graph edge |
| status: outlined | cut candidate | shadow status; piece.md `status` is the real lifecycle |
| tier | cut candidate | write-only |
| last_refreshed | keep | freshness |
| Body sections (## Intro, body, ## Ending, ## To build) | keep | the deliverable; vid-ending reads ## Intro verbatim (END:60,261), vid-segment reads ## Blocks to capture (SEG:112), PT audits whole file |

## brain-dump.md

| Field | Verdict | Reason |
|---|---|---|
| type, slug, captured | keep | identity |
| intake_mode | cut candidate | explicitly "a record, not a routing decision" (INTAKE:49); nothing reads it |
| iceberg_aligned, alignment_note | cut candidates | same dead flags as piece.md |
| Body (raw dump, topic, audience, outcome, material, claims/TODOs) | keep | the lossless source all writers mine (framing:26,39; STRUCT:29,47; SEG:67; TITLE:52; PT:53) |

## thumbnail-brief.md

| Field | Verdict | Reason |
|---|---|---|
| title_paired | keep | vid-intro derives Top-3 questions from title+thumbnail (INTRO:59,71) |
| body: locked picks + BENS + rationale | keep | vid-intro reads picks (INTRO:59); vid-title avoids repeating picks (TITLE:109) |
| strategies_tested, picks | keep (thin) | post-publish learning record |
| creation_path | keep | self-consumed in wrap-up (THUMB:172-176) |
| status: brief-ready | cut candidate | pipeline routes on FILE PRESENCE (PIPE:87), not this field |

D1 relevance: the fields downstream skills actually consume from thumbnail-brief are title_paired + the locked picks. Everything else is process record. That is the payload size to weigh when deciding whether the brief folds into piece.md.

## Bank entries

Internally consistent: every field is schema-defined and has at least a query/filter consumer (SEG:97-102, INTRO:61-62, END:69; used_in reciprocal updates SEG:201, END:192). The breakage lives on the piece.md side (contradictions 4 and 5) and in the F1 framework folder split (see reference map).

## Live-vault ground truth (business-os Content/pieces/)

- **18 of 20 piece.md files are hermes-generated stubs** with a foreign schema (generated-by, department, platforms, subject_line...). No vid-* skill writes or reads those fields. vid-pipeline's Step 2 scan (PIPE:67) reads `Content/pieces/*/piece.md` and would misread these as in-progress video pieces. Live collision risk between the hermes system and the vid pipeline sharing one folder.
- **The one real pipeline piece** (21-claude-cowork-lessons) matches current producers on every live field, and carries exactly the dead set this registry predicts: iceberg_aligned, problem_addressed, viewer_stage, outlier_anchor/anchor_confidence, goal: email (the drifted enum).
