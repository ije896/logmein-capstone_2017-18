#!/usr/bin/env python

'''
Video Analysis
====================
This video analyzer tracks the users movement using face tracking
and returns sentiment and face-tracking coordinates along with a timestamp
as a list or json object.
-----
VideoAnalysis.py [<video_source>]
----
ESC - exit
'''
import numpy as np
import json
import cv2
import io
import os
import sys
from google.cloud import vision
from google.cloud.vision import types

face_cascade = cv2.CascadeClassifier('./Video/haarcascade_frontalface_default.xml')
client = vision.ImageAnnotatorClient()

class VideoAnalysis:
    def __init__(self, video_src):
        self.coords_and_time = [] #a tuple of x, y coord, sec
        self.sentiment_and_time = []
        self.video_src = video_src
        self.video_duration = None
        self.total_frames = int(cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FPS)
        self.width = int(cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.current_frame = 0
        self.google_api_requests = 0
        self.open_cv_requests = 0
        self.run();

    def get_coords(self):
        return self.coords_and_time

    def get_sentiment(self):
        return self.sentiment_and_time

    def get_fps(self):
        return self.fps

    def get_video_width(self):
        return self.width

    def get_video_height(self):
        return self.height

    def get_video_duration(self):
        return self.video_duration

    def to_json(self):
        json_obj = json.dumps(self,indent=2,default=lambda o: o.__dict__)
        print (json_obj)
        return json_obj

    def _google_analysis(self,file_path, video_time):
        with io.open(file_path, 'rb') as image_file:
            content = image_file.read()

        self.google_api_requests += 1
        image = types.Image(content=content)

        response = client.face_detection(image=image)
        faces = response.face_annotations
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
        sent_conf = {}

        for face in faces:
            sent_conf["anger"] = likelihood_name[face.anger_likelihood]
            sent_conf["joy"] = likelihood_name[face.joy_likelihood]
            sent_conf["sorrow"] = likelihood_name[face.sorrow_likelihood]
            sent_conf["surprise"] = likelihood_name[face.surprise_likelihood]

            vertices = [(vertex.x,vertex.y)
                        for vertex in face.bounding_poly.vertices]

            if len(vertices) != 0:
                face_bounds = vertices
                self.coords_and_time.append({"face_bounds": face_bounds,"sec": video_time})
                self.sentiment_and_time.append({"sentiment": sent_conf, "sec": video_time })
        os.remove(file_path)

    def run(self):
        cap = cv2.VideoCapture(self.video_src)
        # Will only analyze the frame at every second
        for frame_no in np.arange(0, self.total_frames, self.fps):
            cap.set(1, frame_no)
            ret, frame = cap.read()
            self.current_frame = frame_no
            video_time = round(self.current_frame/self.fps,2)

            if ret:
                file_name = "frame_{}.jpg".format(int(video_time))
                file_path = os.path.join("./", file_name)
                cv2.imwrite(file_path, frame)
                self._google_analysis(file_path, video_time)

            else:
                break
                
        self.video_duration = video_time

