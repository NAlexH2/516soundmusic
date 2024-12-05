from time import sleep
import numpy as np
import sounddevice as sd
import scipy.signal as signal
from scipy.io import wavfile
from projGlobals import *
import matplotlib.pyplot as plt


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
        return audio

    def compareNote(self):
        # termClear()
        again = "s"
        test_note = NOTES_DICT.get(self.note)
        test_freq = FREQ_DICT.get(self.note)
        while again == "s":
            # termClear()
            conf = "y"
            # conf = input(
            #     f"Start recording for analysis using device {self.rec_dev_name}\n"
            #     f"and note {test_note}? 'N' will return you to note selection.\n"
            #     "\nRecord? Y/N: "
            # ).lower()
            if conf == "y":
                # termClear()
                fft_res = np.fft.fft(self.recAudio())
                magnitude = np.abs(fft_res)
                freqs = np.fft.fftfreq(fft_res.size, 1 / SAMPLE_RATE)
                range_mask = (freqs > 50.0) & (freqs < 400.0)
                filtered_freqs = freqs[range_mask]
                filtered_magnitude = magnitude[range_mask]

                # Find peaks in the recorded signal (if any)
                # e2
                # peaks, _ = signal.find_peaks(x=filtered_magnitude, height=50)
                # a2
                # peaks, _ = signal.find_peaks(x=filtered_magnitude, height=1300)
                # d3
                peaks, _ = signal.find_peaks(
                    x=filtered_magnitude,
                    height=50,  # Minimum peak height
                    distance=200,  # Minimum distance between peaks
                    prominence=100,  # Minimum prominence of peaks
                )

                # set some defaults for the next step
                fund_freq_idx = 0
                fund_freq = (
                    None  # None used if no peaks found (no audio recorded)
                )
                if len(peaks) > 0:
                    fund_freq_idx = peaks[0]
                    fund_freq = filtered_freqs[fund_freq_idx]

                # peaks had data, so we captured it in fund_freq
                if fund_freq:
                    fund_freq = float("{:.3f}".format(fund_freq))
                    print(f"\nExpected frequency: {test_freq}")
                    print(f"Recored frequency: {fund_freq}")
                    diff_freq = abs(
                        float("{:.3f}".format(test_freq - fund_freq))
                    )
                    if test_freq > fund_freq:
                        diff_freq *= -1
                    print(freqDifference(test_note, diff_freq), "\n")
                    again = "d"
                else:  # no peaks found therefor no fund_freq set (fund_freq == None)
                    print(
                        "No significant frequency detected in the recorded audio."
                    )
            elif conf == "n":
                return
            else:
                # termClear()
                conf = "n"
                print("Input Error: Only Y or N please...\n")
            # again = input(
            #     "\nRecord same note or a different one? S/D: "
            # ).lower()
        magnitude_db = 20 * np.log10(magnitude)
        filtered_magnitude_db = 20 * np.log10(filtered_magnitude)
        plt.figure(figsize=(10, 6))
        plt.plot(filtered_freqs, filtered_magnitude_db)
        plt.plot(filtered_freqs[peaks], filtered_magnitude_db[peaks], "ro")

        # Add text labels for each peak
        for i, peak in enumerate(peaks):
            plt.annotate(
                f"Peak {i}\n{filtered_freqs[peak]:.2f} Hz\n{filtered_magnitude_db[peak]:.2f} dB",
                (filtered_freqs[peak], filtered_magnitude_db[peak]),
                xytext=(40, -20),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
            )

        plt.title(
            f"Frequency Spectrum with Peaks - {NOTES_DICT.get(self.note)} Note",
            pad=20,
        )
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude (dB)")
        plt.show()
        plt.ioff()
        return

    def interStart(self):
        # self.rec_dev_num, self.rec_dev_name, self.rec_dev_chnls = (
        #     selectRecordingDevice()
        # )
        self.rec_dev_chnls = 2
        self.rec_dev_name = "Brio Webcam"
        self.rec_dev_num = 3
        sd.default.device = self.rec_dev_num
        sd.default.samplerate = SAMPLE_RATE
        # termClear()
        opts = [0, 6]
        while opts:
            self.note = opts.pop()
            # context = (
            #     f"Using device #{self.rec_dev_num} - {self.rec_dev_name}\n"
            #     + "Which note will you be tuning for?"
            # )
            # opt = noteMenu(context)
            print(f"\nTuning for {NOTES_DICT.get(self.note)} note.\n")
            if self.note == 0:
                sd.stop()
                return
            self.compareNote()
            # termClear()
            print(f"No longer tuning for {NOTES_DICT.get(self.note)} note.\n")
            # opt = -1
            # self.note = -1


if __name__ == "__main__":
    intd = InteractiveDetection()
    intd.interStart()
    exit(0)
