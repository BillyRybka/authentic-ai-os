#!/usr/bin/env python3
"""
youtube_fetch.py: Pull a YouTube channel's videos straight off the channel's
public Videos tab.

Used by vid-research to fetch outlier candidate data per channel. Outputs JSON
to stdout with channel metadata + video list (filtered to last N days, excluding
shorts and live streams). Reads the same ytInitialData JSON any browser renders,
and pages older videos through YouTube's own browse endpoint using the public
client config embedded in the page. Stdlib only.

Usage:
    python youtube_fetch.py --handle "@coachx" --days 365
    python youtube_fetch.py --channel-id "UCxxx" --days 365
    python youtube_fetch.py --url "https://youtube.com/@coachx" --days 365

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
      "date_precision": "approximate",
      "videos": [
        {
          "video_id": "abc123",
          "title": "Some Title",
          "view_count": 145000,
          "thumbnail_url": "https://...",
          "published_at": "2025-08-12T00:00:00+00:00",
          "duration_seconds": 660,
          "is_short_suspect": false,
          "clears_2x_floor": true
        },
        ...
      ],
      "fetched_at": "2026-05-10T..."
    }

Precision notes:
    - published_at is derived from the public "8 months ago" labels, so it is
      approximate (day-level for recent videos, month-level past a few weeks).
      Plenty for outlier math; do not present it as an exact date.
    - subscriber_count is parsed from the public "50K subscribers" label, so it
      is a rounded figure.
    - view_count is exact where YouTube serves the exact figure and the public
      rounded label ("82M views") where it does not. Rounded is plenty for
      outlier floors and multipliers; do not present these as exact counts.

Note: 2x median is the FLOOR, not the bar. `median_2x_reference` and
`clears_2x_floor` are coarse hints. The skill scales the real per-channel
outlier floor from the median plus `videos_per_month` (see
outlier-identification-rules.md).

Note: the Videos tab already excludes Shorts and live streams, and this script
hard-excludes anything at or under 60 seconds as a second guard. Longer
short-form now exists, so `is_short_suspect` is true for any returned video at
or under 120 seconds. The skill surfaces these for review rather than silently
counting them in the outlier set.

If YouTube throttles or consent-walls the fetch, the script retries with
backoff and then fails LOUDLY instead of returning a thin page as if it were
the whole channel. Wait a few minutes and rerun, or pull the channel page
through the browser and collect the same fields there.
"""

import argparse
import json
import random
import re
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

# Videos at or under this duration are hard-excluded as Shorts.
SHORTS_HARD_MAX_SECONDS = 60
# Videos above the hard cut but at or under this duration are still returned,
# flagged is_short_suspect=true, so the skill surfaces them instead of silently
# counting them.
SHORT_SUSPECT_MAX_SECONDS = 120

# Safety cap on continuation pages (~30 videos per page).
MAX_PAGES = 40

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    # Consent + language cookies so the page serves data (not a consent wall)
    # and English relative-date labels the parser understands.
    "Cookie": "CONSENT=YES+cb; SOCS=CAI; PREF=hl=en&gl=US",
}


class BlockedError(RuntimeError):
    """YouTube appears to be throttling or walling us. Fail loudly rather than
    return partial data as if it were the whole channel."""


def http_request(url: str, payload: dict = None, timeout: int = 20, retries: int = 3) -> str:
    """GET (or POST json if payload given) with retry + backoff on throttle
    codes. Returns response text. Raises BlockedError after repeated blocks."""
    last_err = None
    for attempt in range(retries):
        data = None
        headers = dict(HEADERS)
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 403, 503):
                last_err = f"HTTP {e.code}"
                time.sleep(min(30.0, 2.0 ** attempt) + random.uniform(0, 1.0))
                continue
            if e.code == 404:
                raise RuntimeError(
                    "Channel page not found (HTTP 404). Verify the handle/URL is correct."
                ) from e
            raise RuntimeError(f"HTTP {e.code} fetching {url}") from e
        except urllib.error.URLError as e:
            last_err = f"network error: {e.reason}"
            time.sleep(min(30.0, 2.0 ** attempt) + random.uniform(0, 1.0))
            continue
    raise BlockedError(
        f"YouTube kept refusing the request ({last_err}). Wait a few minutes and "
        "rerun, or pull the channel page through the browser instead."
    )


