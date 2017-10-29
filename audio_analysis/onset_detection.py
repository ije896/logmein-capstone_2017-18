#general audio library
import librosa
#used for plotting
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
#used for rw of onset times to files
import csv
import json


#differences = []

speech_file = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
    #librosa.util.example_audio_file()

csv_file = 'onset_times.csv'
json_file = 'onset_times.json'

def calc_onset_times(afile, out_file):
    y, sr = librosa.load(afile)

    #tempo, pulse_frames = librosa.beat.beat_track(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    # for i in range(len(onset_times)-1):
    #     tmp = onset_times[i+1] - onset_times[i]
    #     differences.append(tmp)

    print("onsets: ", onset_times)
    #print("differences: ", differences)

    # with open(out_file, 'w') as cfile:
    #     wr = csv.writer(cfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(onset_times)
    formatted = onset_times.tolist()
    with open(out_file, 'w') as jfile:
        json.dump(formatted, jfile)
    return onset_times

def calc_wpm(infile):
    with open(infile, 'r') as ifile:
        times = json.load(ifile)
    num_of_words = len(times)
    len_of_speech = times[num_of_words-1] - times[0]
    speech_in_mins = len_of_speech/60
    wpm = num_of_words/speech_in_mins
    print(wpm)

calc_wpm(json_file)

def plot_onsets():
    o_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

    D = librosa.stft(y)
    plt.figure()
    ax1 = plt.subplot(2, 1, 1)
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                             x_axis='time', y_axis='log')
    plt.title('Power spectrogram')
    plt.subplot(2, 1, 2, sharex=ax1)
    plt.plot(times, o_env, label='Onset strength')
    plt.vlines(times[onset_frames], 0, o_env.max(), color='r', alpha=0.9,
               linestyle='--', label='Onsets')
    plt.axis('tight')
    plt.legend(frameon=True, framealpha=0.75)

    plt.show()

# calc_onset_times(speech_file, json_file)
