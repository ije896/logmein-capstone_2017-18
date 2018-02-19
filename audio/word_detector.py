import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import json
from watson_developer_cloud import SpeechToTextV1

class WordDetector:
    def __init__(self, afile):
        self.time_inc = 2
        results = self.run_word_detection(afile)
        self.transcript = results['transcript']
        self.word_count = results['wc']
        self.length_of_speech = results['length']
        self.avg_wpm = results['wpm']
        self.cum_wpm = results['cum_wpm']
        self.phrase_wpms = results['phrase_wpms']
        self.interval_lpm = results['interval_lpm']
        self.interval_wpm = results['interval_wpm']


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
        timestamps = [] # the list of phrases
        simple = [] # the list of words, still with timestamps
        for phrase in stt_json['results']:
            timestamps.append(phrase['alternatives'][0]['timestamps'])
            for word in phrase['alternatives'][0]['timestamps']:
                simple.append([word[0], word[2]]) # word, endtime
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

    def calc_avg_wpm(self, length, word_count):
        speech_in_mins = length/60
        wpm = word_count/speech_in_mins
        return round(wpm)

    def calc_cum_wpm(self, simple, interval):
        wpm = []
        word_count = 0
        last_time = 0
        time_acc = interval
        for word in simple:
            if(word[1]>=time_acc):
                if(last_time!=0):
                    wpm.append([last_time, word_count/(last_time/60)])
                time_acc += interval
            word_count+=1
            last_time = word[1]
        wpm.append([last_time, word_count/(last_time/60)])
        return wpm

    def calc_interval_wpm(self, simple, interval):
        wpm = []
        time_acc = interval
        word_count = 0
        for word in simple:
            if(word[1]>=time_acc):
                wpm.append([time_acc, word_count/(interval/60)])
                time_acc+=interval
                word_count = 0
            word_count+=1
        if(word_count!=0):
            final_time = simple[-1][1]
            final_interval = final_time - (time_acc - interval)
            wpm.append([final_time, word_count/(final_interval/60)])
        return wpm

    def calc_interval_lpm(self, simple, interval):
        lpm = []
        time_acc = interval
        letter_count = 0
        for word in simple:
            if(word[1]>=time_acc):
                lpm.append([time_acc, letter_count/(interval/60)])
                time_acc+=interval
                letter_count = 0
            letter_count+=len(word[0])
        if(letter_count!=0):
            final_time = simple[-1][1]
            final_interval = final_time - (time_acc - interval)
            lpm.append([final_time, letter_count/(final_interval/60)])
        return lpm

    def calc_phrase_wpms(self, timestamps):
        phrase_wpms = []
        avg = 0
        for phrase in timestamps:
            phrase_len = self.calc_length(phrase) #phrase in mins
            wc = self.calc_word_count(phrase)
            wpm = self.calc_avg_wpm(phrase_len, wc)
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
        final['wpm'] = self.calc_avg_wpm(final['length'], wc)
        final['cum_wpm'] = self.calc_cum_wpm(simple_ts, 2)
        final['interval_wpm'] = self.calc_interval_wpm(simple_ts, 2)
        final['interval_lpm'] = self.calc_interval_lpm(simple_ts, 2)
        final['phrase_wpms'] = self.calc_phrase_wpms(timestamps)
        return final


# wd = WordDetector()

#
# with open('nonsense_object.pkl', 'wb') as output:
#     pickle.dump(a.word_detector.data, output, pickle.HIGHEST_PROTOCOL)
#
# with open('stt_object.pkl', 'rb') as input:
#     mine = pickle.load(input)
