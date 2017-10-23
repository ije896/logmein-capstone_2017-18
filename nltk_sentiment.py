#!/usr/bin/env python3

import os
import sys

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Make sure you have nltk downloaded (pip3 install nltk)
# Make sureyou have vader_lexicon downloaded (nltk.download('vader_lexicon'))
# 		I believe this has to be done in the repl


# USAGE:
# (1) pass in a file as argument that contains text to be analyzed
# (2) pass in no argument and be prompted for text


# Analysis using NLTK Vader Sentiment Analyzer
def nltkVaderAnalyzer(text):
	sid = SentimentIntensityAnalyzer()
	ss = sid.polarity_scores(text)
	print("pos: " + str(ss['pos']) + ", neu: " + str(ss['neu']) + ", neg: " + str(ss['neg']) + ", com: " + str(ss['compound']))

def main():
	print("Key: \n pos: \t positive tone \n neu: \t neutral tone \n neg: \t negative tone: \n com: \t overall user experience \n")
	
	try:
		file = open(sys.argv[1], 'r')
		text = file.read()
		file.close()

		nltkVaderAnalyzer(text)
	except:
		while(1):
			text = input("Enter the text you want to analyze, or 'done' to exit: ")
			if text == 'done':
				exit()

			nltkVaderAnalyzer(text)
			print()


if __name__ == '__main__':
	main()


