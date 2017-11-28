#general audio library
import librosa
from librosa import display
import matplotlib.pyplot as plt
import pprint

sine = '/Users/iegan/Downloads/440.wav'
major = '/Users/iegan/Downloads/major.wav'
speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'

speech = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
y, sr = librosa.load(sine)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

idx = (magnitudes>0)

print("idx:", pitches[idx])


inds = []
pitch = []

def detect_pitch(magnitudes, pitches, t):
  index = magnitudes[:, t].argmax()
  pitch = pitches[index, t]
  return pitch

for time in range(len(pitches[1])):
  p = detect_pitch(magnitudes, pitches, time)
  time *= 512 / sr
  pitch.append((time, p))

print(pitch)

#zip(*pitch)
#print("zipped:", pitch)
#plt.plot(*zip(*pitch))
#plt.show()

# pos = 0
# # pitches/magnitudes [bin f, time t]
# for xind, x in enumerate(pitches):
#     for val, val in enumerate(x):
#             inds.append((pos, val))
#             pos+=1
#
# zip(*inds)
#
# plt.plot(*zip(*inds))
# plt.show()
