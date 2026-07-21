#!/usr/bin/env python3
"""
Tier A eval for vid-ending. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (script.md with the filled ## Ending
block, piece.md with ending_locked + next_video) and scores it against the
frozen corpus + fixtures + the suite-local upstream stage and published-video
catalog. An output passes Tier A only when every error-level assertion passes.
Warnings (AI-isms, hedge words) are reported but never gate. Prints a
per-assertion breakdown and a final METRIC line the autoresearch optimizer
reads.

The produced files per case are script.md, piece.md, and optionally
transcript.md. Only script.md and piece.md are scored: transcript.md
legitimately echoes the creator's own words and is never checked for
fabrication or brand rules.

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  ending_block_present, pivot_gap_bridge_beats, bridge_is_last,
  beat_sentence_budget, close_length, no_banned_cta_language,
  next_video_resolves, goal_cta_rules, gap_traces_to_top3,
  ending_locked_set, handoff_ending_to_pressure_test
Warnings (reported only):
  no_aiisms, no_hedge_words

Usage:
  python eval.py [outputs_dir]
"""

import json
import os
import re
import sys

# make tests/lib importable
_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.normpath(os.path.join(_HERE, "..", "..", "lib"))
sys.path.insert(0, _LIB)

import tier_a_universal as t  # noqa: E402
from frontmatter import split_frontmatter  # noqa: E402

# --- constants per vid-ending SKILL.md, its references, and the ending template ---

# Beat markers from assets/ending-block-template.md. The skill fills the
# template's slots, so the locked block keeps these HTML comment markers.
RE_PIVOT = re.compile(r"<!--\s*PIVOT\s*-->", re.IGNORECASE)
RE_GAP = re.compile(r"<!--\s*GAP\s*-->", re.IGNORECASE)
RE_CTA = re.compile(r"<!--\s*CTA", re.IGNORECASE)  # template's CTA comment carries a condition note
RE_BRIDGE = re.compile(r"<!--\s*BRIDGE\s*-->", re.IGNORECASE)
RE_ENDSCREEN = re.compile(r"<!--\s*END SCREEN", re.IGNORECASE)

# The end-screen cue line, e.g. [END SCREEN: some-slug, card animates in ...]
RE_ENDSCREEN_CUE = re.compile(r"\[END SCREEN:[^\]]*\]")
RE_ENDSCREEN_CUE_SLUG = re.compile(r"\[END SCREEN:\s*([A-Za-z0-9][A-Za-z0-9-]*)")

# Any HTML comment line or editor cue bracket line is not spoken prose.
RE_HTML_COMMENT = re.compile(r"<!--.*?-->")

# Banned close language. From references/ending-anti-patterns.md Section 5
# (the auto-reject list) plus the ending-relevant Tier 1 phrases from
# knowledge/transition-patterns.md Section 4. Substring scan, case-insensitive,
# applied to the ## Ending block only.
BANNED_CLOSE_PHRASES = [
    "and finally", "and lastly",
    "to wrap this up", "to wrap it up", "to wrap things up",
    "in conclusion",
    "thanks for watching", "thank you for watching", "appreciate you watching",
    "if you liked", "if you enjoyed",
    "please subscribe", "smash the like", "smash that like",
    "stay tuned", "until next time", "catch you in the next", "see you next time",
    "without further ado",
    "today's video was about", "in this video we covered", "in today's video",
    "i hope you enjoyed",
    "let me know in the comments", "let me know what you think",
    "drop a comment", "drop your comment",
    "don't forget to",
    "hit the bell", "turn on notifications",
    "more to learn",  # the vague-gap dead noun (S-9 / gap near-miss)
]

# Keyword sets that make the Gap traceable to a creator-foundation Top 3
# problem instead of an invented one. Derived from the frozen
# fixtures/shared/foundation/creator-foundation.md Top 3:
#   1. drowning in the work, never enough time
#   2. everything depends on me, cannot delegate or step away
#   3. undercharging and overworking
# If the frozen foundation changes its Top 3, update these sets with it.
TOP3_KEYWORDS = {
    1: ["time", "hours", "hour", "week", "drowning", "slammed", "capacity",
        "room to work", "enough of you"],
    2: ["delegat", "bottleneck", "depends on", "depend on", "document",
        "steps", "hand off", "handed", "someone else", "in your head",
        "in their head", "team", "step away", "on you"],
    3: ["charg", "price", "pricing", "money", "worth", "undercharg",
        "rate", "rates", "fees"],
}

