# https://raw.githubusercontent.com/vmedea/ckb-next-integrations/main/ckbpipe.py


class CKBPipe:
    """Interface to ckb-next 'pipe' animation."""

    def __init__(self, filename: str) -> None:
        """
        Create a new CKBPipe instance for connecting to the specified filename. This does not actually create a connection yet.
        """
        self.filename: str = filename

    def send_command(self, cmd: str) -> None:
        try:
            with open(self.filename, "w") as file:
                file.write(cmd + "\n")
        except IOError:
            print(f"Error while opening or writing to pipe: " + self.filename + "\n")

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

    def set_rgb(self, rgb: str, key: str | None = None) -> None:
        rgb = rgb.replace("#", "")
        key_insert = ""
        if key != None:
            key_insert = key_insert + ":"
        self.send_command("rgb " + key_insert + rgb)

    def set_rgb_key_mapping(self, color_mapping: dict[str, str]) -> None:
        """
        Set colors for keys. Pass a dictionary of `'keyname': 'RRGGBBAA'`.
        See ALL_LEDS for the key names that can be used.
        """
        for (key, value) in color_mapping.items():
            self.send_command("rgb " + key + ":" + value)
