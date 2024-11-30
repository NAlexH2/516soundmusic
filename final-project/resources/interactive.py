import numpy as np
import sounddevice as sd
import librosa
from scipy import fft
from .projGlobals import *


class InteractiveDetection:

    def interStart(self):
        termClear()
        print("inter start")
