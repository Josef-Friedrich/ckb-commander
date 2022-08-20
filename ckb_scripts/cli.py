from typing import NoReturn
import click

from .ckbpipe import CKBPipe
from .workspace_indicator import monitor_workspaces
from .colors import print_colors, set_colors

pipe: CKBPipe


def main() -> None:
    @click.group()
    @click.option(
        "--pipe",
        "-p",
        "pipePath",
        required=True,
        type=str,
        help="The ckb pipe socket (e. g. /dev/input/ckb1/cmd)",
    )
    def cli(pipePath: str) -> None:
        "Control the ckb-next-daemon"
        global pipe
        pipe = CKBPipe(pipePath)

    @cli.command()
    def activate() -> None:
        pipe.activate()

    @cli.command()
    def deactivate() -> None:
        pipe.deactivate()

    @cli.command()
    def switch_mode() -> None:
        pipe.switch_mode(1)

    @cli.command()
    def indicate_workspace() -> NoReturn:
        "Workspace (virtual desktops) switch monitor"
        monitor_workspaces(pipe)

    @cli.command()
    def show_color_names()  -> None:
        "Print all color names to stdout"
        print_colors()

    @cli.command()
    def set_all_colors() -> None:
        "Set all keys to the same color. Loop through all colors."
        set_colors(pipe)

    cli()
