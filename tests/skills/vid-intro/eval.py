#!/usr/bin/env python3
"""
Tier A eval for vid-intro. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (script.md, piece.md, transcript.md, plus
any updated bank entry files) and scores it against the frozen corpus + shared
fixtures + the suite-local after-structure stage. An output passes Tier A only
when every error-level assertion passes. Warnings are reported but never gate.
Prints a per-assertion breakdown and a final METRIC line the autoresearch
optimizer reads.

The produced files per case are script.md (intro stub replaced by the locked
6-part intro), piece.md (intro_locked, viewer_questions, used tracking), and
transcript.md. Only script.md and piece.md are scored: transcript.md
legitimately echoes the creator's own words and is never checked for
fabrication or brand rules (it IS read as a fallback location for the locked
Top 3 viewer questions, per the skill's "locked in piece.md or transcript"
contract).

Case layout (matches test_cases.json, input stage = suite-local
fixtures/after-structure because the global stage tree stops at after-intake):
  case_00 -> systems-beat-hustle            (deep-dive; receipt available)
  case_01 -> fired-himself-delegation       (case-study; inverted intro, receipt first)
  case_02 -> new-scheduling-feature-reaction(news; no setup, no credibility)
  case_03 -> 5-onboarding-mistakes          (listicle; count tease)
  case_04 -> thin-pricing-dump              (ADVERSARIAL: no numbers, no story)
  case_05 -> tempting-numbers-client-story  (ADVERSARIAL: numbers withheld, no bank links)

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  intro_section_present, hook_length, no_bolted_on_self_intro,
  no_tier1_banned_transitions, top3_questions_locked, setup_show_verb,
  intro_locked, bank_pull_tracked, handoff_intro_to_segment
Warnings (reported only):
  no_aiisms, no_hedge_words, hook_length_ideal, intro_total_length,
  tier2_flagged_transitions, bank_side_used_in

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

# --- constants from knowledge/transition-patterns.md Section 4 ---

# Tier 1 (auto-reject): B-1, B-2, B-3, B-6. These never surface in a saved intro.
TIER1_BANNED_TRANSITIONS = [
    ("B-1", re.compile(r"\blet'?s dive in\b", re.IGNORECASE)),
    ("B-2", re.compile(r"\blet'?s talk about\b", re.IGNORECASE)),
    ("B-3", re.compile(r"\blet me tell you\b", re.IGNORECASE)),
    ("B-6", re.compile(r"\band (finally|lastly)\b", re.IGNORECASE)),
]

# Tier 2 (soft friction): surfaced and flagged, creator decides. Warning only.
TIER2_FLAGGED_TRANSITIONS = [
    ("B-4", re.compile(r"\bwithout further ado\b", re.IGNORECASE)),
    ("B-5", re.compile(r"\bbefore we begin\b", re.IGNORECASE)),
    ("B-7", re.compile(r"\bhere'?s where it got interesting\b", re.IGNORECASE)),
    ("B-8", re.compile(r"\byou won'?t believe what happened next\b", re.IGNORECASE)),
    ("B-9", re.compile(r"\bnow let me tell you a quick story\b", re.IGNORECASE)),
    ("B-10", re.compile(r"\bstay tuned for\b", re.IGNORECASE)),
    ("B-11", re.compile(r"\btoday'?s video is about\b", re.IGNORECASE)),
    ("B-12", re.compile(r"\banyway,? moving on\b", re.IGNORECASE)),
]

# Bolted-on self-introduction (hook-patterns.md anti-pattern A-1): a greeting
# plus an "I am <name>" opener as a standalone beat. Credibility must weave
# into a claim moment, never open as a CV line.
_BOLTED_ON_RE = re.compile(
    r"(?im)^\s*(hi|hey|hello)\b[,.!]?\s+(i'?m|my name is)\b"
)

# Setup verbs per SKILL.md Phase 3: "show you" / "walk you through", never
# "talk about" / "tell you" (the negative half is covered by Tier 1 B-2/B-3).
_SETUP_VERB_RE = re.compile(r"\b(show you|walk you through)\b", re.IGNORECASE)

# Bank citation in the intro -> the piece-side tracking field that must hold it.
_BANK_FIELD_MAP = {
    "story-bank": "stories_used",
    "proof-bank": "proofs_used",
    "testimonial-bank": "testimonials_used",
    "metaphor-bank": "metaphors_used",
    "framework-bank": "frameworks_used",
}
_BANK_LINK_RE = re.compile(
    r"\[\[(story-bank|proof-bank|testimonial-bank|metaphor-bank|framework-bank)"
    r"/([^\]\|#]+)\]\]"
)

# A numbered question line in a transcript: "1. What is the trick?"
_NUMBERED_QUESTION_RE = re.compile(r"^\s*\d+[\.\)]\s+\S.*\?\s*$")

# Hook pacing: SKILL.md says under 5 seconds (roughly 15 words). 25 words is
# the hard ceiling (clear break), 15 is the ideal (flagged).
HOOK_WORDS_ERROR = 25
HOOK_WORDS_WARN = 15

# Whole-intro pacing by format planner typical length, at ~3 spoken words/sec.
# Warning only: the format planners treat length as a default, not a law.
INTRO_WORDS_WARN = {
    "news": 30,           # 5-10s
    "short-process": 45,  # 10-15s
    "listicle": 75,       # 15-25s
    "deep-dive": 180,     # 30-60s
}
INTRO_WORDS_WARN_DEFAULT = 90  # 30s

# The intro stub marker the after-structure script.md carries.
_STUB_MARKER = "intro stub"

# What vid-segment reads next (suite-local contract; tests/lib/check_handoff.py
# has no structure->intro or intro->segment boundary yet and lib is locked).
HANDOFF_PIECE_FIELDS = ["type", "slug", "format", "intro_locked"]


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


def _stage_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["input_stage"]))


def _read_if_exists(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _source_text(seed, fixtures_root, stage_root, slug):
    """
    The only legitimate source for numbers, links, and claims in this video's
    intro:

      1. The original seed text (the creator's raw dump from the corpus).
      2. The persona reveals (the creator's answers to follow-up questions).
      3. The persona withholds (gap labels only, never approved numbers).
      4. Any bank entries the seed explicitly allows (bank_pulls_allowed).
      5. The after-structure stage files for this slug: brain-dump.md,
         piece.md (locked title + thumbnail text), and script.md (the outline
         the Setup and Transition must forward into).
      6. foundation/creator-foundation.md, because SKILL.md Phase 2 pulls the
         credibility line from the foundation's brags or the brain dump.

    Mirrors the vid-framing pattern, extended with (5) and (6).
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        parts.append(_read_if_exists(os.path.join(fixtures_root, "banks", rel + ".md")))
    stage_dir = os.path.join(stage_root, slug)
    parts.append(_read_if_exists(os.path.join(stage_dir, "brain-dump.md")))
    parts.append(_read_if_exists(os.path.join(stage_dir, "piece.md")))
    parts.append(_read_if_exists(os.path.join(stage_dir, "script.md")))
    parts.append(_read_if_exists(
        os.path.join(fixtures_root, "foundation", "creator-foundation.md")
    ))
    return "\n\n".join(p for p in parts if p)


def _read_case_files(outputs_dir, i):
    """Read all .md files from outputs/case_NN/ (recursive, so updated bank
    entries are picked up). Returns None if folder missing."""
    case_dir = os.path.join(outputs_dir, f"case_{i:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for root, _dirs, names in os.walk(case_dir):
        for name in names:
            if name.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, name), case_dir)
                with open(os.path.join(root, name), encoding="utf-8") as f:
                    files[rel.replace(os.sep, "/")] = f.read()
    return files


# --- intro-section extraction helpers ---

def _extract_intro_section(script_text):
    """
    Return the raw text of the '## Intro' section (everything between the Intro
    heading and the next heading), or None if no Intro heading exists.
    """
    _, body = split_frontmatter(script_text)
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("#") and "intro" in s.lstrip("#").strip().lower():
            start = i
            break
    if start is None:
        return None
    section = []
    for line in lines[start + 1:]:
        if line.strip().startswith("#"):
            break
        section.append(line)
    return "\n".join(section)


def _spoken_lines(intro_text):
    """
    Spoken lines of the intro: non-empty, non-blockquote. Blockquote lines are
    production callouts (visual-proof notes, TODOs), not on-camera words.
    """
    out = []
    for line in intro_text.splitlines():
        s = line.strip()
        if not s or s.startswith(">"):
            continue
        out.append(s)
    return out


def _word_count(text):
    return len(text.split())


# --- skill-specific assertion functions ---

def check_intro_section_present(script_text):
    """
    Assert script.md has an '## Intro' section whose stub was actually replaced:
    the stub marker is gone and at least 25 spoken words are present (Hook +
    Problem/Result + Setup + Transition cannot land in fewer).
    """
    intro = _extract_intro_section(script_text)
    if intro is None:
        return t.CheckResult(
            "intro_section_present", False, "error",
            {"missing": "## Intro section"},
        )
    spoken = _spoken_lines(intro)
    words = sum(_word_count(l) for l in spoken)
    stub_left = _STUB_MARKER in intro.lower()
    ok = not stub_left and words >= 25
    detail = {}
    if stub_left:
        detail["stub_marker_left_in_place"] = True
    if words < 25:
        detail["spoken_words"] = words
    return t.CheckResult("intro_section_present", ok, "error", detail)


def check_hook_length(script_text):
    """
    Assert the Hook (first spoken line of the intro) is within the hard
    ceiling of 25 words. SKILL.md targets under 5 seconds (roughly 15 words);
    the worked credibility-hook examples run to about 19, so 25 is the line
    where a hook is unambiguously blown.
    """
    intro = _extract_intro_section(script_text) or ""
    spoken = _spoken_lines(intro)
    if not spoken:
        return t.CheckResult(
            "hook_length", False, "error", {"error": "no spoken intro lines"}
        )
    words = _word_count(spoken[0])
    ok = words <= HOOK_WORDS_ERROR
    detail = {} if ok else {"hook_words": words, "ceiling": HOOK_WORDS_ERROR,
                            "hook_line": spoken[0][:80]}
    return t.CheckResult("hook_length", ok, "error", detail)


def check_hook_length_ideal(script_text):
    """Warning: flag hooks over the 15-word / 5-second ideal."""
    intro = _extract_intro_section(script_text) or ""
    spoken = _spoken_lines(intro)
    if not spoken:
        return t.CheckResult("hook_length_ideal", True, "warning", {})
    words = _word_count(spoken[0])
    ok = words <= HOOK_WORDS_WARN
    detail = {} if ok else {"hook_words": words, "ideal": HOOK_WORDS_WARN}
    return t.CheckResult("hook_length_ideal", ok, "warning", detail)


def check_intro_total_length(script_text, piece_text):
    """Warning: flag intros over the format planner's typical length."""
    intro = _extract_intro_section(script_text) or ""
    words = sum(_word_count(l) for l in _spoken_lines(intro))
    fm, _ = split_frontmatter(piece_text)
    fmt = str(fm.get("format", "")).strip().lower()
    ceiling = INTRO_WORDS_WARN.get(fmt, INTRO_WORDS_WARN_DEFAULT)
    ok = words <= ceiling
    detail = {} if ok else {"intro_words": words, "format": fmt,
                            "typical_ceiling": ceiling}
    return t.CheckResult("intro_total_length", ok, "warning", detail)


def check_no_bolted_on_self_intro(script_text):
    """
    Assert the intro does not open with a bolted-on self-introduction
    ("Hi, I'm Sam..."). Hard rule 3 in SKILL.md: credibility weaves into a
    claim moment, never a separate self-introduction.
    """
    intro = _extract_intro_section(script_text) or ""
    spoken = "\n".join(_spoken_lines(intro))
    m = _BOLTED_ON_RE.search(spoken)
    ok = m is None
    detail = {} if ok else {"hit": m.group(0)}
    return t.CheckResult("no_bolted_on_self_intro", ok, "error", detail)


def _transition_scan(script_text, patterns):
    intro = _extract_intro_section(script_text) or ""
    spoken = "\n".join(_spoken_lines(intro))
    hits = []
    for tag, rx in patterns:
        m = rx.search(spoken)
        if m:
            hits.append(f"{tag}: \"{m.group(0)}\"")
    return hits


def check_no_tier1_banned_transitions(script_text):
    """
    Assert no Tier 1 banned transition phrase (transition-patterns.md Section
    4: B-1 'let's dive in', B-2 'let's talk about', B-3 'let me tell you',
    B-6 'and finally/lastly') appears in the intro. Hard rule 2 in SKILL.md.
    """
    hits = _transition_scan(script_text, TIER1_BANNED_TRANSITIONS)
    return t.CheckResult("no_tier1_banned_transitions", not hits, "error", hits)


def check_tier2_flagged_transitions(script_text):
    """Warning: Tier 2 phrases are soft friction, surfaced not auto-rejected."""
    hits = _transition_scan(script_text, TIER2_FLAGGED_TRANSITIONS)
    return t.CheckResult("tier2_flagged_transitions", not hits, "warning", hits)


def check_top3_questions_locked(piece_text, transcript_text):
    """
    Assert the Top 3 viewer questions were locked and persisted: either
    piece.md frontmatter carries a non-empty viewer_questions field, or the
    transcript shows the numbered list of 3 questions the creator approved.
    """
    fm, _ = split_frontmatter(piece_text)
    vq = fm.get("viewer_questions")
    if vq is not None and str(vq).strip().lower() not in ("", "null", "[]"):
        return t.CheckResult("top3_questions_locked", True, "error", {})
    questions = [
        l for l in transcript_text.splitlines()
        if _NUMBERED_QUESTION_RE.match(l)
    ]
    ok = len(questions) >= 3
    detail = {} if ok else {
        "viewer_questions_field": "absent",
        "numbered_questions_in_transcript": len(questions),
    }
    return t.CheckResult("top3_questions_locked", ok, "error", detail)


def check_setup_show_verb(script_text, piece_text):
    """
    Assert the Setup uses a show-verb ("show you" / "walk you through"), per
    SKILL.md Phase 3. Skipped for the news format, whose planner drops the
    Setup entirely (no Setup, no credibility line).
    """
    fm, _ = split_frontmatter(piece_text)
    fmt = str(fm.get("format", "")).strip().lower()
    if fmt == "news":
        return t.CheckResult(
            "setup_show_verb", True, "error",
            {"skipped": "news format has no Setup beat"},
        )
    intro = _extract_intro_section(script_text) or ""
    spoken = "\n".join(_spoken_lines(intro))
    ok = bool(_SETUP_VERB_RE.search(spoken))
    detail = {} if ok else {"missing": "\"show you\" or \"walk you through\""}
    return t.CheckResult("setup_show_verb", ok, "error", detail)


def check_intro_locked(piece_text):
    """Assert piece.md frontmatter carries intro_locked: true (Phase 5 save)."""
    fm, _ = split_frontmatter(piece_text)
    raw = fm.get("intro_locked")
    ok = raw is not None and str(raw).strip().lower() == "true"
    detail = {} if ok else {"intro_locked": raw}
    return t.CheckResult("intro_locked", ok, "error", detail)


def check_bank_pull_tracked(script_text, piece_text):
    """
    Piece-side of the vault-integration rule: every bank entry cited in the
    intro must appear in the matching piece.md frontmatter field
    (stories_used / proofs_used / testimonials_used / metaphors_used /
    frameworks_used). An intro that cites [[proof-bank/x]] without tracking it
    breaks the graph.
    """
    intro = _extract_intro_section(script_text) or ""
    fm, _ = split_frontmatter(piece_text)
    untracked = []
    for bank, slug in _BANK_LINK_RE.findall(intro):
        field = _BANK_FIELD_MAP[bank]
        tracked = str(fm.get(field, ""))
        if f"[[{bank}/{slug}]]" not in tracked:
            untracked.append({"link": f"[[{bank}/{slug}]]", "field": field})
    return t.CheckResult("bank_pull_tracked", not untracked, "error",
                         {"untracked": untracked} if untracked else {})


def check_bank_side_used_in(files, slug):
    """
    Bank-side of the vault-integration rule (warning: the secondary write is
    reflective per vault-integration.md, and the runner may not copy updated
    bank entries into the case folder). For every bank entry the piece tracks,
    if the case folder includes the updated bank file, its used_in must name
    the piece slug and its status must read 'used'.
    """
    piece_text = files.get("piece.md", "")
    fm, _ = split_frontmatter(piece_text)
    problems = []
    for field in ("stories_used", "proofs_used", "testimonials_used",
                  "metaphors_used", "frameworks_used"):
        for bank, bank_slug in _BANK_LINK_RE.findall(str(fm.get(field, ""))):
            target = None
            for rel in files:
                if rel.endswith(f"/{bank_slug}.md") or rel == f"{bank_slug}.md":
                    target = rel
                    break
            if target is None:
                problems.append(f"{bank}/{bank_slug}: updated bank file not in outputs")
                continue
            bank_fm, _ = split_frontmatter(files[target])
            if slug not in str(bank_fm.get("used_in", "")):
                problems.append(f"{bank}/{bank_slug}: used_in missing [[{slug}]]")
            if str(bank_fm.get("status", "")).strip().lower() != "used":
                problems.append(f"{bank}/{bank_slug}: status not 'used'")
    return t.CheckResult("bank_side_used_in", not problems, "warning", problems)


def check_handoff_intro_to_segment(script_text, piece_text):
    """
    Suite-local handoff boundary: what vid-segment reads next. piece.md must
    still carry the pipeline identity fields plus intro_locked, and script.md
    must still carry at least one body segment heading besides Intro (the
    outline the intro forwards into must survive the save).
    """
    fm, _ = split_frontmatter(piece_text)
    missing = [f for f in HANDOFF_PIECE_FIELDS
               if f not in fm or str(fm.get(f, "")).strip() in ("", "null")]
    _, body = split_frontmatter(script_text)
    body_segments = [
        l for l in body.splitlines()
        if l.strip().startswith("#") and "intro" not in l.strip().lstrip("#").strip().lower()
    ]
    detail = {}
    ok = True
    if missing:
        detail["piece_missing"] = missing
        ok = False
    if not body_segments:
        detail["script_body_segments"] = "none found besides Intro"
        ok = False
    return t.CheckResult("handoff_intro_to_segment", ok, "error", detail)


def evaluate_case(seed, files, fixtures_root, stage_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    script = files.get("script.md", "")
    piece = files.get("piece.md", "")
    transcript = files.get("transcript.md", "")
    slug = seed.get("slug", "")

    # script.md and piece.md are the vault files vid-intro writes.
    # transcript.md is excluded: it legitimately echoes the creator's words.
    vault_files = {"script.md": script, "piece.md": piece}

    source_text = _source_text(seed, fixtures_root, stage_root, slug)

    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures_root,
    }

    results = []
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))
    results.append(check_intro_section_present(script))
    results.append(check_hook_length(script))
    results.append(check_no_bolted_on_self_intro(script))
    results.append(check_no_tier1_banned_transitions(script))
    results.append(check_top3_questions_locked(piece, transcript))
    results.append(check_setup_show_verb(script, piece))
    results.append(check_intro_locked(piece))
    results.append(check_bank_pull_tracked(script, piece))
    results.append(check_handoff_intro_to_segment(script, piece))

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    results.append(check_hook_length_ideal(script))
    results.append(check_intro_total_length(script, piece))
    results.append(check_tier2_flagged_transitions(script))
    results.append(check_bank_side_used_in(files, slug))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = _fixtures_root(manifest)
    stage_root = _stage_root(manifest)

    error_assertions = [
        "no_em_dash",
        "no_banned_words",
        "no_fabrication",
        "intro_section_present",
        "hook_length",
        "no_bolted_on_self_intro",
        "no_tier1_banned_transitions",
        "top3_questions_locked",
        "setup_show_verb",
        "intro_locked",
        "bank_pull_tracked",
        "handoff_intro_to_segment",
    ]
    warn_assertions = [
        "no_aiisms",
        "no_hedge_words",
        "hook_length_ideal",
        "intro_total_length",
        "tier2_flagged_transitions",
        "bank_side_used_in",
    ]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-intro Tier A ({len(corpus)} seeds) ---")
    for i, seed in enumerate(corpus):
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{seed['slug']}]: NO OUTPUT (skipped)")
            continue
        if "script.md" not in files or "piece.md" not in files:
            print(f"  case {i:02d} [{seed['slug']}]: MISSING script.md or piece.md (skipped)")
            continue
        total += 1
        results = evaluate_case(seed, files, fixtures_root, stage_root)
        by_name = {r.name: r for r in results}

        if t.gate(results):
            total_pass += 1
        for a in error_assertions:
            if by_name[a].passed:
                assertion_pass[a] += 1
        for a in warn_assertions:
            if not by_name[a].passed:
                warn_hits[a] += 1

        print(t.format_case(f"{i:02d} [{seed['slug']}]", results))

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
    if pass_rate < 1.0:
        sys.exit(1)


if __name__ == "__main__":
    main()
