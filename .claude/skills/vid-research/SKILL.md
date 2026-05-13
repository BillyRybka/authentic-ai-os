---
name: vid-research
description: Build or refresh the creator's pattern banks via Three-Circle Research (own channel + 5 niche competitors + 3-5 adjacent niches). Pulls outliers via the YouTube Data API, classifies thumbnails via vision analysis, extracts power words / title patterns / thumbnail patterns / format patterns / topic patterns / viewer-hate patterns, runs a Theory of One curation pass with the creator, saves to seven focused bank files. Three modes — first build (~1.5 hours), quarterly refresh (~30-45 minutes, sticky-curated entries persist), single outlier add (~5 minutes). Anti-fluke filter catches off-niche outliers (a sewing video on a YouTube-marketing channel doesn't pollute the pattern set). Anti-fabrication. Use this skill whenever a creator needs to build their pattern bank from scratch, refresh it on schedule (default every 90 days), or capture a single outlier they spotted in the wild. Phrases like "build my pattern bank", "refresh my research", "I just saw an outlier", "research my niche", "let's update the bank", "what's working in [niche] right now", "I want to research [channel]", or any first-run setup that needs banks before vid-framing should fire this skill.
---

# Video Research

Builds and refreshes the creator's seven pattern banks. Pattern banks are the raw research outputs that vid-framing, vid-title, vid-thumbnail, and downstream writing skills load at runtime to ground every decision in evidence rather than guesses. The skill handles the full Three-Circle Research workflow (own channel + 5 niche competitors + 3-5 adjacent niche channels), the YouTube data fetch, the thumbnail vision analysis, the cross-channel pattern synthesis, and the Theory of One curation pass with the creator.

This skill exists because the alternative — making videos based on what the creator THINKS will work — is the dominant failure mode for business channels. Pattern research turns guesses into hypotheses backed by the data of what audiences actually click, watch, and come back for. The pattern bank is the difference between shipping a video that aligns with proven outliers and shipping a video that feels right but flops.

