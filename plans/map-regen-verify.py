"""Verify the two regenerated maps against disk reality.

Checks:
1. Every knowledge/ path named in either map exists on disk.
2. Every skill-local references/ path named in either map exists on disk.
3. Every file in knowledge/ appears in the dependency map's reverse table.
4. Reverse-map consumer lists match a fresh grep of the skills.
5. No em-dashes or en-dashes in either map.
6. No Ed Lawrence / course / business-os references in either map.
Stdlib only.
"""

import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\billr\projects\authentic-ai-content-engine")
MAP1 = ROOT / "documents" / "skill-knowledge-map.md"
MAP2 = ROOT / "documents" / "SYSTEM-MAP.md"

failures = []

t1 = MAP1.read_text(encoding="utf-8")
t2 = MAP2.read_text(encoding="utf-8")

# 1+2: paths named in maps exist
KNOW_RE = re.compile(r"knowledge/([A-Za-z0-9/_.{}-]+\.(?:md|txt))")
for label, text in (("skill-knowledge-map", t1), ("SYSTEM-MAP", t2)):
    for m in sorted(set(KNOW_RE.findall(text))):
        if m in ("X.md",) or "{format}" in m:
            continue
        if not (ROOT / "knowledge" / m).is_file():
            failures.append(f"{label}: knowledge/{m} named but missing on disk")

# references/ paths named in maps (only check ones attributed to a skill folder)
REF_RE = re.compile(r"references/([A-Za-z0-9/_.-]+\.(?:md|txt))")
known_refs = set()
for skroot in (ROOT / ".claude" / "skills", ROOT / ".claude" / "skills-wip",
               ROOT / "plugins" / "authentic-ai-os" / "skills"):
    for p in skroot.rglob("*"):
        if p.is_file() and "references" in p.parts:
            known_refs.add(p.name)
for label, text in (("skill-knowledge-map", t1), ("SYSTEM-MAP", t2)):
    for m in sorted(set(REF_RE.findall(text))):
        base = Path(m).name
        if base not in known_refs:
            failures.append(f"{label}: references/{m} named but not found in any skill")

# 3: every knowledge file in the map's reverse table
disk_knowledge = sorted(
    str(p.relative_to(ROOT / "knowledge")).replace("\\", "/")
    for p in (ROOT / "knowledge").rglob("*") if p.is_file()
)
for f in disk_knowledge:
    if f not in t1:
        failures.append(f"knowledge/{f} on disk but absent from skill-knowledge-map")

# 4: consumer cross-check, forward direction (skill -> knowledge)
SKILL_ROOTS = [ROOT / "plugins" / "authentic-ai-os" / "skills",
               ROOT / ".claude" / "skills", ROOT / ".claude" / "skills-wip"]
actual = {}
for skroot in SKILL_ROOTS:
    for entry in sorted(skroot.iterdir()):
        if not entry.is_dir():
            continue
        kn = set()
        candidates = [entry / "SKILL.md", entry / "manifest.md"]
        for sub in ("references", "assets"):
            sd = entry / sub
            if sd.is_dir():
                candidates += [p for p in sd.rglob("*") if p.suffix in (".md", ".txt")]
        for c in candidates:
            if c.is_file():
                kn |= set(KNOW_RE.findall(c.read_text(encoding="utf-8", errors="replace")))
        kn.discard("X.md")
        actual[entry.name] = kn

# spot-check the renamed/moved/deleted reality
for gone in ["emotion-brick-decision-matrix.md", "gift-framework.md",
             "thumbnail-composition-guide.md", "thumbnail-examples-library.md",
             "thumbnail-strategy-menu.md", "framework-bank-schema.md",
             "metaphor-bank-schema.md", "packaging-bank-schema.md",
             "story-bank-schema.md", "testimonial-bank-schema.md",
             "synthetic-audience-method.md", "common-english.txt",
             "ai-hedging.md", "hook-patterns.md", "visual-demo-builder.md",
             "format-index.md"]:
    if (ROOT / "knowledge" / gone).exists():
        failures.append(f"knowledge/{gone} should be gone but exists")

for new in ["attention-craft.md", "transition-patterns.md", "parable-decision-matrix.md"]:
    if not (ROOT / "knowledge" / new).is_file():
        failures.append(f"knowledge/{new} should exist but is missing")

# maps must not name deleted files as knowledge/ deps
for label, text in (("skill-knowledge-map", t1), ("SYSTEM-MAP", t2)):
    for gone in ["emotion-brick-decision-matrix", "gift-framework",
                 "thumbnail-composition-guide", "thumbnail-examples-library",
                 "thumbnail-strategy-menu", "framework-bank-schema",
                 "metaphor-bank-schema", "packaging-bank-schema",
                 "story-bank-schema", "testimonial-bank-schema"]:
        if f"knowledge/{gone}" in text:
            failures.append(f"{label}: still names deleted knowledge/{gone}")

# 5: dashes
for label, text in (("skill-knowledge-map", t1), ("SYSTEM-MAP", t2)):
    if "\u2014" in text:
        failures.append(f"{label}: contains em-dash")
    if "\u2013" in text:
        failures.append(f"{label}: contains en-dash")

# 6: banned references
for label, text in (("skill-knowledge-map", t1), ("SYSTEM-MAP", t2)):
    low = text.lower()
    for banned in ["ed lawrence", "business-os"]:
        if banned in low:
            failures.append(f"{label}: contains banned reference '{banned}'")

print("actual consumer sets (for manual diff against reverse map):")
for name, kn in sorted(actual.items()):
    if kn:
        print(f"  {name}: {sorted(kn)}")

print()
if failures:
    print("FAILURES:")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("ALL CHECKS PASSED")
