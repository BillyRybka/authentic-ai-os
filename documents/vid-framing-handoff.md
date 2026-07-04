# vid-framing optimization — session handoff (2026-06-29)

Detailed state so I can resume exactly. This is the `/vid-framing` skill-optimization
pass (ruthless audit + rewrite + eval), part of the same series that already rebuilt
`vid-intake`. Lessons doc: `documents/skill-writing-lessons.md`. Plan file:
`C:\Users\billr\.claude\plans\you-are-optimizing-one-radiant-lake.md`.

## Where we are RIGHT NOW (the live thread)

Billy just pasted Ed Lawrence's **framing doctrine** and said it gives us "more info
about framing." It significantly deepens the skill. I replied proposing a
framing/title boundary split and asked him to confirm before I fold it in. **AWAITING
his answer on the boundary.** Do not rewrite until he confirms the boundary.

### The doctrine Billy pasted (capture verbatim, it must inform the skill)
- **Core principle: "interesting is the frame, not the information."** You don't make
  an idea interesting with better info; you frame known info so it feels new. The
  reframe is the entire job. (Ed's example: deep-data YouTube course bombed; same ideas
  reframed as "YouTube is a 5-link chain" got 900K.)
- **BENS filter** (from Kyle Milligan): Big / Easy / New / Safe. Run any angle/title
  through it. You don't need all four; one strong letter works. New is the most
  powerful (frustrated viewer hunting the one fresh thing).
- **New / Easy / Inspiring triangle**: every chunk must feel fresh, make the viewer feel
  smart (not confused), and feel doable.
- **Subtext**: don't state the idea fully; frame so the viewer's brain fills the gap
  (the curiosity that makes them click). "The Silent Hack YouTubers Use" works because
  the hack is never named.
- **Specificity + urgency**: "$14,332" beats "money"; add stakes/timeframe.
- **Contrarian / cognitive-dissonance flip**: frame against what the viewer believes
  ("VIDEOS DON'T GROW CHANNELS"). Prompt: what does most of my audience do that's wrong?
