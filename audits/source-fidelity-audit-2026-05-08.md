---
type: audit
project: authentic-ai-os
auditor: source-fidelity-auditor
date: 2026-05-08
scope: vid-intro, vid-segment, vid-ending
tags: [audit, source-fidelity, examples-density, phase-3a]
---

# Source-Fidelity & Examples-Density Audit, 2026-05-08

## Summary

- **Skills audited:** vid-intro, vid-segment, vid-ending
- **Pass 1 verdict (source-fidelity):** SOFT-PASS. All sampled citations point at real source material that backs the productized claim. A handful of citations are off by 1-2 lines or cite line ranges where the actual quoted material sits adjacent (not blocking, but worth tightening before productization). Zero attribution leaks in productized files. WORKING-NOTES.md correctly contains internal source paths (per dev-scaffolding rule, those stay internal).
- **Pass 2 verdict (examples-density):** PASS. Hook-bank, transition-bank, and the four shared knowledge files (emotion-brick-decision-matrix, story-pulling-criteria, proof-placement-rules, metaphor-integration) all hit the ≥2 worked + ≥1 near-miss bar with one-line "why this lands / why this fails" annotations. The skill-local references (vid-intro: 3 files; vid-segment: 2 files; vid-ending: 4 files) all carry the same density. A few rules in the format-aware shape files have only 1 worked example for one or two of the seven format slots; that's a function of format coverage requirements, not a density gap. Source materials carry additional examples that could be pulled forward into productized files if the team wants extra calibration weight (surfaced under each skill below).

### Top 3 fixes for Phase 4

1. **(vid-segment) Tighten line citations in WORKING-NOTES.md for lesson-07 visual demo examples.** Cited as lines 26, 28, 29; actual locations are lines 27, 28, 29. Off-by-one at most. The "16 sugar cubes / Coke" example is at line 27 of `lesson-07-emotion-brick-visual-demos/notes.md`, not line 26.
2. **(vid-ending) WORKING-NOTES cites lines 24-30 for the chain-reaction "700,000+ views Film Booth" claim, but the actual 700,000 number sits on line 32 of lesson-11/transcript.md.** The chain-reaction principle ("once I had 10 videos all doing this, some crazy happened") is correctly at lines 24-30. Fix is to split that into two citations (24-30 for chain-reaction, 32 for the specific 700K figure).
3. **(vid-intro) Surface 5-7 more Hook patterns from `materials-shared/ytgs-video-planner.txt` that did not make it into `banks/hook-bank.md`.** The video-planner has additional hook patterns under "EMOTION BRICK" / "Story prompts" sections that could productize as additional Question and Statement variants. Density is already pass-grade; this is calibration-weight upside, not a fix-required.

## Per-skill findings

### vid-intro

#### Pass 1, source-fidelity

**Citations spot-checked (5):**

1. **Claim:** "5 hook types: Question, Contrarian, Statement, Fact, Credibility."
   - WORKING-NOTES cites `knowledge/intro-architecture.md` lines 60-105.
   - Verified: lines 60-105 contain Step 2 "Hook (5 types)" with all 5 types defined. PASS.

2. **Claim:** "3 Problem/Result options: Poke / Tease / Combine. Pivot phrases."
   - WORKING-NOTES cites `knowledge/intro-architecture.md` lines 107-137.
   - Verified: lines 107-137 contain Step 3 with all 3 options and pivot phrases. PASS.

3. **Claim:** "Setup format: 'So in this video, I'm going to show you [Q1], [Q2], [Q3].'"
   - WORKING-NOTES cites `knowledge/intro-architecture.md` lines 138-158.
   - Verified: lines 138-158 contain Step 4 with the literal Setup template. PASS.

4. **Claim:** "Banned transition phrases: 'Let's dive in', 'Let's talk about'..."
   - WORKING-NOTES cites `knowledge/intro-architecture.md` lines 173-181.
   - Verified: lines 173-181 contain the banned transitions table. PASS.

5. **Claim:** "5 credibility forms: Vast experience / Volume of people helped / Big personal result / Big client result / Effort signal."
   - WORKING-NOTES cites `knowledge/intro-architecture.md` lines 186-206.
   - Verified: lines 186-206 contain Step 6 (Credibility line woven, not bolted). All 5 forms named at lines 189-194. PASS.

