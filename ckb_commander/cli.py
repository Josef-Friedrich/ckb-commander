from typing import NoReturn

import click
from click import Context, Option

from .colors import print_colors, set_colors
from .device import Device
from .workspace_indicator import monitor_workspaces


def setup_device(ctx: Context, param: Option, path: str) -> None:
    device = Device(path)
    ctx.obj = device


def set_color(ctx: Context, param: Option, color: str) -> None:
    if not color:
        return
    print("Set color " + color)
    ctx.obj.set_color_by_command_string(color)


def activate(ctx: Context, param: Option, flag: bool) -> None:
    if not flag:
        return
    ctx.obj.activate()


def deactivate(ctx: Context, param: Option, flag: bool) -> None:
    if not flag:
        return
    ctx.obj.deactivate()


def indicate_workspace(ctx: Context, param: Option, flag: bool) -> None | NoReturn:
    if not flag:
        return
    monitor_workspaces(ctx.obj)


@click.group()
@click.option(
    "--device",
    "-d",
    required=True,
    type=str,
    help="The path of the directory in the /dev/input folder (e. g. /dev/input/ckb1)",
    callback=setup_device,
)
def cli(device: str) -> None:
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


@cli.group()
def color() -> None:
    "Show informations about the available color names"
    pass


@color.command()
def name() -> None:
    """Show all color names"""
    print_colors()


@color.command()
@click.pass_context
def set(ctx: Context) -> None:
    "Set all keys to the same color. Loop through all colors."
    set_colors(ctx.obj)


@cli.command()
@click.pass_context
def device(ctx: Context) -> None:
    """Print informations about the specified device"""

    device = ctx.obj
    print(device.rgb)


def main() -> None:
    cli()
