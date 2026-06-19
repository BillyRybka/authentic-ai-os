---
name: vid-title
description: Generate BENS-aligned title candidates for one video and lock 1 with the creator. Builds candidates from the creator's proven patterns in `banks/title-bank.md` and `banks/power-words-bank.md`, the video's specific material (brain-dump, framing, or script), and the BENS framework. Wide divergent pass, then a convergent cut. Anti-fabrication. Every claim backed by the script. Runnable standalone OR invoked by the orchestrator during the packaging phase (after framing, before structure). Triggers on "generate titles", "title options for [video]", "lock the title", "rename this video", or when a downstream pipeline needs a locked title.
---

# Video Title Generator

Generates BENS-aligned title candidates for one video, then locks one with the creator.

**Scope boundary:** this skill produces THE title only. It does not write thumbnails (that is `vid-thumbnail`), hooks (`vid-intro`), or scripts. If the creator wants thumbnail text too, they run `vid-thumbnail` separately or via the orchestrator.

## What this produces

A locked title for one video, saved to `content/pieces/{slug}/piece.md` (the `title:` field). The save happens in both standalone and pipeline mode. When invoked as a sub-skill by `vid-pipeline`, it also returns the title string to the caller for assembly awareness.

## When to run this

- A video is framed and needs its title locked before structure and scripting (the packaging step)
- Creator wants to re-title an existing piece based on a better read of the angle
- Orchestrator (`vid-pipeline`) invokes during the packaging phase, after framing and before structure

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists with avatar plus Top 3 problems (so candidates align with what the audience cares about)
- `foundation/packaging-system.md` exists with current packaging defaults and format guidance
- `content/pieces/{slug}/` exists with at minimum `piece.md` OR a brain-dump / framing artifact that explains what the video is about

If the foundation docs are missing, hard stop. Tell the creator to run `/foundation` first.

If `banks/title-bank.md` is missing, fall back to BENS-framework patterns plus the title-bank seed at `${CLAUDE_PLUGIN_ROOT}/skills/vid-research/assets/title-bank-template.md` (or `.claude/skills/vid-research/assets/title-bank-template.md` in the dev workspace). Note in the brief: "Title bank not yet scaffolded. Using seed patterns only." Without a real bank the output will skew generic, so say so.

## Invocation modes

**Standalone:** creator invokes directly. After lock, save the title to `content/pieces/{slug}/piece.md` and end.

**Sub-skill:** the orchestrator invokes mid-pipeline during packaging. The save to `piece.md` still happens here; also return the locked title string (and the BENS letters it hits) to the caller for assembly awareness.

If invoked with context from a caller (e.g. "title for video about X, format=case-study, locked angle=Y"), skip questions the caller has already answered and go straight to generation.

## The engine: build from proven patterns

The creativity lives in the creator's own researched winners, not in free-form invention. `banks/title-bank.md` holds fill-in-the-blank patterns, each with worked examples drawn from real outlier titles (and the channels and view counts behind them). `banks/power-words-bank.md` holds the words that move this audience, each with when-it-lands and when-it-fails notes. These two files are the source you generate FROM, not optional reference you glance at.

Most candidates should be a named bank pattern with its slots filled by this video's actual material, using power words selected by the land/fail criteria. Free-form BENS titles are allowed, but they are the minority. Lean on the patterns with the widest spread (used across the most channels) and the strongest worked examples first, because those are the most proven.

**This skill is a conversation, not a document.** Keep messages short. Do not paste bank contents or reference material into chat. The references are what you think with. The creator sees the candidate list and your recommendation.

## Phase 1: Load context and build the lock list

**Silent loads** (do NOT paste into chat):

