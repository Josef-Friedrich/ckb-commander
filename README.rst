ckb-commander
=============

Control your Corsair keyboard via the ckb-next-daemon.

:: 

    Traceback (most recent call last):
      File "/home/jf/repos/python/ckb_commander/.tox/docs/bin/ckb-commander.py", line 5, in <module>
        from ckb_commander.cli import main
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/ckb_commander/cli.py", line 8, in <module>
        from .workspace_indicator import monitor_workspaces
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/ckb_commander/workspace_indicator.py", line 16, in <module>
        ewmh = EWMH()
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/ewmh/ewmh.py", line 70, in __init__
        self.display = _display or display.Display()
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/Xlib/display.py", line 89, in __init__
        self.display = _BaseDisplay(display)
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/Xlib/display.py", line 71, in __init__
        protocol_display.Display.__init__(self, *args, **keys)
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/Xlib/protocol/display.py", line 84, in __init__
        name, protocol, host, displayno, screenno = connect.get_display(display)
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/Xlib/support/connect.py", line 73, in get_display
        return mod.get_display(display)
      File "/home/jf/repos/python/ckb_commander/.tox/docs/lib/python3.10/site-packages/Xlib/support/unix_connect.py", line 76, in get_display
        raise error.DisplayNameError(display)
    Xlib.error.DisplayNameError: Bad display name ""

workspace-indicator.py
----------------------

Small script that displays on a keyboard using the ckb-next daemon which
desktop (no 0, 1, 2, ...) you are on.

Other pipe scripts:
-------------------

* https://github.com/vmedea/ckb-next-integrations (Python)
* https://github.com/cmd-johnson/ckbpy (Python)
* https://github.com/cmd-johnson/ckb-cloud (NodeJs)
* https://github.com/Misterio77/rgbdaemon
* https://github.com/keesvv/ckbanimate (Rust)
* https://github.com/blockjoe/ckb-animation (Shell)
