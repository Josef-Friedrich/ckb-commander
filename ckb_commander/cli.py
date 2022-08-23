from typing import NoReturn

import click
from click import Context, Option

from .colors import print_colors, set_colors
from .device import Device
from .workspace_indicator import monitor_workspaces

pipe: Device


def setup_pipe(ctx: Context, param: Option, path: str) -> None:
    global pipe
    pipe = Device(path)


def set_color(ctx: Context, param: Option, color: str) -> None:
    if not color:
        return
    print("Set color " + color)
    pipe.set_color_by_command_string(color)


def activate(ctx: Context, param: Option, flag: bool) -> None:
    if not flag:
        return
    pipe.activate()


def deactivate(ctx: Context, param: Option, flag: bool) -> None:
    if not flag:
        return
    pipe.deactivate()


def indicate_workspace(ctx: Context, param: Option, flag: bool) -> None | NoReturn:
    if not flag:
        return
    monitor_workspaces(pipe)


@click.group()
@click.option(
    "--pipe",
    "-p",
    "pipePath",
    required=True,
    type=str,
    help="The ckb pipe socket (e. g. /dev/input/ckb1/cmd)",
    callback=setup_pipe,
)
def cli(pipePath: str) -> None:
    "Control the ckb-next-daemon"
    pass


@cli.command()
@click.option(
    "--activate",
    "-1",
    help="When plugged in, all devices start in hardware-controlled mode "
    "(also known as idle mode) and will not respond to commands. "
    "Use this option to activate the device.",
    type=str,
    callback=activate,
    is_flag=True,
    expose_value=False,
)
@click.option(
    "--deactivate",
    "-0",
    help="To put the device back into hardware mode, use this option.",
    type=str,
    callback=deactivate,
    is_flag=True,
    expose_value=False,
)
@click.option(
    "--color",
    "-c",
    type=str,
    help="Set the backlight of a single key, "
    "of selected keys or of the entire keyboard to the specified color. "
    "A color name or a RGB value in hex format.",
    callback=set_color,
    expose_value=False,
)
@click.option(
    "--indicate-workspace",
    "-w",
    is_flag=True,
    help="Indicate the current workspace (virtual desktop).",
    callback=indicate_workspace,
    expose_value=False,
)
def control() -> None:
    pass


@cli.command()
def switch_mode() -> None:
    pipe.switch_mode(1)


@cli.group()
def color() -> None:
    "Show informations about the available color names"
    pass


@color.command()
def name() -> None:
    """Show all color names"""
    print_colors()


@color.command()
def set() -> None:
    "Set all keys to the same color. Loop through all colors."
    set_colors(pipe)


def main() -> None:
    cli()
