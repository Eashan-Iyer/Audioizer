import numpy as np
import math
import scipy.io.wavfile as wav
duration = 2  # in seconds
sampling_rate = 44100  # in Hz

time_array = np.linspace(0, duration, duration * sampling_rate, endpoint=False)

# Input the function you want to hear
function = lambda t: 300*((t-1)*np.sqrt(1-(t-1)**2)+np.arcsin(t-1))

vfunc = np.vectorize(function)

wave = np.sin(2 * np.pi * vfunc(time_array))

wav.write('compound_wave.wav', sampling_rate, wave)
