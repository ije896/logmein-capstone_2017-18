#!/usr/bin/env python3

import sys
import os
import subprocess
import pickle

from text import Interface as t_int
from audio import Interface as a_int
from Video import Interface as v_int

def av_decouple(video_file):
	audio_file = video_file[:-4] + '.wav'
	command = "ffmpeg -i "+ video_file + " -ab 160k -ac 2 -ar 44100 -vn " + audio_file
	subprocess.call(command, shell=True)
	return audio_file


t = t_int()
a = a_int()
v = v_int()

def main():
	try:
		#text_file = sys.argv[1]
		#audio_file = sys.argv[1]
		video_file = sys.argv[1]
	except:
		print( "Usage: python3 {} input_file [max 128kB] ".format(sys.argv[0]) )
		exit(1)

	# t = t_int.Interface()
	# a = a_int.Interface()
	# v = v_int.Interface()


	# Holding off on this so I can just analyze pre cut 2min video
	#audio_file = av_decouple(video_file)
	# audio_file = 'media/enigma_tc/enigma_tc_crop.wav'
	audio_file = 'media/isaiah_enigma_tc/isaiah_enigma_tc.wav'
	#audio_file = 'audio_media/nonsense.wav'

	a.process_filepath(audio_file, {'run_all': True})
	#v_json = v.process_filepath(video_file, {'run_all': True})

	with open('media/isaiah_enigma_tc/isaiah_enigma_tc.pkl', 'wb') as output:
		pickle.dump(a, output, pickle.HIGHEST_PROTOCOL)

	fd = open('media/isaiah_enigma_tc/isaiah_enigma_tc.txt', 'w')
	fd.write(a.to_json())
	fd.close()

	#print(v_json)

	#text_file = a.get_transcript()
	#t.prcoess_filepath(text_file, {'run_all': True})




	#output = t.process_filepath(text_file, {'run_all': True})

	# a = Interface()
	# print("Opened interface")
	# output = a.process_filepath(audio_file, {'word': True})
	# print("Processed filepath")
	#
	# print(a.get_transcript())
	# print("Finished outputting transcript")

if __name__ == '__main__':
	main()