# Close length budget from SKILL.md Phase 2: 30-60 seconds read aloud,
# "roughly 60-150 words". Deterministic gate allows a small tolerance band
# around that rough figure; Tier B judges the read-aloud feel.
CLOSE_MIN_WORDS = 50
CLOSE_MAX_WORDS = 160

# What the NEXT skill (vid-pressure-test) reads from piece.md. Declared
# locally because tests/lib/check_handoff.py is locked shared infra and has
# no ending boundary yet; mirror this into HANDOFF_CONTRACTS when lib opens.
PRESSURE_TEST_CONTRACT = [
    "type", "slug", "format", "goal", "ending_locked", "next_video",
]


def _load_manifest():
    path = os.path.join(_HERE, "test_cases.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_corpus(manifest):
    corpus_path = os.path.normpath(os.path.join(_HERE, manifest["corpus"]))
    with open(corpus_path, encoding="utf-8") as f:
        return json.load(f)


def _fixtures_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["fixtures"]))


def _upstream_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["upstream_stage"]))


def _catalog_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["catalog"]))


def _read_rel(root, *parts):
    path = os.path.join(root, *parts)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _source_text(seed, fixtures_root, upstream_root, slug):
    """
    The only legitimate source for numbers, links, and claims in this video's
    ending: the seed, the persona reveals and withholds, the allowed bank
    entries, the after-intake brain-dump, and the frozen upstream script.md
    (the lock list the SKILL builds in Phase 1: every number in the close must
    already appear in the script).
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        bank_text = _read_rel(fixtures_root, "banks", rel + ".md")
        if bank_text:
            parts.append(bank_text)
    brain_dump = _read_rel(
        os.path.normpath(os.path.join(_HERE, "..", "..", "fixtures", "stages", "after-intake")),
        slug, "brain-dump.md",
    )
    if brain_dump:
        parts.append(brain_dump)
    upstream_script = _read_rel(upstream_root, slug, "script.md")
    if upstream_script:
        parts.append(upstream_script)
    upstream_piece = _read_rel(upstream_root, slug, "piece.md")
    if upstream_piece:
        parts.append(upstream_piece)
    return "\n\n".join(parts)


def _read_case_files(outputs_dir, i):
    """Read all .md files from outputs/case_NN/. Returns None if folder missing."""
    case_dir = os.path.join(outputs_dir, f"case_{i:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for name in os.listdir(case_dir):
        if name.endswith(".md"):
            with open(os.path.join(case_dir, name), encoding="utf-8") as f:
                files[name] = f.read()
    return files


# --- ending-block parsing helpers ---

def _extract_ending_block(script_text):
    """
    Return the body text under the '## Ending' heading, up to the next level-2
    heading or end of file. Empty string when the heading is absent.
    """
    _, body = split_frontmatter(script_text)
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+Ending\b", line.strip(), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return ""
    block = []
    for line in lines[start:]:
        if re.match(r"^##\s+\S", line.strip()) and not line.strip().lower().startswith("## ending"):
            break
        block.append(line)
    return "\n".join(block)


def _beat_positions(block):
    """Marker -> start offset of the marker comment within the block."""
    marks = {}
    for name, rx in (("pivot", RE_PIVOT), ("gap", RE_GAP),
                     ("cta", RE_CTA), ("bridge", RE_BRIDGE),
                     ("endscreen", RE_ENDSCREEN)):
        m = rx.search(block)
        if m:
            marks[name] = (m.start(), m.end())
    return marks


def _beat_text(block, marks, name):
    """Spoken text between this marker and the next marker, comments stripped."""
    if name not in marks:
        return ""
    start = marks[name][1]
    following = [v[0] for k, v in marks.items() if v[0] >= start]
    end = min(following) if following else len(block)
    segment = block[start:end]
    segment = RE_HTML_COMMENT.sub("", segment)
    segment = RE_ENDSCREEN_CUE.sub("", segment)
    return segment.strip()


def _spoken_words(block):
    """All spoken words in the block: strip comments and editor cue lines."""
    text = RE_HTML_COMMENT.sub("", block)
    kept = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("[END SCREEN"):
            continue
        kept.append(s)
    return len(" ".join(kept).split())


# --- skill-specific assertion functions ---

def check_ending_block_present(script_text):
    """script.md must carry a ## Ending heading with real content under it."""
    block = _extract_ending_block(script_text)
    ok = bool(block.strip())
    detail = {} if ok else {"missing": "## Ending block in script.md"}
    return t.CheckResult("ending_block_present", ok, "error", detail)