**Scope boundary:** vid-research builds/refreshes pattern banks. It does NOT pick angles for a specific video (that's vid-framing). It does NOT lock titles or thumbnails (that's vid-title and vid-thumbnail). It does NOT track post-publish winners (that's vid-measurement, future). It produces the research substrate every other skill consumes.

## What this produces

Seven bank files in `banks/`:

- `pattern-bank.md` — synthesis index. Cross-channel insights, last-rebuild date, channels analyzed, pointers to the other banks. The creator's entry point for browsing research.
- `power-words-bank.md` — frequency-ranked words, split into Global (work everywhere) and Audience-Specific (work for THIS audience).
- `title-patterns-bank.md` — fill-in-the-blank title shapes with worked examples and near-miss anti-patterns.
- `thumbnail-patterns-bank.md` — the 6 thumbnail strategies populated with real outlier examples, embedded thumbnail images, vision-classified composition notes, and anti-patterns.
- `format-patterns-bank.md` — which of the 7 formats land for this audience, with example outliers per format.
- `topic-patterns-bank.md` — topic clusters that pulled views (own + niche only, NEVER adjacent topics).
- `viewer-hates-bank.md` — flop signals, what tanks for this audience, why each fails.

Plus per-channel raw research data sections inside `pattern-bank.md` showing the WHOLE PACKAGING for each studied outlier (title + thumbnail text + thumbnail image embed + view count + format + extracted patterns). Critical for visual coherence — the creator can see complete title-thumbnail combos in one view, not just decomposed patterns.

## When to run this

- **First build (Mode 1):** creator has just run vid-foundation and vid-voice-capture. No pattern banks exist yet. Run vid-research before vid-framing for the first time.
- **Quarterly refresh (Mode 2):** 90+ days since `last_full_rebuild` in `pattern-bank.md` frontmatter. Or when new outliers have stacked up the creator wants surfaced.
- **Single outlier add (Mode 3):** creator spotted an outlier between rebuilds and wants to capture it without a full session.

If the creator runs vid-framing without any pattern banks present, vid-framing should redirect them to vid-research first.

## Prerequisites

Hard requirements:

- `foundation/creator-foundation.md` exists. vid-research reads the iceberg statement, audience profile, and niche keywords to propose channel candidates.
- YouTube Data API key configured. If first run, walks the creator through `assets/api-key-setup-guide.md` (5-minute Google Cloud Console flow).

Soft requirements:

- `foundation/voice-profile.md` for mirroring style during the conversation. Skill works without it but feels less personal.
- Existing pattern banks (Mode 2 / Mode 3 only). Mode 1 starts from empty.

## Invocation modes

**Standalone:** creator invokes directly. Skill detects which mode based on existing bank state. Runs the matching flow.

**Sub-skill:** vid-pipeline (future) may invoke during onboarding. Returns a status packet ("banks built / refreshed / outlier captured + N entries").

## The 5 phases (Mode 1 — first build)

Mode 2 (refresh) runs the same phases but skips already-validated channels and surfaces only NEW outliers. Mode 3 (single add) runs Phase 4-6 directly with one channel and one outlier.

### Phase 1: Setup and own-channel research

**Setup checks (silent unless missing):**

1. `foundation/creator-foundation.md` exists → load iceberg, audience, niche keywords, top 12 outliers if existing channel.
2. YouTube Data API key configured. Path: `foundation/youtube-api-config.md` if creator has set this up before. If missing, walk through `assets/api-key-setup-guide.md` first.
3. Test API call against creator's own channel handle. If fails, walk creator through troubleshooting (key invalid, channel handle wrong, quota exhausted).

**Own channel pull:**

4. Creator confirms own channel handle (auto-loaded from creator-foundation if present).
5. Run `scripts/youtube_fetch.py --handle {creator-handle} --days 730`. Returns JSON: `{channel_id, channel_avg_views, videos: [{title, view_count, video_id, thumbnail_url, published_at, duration}]}`.
6. Compute outliers: 2x channel average AND raw view count meaningful for the niche (see `knowledge/outlier-identification-rules.md` for the threshold logic).
7. **Run the fluke filter on every outlier.** For each outlier, AI summarizes the channel's primary themes from the last 30 video titles, then checks "is this outlier on-niche for this channel?" Off-niche flukes get flagged: "This 700K-view video is about [topic], but the channel is about [primary themes]. Likely a fluke. Skip, or study?" Default skip. See `references/pattern-extraction-prompts.md` for the fluke detection prompt.
8. For each confirmed on-niche outlier (top 10 prioritized): pull thumbnail via `scripts/thumbnail_download.py`, run vision classification per `references/thumbnail-vision-classification.md` (which of 6 strategies, hero element, color palette, text content, expression).
9. Extract patterns per `references/pattern-extraction-prompts.md`: power words (global + audience-specific), title patterns, format identification, topic clusters, things-viewers-hate (from flops in same data set).
10. **Save partial state:** append draft entries to `pattern-bank.md` per-channel section + draft entries flagged `status: draft-pending-curation` to relevant banks (`power-words-bank.md`, `title-patterns-bank.md`, etc.). Frontmatter `last_phase_completed: 1` so resume works if session ends here.

### Phase 2: Niche channel research (5 channels)

**Niche candidate proposal (hybrid LLM + API):**

1. AI proposes 10-15 candidate niche channels based on creator-foundation niche keywords, audience description, and known channel patterns. LLM proposes handles, then a single batch API call (`channels.list` with comma-separated handles) validates each handle resolves and pulls real channel info (subscriber count, recent video themes, channel description).
2. Surface candidates with rich context (use Obsidian-friendly formatting — embedded thumbnails, callouts):

```
> [!note] Niche-similar candidates (same audience, same problem space)
> 
> ![channel-banner-url](banner) **@ChannelHandle** — 250k subs
> Recent themes: thumbnail strategy, retention, hook writing
> Top recent outlier: "Stop Making Boring Thumbnails" (1.2M views)
> Channel description: ...
```

3. Creator confirms 5 channels from the list. Override: creator can paste their own handles instead.

**Per-channel research (same as Phase 1 steps 5-10 for each of the 5):**

4. Pull videos via `scripts/youtube_fetch.py`.
5. Identify outliers (2x rule + raw count threshold).
6. Run fluke filter (this is where the underwater-basket-weaving-on-a-dog-training-channel problem gets caught).
7. For each confirmed on-niche outlier: top 5 per channel get thumbnail vision classification.
8. Extract patterns per category.
9. **Save partial state** after each channel finishes. Frontmatter `last_phase_completed: 2`, `niche_channels_done: [list]`.

### Phase 3: Adjacent niche research (3-5 channels via two-stage proposal)

**Stage A — propose adjacent niche CATEGORIES:**

1. AI proposes 5-7 adjacent niche categories based on the creator's niche. Examples: for fitness coaching → mobility, athletic performance, longevity, nutrition science, productivity-as-fitness, sports psychology. For YouTube growth coaching → copywriting, email marketing, personal branding, content strategy, course creation. For each category, surface a one-line rationale ("mobility shares the 'optimization for output' angle but pulls a different content style").
2. Creator confirms 3-5 categories. Override: creator can name their own.

**Stage B — for each confirmed category, propose channels:**

3. AI proposes 3-5 candidate channels per confirmed category, validated via batch API call (same pattern as Phase 2). Surface with same rich context.
4. Creator picks 1 channel per category (could pick more if they want).

**Per-channel research (adjacent extraction rule):**

5. Pull videos, identify outliers, run fluke filter.
6. Top 3 per channel get thumbnail vision classification.
7. **Adjacent extraction rule (critical):** capture title structures, power words, thumbnail patterns, formats. DO NOT capture topics from adjacent niches — adjacent gives you the SHAPE that translates, not the subject matter. Topics from adjacent niches pollute the bank.
8. **Save partial state.** Frontmatter `last_phase_completed: 3`, `adjacent_channels_done: [list]`.

### Phase 4: Cross-channel synthesis

**LLM synthesis pass:**

1. AI loads all draft entries from Phases 1-3.
2. Identifies CONVERGENT patterns: which power words appear across 5+ channels? Which title structures appear across the niche set? Which thumbnail strategies converge between niche and adjacent (strongest signal)?
3. Identifies UNIQUE patterns: what's distinctive to one channel that may or may not transfer?
4. Builds a confidence-ranked pattern brief: `pattern X — confidence HIGH (8 of 11 channels), pattern Y — confidence MEDIUM (4 of 11), pattern Z — confidence LOW (2 of 11, may be noise)`.
5. Appends synthesis to `pattern-bank.md` `## Synthesis` section as draft.
6. **Save partial state.** Frontmatter `last_phase_completed: 4`.

### Phase 5: Theory of One curation pass (the human filter)

This is the irreplaceable step. AI surfaces every draft pattern in confidence-ranked order. Creator hits Keep / Drop / Modify per pattern.

**Surface format per pattern:**

```
> Pattern: "STOP [common practice]" hook structure (Title Pattern T-7)
> 
> Confidence: HIGH — appears in 8 of 11 channels analyzed
> Worked examples (your data):
> 1. "STOP Using These 5 Outdated Hook Patterns" (@chan1, 1.4M views)
> 2. "STOP Recording Without This Setting" (@chan2, 800k views)
> 3. ...
> 
> Theory of One check: does this fit YOUR audience's expectations of you?
> Your iceberg: "I help [audience] [outcome] by [solving problem]"
> Your audience expects: [authority + clear strategic promises + evidence]
> 
> Keep / Drop / Modify?
```

Creator hits Keep, Drop (with optional one-line rationale), or Modify (rewrites the pattern in their own framing).

**Bulk-keep mode:** for high-confidence patterns the creator clearly wants, batch confirmation: "I'm bulk-keeping 8 high-confidence patterns. Want to skim them or trust the synthesis?"

**Sticky-curated growth (Mode 2 only):** patterns previously curated as Keep persist with `last_validated: {date}` updated. Patterns previously Dropped move to `## Considered + dropped` appendix with rationale, and don't get re-surfaced this session.

**Drop rationale capture:** when a pattern is dropped, ask "one line on why so future runs don't re-surface this?" Common reasons: "doesn't fit my audience's expected tone", "tested in past, flopped", "feels generic", "off-brand for me". Captured rationale prevents re-surfacing and trains the AI's proposal logic over time.

After curation, all `status: draft-pending-curation` entries either become `status: curated` (Keep), get rewritten (Modify), or move to dropped appendix (Drop).

### Phase 6: Save and confirm

1. Final write: `pattern-bank.md` with synthesis updated, all 7 banks with curated entries promoted, dropped patterns archived, frontmatter timestamps updated.
2. Confirm save with summary:

```
Pattern banks built. Saved across 7 bank files in banks/.
Channels analyzed: 1 own + 5 niche + 4 adjacent = 10 total
Outliers studied: 47
Patterns curated: 31 kept, 8 dropped, 4 modified
Next refresh recommended: 2026-08-08 (90 days)

Run vid-framing now to use these banks for your next video.
```

3. Frontmatter on `pattern-bank.md` updated: `last_full_rebuild: today`, `last_refresh: today`, `pattern_count: N`, `status: active`.

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

- **Visual presentation matters.** This skill outputs to Obsidian. Use Obsidian-native syntax everywhere — embedded thumbnails (`![alt](url)`), callouts (`> [!note]`), wikilinks for cross-bank references. The creator scrolls bank files in Obsidian, not raw text.
- **Listen during dump phases.** When creator drops 5 channel handles or 3 adjacent niche categories, listen to all of it before responding. Don't interrupt mid-list.
- **Specificity in proposals.** When AI proposes channels or categories, never just hand a list. Each candidate gets context — recent themes, top outlier, sub count, why it fits this circle. The creator confirms with information, not blind trust.
- **Power user mode for curation.** Theory of One pass can be slow. Offer bulk-keep for high-confidence patterns, fast-skip for low-confidence ones the creator obviously won't want. Don't drag a 30-pattern review through 30 questions.
- **Incremental save after every phase.** Never lose a session's work. If creator's session ends mid-way, resume protocol picks up at `last_phase_completed + 1`.

## Hard friction (auto-flag)

1. **Foundation missing.** Don't run without `creator-foundation.md`. Tell creator to run vid-foundation first.
2. **API key missing or invalid.** Walk through setup before proceeding. Don't skip with "we'll just use LLM knowledge of channels" — that's hallucination territory.
3. **Off-niche outliers (flukes).** Default skip. Creator can override only with explicit Theory of One rationale.
4. **Adjacent niche topics polluting the bank.** Hard rule: never extract topics from adjacent niches. Title structures, power words, thumbnail patterns, formats yes. Topics no.
5. **Em-dashes.** Brand-level no.
6. **Attribution leaks.** Productized files reference no source curriculum, no named third-party creators in bank entries (channel handles are fine — those are public, factual, and don't claim methodology). The methodology itself is presented as the system's own.

## Soft friction (surface and explain, creator decides)

1. **Low-confidence patterns.** Surface with explicit confidence ranking. Creator can choose to test a low-confidence pattern as a deliberate experiment.
2. **Pattern bank getting bloated.** If pattern_count exceeds 100 across all banks, suggest a curation pass to drop stale entries.
3. **Stale rebuild.** If `last_full_rebuild` is 180+ days old, suggest full rebuild instead of just refresh.
4. **Empty adjacent niches.** If creator can't or won't confirm any adjacent categories, run with niche-only. Pattern bank quality suffers but skill ships valid data.

## Reference index

| File | When to read it |
|---|---|
| `references/pattern-extraction-prompts.md` | Phase 1, 2, 3 — the LLM prompts for extracting power words, title patterns, formats, fluke detection. Run-time decision logic. |
| `references/thumbnail-vision-classification.md` | Phase 1, 2, 3 — vision prompt template for thumbnail analysis (6 strategies + composition extraction). |
| `references/theory-of-one-curation.md` | Phase 5 — examples of Keep/Drop/Modify decisions, drop rationale capture, bulk-keep heuristics. |
| `knowledge/three-circle-research.md` | Phase 1, 2, 3 — the methodology. Shared with future vid-channel-audit and vid-measurement. |
| `knowledge/outlier-identification-rules.md` | Phase 1, 2, 3 — the 2x rule plus raw-count threshold plus fluke filter logic. Shared with future vid-measurement. |
| `assets/pattern-bank-template.md` | Phase 6 — the file structure for pattern-bank.md if it doesn't exist yet. |
| `assets/{type}-bank-template.md` | Phase 6 — templates for each of the 6 sub-banks. |
| `assets/api-key-setup-guide.md` | Phase 1 setup if API key not configured. Walks creator through Google Cloud Console flow. |
| `scripts/youtube_fetch.py` | Phase 1, 2, 3 — pulls channel videos with view counts and thumbnail URLs via YouTube Data API. |
| `scripts/thumbnail_download.py` | Phase 1, 2, 3 — downloads thumbnail images for vision analysis. |

## Principles (the why)

- **Pattern research is the difference between hypothesis and guess.** Every framing decision downstream lands or fails based on whether the creator was working from real data or wishful thinking. vid-research generates the data.
- **Three circles, not one.** Most creators only research their own niche and end up copying each other. The intersection of own + niche + adjacent is where differentiation lives. Adjacent niches are usually the breakthrough — same shape, different topic, applied to your audience.
- **Outliers, not averages.** A 2x outlier signals what viewers want more of. The channel's average tells you what's expected. Pattern bank captures outliers exclusively.
- **The creator's judgment is irreplaceable.** AI does the data heavy lifting. The Theory of One filter — does this pattern fit MY audience? — only the creator can answer. The skill structures the conversation; the creator owns the decisions.
- **Pattern bank grows over time.** Sticky-curated entries persist. Quarterly refreshes layer NEW signal on top of validated existing patterns. Don't rebuild from scratch when the existing bank works.
- **The whole packaging is the unit.** Outliers in `pattern-bank.md` per-channel sections show title + thumbnail text + thumbnail image + format + view count as one visual unit. Patterns extracted into focused banks for downstream use, but the source view stays coherent.

## Related skills

- `vid-foundation` produces creator-foundation.md (iceberg, audience, niche keywords) — vid-research reads.
- `vid-voice-capture` produces voice-profile.md — vid-research reads for mirroring style only.
- `vid-framing` reads pattern banks vid-research produces — picks angle for THIS video grounded in patterns.
- `vid-title` reads `power-words-bank.md` and `title-patterns-bank.md` — generates titles using patterns.
- `vid-thumbnail` reads `thumbnail-patterns-bank.md` — generates thumbnail brief using strategies.
- `vid-pipeline` (future) may invoke vid-research during onboarding before the first video is built.
- `vid-measurement` (future) writes confirmed winners back to relevant banks with `confidence: proven` flag, closing the feedback loop.
- `vid-channel-audit` (future) shares `knowledge/three-circle-research.md` and `knowledge/outlier-identification-rules.md`.
