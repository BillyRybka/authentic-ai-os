---
type: dev-notes
status: in-progress
skill: vid-segment
captured: 2026-05-08
---

# Skill Working Notes (vid-segment)

Internal source-citation tracking. Lead deletes this file before productization. Phase 3 QA agent verifies citations from productized claims back to underlying sources.

---

## Source citations

### SKILL.md

- **Claim:** Two-pass review (structure first, prose second)
- **Source:** Build-plan locked decision #14 ("No expand-to-tier-2 skill: vid-segment handles two-pass review (structure → prose) internally")
- **Lines:** build-plan.md:407
- **Notes:** This is the architectural decision driving the entire skill design.

- **Claim:** Setup / Tension / Payoff is the universal segment arc
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-15-how-to-write-a-script-basics/notes.md`
- **Lines:** 21-26 (Setups & Payoffs Tension Graph framework)
- **Notes:** Direct adaptation. "Tension graph" framing maps to STP. Source uses "setup/payoff," productized as "Setup / Tension / Payoff" because the tension block is where emotion bricks live (per lesson-06).

- **Claim:** Emotion brick + Logic brick = full segment
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-06-how-to-make-a-point/notes.md`
- **Lines:** 21-22 (Emotion-Logic Brick System)
- **Notes:** Direct adaptation. Source frames every video point as Emotion → Logic. Productized as the Tension block of STP.

- **Claim:** Format-aware segments load `knowledge/format-planners/{format}.md`
- **Source:** `c:/Users/billr/projects/authentic-ai-os/build-plan.md`
- **Lines:** 364-376 (Format-aware writing section)
- **Notes:** Locked architectural decision #7. Output is format-aware.

- **Claim:** "Update both sides" rule for bank `used_in:`
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/vault-integration.md`
- **Lines:** 246-256 (Wikilink patterns when a writing skill USES a story)
- **Notes:** Direct adaptation of the canonical contract.

- **Claim:** Anti-fabrication discipline (no invented numbers / names / claims)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/.claude/skills/vid-title/SKILL.md`
- **Lines:** 102-107 (Hard filters), 199-209 (Anti-fabrication discipline)
- **Notes:** Pattern reused from vid-title. Same rule applies to vid-segment: every number/name traces to brain-dump, reference-block, foundation, or bank entry.

- **Claim:** Voice pressure-test runs before save
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/voice-pressure-test.md`
- **Lines:** 18-25 (When to run)
- **Notes:** Direct integration. vid-segment is one of the writing skills explicitly listed in voice-pressure-test.md frontmatter `loaded_by:`.

- **Claim:** Read-aloud test is the final voice gate
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/vault-integration.md`
- **Lines:** 463-470 (The read-aloud test)
- **Notes:** Cross-skill canonical rule. Already enforced in vid-title and vid-capture.

- **Claim:** Banks first, fabrication never (route to vid-capture if banks empty)
- **Source:** Build-plan.md locked decision #6 + `c:/Users/billr/projects/authentic-ai-os/.claude/skills/vid-capture/SKILL.md` lines 17-21 (Sub-skill invocation mode)
- **Lines:** build-plan.md:399-400, vid-capture/SKILL.md:17-21
- **Notes:** vid-capture's sub-skill mode was explicitly designed for this case (a writing skill mid-script needs material the banks don't have).

### references/setup-tension-payoff-shapes.md

- **Claim:** Deep dive uses heavy STP per segment
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/deep-dive.md`
- **Lines:** 25-31 (The structure section, "Proof woven throughout")
- **Notes:** Direct adaptation of the format planner's segment shape.

- **Claim:** Short Process default = lean Logic-only with optional mini-emotion brick
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/short-process.md`
- **Lines:** 27-34 (The structure, "Optional second emotion brick before a hard step")
- **Notes:** Direct adaptation.

- **Claim:** Listicle = full STP per point with varied brick types
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/listicle.md`
- **Lines:** 25-32, 65-77 (per-point structure + emotion brick decision matrix per point)
- **Notes:** Direct adaptation.

- **Claim:** Case Study = one big STP across the body (one segment)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/case-study.md`
- **Lines:** 25-32 (The structure section)
- **Notes:** Direct adaptation. Case study body is one segment, not multi-segment.

- **Claim:** News = compressed STP (what happened / why it matters / what to do)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/news.md`
- **Lines:** 25-33 (The structure section)
- **Notes:** Direct adaptation.

- **Claim:** Roast = per-review STP (show what they have / show what's wrong / show the fix)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/roast.md`
- **Lines:** 25-43 (Structure + per-review breakdown)
- **Notes:** Direct adaptation.

