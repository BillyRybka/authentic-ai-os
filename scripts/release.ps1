#!/usr/bin/env pwsh
# release.ps1 - Build the lean `main` (storefront) branch from `dev` (workshop).
#
# `main` is an ALLOWLIST. Only the paths named below ever reach it. WIP skills,
# unused knowledge, and internal docs that live on `dev` can never leak to a
# client, because the script rebuilds `main` from scratch and copies only the
# allowlisted paths.
#
# Usage:   pwsh scripts/release.ps1 -Version 0.2.0
#
# Run from `dev` with a clean working tree. The script switches to `main`,
# rebuilds it, commits, and returns you to `dev`. It does NOT push - it prints
# the push command so you review the result first.

param(
    [Parameter(Mandatory = $true)]
    [string]$Version
)

$ErrorActionPreference = 'Stop'

# --- THE ALLOWLIST -----------------------------------------------------------
# The skill list is read from documents/skill-knowledge-map.md (single source
# of truth). Any skill tagged `SHIPPED` in that map ships; anything tagged
# `WIP` does not. The `release` skill marks the tag when a WIP graduates.
function Get-ShippedSkills {
    $mapPath = 'documents/skill-knowledge-map.md'
    if (-not (Test-Path $mapPath)) {
        throw "Missing $mapPath. The map is the source of truth for what ships."
    }
    $map = Get-Content $mapPath -Raw
    $found = [regex]::Matches($map, '(?m)^\*\*([a-z][a-z0-9-]+)\*\*\s+`SHIPPED`')
    $skills = @($found | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique)
    if (-not $skills) { throw "No SHIPPED skills found in $mapPath." }
    return $skills
}
$ShipSkills = Get-ShippedSkills

# Always-ship paths (non-skill, non-knowledge). knowledge/ is auto-detected.
# Bank schemas live in knowledge/{bank}-schema.md and ship via knowledge/ auto-detection.
# CLAUDE.md ships as plugin documentation. It describes shipped reality only (the
# folder structure creator-setup actually scaffolds and the routing for shipped skills).
# Clients also get a workspace-scoped CLAUDE.md from creator-setup's assets/CLAUDE.md.
$AlwaysShip = @('.claude-plugin', 'CLAUDE.md', '.gitignore')

# --- preconditions -----------------------------------------------------------
$repoRoot = (git rev-parse --show-toplevel).Trim()
Set-Location $repoRoot

$branch = (git branch --show-current).Trim()
if ($branch -ne 'dev') { throw "Run this from 'dev' (currently on '$branch')." }
if ((git status --porcelain | Out-String).Trim()) {
    throw "Working tree is dirty. Commit or stash on 'dev' first."
}

Write-Host "Releasing v$Version : rebuilding 'main' from 'dev'..." -ForegroundColor Cyan

try {
    # --- switch to main and clear it to a blank slate ------------------------
    git checkout main
    git rm -r --quiet --ignore-unmatch . | Out-Null

    # --- restore always-ship paths -------------------------------------------
    foreach ($p in $AlwaysShip) { git checkout dev -- $p }

    # --- restore the allowlisted skills --------------------------------------
    foreach ($s in $ShipSkills) { git checkout dev -- ".claude/skills/$s" }

    # --- auto-detect the knowledge those skills reference, restore only that -
    # Scan ONLY the allowlisted skill folders, never the whole .claude/skills/
    # tree (which on dev also holds parked non-shipping skills like vid-research).
    $knowledgeRefs = @{}
    foreach ($s in $ShipSkills) {
        foreach ($f in (Get-ChildItem ".claude/skills/$s" -Recurse -Filter '*.md' -File -ErrorAction SilentlyContinue)) {
            foreach ($r in (Select-String -Path $f.FullName -Pattern 'knowledge/([A-Za-z0-9_/-]+\.md)' -AllMatches)) {
                foreach ($m in $r.Matches) { $knowledgeRefs[$m.Groups[1].Value] = $true }
            }
        }
    }
    $restored = @(); $skipped = @()
    foreach ($k in ($knowledgeRefs.Keys | Sort-Object)) {
        git cat-file -e "dev:knowledge/$k" 2>$null
        if ($LASTEXITCODE -eq 0) { git checkout dev -- "knowledge/$k"; $restored += $k }
        else { $skipped += $k }   # e.g. the literal `knowledge/X.md` placeholder
    }

    # --- bump the version in both manifests ----------------------------------
    foreach ($mf in @('.claude-plugin/plugin.json', '.claude-plugin/marketplace.json')) {
        $raw = Get-Content $mf -Raw
        $raw = $raw -replace '("version"\s*:\s*")[^"]*"', ('${1}' + $Version + '"')
        Set-Content -Path $mf -Value $raw -NoNewline
    }

    # --- commit --------------------------------------------------------------
    # Stage ONLY the allowlist. Never `git add -A` here: a background process
    # (Obsidian, an editor) can drop an untracked file into the tree mid-run,
    # and -A would sweep it onto main. The `git rm` above already staged every
    # deletion; `git checkout dev -- <path>` already staged every restore; only
    # the two version-bumped manifests still need re-staging. Untracked files
    # left in the working tree never enter the index, so the commit stays clean.
    git add .claude-plugin/plugin.json .claude-plugin/marketplace.json
    git commit -m "Release v$Version"
    $ok = $true
}
finally {
    # Always return to the workshop. -f discards a half-built main on failure;
    # main's HEAD is untouched until the commit above succeeds.
    git checkout -f dev | Out-Null
}

if ($ok) {
    Write-Host ""
    Write-Host "main rebuilt for v$Version." -ForegroundColor Green
    Write-Host "  Skills:    $($ShipSkills -join ', ')"
    Write-Host "  Knowledge: $($restored -join ', ')"
    if ($skipped.Count) {
        Write-Host "  Skipped (not real files): $($skipped -join ', ')" -ForegroundColor DarkGray
    }
    Write-Host ""
    Write-Host "Review with:  git checkout main; git ls-files; git checkout dev" -ForegroundColor Yellow
    Write-Host "Publish with: git push origin main" -ForegroundColor Yellow
}
