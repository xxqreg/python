import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import read_wave

wave = read_wave('G:\学习\python1xxq\python\实验五\\72475__rockwehrmann__glissup02.wav')
wave.make_audio()
wave.play('3-4.wav')
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()