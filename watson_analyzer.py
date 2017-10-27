#!/usr/bin/env python3

import os
import sys
import requests
import json
from watson_developer_cloud import ToneAnalyzerV3

# Notes from API Reference
# https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/?python#error-handling


# This might not work anymore
# Unsure if the credentials are wiped
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

	print(json.dumps(tone, indent=2))



def main():
	try:
		text = sys.argv[1]
	except:
		print("Usage: python3 %s input_file (max 128kB) ", sys.argv[0])
		exit(1)

	tone_analyzer(text)


if __name__ == '__main__':
	main()