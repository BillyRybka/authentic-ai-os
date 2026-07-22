# Idea generation rules

Runtime logic for `vid-ideas` Phase 2 (generate) and Phase 3 (the dial). Not chat content. This is how the skill turns the creator's positioning plus the real winning titles into a batch that would actually get clicked.

## Start from the raw winner, not the label

The pattern-bank has two layers. The **Synthesis** names patterns in the abstract ("speed-to-outcome compression", "steal-this generosity"). The **per-channel rows** hold the actual winning titles with real views and median-multiples.

Generate from the RAW TITLES, never the labels. The Synthesis is only a map: it tells you which shapes have spread and what is on-lane versus off-lane. It does not tell you why a specific title won. The label editorializes; the title is the evidence. "Systems content that promises speed" is a label. "I Cook a Week of Dinners in 90 Minutes (One Pan)" is the title, and its engine is "in 90 Minutes" plus "(One Pan)", a week of output compressed into one small block, not "speed". Use the Synthesis to decide which patterns to mine, then open the per-channel rows and work from the actual titles.

## The engine is a form, not a theme

Before you move anything, take the raw title and name the ONE element that drove the multiple. Not the abstract job ("it promises speed", "it flips an identity"). The specific load-bearing phrasing:

- its **number**: "95% of Freelancers Invoice Wrong" lives on the 95%. "Most Freelancers Invoice Wrong" is the same theme with the engine removed.
- its **hot proper noun**: the named tool, the named client, the named method everyone in the niche already talks about.
- its **parenthetical kicker**: "(No Gym)", "(One Pan)", "(Full System)". The kicker is where the proof or the objection-killer sits.
- its **named system**: "The 3-Tier Pricing Page", "The Weekly Review". A name turns advice into a thing the viewer can take.

Worked reads (synthetic, across niches):

- "I Got My Clients Stronger in 20 Minutes a Day (No Gym)" (@shedstrong, 412k, 18.2x) -> the contrast: real results, tiny time, no equipment. The "(No Gym)" kicker carries it.
- "95% of Freelancers Invoice Wrong" (@ledgerline, 88k, 9.4x) -> the superiority stat. The 95% IS the engine: it tells the viewer they probably do this wrong.
- "I Cook a Week of Dinners in 90 Minutes (One Pan)" (@weeknightplate, 1.2M, 22.6x) -> "in 90 Minutes" plus the "(One Pan)" kicker, a whole week compressed into one small block.
- "Why Quiet Consultants Close the Biggest Clients (Nobody Talks About This)" (@quietcloser, 156k, 11.3x) -> the identity flip plus the exclusion kicker: the trait you hide is the advantage.

Ask the real question: why did this beat its channel's median by Nx? The answer is the thing you must keep, in its sharp form.

**A dull synonym of the sharp form is a floor failure.** "Without a gym membership" is not "(No Gym)". "Most freelancers" is not "95%". "With minimal cleanup" is not "(One Pan)". The synonym keeps the theme and kills the engine. If your bend reads duller than its source, it failed the floor, no matter how on-brand it sounds.

## Carry the engine at full sharpness

Move the creator's topic onto the title while keeping the load-bearing element recognizable at full strength. Three rules and a test:

- **Fidelity floor:** the engine's form survives. Keep the number, the kicker, the hot proper noun, the named system. Lose the form and the idea has left its evidence behind; the receipt becomes decoration. Reject it.
- **Borrowed numbers and hot words are allowed.** The anti-fabrication rule protects the creator's own claims: their results, their client numbers, their story receipts. It says nothing about the borrowed shape's number, because that number is not the creator's claim, it is part of the cited receipt, quoted in full next to the idea. Keep the source's number ("95%", "in 90 Minutes") or, when the bend genuinely changes the scale, use a bracketed placeholder ("in [N] minutes"). Never invent a figure the source did not have, and never soften the figure it did have.
- **The seed is provisional.** It may stay close to the source (see the next section). What it may never do is bend dull.

Show, don't tell. Source: "95% of Freelancers Invoice Wrong" (@ledgerline, 88k, 9.4x). Engine: the "95%" superiority stat.

