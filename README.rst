ckb-commander
=============

Control your Corsair keyboard via the ckb-next-daemon.

:: 

    Usage: ckb-commander.py [OPTIONS] COMMAND [ARGS]...

      Control the ckb-next-daemon

    Options:
      -d, --device TEXT  The path of the directory in the /dev/input folder (e. g.
                         /dev/input/ckb1)  [required]
      --help             Show this message and exit.

    Commands:
      color    Show informations about the available color names
      control
      device   Print informations about the specified device

color
-----

:: 

    Usage: ckb-commander.py color [OPTIONS] COMMAND [ARGS]...

      Show informations about the available color names

    Options:
      --help  Show this message and exit.

    Commands:
      name  Show all color names
      set   Set all keys to the same color.

control
-------

:: 

    Usage: ckb-commander.py control [OPTIONS]

    Options:
      -1, --activate                When plugged in, all devices start in
                                    hardware-controlled mode (also known as idle
                                    mode) and will not respond to commands. Use
                                    this option to activate the device.
      -0, --deactivate              To put the device back into hardware mode, use
                                    this option.
      -c, --color TEXT              Set the backlight of a single key, of selected
                                    keys or of the entire keyboard to the
                                    specified color. A color name or a RGB value
                                    in hex format.
      -w, --indicate-workspace      Indicate the current workspace (virtual
                                    desktop).
      -a, --indicate-active-window  Indicate active window.
      --help                        Show this message and exit.

Other pipe scripts:
-------------------

* https://github.com/vmedea/ckb-next-integrations (Python)
* https://github.com/cmd-johnson/ckbpy (Python)
* https://github.com/cmd-johnson/ckb-cloud (NodeJs)
* https://github.com/Misterio77/rgbdaemon
* https://github.com/keesvv/ckbanimate (Rust)
* https://github.com/blockjoe/ckb-animation (Shell)