def channel_videos_url(identifier: str) -> str:
    """Handle (@x), channel ID (UCxxx), bare name, or URL -> Videos tab URL."""
    identifier = identifier.strip()
    if identifier.startswith("UC") and len(identifier) >= 20 and "/" not in identifier:
        return f"https://www.youtube.com/channel/{identifier}/videos"
    if "youtube.com" in identifier:
        path = urllib.parse.urlparse(
            identifier if "://" in identifier else "https://" + identifier
        ).path.strip("/")
        parts = path.split("/")
        if parts and parts[0].startswith("@"):
            return f"https://www.youtube.com/{parts[0]}/videos"
        if parts and parts[0] == "channel" and len(parts) > 1:
            return f"https://www.youtube.com/channel/{parts[1]}/videos"
        if parts and parts[0] in ("c", "user") and len(parts) > 1:
            return f"https://www.youtube.com/{parts[0]}/{parts[1]}/videos"
        if parts and parts[0]:
            return f"https://www.youtube.com/@{parts[0]}/videos"
        raise ValueError(f"Could not parse channel URL: {identifier}")
    handle = identifier if identifier.startswith("@") else "@" + identifier
    return f"https://www.youtube.com/{handle}/videos"


def extract_yt_initial_data(html: str) -> dict:
    """Pull the ytInitialData JSON blob via brace-matched raw_decode. Handles
    `var ytInitialData =` and `window["ytInitialData"] =`; skips decoy mentions."""
    decoder = json.JSONDecoder()
    for m in re.finditer(r'ytInitialData"?\]?\s*=\s*', html):
        start = html.find("{", m.end())
        if start == -1 or start - m.end() > 5:
            continue
        try:
            obj, _ = decoder.raw_decode(html, start)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and ("contents" in obj or "metadata" in obj):
            return obj
    raise BlockedError(
        "Page loaded but carried no channel data (likely a consent or bot wall). "
        "Wait a few minutes and rerun, or pull the channel page through the browser."
    )


def extract_innertube_cfg(html: str) -> tuple:
    """(innertube_key, client_version) from the page's embedded public client config.
    This is YouTube's own web-client config present on every page for every
    visitor; it is not a user credential."""
    key_m = re.search(r'"INNERTUBE_API_KEY"\s*:\s*"([^"]+)"', html)
    ver_m = re.search(r'"INNERTUBE_CONTEXT_CLIENT_VERSION"\s*:\s*"([^"]+)"', html)
    return (
        key_m.group(1) if key_m else None,
        ver_m.group(1) if ver_m else "2.20240101.00.00",
    )


def walk(node, key):
    """Yield every dict value found under `key` anywhere in a nested structure."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == key:
                yield v
            else:
                yield from walk(v, key)
    elif isinstance(node, list):
        for item in node:
            yield from walk(item, key)


def text_of(obj) -> str:
    """Flatten YouTube's text objects ({simpleText} or {runs:[...]}) to a string."""
    if not isinstance(obj, dict):
        return ""
    if "simpleText" in obj:
        return obj["simpleText"]
    return "".join(r.get("text", "") for r in obj.get("runs", []))


def parse_view_count(video_renderer: dict):
    """Exact count from viewCountText ('123,456 views'); falls back to the
    rounded shortViewCountText ('12K views'). None if neither parses."""
    exact = text_of(video_renderer.get("viewCountText", {}))
    m = re.search(r"([\d,]+)\s+view", exact)
    if m:
        return int(m.group(1).replace(",", ""))
    if re.search(r"^no\s+views", exact.strip(), re.IGNORECASE):
        return 0
    approx = text_of(video_renderer.get("shortViewCountText", {}))
    m = re.search(r"([\d.]+)\s*([KMB]?)\s+view", approx, re.IGNORECASE)
    if m:
        mult = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
        return int(float(m.group(1)) * mult[m.group(2).upper()])
    return None


# Deliberately generous granularity: YouTube rounds labels down ("13 months
# ago" shows as "1 year ago"), so month=30/year=365 keeps boundary videos
# inside a 365-day window instead of dropping them.
RELATIVE_UNITS = {
    "second": 1 / 86400.0,
    "minute": 1 / 1440.0,
    "hour": 1 / 24.0,
    "day": 1.0,
    "week": 7.0,
    "month": 30.0,
    "year": 365.0,
}


def parse_published_age_days(label: str):
    """'8 months ago' -> approximate age in days. None if unparseable."""
    m = re.search(r"(\d+)\s+(second|minute|hour|day|week|month|year)s?\s+ago", label)
    if not m:
        return None
    return int(m.group(1)) * RELATIVE_UNITS[m.group(2)]


