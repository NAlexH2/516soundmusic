import numpy as np
import os
import sounddevice as sd

# Used throughout the program
SAMPLE_RATE = 48000
STANDING_DUR = 3
T_SPACE = np.linspace(
    0,
    STANDING_DUR,
    int(SAMPLE_RATE * STANDING_DUR),
    endpoint=False,
    dtype=np.int16,
)

NOTES_TO_FREQ_DICT = {
    "E2": 82.41,
    "A2": 110,
    "D3": 146.83,
    "G3": 196,
    "B3": 246.94,
    "E4": 329.63,
}


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


def displayRecordingDevices():
    print("\nDisplaying available devices to choose from.\n")
    for device in sd.query_devices():
        if device["max_input_channels"] >= 1 and device["hostapi"] == 0:
            print(
                f"#{device["index"]} -- {device["name"]} -- {device["max_input_channels"]}"
            )
    return


def getDeviceInfo(opt):
    device_list = dict()
    for device in sd.query_devices():
        if device["max_input_channels"] > 1 and device["hostapi"] == 0:
            iInfo = device["index"]
            nInfo = device["name"]
            cInfo = device["max_input_channels"]
            device_list[iInfo] = (nInfo, cInfo)

    return opt, device_list[opt][0], device_list[opt][1]
