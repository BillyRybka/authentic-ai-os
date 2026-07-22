---
type: bank
kind: title
project: authentic-ai-os
status: active
last_refreshed: 2026-07-20
total_patterns: 9
tags: [title-bank, fixture, synthetic-persona]
---

# Title Bank

Fill-in-the-blank title shapes for Nora's audience (the weekend woodworker who owns more tools than finished pieces). Each heading IS the template. One template, one pattern. Worked examples come from the [[pattern-bank]] outlier set. Loaded by `vid-title`.

> [!warning] Synthetic test fixture
> Every worked example below is invented for the eval. The schema mirrors a real title bank so the skill runs end to end.

This file is both the research output and Nora's curated set. Edit in place: delete shapes that don't sound like you, reword the slots, add winners over time.

## How to read this bank

Each heading is a STRUCTURE, not a phrase. The `[SLOTS]` get filled with your actual content. Spread (how many of the 12 analyzed channels used the pattern) and the channels show repeatability. No confidence rank: the spread is the signal. All nine below were kept in the curation pass.

## Patterns

### `Why [common beginner belief] Is [a blunt flip]` / `Why [underdog] Build the BEST [outcome]`

- pattern_id: contrarian-identity
- spread: 2 of 12 channels (both direct)
- channels: [[@wrenhalloran]], [[@maplemaineco]]
- own_channel_proven: false

**Why it lands:** it contradicts the advice the audience hears everywhere (save up, buy the shop, then start), so the click is "wait, what?" This is the closest shape to Nora's whole positioning (against the dream-shop default).

**Worked examples:**
- "Why Beginners Build the BEST Furniture (Nobody Talks About This)" → [[pattern-bank]] (@wrenhalloran, 126k)
- "Why Garage Shops Make Better Furniture" → [[pattern-bank]] (@maplemaineco, 49k)

**Near-miss:** "Why You Should Start Woodworking." Agrees with the default. No tension, no click.

**When not to use:** when you don't actually hold the contrarian position. A faked reversal collapses trust, which is the one thing this brand cannot spend.

### `DON'T [common practice]. [Do the better thing] Instead`

- pattern_id: contrarian-correction
- spread: 5 of 12 channels
- channels: [[@maplemaineco]], [[@wrenhalloran]], [[@salvageandsaw]], [[@workshopwars]], [[@builtbybea]]
- own_channel_proven: false

**Why it lands:** names a thing the viewer is probably doing, says it's wrong, and promises the fix. Variants: "You've Been [X] the Hard Way," "Stop [X] WRONG."

**Worked examples:**
- "DON'T Buy Another Tool, Build the Bed Frame First!" → [[pattern-bank]] (@maplemaineco, 86k)
- "Stop Sharpening Your Chisels WRONG (Do This Instead)" → [[pattern-bank]] (@maplemaineco, 56k)
- "You've Been Sawing the Hard Way (Do This Instead)" → [[pattern-bank]] (@workshopwars, 1.7M)

**Near-miss:** "Stop Making These Mistakes." No specific practice named, no replacement promised.

**When not to use:** when you can't name the specific wrong thing AND the specific replacement. The pairing is the pattern.

### `I Built [specific outcome] (No Shop)` / `[outcome] With No [expensive tool]`

- pattern_id: no-shop-build
- spread: 4 of 12 channels
- channels: [[@wrenhalloran]], [[@builtbybea]], [[@twoboardtom]], [[@northfielddiy]]
- own_channel_proven: false

**Why it lands:** it's the avatar's exact dream stated as proof: real furniture without the dream shop. Variants: "I Furnished My Whole [space] With [N] Tools," "I Quit My [big tool] for [N] Days."

**Worked examples:**
- "I Built a Whole Bedroom Set With No Table Saw (No Shop)" → [[pattern-bank]] (@wrenhalloran, 37k)
- "I Furnished My Whole Apartment With 5 Tools (No Shop)" → [[pattern-bank]] (@builtbybea, 115k)

**Near-miss:** "Woodworking on a Budget." No build named, no constraint tension.

**When not to use:** when the outcome is vague. "(No Shop)" only pays off against a concrete, normally-needs-a-real-shop result.

### `[Tool] Just [Dropped / Changed] [your domain]`

- pattern_id: news-jack-release
- spread: 2 of 12 channels (concentrated in the tool-review circle)
- channels: [[@coppercreekshop]], [[@sawdustempire]]
- own_channel_proven: false

**Why it lands:** rides a fresh release the gear-watching audience is already curious about, and ties it to their shop. Pairs with the News format.

**Worked examples:**
- "Copper Creek Just Dropped a Self-Squaring Track Guide (First Cut)" → [[pattern-bank]] (@coppercreekshop, 133k)
- "The New Meridian Track Saw Just Changed Straight Cuts" → [[pattern-bank]] (@coppercreekshop, 118k)

**Near-miss:** "A New Tool Was Announced." No named tool, no stakes, no shop.

**When not to use:** when the release is stale by the time you publish. This shape decays fast; speed is the whole game. And never borrow a measured claim you haven't made yourself.

### `[Outcome] in [N] Minutes` / `The [N]-Minute [Finish]`

- pattern_id: speed-mastery
- spread: 3 of 12 channels
- channels: [[@maplemaineco]], [[@finegrainfilms]], [[@thedovetaildaily]]
- own_channel_proven: false

**Why it lands:** specific outcome + a small time cost = low-risk click.

