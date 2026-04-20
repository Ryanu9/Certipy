# Custom Fork Changelog

Tracks changes that exist **only in this fork**, separate from upstream
[ly4k/Certipy](https://github.com/ly4k/Certipy) releases.

Format: most recent first. Each entry references the upstream base it was
applied on top of.

## [Unreleased]

### Added
- Fork scaffolding: `certipy/commands/custom/` package, `parsers/custom/`
  registry, `CUSTOM COMMANDS` block in `parsers/__init__.py`.
- Example custom command: `certipy example`.
- `scripts/sync-upstream.ps1` helper for fetching upstream + open PRs.
- `FORK_NOTICE.md` describing fork policy.
- Merge upstream PR #344: Enum ESC17
- Merge feature/enumerate-enrollment-agent-restrictions

### Changed
- `.gitignore`: ignore `.vscode/mcp.json` and `.github/copilot-instructions.md`.

### Upstream base
- `ly4k/Certipy` @ tag `5.0.4` (commit `c1d84d7`).
