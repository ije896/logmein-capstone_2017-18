#general audio library
import librosa
from librosa import display
import matplotlib.pyplot as plt
import pprint
import numpy

sine = '/Users/iegan/Downloads/440.wav'
major = '/Users/iegan/Downloads/major.wav'
cscale = '/Users/iegan/Downloads/c_scale.wav'
speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'

speech = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
y, sr = librosa.load(cscale)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
hop_length = 100

idx = (magnitudes>0)

onset_samples = librosa.onset.onset_detect(y,
                                         sr=sr, units='samples',
                                         hop_length=hop_length,
                                         backtrack=False,
                                         pre_max=20,
                                         post_max=20,
                                         pre_avg=100,
                                         post_avg=100,
                                         delta=0.2,
                                         wait=0)
onset_boundaries = numpy.concatenate([[0], onset_samples, [len(y)]])

inds = []
pitch = []

def detect_pitch(magnitudes, pitches, t):
  index = magnitudes[:, t].argmax()
  pitch = pitches[index, t]
  return pitch

def pip_track(magnitudes, pitches):
  global pitch
  for time in range(len(pitches[1])):
    p = detect_pitch(magnitudes, pitches, time)
    time *= 512 / sr
    pitch.append((time, p))

def estimate_pitch(segment, sr, fmin=50.0, fmax=2000.0):
  global hop_length
  r = librosa.autocorrelate(segment)
  # Define lower and upper limits for the autocorrelation argmax.
  i_min = sr/fmax
  i_max = sr/fmin
  r[:int(i_min)] = 0
  r[int(i_max):] = 0
  # Find the location of the maximum autocorrelation.
  i = r.argmax()
  f0 = float(sr)/i
  return f0

def estimate_pitch_for_segment(x, onset_samples, i, sr):
    n0 = onset_samples[i]
    n1 = onset_samples[i+1]
    f0 = estimate_pitch(x[n0:n1], sr)
    return f0
autocorred = []
for i in range(len(onset_boundaries)-1):
  autocorred.append((onset_samples[i-1],estimate_pitch_for_segment(y, onset_boundaries, i, sr=sr)))



plt.plot(autocorred)
plt.show()


#pip_track(magnitudes, pitches)
#print(pitch)

# zip(*pitch)
# plt.plot(*zip(*pitch))
# plt.show()

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
