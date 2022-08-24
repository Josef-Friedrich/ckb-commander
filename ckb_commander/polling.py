from ewmh.ewmh import EWMH

from .device import Device

ewmh: EWMH = EWMH()


class Poller:
    device: Device

    def __init__(self, device: Device) -> None:
        self.device = device

    def poll(self) -> None:
        ...


class WorkspaceMonitor(Poller):
    old_desktop_id: int
    desktop_id: int

    # Names of keys to highlight for workspaces.
    KEYS: list[str] = ["f1", "f2", "f3", "f4"]

    # Color for inactive, active workspace key (RRGGBBAA).
    COLORS: list[str] = ["gray", "green"]

    def __init__(self, device: Device) -> None:
        super().__init__(device)
        self.old_desktop_id = 0
        self.desktop_id = 0

        self.__highlight_current_workspace()

    def __get_current_workspace(self) -> int:
        try:
            return ewmh.getCurrentDesktop()
        except TypeError:
            return 0

    def __highlight_current_workspace(self) -> None:
        print("Highlight the workspace {}".format(self.desktop_id + 1))
        self.device.set_color_by_mapping(
            {
                key: self.COLORS[self.desktop_id == i]
                for (i, key) in enumerate(self.KEYS)
            }
        )
        self.device.set_color_by_mapping(
            {
                "del": self.COLORS[self.desktop_id != 0],
                "pgdn": self.COLORS[self.desktop_id != 3],
            }
        )

        self.device.set_color_by_mapping(
            {
                "lwin": self.COLORS[1],
                "lshift": self.COLORS[1],
            }
        )

    def poll(self) -> None:
        self.desktop_id = self.__get_current_workspace()
        if self.old_desktop_id != self.desktop_id:
            self.__highlight_current_workspace()
            self.old_desktop_id = self.desktop_id


class ActiveWindow(Poller):
    old_wm_class: str | None
    wm_class: str | None
    keys: str

    KEYS: list[str] = ["f5", "f6", "f7", "f8"]

    def __init__(self, device: Device) -> None:
        super().__init__(device)
        self.old_wm_class = None
        self.wm_class = None
        self.keys = ",".join(self.KEYS)

    def __get_wm_class(self) -> str | None:
        win = ewmh.getActiveWindow()
        if win:
            return win.get_wm_class()[1].lower()

    def __highlight_active_window(self) -> None:
        print(self.wm_class)
        if not self.wm_class:
            return
        if "code" in self.wm_class:
            self.device.set_color("blue", self.keys)
        elif "terminal" in self.wm_class:
            self.device.set_color("white", self.keys)
        elif "firefox" in self.wm_class:
            self.device.set_color("orange", self.keys)
        else:
            self.device.set_color("black", self.keys)


    def poll(self) -> None:
        self.wm_class = self.__get_wm_class()
        if self.old_wm_class != self.wm_class:
            self.__highlight_active_window()
            self.old_wm_class = self.wm_class
