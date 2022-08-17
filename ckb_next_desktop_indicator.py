#! /usr/bin/env python

# https://github.com/ckb-next/ckb-next/wiki/CKB-Daemon-Manual

import time
from ewmh.ewmh import EWMH
ewmh = EWMH()

print(ewmh.getCurrentDesktop())

# del KEY_DELETE
# { "pgdn",           78, KEY_PAGEDOWN },


with open('/dev/input/ckb1/cmd', 'w') as f:
    f.write('rgb ff0000\n')

time.sleep(1)

with open('/dev/input/ckb1/cmd', 'w') as f:
    f.write('rgb 0000ff\n')
