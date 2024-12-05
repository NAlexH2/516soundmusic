import os
import interactive, standing
import projGlobals as pg
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--mode", type=str, choices=["sw", "ia"])
ap.add_argument(
    "--note", type=str, choices=["E2", "A2", "D3", "G3", "B3", "E4"]
)


def printOptions():
    print("Please select an option to use for tuning your instrument.")
    print(
        "1 - Standing Wave - Listen to a tone for each note to pitch match \n"
        + "    against.\n"
    )
    print(
        "2 - Interactive Detection - Pick a note, play and record the note, then\n"
        + "    see how correct its pitch is.\n"
    )
    print("0 - Closes this program.\n")
    print("Option:", end=" ")


def mainMenu():
    opt = -1
    clrs = False
    sw = standing.StandingWave()
    interDec = interactive.InteractiveDetection()
    while opt < 0 or opt > 2:
        if clrs == True:
            pg.termClear()
            clrs = False
        if opt < -1 or opt > 2:
            print(f"**ERROR** --- {opt} is an invalid option!\n")
            opt = -1
            clrs = True
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
                pg.termClear()
                print("\nExiting program. . .")
                return
            case 1:
                sw.standingMenu()
                opt = -1
            case 2:
                interDec.interStart()
                opt = -1
            case _:
                pass
        clrs = True


if __name__ == "__main__":
    pg.termClear()
    print("---- About this program ----")
    print(
        "This program is designed to give a user the option to tune a \n"
        + "guitar or similar instruments that follow the 'E A D G B E' note \n"
        + "scale.\n"
    )
    mainMenu()

    exit()
