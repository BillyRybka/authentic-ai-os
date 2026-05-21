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
# The only skills that ship. A WIP skill graduates by being added to this list
# (and nowhere else). Nothing not named here can reach `main`.
$ShipSkills = @(
    'creator-setup',
    'vid-foundation',
    'vid-avatar',
    'vid-positioning',
    'vid-pillars',
    'vid-credibility',
    'vid-backstory'
)
# Always-ship paths (non-skill, non-knowledge). knowledge/ is auto-detected.
$AlwaysShip = @('.claude-plugin', 'CLAUDE.md', 'banks', '.gitignore')

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
    $knowledgeRefs = @{}
    foreach ($f in (Get-ChildItem '.claude/skills' -Recurse -Filter '*.md' -File)) {
        foreach ($r in (Select-String -Path $f.FullName -Pattern 'knowledge/([A-Za-z0-9_/-]+\.md)' -AllMatches)) {
            foreach ($m in $r.Matches) { $knowledgeRefs[$m.Groups[1].Value] = $true }
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
    git add -A
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
