#!/usr/bin/env python3

import os
import sys
from text import WatsonAnalyzer
from text import tf_idf


# This class can be invoked with either the text itself
# or the relative path of the text file
class TextAnalysis:
	def __init__(self, text):
		self.script          = self.check_file(text)
		self.watson_analysis = WatsonAnalyzer(self.script)
		self.tfidf			 = tf_idf.TfIdf()

	def get_json(self):
		return self.watson_analysis.json

	def get_emotion(self):
		return self.watson_analysis.emotion

	def get_social(self):
		return self.watson_analysis.social

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

	def get_tf_idf(self):
		return self.tfidf.get_tf_idf(self.script)

	def get_tf_cf(self):
		return self.tfidf.get_tf_cf(self.script)