def parse_duration_seconds(label: str) -> int:
    """'12:34' or '1:02:33' -> seconds. 0 if unparseable."""
    parts = label.strip().split(":")
    if not all(p.strip().isdigit() for p in parts):
        return 0
    total = 0
    for p in parts:
        total = total * 60 + int(p)
    return total


def parse_approx_number(label: str):
    """'1.23M' / '50K' / '987' -> int. None if unparseable."""
    m = re.match(r"([\d.,]+)\s*([KMB]?)", label.strip(), re.IGNORECASE)
    if not m or not m.group(1):
        return None
    try:
        base = float(m.group(1).replace(",", ""))
    except ValueError:
        return None
    mult = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
    return int(base * mult[m.group(2).upper()])


def extract_from_lockups(node, now: datetime) -> list:
    """Pull videos from the newer lockupViewModel grid layout. View counts here
    are the public rounded labels ('82M views'), which is the precision the
    outlier math needs anyway."""
    videos = []
    for lv in walk(node, "lockupViewModel"):
        if lv.get("contentType") != "LOCKUP_CONTENT_TYPE_VIDEO":
            continue
        video_id = lv.get("contentId")
        md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
        if not video_id or not md:
            continue
        parts = []
        for row in walk(md.get("metadata", {}), "metadataParts"):
            for part in row:
                content = part.get("text", {}).get("content", "")
                if content:
                    parts.append(content)
        view_count = None
        age_days = None
        streamed = False
        for p in parts:
            if p.startswith("Streamed"):
                streamed = True
            m = re.match(r"^([\d.,]+[KMB]?)\s+views?$", p, re.IGNORECASE)
            if m and view_count is None:
                view_count = parse_approx_number(m.group(1))
            if re.match(r"^no\s+views$", p.strip(), re.IGNORECASE) and view_count is None:
                view_count = 0
            if age_days is None:
                age_days = parse_published_age_days(p)
        if streamed or view_count is None or age_days is None:
            continue
        duration_seconds = 0
        for badge in walk(lv.get("contentImage", {}), "thumbnailBadgeViewModel"):
            label = badge.get("text", "")
            if re.match(r"^\d+(:\d+)+$", label):
                duration_seconds = parse_duration_seconds(label)
                break
        if duration_seconds == 0:
            continue  # live/premiere placeholders
        sources = (
            lv.get("contentImage", {})
            .get("thumbnailViewModel", {})
            .get("image", {})
            .get("sources", [])
        )
        thumb_url = (
            sources[-1].get("url")
            if sources
            else f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        )
        published_at = (now - timedelta(days=age_days)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        videos.append(
            {
                "video_id": video_id,
                "title": md.get("title", {}).get("content", ""),
                "view_count": view_count,
                "thumbnail_url": thumb_url,
                "published_at": published_at.isoformat(),
                "duration_seconds": duration_seconds,
                "is_short_suspect": duration_seconds <= SHORT_SUSPECT_MAX_SECONDS,
                "_age_days": age_days,
            }
        )
    return videos


def extract_videos(node, now: datetime) -> list:
    """Pull every video under `node`, handling both the classic videoRenderer
    layout and the newer lockupViewModel layout (dedupe happens downstream)."""
    videos = extract_from_lockups(node, now)
    for vr in walk(node, "videoRenderer"):
        video_id = vr.get("videoId")
        if not video_id:
            continue
        published_label = text_of(vr.get("publishedTimeText", {}))
        # Past live streams carry a 'Streamed ...' label; upcoming/live carry
        # none. Neither belongs in the outlier set.
        if not published_label or published_label.startswith("Streamed"):
            continue
        age_days = parse_published_age_days(published_label)
        if age_days is None:
            continue
        duration_seconds = parse_duration_seconds(text_of(vr.get("lengthText", {})))
        if duration_seconds == 0:
            continue  # live/premiere placeholders
        view_count = parse_view_count(vr)
        if view_count is None:
            continue  # private/processing
        # The grid's largest thumb (typically 720p) always exists; the
        # constructed hqdefault path is the fallback when the grid has none.
        thumbs = vr.get("thumbnail", {}).get("thumbnails", [])
        thumb_url = (
            thumbs[-1].get("url")
            if thumbs
            else f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        )
        published_at = (now - timedelta(days=age_days)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        videos.append(
            {
                "video_id": video_id,
                "title": text_of(vr.get("title", {})),
                "view_count": view_count,
                "thumbnail_url": thumb_url,
                "published_at": published_at.isoformat(),
                "duration_seconds": duration_seconds,
                "is_short_suspect": duration_seconds <= SHORT_SUSPECT_MAX_SECONDS,
                "_age_days": age_days,
            }
        )
    return videos


def find_continuation_token(node):
    for cir in walk(node, "continuationItemRenderer"):
        token = (
            cir.get("continuationEndpoint", {})
            .get("continuationCommand", {})
            .get("token")
        )
        if token:
            return token
    return None


def extract_channel_meta(data: dict, html: str, fallback_handle: str) -> dict:
    meta = data.get("metadata", {}).get("channelMetadataRenderer", {})
    if not meta:
        raise RuntimeError(
            "No channel metadata on the page. Verify the handle/URL is correct."
        )
    handle = fallback_handle
    vanity = meta.get("vanityChannelUrl", "")
    m = re.search(r"(@[^/]+)$", vanity)
    if m:
        handle = m.group(1)
    sub_m = re.search(r'"([\d.,]+[KMB]?)\s+subscribers?"', html)
    subscriber_count = parse_approx_number(sub_m.group(1)) if sub_m else 0
    return {
        "channel_id": meta.get("externalId", ""),
        "channel_handle": handle,
        "channel_title": meta.get("title", ""),
        "subscriber_count": subscriber_count or 0,
    }


def fetch_channel(identifier: str, days: int) -> dict:
    now = datetime.now(timezone.utc)
    url = channel_videos_url(identifier)
    html = http_request(url)
    data = extract_yt_initial_data(html)
    innertube_key, client_version = extract_innertube_cfg(html)

    fallback_handle = ""
    hm = re.search(r"(@[^/]+)", url)
    if hm:
        fallback_handle = hm.group(1)
    channel = extract_channel_meta(data, html, fallback_handle)

    videos = extract_videos(data.get("contents", {}), now)
    token = find_continuation_token(data.get("contents", {}))

    # Page older videos until we're past the window (with a buffer, because the
    # labels are coarse) or the channel runs out.
    pages = 0
    while token and innertube_key and pages < MAX_PAGES:
        oldest = max((v["_age_days"] for v in videos), default=0)
        if oldest > days + 60:
            break
        browse_url = (
            "https://www.youtube.com/youtubei/v1/browse?"
            + urllib.parse.urlencode({"key": innertube_key, "prettyPrint": "false"})
        )
        payload = {
            "context": {
                "client": {
                    "clientName": "WEB",
                    "clientVersion": client_version,
                    "hl": "en",
                    "gl": "US",
                }
            },
            "continuation": token,
        }
        resp = json.loads(http_request(browse_url, payload=payload))
        actions = resp.get("onResponseReceivedActions", [])
        new_videos = extract_videos(actions, now)
        token = find_continuation_token(actions)
        if not new_videos:
            break
        videos.extend(new_videos)
        pages += 1
        time.sleep(random.uniform(0.4, 1.0))  # be a polite visitor

    # Dedupe, window, exclude Shorts.
    seen = set()
    kept = []
    for v in videos:
        if v["video_id"] in seen:
            continue
        seen.add(v["video_id"])
        if v["_age_days"] > days:
            continue
        if v["duration_seconds"] <= SHORTS_HARD_MAX_SECONDS:
            continue
        del v["_age_days"]
        kept.append(v)
    kept.sort(key=lambda v: v["published_at"], reverse=True)
    return {"channel": channel, "videos": kept}


def compute_outlier_threshold(view_counts: list) -> tuple:
    """Returns (median, median*2). The 2x value is a reference floor, not the
    outlier bar; the skill scales the real per-channel floor from median +
    cadence. Median is robust against the outliers themselves."""
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
    args = parser.parse_args()

    identifier = args.handle or args.channel_id or args.url

    try:
        result_raw = fetch_channel(identifier, args.days)
        channel = result_raw["channel"]
        videos = result_raw["videos"]
        view_counts = [v["view_count"] for v in videos]
        median, median_2x = compute_outlier_threshold(view_counts)

        # Posting cadence. A high cadence deflates the median (a pile of
        # low-view uploads), which is why a flat 2x is too loose for prolific
        # channels. The skill reads this to scale the per-channel floor; the
        # script does not set the bar.
        videos_per_month = round(len(videos) / (args.days / 30.0), 1) if args.days else 0

        for v in videos:
            # 2x median is the FLOOR, not the bar. The skill/analyze sets the
            # real per-channel floor from median + cadence. Coarse hint only.
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
            "date_precision": "approximate",
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
