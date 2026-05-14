---
name: vid-foundation
description: Thin orchestrator for the Authentic AI OS foundation. Checks what's locked in creator-foundation.md and packaging-system.md, then points the creator at the next skill in the foundation sequence. Use this when a creator is new to the system, when they're not sure what foundation step to run next, or when a downstream skill is missing inputs and the creator needs to know which foundation skill produces them. Triggers on "set up my channel", "start my creator foundation", "what's the next foundation step", "where am I in the foundation", "I'm new to Authentic AI OS".
---

# Foundation

Thin orchestrator. Checks foundation state, points the creator at the next skill in the sequence. Doesn't run interviews itself.

The actual interview work happens in six focused skills:

1. `vid-avatar`. Offer plus avatar plus Top 3 perceived problems.
2. `vid-positioning`. Iceberg Statement.
3. `vid-pillars`. 8 to 12 content pillars.
4. `vid-credibility`. Three viewer-relevant brags.
5. `vid-backstory`. Problem-Action-Outcome backstory.
6. `vid-packaging`. Gift framework, format rotation, title bank seed, thumbnail strategy, design guardrails, creation path.

Plus `vid-voice-capture` for the voice profile (run after `vid-packaging`).

## Contract

**Inputs (optional):** `foundation/creator-foundation.md`, `foundation/packaging-system.md`, `foundation/voice-profile.md`. Any combination, any state.

**Outputs:** none directly. This skill routes. The sub-skills produce.

## How this skill runs

### Step 1: Read state silently

Check three files. Quiet reads. Don't announce.

- `foundation/creator-foundation.md`: does it exist? Which sections are populated?
- `foundation/packaging-system.md`: does it exist?
- `foundation/voice-profile.md`: does it exist?

### Step 2: Map state to next skill

Use this routing table:

| State | Next skill to invoke |
|---|---|
| Nothing exists | `vid-avatar` |
| Avatar/Offer/Top 3 missing or partial | `vid-avatar` |
| Avatar locked, Iceberg Statement missing | `vid-positioning` |
| Iceberg Statement locked, Content pillars missing | `vid-pillars` |
| Content pillars locked, Credibility brags missing | `vid-credibility` |
| Credibility brags locked, Backstory missing | `vid-backstory` |
| Backstory locked, `packaging-system.md` missing or incomplete | `vid-packaging` |
| Foundation complete, `voice-profile.md` missing | Point at `vid-voice-capture` (don't auto-invoke; it needs source material) |
| Everything complete | Foundation done. Point at next paths. |

### Step 3: Tell the creator where they are, then auto-invoke

Short message. Mirror what's already locked. Name the next skill. Then invoke it via the Skill tool immediately. No friction step. The creator doesn't need to type another command.

Shape:

> "Here's where you are.
>
> Locked: [list filled sections, plain language, no jargon].
>
> Picking up with `[next skill]`. That [one sentence on what it produces]."

Then immediately invoke the next skill. From there, each sub-skill auto-advances to the one after it. The whole foundation runs end-to-end unless the creator says stop.

### Step 4: Handle the stop signals

If the creator says any of these, halt the chain and don't invoke the next skill:

- "stop here", "stop", "halt"
- "let me come back to this later"
- "I need a break"
- "hold on"

If they're quiet between sub-skills but engaged in the previous one's content, that's not a stop signal. Continue.

### Step 5: Foundation complete

When all 6 foundation sub-skills have locked their sections plus `packaging-system.md` exists, congratulate briefly and surface the per-video paths:

> "Foundation complete. You're ready to make videos.
>
> Three paths from here:
> 1. Run `vid-voice-capture` to build your voice profile. Critical for every script. Bring 2 to 3 transcripts or a 10-minute live riff.
> 2. Capture raw material when it lands (`vid-capture`).
> 3. Build pattern banks from your channel and competitors (`vid-research`).
>
> What sounds right?"

`vid-voice-capture` is NOT auto-invoked because it needs source material the creator has to bring. The handoff is a stopping point.

## What this skill is NOT

- An interview skill. It doesn't ask the creator any of the foundation questions. Those live in the six sub-skills.
- A combined run. It doesn't run all six skills back-to-back. Each interview deserves a dedicated session.
- A refresh tool. If the creator wants to refresh a specific section, they run the sub-skill directly.

If the creator asks foundation questions during this skill ("can you write my Iceberg Statement?"), redirect:

> "That's `vid-positioning`'s job. It runs a focused session for the Iceberg Statement and saves it to `foundation/creator-foundation.md`. Want me to point you there?"

## Pre-check

Always read `foundation/creator-foundation.md` and `foundation/packaging-system.md` (silent). If either doesn't exist, the creator is at or near the start. If both exist, check `foundation/voice-profile.md` last.

## Anti-patterns

- Running any sub-skill's interview content here. This skill routes, not interviews.
- Reading the references inside `vid-avatar`, `vid-positioning`, etc. Those belong to their skills.
- Asking the creator to type the next command. Auto-invoke the next skill via the Skill tool.
- Continuing to invoke skills after a clear stop signal.
- Auto-invoking `vid-voice-capture` when the foundation completes. That skill needs source material and is a manual start.
- Surfacing jargon (Iceberg Statement, BENS, 3+1 rotation) without context. Translate when needed.

## References

None. This skill is route-only.
