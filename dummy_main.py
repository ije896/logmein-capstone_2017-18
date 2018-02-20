#!/usr/bin/env python3

import sys
from text import Interface as TextInterface
from audio import Interface as AudioInterface

def main():
	try:
		text_file = "research/enigma_tc_transcript.txt"
		#text_file = sys.argv[1]
		#audio_file = sys.argv[1]
	except:
		print( "Usage: python3 {} input_file [max 128kB] ".format(sys.argv[0]) )
		exit(1)

	t = TextInterface()
	print("Opened TextInterface")
	output = t.process_filepath(text_file, {'art': True})
	print("Processed text filepath")



	# a = AudioInterface()
	# print("Opened Audiointerface")
	# output = a.process_filepath(audio_file, {'word': True})
	# print("Processed audio filepath")

	# print(a.get_transcript())
	# print("Finished outputting transcript")

if __name__ == '__main__':
	main()
