#!/usr/bin/env python3

import os
import sys
import requests
import json
from watson_developer_cloud import ToneAnalyzerV3

# Notes from API Reference
# https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/?python#error-handling

# These credentials were made with a trial account
def tone_analyzer(text):
	tone_analyzer = ToneAnalyzerV3(
		version='2016-05-19',
		username='3eb02c6f-fe6e-4f90-b619-f6d93ba0e9e8',
		password='3Ipxrj3bXs4T'
	)

	# Tone Analysis
	# tones: emotion, language, social	(default all)
	# sentences: boolean on whether to return analysis on individual sentence (default true)
	# content_type: content type of request, text/plain, text/html, application/json (default text/plain)
	tone = tone_analyzer.tone(text, tones='emotion, social', sentences='true', content_type='text/plain')

	json_tone = json.dumps(tone, indent=2)
	
	tone_tuple = {json_tone, tone}

	print(json_tone)
	return tone_tuple


def main():
	try:
		text = sys.argv[1]
	except:
		print("Usage: python3 %s input_file (max 128kB) ", sys.argv[0])
		exit(1)

	# Returns a tuple
	# {json, dictionary}
	tone_tuple =  = tone_analyzer(text)

	emotion_tone =  tone["document_tone"]["tone_categories"][0]["tones"]
	social_tone =  tone["document_tone"]["tone_categories"][1]["tones"]

	emotion_dict = {}
	social_dict = {}

	# Parse items out of 
	for item in emotion_tone:
		emotion_dict[item["tone_name"]] = item["score"]

	for item in social_tone:
		social_dict[item["tone_name"]] = item["score"]


	print(emotion_dict)
	print(social_dict)


if __name__ == '__main__':
	main()