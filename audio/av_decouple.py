import sys
import os
import subprocess

video_folder = '/Users/iegan/Documents/School/W18\ Classes/CS189B/logmein-capstone_2017-18/sample_videos/'
audio_folder = '/Users/iegan/Documents/School/W18\ Classes/CS189B/logmein-capstone_2017-18/audio_media/speech_audio/'
presentation_name = 'vurb_tc'
videoin = video_folder + presentation_name + '.mp4'
audioout = audio_folder + presentation_name + '.wav'
command = "ffmpeg -i "+ videoin + " -ab 160k -ac 2 -ar 44100 -vn " + audioout

subprocess.call(command, shell=True)
