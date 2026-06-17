"""
Minimal YAML-frontmatter reader. No external dependency (pyyaml not assumed).

Handles the flat frontmatter the vid-* skills produce: scalar keys, quoted
strings, and inline lists like `stories_used: ["[[a]]", "[[b]]"]`. Nested
blocks are ignored (Tier A only checks flat field presence). If pyyaml is
installed it is used for robustness, otherwise the built-in parser runs.
"""

import re

try:
    import yaml  # type: ignore
    _HAS_YAML = True
except Exception:
    _HAS_YAML = False


_FM_RE = re.compile(r"^\s*---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def split_frontmatter(text):
    """
    Return (frontmatter_dict, body_text).
    frontmatter_dict is {} when the text has no frontmatter block.
    """
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)

    if _HAS_YAML:
        try:
            data = yaml.safe_load(raw)
            if isinstance(data, dict):
                return data, body
        except Exception:
            pass  # fall through to the minimal parser

    fm = {}
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        # only treat top-level (non-indented) keys as fields
        if line[:1] in (" ", "\t"):
            continue
        mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not mm:
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if (val.startswith('"') and val.endswith('"')) or (
            val.startswith("'") and val.endswith("'")
        ):
            val = val[1:-1]
        fm[key] = val
    return fm, body


def has_fields(frontmatter, required):
    """
    Return (ok, missing). A field counts as present when the key exists and its
    value is not empty / not the literal 'null'. Lists count as present when the
    key exists even if the list is empty (e.g. fresh stories_used: []).
    """
    missing = []
    for field in required:
        if field not in frontmatter:
            missing.append(field)
            continue
        val = frontmatter[field]
        if val is None:
            missing.append(field)
            continue
        if isinstance(val, str) and val.strip().lower() in ("", "null"):
            missing.append(field)
    return (len(missing) == 0, missing)
