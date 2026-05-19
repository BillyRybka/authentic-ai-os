---
type: dev-notes
status: in-progress
skill: vid-research
captured: 2026-05-10
---

# vid-research WORKING-NOTES

Source citations for every claim, rule, and example. Dev scaffolding — deleted before productization. Phase 3 QA agent uses this to verify source-backing trace.

Source root: `c:/Users/billr/projects/business-os/Resources/references/ed-lawrence-ygs/`

## Methodology citations

- **Three-Circle Research (own + niche + adjacent)** — `modules/phase-04-video-strategy-ideation/lesson-03-the-basics-of-research-strategy/notes.md` lines 27-30
- **Outliers = 2x channel average + raw-count meaningful** — same file, lines 22-25
- **Adjacent niches: extract structures NOT topics** — `modules/phase-04-video-strategy-ideation/lesson-04-task-how-to-find-patterns/transcript.md` line 60
- **Pattern bank fields (topics, title structures, power words, thumbnail styles, thumbnail text, formats, things-viewers-hate)** — same file, line 16
- **Theory of One ("just because a pattern worked for another channel doesn't mean it will work for yours")** — `modules/phase-04-video-strategy-ideation/lesson-07-task-how-to-ideate-your-next-3-4-videos/notes.md` line 47
- **5 niche channels minimum, 10 ideal** — `lesson-04-task-how-to-find-patterns/transcript.md` line 52
- **Repeat what works first, raid niche after** — same file, line 46
- **Avoid analyzing channels too large (Hormozi-tier)** — `lesson-03-the-basics-of-research-strategy/notes.md` line 56
- **Pattern bank rebuilt every 6 months** — `video-pipeline-map.md` line 119. We use 90-day refresh + 6-12 month full rebuild.
- **3-4 hours first time, 15 min/day to build muscle** — `lesson-04-task-how-to-find-patterns/transcript.md` line 70. We target ~1.5 hours with AI compression.
- **6 thumbnail strategies (Cognitive Dissonance, Result, Social Hack, Curiosity, Before/After, Minimal)** — `video-pipeline-map.md` line 99 + `lesson-07-task-how-to-ideate-your-next-3-4-videos/notes.md` line 33

## Example citations

- **Livin Leggings (yoga → 25k to 450k subs via adjacent niche)** — `lesson-03-the-basics-of-research-strategy/notes.md` lines 33-34, 46-47. First video 2.4M, second 8.2M. Public, widely-known case. Per decision #15, name flagged for QA judgment — replace with "a yoga channel" if stricter scrub preferred.
- **"Just use one that already worked and change the color of your outfit" quote** — same file, line 62. Used illustratively without naming the speaker.
- **HealthyGamerGG outlier (~200k avg, 700k "Self Loathing Man of Inaction")** — same file, line 23. Held in reserve; not currently in productized files.

## Synthesized rules (not directly stated in source, but consistent with it)

- **Fluke filter (Layer 3 of outlier identification)** — Synthesized from Three-Circle's "study what your viewers want" framing. Off-niche flukes don't represent audience demand. "Underwater basket weaving on a dog training channel" framing created with Billy 2026-05-09.
- **Power words split (Global vs Audience-Specific)** — Refinement of source's single-category treatment. Introduced by Billy 2026-05-09.
- **Sticky-curated growth model** — Productization choice. Source treats research as periodic full rebuild; we layer sticky-curation on top so creator's accumulated taste compounds across sessions.
- **AI-compressed timeline (1.5 hours vs source's 3-4 hours)** — Productization claim. Manual work compresses with API + vision + LLM extraction. Theory of One curation remains roughly same length.

## Cross-skill dependencies

- **Reads:** `foundation/creator-foundation.md`, `foundation/voice-profile.md`
- **Writes:** 7 bank files in `banks/`
- **Downstream consumers:** vid-framing (pattern-bank synthesis + topic clusters + 3 sub-banks), vid-title (power-words, title-patterns), vid-thumbnail (thumbnail-patterns, power-words). Also authors packaging-system.md (read by vid-title, vid-thumbnail, vid-framing, vid-structure, vid-pressure-test). Banks consolidated 7 to 4 on 2026-05-19; format-patterns / topic-patterns / viewer-hates retired (see build-plan).
- **Shared knowledge:** `knowledge/three-circle-research.md`, `knowledge/outlier-identification-rules.md` (both loaded by future vid-channel-audit and vid-measurement)
- **Future feedback loop:** vid-measurement writes confirmed winners back to relevant banks with `confidence: proven` flag

## QA notes

- All productized files (SKILL.md, references/*, knowledge/*, assets/*, scripts/*) must have ZERO source-curriculum attribution. Grep for: "Ed", "Ed Lawrence", "YGS", "ytgs", "ed-lawrence-ygs", "source teacher", "source curriculum", named-instructor.
- One named-creator example survives in `knowledge/three-circle-research.md`: "Livin Leggings." Public case; per decision #15, public-figure named creators in calibration material get replaced with niche/category descriptors. If QA wants stricter scrub, swap "Livin Leggings" → "a yoga channel" (example still works without name).
- Python scripts use Python stdlib only. No pip dependencies. Setup is "Python 3.7+ installed."
- All synthesized examples (strength coach @CoachX, YouTube growth coach, etc.) use placeholder channel handles. No real channels referenced.
- "Underwater basket weaving" example created in this conversation as a memorable illustration of off-niche flukes.

Delete this file when the skill is finalized.