- **How to make a known idea feel new** (the reframe toolkit): a fresh comparison/
  metaphor; a visual framework; your own story; a named system/rule ("The 15-Second
  Rule"). The info can be old; the frame is what's new.
- **Practical sequence**: (1) start from the viewer's existing belief/frustration, not
  your info; (2) find the angle that makes it feel new (comparison, contrarian flip,
  named system, specific number); (3) pressure-test against BENS + New/Easy/Inspiring;
  (4) write as subtext (tease result, withhold mechanism); (5) make the promise specific,
  add stakes; (6) check it matches credibility.

### The boundary problem I flagged (the decision Billy must make)
A lot of that toolkit ALREADY lives in `vid-title` (it opens with "name the sharpest
claim, the disagreeable true thing," then runs BENS + subtext + specificity on the
title). If I pour the full doctrine into vid-framing, the two skills overlap and fight.

**My proposed split (awaiting Billy's confirm):**
- **vid-framing owns the FRAME (the idea):** the reframe that makes known info feel new
  — comparison, contrarian flip, named system, the creator's story, visual framework.
  Light gut-check vs BENS / New-Easy-Inspiring. Output: the angle, one line, in the
  creator's voice.
- **vid-title owns the TITLE (the words):** takes the frame and writes the clickable
  line — subtext, specificity, stakes, exact wording, competitor-gap. BENS pressure-
  tests the *words*.
- Implication: later pull the "name the claim" opener OUT of vid-title (it's framing's
  job) so they stop overlapping. That's a separate vid-title pass, NOT this one.

### What this changes about the pending fix
Before the doctrine, the next edit was just "make `selected_angle` one line in the
creator's words (capture, not paraphrase), TODOs out of the field." That still holds,
BUT the doctrine upgrades it: the angle should be a **reframe that makes the idea feel
new** (using the toolkit), said in the creator's voice — not merely an accurate
restatement. This directly addresses the Tier B angle-quality gap (judge said angles
were "accurate restatements, not reframes"). Earlier in the convo Billy rejected
"almost-disagreeable" as the bar (that's vid-title's job); the doctrine reconciles it:
the *contrarian flip* is one framing tool among several, found at framing, sharpened
into a disagreeable TITLE by vid-title.

## NEXT ACTIONS (once Billy confirms the boundary)
1. Fold "interesting is the frame, not the information" + the reframe toolkit (comparison,
   contrarian flip, named system, story, visual framework) into vid-framing's angle step
   (flow step 3). Keep it GENERIC (no Ed/Kyle/source names — attribution rule). Add a
   light BENS/New-Easy-Inspiring gut-check. Start step 2 explicitly from the viewer's
   existing belief/frustration.
2. Make `selected_angle` = the reframe, one line, in the creator's voice. core_payoff
   stays its own field. TODOs go to open-questions, never in the angle field.
3. Add a short before/after anchor in the skill (accurate-restatement vs real reframe).
4. Cite the source in `WORKING-NOTES.md` (dev-only ledger, source root
   `C:/Users/billr/projects/business-os/resources/references/ed-lawrence-ygs/`).
5. Update the eval's **angle_quality** rubric dimension to reward a genuine reframe
   (not just accuracy). The rubric is owned by the isolated eval-agent; re-delegate the
   rubric tweak to keep four-way separation, OR adjust the criteria and have the eval-
   agent revise. Do NOT hand-tune the rubric to pass my own outputs.
6. Re-run the loop: test-runner (regenerate the 6 outputs with the updated skill) ->
   eval.py (Tier A) -> judge (Tier B). Compare angle_quality + voice against the
   baseline (3.83 / 3.83).
7. Sync the change into the business-os temp copy OR just note it's superseded (see
   housekeeping). Then delete the temp copy when Billy says.

## WORK ALREADY DONE THIS SESSION (all uncommitted)

### The rewrite (psychology-first), in authentic-ai-os `.claude/skills/vid-framing/`
- `SKILL.md`: rewritten 226 -> ~67 lines. New flow: (1) read brain-dump; (2) get into
  the viewer's head (main problem, tension, transformation), name core_payoff, lay it
  back, WAIT for a yes; (3) only after the yes, bring in pattern-bank to shape + ground
  the angle (anti-fabrication); (4) frame it (creator picks angle, confirm format,
  pick goal); (5) save piece.md + hand to vid-title. Lazy loads (4, at point of use) not
  ~10 eager. Output 5 fields not 9. Rules section includes the brand-word guardrail
  added this session (no em-dashes AND no banned words: leverage, optimize, unlock,
  unleash, use, supercharge, empower, methodology, streamline).
- `assets/piece-framing-additions.md`: slimmed to new field set (selected_angle,
  core_payoff, format, goal, voice_context default, last_updated) + body section
  "## Considered + Dropped Angles". Pointer fixed to knowledge/vault-integration.md
  (was the dead gitignored build-plan.md). Append check fixed to `type: content-piece`.
- `references/angle-anchor-rules.md`: shrunk 169 -> ~41 lines to "real grounding vs
  hand-waving" + anti-fabrication + fluke note.
- `references/framing-conversation-examples.md`: rewritten 254 -> ~57 lines to intent
  register (no verbatim AI scripts) + the near-misses.
- `references/audience-temperature-fit.md`: DELETED.
- `WORKING-NOTES.md`: added a 2026-06-28 revision-log entry documenting the rewrite +
  cuts. (Still has the pre-existing "Conversion Optimization System" source citation at
  line ~90 — "optimization" is a banned word but it's a proper-noun citation in a
  dev-only file the real eval never scans. Left as-is intentionally.)

### Fields CUT from framing output (and why): `viewer_stage` (whole temperature
apparatus; only real reader was vid-pressure-test, which can derive temp from the
finished script), `outlier_anchor` + `anchor_confidence` (write-only, nothing reads
them; the "vid-title needs the null fallback" story was fiction — vid-title ignores the
anchor). Anchor still cited in-conversation for anti-fabrication, just not stored.

