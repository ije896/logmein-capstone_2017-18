#general audio library
import librosa
from librosa import display
import matplotlib.pyplot as plt

sine = '/Users/iegan/Downloads/440.wav'
speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'

speech = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
y, sr = librosa.load(speech_file_short)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('Volume')

plt.show()
