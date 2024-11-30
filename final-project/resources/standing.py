import numpy as np
import sounddevice as sd
from .projGlobals import *


# Define how long we want the fade to be, then generate those samples
fade_duration = 0.03  # in seconds
fade_samples = int(fade_duration * SAMPLE_RATE)

# Create global fade-in and fade-out envelopes
global_fade_in = np.linspace(0, 1, fade_samples)
global_fade_out = np.linspace(1, 0, fade_samples)


class StandingWave:
    def __init__(self):
        # Create sine waves here. Reduce amplitude so it's not super loud
        # first play by user.

        self.E2 = self.apply_fade(self.buildNote(E2_FREQ))
        self.A2 = self.apply_fade(self.buildNote(A2_FREQ))
        self.D3 = self.apply_fade(self.buildNote(D3_FREQ))
        self.G3 = self.apply_fade(self.buildNote(G3_FREQ))
        self.B3 = self.apply_fade(self.buildNote(B3_FREQ))
        self.E4 = self.apply_fade(self.buildNote(E4_FREQ))

    # Fade notes so they don't have popping on loop.
    def apply_fade(self, note: np.ndarray):

        if note.size < 2 * fade_samples:
            half = note.size // 2
            fade_in = np.linspace(0, 1, half)
            fade_out = np.linspace(1, 0, half)
        else:
            fade_in = global_fade_in
            fade_out = global_fade_out

        note[: fade_in.size] *= fade_in
        note[-fade_out.size :] *= fade_out
        return note

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
        termClear()
        while True:
            opt = noteMenu()
            print(
                f"\nNow listening to {NOTES_DICT.get(opt)} "
                + "note standing wave tone."
            )
            print("Press Ctrl+C to stop listening.")
            try:
                match opt:
                    case 1:
                        sd.play(data=self.E2, samplerate=SAMPLE_RATE, loop=True)
                    case 2:
                        sd.play(data=self.A2, samplerate=SAMPLE_RATE, loop=True)
                    case 3:
                        sd.play(data=self.D3, samplerate=SAMPLE_RATE, loop=True)
                    case 4:
                        sd.play(data=self.G3, samplerate=SAMPLE_RATE, loop=True)
                    case 5:
                        sd.play(data=self.B3, samplerate=SAMPLE_RATE, loop=True)
                    case 6:
                        sd.play(data=self.E4, samplerate=SAMPLE_RATE, loop=True)
                    case 0:
                        return
                while True:
                    pass
            except KeyboardInterrupt:
                sd.stop()
                termClear()
                print(
                    f"No longer listening to {NOTES_DICT.get(opt)} "
                    + "note standing wave tone.\n"
                )
                opt = -1
