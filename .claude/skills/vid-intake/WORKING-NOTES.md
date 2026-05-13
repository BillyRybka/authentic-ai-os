---
type: dev-notes
status: in-progress
skill: vid-intake
captured: 2026-05-09
---

# vid-intake WORKING-NOTES

Source citations for every claim, example, and rule in vid-intake. This file lives during development. Lead deletes before productization. Phase 3 QA agent uses it to verify source-backing trace.

## Source citations

- **Claim:** "20+ videos solving the same 3 problems your audience cares about" / channel coherence anchored in Top 3
- **Source:** `c:/Users/billr/projects/business-os/Resources/references/ed-lawrence-ygs/materials-shared/ytgs4-manuals-instructions.txt`
- **Lines:** 175-176 ("the channel's top 3 problems viewers come back for" + "your buyers' top 3 problems"), 2240 ("20+ videos solving the same 3 problems your audience cares about")
- **Notes:** Drives the alignment check. Productized as the Top 3 layer of the alignment gate. No attribution.

- **Claim:** "make sure it aligns with the 3 problems your viewer cares about" (validation step on a video idea)
- **Source:** `materials-shared/ytgs4-manuals-instructions.txt`
- **Lines:** 2119
- **Notes:** Productized as Phase 4 alignment surface. Verbatim sanity check shape.

- **Claim:** Ending Pivot/Gap/Bridge calls out "the next of your channel's three core problems"
- **Source:** `materials-shared/ytgs4-manuals-instructions.txt` line 3068, plus `Resources/references/ed-lawrence-ygs/frameworks.md` line 372
- **Notes:** Cited in vid-intake as why the Top 3 alignment matters (not enforced in vid-intake save, just rationale for the gate). vid-ending will read `aligned_with` to pick the next-problem Gap.

- **Claim:** Buyer Top 3 = Viewer Top 3 (you build an audience full of your buyers)
- **Source:** `materials-shared/ytgs4-manuals-instructions.txt`
- **Lines:** 175-176
- **Notes:** Source treats them as the same. Verified explicitly with Billy 2026-05-09. No separate buyer/viewer Top 3 fields in foundation schema.

- **Claim:** Iceberg = source's "umbrella" concept (creator-facing rename)
- **Source:** Locked in `build-plan.md` Section 12 work log entry 2026-05-05 (vid-foundation Stage 1 restructure to Iceberg Discovery). Source uses "umbrella" terminology, productized as "iceberg" everywhere.
- **Notes:** vid-intake productized files NEVER reference "umbrella" or "aka umbrella". Iceberg only.

- **Claim:** Story-first mode → P-A-O capture, then locate the lesson
- **Source:** `knowledge/story-capture-guide.md` lines 69-93 (P-A-O structure) + lines 95-309 (6 dynamic prompts)
- **Notes:** Mode 7 in vid-intake invokes this guide. The 6 prompts handle the unlock-when-stuck case. No duplication of guide content in vid-intake references.

- **Claim:** Case study videos must be teaching arcs, not biographies
- **Source:** Confirmed with Billy 2026-05-08 directly ("we have to wrap it up so it can't be like 'why Aaron did this, why Aaron did that'"). Billy's interpretation of source case-study teaching from Phase 05.
- **Notes:** Mode 6 in vid-intake forces the pivot from proof capture to lesson capture. The skill explicitly asks "what does the viewer learn that they can DO?" before saving.

- **Claim:** Inspired-by mode source is invisible in productized output
- **Source:** Confirmed with Billy 2026-05-09 ("You'll never reference and be like 'Oh, Steve did this' so I think that is wrong"). Aligns with locked decision #15 (attribution scrub) at the source-creator level.
- **Notes:** Mode 4 captures source points in `source_internal_only` frontmatter field. Skill explicitly states this contract upfront when running Mode 4.

