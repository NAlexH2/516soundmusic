import os
import interactive, standing
import projGlobals as pg
import argparse

ap = argparse.ArgumentParser()
ap.add_argument(
    "-m",
    "--mode",
    type=str,
    choices=["sw", "ia"],
    help="sw = Standing wave - Tune by ear. ia = Interactive - Tune programmatically. Defaults to sw.",
    default="sw",
)

ap.add_argument(
    "-n",
    "--note",
    type=str,
    choices=["E2", "A2", "D3", "G3", "B3", "E4"],
    help="Depending on mode, select which note to use for the specified mode. Defaults to E2.",
    default="E2",
)

ap.add_argument(
    "-ld",
    "--list_devices",
    help="Displays devices to select from for recording then closes program.",
    action="store_true",
    required=False,
)

ap.add_argument(
    "-d",
    "--device",
    type=int,
    help="Device number displayed by the -ld/--list_devices option.",
)

if __name__ == "__main__":
    args = ap.parse_args()
    if args.mode == "ia" and args.device is None:
        ap.error(
            "\nArgument '-d/--device' is required when -m/--mode' is set to 'ia'.\n"
        )
        exit()

    if args.list_devices == True:
        pg.displayRecordingDevices()
        exit()
    if args.mode.lower() == "sw":
        sw = standing.StandingWave()
        sw.standingStart(args.note)
    else:
        ia = interactive.InteractiveDetection()
        ia.interStart(args.note, args.device)

    exit()
