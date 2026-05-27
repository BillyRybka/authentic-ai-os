---
name: foundation
description: Thin orchestrator for the Authentic AI OS foundation. Checks what's locked in creator-foundation.md and points the creator at the next skill in the foundation sequence. Use this when a creator is new to the system, when they're not sure what foundation step to run next, or when a downstream skill is missing inputs and the creator needs to know which foundation skill produces them. Triggers on "set up my channel", "run the foundation", "where am I in the foundation", or "what's next".
---

> 🔄 **Pre-flight (mandatory).** Before doing anything else, read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` and follow it. If a newer version exists, halt and tell the creator. If you're up to date, continue with the skill below.

# Foundation

Thin orchestrator. Checks foundation state, points the creator at the next skill in the sequence. Doesn't run interviews itself.

The actual interview work happens in five focused skills:

1. `vid-avatar`. Offer plus avatar plus Top 3 perceived problems.
2. `vid-positioning`. Iceberg Statement.
3. `vid-pillars`. 8 to 12 content pillars.
4. `vid-credibility`. Three viewer-relevant brags.
5. `vid-backstory`. Problem-Action-Outcome backstory.

More skills are in development: voice capture, content production, pattern banks, packaging defaults. They will arrive in future plugin updates. This release ships the five foundation interview skills only.

## Response format

Keep responses scannable. The creator should be able to skim and know what you're saying.

Break by idea. A new thought gets a new paragraph with a blank line above it. Walls of text don't get read.

Plain language. If the creator wouldn't say a word out loud, don't write it. Default to how they talk.

Lists go in bullets, not comma-separated runs inside a sentence.

### Bad

> "Your business is structured around a hybrid model combining consulting engagements with productized services, which creates revenue volatility because consulting hours fluctuate while productized commitments compound, and that's compounded by your team being optimized for delivery rather than acquisition, so even when leads come in there's no dedicated handler, meaning the funnel leaks at the top."

### Good

> "Your business mixes consulting with productized services.
>
> Consulting hours swing month to month. Productized work piles up. That makes revenue lumpy.
>
> The team is built to deliver, not to win new work. When leads show up, no one's handling them, so they fall out at the top.
>
> Where do you want to start?"

Same content. Broken by idea. Plain words. The creator can scan it in three seconds.

## Contract

**Inputs (optional):** `foundation/creator-foundation.md`. Any state.

**Outputs:** none directly. This skill routes. The sub-skills produce.

## How this runs

### Step 1: Read state silently

Two checks, in order. Both silent. Don't announce them. Only surface output if action is needed.

**Workspace check.** Verify the workspace is scaffolded at the current location:

- `foundation/` directory exists.
- Workspace `CLAUDE.md` exists at the same level.

If both present: continue to the foundation state check below.

If either is missing: tell the creator in one short line, then invoke `creator-setup` via the Skill tool. Don't continue with foundation's routing until creator-setup completes. Be honest about state — if `foundation/` exists but `CLAUDE.md` doesn't (or vice versa), name what's actually missing. Don't claim "not set up" if it's partially set up.

Shape (when nothing is set up):

> "Workspace isn't scaffolded here yet. Running `creator-setup` first to lay down the folder structure, then we'll pick up the foundation."

Shape (when partially set up, e.g. `foundation/` missing but `CLAUDE.md` exists):

> "Workspace is partially set up — I see `CLAUDE.md` but no `foundation/` folder. Running `creator-setup` to fix the structure before we go further."

Then immediately invoke `creator-setup` via the Skill tool. After it completes, the creator can re-invoke `/foundation` to start the interview chain.

**Foundation state check.** Read `foundation/creator-foundation.md` (silent). Does it exist? Which sections are populated (Offer, Avatar, Top 3, Iceberg Statement, Pillars, Credibility, Backstory)?

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

## What this is NOT

- An interview. It doesn't ask the creator any of the foundation questions. Those live in the five sub-skills.
- A combined run. It doesn't run all five skills back-to-back. Each interview deserves a dedicated session.
- A refresh tool. If the creator wants to refresh a specific section, they run the sub-skill directly.

If the creator asks foundation questions during this skill ("can you write my Iceberg Statement?"), redirect:

> "That's `vid-positioning`'s job. It runs a focused session for the Iceberg Statement and saves it to `foundation/creator-foundation.md`. Want me to point you there?"

## Anti-patterns

- Running any sub-skill's interview content here. This routes, not interviews.
- Reading the references inside `vid-avatar`, `vid-positioning`, etc. Those belong to their skills.
- Asking the creator to type the next command. Auto-invoke the next skill via the Skill tool.
- Continuing to invoke skills after a clear stop signal.
- Promising unreleased skills (voice capture, content production, pattern research) as immediate next steps. They are in development. Acknowledge them in the close, do not route to them.
- Surfacing jargon (Iceberg Statement, BENS, 3+1 rotation) without context. Translate when needed.
- Lying about workspace state. If `foundation/` or `CLAUDE.md` is missing, say so. Don't proceed as if everything's there.
