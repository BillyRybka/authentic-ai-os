---
name: vid-title
description: Generate 5-10 BENS-aligned title candidates for one video and lock 1 with the creator. Pulls from creator-specific patterns in `banks/title-bank.md`, the video's specific material (brain-dump or framing artifact), and the BENS framework. Anti-fabrication. Every claim must be backed by the script. Runnable standalone OR invoked by `vid-structure` during the structure phase. Triggers on "generate titles", "title options for [video]", "lock the title", "rename this video", or when a downstream pipeline needs a locked title.
---

# Video Title Generator

Generates BENS-aligned title candidates for one video. Three phases: load context, present candidates, creator picks, save.

**Scope boundary:** this skill produces THE title only. It does not write thumbnails (that's `vid-thumbnail`), hooks (`vid-intro`), or scripts. If the creator wants to also generate thumbnail text, they run `vid-thumbnail` separately or via the orchestrator.

## What this produces

A locked title for one video, saved to `content/pieces/{slug}/piece.md` (the `title:` field). When invoked as a sub-skill by `vid-structure` or `vid-pipeline`, returns the title string to the caller instead.

## When to run this

- A video is in framing/structure phase and needs a title before the script gets written
- Creator wants to re-title an existing piece based on better understanding of the angle
- Orchestrator (vid-pipeline) invokes during STRUCTURE phase

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists with avatar plus Top 3 problems (so candidates align with what the audience cares about)
- `foundation/packaging-system.md` exists with current packaging defaults and format guidance
- `content/pieces/{slug}/` exists with at minimum `piece.md` OR a brain-dump / framing artifact that explains what the video is about

If the foundation docs are missing, hard stop. Tell the creator to run `vid-foundation` first.

If `banks/title-bank.md` is missing, fall back to using BENS-framework patterns directly plus the title-bank seed at `${CLAUDE_PLUGIN_ROOT}/skills/vid-foundation/assets/title-bank-seed.md` (or in the current dev workspace, `assets/title-bank-seed.md`). Note in the brief: "Title bank not yet scaffolded. Using seed patterns only."

## Invocation modes

**Standalone:** creator invokes directly. After lock, save the title to `content/pieces/{slug}/piece.md` and end.

**Sub-skill:** another skill (vid-structure, vid-pipeline) invokes mid-pipeline. Skip the save step; return the locked title string to the caller. The caller writes it to piece.md as part of its own flow.

If invoked with context from a caller (e.g. "title for video about X, format=case-study, locked angle=Y"), skip questions the caller has already answered and go straight to candidate generation.

## The walkthrough (3 phases)

**This skill is a conversation, not a document.** Keep messages short. Never dump reference content into chat. The references (BENS, title-bank, the video's material) are for YOUR thinking. Pull from them selectively. Same hard rules as `vid-thumbnail`: no fabrication, specificity wins, pull-from-script-only.

### Phase 1: Load context and generate candidates

**Silent loads** (do NOT paste into chat):

1. `foundation/creator-foundation.md` (avatar, Top 3 problems, credibility brags)
2. `foundation/packaging-system.md` (format guidance, current packaging defaults)
3. `knowledge/BENS-framework.md` (Big / Easy / New / Safe rules and examples)
4. `banks/title-bank.md` (fill-in-the-blank title patterns, research + creator-curated in one file)
5. `banks/power-words-bank.md` (global + audience-specific words. Loaded for word selection when filling pattern slots and writing fresh titles. Use the when-it-lands / when-it-fails criteria for fit, not raw word frequency)
6. `content/pieces/{slug}/piece.md` (the video's format, goal, pillar)
7. `content/pieces/{slug}/brain-dump.md` AND/OR `piece.md` AND/OR `script.md`. Whatever exists. Pull the actual angle, the specific numbers, named methods, story moments.
8. `banks/packaging-bank/*.md` (filtered to `source: own`). Past winning titles, used as style anchors for what works for THIS creator.

**Build the lock list:** every number, dollar figure, percentage, timeframe, named method that actually appears in the script. Title candidates may ONLY use numbers from this lock list. No fabrication.

**Identify the avatar's top problem this video addresses** (1, 2, or 3 from creator-foundation). Title candidates should hook into that problem.

**Identify the format's natural BENS bias** from packaging-system:
- Case Study: S (specific receipts) plus B (transformation size)
- Short Process: E (achievable, defined steps) plus B
- Roast: N (contrarian) plus B
- Deep Dive: B plus N plus S (authority through depth)
- Interview: S (borrowed credibility) plus N (unexpected take)
- News: N (timely) plus B (stakes)
- Listicle: E (numbered, digestible) plus N

**Generate 5-10 candidates** drawing from:
- `banks/title-bank.md` patterns (fill in the variables with the video's actual material)
- Free-form titles that follow BENS but aren't pattern-derived
- Past creator-own winners in packaging-bank as style anchors (if any)

Each candidate must:
- Be 50 characters or fewer (hard ceiling, YouTube cuts off after 50)
- Hit at least one BENS letter (annotate which)
- Use ONLY numbers from the lock list (no fabrication)
- Be distinct from the others (different patterns, different BENS letters, different angles)

**THE primary filter: read aloud test.** A title must read as ONE continuous thought spoken in natural English. Read it out loud. If it sounds like a human said it in conversation, it passes. If it sounds like fragments stitched together, REJECT.

Examples that PASS the read-aloud test (real published titles):
- "How I Added 50 Pounds To My Squat In 12 Weeks" (one breath, one thought)
- "I QUIT My $120,000 Job After Learning 3 Things" (natural complex sentence)
- "Why Looking Poor Is Important" (short, complete claim)
- "I Made $12M Selling A Fruit" (subject plus verb plus specific)
- "Why You Should Eat Chocolate Every Day" (conversational, complete)
- "The 21 Principles of the Top 0.01%" (defined number plus specific group, one phrase)
- "Top 10 Most HARMFUL Foods People Keep EATING" (superlative plus specific group, flows)

Examples that FAIL (and would be rejected):
- "365 To 405 In 11 Weeks (3 Changes)" (three fragments plus a clutter parenthetical, no human says this)
- "I Hired A VA. Revenue Dropped 30%." (mid-title period creates two failed sentences, real titles don't punctuate like this)
- "Stop Hiring VAs. Start With 12 SOPs." (same problem, two commands jammed together)
- "The Pause Squat Rule That Unsticks 365s" ("Unsticks 365s" is invented compound noun, not English)
- "The 12-SOP Rule" ("12-SOP" is a count, not a duration, compare "The 90 Minute Rule" where "90 minute" describes time and reads as a system, while "12-SOP" reads as a label/stat)
- "Numbers Smashed Together In A Sentence Stuffed With More Numbers" (a title with 3+ numbers is almost always a data dump, not a sentence)

If a candidate fails the read-aloud test, regenerate. Don't ship.

**Hard filters (genuine constraints, auto-reject):**

1. **Anti-fabrication.** Any number not in the lock list, REJECT. Fabricated numbers lie to the viewer; this is non-negotiable.
2. **Over 50 characters.** REJECT. YouTube literally truncates after 50. Anything over is invisible to the user.
3. **Invented compound nouns.** Phrases like "Unsticks 365s" / "100xs your X" / "Outperforms-A-Y" aren't English. If a Google search of the phrase returns zero hits, the phrase isn't real language. REJECT.
4. **Read-aloud failure.** If the candidate doesn't sound like one continuous human thought when spoken aloud, REJECT. (This is the primary filter at the top of Phase 1.)

**Soft friction (these tend to under-perform; flag and explain, let creator decide):**

5. **Generic** ("How To Make Money Online", too broad, fits any video). Tends to fail because viewers can't tell what's specifically inside. The creator may have a reason. Flag it, ask if they want to add specificity from the script.
6. **Hedge words** ("Maybe," "Probably," "How To Possibly"). Tend to undermine click confidence. Some creators have a deliberately humble brand where hedges fit voice. Let them choose.
7. **Stock phrases** ("Game-Changer," "Mind-Blowing," "Revolutionary," "Insane"). Tend to read as low-effort marketing. Some land when used self-aware or ironic. Default to flagging.
8. **Visual metaphors as the title** ("The Roadmap to Wealth" / "Unlock Your Potential"). Tend to require viewer decoding. Some metaphors land. "The Operating Manual For X" works because it's a literal-feeling metaphor. Default flag.
9. **Audience mismatch.** If avatar is solo founders and the title is "Why Every CEO Should X," that targets a different audience. Tends to bring the wrong viewers. The creator might be deliberately broadening. Flag and ask.
10. **Colons and pipe characters** ("Tutorial: How To X" or "X | Y | Z"). Tend to read as cluttered. Some titles use them effectively (especially in news / news-flavored content). Flag, don't auto-reject.
11. **Credibility-mismatched titles** ("My Morning Routine," "79 Minutes Of Advice," "How I Built A $1M Business"). Tend to fail on small/new channels because cold viewers don't care about an unknown "I" yet. If a single dramatic claim earns the credibility, the title can land regardless of channel size. Flag and let the creator decide.
12. **Mid-title periods or two-sentence smash-ups** ("X. Y." pattern). Tend to read as fragments. Some titles intentionally use period-as-punch ("STOP. THIS IS IMPORTANT."). Flag with explanation.
13. **Number-stuffed titles** (3+ separate numbers). Tend to read as data dumps. Some land. "$3 to $30M in 30 days" is legitimately three numbers and works because they form an arc. Default flag.
14. **Parenthetical clutter.** Parentheticals work when they ADD context that flows ("Change Your Life in 6 Months (My 5-Step Process)"). They tend to fail as tag-on labels ("(3 Changes)" / "(For Real)" / "(Honest Story)"). Flag the latter type.

**The principle:** hard filters block what's literally broken (fabricated numbers, truncated titles, non-English phrases, titles the creator wouldn't say aloud). Soft filters flag what tends to under-perform. The creator gets the final call. Defaults exist because they pattern-match what works most often, not because they're laws.

When showing candidates that triggered soft filters, surface the friction in the annotation: e.g. "5. 'Maybe You're Hiring Too Early', pattern: cognitive-dissonance, BENS: N (39 chars). Soft flag: hedge word 'maybe'." The creator sees the option AND the concern; they choose.

## Natural language patterns that work

When generating, lean toward shapes that real winners use. These read as one human thought:

- **"How I [verb] [specific thing] [in/after/before/etc] [context]"** for "How I Added 50 Pounds To My Squat In 12 Weeks"
- **"Why [subject] [verb-phrase]"** for "Why Looking Poor Is Important"
- **"I [past-tense action] [object/number] [tag]"** for "I Made $12M Selling A Fruit" or "I QUIT My $120,000 Job After Learning 3 Things"
- **"The [number/superlative] [thing] That [verb-phrase]"** for "The 21 Principles of the Top 0.01%"
- **"[Number] [adjective] [things] [target] [verb-phrase]"** for "Top 10 Most HARMFUL Foods People Keep EATING"
- **"Stop [-ing verb] [object]"** for "Stop Asking This!" (single command, not two)
- **"What [subject] [verb] About [topic]"** for "What [Group] Won't Tell You About X"

These shapes scale across niches because they're natural English sentence patterns. The skill should generate WITHIN these shapes, swapping the variables for the video's specific material.

## Title craft notes (for YOUR thinking, not for the chat)

These are the deeper principles that separate good titles from generic ones. Use them to judge candidates internally before showing the list.

**1. Subtext is the actual product.** The viewer doesn't read the words. They FEEL the words and their brain fills in what's not said. "How To Get SO Rich You Question The Meaning Of Making Money" never says "you want that, click for the answer", but that's exactly what the viewer feels. When evaluating a candidate, read it and ask: "What does the viewer's mind fill in here?" If the answer is "nothing, it's just description," the title is weak. If it's "I want that / how do they do it / what's the secret", strong.

**2. "Feel new" beats "be new".** N (New) is the most powerful BENS letter for audiences who have tried solutions and failed. Information doesn't need to be literally new. Repackaged old wisdom can hit N if the framing, the story, or the metaphor is fresh. Don't reject a candidate just because the topic isn't new; ask whether THIS framing makes the viewer feel they haven't seen this take before.

**3. Specificity equals credibility.** "$14,332" beats "make money." "23:07 to 19:42" beats "I got faster." "400 sq ft" beats "small apartment." When pulling from the script, default to the most specific number available. Round numbers feel made up; cents and decimals feel real.

**4. Naming a system or rule does double duty.** "The 90 Minute Rule" hits N (sounds proprietary) AND E (defined process feels achievable) AND B (if the claim is bold). When the script teaches a multi-step method, see if naming it works as a title angle.

**5. Stakes and urgency drive clicks.** Why should the viewer act now or pay attention? "(Avoid This Mistake)" / "Before It's Too Late" / "Stop Doing This". When used honestly (not clickbait), urgency tells viewers their inaction has a cost.

**6. The read-aloud test still applies.** Generated titles get evaluated against the creator's voice profile. If the creator wouldn't say it out loud, drop it. Particularly: AI-default phrasings ("Discover the secret to..." / "Unlock your..." / "The ultimate guide to...") are dead on arrival.

**Present options as a numbered list** with BENS annotation:

```
1. "I Hired A VA. Then Lost 30% Revenue"        BENS: B+S (47 chars)
2. "Don't Hire Until You Have These 12 SOPs"    BENS: E+N (43 chars)
3. "The Mistake That Cost Me 6 Weeks of Revenue" BENS: B+N (44 chars)
4. "Why Your First VA Hire Will Tank Revenue"   BENS: B+N (41 chars)
...
```

Char count and BENS letters explicitly shown so creator can scan tradeoffs.

### Phase 2: Pick the winner

Ask:

> "Which one? Or want me to regenerate with a different angle, or hit different BENS letters?"

Wait. If they pick, go to Phase 3.

If they want changes:
- "Different angle" means re-generate using a different problem-hook from the Top 3
- "Different BENS" means regenerate weighted toward the letters they want (e.g. "more N less B")
- "Shorter" means regenerate under 40 chars
- "Make it more specific" means pull more script-verbatim numbers and named methods into candidates
- "Scrap and start over" means re-run Phase 1, often with the creator pasting new framing

**Push back when picks are weak:**
- They want a generic option ("How To Build A Business"). Flag it: "This would fit 1000 other videos. Want me to add a specific number, named method, or contrarian angle from the script?"
- They want a fabricated number. REJECT and explain. Only script-verbatim numbers allowed.
- They want over 50 chars. REJECT (hard rule).

### Phase 3: Lock and save

Once picked:

**If standalone mode:**
- Save the title to `content/pieces/{slug}/piece.md` `title:` field
- Update `piece.md` `last_refreshed:` to today's date
- Confirm save: "Title locked: '{title}'. Saved to piece.md."

**If sub-skill mode:**
- Return the title string to the caller (and the BENS letters it hits)
- Caller handles the save

**STOP.** Do not generate the thumbnail, hook, or script. Those are different skills.

## Anti-fabrication discipline

Every number, name, claim, or specific phrase in a title MUST be backed by something in the script or foundation docs. If it's not there, the title can't claim it.

If the creator wants a number-driven title and the script doesn't have a usable number, kick it back: "The script doesn't have a number to ground this. Either drop the number-driven angle or add the missing number to the script first."

This is the same rule that lives in `vid-thumbnail`. Kept consistent across writing skills.

## Title-thumbnail pairing awareness

Title and thumbnail will pair eventually (`vid-thumbnail` produces the thumbnail text). They should NOT repeat words. If `vid-thumbnail` has already run for this piece and produced a `thumbnail-brief.md`, read its picks and avoid repeating their key words in the title.

If `vid-thumbnail` hasn't run yet, just lock the title. `vid-thumbnail` will respect the title's lock-words later (this is the rule in `knowledge/thumbnail-text-patterns.md`).

## Principles

- **Conversation, not document.** Short messages. Never dump reference content. References are for Claude to think with.
- **Creator drives, Claude structures.** The candidates draw from the creator's actual material: the angle, the numbers, the moments. Claude doesn't invent claims to make a title sound better.
- **Specificity wins.** Real numbers over round numbers. Named methods over generic descriptions. Specific person/situation over "people."
- **Fit the video AND the avatar.** A title that fits the video but not the avatar misses. A title that fits the avatar but doesn't reflect the video is bait. Both must hold.
- **Under 50 chars is hard.** YouTube cuts off after 50. Don't ship something they won't see.

## Reference index

| File | Why |
|---|---|
| `knowledge/BENS-framework.md` | Big/Easy/New/Safe rules and examples |
| `banks/title-bank.md` | Fill-in-the-blank title patterns (research + creator-curated in one file) |
| `banks/power-words-bank.md` | Global + audience-specific power words, loaded for word selection |
| `assets/title-bank-seed.md` (vid-foundation) | Fallback patterns if title-bank.md not yet scaffolded |
| `foundation/creator-foundation.md` | Avatar, Top 3 problems |
| `foundation/packaging-system.md` | Format guidance, current packaging defaults |
| `content/pieces/{slug}/*` | The video's actual material (brain-dump, framing, script) |
| `banks/packaging-bank/*.md` (own) | Past winning titles for THIS creator as style anchors |

## Related skills

- `vid-foundation` produces the foundation docs this skill loads
- `vid-thumbnail` pairs with this skill; coordinate to avoid word repeats
- `vid-structure` (future) invokes this skill during STRUCTURE phase
- `vid-pipeline` (future) is the orchestrator that calls this skill via vid-structure
- `vid-measurement` (future) does post-publish analysis, logs winning titles back into `banks/title-bank.md` and `banks/packaging-bank/`
