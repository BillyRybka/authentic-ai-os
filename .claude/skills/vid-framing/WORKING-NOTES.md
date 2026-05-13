---
name: vid-framing WORKING-NOTES
status: dev-only
audience: skill builder, not runtime
last_updated: 2026-05-11
---

# vid-framing: Source Citations (dev-only)

Not loaded at runtime. Exists so the skill builder (or a future audit) can verify every rule traces to source material. No productized file (SKILL.md, references/, assets/, knowledge/) names the source, the creator, or the course.

Source root: `C:/Users/billr/projects/business-os/Resources/references/ed-lawrence-ygs/`

## Source citations by decision

### Person → Problem → Positioning (Theory of One filter)
`frameworks.md:25`, "Identify the perfect buyer, identify the biggest problem they know they have, then write one short statement, 'We solve this problem for this person.' Position every video, email, and offer as the solution to that one problem for that one person, consistently."

Used by: Phase 3 Theory of One filter. The three-step test IS the filter.

### One-in-Four Problem (why angle must land on Top 3)
`frameworks.md:43`, "If only one in four videos appeals to a viewer's reason for subscribing: (1) they watch 25% of content in the key 30-day warming window... (2) YouTube stops testing videos with that viewer bucket... (3) an email list of 3,000 is functionally a list of 750."

Used by: justifies hard-gate that angles must land on Top 3 or be flagged outlier-within-iceberg. Drift kills compounding.

### Three-Circle Research Model (anchor source)
`frameworks.md:108` / `video-pipeline-map.md:128`, "Three-Circle Research Model (your channel ∩ niche ∩ adjacent)... The intersection is where differentiation lives."

Used by: anchor candidates draw from pattern bank (the materialized output of three-circle research). Don't re-explain the model in vid-framing, knowledge/three-circle-research.md owns it.

### Adjacent Niche transfer (yoga case)
`frameworks.md:117-121`, "Livin Leggings full story: stuck at 25,000 subscribers in the yoga niche. Ed looked at mobility and weightlifting niches and found short bingeable tip videos with simple thumbnails. Applied the 'before/after' comparison format and scientific dot overlay (from Jeff Nippard's weightlifting thumbnails) to yoga content. First video in the new format: 2.4M views."

Used by: justifies adjacent-niche structural transfer. Soft signal for "experimental" angle slot, adjacent structural pattern + own topic = breakthrough configuration.

### Rule of 3 + 1 (EXTENDED to angles)
`frameworks.md:125-126`, "Maintain 3 proven video format templates rotating consistently. Every 4th video is an experimental test. If the test wins, promote it into the core 3 and retire the weakest format."

Used by: the principle behind "3 anchored + 1 experimental angle." Source applies this to FORMAT rotation across a quarter, NOT to per-video angle generation.

**Extension caveat:** the productized skill extends the *principle* (proven + 1 experimental per cycle) from format-rotation-across-quarter to angle-generation-per-session. This is inspired-by, not direct application. Honest extension. If a future audit questions this, the answer is: same principle, smaller cycle.

### Repeat What Works (no freshness test)
`frameworks.md:134-135`, "Once a video format proves itself, clone the packaging: same thumbnail structure, same intro template, same script format."

Used by: vid-framing doesn't enforce a "freshness" filter. Repeating a proven angle is GOOD if anchor confidence is HIGH. Surface this affirmatively when an angle matches a proven winner from the creator's own channel.

### Audience Temperature Model (viewer_stage definition)
`frameworks.md:540-541`, "Cold = discovering you for the first time. Warm = seen a few videos, curious but not ready. Hot = feels you're speaking directly to them, ready to buy. What determines temperature: topics chosen, problems addressed, stories told, frameworks shared. A hot audience on low views will out-convert a cold audience on high views."

`frameworks.md:543`, "Broad video: 250k cold viewers → 5,000 sales page visits → 10 sales. Specific video: 50k hot viewers → 1,000 sales page visits → 40 sales."

Used by: `viewer_stage` field. ENTIRE basis for `references/audience-temperature-fit.md` and `knowledge/audience-temperature-model.md`.

### Dollar Per View (temperature signal)
`frameworks.md:549-552`, "Revenue generated divided by total views. A low-view video with high DPV signals extremely hot audience temperature. The lesson is to repeat the topic, problem framing, story, or framework that drove it."

Used by: knowledge/audience-temperature-model.md as supporting framework. Not load-bearing in vid-framing itself but explains why temperature matters for goal-fit decisions.

