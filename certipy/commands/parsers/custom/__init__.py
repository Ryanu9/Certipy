"""
Registration list for fork-local commands.

This module is the single integration point between custom commands and the
upstream parser registry. Keeping the list isolated here means upstream changes
to `certipy/commands/parsers/__init__.py` only collide on a single import line.
"""

from . import example

# Append your custom parser modules here.
CUSTOM_ENTRY_PARSERS = [
    example,
]
