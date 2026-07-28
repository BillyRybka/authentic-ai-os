"""
Anti-fabrication checks. This is the spine of the whole harness.

Two failure modes, both deterministic because the corpus and fixtures are frozen:

1. Fabricated wikilink: the output cites [[bank/slug]] for a story, proof,
   metaphor, testimonial, or framework that does not exist on disk in the
   frozen fixtures. The skill invented a source.

2. Fabricated number: a dollar figure, percentage, or multiplier appears in the
   output prose but nowhere in the seed's provided source material. The skill
   invented a result. Plain small integers (counts like "3 mistakes") are
   ignored on purpose, only claim-shaped numbers are checked.
"""

import os
import re

from frontmatter import split_frontmatter

# [[bank-name/slug]] or [[slug]] or [[Note#Heading]] or [[Note|Display]]
_WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

# Claim-shaped numbers: money, percentages, multipliers, and large round counts.
_MONEY_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?\s?[kKmMbB]?")
_PERCENT_RE = re.compile(r"\b\d[\d,]*(?:\.\d+)?\s?%")
_MULTIPLIER_RE = re.compile(r"\b\d[\d,]*(?:\.\d+)?\s?[xX]\b")
_BIG_NUMBER_RE = re.compile(r"\b\d{3,}(?:,\d{3})*(?:\.\d+)?\b")

# Bank subfolders that a [[link]] might point into (per bank-contract.md).
_BANK_DIRS = [
    "story-bank", "proof-bank", "metaphor-bank",
    "testimonial-bank", "framework-bank", "packaging-bank",
]


def _link_target(raw):
    """Normalize a wikilink body to the slug to look up on disk."""
    target = raw.split("|", 1)[0]      # drop display text
    target = target.split("#", 1)[0]   # drop heading anchor
    return target.strip()


def _bank_link_targets(text):
    """
    Return wikilinks that look like bank citations: either an explicit
    bank-dir prefix (story-bank/foo) or a bare slug we will search the banks for.
    People links and foundation anchors are not bank citations and are skipped.
    """
    targets = []
    for raw in _WIKILINK_RE.findall(text):
        t = _link_target(raw)
        if not t:
            continue
        # foundation cross-refs and headings are not bank entries
        if t.lower().startswith("creator-foundation"):
            continue
        targets.append(t)
    return targets


def find_fabricated_links(text, fixtures_root):
    """
    Return the list of cited bank wikilinks whose target file does not exist in
    the frozen fixtures banks/ tree. A bare slug is matched against every bank
    subfolder; an explicit `bank-dir/slug` is matched against that folder.
    """
    banks_root = os.path.join(fixtures_root, "banks")
    fabricated = []
    for t in _bank_link_targets(text):
        if "/" in t:
            sub, slug = t.split("/", 1)
            candidates = [os.path.join(banks_root, sub, slug + ".md")]
        else:
            # could be a single-file bank or a people link; only treat as a
            # fabrication when it clearly names a bank slug that is missing
            # everywhere. People profiles live outside banks and are checked
            # elsewhere, so a bare name that matches no bank file is NOT flagged
            # here unless it carries a bank-dir prefix.
            candidates = [os.path.join(banks_root, d, t + ".md") for d in _BANK_DIRS]
        if not any(os.path.exists(c) for c in candidates):
            # only flag explicit bank-dir citations as fabricated; bare names
            # are too ambiguous to fail on (avoids false positives on prose)
            if "/" in t:
                fabricated.append(t)
    return fabricated


def find_fabricated_numbers(body_text, source_text):
    """
    Return claim-shaped numbers present in body_text but absent from source_text.
    Comparison is on a digits-only normalization so "$250K" matches a seed that
    says "250k" and "3x" matches "3 x". Dates are excluded by ignoring the
    frontmatter (callers pass body only).
    """
    source_norm = _normalize_numbers(source_text)
    fabricated = []
    for rx in (_MONEY_RE, _PERCENT_RE, _MULTIPLIER_RE, _BIG_NUMBER_RE):
        for hit in rx.findall(body_text):
            digits = re.sub(r"[^\dkmb]", "", hit.lower())
            if not digits or digits in ("", "k", "m", "b"):
                continue
            if digits not in source_norm:
                fabricated.append(hit.strip())
    # de-dup, keep order
    seen = set()
    out = []
    for h in fabricated:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out


def _normalize_numbers(text):
    """Collapse every claim-shaped number in text to its digits-only form set."""
    norm = set()
    for rx in (_MONEY_RE, _PERCENT_RE, _MULTIPLIER_RE, _BIG_NUMBER_RE):
        for hit in rx.findall(text):
            digits = re.sub(r"[^\dkmb]", "", hit.lower())
            if digits:
                norm.add(digits)
    # also index any bare run of digits so "grew to 40,000" in the seed covers
    # "40000" in the output even if the output omits the comma
    for hit in re.findall(r"\d[\d,]*", text):
        norm.add(re.sub(r"[^\d]", "", hit))
    return norm


def check_no_fabrication(body_text, full_output_text, source_text, fixtures_root):
    """
    Combined gate. Returns (passed, detail_dict).
    body_text       = prose only (frontmatter stripped), used for number checks
    full_output_text = whole file(s), used for wikilink scan
    source_text     = the seed dump + persona answers, the only legitimate source
    """
    bad_links = find_fabricated_links(full_output_text, fixtures_root)
    bad_numbers = find_fabricated_numbers(body_text, source_text)
    passed = not bad_links and not bad_numbers
    return passed, {"fabricated_links": bad_links, "fabricated_numbers": bad_numbers}


def strip_frontmatter_body(text):
    """Convenience: return prose body with frontmatter removed."""
    _, body = split_frontmatter(text)
    return body
