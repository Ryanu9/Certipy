# Sync upstream main and all open PR refs into local refs.
# Usage: pwsh ./scripts/sync-upstream.ps1
#
# This only fetches; it never merges automatically. Merging into custom/main
# is left as a manual step so you stay in control.

$ErrorActionPreference = 'Stop'

Write-Host '==> fetching upstream main + tags...' -ForegroundColor Cyan
git fetch upstream --tags --prune

Write-Host '==> fast-forwarding local main to upstream/main...' -ForegroundColor Cyan
$current = (git rev-parse --abbrev-ref HEAD).Trim()
git checkout main
git merge --ff-only upstream/main
git push origin main

if ($current -ne 'main') {
    git checkout $current
}

Write-Host ''
Write-Host 'Done. To integrate upstream into custom/main:' -ForegroundColor Green
Write-Host '  git checkout custom/main'
Write-Host '  git merge --no-ff main -m "Sync: merge upstream main"'
Write-Host ''
Write-Host 'To list newly arrived upstream PR refs:' -ForegroundColor Green
Write-Host '  git for-each-ref refs/remotes/upstream/pr/ --format="%(refname:short) %(committerdate:short)" | Sort-Object -Descending | Select-Object -First 20'
