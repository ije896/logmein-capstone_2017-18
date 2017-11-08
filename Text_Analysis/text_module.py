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

	def get_top5_syns(self, index=-1):
		recent_text = self.get_sentiment(index)
		top5_idf = recent_text.get_tf_idf_top5()
		syns = {word:self.syns.get_syns(word) for word in top5_idf}
		return syns

	def get_sentiment(self, index=-1):
		return self.text_list[index]

	def new_sentiment(self, text):
		self.text_list.append(text_analysis(text))