- GOOD: "95% of Service Owners Undercharge on Every Invoice." The number survives, the claim moves onto the creator's pricing lane. Side by side, the bend competes with the source.
- FLOOR FAIL: "The Way Most Service Owners Invoice Is Costing Them Money." Theme kept, 95% gone. The source gets the click every time.
- FLOOR FAIL: "How to Run a Carpentry Business With Minimal Overhead", bent from "I Run a $40k a Month Carpentry Business From One Garage (Full System)". "With minimal overhead" is a dull synonym of "From One Garage (Full System)". The kicker was the engine.

**The side-by-side sharpness test.** Put your bend directly under the source line and read the pair the way a scroller would. If the SOURCE gets the click, the bend failed. Sharpen it (restore the form you dropped) or re-roll. Only surface a bend you would honestly click over its source. This test catches the dull bend that every abstract checklist misses, because the comparison is concrete: two lines, one click.

## The seed is provisional by design

The idea line this skill surfaces is a seed for judging WHICH video to make, not the title the video ships with. Two consequences:

- **The seed may stay close to the source.** Adjust the outlier to the creator's topic and stop there. "I Write a Week of Client Emails in 90 Minutes (One Doc)" is a fine seed from the dinners title: same engine, new topic, close phrasing. Closeness is not copying at seed stage; it keeps the shape legible while the creator judges the topic.
- **The do-not-copy ceiling applies to the FINAL title, which `vid-title` crafts later.** After intake captures the creator's real material, `vid-title` writes the actual title from that material, and there the source's phrasing must not survive slot-for-slot. The seed hands `vid-title` the shape plus the full receipt, and it enters as the leading candidate to beat. The ceiling is `vid-title`'s to enforce; it is not a reason to dull the seed.

So the old fear is inverted: the seed's failure mode is not staying too close, it is bending dull. Sharpen freely; the ceiling waits downstream.

## The click test (run on every idea before surfacing)

For each candidate, put it next to the others and ask the real question: scrolling the feed, would the avatar click THIS, and why?

- Run the side-by-side sharpness test against the source first (above). A bend the source beats is already dead.
- A dream outcome beats a defensive reassurance. "Every invoice paid within a week" pulls harder than "...and it works with the spreadsheet you already have". Reassurance is a footnote, not a hook.
- If the strongest thing about the line is that it is on-brand, it fails. On-brand is the floor, not the pull.
- It reads like one line a person would actually say out loud. No crushed, stiff, keyword-stuffed phrasing.
- If you cannot say in one sentence why a human clicks this over the next one, it is not ready.

Do not bend ideas toward the creator's positioning. The differentiator is the creator's flag, and the standing temptation is to staple it onto every line. It belongs only where that difference IS the premise of the video, never as a clause bolted onto a speed or systems line where it dilutes the pull.

## Fit is a floor, checked after pull

Generate for the click first. THEN check fit, as a gate, not a target:

- Inside the iceberg (the boundary in `creator-foundation.md`)? If no, drop it. Off-iceberg never surfaces. This is the only hard fit gate. (`knowledge/iceberg-and-top-3-alignment.md` is the fit check; use its iceberg layer.)
- The Top 3 problems are an OPTIONAL lens, not a requirement. Tag a problem when the idea genuinely serves one, leave it blank when it does not. An idea that is a strong video inside a pillar and inside the iceberg is valid whether or not it maps to one of the three pains. Do not force a problem tag, do not stamp ideas "outlier" for not hitting one, do not require the batch to cover 2 of 3.
- Theory of One (`knowledge/theory-of-one-curation.md`): a shape that wins on every channel can still miss THIS audience. When fit is uncertain, name the tension instead of assuming it transfers.

## Range across the pillars

The territory is the creator's 8 to 12 content pillars, not the 3 pains. A batch ranges across 3-4 different pillars so it does not read as a rut. Pillar coverage is the spread to watch, not problem coverage. Favor own-channel-proven shapes first, then adjacent-niche structures bent onto a pillar (they read as original because nobody in the direct niche runs them yet), then niche-saturated shapes last.

## Signal tiers (what counts as proven)

Read strength from the raw rows:

- **STRONG:** own-channel-proven, OR a Confirmed winner, OR the shape spreads across 5+ channels, OR a single raw row at 15x+ its channel median that also clears that channel's outlier floor. Lead with these.
- **MODERATE:** 3-4 channels, or a single row at 8-15x median that clears the floor.
- **WEAK:** 1-2 channels with no row above 8x. Do not surface as a proven anchor. If interesting, it becomes a flagged swing.
- **SWING:** no proven anchor. A contrarian take, an adjacent-niche structure, or the creator's own backstory. Always flagged `swing (unproven)`. Never dressed as proven.

