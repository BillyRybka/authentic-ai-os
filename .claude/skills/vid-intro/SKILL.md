---
name: vid-intro
description: Produce the full 6-part video intro (Top 3 viewer questions, Hook, Problem/Result, Setup, Transition, credibility woven in) for one video. Format-aware, title-aware, thumbnail-aware. Runnable standalone OR invoked by vid-pipeline during the script phase. Use whenever the creator needs the opening of a video written, even if they don't say "intro": "write the intro", "intro for [video]", "lock the hook", "rewrite the intro", "fix the intro", "what should I open with", "how do I start this video", "I need a hook", "the opening feels off", "help me set up this video".
---

# Video Intro Builder

Writes the opening of one video: Hook, Problem/Result with credibility woven in, Setup, and Transition, anchored to the Top 3 questions the viewer clicked to get answered. The title and thumbnail made a promise; the intro is where the video starts keeping it.

**This is a conversation, not a document.** Short messages, one decision at a time, creator approves each lock. References are for your thinking; never paste them at the creator.

## What loads, and when

Load each file at the phase that needs it. Do not front-load.

| Phase | Load | For |
|---|---|---|
| 1 | `content/pieces/{slug}/piece.md` | locked `title`, `thumbnail_text`, format, goal, pillar, voice_context |
| 1 | `content/pieces/{slug}/brain-dump.md` + `script.md` (the outline) | the material, the lock list, what the body will deliver |
| 1 | `foundation/creator-foundation.md` | avatar, Top 3 problems, credibility brags |
| 1 | `knowledge/intro-architecture.md` | the 6-part architecture, 5 hook types, 3 problem/result options, soft-friction list |
| 1 | `knowledge/format-planners/{format}.md` | how THIS format trims, expands, or reorders the intro |
| 1 | `references/hook-type-selection-flow.md` | the hook-lane decision: format x voice x channel size x material |
| 1 | `foundation/voice-profile.md` (see fallback below) | guardrail + optional `preferred_hook_types` |
| 2 | `knowledge/hook-patterns.md` | fill-in patterns for the chosen hook lane |
| 2 | `references/problem-result-options.md` | reading pain-acuteness vs result-drama to pick Poke / Tease / Combine |
| 2 | `references/credibility-line-weaving.md` | which slot (Hook / Problem-Result / Setup) the credibility line weaves into |
| 2, conditional | `banks/story-bank/` + `knowledge/story-pulling-criteria.md` | only if a credibility candidate weaves a story; stage-match is the top filter here |
| 2, conditional | `banks/proof-bank/`, `banks/testimonial-bank/` + `knowledge/proof-placement-rules.md` | only if the credibility line cites a number, screenshot, or testimonial |
| 2, conditional | `knowledge/metaphor-integration.md` | only if a Hook candidate uses metaphor framing (drop clean, 3-sentence cap) |
| 3 | `knowledge/transition-patterns.md` Sections 1 + 4 | hook-forward patterns and the banned-phrase tiers |
| 4 | `foundation/reference-pieces/{voice_context}.md` | the voice engine for the grain check |
| 4 | `knowledge/voice-pressure-test.md` + `knowledge/voice-rhythm.md` | the two-pass voice check, judged by ear |
| 4 | `knowledge/visual-proof-callouts.md` | callout syntax for claims needing visual proof |
| 5 | `knowledge/vault-integration.md` | the update-both-sides rule for any bank pull |

## Prerequisites

- `content/pieces/{slug}/piece.md` with `title` and `thumbnail_text` locked. Missing → run `vid-title` / `vid-thumbnail` first. The Top 3 viewer questions derive from that package.
- `content/pieces/{slug}/script.md` exists as vid-structure's outline (`segment_purposes` set in piece.md). **No outline → hard stop: run `vid-structure` first.** The Transition forwards into the first body point and the Setup promises what the body delivers; neither exists before the outline. (Running early also gets the intro destroyed when vid-structure later writes its skeleton.)
- `content/pieces/{slug}/brain-dump.md` exists.
- `foundation/creator-foundation.md` exists.
- `foundation/voice-profile.md`: load if present. If missing, fall back to the universal hard rules (no em-dashes, no AI-isms, no hedging), note "Voice profile not captured, using default guardrails. Run `vid-voice-capture` for sharper voice fit," and continue. Voice is never a blocker.

**Invoked by the pipeline:** the caller has verified prerequisites; skip re-checking them and skip questions the caller already answered. Never skip the creator locks (Top 3 questions, hook lane, candidate picks). Standalone or pipeline, the flow and the saves are identical.

## Phase 1: Anchor

**Build the lock list:** every number, dollar figure, percentage, timeframe, named method, named client, and specific result that appears verbatim in the brain dump, outline, or foundation. Candidates may use ONLY material from this list. Nothing invented.

**Name the avatar's problem this video addresses** (usually one of the Top 3 from creator-foundation). The Problem/Result poke and the viewer questions both anchor here.

**Derive the Top 3 viewer questions.** Read the locked title and thumbnail text together as one package. The viewer just clicked that package cold: what do they most want answered in the next 30 seconds? Surface 3 questions as a numbered list and ask the creator: look right, or redraft? **Wait. Lock with creator approval.** These become the Setup's on-camera promises.

