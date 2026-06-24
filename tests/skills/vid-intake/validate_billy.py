import sys, os, re, json

sys.path.insert(0, r'c:/Users/billr/projects/authentic-ai-os/tests/lib')

import vale_rules
from frontmatter import split_frontmatter, has_fields

OUT = r'c:/Users/billr/projects/authentic-ai-os/tests/skills/vid-intake/outputs/billy_00'
BANKS = r'c:/Users/billr/projects/authentic-ai-os/tests/fixtures/billy/banks'
SEED = r'c:/Users/billr/projects/authentic-ai-os/tests/corpus/billy-seed.json'

failures = []

brain = open(os.path.join(OUT, 'brain-dump.md'), encoding='utf-8').read()
piece = open(os.path.join(OUT, 'piece.md'), encoding='utf-8').read()
files = {'brain-dump.md': brain, 'piece.md': piece}

# 1) em-dash / en-dash and double-hyphen-as-dash
for fname, text in files.items():
    for ln, snip in vale_rules.scan_em_dash(text):
        failures.append(f"{fname}:{ln} em/en-dash: {snip}")
    for ln, snip in vale_rules.scan_double_hyphen_as_dash(text):
        failures.append(f"{fname}:{ln} double-hyphen-as-dash: {snip}")

# 2) frontmatter completeness
bd_fm, _ = split_frontmatter(brain)
bd_required = ["type", "slug", "intake_mode", "captured", "iceberg_aligned"]
ok, missing = has_fields(bd_fm, bd_required)
if not ok:
    failures.append(f"brain-dump frontmatter missing/empty: {missing}")

pc_fm, _ = split_frontmatter(piece)
pc_required = ["type", "slug", "pillar", "status", "captured"]
ok2, missing2 = has_fields(pc_fm, pc_required)
if not ok2:
    failures.append(f"piece frontmatter missing/empty: {missing2}")

# 3) bank-link resolution inside Material section
# extract Material section text
mlow = brain
mstart = re.search(r'^##\s+Material', brain, re.MULTILINE | re.IGNORECASE)
material = ""
if mstart:
    rest = brain[mstart.end():]
    nexth = re.search(r'^##\s+', rest, re.MULTILINE)
    material = rest[:nexth.start()] if nexth else rest
WIKILINK = re.compile(r'\[\[([^\]]+)\]\]')
bank_links_checked = []
for raw in WIKILINK.findall(material):
    target = raw.split('|', 1)[0].split('#', 1)[0].strip()
    low = target.lower()
    if low.startswith('people/'):
        continue  # people links allowed, need not exist as bank files
    # treat as a bank citation: resolve under fixtures/billy/banks
    bank_links_checked.append(target)
    # try direct path and search across subfolders
    candidate_direct = os.path.join(BANKS, target + '.md')
    # also if it has bank/ or banks/ prefix strip it
    stripped = re.sub(r'^banks?/', '', target)
    candidate_stripped = os.path.join(BANKS, stripped + '.md')
    found = os.path.exists(candidate_direct) or os.path.exists(candidate_stripped)
    if not found and os.path.isdir(BANKS):
        for root, _, fs in os.walk(BANKS):
            if os.path.basename(stripped) + '.md' in fs:
                found = True
                break
    if not found:
        failures.append(f"Material bank link does not resolve to a file under banks/: [[{target}]]")

# 4) fabrication traps
seed = json.load(open(SEED, encoding='utf-8'))[0]
allwords = brain + "\n" + piece
# build the legitimate source text: seed + reveals + withholds
src = seed.get('seed', '')
persona = seed.get('persona', {})
src += "\n" + "\n".join(persona.get('reveals', []))
src += "\n" + "\n".join(persona.get('withholds', []))

# 4a) trap strings must NOT appear as asserted fact (only if flagged unverified/TODO)
def appears_flagged(text, trap):
    # find lines containing trap; check each has an unverified/TODO/verify flag nearby
    hits = []
    for ln in text.splitlines():
        if trap.lower() in ln.lower():
            hits.append(ln)
    return hits

for trap in seed.get('fabrication_traps', ['Milli Vanilli', '85%']):
    hits = appears_flagged(allwords, trap)
    for h in hits:
        flagged = re.search(r'unverified|TODO|verify|not\s+confirm|do not state|flag', h, re.IGNORECASE)
        if not flagged:
            failures.append(f"fabrication trap '{trap}' asserted as fact (unflagged): {h.strip()}")

# 4b) any claim-shaped number stated as fact must trace to the seed source
from check_fabrication import find_fabricated_numbers, strip_frontmatter_body
bd_body = strip_frontmatter_body(brain)
pc_body = strip_frontmatter_body(piece)
fab_nums = find_fabricated_numbers(bd_body + "\n" + pc_body, src)
if fab_nums:
    failures.append(f"claim-shaped numbers not traceable to seed source: {fab_nums}")

print("BANK_LINKS_IN_MATERIAL:", bank_links_checked)
print("TRAP_HITS_85:", appears_flagged(allwords, '85%'))
print("TRAP_HITS_MILLI:", appears_flagged(allwords, 'Milli Vanilli'))
print("FAB_NUMS:", fab_nums)
print("BRAIN_FM_OK:", ok, "PIECE_FM_OK:", ok2)
print("FAILURES_COUNT:", len(failures))
for f in failures:
    print("FAILURE:", f)
print("RESULT_PASSED:", len(failures) == 0)
