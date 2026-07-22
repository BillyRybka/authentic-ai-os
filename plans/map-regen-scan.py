"""Scan all three skill roots for knowledge/ and references/ dependencies.

Derives each skill's dependency list by grepping its SKILL.md, references/,
assets/, and manifest.md for knowledge/ paths, references/ paths, and
format-planners mentions. Cross-checks every referenced path against disk.
Stdlib only.
"""

import os
import re
from pathlib import Path

ROOT = Path(r"C:\Users\billr\projects\authentic-ai-content-engine")

SKILL_ROOTS = {
    "RELEASED": ROOT / "plugins" / "authentic-ai-os" / "skills",
    "STAGED": ROOT / ".claude" / "skills",
    "WIP": ROOT / ".claude" / "skills-wip",
}

KNOWLEDGE = ROOT / "knowledge"

KNOW_RE = re.compile(r"knowledge/([A-Za-z0-9/_.{}-]+\.(?:md|txt))")
REF_RE = re.compile(r"references/([A-Za-z0-9/_.{}-]+\.(?:md|txt))")
ASSET_RE = re.compile(r"assets/([A-Za-z0-9/_.{}-]+\.(?:md|txt))")
BANK_RE = re.compile(r"banks/([A-Za-z0-9/_.{}-]+\.(?:md|txt))")
BRAND_RE = re.compile(r"brand\.md")


def scan_file(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return "", [], [], [], []
    kn = set(KNOW_RE.findall(text))
    rf = set(REF_RE.findall(text))
    an = set(ASSET_RE.findall(text))
    bk = set(BANK_RE.findall(text))
    return text, kn, rf, an, bk


def main():
    skills = {}  # name -> {tier, knowledge, refs, assets, banks, files_scanned, brand}
    for tier, root in SKILL_ROOTS.items():
        if not root.is_dir():
            continue
        for entry in sorted(root.iterdir()):
            if not entry.is_dir():
                continue
            name = entry.name
            kn_all, rf_all, an_all, bk_all = set(), set(), set(), set()
            scanned = []
            brand = False
            candidates = [entry / "SKILL.md", entry / "manifest.md"]
            for sub in ("references", "assets"):
                subdir = entry / sub
                if subdir.is_dir():
                    candidates.extend(sorted(subdir.rglob("*.md")))
                    candidates.extend(sorted(subdir.rglob("*.txt")))
            for cand in candidates:
                if not cand.is_file():
                    continue
                scanned.append(str(cand.relative_to(ROOT)))
                text, kn, rf, an, bk = scan_file(cand)
                kn_all |= kn
                rf_all |= rf
                an_all |= an
                bk_all |= bk
                if BRAND_RE.search(text):
                    brand = True
            # drop the X.md placeholder
            kn_all.discard("X.md")
            skills[name] = {
                "tier": tier,
                "knowledge": sorted(kn_all),
                "refs": sorted(rf_all),
                "assets": sorted(an_all),
                "banks": sorted(bk_all),
                "scanned": scanned,
                "brand": brand,
            }

    print("=" * 70)
    print("PER-SKILL DEPENDENCIES (derived from disk)")
    print("=" * 70)
    for name, data in skills.items():
        print(f"\n### {name} [{data['tier']}]")
        print(f"  scanned: {', '.join(data['scanned'])}")
        if data["brand"]:
            print("  !! brand.md reference found")
        for k in data["knowledge"]:
            exists = (KNOWLEDGE / k).is_file()
            print(f"  K: {k}{'' if exists else '  !! MISSING ON DISK'}")
        for r in data["refs"]:
            exists = (SKILL_ROOTS[data["tier"]] / name / "references" / r).is_file()
            print(f"  R: references/{r}{'' if exists else '  !! MISSING ON DISK'}")
        for a in data["assets"]:
            exists = (SKILL_ROOTS[data["tier"]] / name / "assets" / a).is_file()
            print(f"  A: assets/{a}{'' if exists else '  !! MISSING ON DISK'}")
        for b in data["banks"]:
            print(f"  B: banks/{b}")

    # reverse map
    print("\n" + "=" * 70)
    print("REVERSE MAP: knowledge file -> consumers")
    print("=" * 70)
    consumers = {}
    for name, data in skills.items():
        for k in data["knowledge"]:
            consumers.setdefault(k, []).append(name)
    disk_files = sorted(
        str(p.relative_to(KNOWLEDGE)) for p in KNOWLEDGE.rglob("*") if p.is_file()
    )
    for f in disk_files:
        f_fwd = f.replace(os.sep, "/")
        who = sorted(consumers.get(f_fwd, []))
        print(f"  {f_fwd}: {', '.join(who) if who else 'NO CONSUMER'}")

    # referenced but not on disk
    print("\n" + "=" * 70)
    print("REFERENCED knowledge paths NOT on disk:")
    print("=" * 70)
    disk_set = {f.replace(os.sep, "/") for f in disk_files}
    for k, who in sorted(consumers.items()):
        if k not in disk_set and "{format}" not in k:
            print(f"  {k}  <- referenced by {', '.join(sorted(who))}")

    # brand.md anywhere
    print("\n" + "=" * 70)
    print("brand.md references:")
    print("=" * 70)
    any_brand = False
    for name, data in skills.items():
        if data["brand"]:
            print(f"  {name}")
            any_brand = True
    if not any_brand:
        print("  none in any skill file")


if __name__ == "__main__":
    main()
