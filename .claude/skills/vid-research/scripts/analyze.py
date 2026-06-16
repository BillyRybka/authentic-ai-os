#!/usr/bin/env python3
"""
analyze.py: Consolidate per-channel youtube_fetch outputs into one outlier
inventory, applying the per-channel floors the skill decided.

Why this exists: outlier math (median, cadence, sorting, multipliers) plus titles
that may contain emoji or smart quotes will crash an ad-hoc `python -c` one-liner
on Windows (cp1252 console). This script is UTF-8 hardened end to end, so the skill
never has to hand-roll fragile inline Python. Run this instead of improvising.

Inputs:
  --fetch-dir DIR   Directory of fetch JSON files, one per channel, each the raw
                    stdout of youtube_fetch.py saved as {slug}.json.
  --floors FILE     JSON mapping each {slug} to the floor the skill set (with the
                    creator). The floor is a raw view count, scaled to the channel
                    (see outlier-identification-rules.md). Optional bucket label.
                    Example:
                      {
                        "coachx":  {"floor": 60000,  "bucket": "direct"},
                        "dailyfit":{"floor": 48000,  "bucket": "adjacent"},
                        "mega":    {"floor": 1000000,"bucket": "style-only"}
                      }
  --out FILE        Where to write consolidated.json (default: <fetch-dir>/consolidated.json).
  --cut YYYY-MM-DD  Optional. Only count videos published on/after this date, for
                    narrowing the window without re-fetching. Default: use all
                    videos in each fetch file (already windowed by youtube_fetch).

Output: writes consolidated.json and prints a UTF-8-safe summary table.

All examples here are generic placeholders. No real channel data lives in this file.
"""

import argparse
import json
import os
import statistics
import sys


def harden_utf8():
    """Force UTF-8 on stdout/stderr so emoji/smart-quotes in titles never crash
    the run on a cp1252 console. Guarded for interpreters older than 3.7."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def main():
    harden_utf8()
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fetch-dir", required=True, help="Dir of {slug}.json fetch outputs")
    ap.add_argument("--floors", required=True, help="JSON mapping slug -> {floor, bucket}")
    ap.add_argument("--out", default=None, help="Output consolidated.json path")
    ap.add_argument("--cut", default=None, help="Optional published-on-or-after YYYY-MM-DD")
    args = ap.parse_args()

    floors = load_json(args.floors)
    out_path = args.out or os.path.join(args.fetch_dir, "consolidated.json")

    consolidated = {}
    for slug, cfg in floors.items():
        fpath = os.path.join(args.fetch_dir, slug + ".json")
        if not os.path.exists(fpath):
            print(f"WARN: no fetch file for '{slug}' at {fpath}, skipping", file=sys.stderr)
            continue
        d = load_json(fpath)
        floor = cfg.get("floor", d.get("median_2x_reference", 0))
        bucket = cfg.get("bucket", "")

        vids = d.get("videos", [])
        if args.cut:
            vids = [v for v in vids if (v.get("published_at", "")[:10] >= args.cut)]
        median = statistics.median([v["view_count"] for v in vids]) if vids else 0
        median = int(median) or 1

        outliers = sorted(
            [v for v in vids if v["view_count"] >= floor],
            key=lambda v: v["view_count"], reverse=True,
        )
        for v in outliers:
            v["multiplier"] = round(v["view_count"] / median, 1)

        consolidated[slug] = {
            "handle": d.get("channel_handle"),
            "title": d.get("channel_title"),
            "subscriber_count": d.get("subscriber_count"),
            "median": median,
            "videos_per_month": d.get("videos_per_month"),
            "floor": floor,
            "bucket": bucket,
            "outlier_count": len(outliers),
            "outliers": outliers,
        }

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(consolidated, fh, ensure_ascii=False, indent=1)

    total = sum(c["outlier_count"] for c in consolidated.values())
    print(f"Wrote {out_path}. Channels: {len(consolidated)}. Total outliers: {total}")
    print(f"{'slug':<16}{'bucket':<12}{'median':>9}{'floor':>10}{'outliers':>9}")
    for slug, c in consolidated.items():
        print(f"{slug:<16}{c['bucket']:<12}{c['median']:>9,}{c['floor']:>10,}{c['outlier_count']:>9}")


if __name__ == "__main__":
    main()
