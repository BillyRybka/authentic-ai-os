---
name: vid-format-plan
description: Co-plan one video against its format planner, one blank at a time, into a plan file the creator watches fill. Case study only in this build. Use when a creator has a video in mind and wants the format worked out before anything gets written. Fires on "I want to plan a case study video", "plan this one as a case study", "walk me through the case study format", "what do I need for a case study", "let's plan the video", "format plan for X", "I've got a client story I want to turn into a video". Also fires on returning to a plan that never finished, like "finish the format plan", "pick up the case study plan", "what's left on that plan". Not for capturing raw material, not for titles or thumbnails, not for writing intro, segment, or ending prose.
---

# vid-format-plan

One session. The creator arrives with a video already in their head, usually a working title and a thumbnail idea done. The plan file gets written before the first real question, then fills one blank at a time while they watch.

## The one rule

The file on disk is the progress bar. It exists from turn one and every answer lands in it before the next question goes out. A plan assembled in context and written at the end is a plan the creator never saw being built, and a session that gets cut short halfway leaves nothing behind.

## What this build covers

Case study, and nothing else yet. The other six formats have no card, which means the format is not a question you ask. State it and move.

If the creator names one of the other six, say that one is not wired up yet, name case study as the one that runs, and stop. A format with no card gets no improvised plan.

## 0. Open

Five things, one turn. A line of setup, the five on five lines, a line saying rough is fine.

> Quick setup, then we plan it.
>
> - What's the video?
> - Which format? Case study is the one that's built.
> - Working title, if you have one
> - What's on the thumbnail
> - Sales, emails, or views
>
> Rough is fine. Skip anything you don't have yet.

**Five lines, never one sentence.** "Which format, one line on what the video is, the working title, what's on the thumbnail, and the goal" is the same five things and it reads as a wall. Five short lines get answered in ten seconds. One long line gets read twice and answered badly.

**This is the only turn that asks for more than one thing.** These are five things the creator already has, not five things they have to think about. Everything after this is one ask per turn, because everything after this needs thinking.

Never re-ask for something they already said in the message that started this. "Plan a case study about Steve" answers the format and answers the video, so those two lines come out of the list.

Nothing here is a gate. Whatever comes back, take it and scaffold. Format, title, thumbnail, and goal are blanks 1 and 2 on the card: what they hand over lands in the file already filled, and what they skip stays empty and comes up in the walk like every other blank.

## 1. Scaffold

Build the slug in kebab-case from the video, three to five words. List `content/pieces/` and check it. If a folder of that name is there, go to "Returning to a plan". If the path `content/pieces/` does not exist, list `pieces/` at the vault root and use that instead. If neither exists, create `content/pieces/`.

Write `content/pieces/{slug}/format-plan.md` now, before any real question. `templates/format-plan.md` is the frame, `references/case-study.md` is the section list. Every blank on the card gets a heading, in card order, each one holding an empty marker.

Then say the path, once:

> `content/pieces/steve-80k-months/format-plan.md`. Keep it open if you want to watch it fill.

Nothing else in that folder gets read, written, or created.

## 2. Fill

Load `references/case-study.md`. Walk it in file order, one blank per turn.

**Write to the file after every answer.** Their answer replaces the empty marker in that section, and only then does the next question go out. Never two questions in one turn, never a batch, never a form.

**Their words, lightly held.** Write what they said in their phrasing. Cut the throat-clearing out of a rambling answer, keep the nouns and the numbers exactly as they said them. Never upgrade a vague answer into a specific one on the way to the file.

**One thing per ask.** Under ten words wherever the question allows it. A blank that holds two things gets two asks, not one long one, and the count does not move between them. Every question that arrives as a list of clauses gets answered as a form, and a form gets the shallowest answer a creator can give.

**Turn shape.** A short progress line, then the ask. That is the whole turn.

> 6 of 15. Story, then the principle.
> What was their problem when they came to you?

The specifics live in the push, not in the ask. "A number and a date, not stuck" bolted onto the first question tells them the answer before they reach for it, and what comes back is the shape you asked for rather than what happened.

No preamble, no recap of what they just said, no praise, no reading their answer back at them. Explain why a blank matters only when they ask.

## 3. The push

The card marks which blanks are load-bearing. For case study those are the five story questions, because the planner says a missing one leaves the video with a hole.

**A load-bearing blank that comes back thin gets up to two follow-ups**, both written on the card, each asking for one specific thing: a number, a date, a name, a quote. Never a general "can you say more about that."

Still thin after two, write the gap callout, name what is missing and why the video needs it, then move to the next blank.

> [!warning] Gap: no number on the outcome
> The planner wants a specific figure and a specific timeframe. Without one this plays as a claim rather than a receipt.

**Never block on a blank.** A gap is a marked hole in a file the creator can walk back into, and the plan keeps moving.

**Non-load-bearing blanks get one ask** and take whatever comes back. Thin is a call they are allowed to make.

**Offering candidates is fine.** Built from something they already said this session, never from anywhere else. "You said the first two months went backwards. Is the lesson that the dip is part of it?" is a candidate. Anything they did not say is invention and does not go in the file.

## 4. Navigation

Linear by default. Honor the four things they will say:

| They say | You do |
|---|---|
| "Skip that" | Gap callout naming what is skipped, then the next blank |
| "Come back to it" | Leave the empty marker, next blank, raise it again at the close |
| "Jump to the ending" | Go to that blank, then back to the first empty one |
| "What's left" | The empty and gapped section names, nothing else |

## 5. Close

The session ends when no empty markers are left. Every section is filled or carries a gap callout.

Set `status: planned`, bump `last_updated`. Then the closing turn: the path, the filled count, the gap list. Nothing after it.

> `content/pieces/steve-80k-months/format-plan.md`. 13 of 15 filled.
> Two gaps: the proof screenshot (you're asking Steve for it) and the end-screen video.

## Returning to a plan

A `format-plan.md` that already exists is one of two things, and the file says which.

**Empty markers left.** Read the file, say the count and the first section still empty, then ask that blank's question. One line, then the ask.

> 9 of 15. You stopped at the outcome.
> The number, and how long it took.

**No empty markers.** The plan closed. Do not walk it again. If they have something to add, take it into the section it belongs to, bump `last_updated`, and stop.

Never rebuild a question from your read of the file when the card holds the wording. A regenerated question comes out different the second time, and the creator answers the same blank twice.

## Names and links

Names stay plain text, spelled the way the creator said them. No `people/` stubs, no bank links written on faith. A wikilink goes in only when its target is on disk and you checked: an existing proof entry is `[[proof-bank/{slug}]]`, verified before it is written.

## Never

- Never write `piece.md` or `script.md`. Both belong to the existing chain and this skill stays out of them.
- Never write intro prose, segment prose, or an ending. This plans the video. Something else writes it.
- Never restate the planner at the creator. Read it, ask from it, keep it behind the conversation.
- Never invent a fact, a number, a name, or a lesson. An empty section behind a gap callout is the correct output when they have nothing.
- Never batch questions, and never send one without writing the last answer first.
- Never ask for the format twice.
- Never an em-dash, in this skill or in anything it writes, frontmatter included.