**Pick the hook lane** per `references/hook-type-selection-flow.md`: the format planner says which of the 5 types fit this format, `preferred_hook_types` says where the creator naturally lands, the material says what's available. One flag worth surfacing: a Credibility hook on a small or new channel tends to fail the cold-trust test; say so and let the creator call it. Confirm the lane in one short message.

## Phase 2: Hook + Problem/Result

**Generate 2-3 Hook candidates** from `knowledge/hook-patterns.md` patterns in the chosen lane, slots filled from the lock list only. Each: under 5 seconds spoken (roughly 15 words), distinct from the others, sayable by THIS creator. If a pattern's slot can't be filled from the lock list, skip the pattern.

**Generate 2-3 Problem/Result candidates.** Pick per `references/problem-result-options.md`: acute lived pain → Poke the Problem; a dramatic receipt → Tease the Result; both loud → Combine. The poked problem must be one the avatar actually lives (usually the problem this video was framed around). A poke the avatar doesn't feel loses them; only regenerate if it rings false.

Show both lists short and annotated (pattern, word count, any soft flag). Ask for a pick from each. **Wait.**

Push back on weak picks: fabricated number (hard reject, regenerate), over 5 seconds (flag), a problem the avatar wouldn't feel (flag), hook + problem/result energies that clash (flag, suggest a tighter pairing).

**Weave the credibility.** Per `references/credibility-line-weaving.md`, pick the slot (Hook / Problem-Result / Setup, most often Problem/Result, where claims earn it) and the form (one of the 5 in intro-architecture Step 6). Pull the actual brag from creator-foundation or the brain dump. Woven into a claim moment, never a separate self-introduction. Show the creator the line in context and confirm.

## Phase 3: Setup + Transition

**Setup:** "So in this video, I'm going to show you [Q1], [Q2], [Q3]." Each clause maps to one locked viewer question. Maximum 3 (the format planner may trim to 1 or extend for long Deep Dives). Verbs: "show you" / "walk you through," never "talk about" / "tell you." Push back if a clause maps to no locked question or promises something the outline doesn't deliver. The Setup is a contract; the body pays it.

**Transition:** 1-2 candidates from `transition-patterns.md` Section 1 (hook-forward). Each forwards into the outline's FIRST body point with a result the avatar cares about, and signals the content has started. Tier 1 banned phrases (Section 4) never surface as options; Tier 2 phrases surface flagged with the failure mechanism, creator decides. If a picked transition forwards to something the first body point doesn't deliver, flag it.

## Phase 4: Assemble + pressure-test

Stitch: Hook → Problem/Result (credibility woven) → Setup → Transition. Show it as one clean spoken block, no labels or annotations, exactly as they'd read it on camera.

**Length check** by ear: under 30 seconds default, 15 ideal; the format planner flexes it (News compresses to 5-10s, Deep Dive earns more). Flag if long.

**Visual-proof callouts:** mark each claim needing on-screen proof per `knowledge/visual-proof-callouts.md` (callout after the claim line + `visual_proofs_called_out` tracking); surface any missing-proof cases at save time.

**Voice check, two passes** per `knowledge/voice-pressure-test.md`: Pass 1 guardrail (anti-patterns and creator hard rules = hard reject, restructure; words-avoided = propose the swap; auto-swap only when the refusals define a clean swap). Pass 2 grain: read a reference-piece passage aloud, then the intro, and judge by ear. No reference piece for this voice_context → skip Pass 2 and note the gap.

**Read-aloud test:** ask the creator to read it out loud once. Would they reword anything? If yes, drop back to the specific beat and restructure preserving their exact phrasing. If the reword sounds like a permanent rule ("never use X", "I'd never say that"), hand it to `vid-voice-update` first (it decides permanent vs one-time), then apply. One-time edits just get applied.

## Phase 5: Lock and save

Always, both modes:

- Write the intro into `content/pieces/{slug}/script.md` under `## Intro`, replacing the stub vid-structure left.
- Update piece.md: `intro_locked: true`, bump `last_updated:`.
- Any bank pull gets both sides updated per `knowledge/vault-integration.md`: the piece's `stories_used` / `proofs_used` / `testimonials_used` AND the bank entry's `used_in` + `status`.
- Confirm in chat with the real voice-check result (clean / soft-flagged), not a scripted "pass."

**STOP.** Body segments, ending, title, thumbnail are other skills' jobs.

## Hard rules (candidates never shown when violated)

1. **No fabrication.** Numbers, names, claims: lock list only. If the creator wants a number-driven hook and no number exists, kick it back: add the number to the brain dump or drop the angle.
2. **Tier 1 banned transition phrases** (transition-patterns Section 4: B-1, B-2, B-3, B-6). Substitute silently.
3. **No bolted-on self-introduction.** Credibility weaves into a claim moment.
4. **Setup clauses map to locked viewer questions.** Otherwise the intro breaks the title/thumbnail promise.
5. **No em-dashes.** Universal hard rule; Vale enforces on save.

Everything softer (credibility hook on a small channel, 4+ setup items, long hooks, teaching creep, hedges, topic-label openers) is soft friction: the list with why-it-tends-to-fail and when-it's-earned lives in `intro-architecture.md`, which is already loaded. Flag it in the candidate annotation and let the creator decide.
