---
name: vid-research
description: Build or refresh the creator's pattern banks via Three-Circle Research (own channel + 5 niche competitors + 3-5 adjacent niches). Pulls outliers via the YouTube Data API, classifies thumbnails via vision analysis, extracts power words / title patterns / thumbnail patterns, runs a Theory of One curation pass with the creator, saves to four focused bank files (pattern-bank synthesis plus power-words, title-patterns, thumbnail-patterns), then authors the creator's starting `packaging-system.md` (format rotation, thumbnail strategy, title-bank seed) from that evidence. Three modes: first build (~1.5 hours), quarterly refresh (~30-45 minutes, sticky-curated entries persist), single outlier add (~5 minutes). Anti-fluke filter catches off-niche outliers (a sewing video on a YouTube-marketing channel doesn't pollute the pattern set). Anti-fabrication. Use this skill whenever a creator needs to build their pattern bank from scratch, refresh it on schedule (default every 90 days), or capture a single outlier they spotted in the wild. Phrases like "build my pattern bank", "refresh my research", "I just saw an outlier", "research my niche", "let's update the bank", "what's working in [niche] right now", "I want to research [channel]", or any first-run setup that needs banks before vid-framing should fire this skill.
---

# Video Research

Builds and refreshes the creator's seven pattern banks. Pattern banks are the raw research outputs that vid-framing, vid-title, vid-thumbnail, and downstream writing skills load at runtime to ground every decision in evidence rather than guesses. The skill handles the full Three-Circle Research workflow (own channel + 5 niche competitors + 3-5 adjacent niche channels), the YouTube data fetch, the thumbnail vision analysis, the cross-channel pattern synthesis, and the Theory of One curation pass with the creator.

This skill exists because the alternative, making videos based on what the creator THINKS will work, is the dominant failure mode for business channels. Pattern research turns guesses into hypotheses backed by the data of what audiences actually click, watch, and come back for. The pattern bank is the difference between shipping a video that aligns with proven outliers and shipping a video that feels right but flops.

**Scope boundary:** vid-research builds/refreshes pattern banks. It does NOT pick angles for a specific video (that's vid-framing). It does NOT lock titles or thumbnails (that's vid-title and vid-thumbnail). It does NOT track post-publish winners (that's vid-measurement, future). It produces the research substrate every other skill consumes.

## What this produces

Four bank files in `banks/`:

- `pattern-bank.md`: the holistic bank. Cross-channel synthesis, last-rebuild date, channels analyzed, per-outlier full-package sections (see below), AND the topic-cluster section (topics that pulled views, own + niche only, NEVER adjacent). The creator's entry point and the source's actual unit of research: the whole outlier, not decomposed silos.
- `power-words-bank.md`: frequency-ranked words, split into Global (work everywhere) and Audience-Specific (work for THIS audience).
- `title-patterns-bank.md`: fill-in-the-blank title shapes with worked examples and near-miss anti-patterns.
- `thumbnail-patterns-bank.md`: the 6 thumbnail strategies populated with real outlier examples, embedded thumbnail images, vision-classified composition notes, and anti-patterns.

These three sub-banks are decomposed only because downstream skills consume specific slices (vid-title reads power-words + title-patterns, vid-thumbnail reads thumbnail-patterns). Everything else stays holistic in pattern-bank.

**Not banks (by 2026-05-19 decision):** format is a menu pick, not a mined pattern (a competitor's format can't be classified from title + thumbnail + metadata without transcripts; see Phase 7, it comes from `knowledge/format-rotation-guide.md`). Topic clusters fold into the pattern-bank synthesis, not a standalone file. "What the audience hates" is post-publish flop diagnosis (future vid-measurement), not pre-research collection.

Plus per-channel raw research data sections inside `pattern-bank.md` showing the WHOLE PACKAGING for each studied outlier (title + thumbnail text + thumbnail image embed + view count + format + extracted patterns). Critical for visual coherence: the creator sees complete title-thumbnail combos in one view, not just decomposed patterns.

Plus one synthesis artifact: `foundation/packaging-system.md`. vid-research authors the creator's starting packaging defaults FROM the evidence it just gathered (format rotation picked from the `knowledge/format-rotation-guide.md` menu, thumbnail strategy from `thumbnail-patterns-bank`, title-bank seed from `title-patterns-bank` + `power-words-bank`). This file is read by vid-framing, vid-title, vid-thumbnail, vid-structure, and vid-pressure-test. Packaging defaults are a research output, never a pre-research guess. (vid-packaging skill was collapsed 2026-05-19; this is its replacement home for the evidence fields. The identity residue, design guardrails and creation path, is parked and not yet homed; leave its section in the template as an explicit unfilled stub, do not fabricate values.)

## When to run this

- **First build (Mode 1):** creator has just run vid-foundation and vid-voice-capture. No pattern banks exist yet. Run vid-research before vid-framing for the first time.
- **Quarterly refresh (Mode 2):** 90+ days since `last_full_rebuild` in `pattern-bank.md` frontmatter. Or when new outliers have stacked up the creator wants surfaced.
- **Single outlier add (Mode 3):** creator spotted an outlier between rebuilds and wants to capture it without a full session.

If the creator runs vid-framing without any pattern banks present, vid-framing should redirect them to vid-research first.

## Prerequisites

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` in this skill is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load `knowledge/X.md` relative to the repo root instead.

Hard requirements:

- `foundation/creator-foundation.md` exists. vid-research reads the iceberg statement, audience profile, and niche keywords to help the creator name their competitors and to suggest a few only if they're stuck.
- YouTube Data API key configured. The key lives in a `.env` file at the vault root as `YT_API_KEY=...`. `.env` is gitignored and the key is NEVER written into any skill file, committed, or saved to the foundation docs. `creator-setup` scaffolds a `.env.example` with the `YT_API_KEY=` line; the creator copies it to `.env` and pastes their key. The `youtube_fetch.py` script reads `YT_API_KEY` from the environment. If first run and no key is set, walk the creator through `assets/api-key-setup-guide.md` (5-minute Google Cloud Console flow), then have them put the key in `.env`.

Soft requirements:

- `foundation/voice-profile.md` for mirroring style during the conversation. Skill works without it but feels less personal.
- Existing pattern banks (Mode 2 / Mode 3 only). Mode 1 starts from empty.

## Invocation modes

**Standalone:** creator invokes directly. Skill detects which mode based on existing bank state. Runs the matching flow.

**Sub-skill:** vid-pipeline (future) may invoke during onboarding. Returns a status packet ("banks built / refreshed / outlier captured + N entries").

## The 5 phases (Mode 1, first build)

Mode 2 (refresh) runs the same phases but skips already-validated channels and surfaces only NEW outliers. Mode 3 (single add) runs Phase 4-6 directly with one channel and one outlier.

### Phase 1: Setup and own-channel research

**Setup checks (silent unless missing):**

1. `foundation/creator-foundation.md` exists → load iceberg, audience, niche keywords, top 12 outliers if existing channel.
2. YouTube Data API key configured. Path: `foundation/youtube-api-config.md` if creator has set this up before. If missing, walk through `assets/api-key-setup-guide.md` first.
3. Test API call against creator's own channel handle. If fails, walk creator through troubleshooting (key invalid, channel handle wrong, quota exhausted).

**Own channel pull:**

4. Confirm the creator's own channel handle. If it's saved in their foundation, reflect it back ("Your channel is @handle, right?"). If it isn't saved, just ask for it in one plain line. Asking is normal here, not an error.
5. Run `scripts/youtube_fetch.py --handle {creator-handle} --days 730`. Returns JSON: `{channel_id, channel_avg_views, videos: [{title, view_count, video_id, thumbnail_url, published_at, duration}]}`.
6. Compute outliers: 2x channel average AND raw view count meaningful for the niche (see `knowledge/outlier-identification-rules.md` for the threshold logic).
7. **Run the fluke filter on every outlier.** For each outlier, AI summarizes the channel's primary themes from the last 30 video titles, then checks "is this outlier on-niche for this channel?" Off-niche flukes get flagged: "This 700K-view video is about [topic], but the channel is about [primary themes]. Likely a fluke. Skip, or study?" Default skip. See `references/pattern-extraction-prompts.md` for the fluke detection prompt.
8. For each confirmed on-niche outlier (top 10 prioritized): pull thumbnail via `scripts/thumbnail_download.py`, run vision classification per `references/thumbnail-vision-classification.md` (which of 6 strategies, hero element, color palette, text content, expression).
9. Extract patterns per `references/pattern-extraction-prompts.md`: power words (global + audience-specific), title patterns, thumbnail patterns. Capture topic clusters into the pattern-bank synthesis section (not a standalone bank). Do NOT attempt format classification (can't be done from title + thumbnail + metadata without transcripts; format is a menu pick handled in Phase 7). Do NOT build a viewer-hates set (flop diagnosis is post-publish, future vid-measurement).
10. **Save partial state:** append draft entries to `pattern-bank.md` per-channel section + draft entries flagged `status: draft-pending-curation` to relevant banks (`power-words-bank.md`, `title-patterns-bank.md`, etc.). Frontmatter `last_phase_completed: 1` so resume works if session ends here.

### Phase 2: Niche research (the creator's direct competitors)

The creator knows their competitors better than the skill does. Ask them first. Only suggest channels yourself if they run dry.

**Ask the creator for their competitors:**

1. Ask one plain question: who are the channels they'd call their direct competitors? Give them the simple test for what counts so they can answer well, in plain words, no jargon:
   - It makes the kind of content the creator wants to be known for.
   - It serves the same kind of viewer.
   - It has at least a few videos that clearly beat that channel's own normal by a wide margin, within roughly the last two years.

   Keep it conversational. Something like: "Who are your top competitors? The channels making the kind of content you want to be known for, for the same kind of viewer, the ones with videos that clearly took off." Then listen.

2. Take their whole list without interrupting. If they name fewer than five, ask once if there are more: "You've named three. Anyone else you watch or measure yourself against?" One nudge, then move on. Don't grind.

3. **Only if they're genuinely stuck** (they can't get to five, or can't name any): suggest a couple of channels you believe are real fits. Build them from the competitors the creator already named plus the known players in that space. Never dump a long list, a couple at a time. Validate each suggestion against the API first (confirm the handle resolves, pull real subscriber count and recent video themes) so you are offering real channels, not guesses. Surface plainly: "A couple you might also count: @handleA (lately: X, Y) and @handleB (lately: X, Y). Either of these fit, or not really?"

4. Confirm the set. Aim for about five, but follow the creator. Resolve every confirmed handle through the API and quietly capture the real channel data.

**Per-channel research (runs silently for each confirmed channel, same engine as Phase 1):**

5. Pull videos via `scripts/youtube_fetch.py`.
6. Identify outliers (2x rule + raw-count threshold, see `knowledge/outlier-identification-rules.md`). Internal math, not narrated.
7. Run the fluke filter. Only bring a fluke to the creator if it genuinely needs their call, and say it plainly: "This big one is about [topic], which is off from what that channel usually does. Worth studying, or skip?"
8. For each confirmed on-niche outlier: top 5 per channel get thumbnail vision analysis.
9. Extract patterns per category.
10. **Save partial state** after each channel finishes. Frontmatter `last_phase_completed: 2`, `niche_channels_done: [list]`.

### Phase 3: Adjacent research (the creator's adjacent channels)

Same order: ask first, suggest only to fill gaps. Adjacent is a fuzzier idea for a creator, so explain it in one plain line and offer examples drawn from their own niche to spark it.

**Ask the creator for adjacent channels:**

1. Explain adjacent in one plain sentence: creators who make a similar type of content, but on a different topic or in a different industry. The kind of channel your viewer might also watch. Then ask if a few come to mind. To help them think, offer two or three adjacent areas drawn from the creator's own niche (generate these at runtime from their foundation, never hardcode them) and let the creator react: "A few next-door areas could be [area 1], [area 2], [area 3]. Any channels you already follow in spaces like that?"

2. Take what they give. If they're stuck, suggest a couple of adjacent channels yourself, one per area, built from their niche and validated against the API first (handle resolves, real subs and recent themes). Offer plainly for a yes or no.

3. Confirm three to five. If the creator can't or won't name any, that is fine, the research still ships valid data with niche-only (the bank is a little thinner, say so once and move on).

**Per-channel research (adjacent extraction rule):**

4. Pull videos, identify outliers, run the fluke filter (all internal).
5. Top 3 per channel get thumbnail vision analysis.
6. **Adjacent extraction rule (critical):** capture title structures, power words, thumbnail patterns, formats. DO NOT capture topics from adjacent niches. Adjacent gives you the structure that transfers, not the subject matter. Topics from adjacent niches pollute the bank.
7. **Save partial state.** Frontmatter `last_phase_completed: 3`, `adjacent_channels_done: [list]`.

### Phase 4: Cross-channel synthesis

**LLM synthesis pass:**

1. AI loads all draft entries from Phases 1-3.
2. Identifies CONVERGENT patterns: which power words appear across 5+ channels? Which title structures appear across the niche set? Which thumbnail strategies converge between niche and adjacent (strongest signal)?
3. Identifies UNIQUE patterns: what's distinctive to one channel that may or may not transfer?
4. Builds a confidence-ranked pattern brief: `pattern X, confidence HIGH (8 of 11 channels), pattern Y, confidence MEDIUM (4 of 11), pattern Z, confidence LOW (2 of 11, may be noise)`.
5. Appends synthesis to `pattern-bank.md` `## Synthesis` section as draft.
6. **Save partial state.** Frontmatter `last_phase_completed: 4`.

### Phase 5: Theory of One curation pass (the human filter)

This is the irreplaceable step. AI surfaces every draft pattern in confidence-ranked order. Creator hits Keep / Drop / Modify per pattern.

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

Show the signal in plain language (how many of their channels it showed up on), not "confidence HIGH, 8 of 11." Keep the internal ranking to yourself; the creator just needs to know it's strong, medium, or a long shot, and whether it fits them.

Creator hits Keep, Drop (with optional one-line rationale), or Modify (rewrites the pattern in their own framing).

**Bulk-keep mode:** for high-confidence patterns the creator clearly wants, batch confirmation: "I'm bulk-keeping 8 high-confidence patterns. Want to skim them or trust the synthesis?"

**Sticky-curated growth (Mode 2 only):** patterns previously curated as Keep persist with `last_validated: {date}` updated. Patterns previously Dropped move to `## Considered + dropped` appendix with rationale, and don't get re-surfaced this session.

**Drop rationale capture:** when a pattern is dropped, ask "one line on why so future runs don't re-surface this?" Common reasons: "doesn't fit my audience's expected tone", "tested in past, flopped", "feels generic", "off-brand for me". Captured rationale prevents re-surfacing and trains the AI's proposal logic over time.

After curation, all `status: draft-pending-curation` entries either become `status: curated` (Keep), get rewritten (Modify), or move to dropped appendix (Drop).

### Phase 6: Save and confirm

1. Final write: `pattern-bank.md` with synthesis + topic clusters + per-outlier packages updated, all 4 banks with curated entries promoted, dropped patterns archived, frontmatter timestamps updated.
2. Confirm with a short, plain message. Not a stats table read aloud. Something like:

```
Done. I went through the channels you picked and pulled out the titles, thumbnails, and hooks that are actually working in your space. The ones that fit you are saved and ready to use.

When you want to plan your next video, run vid-framing. It pulls straight from this.
```

If the creator wants the numbers (how many channels, how many kept), give them, but don't lead with them. The counts and the suggested next-refresh date live in the file's frontmatter either way.

3. Frontmatter on `pattern-bank.md` updated: `last_full_rebuild: today`, `last_refresh: today`, `pattern_count: N`, `status: active`. Suggested next refresh is about 90 days out, stored here, not announced as a deadline.

### Phase 7: Author packaging-system.md from the evidence

The 4 banks are saved. Now synthesize the creator's starting packaging defaults. Load `knowledge/packaging-system-template.md` for the output shape and `knowledge/format-rotation-guide.md` for the format menu. Fill ONLY the evidence-driven fields, each tagged with its evidence basis and a confidence level:

1. **Starting format rotation (3 core + 1 experimental).** Format is a menu pick, NOT a mined pattern. Load `knowledge/format-rotation-guide.md`: it holds the fixed 7-format menu (with Views/Sales/Trust scores), the Rule of 3+1, and the 4-check filter. Propose 3 core + 1 experiment from the menu based on the creator's avatar, strengths, and own-channel data if any, run the 4-check filter, creator confirms. Confidence is generally low at first build (no published data on the new positioning yet); that is expected and honest. The experiment-promote/retire loop is post-publish, deferred to future vid-measurement.
2. **Thumbnail strategy (1-2 to test).** Pull from `thumbnail-patterns-bank.md` outliers. Name the strategy, cite the example outliers it came from, mark confidence.
3. **Title-bank seed.** Seed `banks/title-bank.md` from `title-patterns-bank.md` shapes + `power-words-bank.md`. Real outlier-validated patterns, not generic templates.
4. **Identity residue (design guardrails, creation path).** Leave these sections in the template as explicit unfilled stubs marked `# TBD, not yet homed (see build-plan 2026-05-19)`. Do NOT interview for them here and do NOT fabricate values. This is a parked open question by decision.

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

Talk to the creator the way the foundation skills do. Load `knowledge/interview-posture.md` and follow it: one question at a time, plain words, absorb what they said before asking the next thing. This skill has a lot of machinery under the hood. The creator should never feel it.

- **Ask, don't guess.** The creator names their competitors and adjacent channels. You only suggest channels when they're genuinely stuck, and then just a couple, built from what they already named. Never open with a list you generated.
- **Keep the machinery silent.** Medians, the 2x rule, raw-count thresholds, the fluke filter, vision analysis, quota, draft states. These are how you think, not how you talk. Do the math quietly. Only surface a number or a judgment call when the creator actually needs to decide something, and say it in plain English.
- **One thing at a time.** Short messages. Ask one question, wait, react to the answer, then move. No long preambles, no walls of explanation, no narrating your steps.
- **Listen during dumps.** When the creator rattles off several channels or areas at once, take all of it before responding. Don't interrupt mid-list.
- **Confirm their picks with real info, not blind trust.** Once they name channels, quietly pull the real data and reflect back what you found in a line or two, so they're confirming on facts. Same for any channel you suggest when they're stuck.
- **Make curation fast.** The Keep/Drop/Modify pass can drag. Offer to bulk-keep the obvious winners and skip the obvious no's. Don't march them through thirty questions.
- **Visual presentation matters.** This skill outputs to Obsidian. Use Obsidian-native syntax in the bank files: embedded thumbnails, callouts (`> [!note]`), wikilinks. The creator scrolls those files in Obsidian, not raw text.
- **Save after every phase.** Never lose a session's work. If the session ends mid-way, resume picks up at `last_phase_completed + 1`.

## Hard friction (auto-flag)

1. **Foundation missing.** Don't run without `creator-foundation.md`. Tell creator to run vid-foundation first.
2. **API key missing or invalid.** Walk through setup before proceeding. Don't skip with "we'll just use LLM knowledge of channels", that's hallucination territory.
3. **Off-niche outliers (flukes).** Default skip. Creator can override only with explicit Theory of One rationale.
4. **Adjacent niche topics polluting the bank.** Hard rule: never extract topics from adjacent niches. Title structures, power words, thumbnail patterns, formats yes. Topics no.
5. **Em-dashes.** Brand-level no.
6. **Attribution leaks.** Productized files reference no source curriculum, no named third-party creators in bank entries (channel handles are fine, those are public, factual, and don't claim methodology). The methodology itself is presented as the system's own.

## Soft friction (surface and explain, creator decides)

1. **Low-confidence patterns.** Surface with explicit confidence ranking. Creator can choose to test a low-confidence pattern as a deliberate experiment.
2. **Pattern bank getting bloated.** If pattern_count exceeds 100 across all banks, suggest a curation pass to drop stale entries.
3. **Stale rebuild.** If `last_full_rebuild` is 180+ days old, suggest full rebuild instead of just refresh.
4. **Empty adjacent niches.** If creator can't or won't confirm any adjacent categories, run with niche-only. Pattern bank quality suffers but skill ships valid data.

## Reference index

| File | When to read it |
|---|---|
| `references/pattern-extraction-prompts.md` | Phase 1, 2, 3, the LLM prompts for extracting power words, title patterns, formats, fluke detection. Run-time decision logic. |
| `references/thumbnail-vision-classification.md` | Phase 1, 2, 3, vision prompt template for thumbnail analysis (6 strategies + composition extraction). |
| `references/theory-of-one-curation.md` | Phase 5, examples of Keep/Drop/Modify decisions, drop rationale capture, bulk-keep heuristics. |
| `knowledge/three-circle-research.md` | Phase 1, 2, 3, the methodology. Shared with future vid-channel-audit and vid-measurement. |
| `knowledge/outlier-identification-rules.md` | Phase 1, 2, 3, the 2x rule plus raw-count threshold plus fluke filter logic. Shared with future vid-measurement. |
| `assets/pattern-bank-template.md` | Phase 6, the file structure for pattern-bank.md if it doesn't exist yet. |
| `assets/{type}-bank-template.md` | Phase 6, templates for pattern-bank + the 3 sub-banks (power-words, title-patterns, thumbnail-patterns). |
| `assets/api-key-setup-guide.md` | Phase 1 setup if API key not configured. Walks creator through Google Cloud Console flow. |
| `scripts/youtube_fetch.py` | Phase 1, 2, 3, pulls channel videos with view counts and thumbnail URLs via YouTube Data API. |
| `scripts/thumbnail_download.py` | Phase 1, 2, 3, downloads thumbnail images for vision analysis. |

## Principles (the why)

- **Pattern research is the difference between hypothesis and guess.** Every framing decision downstream lands or fails based on whether the creator was working from real data or wishful thinking. vid-research generates the data.
- **Three circles, not one.** Most creators only research their own niche and end up copying each other. The intersection of own + niche + adjacent is where differentiation lives. Adjacent niches are usually the breakthrough, same shape, different topic, applied to your audience.
- **Outliers, not averages.** A 2x outlier signals what viewers want more of. The channel's average tells you what's expected. Pattern bank captures outliers exclusively.
- **The creator's judgment is irreplaceable.** AI does the data heavy lifting. The Theory of One filter, does this pattern fit MY audience?, only the creator can answer. The skill structures the conversation; the creator owns the decisions.
- **Pattern bank grows over time.** Sticky-curated entries persist. Quarterly refreshes layer NEW signal on top of validated existing patterns. Don't rebuild from scratch when the existing bank works.
- **The whole packaging is the unit.** Outliers in `pattern-bank.md` per-channel sections show title + thumbnail text + thumbnail image + format + view count as one visual unit. Patterns extracted into focused banks for downstream use, but the source view stays coherent.

## Related skills

- `vid-foundation` produces creator-foundation.md (iceberg, audience, niche keywords), vid-research reads.
- `vid-voice-capture` produces voice-profile.md, vid-research reads for mirroring style only.
- `vid-framing` reads pattern banks vid-research produces, picks angle for THIS video grounded in patterns.
- `vid-title` reads `power-words-bank.md` and `title-patterns-bank.md`, generates titles using patterns.
- `vid-thumbnail` reads `thumbnail-patterns-bank.md`, generates thumbnail brief using strategies.
- `vid-title`, `vid-thumbnail`, `vid-framing`, `vid-structure`, `vid-pressure-test` also read `foundation/packaging-system.md`, which vid-research authors in Phase 7 (replaces the deleted vid-packaging skill for the evidence fields).
- `vid-pipeline` (future) may invoke vid-research during onboarding before the first video is built.
- `vid-measurement` (future) writes confirmed winners back to relevant banks with `confidence: proven` flag, closing the feedback loop.
- `vid-channel-audit` (future) shares `knowledge/three-circle-research.md` and `knowledge/outlier-identification-rules.md`.
