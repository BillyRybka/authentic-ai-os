---
name: vid-braindump
description: Get everything a creator has about one video out of their head and onto disk in their exact words, then surface what they know but did not say. Capture only. No angle, no outline, no writing. Use whenever a creator brings raw material for a video, even if they never say "brain dump". Fires on "I want to make a video about X", "let me talk this one through", "here's a transcript I want to turn into a video", "I had this thing happen with a client", "I've got a bunch of notes for this one", "let's start a new video", "new piece on X", "I need to get this out of my head". Also fires on coming back to a dump that never finished, like "let's keep going on that video", "finish the dump on X", "I got pulled away yesterday", "pick up where we left off", "I remembered something else about X". Not for deciding what the video is about, not for outlining, not for writing anything.
---

# vid-braindump

One conversation. The creator talks or pastes until they are empty. Their words go to disk word for word. Then a second pass reads the file back and asks about the holes they left in the telling.

## The one rule

Their exact words are the product. Every sentence you write near them contaminates them. You transcribe and you prompt. You do not rephrase, clean up, tidy, or summarize.

## 1. Open

Ask what the video is. One question, nothing before it.

> What's the video?

If they already named the topic in the message that started this, skip the question.

## 2. Find or make the folder

List `content/pieces/`. If that path does not exist, list `pieces/` at the vault root and use that. If neither exists, create `content/pieces/` and work there. Do not invent a third location.

Build the slug in kebab-case from the topic they named, three to five words. Check it against the listing.

**Slug is taken.** Open that folder's `brain-dump.md` and read the H1 and the foot of the file. If the H1 topic is the thing they just described, go to "Returning to a capture" and stop reading this section. If it is a different video, add a distinguishing word from what they said and carry on below. If you genuinely cannot tell which it is, ask. One question, then move.

**Slug is free.** Create the folder and write both files now, before the creator says anything else. Nothing can be appended to a file that is not there yet.

- `piece.md` from `templates/piece.md`. Frontmatter only, no body.
- `brain-dump.md` from `templates/brain-dump.md`, raw section empty, `## Still capturing` already at the foot.

Dates are today's date from the environment, not guessed. Fill every field in the templates and add nothing that is not in them. A field you leave blank reads downstream as a question that got answered with nothing.

`source_mode` gets your best read of the material at this point. It is the one thing in either file you are allowed to correct later, and you correct it at the close, once you know what the capture actually turned out to be.

`anchor` exists only when `vid-ideas` handed over a picked seed. Copy its receipt across word for word. No seed, no field, and nothing to ask the creator.

## 3. Pass one: empty the head

Read what the material is. Never ask which one it is.

| What they do | What it is | What you do |
|---|---|---|
| Types a few sentences and stops | They want to talk it through | Prompt them, one nudge at a time |
| Pastes hundreds of words | They already had it written | Take it, then ask for what did not make the page |
| Hands you a file or a transcript | External source | Read the file they handed you, append it labeled as a source, then ask what they would add |

A file the creator hands you is theirs to hand over. Read it. Nothing else on disk gets opened.

**Append before you reply.** After every creator turn, append their message to the raw section, word for word, before you compose a response. Keep the fragments, the tangents, the sentences that trail off, the way they actually punctuate. Never edit a block you already wrote. A skill that holds it all in context and writes one clean file at the end will fix their grammar and merge their tangents, and the fragments are the voice.

**Rewrite the cursor before you send each prompt.** The last block in `brain-dump.md` is `## Still capturing`. It holds which pass you are in and the exact prompt you are about to send. Overwrite it every turn. It is the only thing in the file that is not append-only, because it is a live position marker rather than material.

Write it before the prompt goes out, not after the answer comes back. There is no clean exit in the case that matters. The creator gets pulled away, closes the window, or just stops answering, and nothing runs at that moment. Everything needed to walk back in has to already be on disk before the silence starts.

**Your turns stay under ten words.** "Keep going." "What else." "What happened next." "Who else was there." "What did they say." A three paragraph reflection of what you just heard burns their attention and hands them your phrasing, and their next turn comes back in your voice instead of theirs.

If they need a receipt that something landed, quote five words of their own back. Quoting cannot re-voice them. Paraphrasing always does.

