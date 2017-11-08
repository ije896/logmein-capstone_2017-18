#!/usr/bin/env python3

import os
import sys
from Text_Analysis import synonyms
from Text_Analysis import text_analysis


# This class can be invoked with either the text itself
# or the relative path of the text file
class text_module:
	def __init__(self, text):
		self.text_list  = [text_analysis(text)]
		self.syns       = synonyms.synonyms()

	def get_json(self, index=-1):
		recent_text = self.get_sentiment(index)
		return recent_text.get_json()

	def get_emotion(self, index=-1):
		recent_text = self.get_sentiment(index)
		return recent_text.get_emotion()

	def get_social(self, index=-1):
		recent_text = self.get_sentiment(index)
		return recent_text.get_social()

	def get_freq(self, index=-1):
		recent_text = self.get_sentiment(index)
		return recent_text.get_freq()

	def get_top5_idf_syns(self, index=-1):
		recent_text = self.get_sentiment(index)

		tf_idf = recent_text.get_tf_idf()
		syns = {}
		idf_index = 0
		while len(syns) < 5 and idf_index < len(tf_idf):
			word = tf_idf[idf_index]
			synonym = self.syns.get_syns(word)
			if synonym != -1:
				syns[word] = synonym
			idf_index += 1

		return syns

	def get_top5_cf_syns(self, index=-1):
		recent_text = self.get_sentiment(index)

		tf_cf = recent_text.get_tf_cf()
		syns = {}
		cf_index = 0
		while len(syns) < 5 and cf_index < len(tf_cf):
			word = tf_cf[cf_index]
			synonym = self.syns.get_syns(word)
			if synonym != -1:
				syns[word] = synonym
			cf_index += 1

		return syns

	def get_sentiment(self, index=-1):
		return self.text_list[index]

	def new_sentiment(self, text):
		self.text_list.append(text_analysis(text))

