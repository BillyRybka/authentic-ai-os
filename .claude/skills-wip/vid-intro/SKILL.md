---
name: vid-intro
description: Produce the full 6-part video intro (Top 3 viewer questions, Hook, Problem/Result, Setup, Transition, Credibility woven) for one video. Format-aware. Pulls from creator-foundation, voice-profile, reference-pieces, the video's brain dump, the locked title, the thumbnail brief, and the matching format planner. Anti-fabrication. Every claim must trace to script or foundation. Runnable standalone OR invoked by `vid-structure` / `vid-pipeline`. Make sure to use this skill whenever the creator needs the opening of a video written, even if they don't explicitly say "intro". Phrases like "write the intro", "intro for [video]", "lock the hook", "rewrite the intro", "fix the intro", "what should I open with", "how do I start this video", "I need a hook", "the opening feels off", "help me set up this video", or any downstream pipeline that needs the opening of a video should fire this skill.
---

# Video Intro Builder

Produces the full 6-part intro for one video. Five phases: load context, derive viewer questions and pick hook type, build Hook plus Problem/Result, build Setup plus Transition with credibility woven, save.

**Scope boundary:** this skill produces THE intro only (steps 1-5 of the 6-part architecture, with credibility woven into one of 1-3). It does not write body segments (`vid-segment`), endings (`vid-ending`), titles (`vid-title`), or thumbnails (`vid-thumbnail`). If the title or thumbnail aren't locked yet, hard stop and tell the creator to lock those first. The intro depends on them.

## What this produces

A full intro for one video, saved to `content/pieces/{slug}/script.md` under an `## Intro` section. When invoked as a sub-skill by `vid-structure` or `vid-pipeline`, returns the intro as a structured packet to the caller (see "Output packet" below) and skips the save.

## When to run this

- A video has a locked title and thumbnail and now needs the opening written
- Creator wants to rewrite the intro because the current one feels off
- Orchestrator (vid-pipeline) invokes during STRUCTURE phase or SCRIPT phase

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists (avatar, Top 3 problems, credibility brags)
- `foundation/voice-profile.md` exists (the guardrail) and `foundation/reference-pieces/` has at least the `youtube-script` context (the voice engine)
- `content/pieces/{slug}/piece.md` exists with `title:` locked AND `format:` set (and `voice_context:`, default `youtube-script`)
- `content/pieces/{slug}/thumbnail-brief.md` exists with the locked thumbnail picks
- A brain dump or reference block exists at `content/pieces/{slug}/brain-dump.md` or `piece.md` (the actual video material)

If foundation is missing, tell the creator to run `vid-foundation` first. If the title or thumbnail aren't locked, tell them to run `vid-title` and `vid-thumbnail` first. If the brain dump is empty, ask them to fill it in or paste the script material before continuing.

## Invocation modes

**Standalone:** creator invokes directly. After lock, save the intro to `content/pieces/{slug}/script.md` under `## Intro`, update piece.md `voice_pressure_test:`, end.

**Sub-skill:** another skill (vid-structure, vid-pipeline) invokes. Return the intro packet to the caller; skip the save. The caller writes it into the script as part of its own flow.

If invoked with context from a caller (e.g. "intro for piece={slug}, format=case-study, locked-title='X', thumbnail-text='Y'"), skip the load step's questions to creator and go straight to candidate generation.

## The walkthrough (5 phases)

**This skill is a conversation, not a document.** Keep messages short. Never paste reference content into chat. The references (intro-architecture, hook-bank, transition-bank, format planner, voice-profile, reference-pieces) are for YOUR thinking. Pull from them selectively. Same hard rules as `vid-title` and `vid-thumbnail`: no fabrication, specificity wins, every claim traces to the brain dump or foundation.

### Phase 1: Load context, derive viewer questions, pick hook type

**Silent loads** (do NOT paste into chat):

