#!/usr/bin/env python3
"""
Tier A eval for post-write. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (post.md, optional transcript.md) and
scores it against the frozen corpus + fixtures. An output passes Tier A only
when every error-level assertion passes. Warnings (AI-isms, hedge words,
verbatim drift) are reported but never gate. Prints a per-assertion breakdown
and a final METRIC line the autoresearch optimizer reads.

post-write is the terminal skill (it emits posts, nothing downstream reads
them), so there is no handoff contract to assert.

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication, post_frontmatter,
  required_sections, clean_publishable_body, folder_discipline
Warnings (reported only):
  no_aiisms, no_hedge_words, verbatim_preserved

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
from check_fabrication import _normalize_numbers  # noqa: E402


# --- required frontmatter per the post-write note template ---
POST_FIELDS = [
    "type", "post_type", "platforms",
    "problem_addressed", "iceberg_aligned", "captured", "status",
]
# Headings every post note must carry. The core piece and at least one
# publishable platform block.
REQUIRED_SECTION_KEYS = ["core", "publishable"]

# A publishable body is clean copy that leaves the vault. No wikilinks, no
# markdown internal links. Provenance and frontmatter carry those instead.
_WIKILINK_RE = re.compile(r"\[\[")
_MDLINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")

# Spelled-out magnitude detection (WARNING, never gates). The shared fabrication
# check sees digit-form numbers only and deliberately tolerates small integer
# counts, so a spelled figure bound to a unit ("ten hours per client") can slip
# the gate. This surfaces spelled magnitudes (ten and up, so "one task" / "three
# steps" never trip it) whose value is absent from the creator's source.
_SPELLED = {
    "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30",
    "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70",
    "eighty": "80", "ninety": "90", "hundred": "100", "thousand": "1000",
    "million": "1000000",
}
_SPELLED_RE = re.compile(r"\b(" + "|".join(_SPELLED) + r")\b", re.IGNORECASE)


def _spelled_digits(text):
    return {_SPELLED[m.lower()] for m in _SPELLED_RE.findall(text)}


def find_spelled_number_risks(body_text, source_text):
    """
    Spelled magnitudes (ten and up) in the body whose value is not present in the
    source, in either spelled or digit form. Reported as a warning: the shared
    gate intentionally tolerates small integer counts, but an invented spelled
    figure like "ten hours per client" should still be visible to a reviewer.
    """
    src = _normalize_numbers(source_text) | _spelled_digits(source_text)
    seen, out = set(), []
    for m in _SPELLED_RE.findall(body_text):
        digit = _SPELLED[m.lower()]
        if digit in src:
            continue
        label = f"{m.lower()} (={digit})"
        if label not in seen:
            seen.add(label)
            out.append(label)
    return out


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
    The only legitimate source for these posts: the creator's dump, the persona's
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


def check_clean_publishable(post_text):
    """
    The ## Core and ## Publishable blocks are clean copy and must contain no
    wikilinks and no markdown internal links. The ## Provenance block and the
    frontmatter are exempt: that is where the graph links live. Sub-headings
    (### Visual brief) inside a clean block stay clean too.
    """
    _, body = split_frontmatter(post_text)
    bad = []
    in_clean = False
    for ln, line in enumerate(body.splitlines(), start=1):
        s = line.strip()
        if s.startswith("## "):
            heading = s[3:].strip().lower()
            in_clean = ("publishable" in heading) or ("core" in heading)
            continue
        if in_clean:
            if _WIKILINK_RE.search(line):
                bad.append(f"L{ln} wikilink: {s[:60]}")
            if _MDLINK_RE.search(line):
                bad.append(f"L{ln} markdown link: {s[:60]}")
    return t.CheckResult("clean_publishable_body", len(bad) == 0, "error", bad)


def evaluate_case(seed, files, fixtures_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    post = files.get("post.md", "")
    # the fabrication + brand checks look at the produced note only, never the
    # transcript (which legitimately echoes the creator's words)
    vault_files = {k: v for k, v in files.items() if k == "post.md"}

    source_text = _source_text(seed, fixtures_root)
    bundle = {"files": vault_files, "source_text": source_text, "fixtures_root": fixtures_root}

    results = []
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))
    results.append(t.check_frontmatter_complete("post_frontmatter", post, POST_FIELDS))
    results.append(t.check_required_sections("required_sections", post, REQUIRED_SECTION_KEYS))
    results.append(check_clean_publishable(post))

    folder_ok = "post.md" in files
    results.append(t.CheckResult("folder_discipline", folder_ok, "error",
                                 {} if folder_ok else {"missing": "post.md"}))

    # warnings (reported, do not gate). Posts are crafted, not a verbatim dump,
    # so verbatim drift is a signal, not a hard fail. Voice is judged in Tier B.
    vr = t.check_verbatim_preserved(post, seed.get("distinctive_phrases", []), min_ratio=0.5)
    results.append(t.CheckResult("verbatim_preserved", vr.passed, "warning", vr.detail))
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    spelled = find_spelled_number_risks(split_frontmatter(post)[1], source_text)
    results.append(t.CheckResult("spelled_number_risk", len(spelled) == 0, "warning", spelled))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = _fixtures_root(manifest)

    error_assertions = [
        "no_em_dash", "no_banned_words", "no_fabrication",
        "post_frontmatter", "required_sections", "clean_publishable_body",
        "folder_discipline",
    ]
    warn_assertions = ["verbatim_preserved", "no_aiisms", "no_hedge_words", "spelled_number_risk"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- post-write Tier A ({len(corpus)} seeds) ---")
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
