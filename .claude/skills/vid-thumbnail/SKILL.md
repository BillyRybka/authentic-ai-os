---
name: vid-thumbnail
description: Generate thumbnail TEXT options for one video and help the creator pick 1-2 winners. The skill is a TEXT planner only. It does NOT design the visual (no layouts, hero choices, expressions, color application, or AI prompts). Those live in the future vid-thumbnail-gen skill or in the creator's own design process. Outputs a brief with the locked text picks plus rationale (strategy, BENS letters, why it lands). Use when the title is locked and you are packaging the video, or when the creator says "let's do the thumbnail text", "thumbnail options for [video]", or a downstream pipeline invokes it right after vid-title and before vid-structure.
---

# Video Thumbnail Text Planner

Generates thumbnail TEXT candidates for one video and locks 1-2 picks with the creator. Three phases: load context plus generate 5-10 text candidates, creator picks 1-2, save brief with picks plus rationale.

**Scope boundary:** this skill produces text only. Layout, hero element, expression, color application, AI image prompts are OUT OF SCOPE. Handled by `vid-thumbnail-gen` (a future skill) or by the creator using their chosen creation path. Do not drift into designing the visual.

**At session start, load `knowledge/vault-integration.md`.** Every artifact this skill produces follows that contract: frontmatter, wikilinks, tags.

**This skill is a conversation, not a document.** Keep messages short. Never dump reference content into chat. The references (BENS framework, thumbnail strategy menu, gift framework, packaging-system.md, past winners in packaging-bank) are for YOUR thinking. Pull from them selectively.

## What this produces

One file in the creator's workspace:

- `content/pieces/{slug}/thumbnail-brief.md`, the packaging brief: title pairing, 1-2 locked thumbnail text picks, strategy, BENS rationale, and notes for the creator's chosen creation path.

## When to run this

- A video's title is locked (thumbnail is the next packaging step, before structure)
- Creator asks for thumbnail options for an existing piece
- A pipeline orchestrator invokes this in the packaging phase, after vid-title and before vid-structure

## Prerequisites

Hard requirement: `foundation/packaging-system.md` must exist with:
- Current thumbnail strategy (or 2 strategies in test)
- Design guardrails (color, font, hero element, expression rules)
- Creation path picked (Photoshop / AI workflow / batch photos / outsource)

If `packaging-system.md` is missing, hard stop. Tell the creator to run `vid-research` first (it authors packaging-system.md from real outlier evidence).

Also hard: the video `slug` argument, or an existing `content/pieces/{slug}/piece.md` with a locked title.

## The walkthrough (3 phases)

Each phase ends with creator approval before moving on. Do not batch phases. Do not dump references into chat.

### Phase 1: Load context and generate text options

**Silent loads** (do NOT paste into chat):

1. `foundation/packaging-system.md` (current strategy, design guardrails, creation path)
2. `knowledge/thumbnail-strategy-menu.md` (the 6 strategies plus format-strategy pairing)
3. `knowledge/thumbnail-text-patterns.md`. **The playbook for what good thumbnail text actually looks like.** 5 winning patterns with examples, anti-patterns, title-thumbnail pairing rules. **Generation candidates must come from these patterns.**
4. `knowledge/thumbnail-examples-library.md`. **26 annotated real-world title+thumbnail combinations**, organized by category (Curiosity heavy / Comparison / Result / Social Hacking). Each entry has hero element, why it works, and design notes. Use to find the closest analog to the target video and match the SHAPE, not the literal content.
5. `knowledge/BENS-framework.md` (Big / Easy / New / Safe, for thumbnail text logic)
6. `knowledge/gift-framework.md` (packaging philosophy)
7. `content/pieces/{slug}/piece.md` (locked title, format, goal, hook/payoff)
8. `content/pieces/{slug}/script.md` if it exists. Pulls specific lines, numbers, moments worth foregrounding.
9. `banks/packaging-bank/*.md` (past winners and studied outliers, used as TEXT anchors for what wording worked for this creator, NOT for visual style)

Note: `knowledge/thumbnail-composition-guide.md` exists but is NOT loaded here. It's reserved for `vid-thumbnail-gen` (future) which actually designs the visual.

**Empty packaging-bank fallback.** If the bank is empty (fresh creator, no own winners and no logged outliers, exactly the case for first-time users), proceed using design guardrails alone. Note this in the brief's "Notes" section so the creator knows to log a winner post-publish to feed future runs. Do not silently skip the past-winners step. Flag it.

**Opening message** (brief, creator-facing):

> "Thumbnail for *{title}*. Current strategy: {strategy from packaging-system}. Pulling the hook and payoff from the script now. Back with 5-10 text options in a sec."

