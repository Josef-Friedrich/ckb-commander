import time
from typing import NoReturn

from ewmh.ewmh import EWMH

from .device import Device

ewmh = EWMH()

REFRESH_RATE: float = 0.1


# Names of keys to highlight for workspaces.
KEYS: list[str] = ["f1", "f2", "f3", "f4"]

# Color for inactive, active workspace key (RRGGBBAA).
COLORS: list[str] = ["cccccccc", "ff0000ff"]


def get_current_workspace() -> int:
    try:
        return ewmh.getCurrentDesktop()
    except TypeError:
        return 0


def highlight_current_workspace(device: Device, desktop_id: int) -> None:
    print("Highlight the workspace {}".format(desktop_id + 1))
    device.set_color_by_mapping(
        {key: COLORS[desktop_id == i] for (i, key) in enumerate(KEYS)}
    )
    device.set_color_by_mapping(
        {
            "del": COLORS[desktop_id != 0],
            "pgdn": COLORS[desktop_id != 3],
        }
    )

    device.set_color_by_mapping(
        {
            "lwin": COLORS[1],
            "lshift": COLORS[1],
        }
    )


def monitor_workspaces(pipe: Device) -> NoReturn:
    old_display_id: int = 0
    display_id: int = 0

    highlight_current_workspace(pipe, display_id)

    while True:
        win = ewmh.getActiveWindow()
        if win:
            print(win.get_wm_class())

        display_id = get_current_workspace()
        if old_display_id != display_id:
            highlight_current_workspace(pipe, display_id)
            old_display_id = display_id
        time.sleep(REFRESH_RATE)
