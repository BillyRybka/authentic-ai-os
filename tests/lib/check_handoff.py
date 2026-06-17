"""
Handoff-contract check. Proves the chain composes.

Each skill's output must carry the exact fields the NEXT skill reads as input
(its Prerequisites). This is the integration glue: a skill can produce lovely
prose and still break the pipeline by dropping a field the downstream skill
needs. The contract per boundary is declared in handoff_contracts below and
asserted against the produced frontmatter.

Keep this table in sync with each skill's SKILL.md "Prerequisites" section.
"""

from frontmatter import split_frontmatter, has_fields


# What the downstream skill needs to exist in the named upstream artifact.
# boundary -> {artifact filename: [required frontmatter fields]}
HANDOFF_CONTRACTS = {
    # vid-intake -> vid-framing
    "intake->framing": {
        "brain-dump.md": [
            "type", "slug", "mode", "captured",
            "problem_addressed", "iceberg_aligned", "aligned_with",
        ],
        "piece.md": ["type", "slug", "status", "captured"],
    },
    # vid-framing -> vid-structure (added when the rollout reaches framing)
    "framing->structure": {
        "piece.md": [
            "type", "slug", "selected_angle", "core_payoff",
            "format", "goal", "voice_context",
        ],
    },
}


def check_handoff(boundary, artifacts):
    """
    boundary  = key into HANDOFF_CONTRACTS, e.g. "intake->framing"
    artifacts = {filename: file_text}
    Returns (passed, detail_dict) where detail lists missing fields per file.
    """
    contract = HANDOFF_CONTRACTS.get(boundary)
    if contract is None:
        return False, {"error": f"no contract defined for boundary '{boundary}'"}

    detail = {}
    ok = True
    for filename, required in contract.items():
        text = artifacts.get(filename)
        if text is None:
            detail[filename] = {"present": False, "missing": required}
            ok = False
            continue
        fm, _ = split_frontmatter(text)
        field_ok, missing = has_fields(fm, required)
        detail[filename] = {"present": True, "missing": missing}
        if not field_ok:
            ok = False
    return ok, detail
