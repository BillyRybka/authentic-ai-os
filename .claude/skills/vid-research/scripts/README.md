# vid-research scripts

Two scripts that vid-research invokes via Bash during data collection.

## youtube_fetch.py

Pulls a channel's videos (last N days, excluding shorts and live streams) via the YouTube Data API v3. Returns JSON with channel metadata, computed median view count, posting cadence (videos per month), a 2x reference floor, and per-video data (title, view count, thumbnail URL, duration, published date). The 2x value is a reference floor, not the outlier bar; the skill scales the real per-channel floor from the median plus cadence (see `knowledge/outlier-identification-rules.md`).

**Dependencies:** Python 3.7+. Standard library only (no pip installs needed). Uses `urllib`, `json`, `argparse`, `statistics`, `datetime`.

**Usage:**
```bash
python youtube_fetch.py --handle "@coachx" --days 365 --api-key "$YT_API_KEY"
python youtube_fetch.py --channel-id "UCxxx" --days 365 --api-key "$YT_API_KEY"
python youtube_fetch.py --url "https://youtube.com/@coachx" --days 365 --api-key "$YT_API_KEY"
```

API key: pass via `--api-key` flag or set `YT_API_KEY` env var.

**Quota:** ~5-15 units per channel. Free tier daily quota is 10,000 units. Researching 11 channels (1 own + 5 niche + 5 adjacent) costs ~50-150 units. Plenty of headroom.

## analyze.py

Consolidates the per-channel `youtube_fetch.py` outputs into one outlier inventory, applying the per-channel floors the skill set with the creator. Use this instead of ad-hoc `python -c` one-liners: it is UTF-8 hardened end to end, so emoji or smart quotes in channel and video titles never crash the run on Windows.

**Dependencies:** Python 3.7+. Standard library only.

**Usage:**
```bash
python analyze.py --fetch-dir /path/to/fetches --floors /path/to/floors.json --out /path/to/consolidated.json
```

`floors.json` maps each fetch file's slug to the floor (a raw view count, scaled to the channel) and an optional bucket:
```json
{
  "coachx":   {"floor": 60000,   "bucket": "direct"},
  "dailyfit": {"floor": 48000,   "bucket": "adjacent"},
  "mega":     {"floor": 1000000, "bucket": "style-only"}
}
```

Output: writes `consolidated.json` (per channel: median, cadence, floor, sorted outliers with multipliers) and prints a summary table.

## thumbnail_download.py

Downloads thumbnail images from URLs to a local cache directory for vision analysis. Idempotent, re-running skips already-downloaded files. Outputs JSON status per attempt.

**Dependencies:** Python 3.7+. Standard library only.

**Usage:**
```bash
# From file
python thumbnail_download.py --input thumbs.json --output-dir banks/proof-bank/assets/thumbnails

# From stdin
echo '[{"video_id":"abc","thumbnail_url":"https://..."}]' | python thumbnail_download.py --output-dir /tmp/thumbs
```

Input shape:
```json
[
  {"video_id": "abc123", "thumbnail_url": "https://i.ytimg.com/..."},
  {"video_id": "def456", "thumbnail_url": "https://i.ytimg.com/..."}
]
```

Output (per entry):
```json
{
  "video_id": "abc123",
  "local_path": "/abs/path/to/abc123.jpg",
  "status": "ok" | "cached" | "failed",
  "error": "..." (only when failed)
}
```

## How the skill calls these

vid-research SKILL.md Phase 1, 2, 3:

1. Skill builds a list of channel handles to research.
2. For each handle, skill runs `youtube_fetch.py` via Bash, parses JSON.
3. Skill identifies confirmed outliers (after the per-channel scaled floor + fluke filter).
4. Skill builds a list of `[{video_id, thumbnail_url}, ...]` for outliers needing vision analysis.
5. Skill runs `thumbnail_download.py` via Bash with that list.
6. Skill uses Read tool on returned `local_path` values to invoke Claude vision per `references/thumbnail-vision-classification.md`.
7. Vision results get appended to per-channel sections in `pattern-bank.md`.

## Setup gotchas

**API key region restrictions.** When generating the API key in Google Cloud Console, leave application restrictions OFF (or restrict to YouTube Data API v3 only via API restrictions). HTTP referrer restrictions will fail because the script calls from the user's machine.

**Quota errors mid-session.** If you hit 10,000 units on a single API key, you're done for the day. The skill should bail gracefully and resume tomorrow. Quota resets at midnight Pacific Time per Google.

**Rate limits.** YouTube Data API doesn't have a strict rate limit beyond the daily quota, but be polite, don't hammer it with parallel calls. The scripts run sequentially by design.

**Thumbnail download failures.** If a thumbnail URL returns 404, the video may have been deleted or unlisted. Skill should mark the outlier with `vision: unavailable` and skip thumbnail-based pattern extraction for that entry.
