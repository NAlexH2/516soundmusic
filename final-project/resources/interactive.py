from time import sleep
import numpy as np
import sounddevice as sd
from scipy.io import wavfile
from projGlobals import *


class InteractiveDetection:
    def __init__(self) -> None:
        self.rec_dev_num = None
        self.rec_dev_name = None
        self.rec_dev_chnls = None
        self.note = -1

    def recAudio(self):
        to_sleep = 2
        print(f"Recording will start in {to_sleep} seconds...")
        sleep(to_sleep)
        print(f"Recording {STANDING_DUR} seconds of audio...")
        audio = sd.rec(
            frames=SAMPLE_RATE * STANDING_DUR,
            samplerate=SAMPLE_RATE,
            channels=self.rec_dev_chnls,
            dtype=np.float32,
            blocking=True,
        )
        if self.rec_dev_chnls > 1:
            audio = np.mean(a=audio, axis=1, dtype=np.float32)
        audio = np.frombuffer(audio, dtype=np.float32)
        print(f"\nRecording finished!")
        wavfile.write("tmp.wav", SAMPLE_RATE, audio)
        return audio

    def compareNote(self):
        termClear()
        again = "s"
        test_note = NOTES_DICT.get(self.note)
        test_freq = FREQ_DICT.get(self.note)
        while again == "s":
            termClear()
            conf = input(
                f"Start recording for analysis using device {self.rec_dev_name}\n"
                f"and note {test_note}? 'N' will return you to note selection.\n"
                "\nRecord? Y/N: "
            ).lower()
            if conf == "y":
                termClear()
                fft_res = np.fft.fft(self.recAudio())
                magnitude = np.abs(fft_res)
                freqs = np.fft.fftfreq(fft_res.size, 1 / SAMPLE_RATE)
                positive_mask = (freqs > 50) & (freqs < 400)
                fund_freq_idx = np.argmax(magnitude[positive_mask])
                # was dom freq, figure out how to find proper freq from range
                fund_freq = freqs[positive_mask][fund_freq_idx]
                fund_freq = float("{:.3f}".format(fund_freq))
                print(f"\nExpected frequency: {test_freq}")
                print(f"Recored frequency: {fund_freq}")
                diff_freq = abs(float("{:.3f}".format(test_freq - fund_freq)))
                if test_freq > fund_freq:
                    diff_freq *= -1
                print(freqDifference(test_note, diff_freq))

            elif conf == "n":
                return
            else:
                termClear()
                conf = "n"
                print("Input Error: Only S or D please...\n")
            again = input(
                "\nRecord same note or a different one? S/D: "
            ).lower()
        return

    def interStart(self):
        self.rec_dev_num, self.rec_dev_name, self.rec_dev_chnls = (
            selectRecordingDevice()
        )
        opt = -1
        while self.rec_dev_num is None:
            self.selectRecordingDevice()

        termClear()
        print(self.rec_dev_num, self.rec_dev_name)
        while opt == -1:
            context = (
                f"Using device #{self.rec_dev_num} - {self.rec_dev_name}\n"
                + "Which note will you be tuning for?"
            )
            opt = noteMenu(context)
            self.note = opt
            if opt == 0:
                sd.stop()
                return
            self.compareNote()
            termClear()
            print(
                f"No longer comparing against {NOTES_DICT.get(opt)} "
                + "note standing wave tone.\n"
            )
            opt = -1
            self.note = -1


if __name__ == "__main__":
    intd = InteractiveDetection()
    intd.interStart()
    exit(0)
