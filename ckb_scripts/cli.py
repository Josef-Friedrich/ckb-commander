import argparse


from .ckbpipe import CKBPipe
from .workspace_indicator import monitor_workspaces


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Control the ckb-next-daemon")

    parser.add_argument(
        "--pipe",
        "-p",
        required=True,
        help="The ckb pipe socket (e. g. /dev/input/ckb1/cmd)",
    )

    parser.add_argument("--activate", "-1", action="store_true")
    parser.add_argument("--deactivate", "-0", action="store_true")
    parser.add_argument("--switch-mode", "-m")
    parser.add_argument(
        "--workspace-indicator",
        "-w",
        action="store_true",
        help="Workspace (virtual desktops) switch monitor",
    )

    return parser.parse_args()


def main() -> None:
    args: argparse.Namespace = parse_args()

    pipe: CKBPipe = CKBPipe(args.pipe)

    if args.activate:
        pipe.activate()
    elif args.deactivate:
        pipe.deactivate()
    elif args.switch_mode:
        pipe.switch_mode(args.switch_mode)
    elif args.workspace_indicator:
        monitor_workspaces(pipe)

    print(args)
