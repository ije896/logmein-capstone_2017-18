#!/usr/bin/env python3

import json
from watson_developer_cloud import ToneAnalyzerV3

# Notes from API Reference
# https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/?python#error-handling

# These credentials were made with a trial account
# The free trial expires on Nov 22

class WatsonAnalyzer:

	@staticmethod
	def parse_analysis(data):
		emotion_tone =  data["document_tone"]["tone_categories"][0]["tones"]
		social_tone =  data["document_tone"]["tone_categories"][1]["tones"]

		emotion = {}
		social = {}

		# Parse items out of 
		for item in emotion_tone:
			emotion[item["tone_name"]] = item["score"]

		for item in social_tone:
			social[item["tone_name"]] = item["score"]

		tones = {'emotion': emotion, 'social': social}

		return tones

	@staticmethod
	def tone_analysis(text):
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

		return WatsonAnalyzer.parse_analysis(tone)

	@staticmethod
	def get_sentiment(text):
		return WatsonAnalyzer.tone_analysis(text)



