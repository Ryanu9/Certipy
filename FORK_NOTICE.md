# Fork Notice

This repository is a personal fork of [ly4k/Certipy](https://github.com/ly4k/Certipy).

- **Default working branch**: `custom/main` (integrates upstream + selected
  community PRs + fork-local features).
- **Upstream mirror branch**: `main` (kept identical to `upstream/main`,
  never directly modified).
- **Push policy**: this fork will *never* push back to `ly4k/Certipy`.
  Upstream remote has `pushurl = no-push` to enforce this.

## Sync workflow

```powershell
# Pull upstream + community PR refs
./scripts/sync-upstream.ps1

# Merge upstream/main into custom/main
git checkout custom/main
git merge --no-ff main -m "Sync: merge upstream main"

# Cherry-pick or merge a community PR by number
git merge --no-ff upstream/pr/<N> -m "Merge upstream PR #<N>: <desc>"
```

See [CHANGELOG.custom.md](CHANGELOG.custom.md) for the list of fork-local
changes and the upstream base they sit on.
