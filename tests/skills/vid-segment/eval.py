#!/usr/bin/env python3
"""
Tier A eval for vid-segment. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

vid-segment writes ONE body segment per run. Each run produces, in
outputs/case_NN/:

  script.md                 the skeleton with the segment prose appended under
                            its heading; every other section preserved
  piece.md                  frontmatter updated (segments_completed, the
                            matching *_used arrays, last_updated), every other
                            field untouched
  banks/<dir>/<slug>.md     one file per bank entry pulled this run: status
                            flipped captured -> used, used_in gains the piece
  transcript.md             the creator gate conversation. NEVER scored for
                            fabrication or brand rules: it legitimately echoes
                            the creator's own words.

An output passes Tier A only when every error-level assertion passes. Warnings
(AI-isms, hedge words) are reported but never gate. Exits non-zero when any
error-level assertion fails in any scored case (stricter than the front-of-
pipeline model suites, which only exit non-zero when no outputs are found).

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  segment_prose_appended, prior_sections_preserved,
  handoff_piece_fields, piece_fields_preserved,
  segments_completed_updated, used_arrays_updated, bank_entries_flipped,
  parable_present, show_before_tell,
  handoff_transition_present, no_banned_transition_phrases,
  gap_callout_present
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

# --- constants per SKILL.md Step 6 (the save contract) and transition-patterns.md ---

# The five append-only bank-pull arrays in piece.md frontmatter.
USED_ARRAYS = [
    "stories_used", "proofs_used", "metaphors_used",
    "testimonials_used", "frameworks_used",
]

# piece.md fields the NEXT vid-segment run (and vid-ending) read. This mirrors
# what a "segment->segment" entry in tests/lib/check_handoff.py would assert;
# tests/lib is locked, so the contract lives here until the lib catches up.
HANDOFF_FIELDS = [
    "type", "slug", "status", "format", "goal", "voice_context",
    "segment_purposes", "segments_completed", "tension_plan", "last_updated",
]

# piece.md fields vid-segment must never touch ("append only; never touch
# another skill's fields"). Compared verbatim against the fixture.
PROTECTED_FIELDS = [
    "type", "slug", "selected_angle", "core_payoff", "format", "goal",
    "voice_context", "segment_purposes", "tension_plan",
]

# transition-patterns.md Section 4, Tier 1 (auto-reject). Applied to the
# segment prose only.
TIER1_BANNED_TRANSITIONS = [
    "let's dive in", "lets dive in",
    "let's talk about", "lets talk about",
    "let me tell you",
    "and finally", "and lastly",
]

# Tell-signals for the show-before-tell check. If one of these appears in the
# prose BEFORE the parable anchor, the segment named the lesson and then
# explained it, which SKILL.md Step 3 calls the sin that kills the segment.
TELL_MARKERS = [
    "the lesson", "the takeaway", "the point is", "the rule",
    "what this proves", "the mistake:", "the principle",
    "that is the mistake",
]

_WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


# --- loading helpers ---

def _load_manifest():
    with open(os.path.join(_HERE, "test_cases.json"), encoding="utf-8") as f:
        return json.load(f)


def _load_corpus(manifest):
    path = os.path.normpath(os.path.join(_HERE, manifest["corpus"]))
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _read(rel_root, *parts):
    path = os.path.join(rel_root, *parts)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _read_case_files(outputs_dir, case_no):
    """
    Read every .md file under outputs/case_NN/, keyed by path relative to the
    case folder (so banks/story-bank/x.md keeps its subfolder). Returns None if
    the folder is missing.
    """
    case_dir = os.path.join(outputs_dir, f"case_{case_no:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for root, _dirs, names in os.walk(case_dir):
        for name in names:
            if name.endswith(".md"):
                full = os.path.join(root, name)
                rel = os.path.relpath(full, case_dir).replace(os.sep, "/")
                with open(full, encoding="utf-8") as f:
                    files[rel] = f.read()
    return files


def _source_text(seed, fixtures_root, brain_dump_text, fixture_piece, fixture_script):
    """
    The only legitimate source for numbers, links, and claims in this run:
    the seed, the persona answers, the allowed bank entries, the after-intake
    brain dump, and the frozen after-structure state (piece.md + script.md)
    the skill consumed. Mirrors the vid-framing pattern, extended with the
    upstream script skeleton.
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        parts.append(_read(fixtures_root, "banks", rel + ".md"))
    parts.append(brain_dump_text)
    parts.append(fixture_piece)
    parts.append(fixture_script)
    return "\n\n".join(p for p in parts if p)


