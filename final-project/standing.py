import numpy as np
import sounddevice as sd
from projGlobals import *


# Define how long we want the fade to be, then generate those samples
fade_duration = 0.03  # in seconds
fade_samples = int(fade_duration * SAMPLE_RATE)

# Create global fade-in and fade-out envelopes
global_fade_in = np.linspace(0, 1, fade_samples)
global_fade_out = np.linspace(1, 0, fade_samples)


class StandingWave:
    def __init__(self):
        self.tone = None

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
        if freq != NOTES_TO_FREQ_DICT["E4"]:
            note = 0.05 * np.sin(2 * np.pi * freq * T_SPACE)
        else:
            note = 0.2 * np.sin(2 * np.pi * freq * T_SPACE)
        note += self.secondHarmonic(freq)
        note += self.thirdHarmonic(freq)
        return note

    def secondHarmonic(self, freq):
        if freq != NOTES_TO_FREQ_DICT["E4"]:
            return 0.1 * np.sin(2 * np.pi * (2 * freq) * T_SPACE)
        else:
            return 0.04 * np.sin(2 * np.pi * (2 * freq) * T_SPACE)

    def thirdHarmonic(self, freq):
        if freq != NOTES_TO_FREQ_DICT["E4"]:
            return 0.05 * np.sin(2 * np.pi * (3 * freq) * T_SPACE)
        else:
            return 0.04 * np.sin(2 * np.pi * (2 * freq) * T_SPACE)

    def standingStart(self, note):
        termClear()
        self.tone = self.apply_fade(self.buildNote(NOTES_TO_FREQ_DICT[note]))
        try:
            print(f"\nNow listening to {note} " + "note standing wave tone.")
            print("Press Ctrl+C to stop listening.")

            sd.play(data=self.tone, samplerate=SAMPLE_RATE, loop=True)
            while True:
                pass
        except KeyboardInterrupt:
            sd.stop()
            print(f"No longer listening to {note} note standing wave tone.\n")
            opt = -1