**Worked examples:**
- "The 15-Minute Finish That Doubled My Prices" → [[pattern-bank]] (@maplemaineco, 71k)
- "The 3-Year Tool Cabinet, Finished in 18 Minutes" → [[pattern-bank]] (@finegrainfilms, 233k)
- "The Quiet Joy of a Perfect Shaving (21 Minutes)" → [[pattern-bank]] (@thedovetaildaily, 616k)

**Near-miss:** "Learn Hand Planing Fast." No number, no time, no specific outcome.

**When not to use:** when the video can't actually deliver the outcome in the stated time. The promise has to be true.

### `[N]% of Beginners [Do X] Wrong` / `How to [do X] Better Than 99% of People`

- pattern_id: better-than-masses
- spread: 3 of 12 channels
- channels: [[@twoboardtom]], [[@workshopwars]], [[@maplemaineco]]
- own_channel_proven: false

**Why it lands:** positions the viewer to join the skilled minority (or escape the failing majority). Status hook.

**Worked examples:**
- "90% of Beginners Hold a Handsaw Wrong" → [[pattern-bank]] (@twoboardtom, 38k)
- "How to Saw Straighter Than 99% of Beginners" → [[pattern-bank]] (@workshopwars, 1.1M)

**Near-miss:** "How to Saw Well." No comparison, no stakes.

**When not to use:** when you can't actually show the gap between the 99% and the 1%. The body has to earn the claim.

### `From [failure] to [specific result] in [time period]` / `[cheap materials] to [sold piece]`

- pattern_id: result-proof
- spread: 3 of 12 channels
- channels: [[@twoboardtom]], [[@salvageandsaw]], [[@northfielddiy]]
- own_channel_proven: false

**Why it lands:** the ruined-to-sold arc is this niche's trust engine. A specific failure count plus a specific result reads as earned, and the viewer fills in "how."

**Worked examples:**
- "From 9 Ruined Boards to a $3,800 Table in 90 Days" → [[pattern-bank]] (@twoboardtom, 120k)
- "I Turned a Free Pile of Barn Wood Into a $2,600 Table" → [[pattern-bank]] (@salvageandsaw, 89k)
- "I Built a $4,200 Barn Door for $190 (Full Build)" → [[pattern-bank]] (@northfielddiy, 195k)

**Near-miss:** "How I Got Good at Woodworking." No count, no result, no timeframe. This is the slop version.

> [!warning] When not to use
> Only put a number on the title you can actually stand behind. Use Nora's real proof (Dana's counted 11 boards and $2,400 first sale). Never a fabricated price or count. A made-up number is the exact slop this brand is built against, and it's the fastest way to lose the trust.

### `[N] [things] I Can't Live Without (steal my kit)`

- pattern_id: steal-these
- spread: 2 of 12 channels
- channels: [[@twoboardtom]], [[@northfielddiy]]
- own_channel_proven: false

**Why it lands:** generosity hook. "Steal" signals you're handing over something real, not gatekeeping.

**Worked examples:**
- "11 Hand Tools I Can't Live Without (steal my kit)" → [[pattern-bank]] (@twoboardtom, 80k)
- "The 7-Tool Homestead Kit (No Tractor Required)" → [[pattern-bank]] (@northfielddiy, 125k)

**Near-miss:** "My Favorite Tools." No generosity verb, no count, no take-it-now energy.

**When not to use:** when there's nothing concrete to actually hand over. "Steal" promises a deliverable.

### `The Only [X] You'll Ever Need`

- pattern_id: definitive-resource
- spread: 2 of 12 channels
- channels: [[@coppercreekshop]], [[@builtbybea]]
- own_channel_proven: false

**Why it lands:** promises to end the search. One video to rule the topic. Saves the viewer from the tool-review rabbit hole.

**Worked examples:**
- "The Only Chisel Buying Guide You'll Ever Need" → [[pattern-bank]] (@coppercreekshop, 68k)
- "The Only Beginner Tool List You'll Ever Need" → [[pattern-bank]] (@builtbybea, 33k)

**Near-miss:** "A Guide To Buying Tools." No finality, no relief.

**When not to use:** for a narrow or fast-changing topic where "only/ever" is obviously false.

## Considered + dropped

- **Shop-tour reveal** `My [size] Shop Tour` (dropped 2026-07-20). Off-iceberg: feeds tool collecting, pulls browsers not builders.
- The result-proof shape was kept active with the real-number guardrail (see its "When not to use").

## Pattern combinations

Some shapes stack. Worked examples by pattern_id:

- `news-jack-release` + `contrarian-correction`: "The New Meridian Track Saw Just Changed Straight Cuts" (@coppercreekshop). A release tied to a "your setup ritual is dead" correction.
- `speed-mastery` + `result-proof`: "The 15-Minute Finish That Doubled My Prices" (@maplemaineco). Speed promise carrying a money result.
- `no-shop-build` + `steal-these`: "The 7-Tool Homestead Kit (No Tractor Required)" (@northfielddiy). A kit handover pinned to a missing machine.

## Field reference

- **Heading**: the template, backticked. `[SLOTS]` are the variables you fill.
- **pattern_id**: stable kebab slug. What `pattern-bank.md` studied rows link to.
- **spread**: `{N} of {M} channels`. Repeatability across the research set. No HIGH/MEDIUM/LOW label.
- **channels**: wikilinks to where the pattern appeared.
- **own_channel_proven**: whether proven on Nora's own channel. All false this build (no published winners on the current positioning yet).
- **Why it lands / Worked examples / Near-miss / When not to use**: the fit reason, real proof, the failure mode, the authenticity guard.
