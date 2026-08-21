<!-- target: claude-opus-5 · effort: xhigh · subagents: no -->

# Stage 1 of 2: build vid-format-plan, case study only

Build a standalone skill that co-plans one video against its format planner doc. The creator says "I want to plan a case study video," and the skill scaffolds a plan file with every section stubbed, then walks them through filling it one blank at a time. The file on disk is the progress bar. It exists from turn one and the creator watches it fill.

This is a test of the interaction, not a committed part of the pipeline. Billy runs a real planning session against it before anything else gets built, which is why this stage covers one format instead of seven. Nothing in the existing vid-* chain may change.

Build the skill. Do not plan a video with it and do not run a session.

## Where

New directory, the only place you create files:
`c:\Users\billr\projects\authentic-ai-content-engine\.claude\skills\vid-format-plan\`

Read these:

- `knowledge/format-planners/case-study.md` is the content source of truth. Its "8-step planner" is the spine, and its "5 questions every case study answers" section names what is load-bearing.
- `.claude/skills/vid-braindump/SKILL.md` (142 lines) is the file-shape reference: frontmatter form, description style, prose density, length. Match its shape. Do not copy its content or its design.
- `content/pieces/deep-research-skill/` shows the piece folder convention: `brain-dump.md` and `piece.md` sitting alongside each other.

The skill writes its plan to `content/pieces/{slug}/format-plan.md`. That filename is new. No existing skill reads or writes it, which is what keeps this isolated.

## How the skill behaves

**Cold start.** No brain dump required and no check for one. The creator arrives with a video in mind, usually a working title and a thumbnail idea already done. Step 0 collects in a single turn: which of the seven formats, one line on the video, working title, thumbnail idea, goal (sales, emails, or views). If they named the format in their opening line, do not ask for it again.

**Scaffold before the first real question.** Write `format-plan.md` immediately, with every section of the case-study planner stubbed and empty, plus the intro section and one stub per body segment. Each stub carries a status marker. Say the path once. From there the file is the shared reference and the creator can keep it open beside the conversation.

**Fill one blank at a time, in file order, writing to the file after every answer.** The creator sees it grow. Never batch questions.

**Every turn carries a progress line:** step N of M, and what remains. Short.

**Turn shape.** One line of orientation, then the ask. No preamble, no recap of what they just said, no praise, no summarizing back at them. Explain why a blank matters only when the creator asks.

**Navigation.** Linear by default. Honor "skip that," "come back to it," "jump to the ending," "what's left."

**Push rule.** The planner doc decides what is load-bearing. For case study that is the 5 questions, where the doc states that a missing one leaves a hole. On a load-bearing blank that comes back thin, ask up to two sharper follow-ups, each one requesting something specific: a number, a date, a name, a quote. Still thin after two, write a gap callout into the file naming what is missing and why it matters, then move to the next blank. Never block the creator on a blank. Non-load-bearing blanks get one ask and take whatever comes back.

**Never invent.** Where the creator has nothing, the section stays empty behind its gap marker. Offering candidate answers built from something they already said this session is fine and is not invention.

**Done and resume.** The session ends when every section is either filled or marked a gap. The closing turn gives the path, the filled count, and the gap list. Reopening the skill reads the existing file, says where it stopped, and continues at the first unfilled section.

The plan file follows the vault conventions in CLAUDE.md: frontmatter, wikilinks for entity references, Obsidian callouts for gaps.

## The format card

`references/case-study.md` inside the skill directory. One entry per blank, holding the exact question wording, whether that blank is load-bearing, the two follow-up questions for the push, and what a passing answer contains.

It covers all 8 planner steps and all 5 story questions, and it points at `knowledge/format-planners/case-study.md` rather than restating it. Duplicating the planner content means the two drift apart the first time Billy edits one.

Stage 2 clones this card to the other six formats, so its shape has to survive being copied. The formats have different step counts (deep dive 11, listicle 10, roast 10, short process 10, news 8, interview 7) and different mandatory sections.

## Out of scope

- Create files only inside `.claude/skills/vid-format-plan/`. Nothing else in `.claude/skills/` changes.
- The skill never writes `piece.md` or `script.md`. Both are owned by the existing chain and this one stays out of them.
- Do not edit anything in `knowledge/`.
- Do not read the other vid-* skills for design ideas. vid-braindump is the one exception and only for file shape.
- It plans. It does not write intro prose, segment prose, or an ending.

## What done looks like

Run these and paste the output:

1. `git status --porcelain` shows only new files under `.claude/skills/vid-format-plan/`. Nothing modified, nothing deleted. This one has to come back clean. The point of the stage is that the existing chain is untouched.
2. `wc -l .claude/skills/vid-format-plan/SKILL.md` returns under 200.
3. The card carries at least 13 blanks, mapping one to one onto the 8 planner steps and the 5 story questions.
4. `grep -rn "piece.md\|script.md" .claude/skills/vid-format-plan/` returns only the out of scope line that forbids writing them.

## Report back with

The file tree of the new directory, the four outputs above, and a table mapping each blank in the card to the planner step or story question it came from.

The last thing you leave on disk is the skill directory. Billy runs a live planning session against it before stage 2 starts.
