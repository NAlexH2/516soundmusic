import os
import numpy as np
import sounddevice as sd
import librosa
from scipy import fft
from .projGlobals import *


class InteractiveDetection:

    def interStart(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("inter start")