# --- prose helpers ---

def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


def _sections(body):
    """Split a markdown body into (heading_line, [body_lines]) per ## heading."""
    sections = []
    head = None
    buf = []
    for line in body.splitlines():
        if line.startswith("## "):
            if head is not None:
                sections.append((head, buf))
            head = line.strip()
            buf = []
        elif head is not None:
            buf.append(line)
    if head is not None:
        sections.append((head, buf))
    return sections


def _segment_lines(script_text, segment_heading):
    """Return (heading, lines) of the target segment section, else (None, None)."""
    _, body = split_frontmatter(script_text)
    for head, lines in _sections(body):
        if segment_heading.lower() in head.lower():
            return head, lines
    return None, None


def _prose_lines(lines):
    """Drop callouts, plan lines, and blanks; what remains is spoken prose."""
    out = []
    for line in lines:
        s = line.strip()
        if not s or s.startswith(">"):
            continue
        low = s.lower()
        if low.startswith("**parable:**") or low.startswith("**principle:**"):
            continue
        out.append(s)
    return out


def _fm_list(fm, key):
    """Parse a frontmatter field into a list of strings (inline or yaml list)."""
    v = fm.get(key)
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x) for x in v]
    s = str(v).strip()
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip('"').strip("'") for p in inner.split(",")]
    return [s.strip('"').strip("'")] if s else []


def _wiki_set(fm, key):
    """The set of wikilinks carried by a *_used frontmatter array."""
    links = set()
    for item in _fm_list(fm, key):
        links.update(_WIKILINK_RE.findall(item))
    return links


# --- skill-specific assertions ---

def check_segment_prose_appended(output_script, case):
    """
    The segment heading exists in script.md and carries at least min_words of
    spoken prose (callouts and **Parable:**/**Principle:** plan lines do not
    count). A heading with only the skeleton plan under it means the skill
    saved without writing.
    """
    head, lines = _segment_lines(output_script, case["segment_heading"])
    if head is None:
        return t.CheckResult(
            "segment_prose_appended", False, "error",
            {"missing_heading": case["segment_heading"]},
        )
    words = len(" ".join(_prose_lines(lines)).split())
    ok = words >= case["min_words"]
    detail = {} if ok else {"words": words, "min_words": case["min_words"]}
    return t.CheckResult("segment_prose_appended", ok, "error", detail)


def check_prior_sections_preserved(fixture_script, output_script, case):
    """
    Every non-blank fixture line outside the target segment's body must survive
    into the output: prior segment prose, the intro, later plan sections, the
    To build list, the CUTS comment, and every heading including the target's.
    "Append the locked prose. Preserve all prior sections." Lines matching an
    allowed_drops entry (e.g. a To build row this segment consumed) are exempt.
    """
    _, fbody = split_frontmatter(fixture_script)
    _, obody = split_frontmatter(output_script)
    out_norm = _norm(obody).lower()
    target = case["segment_heading"].lower()
    drops = [d.lower() for d in case.get("allowed_drops", [])]
    in_target = False
    missing = []
    for line in fbody.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_target = target in s.lower()
        if not s:
            continue
        if in_target and not s.startswith("## "):
            continue  # the target section body is the part being written
        if any(d in s.lower() for d in drops):
            continue
        if _norm(s).lower() not in out_norm:
            missing.append(s[:120])
    ok = not missing
    detail = {} if ok else {"missing_count": len(missing), "missing": missing[:8]}
    return t.CheckResult("prior_sections_preserved", ok, "error", detail)


