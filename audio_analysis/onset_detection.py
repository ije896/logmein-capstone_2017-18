import librosa
import numpy as np

differences = []

afile = librosa.util.example_audio_file()

y, sr = librosa.load(afile)

tempo, pulse_frames = librosa.beat.beat_track(y=y, sr=sr)

onset_times = librosa.frames_to_time(pulse_frames, sr=sr)
for i in range(len(onset_times)-1):
    tmp = onset_times[i+1] - onset_times[i]
    differences.append(tmp)

print("onsets: ", onset_times)
print("differences: ", differences)
