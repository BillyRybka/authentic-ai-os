---
name: vid-foundation
description: Thin orchestrator for the Authentic AI OS foundation. Checks what's locked in creator-foundation.md and packaging-system.md, then points the creator at the next skill in the foundation sequence. Use this when a creator is new to the system, when they're not sure what foundation step to run next, or when a downstream skill is missing inputs and the creator needs to know which foundation skill produces them. Triggers on "set up my channel", "start my creator foundation", "what's the next foundation step", "where am I in the foundation", "I'm new to Authentic AI OS".
---

# Foundation

Thin orchestrator. Checks foundation state, points the creator at the next skill in the sequence. Doesn't run interviews itself.

The actual interview work happens in five focused skills:

1. `vid-avatar`. Offer plus avatar plus Top 3 perceived problems.
2. `vid-positioning`. Iceberg Statement.
3. `vid-pillars`. 8 to 12 content pillars.
4. `vid-credibility`. Three viewer-relevant brags.
5. `vid-backstory`. Problem-Action-Outcome backstory.

More skills are in development: voice capture, content production, pattern banks, packaging defaults. They will arrive in future plugin updates. This release ships the five foundation interview skills only.

## Contract

**Inputs (optional):** `foundation/creator-foundation.md`. Any state.

**Outputs:** none directly. This skill routes. The sub-skills produce.

## How this skill runs

### Step 1: Read state silently

Quiet read. Don't announce.

- `foundation/creator-foundation.md`: does it exist? Which sections are populated (Offer, Avatar, Top 3, Iceberg Statement, Pillars, Credibility, Backstory)?

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
| Backstory locked (foundation identity complete) | Foundation done. Acknowledge and stop. |

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

When all 5 foundation interview skills have locked their sections, congratulate briefly and stop:

> "Foundation complete. Your avatar, Iceberg, pillars, credibility, and backstory are locked. More skills are coming for voice capture, content production, and pattern research. For now, this is your foundation."

Do not invoke any further skill. The released foundation chain ends here.

## What this skill is NOT

- An interview skill. It doesn't ask the creator any of the foundation questions. Those live in the five sub-skills.
- A combined run. It doesn't run all five skills back-to-back. Each interview deserves a dedicated session.
- A refresh tool. If the creator wants to refresh a specific section, they run the sub-skill directly.

If the creator asks foundation questions during this skill ("can you write my Iceberg Statement?"), redirect:

> "That's `vid-positioning`'s job. It runs a focused session for the Iceberg Statement and saves it to `foundation/creator-foundation.md`. Want me to point you there?"

## Pre-check

Always read `foundation/creator-foundation.md` (silent). If it doesn't exist, the creator is at the start. If it exists, check which sections are populated to determine the next step.

## Anti-patterns

- Running any sub-skill's interview content here. This skill routes, not interviews.
- Reading the references inside `vid-avatar`, `vid-positioning`, etc. Those belong to their skills.
- Asking the creator to type the next command. Auto-invoke the next skill via the Skill tool.
- Continuing to invoke skills after a clear stop signal.
- Promising unreleased skills (voice capture, content production, pattern research) as immediate next steps. They are in development. Acknowledge them in the close, do not route to them.
- Surfacing jargon (Iceberg Statement, BENS, 3+1 rotation) without context. Translate when needed.

## References

None. This skill is route-only.