- **Claim:** Interview = per-question STP (host setup / guest story / guest insight)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/interview.md`
- **Lines:** 25-32 (The structure section), 60-73 (Question planning)
- **Notes:** Adapted. Source frames interview structure as Intro → Questions → End; vid-segment treats each question as a segment.

### knowledge/emotion-brick-decision-matrix.md (promoted from references/ on 2026-05-08)

- **Claim:** 5-question decision matrix (Visual Demo Show-the-Problem / Contrast / Breakdown / Story / Metaphor)
- **Source:** `Resources/references/ed-lawrence-ygs/materials-shared/ytgs-video-planner.txt`
- **Lines:** 1922-1949 (Emotion Brick Decision Matrix)
- **Notes:** Direct adaptation. Question wording paraphrased into productized form. The 5 brick types match the source 1-to-1.

- **Claim:** 16 sugar cubes / Coke can example
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-07-emotion-brick-visual-demos/notes.md`
- **Lines:** 27 (Show the Problem example)
- **Notes:** Direct example, niche substituted from source's weight-loss niche to "food / health niche" for productization. Sugar cube count and Coke can specific kept verbatim.

- **Claim:** Sales-page Contrast Demo example (Final Cut Pro grading)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-07-emotion-brick-visual-demos/notes.md`
- **Lines:** 28 (Contrast Demo example)
- **Notes:** Direct example. "Final Cut Pro Color Grading Masterclass" preserved as a real product reference because it's a generic course product, not a creator name. Headline change ("Stick out faster on social media with HBO quality video") preserved verbatim.

- **Claim:** Airbnb listing Breakdown Demo example
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-07-emotion-brick-visual-demos/notes.md`
- **Lines:** 29 (Breakdown Demo, Airbnb example)
- **Notes:** Direct example. Specifics about main photo / title / bullets preserved.

- **Claim:** Stories activate more memory pathways than facts
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-08-emotion-brick-storytelling/notes.md`
- **Lines:** 40 (Key Insights, "22x more memory pathways")
- **Notes:** Source claims "22x"; productized as "more memory pathways" without the specific multiplier (multiplier wasn't independently verifiable).

- **Claim:** Pricing story P-A-O example ($49 / 3 months / $900 / minimum wage prison)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-08-emotion-brick-storytelling/notes.md`
- **Lines:** 22 (Worked example, pricing a digital product)
- **Notes:** Direct example. All specific numbers preserved.

- **Claim:** Jelly bean channels visual metaphor
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-09-emotion-brick-metaphor/notes.md` (cross-referenced) and `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md`
- **Lines:** metaphor-builder.md:17-30
- **Notes:** Already-productized example pulled from knowledge file (which itself was sourced from the Ed Lawrence module).

### references/framework-shapes.md

- **Claim:** 5 visual shape framework types (arrows / pyramids / cycles / Venns / funnels) plus acronyms
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-10-logic-brick-frameworks-proof-checklists/notes.md`
- **Lines:** 23-34 (5 Visual Shape Framework Types)
- **Notes:** Direct adaptation. Source has 5; productized adds acronym as a 6th because BENS-style acronym frameworks are a separate shape that the source itself uses elsewhere (lesson 10 also discusses acronyms). 6th shape supported by source line 58.

- **Claim:** Framework Selection Matrix (the lookup table)
- **Source:** `Resources/references/ed-lawrence-ygs/materials-shared/ytgs-video-planner.txt`
- **Lines:** 2122-2131 (FRAMEWORKS DECISION MATRIX)
- **Notes:** Direct adaptation, productized as a markdown table.

- **Claim:** NEI triangle (New / Easy / Inspiring)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-10-logic-brick-frameworks-proof-checklists/notes.md`
- **Lines:** 27 (Triangles/Pyramids example)
- **Notes:** Direct example. NEI is from the source curriculum, used as an example of the triangle shape.

- **Claim:** Fail-As-Fast-As-You-Can cycle (MVP → Test → Measure → Adjust)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-10-logic-brick-frameworks-proof-checklists/notes.md`
- **Lines:** 29 (Cycles example)
- **Notes:** Direct example.

