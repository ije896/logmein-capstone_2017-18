#!/usr/bin/env python3

import os
import sys
import requests
import json
import watson_developer_cloud

# Notes from API Reference
# https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/?python#error-handling



def main():
	try:
		text = sys.argv[1]
	except:
		print("Usage: python3 %s input_file (max 128kB) ", sys.argv[0])
		exit(1)

	# tone_analyzer = ToneAnalyzerV3(
	# 	version='2016-05-19',
	# 	username='28179730-932b-41d1-b4c5-8a62fcb3ecd7',
	# 	password='7JRbXc1jr0vr'
	# )

	# Tone Analysis
	# tones: emotion, language, social	(default all)
	# sentences: boolean on whether to return analysis on individual sentence (default true)
	# content_type: content type of request, text/plain, text/html, application/json (default text/plain)
	#tone = tone_analyzer.tone(text, sentences='true', content_type='text/plain')

	#print(json.dumps(tone, indent=2))

	# This code isn't going to run
	# Need to create a Workspace, Entity, and Value
	# THEN we can create synonyms

	conversation = watson_developer_cloud.ConversationV1(
		username = '611de235-d947-46c7-a256-c3e8161eb5d1',
		password = 'dUudSTgGIgWL',
		version = '2017-05-26'
	)

	response = conversation.list_values()

	response = conversation.list_synonyms(
		workspace_id = '9978a49e-ea89-4493-b33d-82298d3db20d',
		entity = 'beverage',
		value = 'soda'
	)

	print(json.dumps(response, indent=2))



if __name__ == '__main__':
	main()