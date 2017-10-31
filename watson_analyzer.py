#!/usr/bin/env python3

import os
import sys
import requests
import json
from watson_developer_cloud import ToneAnalyzerV3
import plotly.plotly as py
import plotly.graph_objs as go

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

	json_tone = json.dumps(tone, indent=2)
	#print 
	#print(json_tone)
	return tone

def graph_it(input_dict1, input_dict2):
	names1 = []
	values1 = []
	names2 = []
	values2 = []

	for key in input_dict1:
		names1.append(key)
		values1.append(input_dict1[key])

	for key in input_dict2:
		names2.append(key)
		values2.append(input_dict2[key])

	plot1 = go.Area(
		r=names1,
		t=values1,
		name='emotion',
		marker=dict(
			color = 'rgb(0,0,255'
		)
	)

	plot2 = go.Area(
		r=names2,
		t=values2,
		name='social',
		marker=dict(
			color = 'rgb(255,0,0'
		)
	)

	plot_data = [plot1, plot2]

	layout = go.Layout(
    title='emotion',
    font=dict(
        size=16
    ),
    legend=dict(
        font=dict(
            size=16
        )
    ),
    radialaxis=dict(
        ticksuffix='%'
    ),
    orientation=270
	)

	fig = go.Figure(data=plot_data, layout=layout)
	py.iplot(fig, filename='emotion')




def main():
	try:
		text = sys.argv[1]
	except:
		print("Usage: python3 %s input_file (max 128kB) ", sys.argv[0])
		exit(1)

	tone = tone_analyzer(text)

	emotion_tone =  tone["document_tone"]["tone_categories"][0]["tones"]
	social_tone =  tone["document_tone"]["tone_categories"][1]["tones"]

	emotion_dict = {}
	social_dict = {}

	for item in emotion_tone:
		emotion_dict[item["tone_name"]] = item["score"]

	for item in social_tone:
		social_dict[item["tone_name"]] = item["score"]


	#print(emotion_dict)
	#print(social_dict)

	graph_it(emotion_dict, social_dict)



if __name__ == '__main__':
	main()