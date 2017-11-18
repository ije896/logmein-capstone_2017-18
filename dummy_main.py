#!/usr/bin/env python3

import sys
from text import Interface

def main():
	try:
		text_file = sys.argv[1]
	except:
		print("Usage: python3 %s input_file (max 128kB) ", sys.argv[0])
		exit(1)

	#file_object = open(text_file, 'r')
	#text_fail = file_object.read()
	#file_object.close()

	# This can be called with either the text_fail file or the text_fail itself
	ta = Interface()
	
	output = ta.processFilepath(text_file, {'run_all':True})

	print(output)


if __name__ == '__main__':
	main()