- **Claim:** Chris Do Venn diagram (Passion / Outcomes / Compensation)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-10-logic-brick-frameworks-proof-checklists/notes.md`
- **Lines:** 31 (Venn Diagrams example)
- **Notes:** Source attributes this to Chris Do; productized strips attribution per locked decision #15 (no named public-figure examples). The framework's substance preserved, name removed.

- **Claim:** AIDA-style funnel (Awareness → Consideration → Conversion → Loyalty)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-10-logic-brick-frameworks-proof-checklists/notes.md`
- **Lines:** 33 (Funnels example)
- **Notes:** Direct adaptation. Marketing-funnel framework is generic, not creator-attributed.

### knowledge/story-pulling-criteria.md (promoted from references/ on 2026-05-08)

- **Claim:** Stage match. Protagonist's before-state must match avatar's current stage.
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/case-study.md`
- **Lines:** 73 ("Match the avatar's stage" rule under Story rules)
- **Notes:** Direct adaptation. Source frames it as a case-study rule; productized as a general story-pulling criterion.

- **Claim:** Specific outcomes (numbers, timelines) required for story to land
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/story-capture-guide.md`
- **Lines:** 89-93 (Outcome section)
- **Notes:** Direct adaptation.

- **Claim:** 3 story types ranked by sales power (client > own > viewer)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-08-emotion-brick-storytelling/notes.md`
- **Lines:** 27-33 (3 Story Types ranked by sales power)
- **Notes:** Direct adaptation. Star ratings (3/3, 2/3) dropped in productization.

### knowledge/proof-placement-rules.md (promoted from references/ on 2026-05-08)

- **Claim:** Proof goes RIGHT AFTER framework, not before
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/proof-capture-guide.md`
- **Lines:** 81-92 (Where proof lands in a script)
- **Notes:** Direct adaptation. The "screenshot-immediately rule" lives upstream; this file enforces the placement rule downstream.

- **Claim:** Wall-of-wins technique (multiple proof screenshots scrolled at speed)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-10-logic-brick-frameworks-proof-checklists/notes.md`
- **Lines:** 44 (Proof bank example, Google Drive folder of 100s of screenshots)
- **Notes:** Direct adaptation. Source describes Ed scrolling through hundreds of testimonials; productized as the "wall-of-wins" technique.

- **Claim:** Verbatim testimonial preservation (no paraphrasing, no polishing)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/testimonial-bank/README.md`
- **Lines:** 22 (capture rule)
- **Notes:** Cross-skill canonical rule.

