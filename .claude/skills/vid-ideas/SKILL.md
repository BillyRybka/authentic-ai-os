---
name: vid-ideas
description: Generate a small batch of signal-backed video ideas for a creator who is blank on what to make next. Reads the creator's iceberg, content pillars, avatar, and Top 3 problems plus the pattern-bank (proven outliers = what worked), filters every idea through the iceberg, and proposes ~5-6 ideas, mostly anchored to real proven signals with 1-2 experimental swings. The creator picks one to make now, flags any others they like (those save to content/ideas-backlog.md), and the picked idea hands a seed to vid-intake. In-session dial: more / tighter / wilder / different pillar re-rolls the batch. Anti-fabrication, every anchored idea cites a real pattern-bank entry. Optional front-door of the pipeline; skip it when the creator already knows what to make. Use this skill whenever a creator does not know what video to make. Phrases like "I don't know what to make", "give me video ideas", "what should I make a video about", "I'm out of ideas", "what's next for my channel", "help me come up with a video", "ideate", "generate some ideas", "I'm blank on content", or any moment the creator needs a topic before vid-intake should fire this skill.
---

# Video Ideas

Generates a small batch of video ideas for the blank-slate moment, grounded in the creator's positioning and in the evidence of what has actually worked. Reads the iceberg, pillars, avatar, and Top 3 problems plus the pattern-bank, proposes ~5-6 signal-anchored ideas, lets the creator turn a dial until the batch lands, then hands the picked idea to `vid-intake`.

**Scope boundary:** this skill picks WHAT video to make (the topic), from a blank slate or the backlog. It does NOT pick the angle (`vid-framing`), capture raw material or create the piece folder (`vid-intake`), craft the final title (`vid-title`) or thumbnails (`vid-thumbnail`), or write any script. It surfaces each idea as a short line wearing the borrowed shape, with the real outlier receipt, as a seed for judging the idea; `vid-title` crafts the real title later from the captured material. This skill hands the chosen idea seed to `vid-intake` and stops.

> **Resolving `knowledge/` and skill paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load the repo-relative path instead. The same applies to skill references named `.claude/skills.../...`.

## What this produces

- A surfaced batch of ~5-6 video ideas in chat. Each leads with the real outlier receipt it borrows (title + @channel + views + xMed), and is tagged to a pillar, its signal tier, and an iceberg-fit verdict, with an optional Top 3 problem tag where one genuinely fits (or flagged as an experimental swing).
- `content/ideas-backlog.md`, created from `assets/ideas-backlog-template.md` on the first keep. Only ideas the creator flags to keep are saved (status `kept`). Dropped backlog ideas are marked `dropped` and never re-proposed.
- A seed packet handed to `vid-intake` for the one idea the creator picks to make now: `{idea_title, pillar, top_3_problem, iceberg_fit, anchor}`. This skill writes no piece folder; `vid-intake` creates it.

## When to run this

- The creator does not know what video to make and wants options
- The creator wants to refill their idea queue from what is working in the niche
- The creator wants to revisit kept ideas from `content/ideas-backlog.md`
- NOT when the creator already has a topic. Send them straight to `vid-intake`.

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists with the iceberg statement, content pillars, avatar, and Top 3 problems. If missing, hard stop: "No foundation docs. Run `/foundation` first so I know your positioning and audience."
- `banks/pattern-bank.md` exists (the signal source). If missing, hard stop: "No pattern bank yet. Run `vid-research` first so ideas can anchor to what actually works, first build takes ~1.5 hours. I can still range off your pillars alone if you want, but the ideas will be guesses, not signals."

