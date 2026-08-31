---
name: vid-intro
description: Write the opening of one video. Hook, problem/result, setup, and transition anchored to the questions the locked title and thumbnail raised, credibility woven in. Format-aware. Standalone or via vid-pipeline in the script phase. Use when the creator needs the opening of a video written, even if they don't say "intro". Triggers on "write the intro", "intro for [video]", "lock the hook", "rewrite the intro", "fix the intro", "what should I open with", "how do I start this video", "I need a hook", "the opening feels off", "help me set up this video".
---

# Video Intro Builder

Writes the opening of one video: Hook, Problem/Result with credibility woven in, Setup, and Transition, anchored to the Top 3 questions the viewer clicked to get answered. The title and thumbnail made a promise; the intro is where the video starts keeping it. The intro is for hooking, not educating: a lesson in the first 30 seconds switches the viewer from curiosity to evaluation, and they leave.

**This is a conversation, not a document.** Short messages, one decision at a time, creator approves each lock. References are for your thinking; never paste them at the creator.

## What loads, and when

Read as you go; never front-load. Skill-local `references/` decision flows are named where they fire.

- **Phase 1 vault reads:** `content/pieces/{slug}/piece.md` (locked `title`, `thumbnail_text`, format, plus framing's `## The Read`), `brain-dump.md` and `script.md` (the material and the outline the intro forwards into), `foundation/avatar.md` (avatar, Top 3 problems), `foundation/credibility.md` (the three proof points), `foundation/voice-profile.md` (guardrails, `preferred_hook_types`; if missing, run on the default guardrails, note "Voice profile not captured, run `vid-voice-capture` for sharper voice fit," and continue; voice is never a blocker).
- **Phase 1 craft:** `knowledge/intro-architecture.md` (the 6-part architecture and friction list), `knowledge/format-planners/{format}.md` (how THIS format trims the intro), and `knowledge/prose-craft.md` (the seven moves, loaded before drafting rather than as a filter after it).
- **Phase 2 patterns:** `references/hook-patterns.md`, plus the creator's `banks/hook-bank.md` if one exists. **Phase 3:** `knowledge/transition-patterns.md` Sections 1 + 4.
- **Phase 4 voice, proof, and pacing:** `foundation/reference-pieces/{voice_context}.md`, `knowledge/voice-pressure-test.md`, `knowledge/voice-rhythm.md`, `knowledge/visual-proof-callouts.md`, `knowledge/attention-craft.md` (pacing and energy of the spoken intro; the ear test behind the length check).
- **Phase 5:** `knowledge/bank-contract.md` (the update-both-sides rule for bank pulls).
- **Conditional depth:** story/proof/testimonial banks with `knowledge/story-pulling-criteria.md` or `knowledge/proof-placement-rules.md` (only when the credibility weave pulls bank material); `knowledge/metaphor-integration.md` (only when a hook runs on metaphor).

## Prerequisites

- `content/pieces/{slug}/piece.md` with `title` and `thumbnail_text` locked (missing → run `vid-title` / `vid-thumbnail` first; the Top 3 viewer questions derive from that package), plus `brain-dump.md`, `foundation/avatar.md` and `foundation/credibility.md`.
- `content/pieces/{slug}/script.md` exists as vid-structure's outline (`segment_purposes` set in piece.md). **No outline → hard stop: run `vid-structure` first.** The Transition forwards into the first body point and the Setup promises what the body delivers; neither exists before the outline. Running early also gets the intro destroyed when vid-structure later writes its skeleton.

**Invoked by the pipeline:** the caller has verified prerequisites; skip re-checking them and skip questions the caller already answered. Never skip the creator locks (Top 3 questions, hook lane, candidate picks). Standalone or pipeline, the flow and the saves are identical.

## Phase 1: Anchor

**Build the lock list:** every number, dollar figure, percentage, timeframe, named method, named client, and specific result that appears verbatim in the brain dump, outline, or foundation. Candidates may use ONLY material from this list. Nothing invented.

**Derive the Top 3 viewer questions.** Read the locked title and thumbnail text together as one package. The viewer just clicked that package cold: what do they most want answered in the next 30 seconds? Surface 3 questions as a numbered list and ask the creator: look right, or redraft? **Wait. Lock with creator approval.** These become the Setup's on-camera promises. The questions and the Problem/Result poke both anchor to the avatar's problem this video addresses (usually one of the Top 3 from `foundation/avatar.md`).

**Pick the hook lane.** The format planner says which of the 5 hook types fit this format, `preferred_hook_types` says where the creator naturally lands, and the lock list says what the material can actually fill (a Fact hook with no surprising stat in the dump is a dead lane). Format wins conflicts, voice breaks ties. One flag worth surfacing: a Credibility hook on a small or new channel usually fails the cold-trust test; say so and let the creator call it. Confirm the lane in one short message. When the inputs disagree and the call is close, `references/hook-type-selection-flow.md` has worked calls.

## Phase 2: Hook + Problem/Result

**Mine `## The Read` first.** Its **Stakes** are the richest hook material in the piece: framing already escalated the consequences and landed the last one somewhere the viewer would not trace back to the cause, which is exactly the shape a cold-open loop wants. The **misattribution** near the end of Stakes, what they blame and try to fix instead, is the Problem/Result poke, because it is the thing the viewer is currently doing and does not know is wrong. Everything mined here still passes through the lock list; the Read is framing's language, not a source of new specifics. Older pieces have no Read section, in which case work from the title package and the dump as before.

### What makes a hook land

Four tests, judged by ear, not by formula:

- **Curiosity gap.** The first line opens a loop the viewer can only close by watching. A line that answers itself, or announces the topic, has no gap and no pull.
- **Specificity is the trust signal.** A named number, pain, or situation tells the cold viewer there is real material behind this. Vague reads as "no information here, skip."
- **The did-they-make-this-for-me test.** The avatar should feel the first line was made for them. A question anyone could ask is a question no one hears.
- **One hook per open.** A question plus a stat plus a command in five seconds reads as panic. Pick the strongest and let it breathe.

> Great: "Have you ever wondered why one of your videos pulls 100k views and the next one barely cracks 1k?"
> Weak: "Have you ever wondered why people are the way they are?"
> Same pattern, same lane. The great one names the exact pain this avatar lives weekly; the weak one could be for anyone, so it lands for no one.

> Great: "The second your video loads, viewers judge it, and if they don't like what they see they leave forever."
> Weak: "The second your video loads, things start happening."
> Same shape. One has stakes with a clock on them, the other has none. Specificity is the whole difference.

> Great: "I'm a fitness coach and I don't do cardio."
> Weak: "Have you ever wondered why fitness is hard? Here's a fact: 80% of people quit. Stop doing what you're doing. I'll show you my system."
> One defensible inversion the body can pay off, versus four hooks stacked into five seconds. Stacked hooks read as panic.

**Generate 2-3 Hook candidates** in the locked lane. Pull patterns from `references/hook-patterns.md`, and from the creator's `banks/hook-bank.md` when it exists: hooks that already held retention on THIS channel outrank generic patterns. The vault bank supplements the plugin patterns, never replaces them, and a missing bank is fine. Fill every slot from the lock list only. Each candidate: under 5 seconds spoken (roughly 15 words), distinct from the others, sayable by THIS creator. If a slot cannot be filled from the lock list, skip that pattern. If the creator wants a number-driven hook and no number exists, kick it back: the number goes into the brain dump first, or the frame changes. Never invent one.

**Generate 2-3 Problem/Result candidates** by matching intensity: acute lived pain → Poke the Problem; a dramatic receipt → Tease the Result; both loud → Combine. The poked problem must be one the avatar actually lives (usually the problem this video was framed around); a poke the avatar does not feel loses them. Close calls: `references/problem-result-options.md` has worked matches.

**The redundancy rule:** when the hook already carries the result (a Credibility hook that IS the receipt, a tease-shaped hook), do not spend a second beat saying it again. Delete the Problem/Result, or cut it to the curiosity pivot ("Three things changed."). Two beats saying one thing reads as stalling.

Show both lists short and annotated (pattern, word count, any soft flag). Ask for a pick from each. **Wait.** Push back on weak picks: fabricated number (hard reject, regenerate), over 5 seconds (flag), a problem the avatar would not feel (flag), clashing energies between the two picks (flag, suggest a tighter pairing). Anything softer (long hooks, teaching creep, topic-label openers, 4+ setup items) lives in the `intro-architecture.md` friction list: flag it with why it usually fails and let the creator decide.

**Weave the credibility.** Pick the slot by what the receipt does: dramatic enough to stop a cold viewer on its own → it IS the Hook; it proves the result being teased → Problem/Result (the default, where claims earn it); it frames why the body can be trusted → Setup. Pull the actual brag from `foundation/credibility.md` or the lock list and set it inside the claim moment, never as a separate self-introduction. Show the line in context and confirm. Worked weaves per slot: `references/credibility-line-weaving.md`. When the format planner says the format usually skips credibility (News, small-channel Roast), skip it; forcing a weave is its own failure.

## Phase 3: Setup + Transition

**Setup:** "So in this video, I'm going to show you [Q1], [Q2], [Q3]." Each clause maps to one locked viewer question. Maximum 3 (the format planner may trim to 1, drop it for News, or extend for long Deep Dives). Verbs: "show you" / "walk you through," never "talk about" / "tell you." Push back if a clause maps to no locked question or promises something the outline does not deliver. The Setup is a contract; the body pays it.

**Transition:** 1-2 candidates from `transition-patterns.md` Section 1 (hook-forward). Each forwards into the outline's FIRST body point with a result the avatar cares about, and signals the content has started. Tier 1 banned phrases (Section 4) never surface as options; substitute silently. Tier 2 phrases surface flagged with the failure mechanism, creator decides. If a picked transition forwards to something the first body point does not deliver, flag it.

## Phase 4: Assemble + pressure-test

Stitch: Hook → Problem/Result (credibility woven) → Setup → Transition. Show it as one clean spoken block, no labels or annotations, exactly as they would read it on camera.

**Length check** by ear: under 30 seconds default, 15 ideal; the format planner flexes it (News compresses to 5-10s, Deep Dive earns more). Flag if long. Over the limit usually means a lesson crept in; move it into the body.

**First-shot match.** The thumbnail set a production-quality expectation, and the first shot has to match it: cinematic thumbnail, cinematic open; scrappy thumbnail, scrappy open. A mismatch reads as a lie and the viewer leaves before the hook lands. Call out the expected first shot as a production note when the intro locks.

**Visual-proof callouts:** mark each claim needing on-screen proof per `knowledge/visual-proof-callouts.md` (callout after the claim line + `visual_proofs_called_out` tracking); surface any missing-proof cases at save time.

**Voice check, two passes** per `knowledge/voice-pressure-test.md`: Pass 1 guardrail (anti-patterns and creator hard rules = hard reject, restructure; words-avoided = propose the swap; auto-swap only when the refusals define a clean swap). Pass 2 grain: read a reference-piece passage aloud, then the intro, and judge by ear. No reference piece for this voice_context → skip Pass 2 and note the gap.

**Read-aloud test:** ask the creator to read it out loud once. Would they reword anything? If yes, drop back to the specific beat and restructure preserving their exact phrasing. If the reword sounds like a permanent rule ("never use X", "I'd never say that"), hand it to `vid-voice-update` first (it decides permanent vs one-time), then apply. One-time edits just get applied.

## Phase 5: Lock and save

- Write the intro into `content/pieces/{slug}/script.md` under `## Intro`, replacing the stub vid-structure left.
- Update piece.md: `intro_locked: true`, the locked `viewer_questions`, bump `last_updated:`.
- Any bank pull gets both sides updated per `knowledge/bank-contract.md`: the piece's `stories_used` / `proofs_used` / `testimonials_used` AND the bank entry's `used_in` + `status`.
- No em-dashes in anything saved. Vale enforces it; catch it here.
- Confirm in chat with the real voice-check result (clean / soft-flagged), not a scripted "pass."

**STOP.** Body segments, ending, title, thumbnail are other skills' jobs.