- **Claim:** Anonymization rule (don't reveal names marked anonymized)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/proof-capture-guide.md`
- **Lines:** 95-103 (Anonymization and permission)
- **Notes:** Direct adaptation.

### knowledge/metaphor-integration.md (promoted from references/ on 2026-05-08)

- **Claim:** Don't announce the metaphor
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md`
- **Lines:** 134-145 (Common mistakes, over-explaining, dragging out)
- **Notes:** Adapted. Source warns against over-explaining; productized "don't announce" rule generalizes that warning to the splice itself.

- **Claim:** Three-sentence cap on metaphor length
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-09-emotion-brick-metaphor/notes.md` (cross-referenced) plus `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md` line 145 ("Dragging it out, metaphors should land fast")
- **Notes:** Direct adaptation. Three sentences is a productized number based on the source's "land fast" rule.

- **Claim:** Pivot phrases for bridge-back-to-logic
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md`
- **Lines:** 117-124 (Pivot phrases section)
- **Notes:** Direct adaptation. Three pivot phrases preserved verbatim.

- **Claim:** Two-layer rule for visual metaphors (spoken + shown)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md`
- **Lines:** 56-67 (Visual vs non-visual metaphors)
- **Notes:** Direct adaptation. The "two layers for visual metaphors" rule is preserved.

---

## Examples sourced from

- **Example:** "I had not slept for 48 hours" (specific-language story example)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-08-emotion-brick-storytelling/notes.md`
- **Lines:** 24 (Specific language rule)
- **Notes:** Direct quote, used as the canonical specificity example in story-pulling-criteria.md (referenced indirectly through `knowledge/story-capture-guide.md` which already productized this).

- **Example:** Steve case study ($42k → $74k MRR in 9 weeks, 2-week vacation)
- **Source:** Composite, niche-substituted into representative B2B-coaching avatar.
- **Lines:** N/A (synthesized for SKILL.md and references/setup-tension-payoff-shapes.md)
- **Notes:** Synthetic example following P-A-O structure with specific numbers, used to demonstrate worked structure in deep-dive shape, case-study shape, and story-pulling criteria. No real client identity.

- **Example:** Re-engagement Trigger framework
- **Source:** Synthesized for setup-tension-payoff-shapes.md as a worked example of a deep-dive segment with a creator-owned framework
- **Lines:** N/A
- **Notes:** Plausible-sounding framework not pulled from any real source. Used to illustrate the structure pattern.

- **Example:** Restaurant with no recipes metaphor
- **Source:** Original synthesis for metaphor-integration.md
- **Lines:** N/A
- **Notes:** Plausible everyday-category metaphor (food category from `knowledge/metaphor-builder.md`). Not directly attributed.

- **Example:** Bouncer-at-a-club metaphor (form fields)
- **Source:** Original synthesis for setup-tension-payoff-shapes.md (listicle Point 5)
- **Lines:** N/A
- **Notes:** Plausible everyday-category metaphor (entertainment / queues). Used to demonstrate metaphor brick variation across listicle points.

- **Example:** Niche channel jelly beans visual metaphor
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md`
- **Lines:** 17-30
- **Notes:** Already-productized example reused.

---

## Anti-patterns sourced from

- **Anti-pattern:** Topic-label setup ("Now we're going to talk about X")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/transition-bank.md`
- **Lines:** 195-205 (Banned phrases B-2 "Let's talk about", B-11 "Today's video is about")
- **Notes:** Cross-skill canonical anti-pattern. Surfaces in all writing skills.

- **Anti-pattern:** Pure-announcement transitions ("Now point 4")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/listicle.md`
- **Lines:** 80-88 (Transitions are the lifeline)
- **Notes:** Direct adaptation. Listicle planner explicitly warns about announcement transitions. Same rule applies to all multi-point segments.

- **Anti-pattern:** Mixed metaphor (garden + rocket ship)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/metaphor-builder.md`
- **Lines:** 137 (Common mistakes, Mixing metaphors)
- **Notes:** Direct adaptation, example phrasing preserved.

- **Anti-pattern:** Fabricated numbers (rounding 9 weeks to 8 to fit framework claim)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/.claude/skills/vid-title/SKILL.md`
- **Lines:** 102-107 (Hard filters), 199-209 (Anti-fabrication discipline)
- **Notes:** Cross-skill canonical rule. vid-segment enforces same rule for prose.

- **Anti-pattern:** Visual demos with too many elements (5 colors instead of 2)
- **Source:** `Resources/references/ed-lawrence-ygs/modules/phase-05-writing-planning-videos/lesson-07-emotion-brick-visual-demos/notes.md`
- **Lines:** 43 (Complexity kills visual demos)
- **Notes:** Direct adaptation.

- **Anti-pattern:** Story starting at journey's beginning instead of moment of struggle
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/story-capture-guide.md`
- **Lines:** 153 (Common mistakes, Starting at the beginning of the journey)
- **Notes:** Direct adaptation.

- **Anti-pattern:** Proof placed before the framework
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/proof-capture-guide.md`
- **Lines:** 91-92 (Where proof lands in a script, proof ahead of framework doesn't land)
- **Notes:** Direct adaptation.

- **Anti-pattern:** Listicle / multi-point video reusing same brick type at every point
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/listicle.md`
- **Lines:** 76-78 (Don't use the same emotion brick type across all points)
- **Notes:** Direct adaptation.

- **Anti-pattern:** Reading off banned phrases from `banks/transition-bank.md` Section 4
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/transition-bank.md`
- **Lines:** 192-247 (Section 4 banned phrases)
- **Notes:** Cross-skill canonical. vid-segment enforces same banned-phrase list at outbound transition generation.

---

## Cross-skill dependencies confirmed

- vid-intro confirmed canonical 5 hook types (Statement, Question, Contrarian, Fact, Credibility) match vid-segment usage. Pending response from vid-intro-builder on this thread (sent 2026-05-08).
- vid-ending confirmed `banks/transition-bank.md` Section 3 ownership (body-to-ending). vid-segment owns Section 2 (segment-to-segment). Both share Section 4 (banned phrases). Pending response from vid-ending-builder (sent 2026-05-08).
- `voice-profile-schema` Layer 2 context maps and `voice-rhythm.md` cadence guidance confirmed loaded by vid-segment per `loaded_by:` field in those files (already declared in their frontmatter).
- `knowledge/voice-pressure-test.md` `loaded_by:` includes vid-segment (already declared in its frontmatter).
- `vid-capture` sub-skill mode (returns wikilink to caller, skips routing loop) is the contract vid-segment uses when banks come up empty mid-segment. Confirmed by vid-capture/SKILL.md lines 17-21.
- `knowledge/vault-integration.md` "update both sides" wikilink rule + failure modes is the canonical contract vid-segment honors at Phase 4 save.

---

Delete this file when the skill is finalized.
