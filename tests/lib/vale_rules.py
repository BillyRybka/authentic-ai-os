"""
Brand-rule scanners, mirrored from .vale/styles/ProductVoice/.

These are the deterministic "does it work" checks for the hardest brand rules.
The tokens here MUST stay in sync with the Vale style files, which are the
source of truth used at save time inside the skills:

  .vale/styles/ProductVoice/EmDash.yml      -> EM_DASH
  .vale/styles/ProductVoice/EnDash.yml      -> EN_DASH
  .vale/styles/ProductVoice/BannedWords.yml -> BANNED_WORDS (level: error)
  .vale/styles/ProductVoice/AIisms.yml      -> AIISMS (level: warning)
  .vale/styles/ProductVoice/HedgeWords.yml  -> HEDGE_WORDS (level: warning)

Em-dash and banned words are errors (Tier A hard fails). AI-isms and hedge
words are warnings (reported, not gating) so the loop can see them without
blocking on style nits.
"""

import re

# --- error-level tokens (gate Tier A) ---

EM_DASH = "—"   # the em-dash character, banned outright
EN_DASH = "–"   # the en-dash character, banned outright

# From BannedWords.yml. ignorecase: true.
BANNED_WORDS = [
    "leverage", "leverages", "leveraged", "leveraging",
    "optimize", "optimizes", "optimized", "optimizing", "optimization",
    "unlock", "unlocks", "unlocked", "unlocking",
    "unleash", "unleashes", "unleashed", "unleashing",
    "utilize", "utilizes", "utilized", "utilizing", "utilization",
    "supercharge", "supercharges", "supercharged", "supercharging",
    "empower", "empowers", "empowered", "empowering",
    "methodology", "methodologies",
    "streamline", "streamlines", "streamlined", "streamlining",
]

# From AIisms.yml and HedgeWords.yml. Warnings only.
AIISMS = [
    "at the end of the day", "when all is said and done", "in today's world",
    "in this day and age", "the fact of the matter is", "needless to say",
    "suffice it to say", "last but not least", "first and foremost",
    "at the core of", "ever-evolving", "ever-changing", "cutting-edge",
    "state-of-the-art", "best-in-class", "world-class", "robust",
    "comprehensive", "holistic", "synergies", "synergy", "paradigm",
    "ecosystem", "disruptive", "revolutionary", "groundbreaking",
    "innovative", "dynamic", "vibrant", "journey", "transformative",
    "transformational", "game-changer", "game changer", "move the needle",
    "ladder up", "north star",
]

HEDGE_WORDS = [
    "kind of", "sort of", "tends to", "tend to", "i think maybe", "perhaps",
    "arguably", "essentially", "basically", "literally",
]


def scan_em_dash(text):
    """Return a list of (line_no, snippet) for every em-dash or en-dash found."""
    hits = []
    for i, line in enumerate(text.splitlines(), start=1):
        if EM_DASH in line or EN_DASH in line:
            hits.append((i, line.strip()))
    return hits


def scan_double_hyphen_as_dash(text):
    """
    Catch ' -- ' used as a stand-in dash. A literal double hyphen surrounded by
    spaces is almost always a smuggled em-dash. Code-fence content is left alone.
    """
    hits = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.search(r"\s--\s", line):
            hits.append((i, line.strip()))
    return hits


def _word_boundary_matches(text, phrases):
    """Return the phrases (lowercased) that appear as whole-word matches."""
    low = text.lower()
    found = []
    for p in phrases:
        # \b works for word-char boundaries. Phrases with hyphens or spaces
        # still anchor on the outer word chars.
        pattern = r"\b" + re.escape(p.lower()) + r"\b"
        if re.search(pattern, low):
            found.append(p)
    return found


def scan_banned_words(text):
    """Return the list of banned words present (error level)."""
    return _word_boundary_matches(text, BANNED_WORDS)


def scan_aiisms(text):
    """Return the list of AI-isms present (warning level)."""
    return _word_boundary_matches(text, AIISMS)


def scan_hedge_words(text):
    """Return the list of hedge words present (warning level)."""
    return _word_boundary_matches(text, HEDGE_WORDS)