Two things count as proof and both are real. Spread says a shape is safe to run. A high multiple says one execution actually hit. Never dismiss a high-multiple row as a fluke for not having spread: spread is a lagging indicator, and by the time five channels run a shape it is saturated. Where the two disagree, take own-channel-proven first, then the higher multiple.

The outlier floor is the guard against small-channel inflation, because a low-median channel manufactures big multiples on ordinary videos. The pattern-bank already computes a floor per channel, so use it. A row that clears its floor did real numbers, not just a flattering ratio.

## The default batch (~5-6)

- 4 anchored to STRONG or MODERATE raw titles (favor STRONG and the creator's own winners).
- 1-2 swings, flagged.
- Spread across 3-4 pillars.
- Each idea anchors off a DIFFERENT source row, and no channel appears more than once per batch, swings included. Two ideas off the same channel read as a rut even when the rows differ.
- Never proven-only (the channel goes derivative). Never all-swing (it gambles with no signal).

## Anti-fabrication (hard rule)

Every anchored idea cites a REAL per-channel row: the actual title, @channel, views, xMed. Never invent a title, a view count, a multiple, or a spread. Never cite a row whose engine you did not actually carry into the line, and carrying means the sharp form: a dull synonym keeps the theme and drops the engine, which is a fake citation wearing a real receipt. Swings are flagged unproven, never dressed as proven.

Scope, so the rule is never misread: it protects the CREATOR'S claims (their results, client numbers, story receipts), not the borrowed shape. The outlier's own number and hot words are part of the receipt and are allowed in the line; the receipt is quoted in full right next to the idea, so nothing is hidden.

## Respect the drop list

Skip any idea built on a `Considered + dropped` pattern. If it is genuinely strong, surface the drop rationale and ask before using it. Never silently re-propose a dropped pattern or a `dropped` backlog idea.

## No repeats across sessions

Before proposing, scan the anchors recorded in `content/ideas-backlog.md` (kept and dropped rows both record anchors already). A row already in the backlog may not anchor a new idea unless the creator asks to revisit it. If they ask, say in one line which backlog entry it came from. This is a scan of the backlog as it stands, not a new file and not a new field on the template.

## The dial (Phase 3 postures)

The creator turns the dial; re-roll with the new posture. Same spine, shift the mix or the territory.

- **"more"** -> a fresh batch, same mix. No repeats from this session or the backlog.
- **"tighter" / "safer"** -> all 5-6 anchored to STRONG raw titles, drop the swings.
- **"wilder" / "more original"** -> 3-4 swings, 2 anchored. Contrarian takes, adjacent-niche structures, the creator's unique pillar angles. Still iceberg-gated.
- **"sharper"** -> re-roll the same territory, pushing each line toward its sharpest legitimate form. Restore the dropped number, the parenthetical kicker, the named system, the hot proper noun, then run the side-by-side test on every line. Sharper never means inventing a claim the source did not have; it means stop leaving the source's best phrasing on the table.
- **"different pillar" / "different problem"** -> regenerate aimed there, or rotate to ones the last batch underused.
- **"regenerate"** -> same posture, all new ideas.

Every re-roll shops fresh. Any dial turn (more, regenerate, wilder, different pillar) anchors off rows and channels not yet shown this session. "tighter" may reuse a row already shown, but only to upgrade its signal tier. Never silently re-present the same anchored row twice in one session. Escape valve: if the bank genuinely cannot fill a fresh batch, say so in one line and flag the repeats as repeats.

After any roll, surface the new batch and repeat the one-line dial offer. Do not narrate the change.

## What gets saved and handed off (Phase 4)

Only ideas the creator flags to keep. The unflagged batch is discarded, not logged. The backlog is a curated queue of ideas the creator actually liked, never a dump. See `assets/ideas-backlog-template.md` for the row shape.

The picked idea hands `vid-intake` a seed packet: `{idea_title, pillar, top_3_problem, iceberg_fit, anchor}`. The anchor MUST carry the full receipt: the source title, the @channel, the views, and the xMed, exactly as they appear in the pattern-bank row. The receipt is the seed's evidence chain: `vid-intake` persists it into piece.md and `vid-title` inherits it from there as the leading candidate to beat. A seed packet without the full receipt is a broken handoff.