def check_piece_fields_preserved(fixture_piece, output_piece):
    """
    Append-only discipline: the fields other skills own (angle, payoff, format,
    goal, voice_context, segment_purposes, tension_plan) must be byte-identical
    to the fixture after normalization.
    """
    f_fm, _ = split_frontmatter(fixture_piece)
    o_fm, _ = split_frontmatter(output_piece)
    changed = []
    for field in PROTECTED_FIELDS:
        fv = _norm(str(f_fm.get(field, "")))
        ov = _norm(str(o_fm.get(field, "")))
        if fv != ov:
            changed.append({"field": field, "was": fv[:80], "now": ov[:80]})
    ok = not changed
    return t.CheckResult(
        "piece_fields_preserved", ok, "error", {"changed": changed} if changed else {}
    )


def check_segments_completed_updated(fixture_piece, output_piece, case):
    """
    segments_completed gains this segment's label and keeps every label the
    fixture already had (append only).
    """
    f_fm, _ = split_frontmatter(fixture_piece)
    o_fm, _ = split_frontmatter(output_piece)
    before = set(_fm_list(f_fm, "segments_completed"))
    after = set(_fm_list(o_fm, "segments_completed"))
    missing_prior = sorted(before - after)
    added = case["segment_label"] in after
    ok = added and not missing_prior
    detail = {}
    if not added:
        detail["missing_label"] = case["segment_label"]
    if missing_prior:
        detail["dropped_prior_labels"] = missing_prior
    return t.CheckResult("segments_completed_updated", ok, "error", detail)


def check_used_arrays_updated(fixture_piece, output_piece, case):
    """
    Each of the five *_used arrays gains EXACTLY the wikilinks the case spec
    declares and loses nothing. Exact-match both ways: a missing pull means the
    save step was skipped; an extra link (the adversarial failure mode) means
    the skill recorded material it was never given.
    """
    f_fm, _ = split_frontmatter(fixture_piece)
    o_fm, _ = split_frontmatter(output_piece)
    expected = case.get("expected_used", {})
    problems = {}
    for arr in USED_ARRAYS:
        before = _wiki_set(f_fm, arr)
        after = _wiki_set(o_fm, arr)
        want = set()
        for item in expected.get(arr, []):
            want.update(_WIKILINK_RE.findall(item))
        if after - before != want or before - after:
            problems[arr] = {
                "expected_new": sorted(want),
                "actual_new": sorted(after - before),
                "dropped": sorted(before - after),
            }
    ok = not problems
    return t.CheckResult(
        "used_arrays_updated", ok, "error", {"problems": problems} if problems else {}
    )


def check_bank_entries_flipped(outputs_files, case):
    """
    Every bank entry pulled this run is written back: file present under
    banks/, status flipped to used, used_in contains [[{piece-slug}]]. Step 6
    updates both sides of the link; piece.md alone is half the job.
    """
    problems = {}
    for rel in case.get("bank_updates", []):
        key = f"banks/{rel}.md"
        text = outputs_files.get(key)
        if text is None:
            problems[rel] = "file missing"
            continue
        fm, _ = split_frontmatter(text)
        status = str(fm.get("status", "")).strip().lower()
        used_in = " ".join(_fm_list(fm, "used_in"))
        issues = []
        if status != "used":
            issues.append(f"status={status!r}")
        if f"[[{case['slug']}]]" not in used_in:
            issues.append(f"used_in missing [[{case['slug']}]]")
        if issues:
            problems[rel] = issues
    ok = not problems
    return t.CheckResult(
        "bank_entries_flipped", ok, "error", {"problems": problems} if problems else {}
    )


