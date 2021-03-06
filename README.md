# Stage Presence
(The backend for the application)

- A visual and aural analyzer that helps you improve your presentation skills
- Web app (thin-client) that takes in a filepath for a video recorded by the user and returns an analysis including scores for each metric as well as recommendations based on the values of the metrics

# INTEGRATED BACKEND

From the perspective of the frontend (flask server), the only communication point is the backend's interface (backend/interface.py). The interface takes in a filepath and challenge_id, and returns a dictionary of all the results. If the backend/process_video.py script is used, it automatically records benchmarks for processing time and stores them in backend/results/\[SHA1 hash of input video file].

The backend automatically performs A/V decoupling so it can send a pure audio file to the audio module.

## Performance

To improve performance, we split off the independent processing branches. We spawn a video thread (which blocks once it starts waiting for I/O from Google's Cloud Vision API), while the main branch of execution analyzes the audio and then passes the results to text.

# MODULES

## Text Module

The Text_Analysis module provides a number of functions to aid in analyzing a presentation's script.

- Analyzes sentiment (tone) with watson_analyzer.py

- Provides synonyms for the top 5 "interesting" words (TF-IDF candidates) for which we have synonyms in our thesaurus

- Analyzes readability and provides a score and a grade

- Takes in a Speech-To-Text transcript from the audio module, compares it to the target script by calculating the word error rate, and outputs a percentage score representating "articulation" (clarity of pronunciation, etc)

**USAGE**:

All calls to the text analysis module can be done through interface.py, which serves as a class that integrates the various submodules (watson_analyzer, synonyms, readability, articulation). Requires a STT transcript from audio to calculate articulation.

Interface is a static class and therefore cannot be instantiated as an object

In order to query the text analysis process_filepath() can be called with the text file and a dictionary of options
    options = {run_all:True/False, sentiment:True/False, synonyms:True/False, readability:True/False, challenge_id:tongue_twister}

process_filepath() will return a dictionary containing the queried information

```
text_obj = text.Interface()
text_json = text_obj.process_filepath(file, options)
```

### Dependencies
* Watson Tone Analyzer API
* Requires STT transcript from audio (not a venv dependency, but still a dependency)

## Video Module

The Video module analyses a video and captures a presenter's face's (x,y) coordinates at each second in the video. At the end of the analysis, a json object containing various properties of the video can be extracted by calling

```
video_obj = VideoAnalysis(<video_path>)
video_details = video_obj.to_json()
```

### Dependencies
The video module uses the following python packages which might need to be installed in your virtual environment:
* OpenCV 3.3
* Numpy
* Google Vision API.

#### Installing dependencies

As always, remember to have your virtual env up before installing any of these dependencies.
```
pip3 install --upgrade google-cloud-vision
pip3 install opencv-python
export GOOGLE_APPLICATION_CREDENTIALS=YOUR_LOCAL_DIRECTORY/logmein-capstone_2017-18/backend/Video/google_api_credentials.json

```

### Want more insight about what's happening here?

You can dive in into some OpenCV documentation [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html#lucas-kanade).

Or read though some basic Python-OpenCV tuts [here](https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/?completed=/mog-background-reduction-python-opencv-tutorial/).

## Audio Module
This module analyzes the audio from the speech to extract the following features:
- Words per minute (over the entire speech, and during continuous phrases)
- Letters per minute
- Pitch of speaker over time (autocorrelation approximation)
- The STT transcript of the speech

You can use this module by instantiating an audio interface object and passing it a filepath to a .wav file:

```
from audio import interface
a = interface.Interface()
a.process_filepath(filepath, options)
```

The object 'a' will then contain a dictionary of the features decribed above.

### Dependencies:
The following Python libraries are required for the Audio module
* Watson Developer Cloud
* Librosa
* SciPy
* NumPy
* MatPlotLib
