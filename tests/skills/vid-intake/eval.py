#!/usr/bin/env python3
"""
Tier A eval for vid-intake. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (brain-dump.md, piece.md, optional
transcript.md) and scores it against the frozen corpus + fixtures. An output
passes Tier A only when every error-level assertion passes. Warnings (AI-isms,
hedge words) are reported but never gate. Prints a per-assertion breakdown and a
final METRIC line the autoresearch optimizer reads.

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication, brain_dump_frontmatter,
  piece_frontmatter, alignment_captured, required_sections, verbatim_preserved,
  folder_discipline, handoff_intake_to_framing
Warnings (reported only):
  no_aiisms, no_hedge_words

Usage:
  python eval.py [outputs_dir]
"""

import json
import os
import sys

# make tests/lib importable
_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.normpath(os.path.join(_HERE, "..", "..", "lib"))
sys.path.insert(0, _LIB)

import tier_a_universal as t  # noqa: E402
from check_handoff import check_handoff  # noqa: E402


# --- required frontmatter per the vid-intake SKILL.md output schema ---
BRAIN_DUMP_FIELDS = [
    "type", "slug", "intake_mode", "captured", "iceberg_aligned",
]
PIECE_FIELDS = ["type", "slug", "status", "captured"]  # pillar may be null
ALIGNMENT_FIELDS = ["iceberg_aligned"]
REQUIRED_SECTION_KEYS = [
    "topic", "audience", "outcome", "material", "open questions",
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


def _source_text(seed, fixtures_root):
    """
    The only legitimate source for this video: the creator's dump, the persona's
    revealed and withheld lines, and any bank entries they were allowed to pull.
    A number or link not traceable to this text is a fabrication.
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        bank_path = os.path.join(fixtures_root, "banks", rel + ".md")
        if os.path.exists(bank_path):
            with open(bank_path, encoding="utf-8") as f:
                parts.append(f.read())
    return "\n\n".join(parts)


def _read_case_files(outputs_dir, i):
    case_dir = os.path.join(outputs_dir, f"case_{i:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for name in os.listdir(case_dir):
        if name.endswith(".md"):
            with open(os.path.join(case_dir, name), encoding="utf-8") as f:
                files[name] = f.read()
    return files


def evaluate_case(seed, files, fixtures_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    brain = files.get("brain-dump.md", "")
    piece = files.get("piece.md", "")
    # the fabrication + brand checks look at the produced vault files only,
    # never the transcript (which legitimately echoes the creator's words)
    vault_files = {k: v for k, v in files.items() if k in ("brain-dump.md", "piece.md")}

    source_text = _source_text(seed, fixtures_root)
    bundle = {"files": vault_files, "source_text": source_text, "fixtures_root": fixtures_root}

    results = []
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))
    results.append(t.check_frontmatter_complete("brain_dump_frontmatter", brain, BRAIN_DUMP_FIELDS))
    results.append(t.check_frontmatter_complete("piece_frontmatter", piece, PIECE_FIELDS))
    results.append(t.check_frontmatter_complete("alignment_captured", brain, ALIGNMENT_FIELDS))
    results.append(t.check_required_sections("required_sections", brain, REQUIRED_SECTION_KEYS))
    results.append(t.check_verbatim_preserved(brain, seed.get("distinctive_phrases", [])))

    folder_ok = ("brain-dump.md" in files) and ("piece.md" in files)
    results.append(t.CheckResult("folder_discipline", folder_ok, "error",
                                 {} if folder_ok else {"missing": "brain-dump.md and/or piece.md"}))

    handoff_ok, handoff_detail = check_handoff("intake->framing",
                                               {"brain-dump.md": brain, "piece.md": piece})
    results.append(t.CheckResult("handoff_intake_to_framing", handoff_ok, "error", handoff_detail))

    # warnings (reported, do not gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = _fixtures_root(manifest)

    error_assertions = [
        "no_em_dash", "no_banned_words", "no_fabrication",
        "brain_dump_frontmatter", "piece_frontmatter", "alignment_captured",
        "required_sections", "verbatim_preserved", "folder_discipline",
        "handoff_intake_to_framing",
    ]
    warn_assertions = ["no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-intake Tier A ({len(corpus)} seeds) ---")
    for i, seed in enumerate(corpus):
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{seed['slug']}]: NO OUTPUT (skipped)")
            continue
        total += 1
        results = evaluate_case(seed, files, fixtures_root)
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
