#!/usr/bin/env python3

import os
import sys
import json
from watson_developer_cloud import ToneAnalyzerV3

# Notes from API Reference
# https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/?python#error-handling

# These credentials were made with a trial account
# The free trial expires on Nov 22

class watson_analyzer:
	def __init__(self, text):
		tone_tuple 	 = self.tone_analysis(text)
		self.json 	 = tone_tuple[0]
		self.emotion = tone_tuple[1]
		self.social  = tone_tuple[2]

	def parse_analysis(self, data):
		emotion_tone =  data["document_tone"]["tone_categories"][0]["tones"]
		social_tone =  data["document_tone"]["tone_categories"][1]["tones"]

		emotion_dict = {}
		social_dict = {}

		# Parse items out of 
		for item in emotion_tone:
			emotion_dict[item["tone_name"]] = item["score"]

		for item in social_tone:
			social_dict[item["tone_name"]] = item["score"]

		return (emotion_dict, social_dict)

	def tone_analysis(self, text):
		tone_analyzer = ToneAnalyzerV3(
			version='2016-05-19',
			username='3eb02c6f-fe6e-4f90-b619-f6d93ba0e9e8',
			password='3Ipxrj3bXs4T'
		)

		# Tone Analysis
		# tones: emotion, language, social	(default all)
		# sentences: boolean on whether to return analysis on individual sentence (default true)
		# content_type: content type of request, text/plain, text/html, application/json (default text/plain)
		tone = tone_analyzer.tone(text, tones='emotion, social', sentences='false', content_type='text/plain')

		json_tone = json.dumps(tone, indent=2)

		analysis_tuple = self.parse_analysis(tone)
		
		tone_tuple = (json_tone, analysis_tuple[0], analysis_tuple[1])

		return tone_tuple






