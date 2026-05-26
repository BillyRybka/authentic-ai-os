#!/usr/bin/env pwsh
# release.ps1 - Build the lean `main` (storefront) branch from `dev` (workshop).
#
# `main` is an ALLOWLIST. Only the paths named below ever reach it. WIP skills,
# internal docs, and Billy's dev tooling that live on `dev` can never leak to a
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
# Whole plugin tree ships as a unit. WIP skills at .claude/skills-wip/ stay off
# main automatically because they live outside the plugin folder. Documents,
# scripts, plans, and Billy's personal vault stay on dev only.
$AlwaysShip = @(
    '.claude-plugin',
    'plugins/authentic-ai-os',
    'CLAUDE.md',
    '.gitignore'
)

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

    # --- restore always-ship paths from dev ----------------------------------
    foreach ($p in $AlwaysShip) { git checkout dev -- $p }

    # --- auto-detect knowledge files referenced by shipped skills, relocate --
    # Skills reference knowledge via paths like `knowledge/X.md`. On the source
    # repo (dev) those live at repo root. In the installed plugin they must
    # resolve under ${CLAUDE_PLUGIN_ROOT}/knowledge/, so on main they relocate
    # to plugins/authentic-ai-os/knowledge/.
    $skillsDir = 'plugins/authentic-ai-os/skills'
    $commandsDir = 'plugins/authentic-ai-os/commands'
    $knowledgeRefs = @{}

    foreach ($dir in @($skillsDir, $commandsDir)) {
        if (-not (Test-Path $dir)) { continue }
        foreach ($f in (Get-ChildItem $dir -Recurse -Filter '*.md' -File -ErrorAction SilentlyContinue)) {
            foreach ($r in (Select-String -Path $f.FullName -Pattern 'knowledge/([A-Za-z0-9_/-]+\.md)' -AllMatches)) {
                foreach ($m in $r.Matches) { $knowledgeRefs[$m.Groups[1].Value] = $true }
            }
        }
    }

    $restored = @(); $skipped = @()
    foreach ($k in ($knowledgeRefs.Keys | Sort-Object)) {
        git cat-file -e "dev:knowledge/$k" 2>$null
        if ($LASTEXITCODE -eq 0) {
            git checkout dev -- "knowledge/$k"
            $dest = "plugins/authentic-ai-os/knowledge/$k"
            $destDir = Split-Path -Parent $dest
            New-Item -ItemType Directory -Force -Path $destDir | Out-Null
            git mv "knowledge/$k" $dest | Out-Null
            $restored += $k
        } else {
            $skipped += $k   # e.g. literal `knowledge/X.md` placeholder strings
        }
    }

    # Drop empty top-level knowledge/ folder if all files relocated
    if (Test-Path 'knowledge') {
        if (-not (Get-ChildItem 'knowledge' -Recurse -File -ErrorAction SilentlyContinue)) {
            Remove-Item 'knowledge' -Recurse -Force
        }
    }

    # --- bump version in plugin.json only ------------------------------------
    # marketplace.json has no version field (plugin.json is source of truth per docs)
    $mf = 'plugins/authentic-ai-os/.claude-plugin/plugin.json'
    $raw = Get-Content $mf -Raw
    $raw = $raw -replace '("version"\s*:\s*")[^"]*"', ('${1}' + $Version + '"')
    Set-Content -Path $mf -Value $raw -NoNewline

    # --- commit --------------------------------------------------------------
    # Re-stage the version-bumped manifest. Other paths already staged by
    # git rm + git checkout + git mv above. Untracked files in the working
    # tree never enter the index so the commit stays clean.
    git add $mf
    git commit -m "Release v$Version"
    git tag "v$Version"

    # --- generate .plugin artifact (zip of plugin folder, renamed) -----------
    # Cowork's auto-update is unreliable. The .plugin file is a manual override:
    # creators drag-drop it into Cowork chat to force-install this exact version.
    $pluginFile = "dist/authentic-ai-os-v$Version.plugin"
    $zipFile = "dist/authentic-ai-os-v$Version.zip"
    New-Item -ItemType Directory -Force -Path 'dist' | Out-Null
    if (Test-Path $pluginFile) { Remove-Item $pluginFile -Force }
    if (Test-Path $zipFile) { Remove-Item $zipFile -Force }
    Compress-Archive -Path 'plugins/authentic-ai-os/*' -DestinationPath $zipFile
    Move-Item $zipFile $pluginFile
    $ok = $true
}
finally {
    # Always return to the workshop. -f discards a half-built main on failure.
    git checkout -f dev | Out-Null
}

if ($ok) {
    # --- sync dev's plugin.json to the released version ----------------------
    # Dev should never lag behind main. After release, bring dev's manifest
    # forward so future work iterates from the released version, not behind it.
    $devManifest = 'plugins/authentic-ai-os/.claude-plugin/plugin.json'
    $raw = Get-Content $devManifest -Raw
    $raw = $raw -replace '("version"\s*:\s*")[^"]*"', ('${1}' + $Version + '"')
    Set-Content -Path $devManifest -Value $raw -NoNewline
    if ((git status --porcelain $devManifest | Out-String).Trim()) {
        git add $devManifest
        git commit -m "Sync dev to v$Version" | Out-Null
    }

    # --- push everything -----------------------------------------------------
    Write-Host ""
    Write-Host "Pushing main, tag, and dev..." -ForegroundColor Cyan
    git push origin main --follow-tags
    git push origin dev

    # --- create GitHub Release and upload .plugin artifact -------------------
    $pluginFile = "dist/authentic-ai-os-v$Version.plugin"
    $releaseTitle = "v$Version"
    Write-Host "Creating GitHub Release v$Version with .plugin asset..." -ForegroundColor Cyan
    gh release create "v$Version" `
        --title $releaseTitle `
        --notes "Plugin release v$Version. See commit log for changes. Drag the attached .plugin file into Cowork chat to force-install this version if auto-update fails." `
        $pluginFile

    Write-Host ""
    Write-Host "Released v$Version." -ForegroundColor Green
    Write-Host "  Knowledge: $($restored -join ', ')"
    if ($skipped.Count) {
        Write-Host "  Skipped (not real files): $($skipped -join ', ')" -ForegroundColor DarkGray
    }
    Write-Host "  Artifact: $pluginFile (uploaded to GitHub Release)"
    Write-Host ""
    Write-Host "GitHub Release: https://github.com/BillyRybka/authentic-ai-os/releases/tag/v$Version" -ForegroundColor Yellow
}