def check_pivot_gap_bridge_beats(script_text, goal):
    """
    The filled template must keep identifiable Pivot, Gap, and Bridge beats, in
    formula order, each with spoken content. The CTA beat is required for
    sales/emails goals and must be omitted for views (per the template note).
    """
    block = _extract_ending_block(script_text)
    if not block.strip():
        return t.CheckResult("pivot_gap_bridge_beats", False, "error",
                             {"missing": "## Ending block"})
    marks = _beat_positions(block)
    detail = {}
    ok = True
    for beat in ("pivot", "gap", "bridge"):
        if beat not in marks:
            detail[beat] = "marker missing"
            ok = False
        elif len(_beat_text(block, marks, beat).split()) < 3:
            detail[beat] = "beat has no spoken content"
            ok = False
    if ok:
        order_ok = marks["pivot"][0] < marks["gap"][0] < marks["bridge"][0]
        if not order_ok:
            detail["order"] = "beats out of Pivot -> Gap -> Bridge order"
            ok = False
    if goal == "views":
        if "cta" in marks and _beat_text(block, marks, "cta"):
            detail["cta"] = "CTA block present but goal=views (template says omit)"
            ok = False
    else:
        if "cta" not in marks or not _beat_text(block, marks, "cta"):
            detail["cta"] = f"CTA block missing but goal={goal}"
            ok = False
    return t.CheckResult("pivot_gap_bridge_beats", ok, "error", detail)


def check_bridge_is_last(script_text):
    """
    The Bridge triggers the end-screen click; nothing spoken may follow it
    (end-screen-design.md Section 5). Only the END SCREEN editor cue may come
    after the Bridge beat.
    """
    block = _extract_ending_block(script_text)
    if not block.strip():
        return t.CheckResult("bridge_is_last", False, "error",
                             {"missing": "## Ending block"})
    marks = _beat_positions(block)
    if "bridge" not in marks:
        return t.CheckResult("bridge_is_last", False, "error",
                             {"missing": "BRIDGE marker"})
    # only the endscreen marker may follow the bridge marker
    late = [k for k, v in marks.items()
            if k != "bridge" and v[0] > marks["bridge"][0] and k != "endscreen"]
    if late:
        return t.CheckResult("bridge_is_last", False, "error",
                             {"markers_after_bridge": late})
    # everything after the bridge beat (or after the endscreen cue when one
    # exists) must be empty once comments and the cue line are stripped
    if "endscreen" in marks:
        tail = block[marks["endscreen"][1]:]
        # the marker regex stops mid-comment; skip to the comment's close
        close = tail.find("-->")
        if close != -1:
            tail = tail[close + 3:]
    else:
        # no endscreen cue: the bridge's own spoken text is allowed, nothing else
        tail = block[marks["bridge"][1]:]
        beat = _beat_text(block, marks, "bridge")
        tail = tail.replace(beat, "", 1)
    tail = RE_HTML_COMMENT.sub("", tail)
    tail = RE_ENDSCREEN_CUE.sub("", tail)
    leftover = tail.strip()
    ok = not leftover
    detail = {} if ok else {"spoken_after_bridge": leftover[:120]}
    return t.CheckResult("bridge_is_last", ok, "error", detail)


def _sentence_count(text):
    """Count sentence-ending punctuation runs. Colons and commas do not count."""
    return len(re.findall(r"[.!?]+(?:\s|$)", text))


