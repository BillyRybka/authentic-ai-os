---
name: foundation
description: Thin orchestrator for the Authentic AI OS foundation. Checks what's locked across the foundation files (offer, avatar, iceberg, credibility, backstory, voice) and points the creator at the next skill in the foundation sequence. Use this when a creator is new to the system, when they're not sure what foundation step to run next, or when a downstream skill is missing inputs and the creator needs to know which foundation skill produces them. Triggers on "set up my channel", "run the foundation", "where am I in the foundation", or "what's next".
---

# Foundation

Thin orchestrator. Checks foundation state, points the creator at the next skill in the sequence. Doesn't run interviews itself.

The actual work happens in six focused skills:

1. `vid-avatar`. Offer plus avatar plus Top 3 perceived problems.
2. `vid-positioning`. Iceberg Statement.
3. `vid-pillars`. 8 to 12 content pillars.
4. `vid-credibility`. Three viewer-relevant brags.
5. `vid-backstory`. Problem-Action-Outcome backstory.
6. `vid-voice-capture`. Reference pieces (the real passages every writing skill drafts from) plus the guardrail.

The first five are interviews and auto-advance into each other. Voice capture needs the creator to bring real material, so it is offered at the close of step 5 and launched only on their go.

Once voice is captured the foundation is complete, and this skill offers `vid-research`. Content production skills are still in development and arrive in future updates.

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

