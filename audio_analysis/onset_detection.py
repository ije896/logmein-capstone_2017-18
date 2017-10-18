import librosa

afile = librosa.util.example_audio_file()

wave, sr = librosa.load(filename)

tempo, pulse_frames = librosa.beat.beat_track(y=y, sr=sr)

# 4. Convert the frame indices of beat events into timestamps
onset_times = librosa.frames_to_time(pulse_frames, sr=sr)

print(onset_times)
