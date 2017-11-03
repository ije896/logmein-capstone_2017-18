#general audio library
import librosa
#used for plotting
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
#used for rw of onset times to files
import json
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KernelDensity

from watson_developer_cloud import SpeechToTextV1

#differences = []

#speech_file = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
speech_file = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'

json_file = 'watson_transcript.json'

def get_watsonSTT(out_file):
    speech_to_text = SpeechToTextV1(
    username='1e702356-275c-4f54-bf57-7c670774ea86',
    password='qEmrozAb1ug7',
    x_watson_learning_opt_out=False
    )

    print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

    with open(speech_file, 'rb') as audio_file:
        with open(out_file, 'w') as jfile:
            stt = speech_to_text.recognize(
                audio_file, content_type='audio/wav', timestamps=True,
                word_confidence=True)
            json.dump(stt, jfile)

# get_watsonSTT(json_file)

def load_json_stt_file(infile):
    with open(infile, 'r') as ifile:
        data = json.load(ifile)
    return data

def get_word_count(stt_json):
    transcript = stt_json['results'][0]['alternatives'][0]['transcript'].split()
    num_words = len(transcript)
    return num_words

def get_len_speech(stt_json):
    start = stt_json['results'][0]['alternatives'][0]['timestamps'][0][1]
    end = stt_json['results'][0]['alternatives'][0]['timestamps'][-1][-1]
    length = end - start
    return(length)

def calc_wpm(infile):
    data = load_json_stt_file(infile)
    num_of_words = get_word_count(data)
    speech_in_secs = get_len_speech(data)
    speech_in_mins = speech_in_secs/60
    wpm = num_of_words/speech_in_mins
    print(wpm)

def cluster_onsets(infile):
    times = load_json_stt_file(infile)
    print(len(times))
    np_times = np.array(times)
    onsets = np_times.reshape(-1, 1)

    kde = KernelDensity(bandwidth = .3).fit(onsets)
    plot = kde.score_samples(onsets)
    print(plot)
    plt.plot(plot, 'b-')
    plt.show()

# estimates the best fitting bandwidth for the function
def grid_search_bandwidth():
    return

def main():



# def calc_onset_times(afile, out_file):
#     y, sr = librosa.load(afile)
#
#     #tempo, pulse_frames = librosa.beat.beat_track(y=y, sr=sr)
#     onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
#     onset_times = librosa.frames_to_time(onset_frames, sr=sr)
#
#     print("onsets: ", onset_times)
#
#     formatted = onset_times.tolist()
#     with open(out_file, 'w') as jfile:
#         json.dump(formatted, jfile)
#     return onset_times
#
# def plot_onsets():
#     o_env = librosa.onset.onset_strength(y, sr=sr)
#     times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr)
#     onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
#
#     D = librosa.stft(y)
#     plt.figure()
#     ax1 = plt.subplot(2, 1, 1)
#     librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
#                              x_axis='time', y_axis='log')
#     plt.title('Power spectrogram')
#     plt.subplot(2, 1, 2, sharex=ax1)
#     plt.plot(times, o_env, label='Onset strength')
#     plt.vlines(times[onset_frames], 0, o_env.max(), color='r', alpha=0.9,
#                linestyle='--', label='Onsets')
#     plt.axis('tight')
#     plt.legend(frameon=True, framealpha=0.75)
#
#     plt.show()

# calc_onset_times(speech_file, json_file)