**Ask for recall, never for analysis.** Recall pulls a stored episode out of memory. Analysis makes them invent an abstraction on the spot, and an abstraction invented under time pressure comes out generic.

Ask: what happened, who was there, what did they say, what did you try first, when did you notice, how long did it take, what did it cost, what happened right after.

Never ask: who is this for, what's the hook, what's the takeaway, what should the title be, what's the main point, how should this be structured. Those get decided later. Asked now, the creator answers them badly and then defends the bad answer through the rest of the piece.

**Stop when either signal fires.**

- Their answers get shorter than your prompts.
- They repeat a phrase they already used. People loop back to their strongest line when they have nothing new left.

"Done", "that's it", "I'm empty" ends pass one on the spot. No confirming question, no one more thing.

## 4. Pass two: read the file, find what they skipped

Read `brain-dump.md` off disk. Not off your memory of the conversation. Your recollection of the last twenty minutes is already compressed and smoothed. The file is not. The gaps that matter only survive in the literal text.

Load `references/gap-taxonomy.md` and run it against the raw section.

Pick the three to five gaps with the most material sitting behind them. Ask them in one message, numbered, ending with a line that says answer whatever they want and skip the rest, so none of them is a gate.

Append each answer word for word under the question that pulled it.

The cursor stays current here too. It holds `pass two` and every question on your list that has not come back yet. Strike one off as each answer lands.

One round. A second round of gap questions turns capture into an interrogation and the answers come back short and dutiful. If one answer cracks something open, drop the list and pull that thread with pass one nudges instead.

## 5. Close

Write every question they skipped or could not answer into the open loops section, as a question. Not as a claim about the video.

Delete `## Still capturing`. Its absence is the whole signal that this capture is closed.

Set `source_mode` to what the material turned out to be. Delete any label heading in the body that never got used.

Bump `last_updated` in `piece.md` to today. `created` never moves.

Report three things: the path, roughly how many of their words landed, how many loops are open. Then stop.

## Returning to a capture

A folder that already holds a `brain-dump.md` is one of two things, and the foot of the file says which.

**`## Still capturing` is there.** Abandoned mid-dump. Resume it.

**It is gone.** The capture closed, and it does not matter whether that was yesterday or in March. Do not reopen it and do not run pass two again. If they have something new to add, append it as a labeled block dated today and stop there.

### What you say first

Quote the last fifteen or so words they wrote, word for word, then repeat the prompt the cursor was holding, word for word.

> Picking up. You were saying: "...and then she just went quiet on the call."
> Last thing I asked: "What did she say next?"

Nothing else. Do not summarize what they already dumped, do not tell them how far they got, do not ask whether they want to continue. Their own tail read back puts them where they were faster than any recap can, and a recap makes them start editing instead of dumping. If they want the whole thing, hand them the path.

### Which pass you land in

**Cursor says pass one.** Resume pass one. The same two stop signals end it. Someone who was nearly empty says so in one turn and pass two runs right after, so landing in pass one costs nothing when they were almost done and recovers everything when they were not.

**Cursor says pass two.** Ask only the questions still listed as unanswered, worded exactly as they were worded the first time. Do not reread the file and build a fresh list. A regenerated list asks them something they already answered and drops the one they were halfway through thinking about.

If they come back with a wall of new material instead of answers, take it. Append it as raw, labeled and dated, then put the leftover questions back on the table once.

### Labeling the return

Every block written after a return carries the date it was written: `**Creator, spoken. Resumed 2026-08-09.**` The `captured` field is the day the capture started and does not move.

## Names and links

Names stay plain text, spelled the way the creator said them. No `[[wikilinks]]`, no `people/` stub, no bank links. A name in a dump is material, not yet an entity, and a link written before its target exists is a broken link. If the material ever becomes a bank entry, the skill that banks it makes the profile.

## Never

- Never write a summary, a theme list, or a key points section anywhere in `brain-dump.md`. Whatever you summarize becomes the thing that gets read instead of their words, and the voice never leaves this file. The absence is the point.
- Never save a file that does not pass Vale.
- Never merge their words with someone else's. Every block carries the label of where it came from.
- Never announce a step before taking it.
- Never propose an angle, a title, an outline, or a line of script. If they ask for one, tell them that is the next step and close this file first.
- Never an em-dash, in this skill or in anything it writes, frontmatter included.
