import os
import numpy as np
import sounddevice as sd
from .projGlobals import *


class StandingWave:
    def __init__(self):
        # Create sine waves here. Reduce amplitude so it's not super loud
        # first play by user.

        self.E2 = self.buildNote(E2_FREQ)
        self.A2 = self.buildNote(A2_FREQ)
        self.D3 = self.buildNote(D3_FREQ)
        self.G3 = self.buildNote(G3_FREQ)
        self.B3 = self.buildNote(B3_FREQ)
        self.E4 = self.buildNote(E4_FREQ)

    def buildNote(self, freq):
        if freq != E4_FREQ:
            note = 0.05 * np.sin(2 * np.pi * freq * T)
        else:
            note = 0.2 * np.sin(2 * np.pi * freq * T)
        note += self.secondHarmonic(freq)
        note += self.thirdHarmonic(freq)
        return note

    def secondHarmonic(self, freq):
        if freq != E4_FREQ:
            return 0.1 * np.sin(2 * np.pi * (2 * freq) * T)
        else:
            return 0.04 * np.sin(2 * np.pi * (2 * freq) * T)

    def thirdHarmonic(self, freq):
        if freq != E4_FREQ:
            return 0.05 * np.sin(2 * np.pi * (3 * freq) * T)
        else:
            return 0.04 * np.sin(2 * np.pi * (2 * freq) * T)

    def standingMenu(self):
        os.system("cls" if os.name == "nt" else "clear")
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
                os.system("cls" if os.name == "nt" else "clear")
                continue
            if opt == 0:
                return

            print(
                f"\nNow listening to {NOTES_DICT.get(opt)} "
                + "note standing wave tone."
            )
            print("Press Ctrl+C to stop listening.")
            try:
                match opt:
                    case 1:
                        sd.play(data=self.E2, samplerate=SAMPLE, loop=True)
                    case 2:
                        sd.play(data=self.A2, samplerate=SAMPLE, loop=True)
                    case 3:
                        sd.play(data=self.D3, samplerate=SAMPLE, loop=True)
                    case 4:
                        sd.play(data=self.G3, samplerate=SAMPLE, loop=True)
                    case 5:
                        sd.play(data=self.B3, samplerate=SAMPLE, loop=True)
                    case 6:
                        sd.play(data=self.E4, samplerate=SAMPLE, loop=True)
                while True:
                    pass
            except KeyboardInterrupt:
                sd.stop()
                os.system("cls" if os.name == "nt" else "clear")
                print(
                    f"No longer listening to {NOTES_DICT.get(opt)} "
                    + "note standing wave tone.\n"
                )
                opt = -1
