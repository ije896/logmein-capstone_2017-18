import sys
import os
from .word_detection import word_detector
import json

# speech_file = str(sys.argv[1])

class audio_analyzer:
    def __init__(self, afile):
        self.word_detector = word_detector(afile)

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
