#! /usr/bin/env python

# https://github.com/ckb-next/ckb-next/wiki/CKB-Daemon-Manual

# https://raw.githubusercontent.com/vmedea/ckb-next-integrations/main/xwsmon-ckb.py

import argparse
import time
from typing import NoReturn
from ewmh.ewmh import EWMH
from .ckbpipe import CKBPipe

ewmh = EWMH()


# Names of keys to highlight for workspaces.
KEYS: list[str] = ["f1", "f2", "f3", "f4"]

# Color for inactive, active workspace key (RRGGBBAA).
COLORS: list[str] = ["cccccccc", "ff0000ff"]


def highlight_current_workspace(pipe: CKBPipe, desktop_id: int) -> None:
    try:
        pipe.set_rgb({key: COLORS[desktop_id == i] for (i, key) in enumerate(KEYS)})
        pipe.set_rgb(
            {
                "del": COLORS[desktop_id != 0],
                "pgdn": COLORS[desktop_id != 3],
            }
        )
        pipe.set_rgb(
            {
                "lwin": COLORS[1],
                "lshift": COLORS[1],
            }
        )
    except IOError:
        print(f"<3>Error while opening or writing to pipe\n")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Workspace switch monitor for ckb-next"
    )

    parser.add_argument(
        "--ckb-pipe",
        "-c",
        required=True,
        help="The ckb-pipe-socket (/dev/input/ckb1/cmd)",
    )

    return parser.parse_args()


def main() -> NoReturn:
    args: argparse.Namespace = parse_args()

    pipe: CKBPipe = CKBPipe(args.ckb_pipe)

    old_display_id: int = 0
    display_id: int = 0

    highlight_current_workspace(pipe, display_id)

    while True:
        display_id: int = ewmh.getCurrentDesktop()
        if old_display_id != display_id:
            highlight_current_workspace(pipe, display_id)
            old_display_id: int = display_id
            time.sleep(0.1)


if __name__ == "__main__":
    main()
