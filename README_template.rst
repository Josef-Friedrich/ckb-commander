ckb-commander
=============

Control your Corsair keyboard via the ckb-next-daemon.

{{ cli('ckb-commander.py --help') | literal }}

{% for command in [
                   'color',
                   'control'
                  ]
%}

{{ command | heading(2) }}

{{ cli('ckb-commander.py --device /dev/input/ckb1 {} --help'.format(command)) | literal }}
{% endfor %}

Other pipe scripts:
-------------------

* https://github.com/vmedea/ckb-next-integrations (Python)
* https://github.com/cmd-johnson/ckbpy (Python)
* https://github.com/cmd-johnson/ckb-cloud (NodeJs)
* https://github.com/Misterio77/rgbdaemon
* https://github.com/keesvv/ckbanimate (Rust)
* https://github.com/blockjoe/ckb-animation (Shell)
