# Ed Audit / Flexibility — 2026-05-08

Auditor: ed-audit-specialist (Phase 3b)
Scope: vid-intro, vid-segment, vid-ending (SKILL.md + skill-local references + shared knowledge files they load + relevant banks)
Method: every finding requires a productized rule citation AND a source quote. No vibes audit.

## Summary

- Skills audited: vid-intro, vid-segment, vid-ending
- Verdict: SOFT-PASS
- Findings recorded with evidence: 4
- Findings considered and dropped (no source evidence): 9
- Top 3 fixes for Phase 4: F-1 (auto-reject banned phrases not source-backed), F-2 (lesson-15 "early payoff is fine" caveat missing from segment), F-3 (lesson-06 "framework is a guide, not a law" never surfaced as principle)

The skills are mostly faithful to the source. The 2026-05-02 softening pass (build-plan line 844) did the heavy lifting — REJECT language was already converted to soft friction across format planners, intro-architecture, and vid-title, and that pattern carried into vid-intro/segment/ending. What remains is mostly auto-rejected lists that grew beyond what the source actually bans (transitions B-4 through B-13, ending banned phrases B-2 through B-13) and one or two missing source-flexibility caveats. None are HARD-FAIL. The system reads as faithful at first pass; the misses are at the edges.

The strongest evidence anchors found in the source for flexibility:
- Lesson-06 line 40: "Missing one emotion brick doesn't kill a video. Obsessing about it causes paralysis. The framework is a guide, not a law." + "Nobody dies if you tweak this a little."
- Lesson-10 line 57: "three is an example, not a rule" (framework-shapes.md already quotes this — faithful).
- Lesson-15 line 39: "Not every point needs to be creative. Half the time, Ed pays something off early and moves on because he can't think of a creative way to frame it."
- Lesson-16 line 47: "If you pay something off early and then you instantly set up something else, you've rehooked them. It's fine."
- Lesson-03 line 112: "Well, there's no set answer. You just try one, and if you can't come up with any, use the hook bank."
- ytgs-video-planner line 1874: "the smart move is just to have 3-4 [transitions] you use over and over again."

## Findings (each with evidence)

### Finding F-1: vid-intro auto-rejects banned transitions B-4 through B-13 without source evidence

