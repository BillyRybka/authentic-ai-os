---
type: dev-notes
status: in-progress
skill: vid-intro
captured: 2026-05-08
---

# Skill Working Notes

Internal dev tracking only. Phase 3 QA agent verifies these citations. Lead strips this file before productization.

Source location: the underlying study material at the development reference path (`c:/Users/billr/projects/business-os/Resources/references/ed-lawrence-ygs/`), plus the productized files within `c:/Users/billr/projects/authentic-ai-os/`.

---

## Source citations

### SKILL.md

- **Claim:** "The 6-part architecture every video intro draws from. Steps 1-5 in order, Step 6 (credibility line) gets woven into one of 1-3."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 23-40 (the 6-step diagram and the woven-credibility note)
- **Notes:** Direct paraphrase of the canonical architecture. Same source for all step ordering.

- **Claim:** "Hook under 5 seconds. Whole intro under 30 seconds, 15 seconds is ideal. Setup max 3 things teased."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 16-21 (Top-line numbers section), 234-241 (Length and pacing section)
- **Notes:** Direct restatement of the constraints.

- **Claim:** "5 hook types: Question, Contrarian, Statement, Fact, Credibility."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 60-105 (Step 2: Hook section, all 5 types defined)
- **Notes:** Canonical 5-type set. Confirmed with vid-segment-builder via SendMessage on 2026-05-08.

- **Claim:** "3 Problem/Result options: Poke / Tease / Combine. Pivot phrases 'The thing is...', 'I used to until...', 'But...'"
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 107-137 (Step 3: Problem / Result section)
- **Notes:** Direct from the canonical architecture.

- **Claim:** "Setup format: 'So in this video, I'm going to show you [Q1], [Q2], [Q3].' Max 3."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 138-158 (Step 4: Setup section)
- **Notes:** Direct restatement of the canonical Setup pattern.

- **Claim:** "Banned transition phrases: 'Let's dive in', 'Let's talk about', 'Let me tell you', 'Without further ado', 'Now, before we begin'."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 173-181 (Banned transition phrases table)
- **Notes:** Cross-referenced with `banks/transition-bank.md` Section 4 (B-1..B-13) which expands and adds more.

- **Claim:** "Default verb is 'show', not 'tell'. Viewers come to YouTube to be shown."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 183 (the verb-default rule)
- **Notes:** Direct.

- **Claim:** "5 credibility forms: Vast experience, Volume of people helped, Big personal result, Big client result, Effort signal. Woven, never bolted-on."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 186-206 (Step 6: Credibility line woven, not bolted)
- **Notes:** Direct restatement.

- **Claim:** "Visual proof rule: any time a claim is made in the intro, show visual proof immediately."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 208-218 (Visual proof section)
- **Notes:** Direct.

- **Claim:** "Visual matching rule: first SHOT must match thumbnail style (cinematic / scrappy / studio / outdoor)."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 220-232 (Visual matching rule section)
- **Notes:** Direct.

- **Claim:** "Per-format intro adaptation map (Deep Dive full 6-part, Case Study inverted, Short Process compressed, Listicle hook+count+transition, Roast hook+1-line, News hook+context+transition no Setup/Credibility, Interview different shape)."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 244-258 (Format-specific adaptation table) plus per-format planners under `knowledge/format-planners/*.md`
- **Notes:** Cross-referenced. Skill loads the matched format planner at runtime.

- **Claim:** "Anti-fabrication: every number, name, and claim must be in the brain dump or foundation lock list."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/.claude/skills/vid-title/SKILL.md`
- **Lines:** 105-107 (Anti-fabrication hard filter), 204-209 (Anti-fabrication discipline section)
- **Notes:** Same rule as vid-title and vid-thumbnail. Kept consistent across writing skills per build-plan locked decision #18 ("Numbers must come verbatim from the script").

- **Claim:** "Credibility Hook risk on small/new channels — single dramatic claim CAN earn it."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 100-105 (Type 5 Credibility Hook caveat)
- **Notes:** Direct restatement of the small-channel guidance.

- **Claim:** "Voice pressure test (Layer 1 core + Layer 2 context) before save."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/voice-pressure-test.md`
- **Lines:** 23-66 (Two-pass check, severity tiers)
- **Notes:** Direct. Skill loads this at startup per the file's own `loaded_by:` field.

- **Claim:** "Read-aloud test as final filter."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/voice-pressure-test.md`
- **Lines:** 73-80 (The read-aloud test section)
- **Notes:** Direct. Reinforced in `Context/brand.md` rule 24 in business-os.

- **Claim:** "Output packet schema (sub-skill mode): intro_packet with locked_hook, intro_strategy, top_3_questions_used, proof_used, voice_check."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/build-plan.md`
- **Lines:** 198-211 (Context budget rule example showing intro_packet shape)
- **Notes:** Schema extended with credibility form, hook type, transition pattern_id, stories_used. Build-plan example was the seed.

