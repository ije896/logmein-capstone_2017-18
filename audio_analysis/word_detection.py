#general audio library
import librosa
#used for plotting
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

import json
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KernelDensity

from watson_developer_cloud import SpeechToTextV1

speech_file_long = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'

json_file = 'long_stt.json'

### We don't really need to dump to json file. Just pass the stt onto next method
def get_watson_STT(afile, out_file):
    speech_to_text = SpeechToTextV1(
    username='1e702356-275c-4f54-bf57-7c670774ea86',
    password='qEmrozAb1ug7',
    x_watson_learning_opt_out=False
    )
    print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

    with open(afile, 'rb') as audio_file:
        with open(out_file, 'w') as jfile:
            stt = speech_to_text.recognize(
                audio_file, content_type='audio/wav', timestamps=True,
                word_confidence=False)
            json.dump(stt, jfile)

### upper comment makes this method irrelevant
def load_json_stt_file(infile):
    with open(infile, 'r') as ifile:
        stt_json = json.load(ifile)
    return stt_json

# eventually pass just the stt json object
# returns structured list of list of timestamps(list)
# list of list of lists
def scrub_json(jfile):
    timestamps = []
    stt_json = load_json_stt_file(jfile)
    for phrase in stt_json['results']:
        timestamps.append(phrase['alternatives'][0]['timestamps'])
    return timestamps


# should return list of lists
def simplify_timestamps(timestamps):
    simple = []
    for phrase in timestamps:
        for word in phrase:
            simple.append(word)
    return simple

def get_word_count(timestamps):
    num_words = len(timestamps)
    return num_words

def get_len_sample(timestamps):
    start = timestamps[0][1]
    end = timestamps[-1][-1]
    length = end - start
    return length

def get_wpm(length, word_count):
    speech_in_mins = length/60
    wpm = word_count/speech_in_mins
    return round(wpm)

def get_transcript(timestamps):
    transcript = ""
    for word in timestamps:
        transcript += word[0] + " "
    return transcript

def get_word_times(timestamps):
    times = []
    for word in timestamps:
        mid = (word[2] + word[1])/2
        times.append(mid)
    return times



# best practice will probably be to return list of timestamps from json scrub
# then call methods on timestamps to extract script, length of speech, word count
def main():
    final = {}
    # get_watson_STT(speech_file_long, json_file)
    timestamps = scrub_json(json_file)
    simple_ts = simplify_timestamps(timestamps)
    wc = get_word_count(simple_ts)
    final['transcript'] = get_transcript(simple_ts)
    final['length'] = get_len_sample(simple_ts)
    final['wpm'] = get_wpm(final['length'], wc)
    print(final)

main()


# def cluster_words(times):
#     np_times = np.array(times)
#     words = np_times.reshape(-1, 1)
#
#     kde = KernelDensity(bandwidth = .3).fit(words)
#     plot = kde.score_samples(words)
#     print(plot)
#     plt.plot(plot, 'b-')
#     plt.show()
#
# # estimates the best fitting bandwidth for the function
# def grid_search_bandwidth():
#     return


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
