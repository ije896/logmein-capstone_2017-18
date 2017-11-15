#!/usr/bin/env python3

import os
import sys
import json

from .text_package import synonym_analysis
from .text_package import text_analysis
from .text_package import readability_analysis

class Interface:
	def __init__(self):
		self.sent 	 = None
		self.syns 	 = None
		self.read    = None

		self.sentiment_list   = None
		self.synonym_list     = None
		self.readability_list = None
		self.json             = None

	def processFilepath(self, text, run_all=False, sentiment=False, synonyms=False, readability=False):
		script = self.check_file(text)
		if run_all:
			sentiment   = True
			synonyms    = True
			readability = True

		json_list = []
		if sentiment:
			self.sent    = text_analysis(script)
			emotion_dict = self.get_emotion
			social_dict  = self.get_social

			self.sentiment_list = {'emotion':emotion_dict, 'social':social_dict}
			json_list.append(self.sentiment_list)

		if synonyms:
			self.syns         = synonym_analysis()
			self.synonym_list = self.get_synonyms()

			json_list.append(self.synonym_list)

		if readability:
			self.read  = readability_analysis()
			read_grade = self.get_readability_grade(script)
			read_score = self.get_readability_score(script)

			self.readability_list = {'grade': read_grade, 'score': read_score}
			json_list.append(self.readability_list)

		self.json = json.dumps(json_list)
		return self.json

	def get_emotion(self):
		return self.sent.get_emotion()

	def get_social(self):
		return self.sent.get_social()

	# Ignoring tf_cf for now
	def get_synonyms(self):
		tf_idf = self.sent.get_tf_idf()
		syns = {}
		idf_index = 0
		while len(syns) < 5 and idf_index < len(tf_idf):
			word = tf_idf[idf_index]
			synonym = self.syns.get_syns(word)
			print("We are on word: " + word)
			if synonym != -1:
				syns[word] = synonym
			idf_index += 1
		return syns

	def get_readability_grade(self, text):
		return self.read.f_k_grade_level(text)

	# Ignoring this for now
	def get_readability_score(self, text):
		return self.read.f_k(text)


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

	

