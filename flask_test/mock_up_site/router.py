from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success/<video_filepath>&<audio_filepath>')
def success(video_filepath, audio_filepath):
	return 'video_fp: %s \n script_fp: %s' % (video_filepath, audio_filepath)

@app.route('/analyze',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		video_filepath = request.form['video-filepath']
		audio_filepath = request.form['audio-filepath']
		return redirect(url_for('success',video_filepath = video_filepath, audio_filepath = audio_filepath))
	else:
		user = request.args.get('video-filepath')
		return redirect(url_for('success',name = user))


# MAIN

app.run(debug = True)