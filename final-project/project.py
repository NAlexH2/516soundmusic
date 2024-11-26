import os
import numpy as np
import sounddevice as sd
import librosa
import matplotlib
from scipy import fft
from resources import automatic, interactive, standing


# This project is going to be a tuner with several options. Specifically, for a
# guitar.

# First is to generate a standing wave of specific frequencies

# Second is going to be interactive to select which note and measure what was
# received and give a good or negative response indicating if it was close enough
# or way off. Floating point value +/- of how far off it was?

# Third is automatic detection. FFT and analyzing peak freqs for the value
# received, and detecting it's closest value.


def printOptions():
    print("Please select an option to use for tuning your instrument.")
    print(
        "1 - Standing Wave - Listen to a tone for each note to pitch match \n"
        + "    against.\n"
    )
    print(
        "2 - Interactive Detection - Pick and play the note to see how \n"
        + "    correct its pitch is.\n"
    )
    print(
        "3 - Automatic Detection - Play any note, and this will automatically \n"
        + "    tell you how close the pitch is and which note you are trying to tune."
        + "\n"
    )
    print("0 - Closes this program.\n")
    print("Option:", end=" ")


def mainMenu():
    opt = -1
    sw = standing.StandingWave()
    interDec = interactive.InteractiveDetection()
    ad = automatic.AutomaticDetection()
    while opt < 0 or opt > 3:
        printOptions()
        try:
            opt = int(input())
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"**ERROR** --- Invalid option!\n")
            opt = -1
            continue
        match opt:
            case 0:
                print("\nExiting program. . .")
                return
            case 1:
                sw.standingMenu()
            case 2:
                interDec.interStart()
            case 3:
                ad.autoStart()
            case _:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"**ERROR** --- {opt} is an invalid option!\n")
        opt = -1


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("---- About this program ----")
    print(
        "This program is designed to give a user the option to tune a \n"
        + "guitar or similar instruments that follow the 'E A D G B E' note \n"
        + "scale.\n"
    )
    mainMenu()

    exit()