### Contract reconciliation (done)
- `knowledge/vault-integration.md`: framing-adds line now `selected_angle, core_payoff`
  (dropped the anchors). `goal` enum already `emails` (plural) there — the rewrite
  writes `emails` to match (old skill wrote singular `email`, which silently missed
  vid-ending's `goal=emails` branch).
- `.claude/skills/vid-structure/SKILL.md`: 3 prose edits dropping `viewer_stage` +
  `outlier_anchor` from its prereq/load/related lists (it only hard-gates on
  selected_angle+format, so no logic break). NOTE: vid-structure still has its own
  `iceberg_aligned: true` prereq bug — logged out of scope.
- check_handoff.py framing->structure (selected_angle, core_payoff, format, goal,
  voice_context) needs NO change; the rewrite still writes all five.

### Out of scope, logged for later: vid-pressure-test re-deriving temperature now that
viewer_stage is gone; vid-pressure-test uses singular `email` (should be `emails`);
vid-structure's `iceberg_aligned: true` prereq; foundation's own avatar/iceberg layout
(Billy hinted it may need its own fix).

## THE EVAL SUITE (built this session, the full four-way loop)

Location `tests/skills/vid-framing/`: `eval.py` (Tier A), `rubric.md` (Tier B),
`test_cases.json`, `creator-simulator.md`, `outputs/case_00..05/`, `judge-scores.json`.
Fixtures: `tests/fixtures/stages/after-intake/{slug}/` (brain-dump.md + ideating
piece.md for the 6 corpus seeds, hand-authored to CURRENT vid-intake schema because the
committed intake outputs are stale). `tests/fixtures/MANIFEST.md` updated (after-intake
row = hand-authored 2026-06-29).

Corpus = `tests/corpus/seeds.json`, 6 Sam Rivera seeds (synthetic), 2 adversarial:
case_00 systems-beat-hustle, 01 fired-himself-delegation, 02 new-scheduling-feature-
reaction, 03 5-onboarding-mistakes, 04 thin-pricing-dump (adv), 05 tempting-numbers-
client-story (adv).

How the loop ran (four-way isolation): I prepped fixtures; the **autoresearch-eval-agent**
wrote the grader blind; the **autoresearch-test-runner** ran the skill blind; the
**autoresearch-judge** scored blind. Run eval.py with:
`cd /c/Users/billr/projects/authentic-ai-os/tests/skills/vid-framing && python eval.py`
(must cd in the same command; bash cwd resets between calls).

Agent IDs (resume via SendMessage if useful):
- test-runner: `accc913d0a489ef73`
- judge: `adee072689d9f8256`
- eval-agent: `a03e6c5128e22e626`
- fixture builder (general): `a9782a811824e5c00`

### Scores
- **Tier A: 1.0000 (6/6).** First pass was 5/6 (case_05 wrote "highest-leverage" in a
  dropped angle). I added the banned-word guardrail to SKILL.md Rules and re-ran case_05
  (via SendMessage to the test-runner) -> clean. no_fabrication 6/6 INCLUDING both
  adversarial seeds (the skill marked TODOs instead of inventing). handoff 6/6.
- **Tier B: 0.85.** psychology_depth 4.67, grounding_honesty 4.67 (the strong ones, the
  redesign's core bets landing), angle_quality 3.83, voice_read_aloud 3.83 (the weak
  ones — the live thread above is fixing these via the framing doctrine).

### The 6 produced selected_angles (the "before" for the reframe fix)
- 00: "Systems beat hustle..." (long, payoff repeated)
- 01: "Marcus ran a small agency... Delegation is not about trust, it is about
  documentation." (the last clause is a real reframe; the rest is explanation)
- 02: "Everyone is about to buy this new scheduling feature and still be slammed..."
- 03: "Five specific onboarding mistakes that keep you as the bottleneck..." (a list,
  NOT reframed — clearest example of the gap)
- 04 (adv): "Undercharging is not a pricing problem, it is a time and freedom problem...
  TODO: add a client story..." (TODO crammed in field; no number invented — good)
- 05 (adv): "A coaching business grew fast... The growth came from the boring system,
  not from a growth hack. TODO:..." (TODO in field; no revenue invented — good)
Target: each becomes a one-line reframe in the creator's voice; payoff in core_payoff;
TODO in open-questions.

## HOUSEKEEPING / GOTCHAS
- **Everything is uncommitted.** GitHub checkpoint = clean pre-rewrite state on
  `origin/dev` (dev had 0 unpushed commits, vid-framing was clean). Billy wants to
  review the diff before any commit. Do NOT commit/push unless asked. Stage only my
  paths (Billy runs parallel sessions; the tree had in-flight vid-intake/title/pipeline
  work at session start — never `reset --hard`, never sweep others' files).
- **business-os temp copy:** `C:\Users\billr\projects\business-os\Skills\vid-framing-TEMP\`
  (with `_TEMP-README.md`). It was for Billy's mobile review. It is now STALE (predates
  the banned-word fix and the coming reframe edit). Do NOT push business-os. Delete the
  temp copy when Billy confirms he's done with it (per the plan).
- **Attribution rule:** productized skill files must NEVER name Ed Lawrence / YGS / Kyle
  Milligan / the course. Source citations live only in `WORKING-NOTES.md` (dev-only).
- **Shared skills stay generic:** vid-framing ships for any creator. Reframe toolkit +
  BENS are generic (fine). Do not bake Billy-specific examples into the skill.
- **Em-dashes: never.** Banned words list is in `tests/lib/vale_rules.py` (leverage,
  optimize, unlock, unleash, use, supercharge, empower, methodology, streamline +
  inflections).
- **Billy's working style:** sharp, no hedging; he steers hard and corrects often; he
  flagged me "doing too much" / over-engineering twice. Recommend, then act on his go.
  One-part-at-a-time. He rejected the multi-question AskUserQuestion in favor of talking
  it through. Reads on mobile sometimes (hence the business-os copy workflow).
- Ultracode is OFF (don't auto-spawn Workflows; use the Agent tool for isolated roles).

## THE PLAN FILE
Full approved plan (psychology-first rewrite, cuts, sequence, verification) is at
`C:\Users\billr\.claude\plans\you-are-optimizing-one-radiant-lake.md`. It predates the
framing-doctrine thread, so the angle step there is now being upgraded per the doctrine.
