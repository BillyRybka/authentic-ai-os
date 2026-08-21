#!/usr/bin/env python3
"""
youtube_fetch.py: Pull a YouTube channel's videos via the YouTube Data API v3.

Used by vid-research to fetch outlier candidate data per channel. Outputs JSON
to stdout with channel metadata + video list (filtered to last N days, excluding
shorts and live streams).

Usage:
    python youtube_fetch.py --handle "@coachx" --days 365 --api-key "$YT_API_KEY"
    python youtube_fetch.py --channel-id "UCxxx" --days 365 --api-key "$YT_API_KEY"
    python youtube_fetch.py --url "https://youtube.com/@coachx" --days 365 --api-key "$YT_API_KEY"

Environment:
    YT_API_KEY can be set as env var instead of --api-key flag.

Output (JSON to stdout):
    {
      "channel_id": "UCxxx",
      "channel_handle": "@coachx",
      "channel_title": "Coach X",
      "subscriber_count": 50000,
      "channel_avg_views_median": 18000,
      "median_2x_reference": 36000,
      "window_days": 365,
      "video_count": 47,
      "videos_per_month": 3.9,
      "videos": [
        {
          "video_id": "abc123",
          "title": "Some Title",
          "view_count": 145000,
          "thumbnail_url": "https://...",
          "published_at": "2025-08-12T...",
          "duration_seconds": 660,
          "is_short_suspect": false,
          "clears_2x_floor": true
        },
        ...
      ],
      "fetched_at": "2026-05-10T..."
    }

Note: 2x median is the FLOOR, not the bar. `median_2x_reference` and
`clears_2x_floor` are coarse hints. The skill scales the real per-channel
outlier floor from the median plus `videos_per_month` (see
outlier-identification-rules.md).

Note: videos at or under 60 seconds are hard-excluded as Shorts. Longer
short-form now exists, so `is_short_suspect` is true for any returned video at
or under 120 seconds. The skill surfaces these for review rather than silently
counting them in the outlier set.

Quota usage (per call):
    channels.list (resolve handle):           1 unit
    channels.list (get uploads playlist):     1 unit (combined with above)
    playlistItems.list (per page of 50):      1 unit
    videos.list (per batch of 50 video IDs):  1 unit

Total per session per channel: ~5-15 units depending on channel size.
"""

import argparse
import json
import os
import re
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

YT_API_BASE = "https://www.googleapis.com/youtube/v3"

# Videos at or under this duration are hard-excluded as Shorts.
SHORTS_HARD_MAX_SECONDS = 60
# Videos above the hard cut but at or under this duration are still returned,
# flagged is_short_suspect=true. Longer short-form now exists, so very short
# videos can slip past a 60s cut and pollute the outlier set. The skill surfaces
# these rather than silently counting them.
SHORT_SUSPECT_MAX_SECONDS = 120


