#!/usr/bin/env python3
"""
Tier A eval for vid-framing. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (piece.md, transcript.md) and scores
it against the frozen corpus + fixtures + after-intake stage files. An output
passes Tier A only when every error-level assertion passes. Warnings (AI-isms,
hedge words) are reported but never gate. Prints a per-assertion breakdown and
a final METRIC line the autoresearch optimizer reads.

The produced files per case are piece.md and transcript.md. Only piece.md is
scored: transcript.md legitimately echoes the creator's own words and is never
checked for fabrication or brand rules.

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  piece_framing_frontmatter, format_enum, goal_enum,
  read_section, handoff_framing_to_structure
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
from check_handoff import check_handoff  # noqa: E402
from frontmatter import split_frontmatter  # noqa: E402

# --- field lists per SKILL.md "Output: piece.md" and piece-framing-additions.md ---

# The six fields vid-framing ADDS to piece.md frontmatter.
# Authority is knowledge/piece-contract.md (field ownership table), which lists
# frame, core_payoff, format, voice_context, goal for vid-framing, plus the
# last_updated bump every writing skill makes.
#
# `mechanism` was required here until 2026-08-06 and was removed: it appears
# nowhere in piece-contract.md and nothing downstream reads it. It came from a
# parallel draft of the skill that never became the shipped one.
FRAMING_FIELDS = [
    "frame",
    "core_payoff",
    "format",
    "goal",
    "voice_context",
    "last_updated",
]

# Valid enumerations, lower-cased for comparison.
VALID_FORMATS = {
    "short-process", "case-study", "roast", "deep-dive",
    "interview", "news", "listicle",
}
VALID_GOALS = {"sales", "emails", "views"}

# The body section vid-framing must append (substring match, case-insensitive).
READ_SECTION_KEY = "the read"

# The three fields '## The Read' must carry, per knowledge/piece-contract.md.
# core_payoff is frontmatter only: it locks with the frame, before the read
# exists, so there is no body copy for it to drift against.
READ_FIELDS = ("target", "transformation", "stakes")


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


def _intake_stage_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["input_stage"]))


def _load_after_intake_brain_dump(intake_stage_root, slug):
    """
    Load the frozen brain-dump.md from the after-intake stage for this seed.
    Returns empty string if the file is missing (case is skipped at higher level).
    """
    path = os.path.join(intake_stage_root, slug, "brain-dump.md")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _source_text(seed, fixtures_root, brain_dump_text):
    """
    The only legitimate source for numbers, links, and claims in this video's
    piece.md:

      1. The original seed text (the creator's raw dump from the corpus).
      2. The persona reveals (the creator's answers to follow-up questions).
      3. The persona withholds (names the topics but gives no data; included so
         the fabrication check can see what the creator mentioned without
         providing proof, but numbers in withholds are NOT approved sources).
      4. Any bank entries the seed explicitly allows (bank_pulls_allowed).
      5. The after-intake brain-dump.md for this slug (frozen upstream output).

    This mirrors the pattern in vid-intake/eval.py and extends it with (5).
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    # withholds describe what is NOT available; they carry the gap labels,
    # never the numbers themselves, so including them is safe.
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        bank_path = os.path.join(fixtures_root, "banks", rel + ".md")
        if os.path.exists(bank_path):
            with open(bank_path, encoding="utf-8") as f:
                parts.append(f.read())
    # add the upstream brain-dump so numbers captured at intake are legitimate
    if brain_dump_text:
        parts.append(brain_dump_text)
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


# --- skill-specific assertion functions ---

def check_piece_framing_frontmatter(piece_text):
    """
    Assert piece.md frontmatter contains all six fields that vid-framing is
    required to write, per SKILL.md 'Output: piece.md' and
    assets/piece-framing-additions.md.

    Fields: frame, core_payoff, format, goal, voice_context, last_updated.
    """
    return t.check_frontmatter_complete(
        "piece_framing_frontmatter", piece_text, FRAMING_FIELDS
    )


def check_format_enum(piece_text):
    """
    Assert the 'format' frontmatter field is one of the seven allowed values:
    short-process, case-study, roast, deep-dive, interview, news, listicle.

    An absent or misspelled format value is a hard fail: the downstream skill
    (vid-structure) reads this field to pick the scaffold.
    """
    fm, _ = split_frontmatter(piece_text)
    raw = fm.get("format", "")
    value = str(raw).strip().lower() if raw else ""
    ok = value in VALID_FORMATS
    detail = {} if ok else {"format_value": raw, "allowed": sorted(VALID_FORMATS)}
    return t.CheckResult("format_enum", ok, "error", detail)


def check_goal_enum(piece_text):
    """
    Assert the 'goal' frontmatter field is one of: sales, emails, views.

    An absent or invalid goal is a hard fail: downstream analytics and the
    vid-title skill use this to set the CTA and packaging direction.
    """
    fm, _ = split_frontmatter(piece_text)
    raw = fm.get("goal", "")
    value = str(raw).strip().lower() if raw else ""
    ok = value in VALID_GOALS
    detail = {} if ok else {"goal_value": raw, "allowed": sorted(VALID_GOALS)}
    return t.CheckResult("goal_enum", ok, "error", detail)




def check_read_section(piece_text):
    """
    Assert piece.md body contains '## The Read' carrying all three fields.

    The section is contracted in knowledge/piece-contract.md as Target /
    Transformation / Stakes. It drifted shape twice while nothing outside
    vid-framing specified it; this check is the mechanical half of that
    fix. Downstream readers are soft (vid-title presses on Stakes, vid-intro
    mines them for hooks, vid-structure builds toward Transformation), so a
    missing field degrades a reader silently rather than failing loudly.

    Heading match is substring, case-insensitive. Field match looks for each
    label anywhere in the section body, so both '**Target:**' and '**Target.**'
    pass.
    """
    lines = piece_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("#") and READ_SECTION_KEY in line.strip().lstrip("#").strip().lower():
            start = i
            break
    if start is None:
        return t.CheckResult("read_section", False, "error", {"missing": "## The Read"})

    body = []
    for line in lines[start + 1:]:
        if line.strip().startswith("## "):
            break
        body.append(line.lower())
    body_text = "\n".join(body)

    missing = [f for f in READ_FIELDS if f not in body_text]
    detail = {} if not missing else {"missing_fields": missing}
    return t.CheckResult("read_section", not missing, "error", detail)


def evaluate_case(seed, files, fixtures_root, intake_stage_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    piece = files.get("piece.md", "")
    slug = seed.get("slug", "")

    # piece.md is the only vault file produced by vid-framing.
    # transcript.md is excluded: it legitimately echoes the creator's words.
    vault_files = {"piece.md": piece}

    brain_dump_text = _load_after_intake_brain_dump(intake_stage_root, slug)
    source_text = _source_text(seed, fixtures_root, brain_dump_text)

    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures_root,
    }

    results = []
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))
    results.append(check_piece_framing_frontmatter(piece))
    results.append(check_format_enum(piece))
    results.append(check_goal_enum(piece))
    results.append(check_read_section(piece))

    handoff_ok, handoff_detail = check_handoff(
        "framing->structure", {"piece.md": piece}
    )
    results.append(
        t.CheckResult("handoff_framing_to_structure", handoff_ok, "error", handoff_detail)
    )

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = _fixtures_root(manifest)
    intake_stage_root = _intake_stage_root(manifest)

    error_assertions = [
        "no_em_dash",
        "no_banned_words",
        "no_fabrication",
        "piece_framing_frontmatter",
        "format_enum",
        "goal_enum",
        "handoff_framing_to_structure",
    ]
    warn_assertions = ["no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-framing Tier A ({len(corpus)} seeds) ---")
    for i, seed in enumerate(corpus):
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{seed['slug']}]: NO OUTPUT (skipped)")
            continue
        if "piece.md" not in files:
            print(f"  case {i:02d} [{seed['slug']}]: MISSING piece.md (skipped)")
            continue
        total += 1
        results = evaluate_case(seed, files, fixtures_root, intake_stage_root)
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


if __name__ == "__main__":
    main()