- **Claim:** Brain dump IS the voice (preserve creator's exact phrasing)
- **Source:** `build-plan.md` locked decision #6 (Voice handling): "The brain dump IS the voice. Claude structures the creator's actual phrases — never generates from scratch."
- **Notes:** Drives all mirror-back behavior. Drives the "use creator's exact phrasing" rule throughout the SKILL.md and references.

- **Claim:** Examples-first contrastive (worked + near-miss + why)
- **Source:** `build-plan.md` locked decision #9 (amplified version added 2026-05-07).
- **Notes:** All 3 references files (mode-conversation-examples, iceberg-and-top-3-alignment, push-vs-pause-rules) follow this structure.

- **Claim:** Conversational discipline = short messages, ask-and-wait, no reference dumping
- **Source:** Pattern matched from `.claude/skills/vid-title/SKILL.md` (gold-standard conversational pattern, locked 2026-05-01)
- **Notes:** Same Q-script discipline applied to vid-intake. Phase structure mirrors vid-title's approach.

## Examples sourced from

- **Example:** Fitness coach iceberg + Top 3 used in mode-conversation-examples.md
- **Source:** Synthesized example, not pulled from source material. Niche descriptors per locked decision #15 (no public-figure named creators).
- **Notes:** "Busy founders building strength habits in 30 min/day" is a synthesized fitness-coaching iceberg. Top 3 problems (time scarcity, cardio-bias, inconsistency under stress) are synthesized but recognizable as common founder-fitness pain points. No specific creator referenced.

- **Example:** James client win (135 to 225 squat in 12 weeks)
- **Source:** Synthesized example, fictional client name. Numbers chosen to be plausible for a fitness coaching scenario.
- **Notes:** Used in Mode 6 example. Anonymizable as "the client" if creator prefers.

- **Example:** $40k in 3 months YouTube depth-vs-frequency
- **Source:** Synthesized claim for the inspired-by mode dialogue. Plausible result for a coaching channel.
- **Notes:** Realistic enough to feel like a real claim in a real conversation.

- **Example:** Steve / "some YouTube guru" example for inspired-by mode
- **Source:** Synthesized scenario. "Steve" is generic, not a real creator. The 4 points (post 3x/week, clickbait, comments, cross-promo) are common YouTube-growth advice.
- **Notes:** Demonstrates the source-invisible contract in Mode 4.

## Anti-patterns sourced from

- **Anti-pattern:** Hard-blocking the creator on alignment fail
- **Source:** `build-plan.md` locked decision #11-12 amplified (implementation engine, not gate). Plus the 2026-05-02 build-plan softening pass (REJECT → soft friction language).
- **Notes:** vid-intake never blocks save. Always allows override with rationale captured.

- **Anti-pattern:** Forcing a fit that isn't there (stretching alignment)
- **Source:** Confirmed with Billy 2026-05-09 ("don't say show because if it really isn't solving a top three problem, then we need to adjust").
- **Notes:** Skill surfaces mismatch honestly rather than papering over it. Captured in iceberg-and-top-3-alignment.md "Near-miss: forcing a fit."

- **Anti-pattern:** Running an interrogation instead of a conversation
- **Source:** Pattern from `.claude/skills/vid-title/SKILL.md` and Billy's repeated guidance about adaptive drilling and pleasurable conversation flow.
- **Notes:** Captured in push-vs-pause-rules.md and the Mode 1 near-miss in mode-conversation-examples.md.

- **Anti-pattern:** Asking the lesson before the story is told (Mode 7)
- **Source:** Logic check based on how stories work emotionally. Confirmed pattern from `knowledge/story-capture-guide.md` (Problem before Outcome rule).
- **Notes:** Captured in mode-conversation-examples.md Mode 7 near-miss.

- **Anti-pattern:** Mode 4 referencing source creator's name in productized output
- **Source:** Confirmed with Billy 2026-05-09. Aligns with locked decision #15.
- **Notes:** Captured in mode-conversation-examples.md Mode 4 near-miss.

- **Anti-pattern:** Mode 6 making a client biography instead of teaching arc
- **Source:** Confirmed with Billy 2026-05-08 directly.
- **Notes:** Captured in mode-conversation-examples.md Mode 6 near-miss.

## Cross-skill dependencies confirmed

- **vid-foundation produces:** creator-foundation.md (iceberg + Top 3 + audience). vid-intake reads at startup.
- **vid-voice-capture produces:** voice-profile.md. vid-intake reads at startup for mirroring style.
- **vid-capture writes:** banks/{type}/{slug}.md entries. vid-intake wikilinks pulls from these into brain-dump.md.
- **vid-framing reads:** brain-dump.md vid-intake produces. Picks angle, format, goal.
- **vid-pipeline (future) invokes:** vid-intake at start of SCRIPT phase.
- **knowledge/story-capture-guide.md:** loaded by vid-intake when Mode 7 runs OR when any mode needs to drill a thin story. Already loaded by vid-capture, vid-segment, vid-intro per its frontmatter.
- **knowledge/vault-integration.md:** loaded by vid-intake to honor frontmatter schema for brain-dump.md and the wikilink contract.

No circular dependencies. vid-intake is upstream of every writing skill except vid-foundation, vid-voice-capture, and vid-capture (which it depends on).

Delete this file when the skill is finalized.
