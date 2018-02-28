#general audio library
import librosa
from librosa import display
import matplotlib.pyplot as plt
import pprint
import numpy as np

class PitchDetector:
  def __init__(self, afile):
    pit = self.run_pitch_detection(afile)
    for i in range(len(pit)):
      pit[i] = (pit[i][0], int(pit[i][1]))
    self.pitches = pit
  def run_pitch_detection(self, afile):
    hop_length = 100
    y, sr = librosa.load(afile)
    onset_samples, onset_boundaries, onset_times = self.calc_onset_values(y, sr, hop_length)
    autocorred = self.autocorrelate_detect_pitch(y, sr, onset_boundaries, onset_times)
    final = self.combine_pitches_and_times(onset_times, autocorred)
    return final

  def calc_onset_values(self, y, sr, hop_length):
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
    onset_boundaries = np.concatenate([[0], onset_samples, [len(y)]])
    onset_times = librosa.samples_to_time(onset_boundaries)
    return onset_samples, onset_boundaries, onset_times

  def estimate_pitch(self, segment, sr, fmin=50.0, fmax=2000.0):
    global hop_length
    r = librosa.autocorrelate(segment)
    i_min = sr/fmax
    i_max = sr/fmin
    r[:int(i_min)] = 0
    r[int(i_max):] = 0
    i = r.argmax()
    f0 = float(sr)/i
    return int(f0)

  def reject_outliers(self, data, indeces, m = 2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m], indeces[s<m]

  def set_and_estimate_segment(self, x, onset_samples, i, sr):
    n0 = onset_samples[i]
    n1 = onset_samples[i+1]
    f0 = self.estimate_pitch(x[n0:n1], sr)
    return f0

  def autocorrelate_detect_pitch(self, y, sr, onset_boundaries, onset_times):
    autocorred = []
    for i in range(len(onset_boundaries)-1):
      autocorred.append(self.set_and_estimate_segment(y, onset_boundaries, i, sr=sr))
    autocorred = np.asarray(autocorred)
    return autocorred

  def combine_pitches_and_times(self, onset_times, autocorred):
    onset_times = np.delete(onset_times, 0, 0)
    autocorred, onset_times = self.reject_outliers(autocorred, onset_times)

    final = list(zip(onset_times, autocorred))
    return final

  # returns tuple of (time, frequency)
  def pip_track(self, magnitudes, pitches):
    pitch = []
    for time in range(len(pitches[1])):
      p = pip_detect_pitch(magnitudes, pitches, time)
      time *= 512 / sr
      pitch.append((time, p))
    return pitch

  def pip_detect_pitch(self, magnitudes, pitches, t):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]
    return pitch