1. `foundation/creator-foundation.md` (avatar, Top 3 problems, credibility brags)
2. `foundation/packaging-system.md` (format guidance, current packaging defaults)
3. `knowledge/BENS-framework.md` (Big / Easy / New / Safe rules and examples)
4. `banks/title-bank.md` (the patterns and worked examples you build from)
5. `banks/power-words-bank.md` (words selected by when-it-lands / when-it-fails, not by raw frequency)
6. `content/pieces/{slug}/piece.md` (the video's format, goal, pillar)
7. `content/pieces/{slug}/brain-dump.md` AND/OR `script.md`, whatever exists. Pull the actual angle, the specific numbers, named methods, story moments.
8. `banks/packaging-bank/*.md` filtered to `source: own`, if any exist. Past winning titles as style anchors for THIS creator.

**Build the lock list.** Every verifiable specific that actually appears in the material: numbers, dollar figures, percentages, timeframes, AND named methods, tools, products, frameworks, and people. Candidates may only use specifics from this lock list. If it is not in the material, it cannot go in a title.

**Name the avatar problem this video addresses** (1, 2, or 3 from creator-foundation). Candidates should hook into that problem.

**Read the format's natural BENS bias** from packaging-system:
- Case Study: S (specific receipts) plus B (transformation size)
- Short Process: E (achievable, defined steps) plus B
- Roast: N (contrarian) plus B
- Deep Dive: B plus N plus S (authority through depth)
- Interview: S (borrowed credibility) plus N (unexpected take)
- News: N (timely) plus B (stakes)
- Listicle: E (numbered, digestible) plus N

## Phase 2: Divergent pass (go wide, internal)

Generate a wide pool of rough title directions for your own thinking. Do NOT show this pool to the creator and do NOT polish it yet.

In this pass, go for spread, not finish:
- Pull from many DIFFERENT title-bank patterns, not your first favorite. Aim to touch at least 5 or 6 distinct patterns.
- Hit different angles: different problems from the Top 3, different BENS letters, different power words.
- Ignore the character ceiling and read-aloud polish for now. A clunky-but-fresh direction is worth keeping at this stage.

The one constraint that never relaxes, even here: anti-fabrication. Never invent a number, method, tool, or name. Everything still comes from the lock list.

Aim for roughly 15 to 20 rough directions. The point is to escape the safe center before any constraint pulls you back to it. If every direction rhymes, you have not gone wide enough; reach for patterns and power words you skipped.

## Phase 3: Convergent pass (bring constraints back, cut)

Now bring the constraints back and cut the pool down to the 5 to 8 strongest, polished candidates. Force them to be distinct from each other.

Each surviving candidate must:
- Use only specifics from the lock list (no fabrication)
- Aim for 50 characters or fewer, with 55 as the hard ceiling. The packaging-system checklist sets ~50 as the target, because punch and front-loading carry the click (mobile and search show fewer characters than the field allows). Flag any candidate of 51 to 55 as over target but allowed; cut anything over 55 unless it is clearly the strongest, in which case surface it and say why.
- Hit at least one BENS letter (annotate which)
- Pass the read-aloud test (below)
- Carry one specific element that makes it impossible to paste onto another video. If you cannot name that element, the candidate is generic; cut it or pull a sharper specific from the material.

**Diversity of the final set:** the 5 to 8 should draw from at least 3 distinct title-bank patterns, and no more than 2 should share the same primary BENS letter. This is what stops the list from being one idea reworded.

**The read-aloud test (the primary gate).** A title must read as one continuous thought spoken in natural English. Say it out loud. If it sounds like a person said it in conversation, it passes. If it sounds like fragments stitched together, cut it.

Examples that PASS (real published titles):
- "How I Added 55 Pounds To My Squat In 12 Weeks" (one breath, one thought)
- "I QUIT My $120,000 Job After Learning 3 Things" (natural complex sentence)
- "Why Looking Poor Is Important" (short, complete claim)
- "I Made $12M Selling A Fruit" (subject plus verb plus specific)
- "The 21 Principles of the Top 0.01%" (defined number plus specific group, one phrase)
- "Top 10 Most HARMFUL Foods People Keep EATING" (superlative plus specific group, flows)

Examples that FAIL (and why):
- "365 To 405 In 11 Weeks (3 Changes)" (three fragments plus a tag-on parenthetical, no human says this)
- "I Hired A VA. Revenue Dropped 30%." (a mid-title period splits it into two failed sentences)
- "The Pause Squat Rule That Unsticks 365s" ("Unsticks 365s" is an invented compound, not English)
- "The 12-SOP Rule" ("12-SOP" is a label, not a duration. Compare "The 90 Minute Rule", where "90 minute" describes time and reads as a system)

**Two more hard cuts** (genuinely broken, not preference):
- **Invented compound nouns.** "Unsticks 365s", "100xs your X". If the phrase returns nothing when you imagine searching it, it is not real language. Cut.
- **AI-default openers.** "The truth about", "Everything you need to know about", "Why you should", "The ultimate guide to", "Discover the secret to", and vague benefit stacks ("faster, easier, better"). These are the on-distribution center the model drifts toward. They could front a thousand videos. Cut and pull a real specific from the material instead.

Everything else (hedge words, stock phrases, colons, parentheticals, credibility-mismatch, number-stuffing, and the rest) is soft friction: it tends to under-perform but the creator may have a reason. Flag it in the annotation and let them decide. The full soft-filter catalog, the natural-language pattern shapes, and the deeper craft notes live in `references/title-filters.md`. Load it when you are judging an edge case or want to widen the divergent pass; do not paste it into chat.

**Final check before you present.** Run the surviving set through these gates and fix any miss before the creator sees it. These enforce the rules above, which are easy to state and easy to skip under generation pressure.

- Every candidate is 55 characters or fewer. Rewrite or cut any that run over.
- No more than 2 candidates share the same primary BENS letter. If 3 or more share one (case-study sets drift to B and S), swap one for a different pattern and a different letter so the set spans the avatar's angles, not just the obvious one.
- A clear majority are built from a named title-bank pattern, not free-form. For a set of 5, at least 4 should name a pattern. Free-form is the minority, not the filler.
- The candidate you will recommend carries a lock-list specific that makes it impossible to paste onto another video. "Claude Cowork Can Now Run Without You" is weaker than "Claude Cowork Scheduled Agents Run Without You" because the first drops the one detail (the named feature) that ties it to this video. If your top pick is generic on that test, sharpen it or pick another.

## Phase 4: Present with a recommendation

Show the surviving candidates as a numbered list. For each: the title, the bank pattern it came from (or "free-form"), the BENS letters, and the character count. Where a soft filter fired, name it in one short clause so the creator sees the option and the concern together.

Present as a creative partner with a point of view, not a stenographer. Lead with your pick and one sentence on why it is the strongest for this video and this avatar. Example shape:

```
My pick: 3. It is the only one that names the $1.3M number and reads in one breath.

1. "I Hired A VA. Then Lost 30% Revenue"        free-form        B+S  (47)
2. "Don't Hire Until You Have These 12 SOPs"    DON'T-do-instead  E+N  (43)
3. "The Mistake That Cost Me 6 Weeks Of Revenue" cost-me-pattern  B+N  (44)
4. "Why Your First VA Hire Tanks Revenue"        Why-X-is         B+N  (40)
```

Then ask:

> "Which one? Or want me to go wider, push a different problem, or hit different BENS letters?"

Wait for the creator. If they pick, go to Phase 5.

If they want changes:
- "Different angle" means re-run the divergent pass weighted toward a different audience problem or angle
- "Different BENS" means weight toward the letters they want (e.g. more N, less B)
- "Shorter" means re-cut under 40 characters
- "More specific" means pull more lock-list specifics into the candidates
- "Scrap it" means re-run Phase 1, often with the creator pasting new framing

**Push back when a pick is weak:**
- Generic pick ("How To Build A Business"): "That would fit a thousand videos. Want me to anchor it to the $1.3M number or the named method from the script?"
- Fabricated number: refuse and explain. Only lock-list specifics are allowed.
- Over the ceiling with no good reason: flag it and offer a tighter cut.

## Phase 5: Lock and save

Once picked, save in BOTH modes. The `title:` field is how the pipeline knows packaging advanced, so the write always happens here; never hand it to the caller:
- Save the title to `content/pieces/{slug}/piece.md` `title:` field
- Bump `piece.md` `last_updated:` to today's date
- Confirm: "Title locked: '{title}'. Saved to piece.md."

**Sub-skill mode** also returns the title string (and the BENS letters it hits) to the caller for assembly. The piece.md write above still happens here regardless of mode.

**Stop.** Do not generate the thumbnail, hook, or script. Those are different skills.

## Anti-fabrication discipline

Every number, name, method, tool, framework, or specific phrase in a title MUST trace to the script, brain-dump, or foundation docs. If it is not in the material, the title cannot claim it. This holds in the divergent pass too: going wide means trying more real angles, never inventing facts.

If the creator wants a number-driven title and the material has no usable number, kick it back: "The script has no number to ground this. Either drop the number-driven angle or add the number to the script first." Same rule as `vid-thumbnail`, kept consistent across the writing skills.

## Title and thumbnail pairing

Title and thumbnail pair eventually (`vid-thumbnail` produces the thumbnail text), and they should not repeat words. If `vid-thumbnail` has already produced a `thumbnail-brief.md` for this piece, read its picks and avoid repeating their key words in the title.

If `vid-thumbnail` has not run yet, just lock the title. The thumbnail will respect the title's lock-words later (the rule lives in `knowledge/thumbnail-text-patterns.md`). vid-title runs first; it does not wait on the thumbnail.

## Principles

- **Build from the bank, not from a blank page.** The proven patterns and power words are the engine. Free-form is the minority.
- **Go wide before you cut.** The divergent pass is where freshness comes from. Skipping it is why title lists drift into one idea reworded.
- **Specificity wins.** Real numbers over round numbers. Named methods over generic verbs. A specific person or situation over "people."
- **Fit the video AND the avatar.** A title that fits the video but not the avatar misses. One that fits the avatar but misreads the video is bait. Both must hold.
- **Read aloud is the voice test.** If the creator would reword it speaking it, it is wrong.
- **Creator drives, Claude structures.** Never invent claims to make a title sound bigger.

## Reference index

- `knowledge/BENS-framework.md`: Big / Easy / New / Safe rules and examples
- `banks/title-bank.md`: the patterns and worked examples you build from
- `banks/power-words-bank.md`: words selected by when-it-lands / when-it-fails
- `references/title-filters.md`: the full soft-filter catalog, natural-language pattern shapes, and craft notes (load on demand)
- `vid-research/assets/title-bank-template.md`: fallback patterns if the bank is not scaffolded
- `foundation/creator-foundation.md`: avatar, Top 3 problems
- `foundation/packaging-system.md`: format guidance, packaging defaults
- `content/pieces/{slug}/*`: the video's actual material
- `banks/packaging-bank/*.md` (own): past winning titles as style anchors

## Related skills

- The `/foundation` chain produces `creator-foundation.md`; `vid-research` produces `packaging-system.md`, `title-bank.md`, and `power-words-bank.md`, the files this skill builds from
- `vid-thumbnail` pairs with this skill; coordinate to avoid word repeats
- `vid-framing` runs before this skill and locks the angle plus format the title is built on
- `vid-ideas` may have surfaced a provisional working title. If `piece.md` carries one, treat it as a single input candidate, not a locked answer. This skill does the real craft and is free to beat it or discard it.
- `vid-pipeline` (future) orchestrates and calls this skill during packaging
- `vid-measurement` (future) does post-publish analysis and logs winning titles back into `banks/title-bank.md` and `banks/packaging-bank/`
