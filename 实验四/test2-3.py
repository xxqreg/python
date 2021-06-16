from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import SinSignal


square = SquareSignal(1500).make_wave(duration=0.5, framerate=10000)
square.plot()
plt.subplot()
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

square.make_audio()

SinSignal(500).make_wave(duration=0.5, framerate=10000).make_audio()
square.play("2-3.wav")


plt.show()