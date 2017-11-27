import sys
import os
import json

from audio import audio_analysis

# speech_file = str(sys.argv[1])
class Interface:
    @staticmethod
    def process_filepath(afile, options):
        word = False
        pitch = False
        aa = audio_analysis.AudioAnalyzer(afile)

        for(key, val) in options.items()
            if val:
                if opt == 'run_all':
                    word = True
                    pitch = True
                elif opt == 'word':
                    word = True
                elif opt == 'pitch':
                    pitch = True

        return aa.to_json()

a = Interface()
speech_file = '/Users/iegan/Documents/School/F17 Classes/CS189A/logmein-capstone_2017-18/audio_samples/speech_sample.wav'
opts = {'word':True}
