#general audio library
import librosa
from librosa import display
import matplotlib.pyplot as plt
speech = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
y, sr = librosa.load(speech)

plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('Volume')

plt.show()
