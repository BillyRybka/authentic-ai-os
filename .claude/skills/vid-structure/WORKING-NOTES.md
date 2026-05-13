---
type: dev-notes
skill: vid-structure
visibility: dev-only
ship: false
last_updated: 2026-05-13
---

# vid-structure Working Notes (dev-only, never ships)

Internal citations and decisions log. NOT shipped with the plugin. NOT loaded at runtime. Used during development to track source-fidelity and design choices.

## Source citations (Ed Lawrence / YGS)

- **Brain-dump to first-draft transition.** Source teaches "open your plan that you've spent time preparing... your only goal is to get to the end of the first draft as fast as you can using it. Dump everything out. There's no editing." Productized: vid-structure mines the brain-dump against the angle BEFORE first-draft writing (vid-segment). The mining step is an honest extension. Source teaches the filtering as embedded in first-draft writing; this system decouples capture (vid-intake) from writing (vid-segment), so the filtering moment lives in vid-structure between them.

- **Format-driven shape.** Source teaches "the structure is [INTRO → EMOTION → LOGIC → END]" or "[INTRO → E/L pairs for each point → END]" depending on format. Different formats prescribe different shapes. Productized: format planners in `knowledge/format-planners/` define the body shape per format; vid-structure reads the matching planner and uses its prescribed shape (narrative arc for case-study, N segments for listicle/short-process/etc.).

- **Segment/point count emerges from material, not formula.** Source teaches "most videos are made up of several points. It could be three, five, ten, twenty, it doesn't really matter." The number emerges from brain-dump material matched to format-fit. Productized: vid-structure surfaces a proposed count derived from mined material, but flags mismatch when material is thin/heavy for the locked format.

- **Title-promise discipline (anti-early-payoff).** Source teaches "if you give away the point too early, there's no tension that remains... So they stop paying attention or comment 'get to the point.'" Productized: knowledge/script-tension-architecture.md formalizes the title-promise location at 60-80% through body, with vid-structure surfacing early-payoff risk as soft friction.

- **Setup-payoff tension architecture.** Source teaches "as soon as you pay off something, you set it up" plus the tension graph metaphor. Productized: knowledge/script-tension-architecture.md teaches the script-level tension graph + threading + handoff rules. Per-segment STP stays in vid-segment's references/setup-tension-payoff-shapes.md. Cross-segment tension is the new shared knowledge.

## Design decisions (with rationale)

### Cut: inline vid-title and vid-intro invocations (changed from 2026-05-11 contract)

Original contract had vid-structure invoking vid-title and vid-intro as sub-skills. Three audit agents (workflow simulator, over-engineering hawk, source fidelity critic) converged on cutting both. Reasons:

- vid-title needs only framing (no segment breakdown). Conflating with structure violates anti-mirror discipline.
- vid-intro needs title + thumbnail (not segment breakdown). Same issue.
- Source treats title-writing and intro-writing as separate downstream craft.
- vid-pipeline (built last) is the right place to sequence skills, not vid-structure.

**Decision:** vid-structure writes script.md skeleton ONLY. Pipeline orchestrates title/thumbnail/intro/segments/ending.

### Cut: piece.md `segment_count` field (changed from 2026-05-11 contract)

Redundant with script.md section headers and `segment_purposes` array. Downstream skills walk segment_purposes or script.md directly. Removed segment_count to keep piece.md as accumulator-not-index.

### Kept: piece.md `segment_purposes` field (material-anchored)

Originally proposed as abstract labels. Billy caught (2026-05-13) that vid-structure mines material AND maps to segments. So segment_purposes are material-anchored, not abstract. This makes them load-bearing for vid-segment ("which lessons land in segment 3?").

### Added: piece.md `tension_plan` block

New field. Captures central_question, title_promise_segment, active_threads. Consumed by vid-segment (per-segment tension role) and vid-pressure-test (retention audit). Honest extension. Source teaches tension architecture as a writing discipline; we formalize it as a planning artifact.

### Two phases, not four (changed from 2026-05-11 contract)

Original contract had 4 phases. Audit-1 over-engineering hawk verdict: merge Keep/Cut/Combine into Phase 1, cut sub-skill invocations (which were Phases 3-4). Result: Phase 1 (mine + propose) + Phase 2 (write skeleton). Two phases, single conversation.

### New shared knowledge: knowledge/script-tension-architecture.md

Cross-segment tension flow as new shared knowledge file (224 lines, under 250 target). Loaded by vid-structure (cross-segment planning), vid-segment (per-segment tension role context), vid-pressure-test (retention audit).

Distinct from vid-segment's local `references/setup-tension-payoff-shapes.md` (per-segment STP). Clean split: per-segment STP in vid-segment skill-local; cross-segment in shared knowledge.

### Cut: references/format-skeleton-shapes.md

Audit-1 trim. SKILL.md Phase 1.3 already inlines format-native shapes (case-study narrative, listicle N items, short-process steps, etc.). Building format-skeleton-shapes.md would duplicate format-planners or restate SKILL.md content. YAGNI cut.

## Files in this skill

```
.claude/skills/vid-structure/
├── SKILL.md (328 lines, target <500 ✓)
├── references/
│   ├── brain-dump-mining.md (under 250 ✓)
│   └── structure-conversation-examples.md (under 250 ✓)
├── assets/
│   └── script-skeleton-template.md (under 250 ✓)
└── WORKING-NOTES.md (this file, dev-only, not shipped)
```

Plus new shared knowledge:
```
knowledge/script-tension-architecture.md (224 lines, target <250 ✓)
```

## Open questions / future work

- **vid-segment integration:** does vid-segment currently read piece.md `segment_purposes` and the script.md bullet outline that vid-structure now produces? If not, audit and patch.
- **vid-ending tension role:** vid-ending should know whether the body ended on the title-promise payoff or post-payoff application (relevant to ending pivot shape). Document handoff in vid-ending references.
- **vid-pressure-test tension audit:** when vid-pressure-test is built, ensure it reads knowledge/script-tension-architecture.md and runs the 5 anti-pattern checks (early-payoff, broken-thread, cold-handoff, overload, promise-drift).
- **Re-structure mode preservation:** when re-structure runs, cuts logged in script.md HTML comment should stick (don't re-propose previously-cut entries). Verified in conversation-examples Example 2; double-check in real testing.

## Live-testing plan

After build: run vid-structure on a real piece end-to-end. Suggested test piece: a recent Billy idea that has brain-dump captured + framing locked. Watch for:

- Does the outline proposal feel like a sparring partner or NPC-tick?
- Does material-anchored purpose generation feel natural, or does Billy want different labels?
- Does the bricks-surfaced-not-locked rhythm hold? Does Billy try to lock at outline time?
- Does script-tension-architecture's title-promise-late discipline surface real friction in his usual writing pattern?
- Does the format-mismatch flag (Case Study vs deep-dive volume) ever fire on real material?

Friction surfaces faster than another round of audits. Build → ship → run → fix.
