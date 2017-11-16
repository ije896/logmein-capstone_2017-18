#!/usr/bin/env python3

import sys
import os
from text import Interface


def main():
	try:
		text_file = sys.argv[1]
	except:
		print("Usage: python3 %s input_file (max 128kB) ", sys.argv[0])
		exit(1)

	#file_object = open(text_file, 'r')
	#text = file_object.read()
	#file_object.close()

	# This can be called with either the text file or the text itself
	ta = Interface()
	
	output = ta.processFilepath(text_file, run_all=True)

	print(output)

	'''
	json = ta.get_json()
	emotion = ta.get_emotion()
	social = ta.get_social()

	print(json)
	print(emotion)
	print(social)
	
	idf_syns = ta.get_top5_idf_syns()
	cf_syns = ta.get_top5_cf_syns()
	print("\nAnalyzing {}:\n".format(text_file))
	print("Here are the top 5 TF-IDF Synonyms: \n")
	print(idf_syns)
	print("\nHere are the top 5 TF-CF Synonyms: \n")
	print(cf_syns)

	ta.output_readability_tests()
	'''


if __name__ == '__main__':
	main()
