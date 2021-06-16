from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal

class SawtoothSignal(Sinusoid):

    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys


sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
sawtooth.make_audio()
plt.subplot(2,2,1)
sawtooth.plot()
plt.subplot(2,2,2)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

sawtooth.make_spectrum().plot(color='gray')
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
plt.subplot(2,2,3)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')


sawtooth.make_spectrum().plot(color='gray')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
plt.subplot(2,2,4)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

plt.show()