def check_beat_sentence_budget(script_text):
    """
    Per pivot-gap-bridge-shapes.md length budgets: Pivot 1-2 sentences (3+ is
    a recap dump, auto-reject), Gap 1-2, Bridge 1-2. This also stops a post-
    Bridge sign-off smuggled inside the Bridge beat (end-screen-design.md
    Section 5: nothing after the Bridge).
    """
    block = _extract_ending_block(script_text)
    if not block.strip():
        return t.CheckResult("beat_sentence_budget", False, "error",
                             {"missing": "## Ending block"})
    marks = _beat_positions(block)
    over = {}
    for beat in ("pivot", "gap", "bridge"):
        text = _beat_text(block, marks, beat)
        if not text:
            continue
        n = _sentence_count(text)
        if n > 2:
            over[beat] = n
    ok = not over
    detail = {} if ok else {"over_budget_sentences": over, "budget": "max 2 per beat"}
    return t.CheckResult("beat_sentence_budget", ok, "error", detail)


def check_close_length(script_text):
    """
    SKILL.md Phase 2: 30-60 seconds read aloud, roughly 60-150 words. Longer
    is a recap (banned, S-10); shorter is a bare CTA (banned, S-4). Gate uses a
    tolerance band around the rough figure.
    """
    block = _extract_ending_block(script_text)
    if not block.strip():
        return t.CheckResult("close_length", False, "error",
                             {"missing": "## Ending block"})
    words = _spoken_words(block)
    ok = CLOSE_MIN_WORDS <= words <= CLOSE_MAX_WORDS
    detail = {} if ok else {
        "words": words,
        "allowed": f"{CLOSE_MIN_WORDS}-{CLOSE_MAX_WORDS}",
    }
    return t.CheckResult("close_length", ok, "error", detail)


def check_no_banned_cta_language(script_text):
    """
    Scan the ## Ending block against the auto-reject phrase list from
    references/ending-anti-patterns.md Section 5 plus ending-relevant Tier 1
    phrases from knowledge/transition-patterns.md Section 4. Any hit is a hard
    fail: these phrases telegraph the end, beg, or wind the video down.
    """
    block = _extract_ending_block(script_text).lower()
    hits = [p for p in BANNED_CLOSE_PHRASES if p in block]
    return t.CheckResult("no_banned_cta_language", len(hits) == 0, "error", hits)


def _next_video_slug(piece_text):
    fm, _ = split_frontmatter(piece_text)
    raw = fm.get("next_video", "")
    if not raw:
        return None, "next_video field missing"
    raw = str(raw).strip()
    m = re.match(r"^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$", raw)
    if not m:
        return None, f"next_video is not a wikilink: {raw!r}"
    return m.group(1).strip(), None


def check_next_video_resolves(script_text, piece_text, catalog_root):
    """
    The Bridge must point at a real, already-published video (end-screen R-2,
    SKILL Phase 4: never save a broken wikilink). The next_video slug must
    resolve to a piece.md in the frozen catalog, and the script's END SCREEN
    cue must name the same slug.
    """
    slug, err = _next_video_slug(piece_text)
    if err:
        return t.CheckResult("next_video_resolves", False, "error", {"error": err})
    target = os.path.join(catalog_root, "content", "pieces", slug, "piece.md")
    detail = {}
    ok = True
    if not os.path.exists(target):
        detail["unresolved_wikilink"] = slug
        ok = False
    block = _extract_ending_block(script_text)
    cue = RE_ENDSCREEN_CUE_SLUG.search(block)
    if not cue:
        detail["end_screen_cue"] = "missing [END SCREEN: slug, ...] cue"
        ok = False
    elif cue.group(1) != slug:
        detail["cue_slug_mismatch"] = {"cue": cue.group(1), "next_video": slug}
        ok = False
    return t.CheckResult("next_video_resolves", ok, "error", detail)


