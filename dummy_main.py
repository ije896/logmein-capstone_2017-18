#!/usr/bin/env python3

import sys
from text import Interface

def main():
	try:
		text_file = sys.argv[1]
	except:
		print( "Usage: python3 {} input_file (max 128kB) ".format(sys.argv[0]) )
		exit(1)

	
	output = Interface.process_filepath(text_file, {'run_all':True})

	print(output)


if __name__ == '__main__':
	main()
