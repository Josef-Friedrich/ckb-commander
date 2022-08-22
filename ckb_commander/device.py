# https://raw.githubusercontent.com/vmedea/ckb-next-integrations/main/ckbpipe.py

from grp import struct_group
from .colors import colors
from pathlib import Path


class Device:
    """A Corsair device."""

    def __init__(self, path: str) -> None:
        """
        :param path: The device path, for example ``/dev/input/ckb1``
        """

        p = Path(path)

        if not p.exists():
            raise Exception("ckb-next pipe file doesn’t exist: " + path)

        self.path: Path = p

    def __read_from_file(self, path: str | Path) -> str:
        """:param path: An absolute path or a path relative to /dev/input/ckbX."""
        read_file: Path
        if isinstance(path, str):
            read_file = self.path / path
        else:
            read_file = path

        with open(read_file, "r") as file:
            content: str = file.read()
            if content:
                return content.strip()

        raise Exception("Could not read from " + str(read_file))

    def __send_command(self, cmd: str) -> None:
        cmd_file = self.path / "cmd"
        try:
            with open(cmd_file, "w") as file:
                file.write(cmd + "\n")
        except IOError:
            print(f"Error while opening or writing to pipe: " + str(cmd_file) + "\n")

    def __get_parameters(self, get: str) -> str:
        self.__send_command("get :" + get)
        notify_path = self.path / "notify0"
        with open(notify_path) as file:
            return file.readline()

    @property
    def dpi(self) -> str:
        return self.__read_from_file("dpi")

    @property
    def features(self) -> str:
        return self.__read_from_file("features")

    @property
    def layout(self) -> str:
        return self.__read_from_file("layout")

    @property
    def fwversion(self) -> str:
        return self.__read_from_file("fwversion")

    @property
    def rgb(self) -> str:
        return self.__get_parameters("rgb")

    def activate(self) -> None:
        """When plugged in, all devices start in hardware-controlled mode (also
        known as idle mode) and will not respond to commands. Before issuing
        any other commands, write active to the command node, like echo active
        > /dev/input/ckb1/cmd"""
        self.__send_command("active")

    def deactivate(self) -> None:
        """To put the device back into hardware mode, issue the idle
        command."""
        self.__send_command("idle")

    def switch_mode(self, number: int) -> None:
        self.__send_command("mode {} switch".format(number))

    def set_color(self, color: str, keys: str | None = None) -> None:
        if color in colors:
            color = colors[color]
        color = color.replace("#", "")
        keys_insert = ""
        if keys != None:
            keys_insert = keys + ":"
        self.__send_command("rgb " + keys_insert + color)

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