Then silently:
- Re-confirm the current strategy (or 2 strategies if testing)
- Pull the script's specific numbers, named methods, paradoxes, and imperatives. These are the raw material.
- **Build a "lock list" from the script:** every number, percentage, dollar figure, timeframe, and named method that actually appears verbatim. Candidates may ONLY use numbers from this lock list. No fabrication.
- **Identify the title's tone:** failure, success, mystery, contrarian, instructive, news. Candidates must pair with this tone (match or productively contrast).
- **Generate 5-10 candidates DRAWING FROM `knowledge/thumbnail-text-patterns.md`.** Use AT LEAST 3 of the 5 winning patterns (cognitive-dissonance / number-hero / named-system / single-word / imperative) so the option set isn't all clustered. Pure number-hero options are valid. Don't always pad numbers with words.

**Quality filters (apply BEFORE showing candidates to the creator):**

1. **Anti-fabrication check.** Scan every number/figure in every candidate. If a number isn't in the script's lock list, REJECT the candidate. Don't invent dollar arcs, percentages, or transformations the script doesn't state.
2. **Curiosity vs Spoiler test.** Read each candidate alone. Can a viewer guess the video's central insight from it? If yes, it's a spoiler. REJECT. The thumbnail's job is to make them want to know, not tell them. "STOP DELEGATING" creates curiosity; "SOPs BEFORE PEOPLE" delivers the payoff.
3. **Tonal pairing check.** Does the candidate's emotional register pair with the title's tone? Failure-framed title plus positive-result thumbnail equals mismatch. REJECT. Either match the tone or productively contrast (same dark register, different angle).
4. **Distinctiveness test.** For single-word and named-system options: would this exact word or name fit 100 other videos in the niche? If yes (e.g. "BOTTLENECK" for any founder video), REJECT. The thumbnail must signal *this specific story*, not the channel's general theme.
5. **Anti-pattern filter.** Visual metaphors (ROADMAP / BLUEPRINT / UNLOCK), vague paradoxes, hedge words, generic claims, stock phrases. All REJECT.
6. **Title-overlap rule** (with exception clause). Default: don't repeat the title's key noun-plus-verb pair. Singular/plural variations or related word forms are OK ONLY if the thumbnail adds a meaningfully different angle (e.g. "VAs suck" as opinion, against title's "Why Hiring a VA Tanked My Revenue" as story). Mark borderline candidates explicitly so the creator sees the trade-off.

**Word count: 2-4 words preferred. 5 is the absolute ceiling.** 6 or more is automatic reject. Single words are valid when they're high-curiosity (LIAR / STOP / BREAKFAST / BACKWARDS).

**Pure-number carve-out:** A candidate that's just a number, currency amount, or transformation arc ("$712,921.88", "+40%", "275 to 175", "23:07 to 19:42") counts as 1 unit regardless of character count. Don't reject these on word-count rules. That's the number-hero pattern.

**Title-overlap rule includes parentheticals.** If the title is "Why Hiring a VA Tanked My Revenue (Fix Inside)", lock-words include VA, HIRING, REVENUE, TANKED, FIX, INSIDE. Parenthetical words count.

**Casing rule:** ALL CAPS is the default. Lowercase ("work less," "this is.... Almost 30") is acceptable when the creator's design guardrails specify it (typically millennial / casual / lifestyle aesthetic). Match the casing in the packaging-system guardrails.

**BENS notation:** Single-letter joined format with `+`: `B+N`, `B+E+S`. No spaces, no commas.

**Pattern annotation:** Each candidate gets `pattern: {name}` so the creator can scan for variety. The 5 patterns: `cognitive-dissonance | number-hero | named-system | single-word | imperative`.

**Present options as a numbered list** with pattern plus BENS annotation:

```
1. "STOP HIRING"               pattern: imperative, BENS: B+N
2. "-30% IN 6 WEEKS"           pattern: number-hero, BENS: B+S
3. "BACKWARDS"                 pattern: single-word, BENS: N
4. "THE PRE-HIRE RULE"         pattern: named-system, BENS: E+N
5. "DELEGATION FAILS"          pattern: cognitive-dissonance, BENS: N
6. "+40%"                      pattern: number-hero (single), BENS: B+S
...
```

Keep annotations short. Creator doesn't need a lecture. They need to scan and pick. Don't cluster all options in one pattern. Span at least 3 of the 5 so the creator sees real range.

**Kill criteria.** If after one full regeneration the options still feel weak (every text generic, no clear strategy fit, the title or script doesn't give you enough specific material to work with), stop generating and tell the creator the issue is upstream. The title may be too vague. The script may be missing the specific number or moment that thumbnails need. Don't keep producing weak text trying to make a thin source work.

**Push back on weak drafts if the creator reviews/rejects options:**
- Over 5 words, trim
- Passive voice, rewrite in active
- Generic "HOW TO" / "THE TRUTH ABOUT", swap for specific language
- Doesn't pair with the thumbnail strategy, flag it and regenerate

### Phase 2: Pick 1-2 winners

**Ask:**

> "Which 1 or 2 would you actually want to test? Pick by number. If two, they should be meaningfully different, not variations of the same idea (different strategy, different tension)."

Wait.

If they pick two that are too similar, push back:
> "#2 and #5 are both result-strategy packages. If you want to A/B test, one should hit a different strategy so the data tells you something useful. Want to swap one?"

If they want to keep both similar ones anyway (edge case where they're testing copy variants within same strategy), OK, note it in the brief.

### Phase 3: Lock the picks and save

**Scope reminder:** this skill is a TEXT planner, not a designer. The job ends when the creator has 1-2 thumbnail texts they want to test. The skill does NOT pick layouts, hero elements, expressions, color application, or generate AI prompts. Those decisions live in the creator's head or in the future `vid-thumbnail-gen` skill, not here.

For each pick, capture a tight rationale (1-2 lines, NOT a composition spec):

1. **The text**, verbatim, with casing matching the creator's guardrails
2. **Strategy plus BENS**: which strategy this hits and which BENS letters
3. **Why it lands**: one sentence on the cognitive gap or proof angle. (Not how to design it. Just why this text works as a hook.)

That's the whole brief content per pick. No layout, no hero choice, no expression, no AI prompt. The creator takes their picks and designs the thumbnail themselves (or runs `vid-thumbnail-gen` later).

**Cross-check each pick against the title-pairing rules in `thumbnail-text-patterns.md`:**
- Text and title carry different curiosity hooks (no word repeats unless the exception clause applies)
- Thumbnail tone pairs with title tone (failure-framed title pairs with failure-tone or productively-contrasting thumbnail)
- The video actually delivers the promise. Clickbait is OK if delivered. If you can't honestly say the script delivers what the thumbnail implies, kick it back to the creator.

### Save

Save to `content/pieces/{slug}/thumbnail-brief.md` with this frontmatter:

```yaml
---
type: thumbnail-brief
project: authentic-ai-os
piece: "[[{slug}]]"
title_paired: "The exact title this thumbnail pairs with"
strategies_tested: [cognitive-dissonance, result]
picks: 2
creation_path: ai-workflow          # pulled from packaging-system.md
captured: YYYY-MM-DD
status: brief-ready                 # brief-ready | in-production | published | winner-logged
tags: [thumbnail, brief, strategy-{slug}]
---
```

Body follows the Composition-brief template in `assets/thumbnail-brief-template.md`.

Then bump `content/pieces/{slug}/piece.md` `last_updated:` to today's date. This happens in both standalone and pipeline mode. The presence of `thumbnail-brief.md` is how the pipeline knows the thumbnail step finished; vid-thumbnail writes no other piece.md field.

### Wrap up

After saving:
1. Confirm file saved at `content/pieces/{slug}/thumbnail-brief.md`
2. Quick next-step prompt based on `creation_path`:
   - AI workflow: "Prompt is ready. Paste into your image tool, iterate until it matches the brief. If a version wins after publishing, log it in `banks/packaging-bank/`."
   - Photoshop/DIY: "Shot list is in the brief. Execute it. When it wins, log it in packaging-bank."
   - Batch photos: "The pose is noted. Grab that shot from your batch, assemble per the layout. Log a winner post-publish."
   - Outsource: "Designer brief is ready to send. When they deliver, QA against the checklist in the brief. Log a winner post-publish."

## Principles

- **Conversation, not document.** Short messages. Never dump the full reference docs at the creator. The creator scans options and picks. They don't read lessons.
- **Creator drives, Claude structures.** Don't invent packaging ideas the creator would reject. Pull from the script, the hook, the past winners. Anchor every option in real content.
- **Test within strategy, not against it.** If two options are picked, they should teach the creator something different. Don't A/B test variants of the same strategy unless explicitly requested.
- **Every pick must pass the one-pager checklist** before the brief saves. Skip the QA and you ship broken packaging.
- **Past winners are the creator's proven style.** When in doubt, copy the patterns that already worked for them, not generic best practice.
- **No fabrication.** Don't invent specific numbers, client names, or quotes for thumbnail text. Pull only what exists in the script or foundation docs.

## Reference index

**Shared** (loaded from `knowledge/`):

| Phase | Reference | Why |
|-------|-----------|-----|
| 1 | `knowledge/thumbnail-strategy-menu.md` | 6 strategies plus when each fits |
| 1 | `knowledge/BENS-framework.md` | Title/thumbnail text logic |
| 1 | `knowledge/gift-framework.md` | Packaging philosophy |
| 1 | `knowledge/vault-integration.md` | Frontmatter, wikilinks, tags |

**From the creator's workspace**:

| Phase | File | Why |
|-------|------|-----|
| 1 | `foundation/packaging-system.md` | Current strategy, design guardrails, creation path |
| 1 | `content/pieces/{slug}/piece.md` | Locked title, format, goal |
| 1 | `content/pieces/{slug}/script.md` | Hook lines, payoff, specific numbers to foreground |
| 1 | `banks/packaging-bank/*.md` | Past winners, the creator's proven packaging style |

Template lives in `assets/`:
- `thumbnail-brief-template.md`

## Related skills

- `vid-research` authors the `packaging-system.md` this skill reads (from outlier evidence)
- `vid-thumbnail-gen` (future) takes a brief from this skill and produces actual images via the creator's AI tool
- `vid-measurement` (future) post-publish analysis that flags winning packaging, creator logs a `packaging-bank/` entry
