#!/usr/bin/env pwsh
# release.ps1 - Publish ONE plugin version to the public marketplace.
#
# Distribution model (since Aug 2026): clients add the PUBLIC marketplace repo
# once (/plugin marketplace add BillyRybka/authentic-ai) and Claude auto-updates
# their installed plugins from it. There are no mirror repos, no .plugin zips,
# no gh releases, and no in-skill update check. Publishing IS the git push.
#
# THE ONE RULE THAT MATTERS: only a HISTORY-FREE SNAPSHOT of the built storefront
# ever reaches the `public` remote. Never push a branch. main's own history is NOT
# clean: its pre-allowlist commits carry Billy's creator-foundation.md, banks/,
# audits/, and WIP skills, so `git push public main` would leak all of it. The
# publish step below builds a snapshot commit (main's tree, no parents from main)
# on the `public-main` lineage and pushes that. dev, feature branches, the vault,
# documents/, plans/ must never be pushed there. A wrong push to public is a data
# leak, not a broken build.
#
# `main` is an ALLOWLIST rebuild: wiped and reconstructed from the paths below,
# so private content stays off it by construction. It always carries EVERY
# shipping plugin. -Plugin selects which plugin's version bumps; it never selects
# which plugins exist (a single-plugin allowlist would delete the others from
# main and break those installs).
#
# Build and safety checks live in scripts/generate-plugins.mjs and
# scripts/qa-plugins.mjs. They run first and abort on any blocker.
#
# Usage:
#   pwsh scripts/release.ps1 -Plugin aai-youtube -Version 0.4.0
#   pwsh scripts/release.ps1 -Plugin aai-youtube -Version 0.4.0 -DryRun

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
if (-not ((git remote | Out-String) -match '(?m)^public$')) {
    throw "No 'public' remote. Add it: git remote add public https://github.com/BillyRybka/authentic-ai.git"
}

$mapPath = '.claude-plugin/plugins-map.json'
$mpPath  = '.claude-plugin/marketplace.json'
$map = Get-Content $mapPath -Raw | ConvertFrom-Json

$pluginNames = $map.plugins.PSObject.Properties.Name
if ($pluginNames -notcontains $Plugin) {
    throw "Unknown plugin '$Plugin'. Defined plugins: $($pluginNames -join ', ')"
}

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
    # Annotated (-a). Lightweight tags are skipped by `git push --follow-tags`.
    git tag -a $tag -m $tag
    $ok = $true
}
finally {
    # Always return to the workshop. -f discards a half-built main on failure.
    git checkout -f dev | Out-Null
}

if (-not $ok) { throw "Release failed while rebuilding main. Nothing was pushed." }

if ($DryRun) {
    Write-Host ""
    Write-Host "DRY RUN. Built locally. Nothing pushed or published." -ForegroundColor Yellow
    Write-Host "  main commit: $(git rev-parse main)"
    Write-Host "  tag:         $tag (LOCAL ONLY)"
    Write-Host ""
    Write-Host "Inspect:   git log main -1; git show main --stat" -ForegroundColor DarkGray
    Write-Host "Roll back: git tag -d $tag; git checkout main; git reset --hard origin/main; git checkout dev; git reset --hard origin/dev" -ForegroundColor DarkGray
    exit 0
}

# --- publish -----------------------------------------------------------------
Write-Host ""
Write-Host "Pushing main + tag + dev to origin (private)..." -ForegroundColor Cyan
git push origin main --follow-tags
if ($LASTEXITCODE -ne 0) { throw "git push origin main failed." }
git push origin dev
if ($LASTEXITCODE -ne 0) { throw "git push origin dev failed." }

# The public push IS the release. Claude pulls marketplace updates from this repo
# and auto-updates clients.
#
# Publish a SNAPSHOT, never the main branch itself: main's pre-allowlist history
# contains private vault content, so its lineage must never leave this repo.
# public-main is a separate lineage holding one clean snapshot commit per release.
Write-Host "Publishing: snapshot of main's tree to the public marketplace repo..." -ForegroundColor Cyan
$tree = (git rev-parse 'main^{tree}').Trim()
$parent = (git rev-parse -q --verify public-main 2>$null | Out-String).Trim()
if ($parent) {
    $snap = (git commit-tree $tree -p $parent -m "Release $Plugin v$Version" | Out-String).Trim()
} else {
    # First release: an orphan commit. The public repo's history starts here, clean.
    $snap = (git commit-tree $tree -m "Release $Plugin v$Version" | Out-String).Trim()
}
if (-not $snap) { throw "commit-tree produced no commit. Clients have NOT been updated." }
git update-ref refs/heads/public-main $snap
git push public public-main:main
if ($LASTEXITCODE -ne 0) { throw "git push public public-main:main failed. Clients have NOT been updated." }

Write-Host ""
Write-Host "Released $Plugin v$Version." -ForegroundColor Green
Write-Host "  Clients auto-update from: https://github.com/BillyRybka/authentic-ai" -ForegroundColor Yellow
Write-Host "  New client install: /plugin marketplace add BillyRybka/authentic-ai  then  /plugin install $Plugin@authentic-ai" -ForegroundColor DarkGray
