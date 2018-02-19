#!/usr/bin/env python3

import sys
#from text import Interface
from audio import Interface

def main():
	try:
		#text_file = sys.argv[1]
		audio_file = sys.argv[1]
	except:
		print( "Usage: python3 {} input_file [max 128kB] ".format(sys.argv[0]) )
		exit(1)

	#t = Interface()

	#output = t.process_filepath(text_file, {'run_all': True})

	a = Interface()
	print("Opened interface")
	output = a.process_filepath(audio_file, {'word': True})
	print("Processed filepath")

	print(a.get_transcript())
	print("Finished outputting transcript")

if __name__ == '__main__':
	main()
