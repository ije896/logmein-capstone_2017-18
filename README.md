# Presentation Helper
This repository contains the work done for the UCSB course, CS189A-B, for the company LogMeIn

- A visual and aural analyzer that helps you improve your presentation skills
- Web app (thin-client) that records you using your webcam and gives you scores and gives you recommendations for your presentation


# MODULES

## Text Module

The Text_Analysis module provides a number of functions to aid in analyzing a presentation's script.

- Analyzes sentiment (tone) with watson_analyzer.py

- Gets (sorted) frequencies of each word in text_analysis.py

- Can be queried for synonyms

**USAGE**:

All calls to the text analysis module can be done through text_module.py, which serves as a class that integrates the various submodules (watson_analyzer, synonyms, etc)

In order to create a text_module object 'text_module' needs to be imported from 'Text_Analysis' and the object needs to be instantiated with the text file (this can be either the text itself or the relative path to the text file).

```
text_obj = text_module(<text_path>)
```

From here you can access a json object of the sentiment analysis, dictionary of the emotion analysis, dictionary of the social analysis, frequency of the words, and synonyms of the most common words.  These can be done by:

```
text_obj.get_json()
text_obj.get_emotion()
text_obj.get_social()
text_obj.get_top5_idf_syns()
text_obj.get_top5_cf_syns()
```

Additionally, you can create multiple text_analysis objects on separate texts within the ame text module.  They can be created and then accessed with the following:

```
text_obj.new_sentiment(<text_path>)
text_obj.get_sentiment(<text_analysis_index>)		NOTE: This is 0 indexed and defaults to most recent
```

## Video Module

The Video module analyses a video and captures a presenter's face x,y coordinates at every second in the video. At the end of the analysis, a json object containing various properties of the video can be extracted by calling

```
video_obj = VideoAnalysis(<video_path>)
video_obj.run()
video_details = video_obj.to_json()
```

In addition, a HeatMap class has also been defined to visualize the extracted coordinates obtained using the VideoAnalaysis module. Some dummy data has been placed for demonstration, but that could be easily changed by instantiating a new HeatMap object and passing to it coordinates from a video you analyzed. You can use it in this way:

```
coords = video_obj.get_coords()
heatmap = HeatMap(coords)
heatmap.plot()
```

### Dependencies
The video module uses the following python packages which might need to be installed in your virtual environment:
* OpenCV 3.3
* Numpy
* Matplot
* Google Vision API (ask me for the api auth if you want to test it)

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