- Productized rule: "Banned transition phrases. Anything in `transition-bank.md` Section 4 (B-1..B-13). REJECT and substitute." (`.claude/skills/vid-intro/SKILL.md` line 293, hard friction #2). Plus transition-bank.md Section 4 line 192-246 lists 13 phrases auto-rejected at candidate generation time, "creator never sees them as options" (line 259).
- Source teaching:
  - Lesson-03 line 196-200 (transcript): "I would also recommend never saying these in a transition. Okay, now let's dive in, because that's something AI says. 'Okay, let's talk about,' because no one came here to talk to you. And also don't say, 'Let me tell you,' because it sounds like you're going to tell them a list of boring information."
  - Three phrases: "let's dive in" (B-1), "let's talk about" (B-2), "let me tell you" (B-3). Source frames as "I would also recommend never" — recommendation, not law. Productized auto-rejects without creator visibility.
  - Lesson-11 line 40 backs B-6: "never end a video. Don't say 'and finally.'" — explicit ban. Faithful.
  - B-4 ("Without further ado"), B-5 ("Now, before we begin..."), B-7 ("But here's where it got interesting..."), B-9 ("Now let me tell you a quick story"), B-10 ("Stay tuned for"), B-12 ("Anyway, moving on") — none appear in lesson-03, lesson-11, or the ytgs-video-planner banks. transition-bank.md DEV NOTES at lines 318-330 admits B-7 is "captured user feedback", B-10 is "derivative; observed failure mode", B-12 is "derivative of source planner line 1870 ('Don't get cute with transitions')". The dev citations are honest about which lack source backing.
  - ytgs-video-planner line 1870-1874 says "Don't get cute with transitions, they shouldn't take more than 30 seconds to write" + "the smart move is just to have 3-4 you use over and over again." Source treats transitions as flexible default-set, not a 13-phrase blocklist.
- Diff: Source explicitly bans 3 transitions (B-1, B-2, B-3) and 1 ending phrase (B-6 "and finally" / "lastly"). Productized expanded to 13 entries auto-rejected at generation, creator never sees them. Source ban list: 4. Productized ban list: 13.
- Severity: SOFT
- Recommended fix: Split Section 4 into two tiers. Tier 1 (auto-reject, source-backed): B-1, B-2, B-3, B-6. Tier 2 (soft friction, flag-and-explain): B-4, B-5, B-7, B-8, B-9, B-10, B-11, B-12, B-13. Creator sees Tier 2 candidates with the failure-mechanism note attached, can override. Aligns with the 2026-05-02 build-plan principle: "Hard rules stay (anti-fabrication, ≤50 chars, invented compound nouns, read-aloud). Soft friction = flag and explain, creator decides."

### Finding F-2: vid-ending auto-reject list expanded well past source-bans

- Productized rule: vid-ending SKILL.md line 120 hard-filter #2: "Banned phrases. 'And finally' / 'Lastly' / 'Thanks for watching' / 'If you liked this, please subscribe' / 'Stay tuned' / 'Without further ado' / 'Today's video was about'. REJECT." Plus references/ending-anti-patterns.md line 19-99 lists B-1 through B-13 auto-rejected (line 21: "Every phrase below is auto-rejected at candidate generation. The creator never sees them as options"). Plus an "auto-reject regex" in the same file lines 215-228.
- Source teaching:
  - Lesson-11 line 40: "The golden rule: never end a video. Don't say 'and finally.' Don't recap. Just set up the next problem and point to the video that solves it." — explicit ban on "and finally" (B-1 in vid-ending) and on recap (S-1 structural).
  - Lesson-11 line 25 (Ed's own example): "No begging. No 'like and subscribe.' Just a well-positioned next step." — explicit ban on "if you liked this, please subscribe" (B-3 in vid-ending).
  - That is it. Lesson-11 transcript and notes contain NO ban on "Thanks for watching" (B-2), "Stay tuned" (B-4), "Without further ado" (B-5), "Today's video was about" (B-6), "I hope you enjoyed today's video" (B-7), "Let me know what you think in the comments" (B-8), "Don't forget to" (B-9), "Until next time" (B-10), "Hit the bell" (B-12), "Catch you in the next one" (B-13). They are all derivations from related principles (e.g. "no begging"), not source-explicit.
- Diff: Source explicitly bans 2 ending phrases ("and finally" / "lastly", "like and subscribe"). Productized auto-rejects 13 plus a regex. The creator never sees 11 of them as candidates.
- Severity: SOFT
- Recommended fix: Split ending-anti-patterns.md Section 1 the same way as F-1 — Tier 1 auto-reject (B-1 "and finally / lastly", B-3 "if you liked this, please subscribe / smash that like" — both source-explicit). Tier 2 soft friction (B-2, B-4 through B-13) — flag and explain, creator decides. Mirror Section 5's "auto-reject regex" change accordingly. Keep the failure-mechanism note attached in either tier.

### Finding F-3: Source's "early payoff is fine" caveat dropped from vid-segment STP shapes

- Productized rule:
  - vid-segment SKILL.md line 268 principle: "Structure dictates voice, not the other way around. Structure pass FIRST. If the segment doesn't work as a unit, no amount of voice polish saves it."
  - setup-tension-payoff-shapes.md line 239 cross-format mistake: "Tension without an emotion brick AND a logic brick. A segment needs both. Pure logic = research summary. Pure emotion = drama without lesson."
  - Lines 92-119 (Listicle Shape 3): every point gets emotion-then-logic. The shape's worked examples both pair an emotion brick with a logic brick.
  - Lines 22-48 (Deep Dive Shape 1): heavy STP per segment, proof woven, every step has its own emotion brick.
- Source teaching:
  - Lesson-15 line 39: "Not every point needs to be creative. Half the time, Ed pays something off early and moves on because he can't think of a creative way to frame it. Skip it, make the next point more interesting, and keep moving."
  - Lesson-16 line 47: "If you pay something off early and then you immediately set up something new, the viewer is rehooked. An early payoff followed by a new setup is not a problem."
  - Lesson-06 line 40: "Missing one emotion brick doesn't kill a video. Obsessing about it causes paralysis. The framework is a guide, not a law."
  - Lesson-15 line 49 (Listicle-specific): "For listicle-format videos: don't go deep on every point. Give people one thing they walk away with. The format doesn't support comprehensive depth on every item."
- Diff: Source explicitly says half of Ed's listicle/deep-dive points pay off early without a creative emotion brick, and that this is FINE. Productized listicle (Shape 3) and deep-dive (Shape 1) shape examples present per-point full STP with emotion brick + logic brick as the worked-example pattern. The cross-format-mistake line 239 hardens this into "a segment needs both," which contradicts lesson-15 line 39.
- Severity: SOFT
- Recommended fix: Add a section to setup-tension-payoff-shapes.md (or to emotion-brick-decision-matrix.md) titled "When a segment runs lean intentionally" that quotes the lesson-15 / lesson-16 caveats: lean Logic-only is fine when an early-payoff is followed by a new setup, when the format calls for "one thing per point" (listicle), or when the creator can't find a creative angle and shouldn't grind for one. Soften "a segment needs both" cross-format mistake (line 239) to "a segment usually needs both, except in lean steps and early-payoff-with-rehook moments." Source-backed flexibility, source citation explicit in the file.

### Finding F-4: emotion-brick-decision-matrix imposes priority order source doesn't teach

- Productized rule: knowledge/emotion-brick-decision-matrix.md line 25-26: "If multiple YES, default order: Visual Demo (any sub-type) > Story > Metaphor. Visual demos land fastest because the viewer's eye does the cognitive work."
- Source teaching:
  - Lesson-06 line 30 (Decision Matrix): "{Persuasive/insight-based video}: Use Emotion + Logic on every point." — source says Emotion + Logic; doesn't rank one emotion brick type over another.
  - Lesson-07, 08, 09 each present a brick type with its own when-to-use criteria. None is ranked above the others.
  - Lesson-09 line 41: "Ed's top-earning videos all used metaphors in the emotion brick." — Metaphor is described as Ed's strongest performer, NOT lowest priority.
  - Lesson-08 line 40: "Stories activate 22x more memory pathways than facts alone." — Story is also high-power.
  - The emotion-brick-decision-matrix file's own header (line 26) admits the rationale: "Visual demos land fastest because the viewer's eye does the cognitive work." That is a runtime efficiency claim, not a source-backed priority.
- Diff: Source teaches three brick types with separate when-to-use filters and no priority order. Productized imposes Visual Demo > Story > Metaphor as a tiebreaker. The matrix's "first YES wins" pattern already resolves most cases; the priority order only fires on ties, which makes the imposition relatively low-impact, but it's still a rule the source doesn't ground.
- Severity: SOFT
- Recommended fix: Replace line 25-26 with: "If multiple YES, surface the matched brick types to the creator and let them pick. The viewer's eye gets cognitive work fastest from Visual Demo, the heart from Story, and the long-term memory from Metaphor — different brick, different lever, all source-validated. Default to whichever the bank has the strongest material for, then to whichever the creator's voice profile leans." Aligns with the build-plan AI-first principle: "Generate multiple useful options when exploration helps. Use source-backed examples to expand creative range, not constrain it."

## Findings dropped (no source evidence)

These rigidity flags I considered and DROPPED for lack of source backing. Listed transparently so future audits can revisit if new source material surfaces.

- **vid-intro hard friction #5 ("Em-dashes in the intro. REJECT").** Source has no opinion on em-dashes — that's a Billy/brand layer rule, not source. Faithful at the brand layer. Not a source-flexibility issue.
- **vid-intro hard friction #6 ("Generic curiosity bait — 'You won't believe what happened next' — REJECT").** Source lesson-03 doesn't explicitly address this phrase or pattern. Productized rule may be defensible from broader source (lesson-08 line 32 "Avoid well-known stories... no surprise, no tension") but the connection is too loose to call a finding either way. Dropped.
- **vid-intro Setup max-3 hard rule.** Source lesson-03 line 156 explicit: "Set up the value to come (max 3 things)." Source agrees. The skill correctly leaves "more than 3" as soft friction (line 304). Faithful.
- **vid-intro hook ≤5 seconds rule.** Source lesson-03 line 70: "Aim for no more than 5 seconds." Productized correctly places "Hook longer than 5 seconds" at soft friction #9, not hard. Faithful.
- **vid-intro auto-reject Setup that doesn't answer Top 3.** Source lesson-03 line 158 makes Setup BY DEFINITION the Top 3 questions in the template. Auto-reject of mismatched Setups is faithful to source method.
- **vid-intro bolted-on self-introduction REJECT.** Source lesson-03 line 208: "not like a random line of a CV inserted." Productized rule is faithful.
- **vid-intro hook-type-selection-flow's 4-input cross-reference (format > voice > channel > material).** Source lesson-03 line 112: "Well, there's no set answer. You just try one." Source teaches freedom; productized adds structure. CONSIDERED as a finding. Dropped because: (a) the file's own line 99 says "It does not enforce voice preferences as laws. Voice profile is a fingerprint, not a rule"; (b) lines 84-92 list explicit override cases; (c) the AI-first workflow standard in build-plan.md lines 154-161 justifies operationalizing fuzzy creator judgment for AI agents. The structure is more deterministic than source but creator override is preserved. Borderline; flagged for future audits if creator complaints surface.
- **vid-segment "Do not write prose until structure locks" + "structure dictates voice."** Source lesson-15 line 49: "First draft: dump everything out with no editing, no perfection." Source's writing options 1-3 (line 26-32) include "Classic First Draft & Edit" and "PointBot Feedback Loop" — both iterative. Productized two-pass (structure → prose) is consistent with source workflow option 3 (PointBot per-point feedback). Not a rigidity finding.
- **vid-segment story-pulling Criterion 1 (stage match).** Source lesson-08 doesn't directly teach stage-match. Productized rule is derived from creator data (Billy directive on credibility-line-weaving stage match, lines 113-124 in the credibility-line-weaving.md file). Per build-plan principle traceability standard (build-plan line 113), creator data is a valid source for productized rules. Not a source-flexibility violation, even if not source-explicit.

## Confidence

What I searched and found:
- All transcripts and notes for lesson-03 (intros), lesson-05 (writing intros), lesson-06 (making points), lesson-07 (visual demos), lesson-08 (stories), lesson-09 (metaphors), lesson-10 (logic bricks), lesson-11 (endings), lesson-13 (sales/email/views optimization), lesson-15 (script writing), lesson-16 (set up and payoffs).
- ytgs-video-planner.txt — hook bank, transition bank, format banks.
- All productized SKILL.md, references/, and assets/ for vid-intro, vid-segment, vid-ending.
- All shared knowledge files loaded by the three skills: intro-architecture, voice-rhythm, voice-pressure-test, format-planners (referenced, not exhaustively read), visual-proof-callouts, emotion-brick-decision-matrix, story-pulling-criteria, proof-placement-rules, metaphor-integration.
- banks/hook-bank.md and banks/transition-bank.md (focused on banned-phrases section, dev citations).

What I did not exhaustively read:
- Each format-planner ({format}.md) was sampled for intro-adaptation rows quoted in upstream files. The full per-format planner audit is the flow-reviewer / source-fidelity-auditor scope.
- proof-placement-rules.md, metaphor-integration.md, visual-proof-callouts.md were read for cross-references and not audited line-by-line for rigidity. They were not the source of any finding here, so the audit doesn't depend on a deep read.

Areas where the source may not address flexibility either way:
- Intro hard friction #6 (generic curiosity bait specifically). Source bans "stay tuned" / future-promise patterns in ending context, never speaks to "you won't believe what happens next" in intro context. Could be argued either way.
- Productized banned-phrases derivations B-7 through B-13. The dev citations honestly admit derivation. Source itself stays silent. The finding F-1 / F-2 fix (split into tiers) is the right move regardless of how source eventually treats them.
- Emotion-brick-decision-matrix's "first YES wins" rule. Source lesson-06 line 30 distinguishes persuasive vs tutorial format but not a question-by-question matrix. Productized matrix is an operationalization. Source neither endorses nor rejects.
