#!/usr/bin/env python3
"""
video_details.py: Pull exact publish dates and exact view counts for specific
videos off their public watch pages.

Used by vid-research AFTER the outlier floor is set: youtube_fetch.py windows a
whole channel using the grid's rounded labels ("1 year ago"), which can be off
by months at the window boundary. Run this on the outlier subset only (the
videos that clear the floor, typically 10-20 per channel, about a second each)
to replace their approximate dates and rounded view counts with exact figures.
Never run it on the full inventory; the rounded data is fine there.

Usage:
    python video_details.py --ids abc123,def456
    python video_details.py --from-fetch coachx.json --min-views 60000

    --from-fetch takes a youtube_fetch.py output file and enriches the videos
    at or above --min-views (the floor the skill set with the creator),
    printing the full fetch JSON back out with those rows updated in place.

Output (--ids mode, JSON to stdout):
    [
      {"video_id": "abc123", "published_at": "2025-08-12T09:00:00-08:00",
       "view_count": 2016906, "status": "ok"},
      {"video_id": "def456", "published_at": null, "view_count": null,
       "status": "failed", "error": "..."},
      ...
    ]

A video that fails keeps its approximate data; the run never dies on one bad
page. Videos whose exact date falls outside the fetch window are NOT dropped
here; the skill decides (in --from-fetch mode they are flagged
"outside_window": true so the decision is visible).
"""

import argparse
import json
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone

from youtube_fetch import http_request


def fetch_details(video_id: str) -> dict:
    """Exact publish timestamp + exact view count from the public watch page."""
    try:
        html = http_request(f"https://www.youtube.com/watch?v={video_id}")
    except Exception as e:
        return {"video_id": video_id, "published_at": None, "view_count": None,
                "status": "failed", "error": str(e)}
    m_date = re.search(r'"publishDate":"([^"]+)"', html)
    m_views = re.search(r'"viewCount":"(\d+)"', html)
    if not m_date or not m_views:
        return {"video_id": video_id, "published_at": None, "view_count": None,
                "status": "failed", "error": "watch page carried no video data"}
    return {
        "video_id": video_id,
        "published_at": m_date.group(1),
        "view_count": int(m_views.group(1)),
        "status": "ok",
    }


def main():
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--ids", help="Comma-separated video IDs")
    src.add_argument("--from-fetch", help="youtube_fetch.py output file to enrich in place")
    parser.add_argument("--min-views", type=int, default=0,
                        help="With --from-fetch: only enrich videos at or above this view count (the outlier floor)")
    args = parser.parse_args()

    if args.ids:
        results = []
        for vid in [v.strip() for v in args.ids.split(",") if v.strip()]:
            results.append(fetch_details(vid))
            time.sleep(random.uniform(0.3, 0.8))
        json.dump(results, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return

    with open(args.from_fetch, "r", encoding="utf-8") as fh:
        fetch = json.load(fh)
    window_start = datetime.now(timezone.utc) - timedelta(days=fetch.get("window_days", 365))
    enriched = 0
    for v in fetch.get("videos", []):
        if v["view_count"] < args.min_views:
            continue
        d = fetch_details(v["video_id"])
        time.sleep(random.uniform(0.3, 0.8))
        if d["status"] != "ok":
            print(f"WARN: {v['video_id']} kept approximate data ({d.get('error')})",
                  file=sys.stderr)
            continue
        v["published_at"] = d["published_at"]
        v["view_count"] = d["view_count"]
        v["date_precision"] = "exact"
        published = datetime.fromisoformat(d["published_at"])
        if published < window_start:
            v["outside_window"] = True
        enriched += 1
    print(f"Enriched {enriched} video(s) with exact dates and view counts.",
          file=sys.stderr)
    json.dump(fetch, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
