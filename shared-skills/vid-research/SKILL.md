---
name: vid-research
description: Builds and refreshes the creator's pattern banks from real YouTube data. Runs Three-Circle Research across the creator's own channel, direct competitors, and adjacent niches. Produces pattern-bank, title-bank, and power-words-bank plus a starting packaging system. Use for a first build, a quarterly refresh, or capturing a single outlier. Triggers on "build my pattern bank", "refresh my research", "I just saw an outlier", "research my niche", or "what's working in my niche right now".
---

# Video Research

Builds and refreshes the creator's three pattern banks. Pattern banks are the raw research outputs that vid-framing and vid-title load at runtime to ground every decision in evidence rather than guesses. The skill handles the full Three-Circle Research workflow (own channel + 5 niche competitors + 3-5 adjacent niche channels), the YouTube data fetch, the thumbnail vision analysis, the cross-channel pattern synthesis, and the Theory of One curation pass with the creator.

This skill exists because the alternative, making videos based on what the creator THINKS will work, is the dominant failure mode for business channels. Pattern research turns guesses into hypotheses backed by the data of what audiences actually click, watch, and come back for. The pattern bank is the difference between shipping a video that aligns with proven outliers and shipping a video that feels right but flops.

**Scope boundary:** vid-research builds/refreshes pattern banks. It does NOT pick angles for a specific video (that's vid-framing). It does NOT lock titles or thumbnails (that's vid-title and vid-thumbnail). It does NOT track post-publish winners (that's vid-measurement, future). It produces the research substrate every other skill consumes.

## What this produces

Three bank files in `banks/`:

- `pattern-bank.md`: the outlier evidence + cross-channel synthesis. A full inventory of every qualifying outlier per channel (the whole set, not just the top performer), plus full-package rows for the studied subset (title linked to video URL, channel, view count, outlier multiplier, pub date, thumbnail image + strategy + text + hero element, patterns linked to the sub-banks by `pattern_id`). Plus the synthesis sections (convergent / niche-specific / adjacent / unique), each pattern tagged with `spread` (how many channels, which ones) and `own_channel_proven`. Plus topic clusters folded into synthesis (own + niche only, NEVER adjacent). Plus Considered+dropped and Confirmed winners sections. The creator's entry point for browsing what works for their audience and the file vid-framing loads for angle selection.
- `title-bank.md`: fill-in-the-blank title shapes with worked examples (linked back to outlier rows) and near-miss anti-patterns. Research output + creator's curated set in the same file (creator edits in place, deleting patterns they would not use). vid-title loads this.
- `power-words-bank.md`: a comprehensive word list mined from the FULL title set, not a token few. Global (pull on any audience) + Audience-specific (resonate uniquely for this creator's audience). Each entry: word, when-it-lands, when-it-fails, worked example linked back to an outlier row. No frequency or confidence ranks (that is what "lean" means, no junk, not a short list). A 100-plus-title set should yield a couple dozen words. vid-title loads this.

**Not banks (by design):**
- format is a menu pick, not a mined pattern (a competitor's format cannot reliably be classified from title + thumbnail + metadata without transcripts; format comes from `references/format-rotation-guide.md`, set in Phase 7)
- thumbnail patterns live in the pattern-bank outlier rows, not a separate file. Future `vid-thumbnail-gen` queries those rows by strategy for visual references
- topic clusters fold into pattern-bank synthesis, not a standalone file
- "what the audience hates" is post-publish flop diagnosis (future vid-measurement), not pre-research collection

Plus one synthesis artifact: `foundation/packaging-system.md`. vid-research authors the creator's starting packaging defaults FROM the evidence it just gathered (format rotation picked from the `references/format-rotation-guide.md` menu, thumbnail strategy from the strategy distribution observed in outlier rows). This file is read by vid-framing, vid-title, vid-thumbnail, vid-structure, and vid-pressure-test. Packaging defaults are a research output, never a pre-research guess. Design guardrails and the creation path are NOT authored here; they are deferred to vid-thumbnail once the creator has made real thumbnails. First-build packaging covers the format rotation and the thumbnail strategy bet only.

## When to run this

- **First build (Mode 1):** creator has just run /foundation. No pattern banks exist yet. Run vid-research before vid-framing for the first time. (Voice capture is still in development; it is not a prerequisite.)
- **Quarterly refresh (Mode 2):** 90+ days since `last_full_rebuild` in `pattern-bank.md` frontmatter. Or when new outliers have stacked up the creator wants surfaced.
- **Single outlier add (Mode 3):** creator spotted an outlier between rebuilds and wants to capture it without a full session.

If the creator runs vid-framing without any pattern banks present, vid-framing should redirect them to vid-research first.

## Prerequisites

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` in this skill is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

Hard requirements:

- `foundation/iceberg.md` and `foundation/avatar.md` exist. vid-research reads the iceberg statement and content pillars from iceberg.md and the audience profile from avatar.md to help the creator name their competitors and to suggest a few only if they're stuck. A vault still on the old single-file `creator-foundation.md` migrates first via `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`.
- YouTube Data API key configured. The key lives in a `.env` file at the vault root as `YT_API_KEY=...`. `.env` is gitignored and the key is NEVER written into any skill file, committed, or saved to the foundation docs. `creator-setup` scaffolds a `.env.example` with the `YT_API_KEY=` line; the creator copies it to `.env` and pastes their key. The `youtube_fetch.py` script reads `YT_API_KEY` from the environment. If first run and no key is set, walk the creator through `assets/api-key-setup-guide.md` (5-minute Google Cloud Console flow), then have them put the key in `.env`.

Soft requirements:

- `foundation/voice-profile.md` for mirroring style during the conversation. Skill works without it but feels less personal.
- Existing pattern banks (Mode 2 / Mode 3 only). Mode 1 starts from empty.

## Invocation modes

**Standalone:** creator invokes directly. Skill detects which mode based on existing bank state. Runs the matching flow.

**Sub-skill:** vid-pipeline (future) may invoke during onboarding. Returns a status packet ("banks built / refreshed / outlier captured + N entries").

## The 5 phases (Mode 1, first build)

Mode 2 (refresh) runs the same phases but skips already-validated channels and surfaces only NEW outliers. Mode 3 (single add) runs Phase 4-6 directly with one channel and one outlier.

### Before you research: load the method

The rigor of this skill lives in a few files, not in this orchestrator. Load them before you select, judge, or extract from any channel, so you run the method instead of improvising it. Skipping this and ranking channels by gut is the known failure mode.

- `references/three-circle-research.md`: the workflow and the channel-selection order.
- `references/outlier-identification-rules.md`: what counts as an outlier (the per-channel scaled floor, the fluke filter, spread).
- `references/pattern-extraction-prompts.md`: how to extract power words and title patterns, and run the fluke check.
- `knowledge/interview-posture.md`: how to talk to the creator.

Path resolution: `knowledge/` files live at `${CLAUDE_PLUGIN_ROOT}/knowledge/` when installed, or repo-root `knowledge/` in dev, never the skill folder. `references/` and `scripts/` are skill-local. Running against a separate vault does not change this; the method files stay plugin-side.

Load silently. Never narrate it to the creator.

### Phase 1: Setup and own-channel research

**Setup checks (silent unless missing):**

1. `foundation/iceberg.md` and `foundation/avatar.md` exist → load the iceberg statement, pillars, and audience; top 12 outliers if existing channel.
2. YouTube Data API key configured as `YT_API_KEY` in a `.env` file at the vault root (see Prerequisites). If missing, walk through `assets/api-key-setup-guide.md` first.
3. Test API call against creator's own channel handle. If fails, walk creator through troubleshooting (key invalid, channel handle wrong, quota exhausted).

**Own channel pull:**

4. Confirm the creator's own channel handle. If it's saved in their foundation, reflect it back ("Your channel is @handle, right?"). If it isn't saved, just ask for it in one plain line. Asking is normal here, not an error.
5. Confirm the research window in one plain line: default last 12 months, offer to expand to 24 if a channel posts rarely and 12 is too thin. Then run `scripts/youtube_fetch.py --handle {creator-handle} --days {window}` (365 for 12 months). Returns JSON with channel metadata, the median view count, posting cadence (videos per window), and per-video data (`title, view_count, video_id, thumbnail_url, published_at`).
6. Set the channel's outlier floor: from the median and posting cadence, propose a floor scaled to the channel (start at 2x median, real bar ~3 to 4x for normal cadence, higher for hyper-cadence, mega-only for giants), say it plainly, and let the creator confirm or adjust (see `references/outlier-identification-rules.md`). Record EVERY video that clears the floor as a full inventory row in `pattern-bank.md`. The whole set, never just the top performer.
7. **Run the fluke filter on every outlier.** For each outlier, AI summarizes the channel's primary themes from the last 30 video titles, then checks "is this outlier on-niche for this channel?" Off-niche flukes get flagged: "This 700K-view video is about [topic], but the channel is about [primary themes]. Likely a fluke. Skip, or study?" Default skip. See `references/pattern-extraction-prompts.md` for the fluke detection prompt.
8. For the studied subset (top ~10 own-channel outliers prioritized; the rest stay in the inventory URL-saved without vision): pull thumbnail via `scripts/thumbnail_download.py`, run vision classification per `references/thumbnail-vision-classification.md` (which of 6 strategies, hero element, color palette, text content, expression).
9. Extract patterns per `references/pattern-extraction-prompts.md`: power words (global + audience-specific), title patterns, thumbnail patterns. Capture topic clusters into the pattern-bank synthesis (own + niche only).
10. **Save partial state:** append draft entries to `pattern-bank.md` per-channel section + draft entries flagged `status: draft-pending-curation` to relevant banks (`power-words-bank.md`, `title-bank.md`). Thumbnail strategy and visual data live IN the outlier rows of pattern-bank, not a separate bank. Frontmatter `last_phase_completed: 1` so resume works if session ends here.

### Phase 2: Niche research (the creator's direct competitors)

Ask the creator first, they know their world. You bring the expertise: pull real data on every channel they name, read it, and propose where each belongs. They make the final call. (Method loaded first, see above.)

**Build the niche set with the creator:**

1. Ask one plain question: "Who are your top competitors? The channels making the kind of content you want to be known for, for the same viewer, the ones with videos that clearly took off." Then listen. (What you are checking for, silently: same audience, real outliers in the last couple of years.)

2. Pull data on every channel they name, including the tentative ones. If they say "maybe so-and-so," pull it anyway, the numbers are how you both decide. Hear the whole list first. If they name only a couple, ask once if there are more, then move on.

3. If the creator doesn't know their competitors, that's normal. Lead: suggest a few real channels you believe fit, each with a one-line reason, built from anyone they named plus the known players in that space. Never open with a generated list, and don't hunt for new channels while they're still naming their own.

4. For each channel, named or suggested, run `scripts/youtube_fetch.py`, then show the real picture in plain terms and propose a bucket:
   - **Direct competitor**: same viewer, same kind of content. Studied fully, topics included.
   - **Adjacent**: same style or packaging, different topic or industry. Carries to Phase 3 (structure only, never topics).
   - **Skip**: no real outliers, or off the creator's niche.

   Outliers are the signal. A channel with a modest typical view count but real breakout videos still has patterns worth studying, so don't write it off for low averages. Big channels are not off-limits either. You study a big channel's packaging (titles, thumbnails, hooks, formats) exactly like any channel. The only difference is you do not benchmark their view counts (their reach rides on an audience the creator does not have yet) and you flag fame-driven spikes (a breakout that took off on the host's name or a guest's fame, not on its packaging) so the creator does not chase a number the packaging alone cannot reproduce. Present the data and your read; the creator decides the bucket. Don't assert taste as fact ("elite packaging"); show what the data says and let them judge fit.

5. Confirm the set. Aim for about five direct competitors, but follow the creator.

**Per-channel research on the confirmed competitors (silent, same engine as Phase 1):**

6. From the pulled data, set the channel's scaled floor and record every outlier that clears it as full inventory (`references/outlier-identification-rules.md`).
7. Run the fluke filter. Surface a fluke only when it needs the creator's call: "This big one is about [topic], off from what that channel usually does. Worth studying, or skip?"
8. The top 5 outliers per channel are the studied subset and get thumbnail vision analysis; the rest stay inventory-only.
9. Extract patterns.
10. **Save partial state** after each channel. Frontmatter `last_phase_completed: 2`, `niche_channels_done: [list]`.

### Phase 3: Adjacent research (same style, different topic)

Adjacent channels make a similar kind of content for a different topic or industry, the kind of thing the creator's viewer might also watch. They give you structure that transfers (title shapes, thumbnail moves, formats), never topics.

1. Most adjacent channels come straight from Phase 2: the ones bucketed adjacent. Research those here.
2. If the creator wants broader coverage and is short on names, lead: name two or three adjacent areas drawn from their niche (from their foundation, not hardcoded) and suggest a channel or two per area, each with a plain reason, validated against real data. Ask if any fit.
3. Aim for three to five. If there are none, that's fine, the research still ships on the niche alone (the bank is thinner, say so once and move on).

**Per-channel research (silent):**

4. Pull, set the scaled floor, record every outlier as full inventory, run the fluke filter.
5. The top 3 outliers per channel are the studied subset and get thumbnail vision analysis; the rest stay inventory-only.
6. Capture title structures, power words, thumbnail patterns, formats. Never capture topics from adjacent niches, the structure transfers, the subject matter does not. This is the one rule that keeps the bank clean.
7. **Save partial state.** Frontmatter `last_phase_completed: 3`, `adjacent_channels_done: [list]`.

### Phase 4: Cross-channel synthesis

**LLM synthesis pass:**

1. AI loads all draft entries from Phases 1-3.
2. Identifies CONVERGENT patterns: which power words appear across 5+ channels? Which title structures appear across the niche set? Which thumbnail strategies converge between niche and adjacent (strongest signal)?
3. Identifies UNIQUE patterns: what's distinctive to one channel that may or may not transfer?
4. Builds a spread-ranked pattern brief: `pattern X, spread 8 of 11 channels, own_channel_proven true; pattern Y, spread 4 of 11; pattern Z, spread 2 of 11 (thin, may be noise)`.
5. Appends synthesis to `pattern-bank.md` `## Synthesis` section as draft.
6. **Save partial state.** Frontmatter `last_phase_completed: 4`.

### Phase 5: Theory of One curation pass (the human filter)

This is the irreplaceable step. AI surfaces every draft pattern in spread-ranked order (widest spread and own-channel-proven first). Creator hits Keep / Drop / Modify per pattern.

**Surface format per pattern:**

```
> Pattern: titles that open with "STOP [common practice]"
> 
> Strong signal. It showed up on 8 of the channels you picked.
> From your research:
> 1. "STOP Using These 5 Outdated Hook Patterns" (@chan1, 1.4M views)
> 2. "STOP Recording Without This Setting" (@chan2, 800k views)
> 
> Does this sound like you? Like something you'd actually title a video?
> 
> Keep it, drop it, or reword it so it sounds like you?
```

Show the signal in plain language: how many of their channels it showed up on, and whether it is proven on their own channel. Say "it showed up on 8 of the channels you picked," not "confidence HIGH." The creator just needs to know it is widespread, somewhat spread, or a long shot, and whether it fits them.

Creator hits Keep, Drop (with optional one-line rationale), or Modify (rewrites the pattern in their own framing).

**Bulk-keep mode:** for wide-spread patterns the creator clearly wants, batch confirmation: "I'm bulk-keeping 8 wide-spread patterns. Want to skim them or trust the synthesis?"

**Sticky-curated growth (Mode 2 only):** patterns previously curated as Keep persist with `last_validated: {date}` updated. Patterns previously Dropped move to `## Considered + dropped` appendix with rationale, and don't get re-surfaced this session.

**Drop rationale capture:** when a pattern is dropped, ask "one line on why so future runs don't re-surface this?" Common reasons: "doesn't fit my audience's expected tone", "tested in past, flopped", "feels generic", "off-brand for me". Captured rationale prevents re-surfacing and trains the AI's proposal logic over time.

After curation, all `status: draft-pending-curation` entries either become `status: curated` (Keep), get rewritten (Modify), or move to dropped appendix (Drop).

### Phase 6: Save and confirm

1. Final write: `pattern-bank.md` with synthesis + topic clusters + per-outlier packages updated, all 3 banks with curated entries promoted, dropped patterns archived, frontmatter timestamps updated.
2. Confirm with a short, plain message. Not a stats table read aloud. Something like:

```
Done. I went through the channels you picked and pulled out the titles, thumbnails, and hooks that are actually working in your space. The ones that fit you are saved and ready to use.

When you want to plan your next video, run vid-framing. It pulls straight from this.
```

If the creator wants the numbers (how many channels, how many kept), give them, but don't lead with them. The counts and the suggested next-refresh date live in the file's frontmatter either way.

3. Frontmatter on `pattern-bank.md` updated: `last_full_rebuild: today`, `last_refresh: today`, `pattern_count: N`, `status: active`. Suggested next refresh is about 90 days out, stored here, not announced as a deadline.

### Phase 7: Author packaging-system.md from the evidence

The 3 banks are saved. Now synthesize the creator's starting packaging defaults. Keep this LIGHT at first build: it is two evidence-driven pieces, not a full identity doc. The creator has no published videos on the new positioning, so everything here is a starting bet, not a lock. Load `references/packaging-system-template.md` for the output shape and `references/format-rotation-guide.md` for the format menu. Author only:

1. **Starting format rotation (3 core + 1 experimental).** Format is a menu pick, NOT a mined pattern. Load `references/format-rotation-guide.md`: it holds the fixed 7-format menu (with Views/Sales/Trust scores), the Rule of 3+1, and the 4-check filter. Propose 3 core + 1 experiment from the menu based on the creator's avatar, strengths, and own-channel data if any, run the 4-check filter, creator confirms. Confidence is generally low at first build (no published data on the new positioning yet); that is expected and honest. The experiment-promote/retire loop is post-publish, deferred to future vid-measurement.
2. **Thumbnail strategy (1-2 to test).** Pull from the thumbnail strategy distribution in `pattern-bank.md` outlier rows. Name the strategy, cite the example outliers it came from, mark confidence.
3. **Title-bank seed.** `banks/title-bank.md` is already written in Phase 6 directly from research. Verify it has the patterns this packaging-system points at; no separate seeding step.
4. **Design guardrails + creation path: do NOT author these at first build.** Omit them from the file entirely. They need production data the creator does not have yet (exact colors, fonts, face rules, DIY-vs-AI workflow), and `vid-thumbnail` owns them once the creator has actually made thumbnails. First-build packaging-system is the format rotation (step 1) plus the thumbnail strategy bet (step 2). Nothing more.

Every evidence field carries: `evidence_basis` (which bank + how many channels), `confidence` (high/medium/low), `watch_for` (the signal that would invalidate it after real videos publish). This makes packaging-system.md a tested hypothesis, not a locked guess. Confirm the synthesis with the creator (propose, they react, lock) before saving.

Save to `foundation/packaging-system.md`. Then add one plain line to the Phase 6 message: you also set up their starting packaging playbook (the formats to lean on, a thumbnail approach to test, and a few title ideas to start from), saved with their foundation.

### Mode 2 (quarterly refresh) flow

Detected when `last_full_rebuild` exists in `pattern-bank.md` and is 60+ days old.

- Phase 1 reuses creator's own channel handle, pulls only videos published since `last_refresh`. Identifies NEW outliers since last session.
- Phase 2 reuses the 5 niche channels. Pulls only NEW videos. NEW outliers extracted.
- Phase 3 reuses the adjacent channels OR offers refresh: "Want to swap any adjacent niches? Yours from last session: [list]." Default keep, optional swap.
- Phase 4 synthesis runs against new data merged with existing curated entries.
- Phase 5 curation only surfaces NEW patterns. Existing curated entries stay sticky unless creator explicitly invalidates them ("this pattern stopped working, drop it").
- Phase 6 save updates `last_refresh`, leaves `last_full_rebuild` alone.

### Mode 3 (single outlier add) flow

Detected when creator opens with "I just saw an outlier" or similar phrasing.

1. Creator drops the video URL or channel + title.
2. Skill pulls the channel context (themes from last 30 videos), identifies if outlier is on-niche, runs fluke filter.
3. If confirmed outlier: thumbnail vision analysis, pattern extraction.
4. Theory of One filter on the extracted patterns.
5. Append to relevant banks. Update `pattern-bank.md` synthesis if patterns shift.
6. Done in 5-10 minutes.

## Conversational discipline

Load `knowledge/interview-posture.md` and follow it: one question at a time, plain words, absorb before you ask again. This skill runs a lot of machinery; the creator should never feel it. A few rules specific to this skill:

- **Expert-led, creator-decided.** You are the strategist in the room. Lead: pull the data, read it, propose buckets and patterns, teach what matters in plain terms. The creator brings knowledge of their world and makes the final calls. Don't make them drive, and don't make them feel they need to know YouTube strategy to use this.
- **Data first.** When the creator names a channel, even a "maybe," pull the real numbers before judging it. Confirm on facts, not vibes. Never open with a list you generated, and don't hunt for new channels while they're still naming their own.
- **Keep the machinery silent.** Medians, the scaled floor, posting cadence, the fluke filter, vision analysis, quota, draft states: that is how you think, not how you talk. Surface a number only when the creator has a decision to make, and say it plainly.
- **Make curation fast.** Offer to bulk-keep the obvious winners and skip the obvious no's. Don't march the creator through thirty questions.
- **Talk straight about big channels.** Channels are channels. A big channel's outliers still teach packaging (the titles, thumbnails, hooks, and formats transfer), so study them. Just never promise their reach. Say the packaging is worth stealing and the view count is theirs, not a target the creator can hit yet (a channel with a big following pulls numbers off that following, not off the thumbnail). Flag a fame-driven spike when you see one so the creator studies the move, not the magnitude.
- **Obsidian output.** The bank files use Obsidian syntax (embedded thumbnails, callouts, wikilinks). The creator reads them there, not as raw text.
- **Save after every phase**, so a dropped session resumes at `last_phase_completed + 1`.

## Hard friction (auto-flag)

1. **Foundation missing.** Don't run without `foundation/iceberg.md` and `foundation/avatar.md`. Tell creator to run /foundation first.
2. **API key missing or invalid.** Walk through setup before proceeding. Don't skip with "we'll just use LLM knowledge of channels", that's hallucination territory.
3. **Off-niche outliers (flukes).** Default skip. Creator can override only with explicit Theory of One rationale.
4. **Adjacent niche topics polluting the bank.** Hard rule: never extract topics from adjacent niches. Title structures, power words, thumbnail patterns, formats yes. Topics no.
5. **Em-dashes.** Brand-level no.
6. **Attribution leaks.** Productized files reference no source curriculum, no named third-party creators in bank entries (channel handles are fine, those are public, factual, and don't claim methodology). The methodology itself is presented as the system's own.

## Soft friction (surface and explain, creator decides)

1. **Thin-spread patterns.** Surface with the plain spread ("this showed up on only 2 of your channels"). Creator can choose to test a thin-spread pattern as a deliberate experiment.
2. **Pattern bank getting bloated.** If pattern_count exceeds 100 across all banks, suggest a curation pass to drop stale entries.
3. **Stale rebuild.** If `last_full_rebuild` is 180+ days old, suggest full rebuild instead of just refresh.
4. **Empty adjacent niches.** If creator can't or won't confirm any adjacent categories, run with niche-only. Pattern bank quality suffers but skill ships valid data.

## Reference index

`knowledge/` paths resolve to `${CLAUDE_PLUGIN_ROOT}/knowledge/` (installed) or repo-root `knowledge/` (dev), never the skill folder. `references/` and `scripts/` are skill-local.

| File | When to read it |
|---|---|
| `references/pattern-extraction-prompts.md` | Phase 1, 2, 3, the LLM prompts for extracting power words, title patterns, formats, fluke detection. Run-time decision logic. |
| `references/thumbnail-vision-classification.md` | Phase 1, 2, 3, vision prompt template for thumbnail analysis (6 strategies + composition extraction). |
| `knowledge/theory-of-one-curation.md` | Phase 5, examples of Keep/Drop/Modify decisions, drop rationale capture, bulk-keep heuristics. |
| `references/three-circle-research.md` | Phase 1, 2, 3, the methodology. Shared with future vid-channel-audit and vid-measurement. |
| `references/outlier-identification-rules.md` | Phase 1, 2, 3, the per-channel scaled floor plus fluke filter plus spread logic. Shared with future vid-measurement. |
| `assets/pattern-bank-template.md` | Phase 6, file structure for pattern-bank.md (outlier evidence + synthesis). |
| `assets/title-bank-template.md` | Phase 6, file structure for title-bank.md (fill-in-the-blank title shapes, research + creator-curated in one file). |
| `assets/power-words-bank-template.md` | Phase 6, file structure for power-words-bank.md (lean word list). |
| `assets/api-key-setup-guide.md` | Phase 1 setup if API key not configured. Walks creator through Google Cloud Console flow. |
| `scripts/youtube_fetch.py` | Phase 1, 2, 3, pulls channel videos with view counts, thumbnail URLs, median, and posting cadence via YouTube Data API. |
| `scripts/analyze.py` | Phase 1, 2, 3, consolidates fetch outputs into the outlier inventory using the per-channel floors. UTF-8 safe; use it instead of ad-hoc Python one-liners (titles with emoji crash a cp1252 console). |
| `scripts/thumbnail_download.py` | Phase 1, 2, 3, downloads thumbnail images for vision analysis. |

## Principles (the why)

- **Hypothesis, not guess.** Real audience data beats intuition. Every downstream framing decision stands or falls on it.
- **Three circles, not one.** Most creators only research their own niche and end up copying each other. The intersection of own + niche + adjacent is where differentiation lives. Adjacent niches are usually the breakthrough, same shape, different topic, applied to your audience.
- **Outliers, not averages.** A real outlier (one that cleared the channel's scaled floor) signals what viewers want more of. The channel's median tells you what's expected. Pattern bank captures outliers exclusively.
- **Expert-led, creator-decided.** The tool carries the YouTube expertise and does the data heavy lifting. The Theory of One filter, does this pattern fit MY audience?, only the creator can answer. The tool leads; the creator owns the calls.
- **Pattern bank grows over time.** Sticky-curated entries persist. Quarterly refreshes layer NEW signal on top of validated existing patterns. Don't rebuild from scratch when the existing bank works.
- **The whole packaging is the unit.** Outliers in `pattern-bank.md` per-channel sections show title + thumbnail text + thumbnail image + view count + outlier multiplier + hero element as one visual unit. Title patterns and power words extracted into focused banks (title-bank, power-words-bank) for vid-title's downstream use, but the outlier row stays coherent and visually browseable.

## Related skills

- `/foundation` produces the foundation files (iceberg.md for the statement and pillars, avatar.md for the audience), vid-research reads.
- `vid-voice-capture` (in development) will produce voice-profile.md; when it exists, vid-research reads it for mirroring style only.
- `vid-framing` reads pattern banks vid-research produces, picks angle for THIS video grounded in patterns.
- `vid-title` reads `power-words-bank.md` and `title-bank.md`, generates titles using patterns and words.
- `vid-thumbnail` reads `foundation/packaging-system.md` (current thumbnail strategy) plus `knowledge/thumbnail-text-patterns.md` for text candidates. Future `vid-thumbnail-gen` (Phase 5) queries `pattern-bank.md` outlier rows by thumbnail strategy for visual references.
- `vid-title`, `vid-thumbnail`, `vid-framing`, `vid-structure`, `vid-pressure-test` also read `foundation/packaging-system.md`, which vid-research authors in Phase 7 (replaces the deleted vid-packaging skill for the evidence fields).
- `vid-pipeline` (future) may invoke vid-research during onboarding before the first video is built.
- `vid-measurement` (future) writes confirmed winners back to relevant banks with the `own_channel_proven: true` flag, closing the feedback loop.
- `vid-channel-audit` (future) shares `references/three-circle-research.md` and `references/outlier-identification-rules.md`.
