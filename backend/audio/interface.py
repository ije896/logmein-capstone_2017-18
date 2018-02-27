import sys
import os
import json

from audio import word_detector as wd
from audio import pitch_detector as pd

# turn this into the audio analysis class
# speech_file = str(sys.argv[1])
class Interface:
    def __init__(self):
        self.word_detector = None
        self.pitch_detector = None

    def process_filepath(self, afile, options):
        word = False
        pitch = False
        for(opt, val) in options.items():
            if val:
                if opt == 'run_all':
                    word = True
                    pitch = True
                elif opt == 'word':
                    word = True
                elif opt == 'pitch':
                    pitch = True
        if word:
            self.word_detector = wd.WordDetector(afile)
        if pitch:
            self.pitch_detector = pd.PitchDetector(afile)
        return

    def get_speech_length(self):
        return self.word_detector.length_of_speech

    def get_word_count(self):
        return self.word_detector.word_count

    def get_transcript(self):
        return self.word_detector.transcript

    def get_avg_wpm(self):
        return self.word_detector.avg_wpm

    def get_phrase_wpms(self):
        return self.word_detector.phrase_wpms

    def get_cum_wpm(self):
        return self.word_detector.phrase_wpms

    def get_interval_wpm(self):
        return self.word_detector.interval_wpm

    def get_interval_lpm(self):
        return self.word_detector.interval_lpm

    def get_pitches(self):
        return self.pitch_detector.pitches

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=2)

# python -i test.py

# import interface
# a = interface.Interface()
# speech_file = '/Users/iegan/Documents/School/W18 Classes/CS189B/logmein-capstone_2017-18/audio_media/speech_sample.wav'

# import interface
# a = interface.Interface()
# speech_file = '/Users/iegan/Documents/School/W18 Classes/CS189B/logmein-capstone_2017-18/audio_media/speech_sample.wav'
# speech_file_short = '/Users/iegan/Documents/School/F17 Classes/CS189B/logmein-capstone_2017-18/audio_media/halloween.wav'
#
# opts = {'run_all':True}
#
# a.process_filepath(speech_file_short, opts)
