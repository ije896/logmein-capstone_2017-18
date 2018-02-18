import sys
import os
import subprocess

folder = '/Users/iegan/Documents/School/W18\ Classes/CS189B/logmein-capstone_2017-18/audio_media/'
videoin = folder + 'decouple_me.mov'
audioout = folder + 'audio.wav'
command = "ffmpeg -i "+ videoin + " -ab 160k -ac 2 -ar 44100 -vn " + audioout

subprocess.call(command, shell=True)

#audio = mp.AudioFileClip(fp)
