#!/usr/bin/env python3

import os
import sys
from text import synonyms
from text import readability
from text import tf_idf
from text import watson


# This class can be invoked with either the text itself
# or the relative path of the text file
class TextAnalysis:
	def __init__(self, fp):
		self.script = self.check_file(fp)
		self.syn = synonyms.Synonyms()

	def get_sentiment(self):
		tones = watson.WatsonAnalyzer.get_sentiment(self.script)
		sentiment = {'sentiment': tones}
		return sentiment

	def get_synonyms(self):
		tfidf = tf_idf.TfIdf.get_tf_idf(self.script)

		syns = {}
		idf_index = 0
		while len(syns) < 5 and idf_index < len(tfidf):
			word = tfidf[idf_index]
			synonym = self.syn.get_syns(word)
			if synonym != -1:
				syns[word] = synonym
			idf_index += 1
		syn_list = {'synonyms': syns}
		return syn_list

	def get_readability(self):
		score = readability.Readability.f_k(self.script)
		grade = readability.Readability.f_k_grade_level(self.script)

		read_list = {'score': score, 'grade': grade}
		read = {'readability': read_list}
		return read

	# Temporary function for demo purposes, can eat later
	@staticmethod
	def output_readability_tests():
		readability.Readability.output_tests()

	@staticmethod
	def check_file(data):
		# Try to open it as a file
		try:
			file_object = open(data, 'r')
			text = file_object.read()
			file_object.close()
			return text
		# If the file doesn't exist, then assume we were given the text_fail
		except:
			return data
