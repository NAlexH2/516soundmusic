import os
import numpy as np
import sounddevice as sd
import librosa
from scipy import fft
from .projGlobals import *


class AutomaticDetection:

    def autoStart(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("auto start")
