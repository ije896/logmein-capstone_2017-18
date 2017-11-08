from flask import Flask, render_template, redirect, url_for, request
from text.Text_Analysis import watson_analyzer
import json
app = Flask(__name__)

video_filepath = ''
script_filepath = ''

wa = None

def readTextIntoString(filepath):
	with open(filepath, 'r') as fp:
		str = fp.read().replace('\n', '')
	return str

@app.route('/')
def index():
	return render_template('index.html')

# @app.route('/success/<video_filepath>&<audio_filepath>')
@app.route('/success/')
def success():
	global video_filepath
	global script_filepath
	global wa
	#return 'video_fp: %s \n script_fp: %s' % (video_filepath, script_filepath)
	# return 'script text: \n %s' % readTextIntoString(script_filepath)
	wa = watson_analyzer(readTextIntoString(script_filepath))
	# wa = watson_analyzer('hello hello hello')
	# return 'tone tuple : %s' % json.dumps(wa.json)
	return render_template('analysis.html', watson_data = wa.json)

@app.route('/analyze',methods = ['POST', 'GET'])
def login():
	global video_filepath
	global script_filepath
	if request.method == 'POST':
		video_filepath = request.form['video-filepath']
		script_filepath = request.form['script-filepath']
		return redirect(url_for('success'))
		# return redirect(url_for('success',video_filepath = video_filepath, audio_filepath = audio_filepath))
	else:
		video_filepath = request.args.get('video-filepath')
		script_filepath = request.args.get('script-filepath')
		return redirect(url_for('success'))
		# return redirect(url_for('success', video_filepath=video_filepath, audio_filepath=audio_filepath))


# MAIN

app.run(debug = True)