1. `knowledge/intro-architecture.md` (the 6-part architecture, the 5 hook types, the 3 problem/result options, banned transition phrases, the visual-matching rule, format-adaptation map)
2. `knowledge/format-planners/{format}.md` (matched to the piece's format: short-process | case-study | roast | deep-dive | interview | news | listicle). This dictates the intro shape for THIS video.
3. `knowledge/voice-rhythm.md` and `knowledge/voice-pressure-test.md` (the rhythm lens and the pre-save check)
4. `foundation/creator-foundation.md` (avatar, Top 3 problems, credibility brags)
5. `foundation/voice-profile.md` (the thin guardrail: fingerprint, signature phrases, refusals, POV/energy, and the optional `preferred_hook_types` / `transition_style_preferences` / `intro_pacing` orientation fields. Always loaded. Contract in `knowledge/voice-profile-schema.md`)
6. `foundation/reference-pieces/{voice_context}.md` (the voice engine: real intact passages to write the intro from, as `## ` sections in one file matched to piece.md `voice_context`, default `youtube-script`. If absent, seed from the guardrail fingerprint and note the gap). **Voice-only, not structure:** reference pieces carry cadence, word choice, register, and signature moves. The intro's architecture (hook arc, problem/result, setup, transition, credibility weave) is fixed by THIS skill's spec. If a reference passage's structural arc conflicts with the spec, follow the spec. Reproduce the grain, not the order of moves.
7. `banks/hook-bank.md` (5-type pattern library with worked plus near-miss examples)
8. `banks/transition-bank.md` Section 1 (hook-forward transitions HF-1..HF-9) plus Section 4 (banned phrases B-1..B-13)
9. `knowledge/emotion-brick-decision-matrix.md` (shared with vid-segment, vid-ending). Energy taxonomy (Visual Demo / Story / Metaphor). Useful for picking which energy lane the Hook + Problem/Result anchors in: question 4 maps to Poke-the-Problem (Story brick), question 5 maps to abstract reframes (Metaphor in hook), question 1 maps to Visual Demo when the avatar's pain is invisible. Body-segment scoped in name, but the underlying lane logic informs intro emotional weight too.
10. `content/pieces/{slug}/piece.md` (format, goal, pillar, locked title)
11. `content/pieces/{slug}/thumbnail-brief.md` (the locked thumbnail picks plus rationale)
12. `content/pieces/{slug}/brain-dump.md` AND/OR `piece.md` AND/OR `script.md` body (the actual material the intro must align to)
13. Conditional: `banks/story-bank/*.md` only if a credibility-line candidate would weave a story (Big-client-result, Volume-of-people-helped). When loading, also load `knowledge/story-pulling-criteria.md` (shared with vid-segment, vid-ending). 5 criteria for picking the right story from N candidates. Stage-match is the highest-priority filter for vid-intro because intro stories need to match the avatar's CURRENT stage, not their aspirational stage.
14. Conditional: `banks/proof-bank/*.md` and `banks/testimonial-bank/*.md` only if the credibility line cites a number, screenshot, or testimonial. When loading, also load `knowledge/proof-placement-rules.md` (shared with vid-segment, vid-ending) for the PLACEMENT decision (proof immediately AFTER claim, not before; presentation-format selection across static-screenshot / before-after-pairing / live-clip / inline-stat). The CALLOUT SYNTAX itself lives in `knowledge/visual-proof-callouts.md` (already pointed at from Phase 4). Two files, two roles: placement-rules answers "where does proof go", visual-proof-callouts answers "how does the script mark it for the editor."
15. Conditional: `knowledge/metaphor-integration.md` (shared with vid-segment, vid-ending) only when a Hook candidate uses metaphor framing. Key rules for hooks: drop clean (no "let me give you an analogy" announcement), 3-sentence cap, two-layer rule if the metaphor needs a visual.

**Build the lock list:** every number, dollar figure, percentage, timeframe, named method, named client, and specific result that actually appears in the brain dump or foundation. The intro may ONLY use numbers and claims from this lock list. No fabrication.

**Identify the avatar's top problem this video addresses** (1, 2, or 3 from creator-foundation). The Problem/Result step poked AND the Top 3 viewer questions both anchor here.

**Derive the Top 3 viewer questions.** Read the locked title and the thumbnail brief together. Imagine the cold viewer just clicked. What do they most want to know in the next 30 seconds? Surface 3 questions to the creator as a numbered list:

> "Top 3 viewer questions for this video, derived from the title plus thumbnail. These will become the 3 things the Setup promises:
> 1. {Q1}
> 2. {Q2}
> 3. {Q3}
>
> Look right? Or want me to redraft."

Wait. Lock with creator approval before moving on.

**Pick the hook type lane.** Format planner dictates which of the 5 types fit this format. Voice profile's `preferred_hook_types` weights which lanes the creator naturally lands. Cross-reference both. Common pairings (full per-format defaults in each format planner):

- Short Process: Question, Contrarian, Statement, sometimes Fact
- Case Study: Question or Statement (lead with outcome). Sometimes Credibility if the result IS the credibility
- Roast: Statement (often paired with a contestant submission as visual emotion brick), or Contrarian
- Deep Dive: Statement, Contrarian, or Question with conviction. Credibility allowed (format earns it)
- Interview: Statement (the GUEST's identity plus achievement)
- News: Statement or Fact (speed). Question wastes seconds
- Listicle: Statement (often the count itself), Question, or Contrarian

**Credibility-Hook risk flag.** If `creator-foundation.md` shows a small or new channel AND a Credibility Hook is in the running, flag it: "Credibility hooks tend to under-perform on small channels because cold viewers don't trust an unknown 'I' yet. Want to keep it as a candidate, or shift to Question/Statement?" Creator's call.

Confirm hook-type lane with creator in one short message, then move to Phase 2.

### Phase 2: Generate Hook + Problem/Result candidates

**Pull from `banks/hook-bank.md`** for patterns matching the chosen hook type lane. Fill the slots from the brain dump's actual material (numbers, named methods, specific moments, named clients). NO fabrication. If a pattern's slot can't be filled from the lock list, skip the pattern. Don't invent.

**Generate 2-3 Hook candidates.** Each must:

- Be under 5 seconds spoken aloud (rough proxy: under 15 words, under 90 characters)
- Use ONLY numbers and claims from the lock list
- Match the format planner's recommended hook lanes
- Match the creator's voice (read aloud, would they say it?)
- Be distinct from the others (different patterns, different angles, different beats)

**Generate 2-3 Problem/Result candidates.** Each picks ONE of the 3 options from `intro-architecture.md`:

- **Option 1: Poke the Problem** (pivot phrase "The thing is...")
- **Option 2: Tease the Result** (pivot phrase "I used to until...")
- **Option 3: Combine Both** (pivot phrase "But...")

The problem poked needs to be one of the avatar's Top 3 problems (from creator-foundation). When the poke matches a real problem the avatar lives, the viewer feels seen and stays. When the poke matches a problem the avatar doesn't actually have, the viewer feels disconnected and leaves. If candidates can't anchor in the Top 3, regenerate from a different angle.

**Surface options as a short numbered list** with annotation. Example shape:

```
HOOK candidates (lane: Question)
1. "Have you ever wondered why your videos pull 1k views one week and 100k the next?" (Q-1, 14 words, ~4s)
2. "Are you making this thumbnail mistake on every video?" (Q-2, 9 words, ~3s)

PROBLEM/RESULT candidates
A. Poke: "Do you hate making thumbnails? Every creator I know does. The thing is, they're the most important part of the video..." (Top 3 problem #1)
B. Combine: "Do you hate making thumbnails? Every creator does. But there's a formula that..." (Top 3 problem #1)
```

Ask:

> "Pick a hook (1 or 2) and a problem/result (A or B). Or want me to regenerate either?"

Wait.

**Push back on weak picks:**

- They pick a Hook with a fabricated number → REJECT, name the hard rule, regenerate
- They pick a Hook over 5 seconds → flag, ask if they want shorter
- They pick a Problem/Result that doesn't anchor in their Top 3 problems → flag, ask if they want a different angle
- They pick a Hook plus Problem/Result combo where the energy clashes (e.g. high-conviction Statement Hook followed by Pure Tease) → flag, suggest a tighter pairing

**Decide where credibility gets woven.** Of the three slots (Hook / Problem-Result / Setup), credibility most often weaves into the Problem/Result section because that's where claims earn it. Pick the slot AND the credibility form (one of 5 from intro-architecture step 6):

1. Vast experience
2. Volume of people helped
3. Big personal result
4. Big client result
5. Effort signal

Pull the actual credibility from `creator-foundation.md` credibility brags or from the brain dump. NOT a separate self-introduction. Woven, not bolted.

Show the creator the credibility line in context (rewritten Problem/Result with credibility woven in) and confirm.

### Phase 3: Build Setup + Transition

**Setup format (from intro-architecture step 4):**

> "So in this video, I'm going to show you [Q1], [Q2], [Q3]."

Each clause maps to one of the Top 3 viewer questions locked in Phase 1. Keep it tight. Maximum 3. The format planner may say fewer is fine (Short Process often runs one line). Deep Dive may extend to 5 things for 45+ minute videos.

Verb defaults to "show you" or "walk you through." Never "talk about" or "tell you" (banned per intro-architecture step 5).

**Generate the Setup as a single draft** and surface for creator review. Push back if any clause:

- Doesn't map to one of the Top 3 viewer questions (intro is misaligned with title/thumbnail promise)
- Uses a banned verb ("talk about," "tell you")
- Promises something the body of the video doesn't deliver (overpromise kills retention)

**Generate 1-2 Transition candidates.** Pull from `banks/transition-bank.md` Section 1 (hook-forward HF-1..HF-9). Each transition must:

- Hook forward into the first body point with a result the avatar cares about
- Carry an orientation cue (signals the intro is over, content has started)
- Default to verb "show," not "tell"
- Avoid Tier 1 phrases in `transition-bank.md` Section 4: B-1 "let's dive in," B-2 "let's talk about," B-3 "let me tell you," B-6 "and finally / lastly" (these are source-explicit auto-rejects)
- Surface Tier 2 phrases (B-4, B-5, B-7-B-13) as soft friction with the failure mechanism explained; creator decides

**Auto-reject any candidate that contains a Tier 1 banned phrase.** Creator never sees those as options. Tier 2 candidates surface with a flag and the override case noted, and the creator picks. Surface candidates with pattern annotation:

```
TRANSITION candidates
1. "So step one is critical if you want to stop posting daily and still grow, and it works like this." (HF-4)
2. "To start, I'm going to show you how to land your first three clients without a website." (HF-2)
```

Creator picks. If the picked transition references material that doesn't appear in the brain dump's first body point, flag it: "This transition forwards to a result the body doesn't deliver yet. Want to adjust the transition or extend the body?"

### Phase 4: Assemble the full intro and pressure-test

Stitch the locked components in order:

1. Hook (locked in Phase 2)
2. Problem/Result with credibility woven (locked in Phase 2)
3. Setup (locked in Phase 3)
4. Transition (locked in Phase 3)

Show the creator the assembled intro as a clean block. No annotations, no labels, no meta. Just the spoken intro the way they'd read it on camera.

**Length check.** Read the assembled intro mentally as if speaking. Estimate seconds. Defaults from intro-architecture: under 30 seconds total, 15 ideal. Format planners may flex (News compresses to 5-10s, Deep Dive earns 30-60s). If the intro runs long, flag: "This is reading at ~45 seconds. Tighten or accept?"

**Visual matching note.** Surface a one-line note about the visual constraint from intro-architecture: "Heads up: the thumbnail style is {cinematic / scrappy / studio / location}. The first SHOT of the video should match." This is for the creator/editor, not a script edit.

**Visual-proof callouts.** Mark each claim that needs visual proof using the convention in [[knowledge/visual-proof-callouts]] (Obsidian callout placed AFTER the claim line, plus `piece.md` `visual_proofs_called_out:` tracking). Surface any `bank_link: null` cases to the creator at save time so they can capture missing proofs before filming. Don't fabricate visuals; anti-fabrication applies to visual proof too.

**Run [[voice-pressure-test]].** Two-pass check:

- Pass 1 (guardrail): scan the intro for anti-patterns and creator hard rules (hard reject), words-avoided (soft reject, propose swap), POV and energy, signature-phrase signal
- Pass 2 (grain): read a passage from `foundation/reference-pieces/{voice_context}.md` aloud, then the intro aloud, and judge by ear whether the opener move, sentence variation, and energy match. No stored numbers. If no file for this `voice_context`, skip Pass 2 and note the gap

Hard rejects: don't save. Restructure and re-loop.

Soft rejects: surface as a short list ("Spotted: 'dive in' in the transition. Replace with 'show'?"). Auto-swap when the swap is clean (per `Context/brand.md` swaps). Otherwise ask creator.

Soft warns: surface in the meta save but allow.

**Run the read-aloud test.** Ask the creator:

> "Read it out loud once. Would you reword anything?"

If yes, drop back to Phase 2 or 3 with the specific beat the creator would change. Don't re-polish. Restructure preserving creator's exact phrasing for that beat.

**Sibling handoff to `vid-voice-update`.** If the creator's reword reads like a permanent rule (signals like "never use X", "I'd never write that", "swap Y for Z", "I hate that word", "drop X from my voice"), hand the trigger off to `vid-voice-update` before applying the rewrite. That skill triages the signal, appends to `foundation/voice-profile.md` refusals when permanent, and returns. Then apply the rewrite. If the signal reads local ("this line specifically", "doesn't fit this intro"), just apply the rewrite. Do not invoke `vid-voice-update` for one-time edits; it is a permanence gate, not a logger.

### Phase 5: Lock and save

**If standalone mode:**

- Save the assembled intro to `content/pieces/{slug}/script.md` under `## Intro`
- Update `content/pieces/{slug}/piece.md`:
  - `intro_locked: true`
  - `intro_strategy: problem-poke | result-tease | combined`
  - `intro_hook_type: question | contrarian | statement | fact | credibility`
  - `intro_credibility_form: vast-experience | volume-helped | big-personal-result | big-client-result | effort-signal | none`
  - `voice_pressure_test:` block (per voice-pressure-test.md schema)
  - `last_refreshed:` to today's date
- If a story, proof, or testimonial got woven in, update both sides of the wikilink graph per `knowledge/vault-integration.md`: piece's `stories_used:`/`proofs_used:`/`testimonials_used:` AND the bank entry's `used_in:` and `status:`. Both sides. Always.
- Confirm save: "Intro locked. Saved to `script.md`. Voice pressure test: pass."

**If sub-skill mode:**

- Return the output packet to the caller (see "Output packet" below)
- Caller handles the save and the bank-update side

**STOP.** Do not generate body segments, the ending, the title, or the thumbnail. Those are different skills.

## Output packet (sub-skill mode)

```yaml
intro_packet:
  slug: {video-slug}
  full_intro: |
    {the assembled intro, ready to drop into script.md}
  hook:
    type: question | contrarian | statement | fact | credibility
    pattern_id: Q-1 | C-3 | S-2 | etc.
    text: "..."
  problem_result:
    strategy: problem-poke | result-tease | combined
    text: "..."
    top_3_problem_anchored: 1 | 2 | 3
  setup:
    text: "..."
    top_3_questions_used:
      - "..."
      - "..."
      - "..."
  transition:
    pattern_id: HF-4 | HF-2 | etc.
    text: "..."
  credibility:
    woven_into: hook | problem-result | setup | none
    form: vast-experience | volume-helped | big-personal-result | big-client-result | effort-signal | none
  proof_used:
    - "[[proof-slug]]"
  stories_used:
    - "[[story-slug]]"
  voice_pressure_test:
    date: YYYY-MM-DD
    result: pass | soft-warn | soft-reject | hard-reject
    pass1_guardrail: true | false
    voice_context: youtube-script
    pass2_grain: true | false | skipped-no-reference
    flags: []
    read_aloud_confirmed: true | false
```

The packet keeps downstream context narrow. Don't pass entire reference files. Pass the locked decisions.

## Anti-fabrication discipline

Every number, name, claim, dollar figure, percentage, timeframe, named method, and specific moment in the intro needs to be backed by something in the brain dump, the script body, or foundation docs. The reason: a fabricated number lies to the viewer, and once the body of the video doesn't deliver on the fabricated promise, retention dies. If the source isn't there, the intro can't claim it.

If the creator wants a number-driven hook and the script doesn't have a usable number, kick it back: "The brain dump doesn't have a number to ground this. Either drop the number-driven angle or add the missing number to the brain dump first."

Same rule that lives in `vid-title` and `vid-thumbnail`. Kept consistent across writing skills.

## Hard friction (auto-reject)

These get blocked at candidate-generation time. Creator never sees them.

1. **Fabricated numbers, names, or claims.** Anything not in the lock list. REJECT.
2. **Tier 1 banned transition phrases.** B-1, B-2, B-3, B-6 in `transition-bank.md` Section 4 (source-explicit bans). REJECT and substitute. Tier 2 phrases (B-4, B-5, B-7-B-13) surface as soft friction in the prior section, not here.
3. **Bolted-on self-introduction.** ("Hi, I'm Bob. I've been doing this for 10 years...") REJECT. Credibility weaves into a claim moment, never as a separate intro.
4. **Setup that doesn't answer any of the Top 3 viewer questions.** REJECT. The intro is misaligned with the title/thumbnail promise.
5. **Em-dashes in the intro.** REJECT (per `Context/brand.md` and Vale enforcement).
6. **Generic curiosity bait** ("You won't believe what happened next") is Tier 2 soft friction, not auto-reject. Surface with the explanation; creator decides whether the format and tone earn it.

## Soft friction (flag and explain, creator decides)

These tend to under-perform. Surface the friction in the candidate annotation. Let the creator override with reasoning.

7. **Credibility Hook on small or new channels.** Tends to fail cold-trust test. A single dramatic claim can earn it.
8. **Setup with more than 3 things.** Tends to overwhelm. Complex methodologies may need it. Deep Dive 45+ minute videos may use 5.
9. **Hook longer than 5 seconds.** Tends to waste attention. Story-driven opens can earn the time.
10. **Whole intro over 30 seconds.** Tends to mean teaching crept in. Some formats (Deep Dive) earn longer setup.
11. **Teaching content inside the intro.** Tends to be a hook-killer. Contextual setup that LOOKS like teaching can land.
12. **Problem-poke that doesn't match avatar Top 3.** Tends to miss audience. A fresh angle on a related problem can work.
13. **Topic-label dressed as hook.** ("Today's video is about how to grow on YouTube.") Tends to announce instead of pull. Surface and ask.
14. **Hedge in the hook.** ("Maybe you've been making a small mistake...") Tends to undermine stakes. Some humble brands defend hedges.

When showing candidates that triggered soft friction, surface the flag in the annotation: "2. {hook}, soft flag: hedge word 'maybe' undermines stakes."

## Natural language patterns that work

When generating, lean toward shapes that real intros use. These read as one continuous human thought.

- **Hook:** match one of the 5 types from `intro-architecture.md`. Patterns live in `banks/hook-bank.md`.
- **Problem/Result:** lean on the pivot phrases (`The thing is...`, `I used to until...`, `But...`).
- **Setup:** the literal "So in this video, I'm going to show you X, Y, Z" template. Don't over-engineer.
- **Transition:** hook-forward patterns from `banks/transition-bank.md` Section 1. Default verb is "show."

## Intro craft notes (for YOUR thinking, not the chat)

These are the deeper principles. Use them to judge candidates internally before showing the list.

**1. The intro is for HOOKING, not EDUCATING.** If the intro starts teaching the lesson before the Setup, the viewer's brain switches to evaluation-mode instead of curiosity-mode. Most leave. Curiosity is the fuel for the rest of the video. Don't burn it in the intro.

**2. The Setup is a contract.** Each of the 3 things named in the Setup must actually appear in the body. If the body doesn't deliver, the contract breaks and retention dies in minute three. When showing the Setup draft, mentally check whether the brain dump actually delivers all three.

**3. Credibility is woven, not bolted.** The bolted-on self-intro ("Hi, I'm Bob. 10 years of experience...") is the most common failure mode in homemade intros. Credibility belongs at the moment a claim is made, not before. If the candidate intro feels like a bio, restructure.

**4. Specificity equals credibility.** "$14,332" beats "made money." "23:07 to 19:42" beats "got faster." When pulling from the brain dump, default to the most specific number available. Round numbers feel made up; cents and decimals feel real.

**5. Format identity beats template fit.** The 6-part architecture is universal, but each format trims, expands, or reorders. Read the format planner before generating. Don't force a Deep Dive's full 30-second intro onto a News video. Don't compress a Case Study's full Combine-Both into News-style speed. The format planner is the adaptation layer.

**6. The read-aloud test is the final arbiter.** Numbers and pattern-matching can pass while the intro still feels off. The creator's mouth knows. If they'd reword it when speaking, the draft is wrong. Every word has to survive being said out loud.

## Reference index

| File | Why |
|---|---|
| `knowledge/intro-architecture.md` | The 6-part architecture, 5 hook types, 3 problem/result options, banned transitions, format-adaptation map |
| `knowledge/format-planners/{format}.md` | Per-format intro adaptation (length, hook lane, setup shape, transition style) |
| `knowledge/voice-rhythm.md` | The lens for hearing rhythm in the reference pieces and the draft; no stored numbers |
| `knowledge/voice-pressure-test.md` | Pre-save validation (Pass 1 guardrail, Pass 2 grain by ear vs reference pieces) |
| `knowledge/visual-proof-callouts.md` | Shared with vid-segment. Owns the CALLOUT SYNTAX: Obsidian `> [!important] Visual proof needed` placement after claim, plus `visual_proofs_called_out:` piece.md schema |
| `banks/hook-bank.md` | 5-type pattern library (Q-1..Q-8, C-1..C-7, S-1..S-8, F-1..F-7, Cr-1..Cr-6) plus anti-patterns |
| `banks/transition-bank.md` Section 1 | Hook-forward transitions HF-1..HF-9 (intro to first point) |
| `banks/transition-bank.md` Section 4 | Banned phrases. Tier 1 (B-1, B-2, B-3, B-6) auto-reject; Tier 2 (others) soft-friction, creator decides |
| `knowledge/emotion-brick-decision-matrix.md` | Shared with vid-segment, vid-ending. 5-question matrix → Visual Demo / Story / Metaphor lane. Informs intro emotional weight when picking Hook + Problem/Result energy |
| `knowledge/story-pulling-criteria.md` | Shared with vid-segment, vid-ending. 5 criteria for picking the right story from N candidates (stage match, problem match, outcome specificity, type match, reuse hygiene). Conditional load when credibility-line weaves a story |
| `knowledge/proof-placement-rules.md` | Shared with vid-segment, vid-ending. Owns the PLACEMENT decision (where proof goes in the segment, bank-pulling, presentation-format selection across static-screenshot / before-after-pairing / live-clip / inline-stat). Pairs with visual-proof-callouts.md (which owns the syntax). Conditional load when credibility line cites a number or screenshot |
| `knowledge/metaphor-integration.md` | Shared with vid-segment, vid-ending. Drop-clean / no-announcement / 3-sentence cap / two-layer rule. Conditional load when a Hook candidate uses metaphor framing |
| `foundation/creator-foundation.md` | Avatar, Top 3 problems, credibility brags |
| `foundation/voice-profile.md` | The thin guardrail: fingerprint, signature phrases, refusals, POV/energy, optional preferred_hook_types / transition_style_preferences / intro_pacing |
| `foundation/reference-pieces/{voice_context}.md` | The voice engine (voice only, not structure): real intact passages to write the intro from, matched to piece.md `voice_context` |
| `content/pieces/{slug}/piece.md` | Locked title, format, voice_context, goal, pillar |
| `content/pieces/{slug}/thumbnail-brief.md` | Locked thumbnail picks (drives Top 3 viewer-question derivation) |
| `content/pieces/{slug}/brain-dump.md` / `piece.md` / `script.md` | The actual material the intro must align to |
| `references/hook-type-selection-flow.md` | RUNTIME decision: how to cross-reference format + voice + channel size + brain dump to lock the hook lane. Does NOT restate the 5 hook types (those live in intro-architecture Step 2 and hook-bank) |
| `references/credibility-line-weaving.md` | RUNTIME decision: which intro slot (Hook / Problem-Result / Setup) the credibility line weaves into given the form available. Does NOT restate the 5 forms or bolted-on rule (those live in intro-architecture Step 6) |
| `references/problem-result-options.md` | RUNTIME decision: how to read pain-acuteness vs result-drama to pick Poke / Tease / Combine. Does NOT restate the 3 options or pivot phrases (those live in intro-architecture Step 3) |

## Principles

- **Conversation, not document.** Short messages. Never dump reference content. References are for Claude to think with.
- **Creator drives, Claude structures.** The intro draws from the creator's actual material: the angle, the numbers, the moments. Claude doesn't invent claims to make a hook sound better.
- **Specificity wins.** Real numbers over round numbers. Named methods over generic descriptions. Specific moments over "people."
- **Format identity matters.** Read the format planner before generating. Each format trims or expands the universal architecture.
- **Credibility is woven, not bolted.** Never write a separate self-introduction.
- **Hook for curiosity, not teaching.** The intro is for hooking. Save teaching for the body.
- **Read aloud or it doesn't ship.** Every beat has to survive being spoken on camera.

## Related skills

- `vid-foundation` produces the foundation docs this skill loads
- `vid-voice-capture` produces voice-profile.md and reference-pieces/*.md
- `vid-title` locks the title before this skill runs
- `vid-thumbnail` locks the thumbnail before this skill runs (drives Top 3 viewer-question derivation)
- `vid-segment` (sister skill) writes body segments after the intro is locked
- `vid-ending` (sister skill) writes the ending close, consumes a different section of transition-bank
- `vid-pressure-test` (future) does adversarial review on the full assembled script
- `vid-pipeline` (future) is the orchestrator that calls this skill during STRUCTURE or SCRIPT phase
