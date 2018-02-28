import sys
import os
import subprocess

video_folder = '/Users/user/CS189A\:B/logmein-capstone_2017-18/research/'
audio_folder = '/Users/user/CS189A\:B/logmein-capstone_2017-18/research/'
presentation_name = 'enigma_rkemper_take2'
videoin = video_folder + presentation_name + '.mov'
audioout = audio_folder + presentation_name + '.wav'
command = "ffmpeg -i "+ videoin + " -ab 160k -ac 2 -ar 44100 -vn " + audioout
#crop_cmd = "ffmpeg -i " + videoin + " -ss 00:00:03 -t 00:00:08 -async 1 " + crop_out


subprocess.call(command, shell=True)
