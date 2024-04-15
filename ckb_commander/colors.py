import time
import typing

import webcolors
from rich.console import Console

if typing.TYPE_CHECKING:
    from .device import Device


console: Console = Console()
colors: dict[str, str] = {**webcolors.CSS21_NAMES_TO_HEX, **webcolors.CSS3_NAMES_TO_HEX}


def print_color(color_name: str, rgb_value: str) -> None:
    console.print(
        "   " + rgb_value.replace("#", "") + " ", style="on " + rgb_value, end=""
    )
    print(" " + color_name)


def print_colors() -> None:
    for color_name, rgb_value in colors.items():
        print_color(color_name, rgb_value)


def set_colors(device: "Device") -> None:
    for color_name, rgb_value in colors.items():
        print_color(color_name, rgb_value)
        device.set_color(rgb_value)
        time.sleep(1)
