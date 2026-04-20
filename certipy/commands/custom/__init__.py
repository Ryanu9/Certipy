"""
Custom commands for this Certipy fork.

All fork-local commands live here so upstream merges have minimal conflicts.
To add a new command:
    1. Create `certipy/commands/custom/<name>.py` with an `entry(options)` function.
    2. Create `certipy/commands/parsers/custom/<name>.py` with `NAME`,
       `entry(options)`, and `add_subparser(subparsers)`.
    3. Append the parser module to `CUSTOM_ENTRY_PARSERS` in
       `certipy/commands/parsers/custom/__init__.py`.
"""
