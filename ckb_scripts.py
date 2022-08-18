#! /usr/bin/env python

# https://github.com/ckb-next/ckb-next/wiki/CKB-Daemon-Manual

import time
from ewmh.ewmh import EWMH

ewmh = EWMH()

DEVICE = "/dev/input/ckb1/cmd"

print(ewmh.getCurrentDesktop())

# del KEY_DELETE
# { "pgdn",           78, KEY_PAGEDOWN },


def send_command(command: str) -> None:
    with open(DEVICE, "w") as f:
        f.write(command + "\n")


time.sleep(1)

with open("/dev/input/ckb1/cmd", "w") as f:
    f.write("rgb 0000ff\n")
