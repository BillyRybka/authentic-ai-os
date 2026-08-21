<!-- target: claude-opus-5 · effort: high · subagents: no -->

# Stage 2 of 2: clone the format card to the remaining six formats

Start by orienting yourself. Run `pwd`. Read `.claude/skills/vid-format-plan/SKILL.md` and `.claude/skills/vid-format-plan/references/case-study.md`. Run `git log --oneline -5`. Read `prompts/003-format-planner-1-build.md` for the constraints stage 1 ran under. All of them still hold.

Billy has run a live planning session against the case study card. Anything he asked to change is already in the files you just read. That version is the pattern, not the one described in stage 1.

Then write one card per remaining format in `.claude/skills/vid-format-plan/references/`, matching the case-study card exactly in shape:

- `deep-dive.md` (11-step planner)
- `listicle.md` (10-step planner, plus the parable decision matrix per point)
- `roast.md` (10-step planner, plus the per-review structure and the submission funnel)
- `short-process.md` (10-step planner)
- `news.md` (8-step planner)
- `interview.md` (7-step planner, plus question planning)

Each card is derived from `knowledge/format-planners/{format}.md` and points at it rather than restating it. Read each planner doc in full before writing its card.

The load-bearing blanks differ per format. Find what each doc states as mandatory, the way case study states that a missing one of the 5 questions leaves a hole, and mark those. A format whose doc names nothing as mandatory has no load-bearing blanks. Do not invent them to make the seven cards symmetrical.

Update `SKILL.md` so it routes to all seven cards by format name.

## Out of scope

Same as stage 1. Files only under `.claude/skills/vid-format-plan/`, nothing in `knowledge/` changes, the skill never writes `piece.md` or `script.md`.

## What done looks like

1. `ls .claude/skills/vid-format-plan/references/` lists seven cards.
2. `git status --porcelain` shows changes only under `.claude/skills/vid-format-plan/`. Nothing else modified.
3. Each card's blank count matches its planner doc's step count plus that format's mandatory section. Paste the per-format numbers.

## Report back with

The three outputs above, plus a per-format table: step count, blank count, which blanks you marked load-bearing, and the line in the planner doc that justified each one.
