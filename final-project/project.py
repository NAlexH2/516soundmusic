import numpy as np
import sounddevice as sd
import librosa
import matplotlib
from scipy import fft


# This project is going to be a tuner with several options. Specifically, for a
# guitar.

# First is automatic detection. FFT and analyzing peak freqs for the value
# received, and detecting it's closest value.

# Second is to generate a standing wave of specific frequencies

# Third is going to be interactive to select which note and measure what was
# received and give a good or negative response indicating if it was close enough
# or way off. Floating point value +/- of how far off it was?


if __name__ == "__main__":
    print("I am main!")
    exit()