### Conversion Optimization System (Goal selection)
`frameworks.md:659-660`, "Pick a goal (Sales, Email, or Views) → plan content around that goal → measure performance with RevTrack → point new videos back to the ones that hit the goal."

`frameworks.md:662`, "Ed wasted over 30 million views with no business goal. One video got barely any views but became his number-one email-collector. Another made ~$250,000 and thousands of emails."

Used by: `goal` field. Phase 4 lock step requires creator to pick one.

### Stage D: 3-4 concepts per batch
`video-pipeline-map.md:116, 121`, "Output 3-4 validated concepts per batch." "Ideate 3-4 concepts, each with 1 title + 3 thumbnail doodles (3 different strategies from Stage C) + vision board of outlier inspiration."

Used by: magic number is 3-4 angles. NOT 5. Adjusted from earlier 3-5 draft.

### Stage C: Format locked at packaging
`video-pipeline-map.md:102`, "Format pick, primary format from the 7-format system... plus 1-2 to test., set-once"

`video-pipeline-map.md:130`. Stage D hands off "format pick for this video (from Stage C options)."

`video-pipeline-map.md:138`, "Pick the format planner from Stage C's locked format."

Used by: vid-framing surfaces ONLY the formats locked in packaging-system (3 core + 1-2 test). Does NOT show all 7.

### Stage A handoff (already upstream)
`video-pipeline-map.md:128`. Stage D requires "avatar profile and top 3 problems · positioning statement" pre-locked.

Used by: vid-framing reads these from creator-foundation.md (already produced by vid-foundation). No re-derivation.

### Don't try to save flops
`video-pipeline-map.md:182, 186`, "Do not try to save flops." "24-hour check, full market test done. Default: if ranking 7-10, write it off and extract the lesson."

Used by: POST-publish guidance only. vid-framing has NO hard kill criteria pre-production. Soft friction only. Kill happens at measurement, not framing.

## Deliberate exclusions

- No Eugene-Schwartz-style "stage of awareness." Source teaches relationship temperature (cold/warm/hot). NOT problem-awareness levels.
- No freshness filter. Source teaches Repeat What Works.
- No pre-production hard kill criteria. Source kills at measurement only.
- No new format planners. `knowledge/format-planners/{format}.md` already exists.
- No iceberg or Top 3 re-derivation. vid-intake locks these upstream.

## File-by-file source mapping

| Productized file | Source decisions it implements |
|---|---|
| `SKILL.md` | Stage D structure (`video-pipeline-map.md:114-131`), Person → Problem → Positioning (`frameworks.md:25`), 3-4 concepts (`video-pipeline-map.md:116`), goal selection (`frameworks.md:659`), no pre-prod kill (`video-pipeline-map.md:182`) |
| `references/angle-anchor-rules.md` | Three-Circle anchor (`frameworks.md:108`), Adjacent Niche transfer (`frameworks.md:117-121`), Repeat What Works (`frameworks.md:134-135`), Rule of 3+1 EXTENDED (`frameworks.md:125-126`) |
| `references/audience-temperature-fit.md` | Audience Temperature Model (`frameworks.md:540-543`), Conversion math (`frameworks.md:543`), Goal (`frameworks.md:659-662`), DPV (`frameworks.md:549-552`) |
| `references/framing-conversation-examples.md` | Theory of One (`frameworks.md:25`), 3-anchored + 1-experimental (Rule of 3+1 extension), bulk-keep power-user mode |
| `assets/piece-framing-additions.md` | All field types map back to specific decisions above |
| `knowledge/audience-temperature-model.md` (shared) | Audience Temperature Model (`frameworks.md:540-543`), DPV (`frameworks.md:549-552`) |

## Schema choices

- `outlier_anchor` allows null for experimental angles. Downstream vid-title needs a fallback for null anchor, uses power-words-bank instead of anchor's title pattern. Note in SKILL.md, confirm during eventual vid-title update.
- `anchor_confidence: experimental` is the explicit flag for the no-anchor slot. Future audit can ask "is the experimental slot creating value?" If creators never pick it, revisit.
- `viewer_stage` is used predictively (what temperature WILL this angle attract). Source describes it primarily in measurement context but says explicitly "What determines temperature: topics chosen, problems addressed, stories told, frameworks shared", which justifies predictive use.

## Maintenance triggers

- Pattern bank schema changes (vid-research updates) → revisit angle-anchor-rules.md citation format.
- New format added to 7-format system → update SKILL.md format enum.
- If `knowledge/audience-temperature-model.md` gets loaded by 3+ skills, confirms multi-skill placement was right.
