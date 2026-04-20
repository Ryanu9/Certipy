"""Parser definition for the custom `example` command."""

import argparse
from typing import Callable, Tuple

NAME = "example"


def entry(options: argparse.Namespace) -> None:
    from certipy.commands.custom import example

    example.entry(options)


def add_subparser(
    subparsers: argparse._SubParsersAction,  # type: ignore
) -> Tuple[str, Callable]:
    sub = subparsers.add_parser(NAME, help="[custom] Example fork-local command")
    _ = sub.add_argument(
        "-message",
        "--message",
        default="hello from custom fork",
        help="Message to print",
    )
    return NAME, entry
