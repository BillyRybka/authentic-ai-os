#!/usr/bin/env python3
"""
thumbnail_download.py: Download thumbnail images for vision analysis.

Used by vid-research to fetch outlier thumbnails before running vision
classification. Saves to a local cache directory and outputs the file paths
so the skill can read them into Claude vision.

Usage:
    python thumbnail_download.py --input thumbs.json --output-dir banks/proof-bank/assets/thumbnails

Input JSON shape (stdin or --input file):
    [
      {"video_id": "abc123", "thumbnail_url": "https://i.ytimg.com/..."},
      {"video_id": "def456", "thumbnail_url": "https://i.ytimg.com/..."},
      ...
    ]

Output JSON to stdout:
    [
      {"video_id": "abc123", "local_path": "/abs/path/to/abc123.jpg", "status": "ok"},
      {"video_id": "def456", "local_path": null, "status": "failed", "error": "..."},
      ...
    ]

The output dir is created if missing. Existing files are skipped (re-running
is idempotent unless you delete the cache).
"""

import argparse
import json
import os
import sys
import urllib.request
from urllib.error import URLError, HTTPError


def download_one(url: str, dest_path: str, timeout: int = 15) -> dict:
    """Download a single thumbnail. Returns status dict."""
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return {"local_path": os.path.abspath(dest_path), "status": "cached"}
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "vid-research/1.0 (pattern bank thumbnail fetch)"
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        if not data:
            return {"local_path": None, "status": "failed", "error": "empty response"}
        with open(dest_path, "wb") as f:
            f.write(data)
        return {"local_path": os.path.abspath(dest_path), "status": "ok"}
    except (URLError, HTTPError) as e:
        return {"local_path": None, "status": "failed", "error": str(e)}
    except Exception as e:
        return {"local_path": None, "status": "failed", "error": f"unexpected: {e}"}


def main():
    # Force UTF-8 on stdout/stderr so non-ascii in paths or errors doesn't
    # crash the run on Windows (default console is cp1252). Guarded for
    # interpreters older than 3.7 that lack reconfigure().
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        help="Path to input JSON file. If omitted, reads stdin.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory to save thumbnails. Created if missing.",
    )
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            payload = json.load(f)
    else:
        payload = json.load(sys.stdin)

    os.makedirs(args.output_dir, exist_ok=True)

    results = []
    for entry in payload:
        video_id = entry["video_id"]
        url = entry["thumbnail_url"]
        if not url:
            results.append(
                {
                    "video_id": video_id,
                    "local_path": None,
                    "status": "failed",
                    "error": "no thumbnail_url provided",
                }
            )
            continue
        # Use .jpg extension regardless of source URL (YouTube thumbs are jpg)
        dest = os.path.join(args.output_dir, f"{video_id}.jpg")
        outcome = download_one(url, dest)
        outcome["video_id"] = video_id
        results.append(outcome)

    json.dump(results, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
