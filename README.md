# Presentation Helper
This repository contains the work done for the UCSB course, CS189A-B, for the company LogMeIn

- A visual and aural analyzer that helps you improve your presentation skills
- Web app (thin-client) that records you using your webcam and gives you scores and gives you recommendations for your presentation


# MODULES

## Text Module

The Text_Analysis module provides a number of functions to aid in analyzing a presentation's script.

- Analyzes sentiment (tone) with watson_analyzer.py

- Provides synonyms for the top 5 most used words (not including words such as the, is, etc)

- Does an analysis on readability and provides a score and a grade

**USAGE**:

All calls to the text analysis module can be done through interface.py, which serves as a class that integrates the various submodules (watson_analyzer, synonyms, etc)

Interface is a static class and therefore cannot be instantiated as an object

In order to query the text analysis process_filepath() can be called with the text file and a dictionary of options
    options = {run_all:True/False, sentiment:True/False, synonyms:True/False, readability:True/False}

process_filepath() will return a JSON object containing the queried information

```
text_obj = text.Interface()
text_json = text_obj.process_filepath(file, options)
```

## Video Module

The Video module analyses a video and captures a presenter's face x,y coordinates at every second in the video. At the end of the analysis, a json object containing various properties of the video can be extracted by calling

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

The Audio module analyzes the speech to extract the following features:
- Words per minute (over the entire speech, and during continuous phrases)

Future:
- Volume tracking of speaker
- Pitch tracking of speaker

Dependencies:
* Watson Developer Cloud
* Librosa