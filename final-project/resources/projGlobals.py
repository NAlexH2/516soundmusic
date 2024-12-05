import numpy as np
import os
import sounddevice as sd

# Used throughout the program
SAMPLE_RATE = 48000
MAX16 = 32767
STANDING_DUR = 3
T = np.int16
T = np.linspace(
    0, STANDING_DUR, int(SAMPLE_RATE * STANDING_DUR), endpoint=False
)
E2_FREQ = 82.41  # low E string on guitar (E2)
A2_FREQ = 110  # A string on guitar (A2)
D3_FREQ = 146.83  # D string on guitar (D3)
G3_FREQ = 196  # G string on guitar (G3)
B3_FREQ = 246.94  # B string on guitar (B3)
E4_FREQ = 329.63  # E string on guitar (E4)


NOTES_DICT = {1: "E2", 2: "A2", 3: "D3", 4: "G3", 5: "B3", 6: "E4"}
FREQ_DICT = {1: 82.41, 2: 110, 3: 146.83, 4: 196, 5: 246.94, 6: 329.63}
NOTES_TO_FREQ_DICT = {
    "E2": 82.41,
    "A2": 110,
    "D3": 146.83,
    "G3": 196,
    "B3": 246.94,
    "E4": 329.63,
}

# Used for DFT tuner (automatic.py)
PITCH_CHECK = 440.0


def termClear():
    os.system("cls" if os.name == "nt" else "clear")


def freqDifference(note: str, diff: float) -> str:
    if diff >= 2:
        if diff > 10:
            return (
                f"Tuned way too high! Turn {note} down!\nDifference: {diff}Hz"
            )
        elif diff > 5:
            return f"Still way too high!\nDifference: {diff}Hz"
        elif diff <= 5:
            return f"Almost there! Too high.\nDifference: {diff}Hz"
        else:
            return f"Very close! Too high.\nDifference: {diff}Hz"

    if diff < -1:
        if diff < -10:
            return f"Tuned way too low! Turn {note} up!\nDifference: {diff}Hz"
        elif diff < -5:
            return f"Still way too low!\nDifference: {diff}Hz"
        elif diff <= 5:
            return f"Almost there! Too low.\nDifference: {diff}Hz"
        else:
            return f"Very close! Too low.\nDifference: {diff}Hz"
    if diff <= 1 and diff >= -1:
        return (
            "\033[32m"
            + f"\nHonestly, close enough!\nDifference: {diff}Hz"
            + "\033[0m"
        )


def noteMenu(ctx: str) -> int:
    opt = -1
    while opt < 0 or opt > 6:
        if ctx:
            print(ctx)
        try:
            opt = int(
                input(
                    "1: E2\t4: G2\n"
                    + "2: A3\t5: B3\n"
                    + "3: D3\t6: E4\n"
                    + "\n0: Exit\n\nOption: "
                )
            )
        except ValueError:
            opt = -1
            termClear()
            continue
        if opt > 6:
            opt = -1
            termClear()
            continue
    return int(opt)


def selectRecordingDevice():
    termClear()
    device_list = dict()
    for device in sd.query_devices():
        if device["max_input_channels"] > 1 and device["hostapi"] == 0:
            iInfo = device["index"]
            nInfo = device["name"]
            cInfo = device["max_input_channels"]
            device_list[iInfo] = (nInfo, cInfo)

    opt = -1
    conf = "n"
    while opt not in device_list or conf != "Y".lower():
        print(
            "Select which device to use for live audio processing "
            "and note comparison: "
        )
        try:
            for d in device_list:
                print(
                    f"   #{d} - Name: {device_list[d][0]} -- Channels: {device_list[d][1]}"
                )
            opt = int(input("\nPlease enter which device number to use: "))
        except ValueError:
            opt = -1
            termClear()
            print("Invalid option...\n")
            continue
        if opt not in device_list:
            opt = -1
            termClear()
            print("Invalid option...\n")
            continue
        else:
            print(f"Selected device --> {device_list[opt]}.")
            conf = input("Is this correct? Y/N: ").lower()
            if conf != "y":
                conf = "n"
                termClear()
                continue

    return opt, device_list[opt][0], device_list[opt][1]
