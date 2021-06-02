import matplotlib.pyplot as plt
from IPython.core.display import publish_display_data
from thinkdsp import read_wave

wave = read_wave('g:/学习/python1xxq/python/实验三/170255__dublie__trumpet.wav')
wave.normalize()
wave.make_audio()


wave.plot()
plt.show()





segment = wave.segment(start=1.1, duration=0.3)
segment.make_audio()
segment.plot()
plt.show()

segment.segment(start=1.1, duration=0.005).plot()
plt.show()


spectrum = segment.make_spectrum()
spectrum.plot(high=7000)
plt.show()


spectrum = segment.make_spectrum()
spectrum.plot(high=1000)
plt.show()

spectrum.peaks()[:30]

spectrum.low_pass(2000)

spectrum.make_wave().make_audio()


