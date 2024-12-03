from time import sleep
import numpy as np
import pyaudio
from pyaudio import PyAudio, Stream, get_format_from_width
from .projGlobals import *


class InteractiveDetection:
    def __init__(self) -> None:
        self.rec_dev_num = None
        self.rec_dev_name = None
        self.note = -1
        self.buffer_size = 1024
        self.chunks = SAMPLE_RATE // self.buffer_size
        self.sound = np.empty(
            (self.chunks * self.buffer_size), dtype=np.float32
        )
        self.stream = None

    def recAudio(self):
        to_sleep = 2
        print(f"Recording will start in {to_sleep} seconds...")
        sleep(to_sleep)
        print(f"Recording {STANDING_DUR} seconds of audio...")
        self.stream.start_stream()
        audio = self.stream.read(SAMPLE_RATE * STANDING_DUR)
        self.stream.stop_stream()
        audio = np.frombuffer(audio, dtype=np.float32)
        print(f"\nRecording finished!")
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
                positive_mask = freqs > 0
                dom_freq_idx = np.argmax(magnitude[positive_mask])
                if test_freq == 82.41:
                    dom_freq = (freqs[positive_mask][dom_freq_idx]) / 2
                else:
                    dom_freq = freqs[positive_mask][dom_freq_idx]
                dom_freq = float("{:.3f}".format(dom_freq))
                print(f"\nExpected frequency: {test_freq}")
                print(f"Recored frequency: {dom_freq}")
                diff_freq = abs(float("{:.3f}".format(test_freq - dom_freq)))
                if test_freq > dom_freq:
                    diff_freq *= -1
                print(freqDifference(test_note, diff_freq))

            elif conf == "n":
                return
            else:
                termClear()
                conf = "n"
                print("Input Error: Only Y or N please...\n")
            again = input(
                "\nRecord same note or a different one? S/D: "
            ).lower()
        return

    def interStart(self):
        self.rec_dev_num, self.rec_dev_name = selectRecordingDevice()
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
                if self.stream:
                    self.stream.close()
                return
            self.stream = PyAudio().open(
                format=pyaudio.paFloat32,
                rate=SAMPLE_RATE,
                input_device_index=self.rec_dev_num,
                input=True,
                channels=1,
                frames_per_buffer=self.buffer_size,
            )
            self.compareNote()
            termClear()
            print(
                f"No longer comparing against {NOTES_DICT.get(opt)} "
                + "note standing wave tone.\n"
            )
            if self.stream.is_active():
                self.stream.stop_stream()
            opt = -1
            self.note = -1
