from pyaudio import PyAudio
import numpy as np
import sounddevice as sd
from projGlobals import *


class AutomaticDetection:

    def __init__(self):
        self.pitch = 0.0
        self.notes = list(NOTES_DICT.values())
        self.nearest_note = ""
        self.nearest_pitch = ""
        self.win_samples = np.zeros(SAMPLE_RATE, dtype=np.float32)
        self.rec_dev_num = None
        self.rec_dev_name = None

    def selectRecordingDevice(self):
        termClear()
        device_list = dict()
        p = PyAudio()
        info = p.get_host_api_info_by_index(host_api_index=0)
        for i in range(info.get("deviceCount")):
            if p.get_device_info_by_host_api_device_index(0, i).get(
                "maxInputChannels"
            ):
                devInfo = p.get_device_info_by_host_api_device_index(0, i)
                iInfo = devInfo.get("index")
                nInfo = devInfo.get("name")
                device_list[iInfo] = nInfo

        opt = -1
        conf = "n"
        while opt < 1 or opt > len(device_list) or conf != "Y".lower():
            print(
                "Select which device to use for live audio processing "
                "and note comparison: "
            )
            try:
                for d in range(len(device_list)):
                    print(f"   #{d+1} - Name: {device_list[d]}")
                opt = int(input("\nPlease enter which device number to use: "))
            except ValueError:
                opt = -1
                termClear()
                print("Invalid option...\n")
                continue
            if opt > len(device_list) or opt < 1:
                opt = -1
                termClear()
                print("Invalid option...\n")
                continue
            else:
                print(f"Selected device --> {device_list[opt-1]}.")
                conf = input("Is this correct? Y/N: ").lower()
                if conf != "y":
                    conf = "n"
                    termClear()
                    continue

        self.rec_dev_num = opt - 1
        self.rec_dev_name = device_list[opt - 1]
        return

    def nearest_neighbor(self):
        notes_len = len(self.notes)
        n = int(np.round((self.pitch / PITCH_CHECK) * notes_len))
        self.nearest_note = self.notes[n % notes_len]
        self.nearest_pitch = PITCH_CHECK * 2 ** (n / notes_len)
        return

    def callback(self, inputD: np.ndarray, frames, dur, state):
        if any(inputD):
            fft_res = np.fft.fft(inputD[:, 0])
            magnitude = np.abs(fft_res)
            freqs = np.fft.fftfreq(fft_res.size, 1 / SAMPLE_RATE)
            positive_mask = freqs > 0
            dom_freq_idx = np.argmax(magnitude[positive_mask])
            self.pitch = freqs[positive_mask][dom_freq_idx]
            self.nearest_neighbor()
            termClear()
            expt_freq = float(
                "{:.3f}".format(NOTES_TO_FREQ_DICT[self.nearest_note])
            )
            freq_diff = float("{:.3f}".format(expt_freq - self.pitch))
            print(
                f"Nearest note: {self.nearest_note}\n"
                f"Expected freq: {expt_freq}\n"
                f"Actual freq: {self.pitch}\n"
                f"{freqDifference(self.nearest_note, freq_diff)}"
            )
        else:
            print("Waiting for you to play!")
        print("CTRL+C to return to main menu!")

    def autoStart(self):
        termClear()
        self.selectRecordingDevice()
        try:
            with sd.InputStream(
                samplerate=SAMPLE_RATE,
                blocksize=SAMPLE_RATE,
                device=self.rec_dev_num,
                channels=1,
                callback=self.callback,
            ):
                while True:
                    pass
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    ad = AutomaticDetection()
    ad.autoStart()
