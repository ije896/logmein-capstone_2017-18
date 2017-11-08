#!/usr/bin/env python3

import sys
import os
from Text_Analysis import text_module


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
	ta = text_module(text_file)
	'''
	json = ta.get_json()
	emotion = ta.get_emotion()
	social = ta.get_social()
	freq = ta.get_freq()

	print(json)
	print(emotion)
	print(social)
	print(freq)
	'''
	idf_syns = ta.get_top5_idf_syns()
	cf_syns = ta.get_top5_cf_syns()
	print("Here are the top 5 TF-IDF Synonyms: \n")
	print(idf_syns)
	print("Here are the top 5 TF-CF Synonyms: \n")
	print(cf_syns)



if __name__ == '__main__':
	main()