def check_parable_present(output_script, case):
    """
    The prose carries the picked parable: at least one anchor token from the
    parable's material (story detail, demo beat, metaphor image) appears in the
    segment body. A principle-only segment where the outline planned a parable
    is a research summary, not a segment.
    """
    _head, lines = _segment_lines(output_script, case["segment_heading"])
    if lines is None:
        return t.CheckResult("parable_present", False, "error",
                             {"missing_heading": case["segment_heading"]})
    prose = " ".join(_prose_lines(lines)).lower()
    anchors = case.get("parable_anchors", [])
    if not anchors:
        return t.CheckResult("parable_present", True, "error", {"skipped": "no parable planned"})
    found = [a for a in anchors if a.lower() in prose]
    ok = len(found) > 0
    detail = {} if ok else {"anchors": anchors}
    return t.CheckResult("parable_present", ok, "error", detail)


def check_show_before_tell(output_script, case):
    """
    Where the outline planned a parable, the show lands before the tell. Fails
    only on positive evidence: a tell-marker phrase ("the lesson", "that is the
    mistake", ...) appears in the prose BEFORE the first parable anchor. If no
    tell-marker appears at all, the check cannot prove a violation and passes.
    Full setup/payoff quality is Tier B territory.
    """
    _head, lines = _segment_lines(output_script, case["segment_heading"])
    if lines is None:
        return t.CheckResult("show_before_tell", False, "error",
                             {"missing_heading": case["segment_heading"]})
    prose = " ".join(_prose_lines(lines)).lower()
    anchors = [a.lower() for a in case.get("parable_anchors", [])]
    anchor_idx = min((prose.find(a) for a in anchors if prose.find(a) >= 0),
                     default=-1)
    tell_idx = min((prose.find(mk) for mk in TELL_MARKERS if prose.find(mk) >= 0),
                   default=-1)
    if anchor_idx == -1 or tell_idx == -1:
        return t.CheckResult("show_before_tell", True, "error",
                             {"note": "no positive tell-before-show evidence"})
    ok = anchor_idx < tell_idx
    detail = {} if ok else {"anchor_at": anchor_idx, "tell_at": tell_idx}
    return t.CheckResult("show_before_tell", ok, "error", detail)


def check_handoff_transition_present(output_script, case):
    """
    The segment closes on a handoff, not a full stop. The last prose paragraph
    must contain at least one forward cue for the next beat (case-spec'd per
    segment: the next point's label, a result word, a next-video hook). "Here's
    step 4" is dead; a segment that ends on its own takeaway strands the next
    writer.
    """
    _head, lines = _segment_lines(output_script, case["segment_heading"])
    if lines is None:
        return t.CheckResult("handoff_transition_present", False, "error",
                             {"missing_heading": case["segment_heading"]})
    prose = _prose_lines(lines)
    if not prose:
        return t.CheckResult("handoff_transition_present", False, "error",
                             {"detail": "no prose in segment"})
    last = prose[-1].lower()
    cues = case.get("handoff_cues", [])
    found = [c for c in cues if c.lower() in last]
    ok = len(found) > 0
    detail = {} if ok else {"last_paragraph": last[:160], "cues": cues}
    return t.CheckResult("handoff_transition_present", ok, "error", detail)


def check_no_banned_transition_phrases(output_script, case):
    """transition-patterns.md Section 4 Tier 1, scanned over the segment prose."""
    _head, lines = _segment_lines(output_script, case["segment_heading"])
    if lines is None:
        return t.CheckResult("no_banned_transition_phrases", False, "error",
                             {"missing_heading": case["segment_heading"]})
    prose = " ".join(_prose_lines(lines)).lower()
    found = [p for p in TIER1_BANNED_TRANSITIONS if p in prose]
    ok = not found
    return t.CheckResult(
        "no_banned_transition_phrases", ok, "error", {"found": found} if found else {}
    )