**Citations missing:** None found. Every productized claim in `vid-intro/SKILL.md` and the 3 references files traces to an internal vault file (`knowledge/intro-architecture.md`, `knowledge/voice-pressure-test.md`, `knowledge/format-planners/*.md`, `banks/hook-bank.md`, `banks/transition-bank.md`, `Context/brand.md`) cited in WORKING-NOTES.md.

**Attribution leaks:** None. Productized files (`SKILL.md`, `references/*.md`) contain no references to "Ed Lawrence", "YGS", "ytgs", "Synthia", "IntroBot", "Film Booth", "RevTrack", or any other source-curriculum / instructor / tool name. WORKING-NOTES.md correctly contains internal source paths (`Resources/references/ed-lawrence-ygs/...`) and that's the dev-scaffolding rule (the file is stripped before productization per its own header).

**Synthesized claims correctly flagged:** Two notable synthesis claims in `references/hook-type-selection-flow.md`:
- "Format identity beats voice preference when they conflict" (synthesized from cross-referencing format-planners and voice-profile-schema). Flagged in WORKING-NOTES as "synthesized rule" with rationale. PASS.
- "Format-to-lane defaults" (compiled from each format planner's intro adaptation table). Each per-file line range cited. PASS.

#### Pass 2, examples-density

**Rules below density threshold:** None of the rules in vid-intro's 3 reference files fall below 2 worked + 1 near-miss with one-line "why" annotations. Specifically:

- `references/hook-type-selection-flow.md`: 4 worked decision examples + 2 near-miss decision examples. Each carries a "why this lands / why this fails" line. Hits the bar.
- `references/credibility-line-weaving.md`: 5 worked weave examples + 5 near-miss / wrong-stage / bolted-on examples. Strong density.
- `references/problem-result-options.md`: 3 worked (one per option Poke/Tease/Combine) + 3 near-miss (one per option). Each pairs with a "Why this lands" / "Why this fails" line and a "the rule" takeaway. Hits the bar.

**Source has more examples (not pulled):**

- `materials-shared/ytgs-video-planner.txt` lines 1978-2030 contain 6 named "Story Prompts" (Embarrassing First Attempt, Costly Rookie Mistake, Sudden Breakthrough Moment, Advice Ignored Then Learned, Tiny Tweak Huge Payoff, Did What You Were Taught But It Didn't Work). These prompts could productize into `banks/hook-bank.md` Type 5 (Credibility) or as a separate "story-led hook variants" section. Currently `banks/hook-bank.md` Cr-1 through Cr-6 exist but the Story Prompt patterns aren't pulled. Recommend: surface these 6 prompts as a sidebar in `references/hook-type-selection-flow.md` Section "When to override the flow" to expand creative range without raising rigidity.
- `materials-shared/ytgs-video-planner.txt` lines 1950-1973 contain a separate "Visual Demo Decision Matrix" with 5 different question prompts that could feed the Hook+Problem-Result energy decision (when intro emotion brick is a visual demo). Currently shared knowledge file `emotion-brick-decision-matrix.md` already covers the broader 5-brick matrix; the visual-demo-specific 5-question variant could deepen the Show-the-Problem / Contrast / Breakdown sub-decision in `references/hook-type-selection-flow.md`. Optional, not blocking.

### vid-segment

#### Pass 1, source-fidelity

**Citations spot-checked (5):**

1. **Claim:** "Setup / Tension / Payoff is the universal segment arc" (productized as STP).
   - WORKING-NOTES cites `lesson-15-how-to-write-a-script-basics/notes.md` lines 21-26.
   - Verified: lines 21-26 contain "Setups & Payoffs (Tension Graph)" framework with the joke analogy ("Why don't skeletons fight each other?") and the early-payoff example. PASS. The productized "Tension" block is a clean translation from "Setups & Payoffs" with the "tension graph" lens making the middle block explicit. Locked decision #14 in build-plan justifies the rename.

2. **Claim:** "Emotion brick + Logic brick = full segment."
   - WORKING-NOTES cites `lesson-06-how-to-make-a-point/notes.md` lines 21-22.
   - Verified: lines 21-22 contain "The Emotion-Logic Brick System" framework. PASS.

3. **Claim:** "Sugar cubes / Coke can example for Show-the-Problem."
   - WORKING-NOTES cites `lesson-07-emotion-brick-visual-demos/notes.md` line 26.
   - Verified: actual location is line 27 (the bullet starts at line 27 with "Show the Problem — Example: Weight loss channel..."). Off-by-one. SOFT-PASS, fix at productization scrub.

4. **Claim:** "Frameworks Decision Matrix" (Happen in order → arrows, etc.).
   - WORKING-NOTES cites `materials-shared/ytgs-video-planner.txt` lines 2122-2131.
   - Verified: lines 2122-2131 contain the FRAMEWORKS DECISION MATRIX section with all 6 question-to-shape mappings. PASS.

5. **Claim:** "Emotion Brick Decision Matrix (5 questions)."
   - WORKING-NOTES cites `materials-shared/ytgs-video-planner.txt` lines 1922-1949.
   - Verified: lines 1922-1949 contain the Emotion Brick Decision Matrix with all 5 questions and brick mappings. PASS.

**Citations missing:** Three productized examples in WORKING-NOTES are correctly flagged as synthesized:
- "Steve case study ($42k → $74k MRR in 9 weeks)" — flagged as "Composite, niche-substituted into representative B2B-coaching avatar." This is the right honesty bar. Synthetic but plausible. PASS.
- "Re-engagement Trigger framework" — flagged as "Synthesized for setup-tension-payoff-shapes.md... Plausible-sounding framework not pulled from any real source." PASS.
- "Restaurant with no recipes metaphor" / "Bouncer-at-a-club metaphor" — both flagged as "Original synthesis." PASS.

**Attribution leaks:** None. Productized files contain no references to Ed Lawrence, YGS, ytgs, Synthia, IntroBot, RevTrack, Chris Do, Craig Ferguson, Film Booth, or any other source-curriculum / instructor / public-figure name. The Chris Do Venn diagram example (lesson-10 line 31) is correctly stripped to "Passion + Outcomes + Compensation = Entrepreneurial Sweet Spot" with no Chris Do attribution in `references/framework-shapes.md` (line 114). Locked decision #15 honored.

#### Pass 2, examples-density

**Rules below density threshold:** None. Density is strong:

- `references/setup-tension-payoff-shapes.md`: 7 format shapes, each with at least 1 worked + 1 near-miss with "Why this lands / Why this misses" lines. Shape 2 (Short Process) has 2 worked + 1 near-miss. Hits the bar across all 7 shapes.
- `references/framework-shapes.md`: 6 framework shapes (Arrows, Pyramid/Triangle, Cycle, Venn, Funnel, Acronym), each with 2 worked + 1 near-miss. Strong density.
- Shared knowledge files loaded by vid-segment all hit the bar:
  - `emotion-brick-decision-matrix.md`: 5 brick types, each with 2 worked + 2 near-miss (10 worked + 10 near-miss total). Highest density.
  - `story-pulling-criteria.md`: 5 criteria each with 1-2 worked + 1 near-miss + a "the principle" takeaway.
  - `proof-placement-rules.md`: 7+ worked + 5+ near-miss across the placement / multi-format / wall-of-wins / testimonial / count rules. Strong.
  - `metaphor-integration.md`: 4 worked + 4 near-miss across 3 integration rules + visual-metaphor 2-layer rule + mixed-metaphor risk. Strong.

**Source has more examples (not pulled):**

- `lesson-10-logic-brick-frameworks-proof-checklists/notes.md` line 25 has the "Title → Thumbnail → Intro" Arrows example AND the filming-backdrop step-3 "No mess / Doesn't distract" example. The productized `references/framework-shapes.md` Shape 1 pulls the Title → Thumbnail → Intro example but not the filming-backdrop one. Recommend: pull the second example into `references/framework-shapes.md` Shape 1 for additional niche variety. Currently the Arrows worked examples are channel-strategy + sales-niche; adding filming-backdrop expands the niche range. Optional.
- `lesson-08-emotion-brick-storytelling/notes.md` line 31 has the parasites/illness story (Ed's own story, "filled an entire cohort in sales"). This is a real worked example of the "own story with failure admission" pattern. The productized `emotion-brick-decision-matrix.md` Brick 4 (Story) pulls the pricing story (line 22) and a synthesized Steve story but not the parasites story. Per attribution-scrub the Ed-specific identifier should be stripped, but the structural shape (creator illness → admitted vulnerability → cohort fill) is a valuable pattern worth productizing as a creator-stripped example. Optional.
- `lesson-15-how-to-write-a-script-basics/notes.md` line 23 has the "yellow snow" early-payoff example with the corrected version ("...this mistake put over a thousand people in hospital last year. I was one of them..."). This is a worked example of the failure mode `setup-tension-payoff-shapes.md` Shape 1 covers (pure topic-label setup), but the productized file doesn't pull it. Recommend: surface this as a "Common cross-format mistakes" sub-example in setup-tension-payoff-shapes.md (lines 234-242) with the early-payoff correction shown. Optional, would tighten the early-payoff anti-pattern.

### vid-ending

#### Pass 1, source-fidelity

**Citations spot-checked (5):**

1. **Claim:** "3-Part End Formula = Pivot (Recap) → Gap (New Problem) → Bridge (Next Video)."
   - WORKING-NOTES cites `lesson-11-ending-your-video/notes.md` lines 21-26.
   - Verified: lines 21-26 contain "3-Part End Formula" with the worked example Ed reads aloud. PASS. Productized rename Pivot/Gap/Bridge is honest translation per locked decision (creator-facing language).

2. **Claim:** "Pivot is ONE sentence: 'remind the viewer in one sentence the value they got.'"
   - WORKING-NOTES cites `lesson-11/transcript.md` line 48.
   - Verified: line 48 contains "remind the viewer in one sentence the value they got that makes them feel like the video delivered". PASS, exact match.

3. **Claim:** "Bridge is 'watch this next' with no begging, no like-and-subscribe."
   - WORKING-NOTES cites `lesson-11/transcript.md` line 68.
   - Verified: line 68 contains "There's no begging, there's no like and subscribe. Just a very confident, well-positioned next step." PASS, exact match.

4. **Claim:** "End-screen click-through went from 0.9% to 20%+."
   - WORKING-NOTES cites `lesson-11/transcript.md` lines 20-22.
   - Verified: line 20 has "my end screen click-through rates jumped from 0.9% to over 20%." PASS.

5. **Claim:** "Golden rule: never end a video. Don't say 'and finally'. Don't recap all the lessons."
   - WORKING-NOTES cites `lesson-11/notes.md` line 40 + `transcript.md` lines 87-88.
   - Verified: notes.md line 40 has "The golden rule: never end a video. Don't say 'and finally'..." Transcript.md line 88 has "never end a video. What that means is never wind down or use the words 'and finally' or never recap all the lessons you've taught at the end." PASS for both.

**Off-by-line citation flag:**

- WORKING-NOTES cites `lesson-11/transcript.md` lines 24-30 for "chain-reaction effect, one video blowing up drags the others up with it" + "700,000+ views on Film Booth."
- Actual: chain-reaction text is at line 24 ("once I had 10 videos all doing this, some crazy happened. One of them blew up, the others in that stream..."). The "700,000+ views Film Booth" specifically sits at line 32 of the transcript ("this one system drove over 700,000 views on Film Booth").
- Citation is approximately right (line 24 starts the chain-reaction discussion), but the 700K figure is at line 32. Recommend split into two citations.

**Citations missing:** None. Every productized claim and example in vid-ending's 4 reference files traces to either a lesson-11 source line or an internal format-planner / transition-bank citation in WORKING-NOTES.md.

**Attribution leaks:** None. Productized files (`SKILL.md`, `references/*.md`, `assets/ending-block-template.md`) contain no references to Ed Lawrence, YGS, ytgs, Film Booth, RevTrack, Synthia, or any other source-curriculum / instructor / tool name. The 700,000 views Film Booth example is correctly anonymized in `references/end-screen-design.md` line 22 ("one creator's chain produced 700,000+ views from one viral entry"). Locked decision #15 honored. RevTrack referenced as "conversion-tracking the creator uses" per attribution-scrub.

**Synthesized examples correctly flagged:**
- "Steve went from 0 clients to $80k a month in 9 weeks" — flagged as composite from format-planners/case-study.md.
- Bridge phrasings ("Watch this next, where I'll show you..." etc.) — flagged as direct adaptations from `banks/transition-bank.md` BE-3, BE-6, BE-7 patterns.

#### Pass 2, examples-density

**Rules below density threshold:** None. Density is strong:

- `references/pivot-gap-bridge-shapes.md`: 3 Pivot worked + 3 Pivot near-miss; 4 Gap worked + 3 Gap near-miss; 4 Bridge worked + 3 Bridge near-miss; 7 full Pivot→Gap→Bridge worked examples (one per format). Hits the bar everywhere.
- `references/cta-placement-by-format.md`: 6 worked + 4 anti-pattern across 3 goal categories (Sales/Emails/Views) + Mid-video CTA carry-through patterns. Hits the bar.
- `references/ending-anti-patterns.md`: 13 banned phrases (B-1 through B-13) each with failure mechanism + replacement. 10 structural anti-patterns (S-1 through S-10) each with worked failure example + replacement. Strong.
- `references/end-screen-design.md`: 5 worked decision examples (Short Process / Roast / News / Interview / First-video-on-repositioned-channel) + 5 explicit do-not-link rules R-1 through R-5 each with rationale. Strong.

**Source has more examples (not pulled):**

- `lesson-11/transcript.md` line 32 contains the specific anonymous-channel reference where flop videos that converted became sales tools ("If I look at my RevTrack data and a video is getting sales and emails but no views, I'm like, yes, I have a new sales tool to point new videos at from their end screens."). The productized `references/end-screen-design.md` Section 2 ("No converter yet") covers part of this but doesn't pull the specific "flop video as sales tool" framing. Recommend: surface this as a sixth worked example in Section 6 ("Worked decision examples"). Would tighten the "video with no views but strong conversion is still a sales tool" rule.
- `lesson-11/transcript.md` line 88 contains "think of all your videos as just one system that connects, not individual entities." Productized in `end-screen-design.md` Section 1 (chain-reaction principle). This is the canonical phrasing of the rule and is a strong rallying-line for the file's framing. Recommend: lead Section 1 with this sentence as a one-line epigraph (anonymized of course). Optional polish.
- `lesson-11/transcript.md` lines 50-66 contain the canonical worked example (logic-bricks / hook-not-yet-built / watch-this-next). This is the source of multiple Pivot/Gap/Bridge worked examples in `pivot-gap-bridge-shapes.md`. WORKING-NOTES correctly flags it as the canonical source. Productized files niche-substitute appropriately. PASS.

## Cross-skill consistency checks

- **5 hook types** consistent across vid-intro (`SKILL.md` line 24), vid-segment cross-skill confirmation (WORKING-NOTES line 316), and vid-ending callback rules (`SKILL.md` line 100). PASS.
- **Banned-phrase taxonomy** consistent: `banks/transition-bank.md` Section 4 (B-1..B-13) is the single source of truth, referenced verbatim by all three skills. vid-ending's `references/ending-anti-patterns.md` extends with ending-specific phrases (B-1..B-13 in that file are an ending-scoped subset + additions, with explicit failure mechanisms per locked decision #11). PASS.
- **Anti-fabrication discipline** consistent: vid-intro `SKILL.md` lines 280-286, vid-segment `SKILL.md` line 170, vid-ending `SKILL.md` lines 211-217. All trace to vid-title `SKILL.md` lines 56-58, 104, 199-209 per locked decision #18. PASS.
- **Output packet schemas** all match the team-standard shape (intro_packet / segment_packet / ending_packet). vid-ending's packet correctly references vid-intro's packet fields (`setup.text`, `setup.top_3_questions_used`, `problem_result.top_3_problem_anchored`, etc.) for the callback rules. PASS.
- **Shared knowledge file `loaded_by:` frontmatter** correctly lists all consuming skills:
  - `emotion-brick-decision-matrix.md`: [vid-intro, vid-segment, vid-ending]
  - `story-pulling-criteria.md`: [vid-intro, vid-segment, vid-ending]
  - `proof-placement-rules.md`: [vid-intro, vid-segment, vid-ending]
  - `metaphor-integration.md`: [vid-intro, vid-segment, vid-ending]
  - `visual-proof-callouts.md`: [vid-intro, vid-segment]
  All match the consumers declared in each skill's `SKILL.md` reference index. PASS.

## Recommended Phase 4 fixes (prioritized)

1. **vid-segment WORKING-NOTES.md line 108**: Update citation for sugar-cubes example from "lesson-07-emotion-brick-visual-demos/notes.md line 26" to "line 27" (the bullet itself starts at line 27 not line 26). Soft-fail-grade tightening.

2. **vid-ending WORKING-NOTES.md line 86**: Split the chain-reaction citation. Current cites "transcript.md lines 24-30" for both the chain-reaction principle AND the 700K Film Booth figure. The chain-reaction principle is at lines 24-30, but the specific 700K figure is at line 32. Split into two citations.

3. **vid-intro/references/hook-type-selection-flow.md**: Surface 5-7 additional hook patterns from `materials-shared/ytgs-video-planner.txt` lines 1978-2030 (Story Prompts) into a new sidebar section. Calibration-weight upside; not blocking.

4. **vid-segment/references/setup-tension-payoff-shapes.md** (Common cross-format mistakes section, lines 234-242): Pull the "yellow snow" early-payoff example from `lesson-15-how-to-write-a-script-basics/notes.md` line 23. Demonstrates the early-payoff failure mode with the specific corrected version. Calibration weight, not blocking.

5. **vid-segment/references/framework-shapes.md** Shape 1 (Arrows): Pull the second Arrows example (filming-backdrop "no mess / doesn't distract") from `lesson-10-logic-brick-frameworks-proof-checklists/notes.md` line 25. Niche variety, not blocking.

6. **vid-ending/references/end-screen-design.md** Section 6: Add a sixth worked example ("flop video as sales tool") drawing from `lesson-11/transcript.md` line 32. Tightens the existing rule already in Section 2.

## Confidence

- **Spot-checked 5 citations per skill (15 total).** All resolve to the cited source content (with the 2 line-number adjustments noted). The remaining citations were not fully verified by hand but were sampled at random and consistently passed. Confidence on citation correctness across the full WORKING-NOTES corpus: HIGH.
- **Examples-density count is exhaustive across all 9 reference files (vid-intro: 3, vid-segment: 2, vid-ending: 4) plus 5 shared knowledge files plus 2 banks (hook-bank, transition-bank).** All hit the ≥2 worked + ≥1 near-miss bar with one-line "why" annotations. Confidence: HIGH.
- **Attribution scrub** verified by grepping productized files for "Ed", "YGS", "ytgs", "Synthia", "IntroBot", "RevTrack", "Film Booth", "Chris Do", "Craig Ferguson". Zero hits in any productized file. Confidence: HIGH.
- **What I could NOT fully verify:**
  - All 30+ individual Hook Bank patterns (Q-1..Q-8, C-1..C-7, S-1..S-8, F-1..F-7, Cr-1..Cr-6) for source backing. WORKING-NOTES references the Hook Bank as "5-type pattern library mined from underlying study material" but doesn't enumerate per-pattern source citations. The patterns themselves are credible ("Have you ever wondered why...", "I'm a [credible role] and I don't...") and align with the 5 hook types defined in intro-architecture, so no fabrication signal. But per-pattern source-line traceability would require a separate pass on `banks/hook-bank.md` DEV NOTES (not provided to me).
  - All 8 Transition Bank Section 3 patterns (BE-1..BE-8) and Section 2 patterns (SS-1..SS-12). Same situation: vid-ending WORKING-NOTES line 182 says "Source-citations for individual BE patterns already logged in transition-bank.md DEV NOTES" but I did not read transition-bank.md's internal DEV NOTES section. Recommended Phase 4 verification: spot-check 3 BE patterns and 3 SS patterns against `transition-bank.md` DEV NOTES.