def check_goal_cta_rules(script_text, piece_text, catalog_root, goal, fmt):
    """
    Goal x format rules from references/cta-placement-by-format.md and
    end-screen-design.md:

    - views: no CTA block (checked in beats), no external links, and no
      description-link language anywhere in the close (R-3).
    - sales/emails: the Bridge target converts for this goal (catalog goal
      field matches; end-screen-design Option 1).
    - news format: the Bridge target is never another news video (R-4);
      for views goal the target must be evergreen.
    """
    block = _extract_ending_block(script_text).lower()
    detail = {}
    ok = True
    if goal == "views":
        if "http" in block or "www." in block:
            detail["external_link"] = "goal=views close carries an external link (R-3)"
            ok = False
        if "description" in block:
            detail["description_link"] = "goal=views close points at a description link (R-3)"
            ok = False
    slug, err = _next_video_slug(piece_text)
    if err:
        detail["next_video"] = err
        return t.CheckResult("goal_cta_rules", False, "error", detail)
    target_text = _read_rel(catalog_root, "content", "pieces", slug, "piece.md")
    if not target_text:
        detail["target"] = f"{slug} not in catalog"
        return t.CheckResult("goal_cta_rules", False, "error", detail)
    tfm, _ = split_frontmatter(target_text)
    target_format = str(tfm.get("format", "")).strip().lower()
    target_goal = str(tfm.get("goal", "")).strip().lower()
    target_evergreen = str(tfm.get("evergreen", "")).strip().lower() in ("true", "yes")
    if fmt == "news" and target_format == "news":
        detail["news_to_news"] = f"bridged to news video {slug} (R-4)"
        ok = False
    if goal in ("sales", "emails") and target_goal != goal:
        detail["goal_mismatch"] = {
            "target": slug, "target_goal": target_goal, "needed": goal,
        }
        ok = False
    if goal == "views" and not target_evergreen:
        detail["not_evergreen"] = f"goal=views must bridge to evergreen, {slug} is not"
        ok = False
    return t.CheckResult("goal_cta_rules", ok, "error", detail)


def check_gap_traces_to_top3(script_text, fixtures_root):
    """
    The Gap names a problem from the creator-foundation Top 3, not an invented
    one (SKILL Phase 1, anti-pattern S-2). Deterministic proxy: the Gap beat
    must contain at least one keyword from one of the three Top 3 keyword sets
    derived from the frozen foundation. Tier B judges whether the Gap is the
    RIGHT problem for the chosen next video.
    """
    foundation = _read_rel(fixtures_root, "foundation", "creator-foundation.md")
    if "top 3" not in foundation.lower():
        return t.CheckResult("gap_traces_to_top3", False, "error",
                             {"fixture": "creator-foundation.md has no Top 3 section"})
    block = _extract_ending_block(script_text)
    marks = _beat_positions(block)
    gap_text = _beat_text(block, marks, "gap").lower()
    if not gap_text:
        return t.CheckResult("gap_traces_to_top3", False, "error",
                             {"missing": "GAP beat"})
    matched = [p for p, kws in TOP3_KEYWORDS.items()
               if any(k in gap_text for k in kws)]
    ok = len(matched) > 0
    detail = {} if ok else {
        "gap_text": gap_text[:160],
        "expected": "a keyword traceable to one Top 3 problem",
    }
    if ok:
        detail = {"matched_top3_problem": matched}
    return t.CheckResult("gap_traces_to_top3", ok, "error", detail)


def check_ending_locked_set(piece_text):
    """piece.md must carry ending_locked: true and a bumped last_updated."""
    fm, _ = split_frontmatter(piece_text)
    raw = fm.get("ending_locked")
    locked = raw is True or str(raw).strip().lower() in ("true", "yes")
    detail = {}
    ok = True
    if not locked:
        detail["ending_locked"] = raw if raw is not None else "missing"
        ok = False
    if not fm.get("last_updated"):
        detail["last_updated"] = "missing"
        ok = False
    return t.CheckResult("ending_locked_set", ok, "error", detail)


def check_handoff_local(piece_text):
    """
    Local handoff contract for the ending -> vid-pressure-test boundary.
    tests/lib/check_handoff.py is locked shared infra with no ending boundary,
    so the contract is declared here; mirror it into HANDOFF_CONTRACTS when
    lib opens for edits.
    """
    fm, _ = split_frontmatter(piece_text)
    missing = [f for f in PRESSURE_TEST_CONTRACT
               if f not in fm or fm[f] in (None, "", "null")]
    return t.CheckResult("handoff_ending_to_pressure_test",
                         len(missing) == 0, "error", {"missing": missing})


