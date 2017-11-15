import sys
import os
import json

from audio_package import word_detection
# speech_file = str(sys.argv[1])

class Interface:
    def __init__(self):
        self.word_detector = None

    def process_filepath(self, afile, run_all=False, word_data=False):
        if run_all:
            word_data = True

        if word_data:
            self.word_detector = word_detection.word_detector(afile)

        return self.to_json()

    def get_speech_length(self):
        return self.word_detector.length_of_speech

    def get_word_count(self):
        return self.word_detector.word_count

    def get_transcript(self):
        return self.word_detector.transcript

    def get_wpm(self):
        return self.word_detector.wpm

    def get_phrase_wpms(self):
        return self.word_detector.phrase_wpms

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=2)

a = Interface()
speech_file = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'

a.process_filepath(speech_file, True)

print(a.get_transcript())
