import numpy as np
import os

SAMPLE_RATE = 48000
MAX16 = 32767
STANDING_DUR = 3
T = np.int16
T = np.linspace(
    0, STANDING_DUR, int(SAMPLE_RATE * STANDING_DUR), endpoint=False
)
E2_FREQ = 82.41  # low E string on guitar
A2_FREQ = 110  # A string on guitar
D3_FREQ = 146.83  # D string on guitar
G3_FREQ = 196  # G string on guitar
B3_FREQ = 246.94  # B string on guitar
E4_FREQ = 329.63  # E string on guitar

NOTES_DICT = {1: "E (Low)", 2: "A", 3: "D", 4: "G", 5: "B", 6: "E (High)"}
FREQ_DICT = {1: 82.41, 2: 110, 3: 146.83, 4: 196, 5: 246.94, 6: 329.63}


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
        if diff > 10:
            return f"Tuned way too low! Turn {note} up!\nDifference: {diff}Hz"
        elif diff > 5:
            return f"Still way too low!\nDifference: {diff}Hz"
        elif diff <= 5:
            return f"Almost there! Too low.\nDifference: {diff}Hz"
        else:
            return f"Very close! Too low.\nDifference: {diff}Hz"
    if diff < 2 and diff > -2:
        return (
            "\033[32m"
            + f"\nHonestly, close enough!\nDifference: {diff}Hz"
            + "\033[0m"
        )


def noteMenu() -> int:
    opt = -1
    while opt < 0 or opt > 6:
        try:
            opt = int(
                input(
                    "1: E (Low)\t4: G\n"
                    + "2: A\t\t5: B\n"
                    + "3: D\t\t6: E (High)\n"
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
    return opt
