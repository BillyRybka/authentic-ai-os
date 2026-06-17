# Idea generation rules

Runtime logic for `vid-ideas` Phase 2 (generate) and Phase 3 (the dial). Not chat content. This is how Claude turns positioning plus evidence into a batch that is sharp, on-channel, and not crappy.

## The raw material

Every idea is built from a cross of three things already loaded:
- A **pillar** (the teaching territory, from the creator's 8-12 pillars)
- A **Top 3 problem** (what the avatar actually complains about, in their words)
- A **signal** (a pattern, outlier, or confirmed winner from `pattern-bank.md` that proves a shape works)

An idea is a pillar's territory, aimed at one avatar problem, wearing the shape of a proven signal, said in the creator's voice. Miss any of the three and it drifts: no pillar means off-positioning, no problem means content-only filler, no signal means a guess.

## Anchor, then adjust (the generative move)

Pick one real outlier and transplant its DNA onto the avatar's named want. Every title does two jobs at once:

- **Structural job:** the frame. List, story, question, challenge, speed claim, concession-plus-payoff, personal testimony.
- **Emotional job:** the trigger. Curiosity gap, loss aversion, desire, pattern interrupt, competence, replacement drama.

Name both, then transplant ONE onto the creator's pillar and problem and rebuild the rest fresh:
- keep the structure, swap the emotional job, or
- keep the emotional job, swap the structure.

**Transplant a job, never the words.** Within a couple of word-swaps of the source = a copy. Reject it. The avatar's want is the headline, not a clause stapled on.

Show, don't tell. Source: "It's Stupid Simple, But It Books Clients Like Crazy" (@channel, 90k, 5x). Structural job: concession plus payoff. Emotional job: pattern interrupt plus desire.
- GOOD (keep structure, swap the emotional job): "It Sounds Too Basic, But Skipping It Is Why Your Videos Flop." Same concession-payoff frame, the trigger is now loss aversion instead of desire.
- GOOD (keep emotional, swap the structure): "The Embarrassingly Simple Trick That Makes Your Content Take Off." Same interrupt-plus-desire trigger, a named-method frame instead of concession-payoff.
- BAD (transcribe): "It's Stupid Simple, But It Makes Content Like Crazy." Same frame, same trigger, same skeleton, nouns swapped. A copy.

Neither GOOD line is a finished title; it is raw material with the right DNA.

One anchor per idea. No fusing two shapes into one line (four competing jobs in one sentence, the viewer skips).

## Signal tiers (what counts as "proven")

Read the anchor's strength from the pattern-bank fields (same logic `vid-framing` uses in `references/angle-anchor-rules.md`):

- **STRONG:** `own_channel_proven: true` (the creator already won with this shape), OR `spread` >= 5 channels, OR a Confirmed winner row. Highest-confidence anchors. Lead with these.
- **MODERATE:** `spread` of 3-4 channels, not own-channel-proven. Real cross-channel signal, lower certainty.
- **WEAK:** `spread` of 1-2 channels. Do not surface as an anchored idea. If a weak pattern is interesting, it becomes an experimental swing (flagged unproven), not a proven anchor.
- **EXPERIMENTAL SWING:** no anchor. The creator's pillar material that does not map to a proven pattern, a contrarian take, or an adjacent-niche shape transferred in. Always flagged `experimental swing (no anchor, unproven)`.

Rank ideas by anchor strength, not by raw view count. A 3x own-channel-proven shape beats a 12x one-channel fluke.

## Differentiation tiebreaker

On a tie between equally strong anchors, prefer the one that differentiates this creator:
- **Own-channel-proven** first. Repeat what already won here.
- **Adjacent-niche shapes** bent onto this pillar next. They read as original because nobody in the direct niche runs them yet.
- **Niche-saturated shapes** last. Proven but derivative.

## The default batch (~5-6)

- 4 anchored to STRONG or MODERATE signals (favor STRONG, favor the creator's OWN winners first, then convergent patterns, then niche-specific).
- 1-2 experimental swings, flagged.
- Spread across at least 2-3 different pillars and at least 2 of the Top 3 problems, unless the creator gave a focus. One pillar, one problem, six ideas reads as a rut.

Never proven-only (the channel goes derivative). Never all-experimental (the channel gambles with no signal).

## How the batch is built (vet each, then present the set)

Build and vet one idea at a time, internally. Per idea:
1. **Pick a slot:** a pillar + a Top 3 problem the batch has not covered yet.
2. **Find the anchor:** the strongest REAL pattern-bank shape that serves that slot (own-channel-proven first, then high spread, then an adjacent-niche shape for differentiation).
3. **Decompose and transplant** per Anchor, then adjust.
4. **Run the gate below.** Pass = hold it. Fail = throw it out and re-pick. Never surface a failed idea.
5. Repeat until the mix is filled (the default batch above).

Then surface only the ideas that passed.

## The per-idea gate (run before surfacing)

Every idea clears every check below before it is shown. Fail any one = re-pick, do not surface.

1. **Anchor or flag, never fake, and show the receipt.** Every anchored idea cites a REAL `pattern-bank.md` outlier as a receipt: the actual title + @channel + views + xMed (the multiple of that channel's median). Never invent an outlier, a view count, a multiplier, or a spread. If you cannot anchor it and it is not a deliberate swing, drop it.
2. **Transplant a job, never the words.** Name the anchor's structural job (the frame) and emotional job (the trigger), then transplant one onto the creator's pillar and problem as a fresh line. Handing back the source with its nouns swapped is a transcribe.
3. **Iceberg gate first.** Run the 2-layer check (`knowledge/iceberg-and-top-3-alignment.md`) before surfacing. Inside iceberg + lands on a Top 3 problem = clean, lead with these. Inside iceberg + no Top 3 = allowed, flagged `outlier_within_iceberg`. Off iceberg = never surfaced.
4. **Theory of One.** A pattern that works on every channel in the niche can still miss THIS audience's expectation of the creator. When an anchor is niche-wide but the fit is uncertain, name the tension (per `knowledge/theory-of-one-curation.md`) instead of assuming it transfers.
5. **Respect the drop list.** Skip any idea built on a `Considered + dropped` pattern. If it is genuinely strong, surface the drop rationale and ask before using it. Never silently re-propose a dropped pattern or a `dropped` backlog idea.
6. **Specificity bar.** A category is not an idea. "Pricing" fails. "The pricing mistake that makes clients ghost after the proposal" passes. If you cannot say the specific tension in one line, the idea is not ready.
7. **Idea-line bar (read-aloud, not char count).** Two checks: it reads like one phrase a human would actually say, and it mirrors the source outlier's shape and length. No character limit, never crush a line to save space (crushing kills the shape).
8. **No invented numbers.** A specific figure in an idea line (minutes, percent, count) is either the borrowed shape's own number or a bracketed placeholder (`in [X] minutes`, `[N] lessons in [N] years`). Never invent one.

## The dial (Phase 3 postures)

The creator turns the dial; re-roll the batch with the new posture. Keep the same shape and tags, just shift the mix or the territory.

- **"more"** -> generate a fresh batch of the same shape (new ideas, same default mix). Do not repeat ideas already surfaced or in the backlog.
- **"tighter" / "safer"** -> drop the experimental swings. All 5-6 anchored to STRONG signals only (own-channel-proven and Confirmed winners first). Lowest crap risk, least range.
- **"wilder" / "more original"** -> flip the mix: 3-4 experimental swings, 2 anchored. Push contrarian takes, adjacent-niche transfers, and the creator's unique pillar angles. Higher risk, more voice. Still iceberg-gated; wild does not mean off-channel.
- **"different pillar" / "different problem"** -> regenerate aimed at the named pillar or problem (or rotate to ones the last batch underused).
- **"regenerate"** -> same posture, all-new ideas.

After any roll, surface the new batch and repeat the one-line dial offer. Do not narrate the change.

## What gets saved (Phase 4)

Only ideas the creator flags to keep. The unflagged batch is discarded, not logged. The backlog is a curated queue of ideas the creator actually liked, never a dump of everything generated. See `assets/ideas-backlog-template.md` for the row shape.
