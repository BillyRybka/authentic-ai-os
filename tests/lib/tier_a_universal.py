"""
Tier A universal checks. Imported by every skill's eval.py so the brand rules
and anti-fabrication logic are written once and never drift per skill.

A "case bundle" is the set of files one skill run produced for one seed, plus
the seed's source text and the fixtures root:

    bundle = {
        "files":        {"brain-dump.md": "<text>", "piece.md": "<text>"},
        "source_text":  "<seed dump + persona answers, the only legit source>",
        "fixtures_root":"<abs path to tests/fixtures/shared>",
    }

Each check returns a CheckResult. eval.py composes the universal checks with
skill-specific ones, then gates: an output passes Tier A only when every
error-level check passes. Warnings are reported but never gate.
"""

import re
from collections import namedtuple

import vale_rules
from frontmatter import split_frontmatter, has_fields
from check_fabrication import check_no_fabrication

# level is "error" (gates) or "warning" (reported only)
CheckResult = namedtuple("CheckResult", ["name", "passed", "level", "detail"])


def _all_text(files):
    return "\n\n".join(files.values())


def check_no_em_dash(files):
    hits = []
    for fname, text in files.items():
        for ln, snip in vale_rules.scan_em_dash(text):
            hits.append(f"{fname}:{ln}  {snip}")
        for ln, snip in vale_rules.scan_double_hyphen_as_dash(text):
            hits.append(f"{fname}:{ln} (double-hyphen)  {snip}")
    return CheckResult("no_em_dash", len(hits) == 0, "error", hits)


def check_no_banned_words(files):
    found = sorted(set(vale_rules.scan_banned_words(_all_text(files))))
    return CheckResult("no_banned_words", len(found) == 0, "error", found)


def check_no_aiisms(files):
    found = sorted(set(vale_rules.scan_aiisms(_all_text(files))))
    return CheckResult("no_aiisms", len(found) == 0, "warning", found)


def check_no_hedge_words(files):
    found = sorted(set(vale_rules.scan_hedge_words(_all_text(files))))
    return CheckResult("no_hedge_words", len(found) == 0, "warning", found)


def check_frontmatter_complete(name, file_text, required):
    fm, _ = split_frontmatter(file_text)
    ok, missing = has_fields(fm, required)
    return CheckResult(name, ok, "error", {"missing": missing})


def check_fabrication(bundle):
    full = _all_text(bundle["files"])
    body = "\n\n".join(split_frontmatter(t)[1] for t in bundle["files"].values())
    passed, detail = check_no_fabrication(
        body_text=body,
        full_output_text=full,
        source_text=bundle["source_text"],
        fixtures_root=bundle["fixtures_root"],
    )
    return CheckResult("no_fabrication", passed, "error", detail)


def check_required_sections(name, file_text, required_keys):
    """
    Assert each required heading key appears in some markdown heading. Match is
    substring containment (case-insensitive) so "material" passes on a heading
    like "## Material" or "## Material pulled", tolerating minor wording drift.
    """
    headings = [
        line.strip().lstrip("#").strip().lower()
        for line in file_text.splitlines()
        if line.strip().startswith("#")
    ]
    missing = [k for k in required_keys if not any(k.lower() in h for h in headings)]
    return CheckResult(name, len(missing) == 0, "error", {"missing": missing})


def check_verbatim_preserved(file_text, phrases, min_ratio=0.6):
    """
    Assert that distinctive phrases from the seed survived into the output
    unaltered. phrases is a list of exact substrings the simulator was told to
    use. Passes when at least min_ratio of them appear verbatim. This is the
    "the brain dump IS the voice" guard: polishing erases the voice.
    """
    # markdown reflows across line breaks, so match whitespace-insensitively:
    # collapse every run of whitespace to a single space on both sides.
    norm = re.sub(r"\s+", " ", file_text.lower())
    def _present(p):
        return re.sub(r"\s+", " ", p.lower().strip()) in norm
    present = [p for p in phrases if _present(p)]
    ratio = (len(present) / len(phrases)) if phrases else 1.0
    missing = [p for p in phrases if not _present(p)]
    return CheckResult(
        "verbatim_preserved", ratio >= min_ratio, "error",
        {"ratio": round(ratio, 2), "missing": missing},
    )


def gate(results):
    """An output passes Tier A only when every error-level check passed."""
    return all(r.passed for r in results if r.level == "error")


def format_case(case_id, results):
    """One-line-per-check human summary for a single case."""
    lines = [f"  case {case_id}: {'PASS' if gate(results) else 'FAIL'}"]
    for r in results:
        if r.passed:
            continue
        tag = "FAIL" if r.level == "error" else "warn"
        lines.append(f"      [{tag}] {r.name}: {r.detail}")
    return "\n".join(lines)
