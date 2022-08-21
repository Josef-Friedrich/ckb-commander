# https://raw.githubusercontent.com/vmedea/ckb-next-integrations/main/ckbpipe.py

from .colors import colors
from pathlib import Path


class CKBPipe:
    def __init__(self, path: str) -> None:
        """
        Create a new CKBPipe instance for connecting to the specified filename. This does not actually create a connection yet.
        """

        p = Path(path)

        if not p.exists():
            raise Exception("ckb-next pipe file doesn’t exist: " + path)

        self.path: Path = p

    def send_command(self, cmd: str) -> None:
        try:
            with open(self.path, "w") as file:
                file.write(cmd + "\n")
        except IOError:
            print(f"Error while opening or writing to pipe: " + str(self.path) + "\n")

    def activate(self) -> None:
        """When plugged in, all devices start in hardware-controlled mode (also
        known as idle mode) and will not respond to commands. Before issuing
        any other commands, write active to the command node, like echo active
        > /dev/input/ckb1/cmd"""
        self.send_command("active")

    def deactivate(self) -> None:
        """To put the device back into hardware mode, issue the idle
        command."""
        self.send_command("idle")

    def switch_mode(self, number: int) -> None:
        self.send_command("mode {} switch".format(number))

    def set_color(self, color: str, keys: str | None = None) -> None:
        if color in colors:
            color = colors[color]
        color = color.replace("#", "")
        keys_insert = ""
        if keys != None:
            keys_insert = keys + ":"
        self.send_command("rgb " + keys_insert + color)

    def set_color_by_command_string(self, cmds: str):
        for cmd in cmds.split():
            c: list[str] = cmd.split(":")
            if len(c) == 2:
                self.set_color(c[1], c[0])
            else:
                self.set_color(c[0])

    def set_color_by_mapping(self, color_mapping: dict[str, str]) -> None:
        for (key, color) in color_mapping.items():
            self.set_color(color, key)
