from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
from pylab import*

points=300
samplerate, data = wavfile.read('triangle500hz.wav')
data=data/(7787.)
timeArray = arange(0, points, 1)
timeArray = timeArray/float(samplerate)
plot(timeArray, data[0:points])
ylabel('Amplitud')
xlabel('Tiempo (ms)')
