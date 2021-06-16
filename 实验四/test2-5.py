from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import SinSignal

def filter_spectrum(spectrum):

    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = TriangleSignal(freq=440).make_wave(duration=0.5)
wave.make_audio()

spectrum = wave.make_spectrum()
spectrum.plot(high=10000, color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

filtered = spectrum.make_wave()
filtered.make_audio()
filtered.play("2-5.wav")
plt.show()