def check_gap_callout_present(output_script, case):
    """
    Adversarial gate: when the skeleton leaves a slot open (proof to build), the
    segment names the gap with a callout instead of filling it with invented
    material. Only active when the case spec sets requires_callout.
    """
    want = case.get("requires_callout")
    if not want:
        return t.CheckResult("gap_callout_present", True, "error",
                             {"skipped": "no open slot in this case"})
    head, lines = _segment_lines(output_script, case["segment_heading"])
    if head is None:
        return t.CheckResult("gap_callout_present", False, "error",
                             {"missing_heading": case["segment_heading"]})
    raw = "\n".join(lines).lower()
    ok = f"> [!{want.lower()}]" in raw
    detail = {} if ok else {"required": f"> [!{want}]"}
    return t.CheckResult("gap_callout_present", ok, "error", detail)


# --- case evaluation ---

def evaluate_case(case, seed, files, fixtures_root, input_stage_root, suite_fixtures_root):
    slug = case["slug"]
    script = files.get("script.md", "")
    piece = files.get("piece.md", "")

    fixture_piece = _read(suite_fixtures_root, slug, "piece.md")
    fixture_script = _read(suite_fixtures_root, slug, "script.md")
    brain_dump = _read(input_stage_root, slug, "brain-dump.md")

    # transcript.md is excluded everywhere: it legitimately echoes the creator.
    vault_files = {k: v for k, v in files.items() if k != "transcript.md"}

    source_text = _source_text(
        seed, fixtures_root, brain_dump, fixture_piece, fixture_script
    )
    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures_root,
    }

    results = []
    # universal brand + fabrication spine
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))

    # script.md: the prose and what it must not break
    results.append(check_segment_prose_appended(script, case))
    results.append(check_prior_sections_preserved(fixture_script, script, case))
    results.append(check_parable_present(script, case))
    results.append(check_show_before_tell(script, case))
    results.append(check_handoff_transition_present(script, case))
    results.append(check_no_banned_transition_phrases(script, case))
    results.append(check_gap_callout_present(script, case))

    # piece.md: the save contract and the downstream handoff
    results.append(
        t.check_frontmatter_complete("handoff_piece_fields", piece, HANDOFF_FIELDS)
    )
    results.append(check_piece_fields_preserved(fixture_piece, piece))
    results.append(check_segments_completed_updated(fixture_piece, piece, case))
    results.append(check_used_arrays_updated(fixture_piece, piece, case))

    # bank entries: the other side of every pulled link
    results.append(check_bank_entries_flipped(files, case))

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = os.path.normpath(os.path.join(_HERE, manifest["fixtures"]))
    input_stage_root = os.path.normpath(os.path.join(_HERE, manifest["input_stage"]))
    suite_fixtures_root = os.path.normpath(os.path.join(_HERE, manifest["suite_fixtures"]))
    cases = manifest["cases"]

    error_assertions = [
        "no_em_dash",
        "no_banned_words",
        "no_fabrication",
        "segment_prose_appended",
        "prior_sections_preserved",
        "handoff_piece_fields",
        "piece_fields_preserved",
        "segments_completed_updated",
        "used_arrays_updated",
        "bank_entries_flipped",
        "parable_present",
        "show_before_tell",
        "handoff_transition_present",
        "no_banned_transition_phrases",
        "gap_callout_present",
    ]
    warn_assertions = ["no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-segment Tier A ({len(cases)} cases) ---")
    for case in cases:
        i = case["case"]
        slug = case["slug"]
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{slug}]: NO OUTPUT (skipped)")
            continue
        if "script.md" not in files or "piece.md" not in files:
            print(f"  case {i:02d} [{slug}]: MISSING script.md or piece.md (skipped)")
            continue
        seed = corpus[case["seed_index"]]
        total += 1
        results = evaluate_case(
            case, seed, files, fixtures_root, input_stage_root, suite_fixtures_root
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
    sys.exit(0 if total_pass == total else 1)


if __name__ == "__main__":
    main()
