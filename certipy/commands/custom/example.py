"""
Example custom command. Safe to delete.

Demonstrates the minimal shape a fork-local command needs.
Run with:  certipy example --message "hello"
"""

import argparse

from certipy.lib.logger import logging


def entry(options: argparse.Namespace) -> None:
    """Entry point invoked by the main dispatcher."""
    logging.info(f"[custom-example] message = {options.message!r}")
