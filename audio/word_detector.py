import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import json
from watson_developer_cloud import SpeechToTextV1

class WordDetector:
    def __init__(self, afile):
        results = self.run_word_detection(afile)
        self.transcript = results['transcript']
        self.word_count = results['wc']
        self.length_of_speech = results['length']
        self.wpm = results['wpm']
        self.phrase_wpms = results['phrase_wpms']

    def calc_watson_STT(self, afile):
        speech_to_text = SpeechToTextV1(
        username= "4c2c6f6c-d4ef-4458-b479-98bc900320f2",
        password= "BKNAbarogTNu",
        x_watson_learning_opt_out=False
        )
        print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

        with open(afile, 'rb') as audio_file:
            stt = speech_to_text.recognize(
                audio_file, content_type='audio/wav', timestamps=True,
                word_confidence=False)
        return stt

    def scrub_json(self, stt_json):
        timestamps = []
        simple = []
        for phrase in stt_json['results']:
            timestamps.append(phrase['alternatives'][0]['timestamps'])
            for word in phrase['alternatives'][0]['timestamps']:
                simple.append(word)
        return timestamps, simple

    def calc_word_count(self, timestamps):
        num_words = len(timestamps)
        return num_words

    def calc_length(self, timestamps):
        start = timestamps[0][1]
        end = timestamps[-1][-1]
        length = end - start
        return round(length, 2)

    def calc_phrase_time(self, phrase):
        start = phrase[0][1]
        end = phrase[-1][-1]
        mid = (start + end)/2
        return round(mid, 2)

    def calc_wpm(self, length, word_count):
        speech_in_mins = length/60
        wpm = word_count/speech_in_mins
        return round(wpm)

    def calc_phrase_wpms(self, timestamps):
        phrase_wpms = []
        avg = 0
        for phrase in timestamps:
            phrase_len = self.calc_length(phrase) #phrase in mins
            wc = self.calc_word_count(phrase)
            wpm = self.calc_wpm(phrase_len, wc)
            time = self.calc_phrase_time(phrase)
            tup = (time, wpm)
            phrase_wpms.append(tup)
        return phrase_wpms

    def calc_transcript(self, timestamps):
        transcript = ""
        for word in timestamps:
            transcript += word[0] + " "
        return transcript

    def run_word_detection(self, sfile):
        final = {}
        stt = self.calc_watson_STT(sfile)
        timestamps, simple_ts = self.scrub_json(stt)
        wc = self.calc_word_count(simple_ts)
        final['transcript'] = self.calc_transcript(simple_ts)
        final['wc'] = wc
        final['length'] = self.calc_length(simple_ts)
        final['wpm'] = self.calc_wpm(final['length'], wc)
        final['phrase_wpms'] = self.calc_phrase_wpms(timestamps)
        return final
