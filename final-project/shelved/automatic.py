import numpy as np
import sounddevice as sd
from projGlobals import *

# Number of samples per FFT. Should be a power of 2.
FFT_LEN = 4096


class AutomaticDetection:

    def __init__(self):
        self.stream = None
        self.dom_freq = 0.0
        self.notes = list(NOTES_DICT.values())
        self.nearest_note = ""
        self.nearest_pitch = ""
        self.rec_dev_num = None
        self.rec_dev_name = None
        self.rec_dev_chnls = None
        self.buffer = np.array([], dtype=np.float64)
        self.frames_processed = 0

    def nearest_neighbor(self):
        notes_len = len(self.notes)
        n = int(np.round((self.dom_freq / PITCH_CHECK) * notes_len))
        self.nearest_note = self.notes[n % notes_len]
        self.nearest_pitch = PITCH_CHECK * 2 ** (n / notes_len)
        return

    def callback(self, inputD: np.ndarray, frames, dur, state):
        if any(inputD):
            if self.rec_dev_chnls > 1:
                inputD = np.mean(a=inputD, axis=1, dtype=np.float32)
            if len(self.buffer) >= FFT_LEN + frames:
                self.buffer = self.buffer[frames:]
            self.buffer = np.append(self.buffer, inputD.flatten())
            fft_res = np.fft.fft(self.buffer[:FFT_LEN])
            magnitude = np.abs(fft_res)
            freqs = np.fft.fftfreq(fft_res.size, 1 / SAMPLE_RATE)
            positive_mask = freqs > 0
            dom_freq_idx = np.argmax(magnitude[positive_mask])
            self.dom_freq = freqs[positive_mask][dom_freq_idx]
            self.nearest_neighbor()
            termClear()
            expt_freq = float(
                "{:.3f}".format(NOTES_TO_FREQ_DICT[self.nearest_note])
            )
            freq_diff = float("{:.3f}".format(expt_freq - self.dom_freq))
            if expt_freq > self.dom_freq:
                freq_diff *= -1
            print(
                f"Nearest note: {self.nearest_note}\n"
                f"Expected freq: {expt_freq}\n"
                f"Actual freq: {self.dom_freq}\n"
                f"{freqDifference(self.nearest_note, freq_diff)}\n"
                "CTRL+C to return to main menu!",
                end="\r",
            )
            self.frames_processed += frames
        else:
            print(
                "Waiting for you to play!\n"
                "If you are, make sure your device is plugged in.\n"
                "CTRL+C to return to main menu!",
                end="\r",
            )
            print()

    def autoStart(self):
        termClear()
        self.rec_dev_num, self.rec_dev_name, self.rec_dev_chnls = (
            selectRecordingDevice()
        )
        try:
            self.stream = sd.InputStream(
                samplerate=SAMPLE_RATE,
                blocksize=64,
                device=self.rec_dev_num,
                channels=self.rec_dev_chnls,
                callback=self.callback,
            )
            self.stream.start()
            sd.wait()
        except KeyboardInterrupt:
            if self.stream and self.stream.active:
                self.stream.stop()
                self.stream.close()
            return