def load_env_file(path: str = ".env") -> None:
    """Load KEY=VALUE pairs from a .env file in the current directory into the
    environment. Does not override variables already set. No third-party
    dependency. Silent if the file is absent. The API key is read from here so
    it never has to live in a skill file or be committed (.env is gitignored).
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
    except FileNotFoundError:
        pass


def fetch_json(path: str, params: dict, api_key: str) -> dict:
    """GET a YouTube Data API endpoint, return parsed JSON."""
    params["key"] = api_key
    url = f"{YT_API_BASE}/{path}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"YouTube API HTTP {e.code} on /{path}: {body[:500]}"
        ) from e


def resolve_channel(identifier: str, api_key: str) -> dict:
    """
    Given a handle (@x), URL, or channel ID, return channel metadata + uploads playlist ID.
    """
    handle = None
    channel_id = None

    if identifier.startswith("UC") and len(identifier) >= 20:
        channel_id = identifier
    elif identifier.startswith("@"):
        handle = identifier
    elif "youtube.com" in identifier:
        # Parse URL forms: youtube.com/@handle, youtube.com/channel/UCxxx, youtube.com/c/customname
        url_path = urllib.parse.urlparse(identifier).path.strip("/")
        parts = url_path.split("/")
        if parts[0].startswith("@"):
            handle = parts[0]
        elif parts[0] == "channel" and len(parts) > 1:
            channel_id = parts[1]
        elif parts[0] in ("c", "user") and len(parts) > 1:
            handle = "@" + parts[1]
        else:
            handle = "@" + parts[0] if parts[0] else None
    else:
        # bare string treated as handle
        handle = "@" + identifier.lstrip("@")

    params = {"part": "id,snippet,contentDetails,statistics"}
    if channel_id:
        params["id"] = channel_id
    elif handle:
        params["forHandle"] = handle
    else:
        raise ValueError(f"Could not parse channel identifier: {identifier}")

    data = fetch_json("channels", params, api_key)
    items = data.get("items", [])
    if not items:
        raise RuntimeError(
            f"Channel not found: {identifier}. Verify handle/ID is correct."
        )

    ch = items[0]
    return {
        "channel_id": ch["id"],
        "channel_handle": ch["snippet"].get("customUrl", handle or ""),
        "channel_title": ch["snippet"]["title"],
        "subscriber_count": int(ch["statistics"].get("subscriberCount", 0)),
        "uploads_playlist_id": ch["contentDetails"]["relatedPlaylists"]["uploads"],
    }


def fetch_uploads(uploads_playlist_id: str, since_date: datetime, api_key: str) -> list:
    """Pull all video IDs from the uploads playlist published since since_date."""
    video_ids = []
    page_token = None
    keep_going = True
    while keep_going:
        params = {
            "part": "snippet,contentDetails",
            "playlistId": uploads_playlist_id,
            "maxResults": 50,
        }
        if page_token:
            params["pageToken"] = page_token
        data = fetch_json("playlistItems", params, api_key)
        items = data.get("items", [])
        for item in items:
            published_at_str = item["contentDetails"].get("videoPublishedAt")
            if not published_at_str:
                continue
            published_at = datetime.fromisoformat(
                published_at_str.replace("Z", "+00:00")
            )
            if published_at < since_date:
                # Once we cross the date threshold, stop paginating
                keep_going = False
                break
            video_ids.append(item["contentDetails"]["videoId"])
        page_token = data.get("nextPageToken")
        if not page_token:
            keep_going = False
    return video_ids


def parse_iso_duration(duration: str) -> int:
    """ISO 8601 duration (e.g. PT4M13S) to seconds."""
    pattern = r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?"
    m = re.match(pattern, duration or "")
    if not m:
        return 0
    days, hours, minutes, seconds = (int(x) if x else 0 for x in m.groups())
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def fetch_video_details(video_ids: list, api_key: str) -> list:
    """Pull view counts, thumbnails, durations for a list of video IDs (batched in 50s)."""
    videos = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        params = {
            "part": "snippet,contentDetails,statistics,liveStreamingDetails",
            "id": ",".join(batch),
        }
        data = fetch_json("videos", params, api_key)
        for item in data.get("items", []):
            duration_seconds = parse_iso_duration(
                item.get("contentDetails", {}).get("duration", "")
            )
            # Skip live streams (live, scheduled, or completed-but-flagged)
            if item.get("liveStreamingDetails"):
                continue
            # Hard-exclude Shorts (at or under SHORTS_HARD_MAX_SECONDS).
            if duration_seconds <= SHORTS_HARD_MAX_SECONDS:
                continue
            # Flag borderline short-form (at or under SHORT_SUSPECT_MAX_SECONDS)
            # so the skill can surface it instead of silently counting it.
            is_short_suspect = duration_seconds <= SHORT_SUSPECT_MAX_SECONDS
            # Skip videos without view counts (private, deleted, processing)
            view_count = item.get("statistics", {}).get("viewCount")
            if view_count is None:
                continue
            thumbs = item.get("snippet", {}).get("thumbnails", {})
            # Prefer maxres, then high, then default
            thumb_url = (
                thumbs.get("maxres", {}).get("url")
                or thumbs.get("high", {}).get("url")
                or thumbs.get("medium", {}).get("url")
                or thumbs.get("default", {}).get("url")
            )
            videos.append(
                {
                    "video_id": item["id"],
                    "title": item["snippet"]["title"],
                    "view_count": int(view_count),
                    "thumbnail_url": thumb_url,
                    "published_at": item["snippet"]["publishedAt"],
                    "duration_seconds": duration_seconds,
                    "is_short_suspect": is_short_suspect,
                }
            )
    return videos


def compute_outlier_threshold(view_counts: list) -> tuple:
    """
    Returns (median, median*2). The 2x value is a reference floor, not the outlier
    bar; the skill scales the real per-channel floor from median + cadence. Median
    is robust against the outliers themselves.
    """
    if not view_counts:
        return (0, 0)
    median = statistics.median(view_counts)
    return (int(median), int(median * 2))


def main():
    # Force UTF-8 on stdout/stderr so emoji and smart-quotes in video titles
    # don't crash the run on Windows (default console is cp1252). Guarded for
    # interpreters older than 3.7 that lack reconfigure().
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8")
    load_env_file()
    parser = argparse.ArgumentParser(description=__doc__)
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--handle", help="Channel handle, e.g. @coachx")
    src.add_argument("--channel-id", help="Channel ID, e.g. UCxxx")
    src.add_argument("--url", help="Channel URL")
    parser.add_argument(
        "--days",
        type=int,
        default=365,
        help="Pull videos published within last N days (default 365 = 12 months; expand to 730 for 24 months)",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("YT_API_KEY"),
        help="YouTube Data API key. Defaults to YT_API_KEY env var.",
    )
    args = parser.parse_args()

    if not args.api_key:
        print(
            "ERROR: API key required. Pass --api-key or set YT_API_KEY env var.",
            file=sys.stderr,
        )
        sys.exit(2)

    identifier = args.handle or args.channel_id or args.url

    try:
        channel = resolve_channel(identifier, args.api_key)
        since_date = datetime.now(timezone.utc) - timedelta(days=args.days)
        video_ids = fetch_uploads(channel["uploads_playlist_id"], since_date, args.api_key)
        videos = fetch_video_details(video_ids, args.api_key)
        view_counts = [v["view_count"] for v in videos]
        median, median_2x = compute_outlier_threshold(view_counts)

        # Posting cadence. A high cadence deflates the median (a pile of low-view
        # uploads), which is why a flat 2x is too loose for prolific channels. The
        # skill reads this to scale the per-channel floor; the script does not set
        # the bar.
        videos_per_month = round(len(videos) / (args.days / 30.0), 1) if args.days else 0

        for v in videos:
            # 2x median is the FLOOR, not the bar. The skill/analyze sets the real
            # per-channel floor from median + cadence. This flag is a coarse hint only.
            v["clears_2x_floor"] = v["view_count"] >= median_2x

        result = {
            "channel_id": channel["channel_id"],
            "channel_handle": channel["channel_handle"],
            "channel_title": channel["channel_title"],
            "subscriber_count": channel["subscriber_count"],
            "channel_avg_views_median": median,
            "median_2x_reference": median_2x,
            "window_days": args.days,
            "video_count": len(videos),
            "videos_per_month": videos_per_month,
            "videos": videos,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }

        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
