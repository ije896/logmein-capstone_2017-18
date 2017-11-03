#!/usr/bin/env python3

import os
import sys
from Text_Analysis import watson_analyzer

# Watson Tone (Sentiment) Analysis
	# json object
	# emotion dictionary
	# social dictionary
# Word Frequency
# Synonym Lookup

# This class can be invoked with either the text itself
# or the relative path of the text file
class text_analysis:
	def __init__(self, text):
		self.script          = self.check_file(text)
		self.watson_analysis = watson_analyzer(self.script)
		self.freq            = self.word_frequency()

	def get_json(self):
		return self.watson_analysis.json

	def get_emotion(self):
		return self.watson_analysis.emotion

	def get_social(self):
		return self.watson_analysis.social

	def get_freq(self):
		return self.freq

	def check_file(self, data):
		# Try to open it as a file
		try:
			file_object = open(data, 'r')
			text = file_object.read()
			file_object.close()
			return text
		# If the file doesn't exist, then assume we were given the text
		except:
			return data

	def word_frequency(self):
		# Remove unnecessary punctuation from the text
		simple_text = self.script.replace('\n', ' ')

		punctuation = ['.', ',', '!', '?', '(', ')', '$', '"', '#', ';', ':']
		for item in punctuation:
			simple_text = simple_text.replace(item, '')

		words = simple_text.split(' ')

		d = {word: words.count(word) for word in words}
		# Don't need the extra spaces
		try:
			del d['']
		# If there isn't a space key in the dictionary
		# We don't need to worry, pass
		except:
			pass
		sort = [(word, d[word]) for word in sorted(d, key=d.get, reverse=True)]
		return sort
