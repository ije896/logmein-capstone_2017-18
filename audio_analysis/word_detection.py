import numpy as np
import matplotlib.pyplot as plt
import json
from watson_developer_cloud import SpeechToTextV1

speech_file_long = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/halloween.wav'
alec = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/alec_baldwin_malice.wav'
json_file = 'watson_transcript.json'

def get_watson_STT(afile):
    speech_to_text = SpeechToTextV1(
    username='1e702356-275c-4f54-bf57-7c670774ea86',
    password='qEmrozAb1ug7',
    x_watson_learning_opt_out=False
    )
    print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

    with open(afile, 'rb') as audio_file:
        stt = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            word_confidence=False)
    return stt

def load_json_stt_file(infile):
    with open(infile, 'r') as ifile:
        stt_json = json.load(ifile)
    return stt_json

def scrub_json(stt_json):
    timestamps = []
    simple = []
    for phrase in stt_json['results']:
        timestamps.append(phrase['alternatives'][0]['timestamps'])
        for word in phrase['alternatives'][0]['timestamps']:
            simple.append(word)
    return timestamps, simple

def get_word_count(timestamps):
    num_words = len(timestamps)
    return num_words

def get_length(timestamps):
    start = timestamps[0][1]
    end = timestamps[-1][-1]
    length = end - start
    return round(length, 2)

def get_phrase_time(phrase):
    start = phrase[0][1]
    end = phrase[-1][-1]
    mid = (start + end)/2
    return round(mid, 2)

def get_wpm(length, word_count):
    speech_in_mins = length/60
    wpm = word_count/speech_in_mins
    return round(wpm)

def get_phrase_wpms(timestamps):
    phrase_wpms = []
    avg = 0
    for phrase in timestamps:
        phrase_len = get_length(phrase) #phrase in mins
        wc = get_word_count(phrase)
        wpm = get_wpm(phrase_len, wc)
        time = get_phrase_time(phrase)
        tup = (time, wpm)
        phrase_wpms.append(tup)
    return phrase_wpms

def get_transcript(timestamps):
    transcript = ""
    for word in timestamps:
        transcript += word[0] + " "
    return transcript

def main():
    final = {}
    stt = get_watson_STT(speech_file_short)
    timestamps, simple_ts = scrub_json(stt)
    wc = get_word_count(simple_ts)
    final['transcript'] = get_transcript(simple_ts)
    final['length'] = get_length(simple_ts)
    final['wpm'] = get_wpm(final['length'], wc)
    final['phrase_wpms'] = get_phrase_wpms(timestamps)
    print(final)

main()