**Inputs (optional):** the five foundation files (`foundation/offer.md`, `foundation/avatar.md`, `foundation/iceberg.md`, `foundation/credibility.md`, `foundation/backstory.md`), plus `foundation/voice-profile.md` and `foundation/reference-pieces/`. Any state. A legacy `foundation/creator-foundation.md` triggers the migration flow in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`.

**Outputs:** none directly. This skill routes. The sub-skills produce.

## How this runs

### Step 1: Read state silently

Four checks, in order. All silent. Don't announce them. Only surface output if action is needed.

**Workspace check.** Verify the workspace is scaffolded at the current location:

- `foundation/` directory exists.
- Workspace `CLAUDE.md` exists at the same level.

If both present: continue to the foundation state check below.

If either is missing: tell the creator in one short line, then invoke `creator-setup` via the Skill tool. Don't continue with foundation's routing until creator-setup completes. Be honest about state. If `foundation/` exists but `CLAUDE.md` doesn't (or vice versa), name what's actually missing. Don't claim "not set up" if it's partially set up.

Shape (when nothing is set up):

> "Workspace isn't scaffolded here yet. Running `creator-setup` first to lay down the folder structure, then we'll pick up the foundation."

Shape (when partially set up, e.g. `foundation/` missing but `CLAUDE.md` exists):

> "Workspace is partially set up. I see `CLAUDE.md` but no `foundation/` folder. Running `creator-setup` to fix the structure before we go further."

Then immediately invoke `creator-setup` via the Skill tool. After it completes, the creator can re-invoke `/foundation` to start the interview chain.

**Migration check.** If `foundation/creator-foundation.md` exists, the breakup into the five foundation files hasn't finished. Follow `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`: with any split file missing it asks upgrade, enhance, or start fresh and waits for the creator's pick; with all five present it finishes the breakup without asking. Either way the content moves first, gets verified in the five files, and only then is the original deleted. Continue once it's gone.

**Foundation state check.** Read the five foundation files (silent): `foundation/offer.md`, `foundation/avatar.md`, `foundation/iceberg.md`, `foundation/credibility.md`, `foundation/backstory.md`. Which exist, and which sections are populated vs still `[pending ...]` (Offer, Avatar, Top 3, Iceberg Statement, Machinery, Pillars, Credibility, Backstory)?

**Voice check.** Voice is captured when `foundation/voice-profile.md` exists AND `foundation/reference-pieces/` holds at least one file. Check both. The guardrail alone is not a voice: the reference pieces are the passages the writing skills draft from, so a profile with an empty reference-pieces folder counts as not captured.

### Step 2: Map state to next skill

Use this routing table:

| State | Next skill to invoke |
|---|---|
| Nothing exists | `vid-avatar` |
| `offer.md` or `avatar.md` missing or partial | `vid-avatar` |
| Avatar locked, Iceberg Statement or Machinery missing or pending in `iceberg.md` | `vid-positioning` |
| Iceberg Statement locked, Content pillars pending in `iceberg.md` | `vid-pillars` |
| Content pillars locked, `credibility.md` missing or pending | `vid-credibility` |
| Credibility brags locked, `backstory.md` missing or pending | `vid-backstory` |
| Backstory locked, voice not captured | Identity complete. Acknowledge, then offer `vid-voice-capture` (Step 5). |
| Voice captured (guardrail plus at least one reference piece) | Foundation complete. Acknowledge, then offer `vid-research` (Step 6). |

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

### Step 5: Identity locked, then offer voice capture

When all 5 interview skills have locked their sections, congratulate briefly, name what is still missing, and offer step 6:

> "Foundation's locked. Avatar, Iceberg, pillars, credibility, backstory.
>
> One thing left. The system knows who you're talking to and what you stand for. It doesn't know what you sound like.
>
> That's `vid-voice-capture`. It takes real passages you've already written or said and turns them into the reference every writing skill drafts from. Bring something you wrote, a transcript, anything in your own words.
>
> Want to do that now, or come back to it?"

If the creator says yes, invoke `vid-voice-capture` via the Skill tool. If they want to wait, respect it and close.

Never fire voice capture without the go. The other five run on conversation alone; this one needs material in hand, and launching into it empty wastes the session.

### Step 6: Foundation complete, then offer vid-research

When voice is captured (guardrail plus at least one reference piece), the foundation is done:

> "Foundation complete. Who you're for, what you stand for, and what you sound like.
>
> The natural next step is `vid-research`. It builds your pattern banks from real YouTube data, what's actually working in your niche, so the videos you plan are grounded in evidence instead of guesses. It runs a real session, so do it when you have the time.
>
> Want to start it now, or come back to it later?"

If the creator says yes (or any clear go), invoke `vid-research` via the Skill tool.

If they want to wait, respect it and close. A completed journey is also a natural moment for feedback: if the `aai-feedback` skill is available, offer it once via the end-of-journey path in `${CLAUDE_PLUGIN_ROOT}/knowledge/feedback-offer.md` (honor its once-per-session guard), and invoke `aai-feedback` only if the creator has something to say.

Content production is still in development; do not route to it. After voice, `vid-research` is the only skill to offer.

## What this is NOT

- An interview. It doesn't ask the creator any of the foundation questions. Those live in the five sub-skills.
- A combined run. It doesn't run all six skills back-to-back. Each session deserves its own sitting.
- A refresh tool. If the creator wants to refresh a specific section, they run the sub-skill directly.

If the creator asks foundation questions during this skill ("can you write my Iceberg Statement?"), redirect:

> "That's `vid-positioning`'s job. It runs a focused session for the Iceberg Statement and saves it to `foundation/iceberg.md`. Want me to point you there?"

## Anti-patterns

- Running any sub-skill's interview content here. This routes, not interviews.
- Reading the references inside `vid-avatar`, `vid-positioning`, etc. Those belong to their skills.
- Asking the creator to type the next command. Auto-invoke the next skill via the Skill tool.
- Continuing to invoke skills after a clear stop signal.
- Promising genuinely unreleased skills (content production) as next steps. They are in development; acknowledge them, do not route to them. `vid-voice-capture` and `vid-research` HAVE shipped: offer each at its own close and launch on consent (Steps 5 and 6).
- Surfacing jargon (Iceberg Statement, BENS, 3+1 rotation) without context. Translate when needed.
- Lying about workspace state. If `foundation/` or `CLAUDE.md` is missing, say so. Don't proceed as if everything's there.