def evaluate_case(seed, case_cfg, files, fixtures_root, upstream_root, catalog_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    script = files.get("script.md", "")
    piece = files.get("piece.md", "")
    slug = seed.get("slug", "")
    goal = case_cfg["goal"]
    fmt = case_cfg["format"]

    # transcript.md is excluded: it legitimately echoes the creator's words.
    vault_files = {"script.md": script, "piece.md": piece}

    source_text = _source_text(seed, fixtures_root, upstream_root, slug)
    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures_root,
    }

    results = []
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))
    results.append(check_ending_block_present(script))
    results.append(check_pivot_gap_bridge_beats(script, goal))
    results.append(check_bridge_is_last(script))
    results.append(check_beat_sentence_budget(script))
    results.append(check_close_length(script))
    results.append(check_no_banned_cta_language(script))
    results.append(check_next_video_resolves(script, piece, catalog_root))
    results.append(check_goal_cta_rules(script, piece, catalog_root, goal, fmt))
    results.append(check_gap_traces_to_top3(script, fixtures_root))
    results.append(check_ending_locked_set(piece))
    results.append(check_handoff_local(piece))

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    seeds_by_slug = {s["slug"]: s for s in corpus}
    fixtures_root = _fixtures_root(manifest)
    upstream_root = _upstream_root(manifest)
    catalog_root = _catalog_root(manifest)

    error_assertions = [
        "no_em_dash",
        "no_banned_words",
        "no_fabrication",
        "ending_block_present",
        "pivot_gap_bridge_beats",
        "bridge_is_last",
        "beat_sentence_budget",
        "close_length",
        "no_banned_cta_language",
        "next_video_resolves",
        "goal_cta_rules",
        "gap_traces_to_top3",
        "ending_locked_set",
        "handoff_ending_to_pressure_test",
    ]
    warn_assertions = ["no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-ending Tier A ({len(manifest['cases'])} cases) ---")
    for case_cfg in manifest["cases"]:
        i = case_cfg["index"]
        slug = case_cfg["slug"]
        seed = seeds_by_slug.get(slug)
        if seed is None:
            print(f"  case {i:02d} [{slug}]: NOT IN CORPUS (skipped)")
            continue
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{slug}]: NO OUTPUT (skipped)")
            continue
        if "script.md" not in files or "piece.md" not in files:
            print(f"  case {i:02d} [{slug}]: MISSING script.md or piece.md (skipped)")
            continue
        total += 1
        results = evaluate_case(
            seed, case_cfg, files, fixtures_root, upstream_root, catalog_root
        )
        by_name = {r.name: r for r in results}

        if t.gate(results):
            total_pass += 1
        for a in error_assertions:
            if by_name[a].passed:
                assertion_pass[a] += 1
        for a in warn_assertions:
            if not by_name[a].passed:
                warn_hits[a] += 1

        print(t.format_case(f"{i:02d} [{slug}]", results))

    if total == 0:
        print("\nERROR: no output case folders found under " + outputs_dir)
        print("METRIC tier_a_pass_rate=0.0000")
        sys.exit(1)

    print(f"\n--- Assertion breakdown ({total} scored) ---")
    for a in error_assertions:
        pct = assertion_pass[a] / total * 100
        print(f"  {a}: {assertion_pass[a]}/{total} ({pct:.0f}%)")
    print("  warnings (not gating):")
    for a in warn_assertions:
        print(f"    {a}: {warn_hits[a]}/{total} cases had hits")

    pass_rate = total_pass / total
    print(f"\nDETAIL {total_pass}/{total} outputs passed ALL Tier A error checks")
    print(f"METRIC tier_a_pass_rate={pass_rate:.4f}")
    # hard gate: non-zero exit when any error-level check failed
    sys.exit(0 if total_pass == total else 1)


if __name__ == "__main__":
    main()
