from flask import render_template, redirect, url_for
from audio_analysis import audio_analysis
import json
from ast import literal_eval

class Results:
	@staticmethod
	def page(request):
		if request.method == 'POST':
			video_filepath = request.form['video-filepath']
			script_filepath = request.form['script-filepath']
			# return 'video_fp: %s \n script_fp: %s' % (video_filepath, script_filepath)
		else:
			video_filepath = request.args.get('video-filepath')
			script_filepath = request.args.get('script-filepath')
			# return 'video_fp: %s \n script_fp: %s' % (video_filepath, script_filepath)
		#aa = audio_analysis.audio_analyzer('/Users/zacharyfeinn/Repos/Capstone189a/logmein-capstone-web-stable/test_data/obama_bin_laden.mp3')
		return json.dumps(literal_eval(open('/Users/zacharyfeinn/Repos/Capstone189a/logmein-capstone-web-stable/test_data/obama_bin_laden_json.txt').read()))
