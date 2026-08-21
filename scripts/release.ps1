#!/usr/bin/env pwsh
# release.ps1 - Publish ONE plugin. Rebuilds the lean `main` (storefront) from `dev`.
#
# `main` is an ALLOWLIST rebuild: it is wiped and reconstructed from the paths named
# below, so the vault, Intelligence/, documents/, plans/, and WIP skills in
# .claude/skills/ can never leak to a client. They stay off by construction.
#
# CRITICAL: main always carries EVERY shipping plugin, not just the one being
# released. Releasing one plugin with a single-plugin allowlist would delete the
# others from main and break those installs. -Plugin selects which plugin's version
# is bumped, artifacted, and published. It never selects which plugins exist.
#
# The build and the safety checks are NOT in this script. They live in
# scripts/generate-plugins.mjs and scripts/qa-plugins.mjs, which run first and abort
# on any blocker. This script only publishes what they have already validated.
#
# Usage:
#   pwsh scripts/release.ps1 -Plugin authentic-ai-os -Version 0.3.3
#   pwsh scripts/release.ps1 -Plugin authentic-ai-os -Version 0.3.3 -DryRun

param(
    [Parameter(Mandatory = $true)][string]$Plugin,
    [Parameter(Mandatory = $true)][string]$Version,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$repoRoot = (git rev-parse --show-toplevel).Trim()
Set-Location $repoRoot

if ($Version -notmatch '^\d+\.\d+\.\d+$') { throw "Version must be semver, got '$Version'." }

# --- preconditions -----------------------------------------------------------
$branch = (git branch --show-current).Trim()
if ($branch -ne 'dev') { throw "Run this from 'dev' (currently on '$branch')." }
if ((git status --porcelain | Out-String).Trim()) {
    throw "Working tree is dirty. Commit or stash on 'dev' first."
}

$mapPath = '.claude-plugin/plugins-map.json'
$mpPath  = '.claude-plugin/marketplace.json'
$map = Get-Content $mapPath -Raw | ConvertFrom-Json

$pluginNames = $map.plugins.PSObject.Properties.Name
if ($pluginNames -notcontains $Plugin) {
    throw "Unknown plugin '$Plugin'. Defined plugins: $($pluginNames -join ', ')"
}

$mirror = $map.plugins.$Plugin.release.mirror
if (-not $mirror) { throw "Plugin '$Plugin' has no release.mirror in $mapPath." }

$tag = "$Plugin-v$Version"
# Prefixed per plugin. Two plugins on independent versions cannot share a v1.2.3 tag.
if ((git tag --list $tag | Out-String).Trim()) { throw "Tag $tag already exists." }

# --- bump the version, then rebuild so plugin.json carries it ----------------
# marketplace.json is the single source of truth for version. The generator writes
# it down into each plugin.json, so there is exactly one place to edit.
Write-Host "Bumping $Plugin to $Version..." -ForegroundColor Cyan
$mpRaw = Get-Content $mpPath -Raw
# (?!"name") stops the match from running past this plugin's object into the next
# one's version field, which is what would happen if this plugin had no version.
$pattern = '("name"\s*:\s*"' + [regex]::Escape($Plugin) + '"(?:(?!"name")[\s\S])*?"version"\s*:\s*")[^"]*(")'
if ($mpRaw -notmatch $pattern) { throw "Could not find a version field for '$Plugin' in $mpPath." }
$mpRaw = [regex]::Replace($mpRaw, $pattern, "`${1}$Version`${2}", 1)
Set-Content -Path $mpPath -Value $mpRaw -NoNewline

# --- build and validate ------------------------------------------------------
Write-Host "Regenerating plugins/ ..." -ForegroundColor Cyan
node scripts/generate-plugins.mjs
if ($LASTEXITCODE -ne 0) { git checkout -- $mpPath; throw "Generation failed. Nothing changed." }

Write-Host "Running the QA gate..." -ForegroundColor Cyan
node scripts/qa-plugins.mjs --ref dev
if ($LASTEXITCODE -ne 0) {
    git checkout -- $mpPath
    node scripts/generate-plugins.mjs | Out-Null
    throw "QA gate found blockers. Nothing released, version bump reverted."
}

# --- commit the bump on dev --------------------------------------------------
git add $mpPath plugins
git commit -m "Release $Plugin v$Version"

$ok = $false
try {
    # --- rebuild main from the allowlist -------------------------------------
    # Every plugin folder ships, always. Only the selected one changed version.
    $alwaysShip = @('.claude-plugin', 'CLAUDE.md', '.gitignore', '.gitattributes')
    foreach ($p in $pluginNames) { $alwaysShip += "plugins/$p" }

    git checkout main
    git rm -r --quiet --ignore-unmatch . | Out-Null
    foreach ($p in $alwaysShip) { git checkout dev -- $p }

    git commit -m "Release $Plugin v$Version"
    # Annotated (-a). Lightweight tags are skipped by `git push --follow-tags`,
    # which then makes `gh release create` fail because the tag never reached origin.
    git tag -a $tag -m $tag

    # --- artifact ------------------------------------------------------------
    # Cowork's auto-update is unreliable. The .plugin file is the manual override:
    # drag-drop it into Cowork chat to force-install this exact version.
    $pluginFile = "dist/$Plugin-v$Version.plugin"
    $zipFile    = "dist/$Plugin-v$Version.zip"
    New-Item -ItemType Directory -Force -Path 'dist' | Out-Null
    Remove-Item $pluginFile, $zipFile -Force -ErrorAction SilentlyContinue
    Compress-Archive -Path "plugins/$Plugin/*" -DestinationPath $zipFile
    Move-Item $zipFile $pluginFile
    $ok = $true
}
finally {
    # Always return to the workshop. -f discards a half-built main on failure.
    git checkout -f dev | Out-Null
}

if (-not $ok) { throw "Release failed while rebuilding main. 'main' was not pushed." }

$pluginFile = "dist/$Plugin-v$Version.plugin"

if ($DryRun) {
    Write-Host ""
    Write-Host "DRY RUN. Built locally. Nothing pushed or published." -ForegroundColor Yellow
    Write-Host "  main commit: $(git rev-parse main)"
    Write-Host "  tag:         $tag (LOCAL ONLY)"
    Write-Host "  artifact:    $pluginFile"
    Write-Host ""
    Write-Host "Inspect:   git log main -1; ls dist/" -ForegroundColor DarkGray
    Write-Host "Roll back: git tag -d $tag; git checkout main; git reset --hard origin/main; git checkout dev; git reset --hard origin/dev" -ForegroundColor DarkGray
    exit 0
}

# --- publish -----------------------------------------------------------------
Write-Host ""
Write-Host "Pushing main, tag, and dev..." -ForegroundColor Cyan
git push origin main --follow-tags
if ($LASTEXITCODE -ne 0) { throw "git push origin main failed." }
git push origin dev
if ($LASTEXITCODE -ne 0) { throw "git push origin dev failed." }

# Internal release record on the private source repo. Clients never see this.
Write-Host "Creating private-repo Release $tag..." -ForegroundColor Cyan
gh release create $tag --title $tag --notes "$Plugin v$Version. See the commit log for changes." $pluginFile
if ($LASTEXITCODE -ne 0) { throw "gh release create failed on the private repo. Re-run: gh release create $tag --title $tag --notes '...' $pluginFile" }

# Public mirror. This is what the client update check reads, and it is per plugin
# on purpose: releases/latest is per repo and does not know which plugin an asset
# belongs to, so a shared mirror serves the wrong file to the wrong clients.
# The mirror keeps the bare v<version> tag so the existing update-check keeps working.
Write-Host "Mirroring to $mirror ..." -ForegroundColor Cyan
gh release create "v$Version" --repo $mirror --title "v$Version" `
    --notes "$Plugin v$Version. Download the .plugin file and drag it into Cowork chat to install. The built-in update checker will notify you of future releases." `
    $pluginFile
if ($LASTEXITCODE -ne 0) { throw "gh release create failed on the public mirror $mirror. Re-run manually." }

Write-Host ""
Write-Host "Released $Plugin v$Version." -ForegroundColor Green
Write-Host "  Artifact: $pluginFile"
Write-Host "  Private:  https://github.com/BillyRybka/authentic-ai-os/releases/tag/$tag" -ForegroundColor DarkGray
Write-Host "  Public:   https://github.com/$mirror/releases/tag/v$Version" -ForegroundColor Yellow