Soft requirements:
- `content/ideas-backlog.md` (loaded if present, for prior keepers and sticky drops)
- `foundation/packaging-system.md` (read only to know the creator's active format rotation, so an idea can hint at a fitting format; never required)

## Invocation modes

**Standalone:** the creator invokes directly. Run the full flow, loop the dial, save keepers, hand the picked idea to `vid-intake`.

**Sub-skill:** `vid-pipeline` (future) may invoke this at the very start of the SCRIPT phase when the creator has no piece yet. Return the picked idea seed packet to the caller instead of invoking `vid-intake` directly.

## The 4 phases

### Phase 1: Lean load and focus

**Silent loads** (do NOT paste into chat). Load ONLY these, and only the named slices. This skill stays lean on purpose.

1. `foundation/creator-foundation.md`, but only: the **Iceberg Statement**, the **Content Pillars** list, the **Avatar** description, and the **Top 3 problems**. Skip credibility, backstory, offer.
2. `banks/pattern-bank.md`: the **Synthesis** sections (convergent / niche-specific / adjacent / unique), **Confirmed winners**, and **Considered + dropped** for orientation (which shapes have spread, what is on-lane), AND the **per-channel raw outlier rows** (the actual winning titles + views + xMed). You generate from the raw titles, not the labels, so the rows are working material, not just citations. The Synthesis is the map; the raw titles are the evidence you decompose.
3. `content/ideas-backlog.md` if it exists, for prior keepers (surface them) and dropped entries (never re-propose).
4. `references/idea-generation-rules.md`, the signal-anchoring, anti-skew, and posture-dial logic. This is your thinking, not chat content.
Do NOT load voice-profile, reference-pieces, BENS, or the title / power-words / thumbnail banks. This skill proposes ideas, not titles, and loads no title source.

**Then ask one short question:**

> "Want me to range across all your pillars, or do you have a direction in mind (a pillar, a theme, or one of your audience's Top 3 problems)?"

A focus narrows generation to that pillar / theme / problem. No focus ranges broadly across the pillars. If `ideas-backlog.md` has keepers, mention it: "You also have {N} kept ideas in the backlog. Want those in the mix?"

### Phase 2: Generate the batch

Generate ~5-6 ideas per `references/idea-generation-rules.md`. Default mix: 4 anchored to proven raw titles, plus 1-2 experimental swings, clearly flagged. Build and vet one idea at a time, then surface the set.

**The spine (per `idea-generation-rules.md`):**
1. **Work from a raw winning title**, not a Synthesis label. Open the per-channel rows.
2. **Name why it won:** the one load-bearing element that drove the multiple (e.g. the kicker "(No Employees)", not the abstract "control").
3. **Carry that engine onto the creator's topic**, bounded both ways: the engine must survive (fidelity floor) and the line must not be the source with its nouns swapped (transcribe ceiling). Rebuild the surface phrasing fresh; numbers stay placeholders.
4. **Click test:** put it next to the others, would the avatar click THIS, and why. A dream outcome beats a defensive reassurance. On-brand is the floor, not the pull. Do not staple the positioning ("without the slop") onto a title where voice is not the premise.
5. **Fit is a floor, checked last:** inside the iceberg = pass, off-iceberg never surfaces. Range across 3-4 pillars. A Top 3 problem is an optional tag, never forced.

Each idea surfaces with exactly this shape (keep it tight, no walls of text). Lead with the receipt:

> **{the idea as one short line, carrying the engine of a real winning title, in the creator's voice}**
> inspired by: "{real outlier title}" (@{channel}, {views}, {xMed}x median)
> Pillar: {pillar} | Iceberg: {one-phrase fit verdict} | Signal: {STRONG | MODERATE | swing} | Problem: {1 | 2 | 3, or omit if none fits}
> Why it could land: {one line on why a human clicks this: the engine carried, plus the avatar's want}

For an experimental swing with no proven anchor, replace the receipt with `swing: {the adjacent-niche or weaker outlier it gestures at}, unproven for this channel`.

**Anti-fabrication (hard rule):** every anchored idea cites a REAL per-channel row (actual title + @channel + views + xMed), and the cited engine must actually be the one carried into the line. Never invent an outlier, a view count, or a spread, and never cite a row you did not use. Swings are flagged unproven, never dressed up as proven.

**Fit gate:** use the iceberg layer of `knowledge/iceberg-and-top-3-alignment.md`. Only surface ideas inside the iceberg; never surface an off-iceberg idea. Top 3 fit is an optional tag, not a gate, and not a reason to stamp an idea `outlier`.

### Phase 3: Adjust and pick (the dial)

Present the batch, then offer the dial in one line:

> "Pick the one to make now. Flag any others you want to keep. Or turn the dial: 'more', 'tighter' (safer, higher signal), 'wilder' (more original swings), 'different pillar', or 'regenerate'."

Act on the creator's call:
- **Pick** -> go to Phase 4 with that idea.
- **Keep flags** -> note them for Phase 4 save.
- **Dial** -> re-roll the batch with the new posture (see `references/idea-generation-rules.md` for what each posture changes). Loop until the creator picks.

Do not over-talk between rolls. Surface the new batch, repeat the one-line dial offer.

### Phase 4: Save keepers and hand off

1. **Save keepers.** For each idea the creator flagged to keep (but is not making now), append a row to `content/ideas-backlog.md` (create it from `assets/ideas-backlog-template.md` on the first keep) with status `kept`, today's date, pillar, problem, and anchor. Do NOT save the unflagged ideas. If the creator explicitly drops a backlog idea, set its status to `dropped` (sticky, never re-proposed).
2. **Hand off the pick.** Pass the seed packet `{idea_title, pillar, top_3_problem, iceberg_fit, anchor}` to `vid-intake`. Tell the creator: "Handing this to `vid-intake` to capture what you'd actually say. It'll drill you for the material and build the brain dump." `vid-intake` runs its idea+dump flow seeded from this packet and creates the piece folder. This skill creates no piece folder.
3. If the picked idea came FROM the backlog, set that backlog row's status to `picked`.

## Conversational discipline

- **Conversation, not a document.** Short messages. Never paste the pattern-bank or foundation into chat. The loads are for your thinking.
- **Signal over volume.** Five or six sharp ideas beat ten mushy ones. The creator's worry is crappy ideas, so every anchored idea earns its place by citing a real signal.
- **Specificity wins.** Each idea is a concrete topic in the creator's voice, not a category ("a video about pricing" is not an idea, "the pricing mistake that makes clients ghost you after the proposal" is).
- **The dial is the creator's, not yours.** Re-roll on request without arguing. If they want wilder, go wilder. If the swings flop, they will tell you.
- **Carry the engine, never the words.** Work from the raw winning title. Name the one load-bearing element that drove its multiple, then carry THAT onto the creator's topic. The engine must survive (fidelity floor) but the line must not be the source with its nouns swapped (transcribe ceiling). A summary label is not the engine; the title is.
- **Run the click test.** Before surfacing, ask which of these a human actually clicks, and why. A dream outcome beats a defensive reassurance. Never bend a title toward the creator's positioning to feel on-brand; on-brand is the floor, not the pull.

## Hard friction (stop and flag)

- Foundation or pattern-bank missing: hard stop per Prerequisites.
- An idea you cannot anchor to a real signal AND that is not flagged as an experimental swing: do not surface it. Anchor it, flag it as a swing, or drop it.
- An anchored idea whose receipt's engine you did not actually carry into the line: that is a fake citation. Re-roll it so the borrowed engine is visible, or drop the receipt and flag it a swing.
- An off-iceberg (NO/NO) idea: do not surface it. If the creator insists the iceberg has shifted, point them at `/foundation` to refresh positioning first.

## Soft friction (surface and let the creator decide)

- Pattern-bank older than ~120 days: "Your pattern bank is {N} days old, so the signals may be stale. Want to refresh with `vid-research` first, or proceed?"
- A strong idea anchored to a `Considered + dropped` pattern: do not silently use it. Surface the drop rationale and ask if the creator wants to reconsider.
- Every surfaced idea lands on the same pillar or problem: flag the narrowness and offer to range wider.

## Reference index

| File | When to read it |
|------|-----------------|
| `references/idea-generation-rules.md` | Phase 2 + Phase 3. Signal-anchoring rules, the anti-skew guards, and what each dial posture changes. |
| `assets/ideas-backlog-template.md` | Phase 4. The `content/ideas-backlog.md` file shape, created on first keep. |
| `knowledge/iceberg-and-top-3-alignment.md` | Phase 2. The iceberg 2-layer fit check + 4 outcomes. Reuse, do not duplicate. |
| `knowledge/theory-of-one-curation.md` | Phase 2. The audience-fit lens when an anchor works everywhere but may not fit this creator. |

## Principles (the why)

- **The blank page is the real failure point.** Most creators stall before intake, not during it. A front-door that turns positioning + evidence into a few concrete options removes the stall.
- **Ideas anchored to evidence beat ideas from the gut.** The pattern-bank is the record of what audiences actually click and watch. Anchoring ideas to it is the difference between a hypothesis and a guess.
- **Originality is a deliberate slice, not the default.** Proven-only ideas make a derivative channel. The 1-2 swings are where the channel's voice gets to gamble, on purpose, flagged as unproven.
- **A kept idea is never lost; a bad idea is never hoarded.** Save only what the creator likes, so the backlog stays a queue worth opening, not a junk drawer.

## Related skills

- The `/foundation` chain produces `creator-foundation.md` (iceberg, pillars, avatar, Top 3) this skill reads
- `vid-research` produces `banks/pattern-bank.md`, the signal source this skill anchors ideas to
- `vid-intake` receives the picked idea seed and captures the brain dump (this skill's downstream handoff)
- `vid-framing` runs after intake and picks the angle (this skill picks the topic, not the angle)
- `vid-title` owns ALL title craft. The idea line this skill surfaces is a provisional seed (a borrowed proven shape), never a crafted title; `vid-title` writes the real title later from the captured material. vid-ideas loads no title source.
- `vid-pipeline` (future) may invoke this at the start of the SCRIPT phase when no piece exists yet
- `vid-measurement` (future) will feed published performance back into the pattern-bank's Confirmed winners, sharpening this skill's signals over time