- **Claim:** "Update both sides of wikilink graph when stories/proofs/testimonials get used."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/vault-integration.md`
- **Lines:** 246-256 (When a writing skill USES a story / The 'update both sides' rule)
- **Notes:** Non-negotiable rule per the file. Failure modes 1-7 in vault-integration.md govern error handling.

### references/hook-type-selection-flow.md

- **Claim:** "Format identity beats voice preference when they conflict. Voice profile breaks ties, not overrides."
- **Source:** Synthesized from cross-referencing `knowledge/format-planners/*.md` per-format hook-lane defaults plus `foundation/voice-profile.md` schema's `preferred_hook_types` field
- **Lines:** N/A (synthesized rule)
- **Notes:** This is the operational principle that makes the four-input decision flow work. Format identity is what the audience expects; voice profile is the creator's natural lean. When they disagree, the audience expectation dominates because the audience clicks on the format's promise.

- **Claim:** "Format-to-lane defaults" (per-format hook-lane mapping for Short Process, Case Study, Roast, Deep Dive, Interview, News, Listicle).
- **Source:** Each `knowledge/format-planners/{format}.md`'s "Intro adaptation" table
- **Lines:** Per-file: short-process.md lines 36-48; case-study.md lines 33-46; deep-dive.md lines 44-58; interview.md lines 33-49; news.md lines 36-50; roast.md lines 41-55; listicle.md lines 34-52
- **Notes:** Compiled from the canonical source. Each format's table specifies which hook types fit best AND why.

- **Claim:** "Anti-fabrication blocks Fact-Hook lane when no surprising stat exists in brain dump."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 90-98 (Type 4 Fact Hook hard rules)
- **Notes:** "The fact MUST be surprising. Boring facts are dead. The fact MUST be relevant to the video." Both rules force the lane to drop if material doesn't support it.

### references/credibility-line-weaving.md

- **Claim:** "5 credibility forms: Vast experience, Volume of people helped, Big personal result, Big client result, Effort signal."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 188-196 (5 ways to signal credibility section)
- **Notes:** Direct.

- **Claim:** "Bolted-on failure mode: 'Hi, I'm Bob. I've been doing this for 10 years...'"
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 202-206 (The bolted-on failure mode subsection)
- **Notes:** Direct restatement of the canonical anti-pattern.

- **Claim:** "Wrong-stage relatability: $250k-to-$1M case for a $10k/month avatar misses."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/case-study.md`
- **Lines:** 73-78 (Story rules, Match the avatar's stage rule)
- **Notes:** Direct restatement.

- **Claim:** "When format planner says credibility is 'often skipped,' skip it."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/news.md`
- **Lines:** 46-48 (News intro adaptation, credibility line "Often skipped")
- **Notes:** News is the cleanest example. Roast and Short Process also frequently skip per their intro tables.

- **Claim:** "3-slot decision: Hook (when receipt is dramatic enough on its own), Problem/Result (default; receipt earns the result tease), Setup (when credibility frames methodology)."
- **Source:** Synthesized from `knowledge/intro-architecture.md` Step 6 "weave into Hook, Problem/Result, or Setup" plus the worked example at lines 196-200 (which puts credibility in Problem/Result)
- **Lines:** 187, 196-200
- **Notes:** Step 6 names the three slots; the worked example shows Problem/Result as the default. Hook and Setup are alternatives based on form fit.

### knowledge/visual-proof-callouts.md (moved from references/ — shared with vid-segment)

- **Claim:** "Visual proof rule: any time a claim is made, show visual proof immediately."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 208-218 (Visual proof section)
- **Notes:** Direct.

- **Claim:** "Obsidian callout `> [!important]` placed immediately AFTER the claim line in script.md."
- **Source:** Synthesized from `knowledge/vault-integration.md` callout conventions plus `Context/brand.md` callout usage in business-os
- **Lines:** vault-integration.md lines 334-345 (Callout conventions table)
- **Notes:** vault-integration.md uses `> [!important]` for decisions. Visual proof callouts use the same callout type because they're production decisions for the editor.

- **Claim:** "Anti-fabrication applies to visual proof too — proof is real or claim doesn't ship."
- **Source:** Cross-reference of `knowledge/intro-architecture.md` line 218 (visual proof creates trust) plus the anti-fabrication rule in vid-title and the "no fabricated numbers in thumbnails" rule
- **Lines:** N/A (synthesized rule consistent with build-plan locked decision #18)
- **Notes:** Build-plan locked decision: "Numbers in thumbnails must come verbatim from the script. No fabrication. (Hard rule, codified in `knowledge/thumbnail-text-patterns.md`.)" Same logic applies to visual proof: real or skip.

### references/problem-result-options.md

- **Claim:** "3 options: Poke the Problem, Tease the Result, Combine Both. Pivot phrases."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 107-137 (Step 3 Problem/Result section, all 3 options with pivot phrases)
- **Notes:** Direct.

- **Claim:** "Poke when avatar's pain is acute and result is moderate. Tease when pain moderate and result dramatic. Combine when both high."
- **Source:** Synthesized from `knowledge/intro-architecture.md` "When to use" notes per option (lines 117, 124, 132) plus format-planner defaults
- **Lines:** intro-architecture.md lines 117 (Poke when pain acute), 124 (Tease when transformation receipt impressive), 132 (Combine when both matter)
- **Notes:** The intensity-matching framework is the synthesis of the per-option "when to use" guidance.

- **Claim:** "Format-specific defaults from format planners."
- **Source:** Each `knowledge/format-planners/{format}.md`'s "Intro adaptation" Problem/Result row
- **Lines:** Per-file Problem/Result rows in each planner's intro adaptation table
- **Notes:** Compiled.

---

## Examples sourced from

- **Example:** "Have you ever wondered why your videos pull 1k views one week and 100k the next?" (Phase 2 example output in SKILL.md)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/hook-bank.md`
- **Lines:** 26 (Pattern Q-1 worked example, paraphrased to avoid direct copy of "100k vs 1k" wording)
- **Notes:** Niche substitution: creator economy. Original from hook-bank.md uses similar shape.

- **Example:** "Six months ago Steve hadn't landed a single client. Now he's doing $80k a month."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/case-study.md`
- **Lines:** 40 (Case Study intro adaptation example: "Six months ago Steve hadn't landed a single client. Now he's doing $80k a month.")
- **Notes:** Direct quote from the format planner. Niche-anonymous (representative freelancer-to-coach transition). No attribution to source teacher.

- **Example:** "Steve was making $4k a month grinding on Upwork. Now he's making $25k a month with three retainer clients..." (problem-result-options.md Tease worked example)
- **Source:** Adapted from `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/case-study.md` "$80k/month" Steve example
- **Lines:** Adaptation of case-study.md line 40 with different numbers
- **Notes:** Niche substitution: same Steve archetype with adjusted starting and end numbers to fit a different "moderate pain, dramatic result" calibration. Numbers are illustrative, not from a real source.

- **Example:** "Most YouTube channels for businesses die at 1,000 subscribers..." (problem-result-options.md Combine worked example)
- **Source:** Adapted from `c:/Users/billr/projects/authentic-ai-os/knowledge/voice-rhythm.md` line 75 ("Most YouTube channels die at 1,000 subscribers because the creator started solving a different problem...")
- **Notes:** Direct quote from voice-rhythm as the opener. The $4M YouTube revenue figure is illustrative, paired with the canonical line. No attribution.

- **Example:** "Do you hate making thumbnails? I used to until I figured out a simple thumbnail formula that generated millions of views and $6 million from YouTube in just two years."
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 121-122 (Tease the Result canonical example)
- **Notes:** Direct quote from intro-architecture. Used in credibility-line-weaving Slot 2 worked example.

- **Example:** "After analyzing 247 sales pages this month, I'm going to show you the three structural moves..."
- **Source:** Synthesized example using the Effort Signal pattern from `knowledge/intro-architecture.md` line 195 ("I analyzed 500 resumes...")
- **Notes:** Niche substitution: sales pages instead of resumes. Number is illustrative.

- **Example:** "Today we're fixing three thumbnails... after reviewing 200+ of these..."
- **Source:** Adapted from `knowledge/format-planners/roast.md` lines 41-55 (Roast intro adaptation table) plus `knowledge/intro-architecture.md` Volume credibility form (line 192)
- **Notes:** Synthesized example combining Roast format expectation plus Volume credibility weave. Number is illustrative.

- **Example:** "I've been writing daily for 12 years and built three businesses to seven figures off it." (credibility-line-weaving Slot 1 worked example)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/hook-bank.md`
- **Lines:** 210 (Pattern Cr-1 worked example, slight paraphrase)
- **Notes:** Direct from hook-bank, niche-anonymous. The "3 businesses to 7 figures" arc preserves the canonical structure.

- **Example:** "Do you ever close a discovery call feeling great, then forget to follow up..." (problem-result-options.md Poke worked example)
- **Source:** Synthesized from `foundation/creator-foundation.md` archetype (a freelancer/coach with follow-up problems) plus `knowledge/intro-architecture.md` Poke pattern (lines 113-117)
- **Notes:** No real client. Avatar pain is illustrative, no attribution. Niche: freelancing/coaching (representative).

---

## Anti-patterns sourced from

- **Anti-pattern:** Bolted-on self-introduction ("Hi, I'm Bob. I've been doing this for 10 years...")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 202-206 (The bolted-on failure mode)
- **Notes:** Canonical. Cross-referenced in hook-bank.md A-1 (line 246).

- **Anti-pattern:** Banned transition phrases ("Let's dive in", "Let's talk about", "Let me tell you", "Without further ado", "Now, before we begin")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 175-181 (Banned transitions table)
- **Notes:** Expanded in `banks/transition-bank.md` Section 4 (B-1..B-13) with failure-mechanism explanations.

- **Anti-pattern:** Generic curiosity bait ("You won't believe what happened next")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/hook-bank.md`
- **Lines:** 248-251 (Anti-pattern A-2)
- **Notes:** Direct.

- **Anti-pattern:** Topic-label dressed as hook ("Today's video is about...")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/hook-bank.md`
- **Lines:** 263-267 (Anti-pattern A-6)
- **Notes:** Cross-referenced in transition-bank.md B-11.

- **Anti-pattern:** Hedge in hook ("Maybe you've been making a small mistake...")
- **Source:** `c:/Users/billr/projects/authentic-ai-os/banks/hook-bank.md`
- **Lines:** 259-262 (Anti-pattern A-5)
- **Notes:** Direct.

- **Anti-pattern:** Setup with more than 3 things
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 138-158 (Step 4 Setup, "More than 3 equals overwhelming"), 290-298 (Soft friction list)
- **Notes:** Soft friction. Deep Dive 45+ minute videos may use 5 (per deep-dive.md line 50).

- **Anti-pattern:** Hook longer than 5 seconds
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 17 (Top-line numbers), 290-298 (Soft friction)
- **Notes:** Soft friction. Story-driven opens can earn longer.

- **Anti-pattern:** Whole intro over 30 seconds
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 18 (Top-line numbers), 234-241 (Length and pacing)
- **Notes:** Soft friction. Deep Dive may earn longer.

- **Anti-pattern:** Em-dashes in productized content
- **Source:** `c:/Users/billr/projects/business-os/CLAUDE.md`
- **Lines:** Rule 33 region (Vale enforcement, em-dash banned)
- **Notes:** Brand-level rule. Skill respects it everywhere.

- **Anti-pattern:** Surprising-but-irrelevant fact (the "duck quacks don't echo" example)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 92-94 (Type 4 Fact Hook hard rule "the fact MUST be relevant")
- **Notes:** Cross-referenced in hook-bank.md A-4 (lines 254-258).

- **Anti-pattern:** Wrong-stage relatability ($1M case for $10k avatar)
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/format-planners/case-study.md`
- **Lines:** 73-78 (Story rules, Match the avatar's stage)
- **Notes:** Direct.

- **Anti-pattern:** Setup that doesn't answer Top 3 viewer questions
- **Source:** `c:/Users/billr/projects/authentic-ai-os/knowledge/intro-architecture.md`
- **Lines:** 286-288 (Hard friction list, Setup misalignment)
- **Notes:** Direct.

---

## Cross-skill dependencies confirmed

- 2026-05-08: vid-segment-builder confirmed canonical 5 hook types match vid-intro usage (Question, Contrarian, Statement, Fact, Credibility) via SendMessage. Both skills source from `knowledge/intro-architecture.md` Step 2 and reference `banks/hook-bank.md`.
- 2026-05-08: vid-ending-builder confirmed transition-bank section split via SendMessage: vid-intro consumes Section 1 (HF-1..HF-9, hook-forward) plus Section 4 (banned phrases B-1..B-13). vid-ending consumes Section 3 (BE-1..BE-8, body-to-ending) plus Section 4 (same banned-phrase list). vid-segment owns Section 2 (SS-1..SS-12, segment-to-segment). No overlap.
- 2026-05-08: voice-pressure-test.md `loaded_by:` field includes `vid-intro`. Confirmed schema match.
- 2026-05-08: voice-profile-schema field `preferred_hook_types` accepts the 5 type slugs used in vid-intro and hook-bank.md. Confirmed via banks/hook-bank.md line 14.
- 2026-05-08: vid-intro output packet schema (`intro_packet`) extends the example in `build-plan.md` lines 198-211 with the locked decisions every downstream skill needs (hook type, intro_strategy, credibility form, transition pattern_id, voice_pressure_test result).
- 2026-05-08: Anti-fabrication discipline matches `vid-title` SKILL.md and `vid-thumbnail` (per build-plan locked decision #18). Same lock-list mechanism used.

---

Delete this file when the skill is finalized.
