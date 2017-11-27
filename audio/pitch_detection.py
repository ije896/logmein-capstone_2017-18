#general audio library
import librosa
from librosa import display
import matplotlib.pyplot as plt
import pprint

sine = '/Users/iegan/Downloads/440.wav'
major = '/Users/iegan/Downloads/major.wav'
speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'

speech = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
y, sr = librosa.load(major)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

idx = (magnitudes>0)

inds = []
p = []

def detect_pitch(y, sr, t):
  index = magnitudes[:, t].argmax()
  pitch = pitches[index, t]

  return pitch


pos = 0
# pitches/magnitudes [bin f, time t]
for xind, x in enumerate(pitches):
    for val, val in enumerate(x):
            inds.append((pos, val))
            pos+=1

zip(*inds)

# for xind, x in enumerate(idx):
#     for yind, y in enumerate(x):
#             if y:
#                 inds.append([xind, yind])
# print(inds)

plt.plot(*zip(*inds))
plt.show()

# for val in inds:
#     #print(val[0], val[1])
#     p.append(pitches[val[0], val[1]])
# print(p)


# This displays the volume over the course of the speech

plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('Volume')

plt.show()
