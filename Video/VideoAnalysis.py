#!/usr/bin/env python

'''
Video Analysis
====================
This video analyzer tracks the users movement using face tracking
and returns those coordinates as an array of (coords and timestamps)
Usage
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

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
client = vision.ImageAnnotatorClient()

class VideoAnalysis:
    def __init__(self, video_src):
        self.coords_and_time = [] #a tuple of x, y coord, sec
        self.video_src = video_src
        self.vide_duration = None
        self.total_frames = int(cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FPS)
        self.width = int(cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(cv2.VideoCapture(video_src).get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.current_frame = 0
        self.frame_filepath = ""

    def get_coords(self):
        print (self.coords_and_time)
        return self.coords_and_time

    def get_fps(self):
        return self.fps

    def get_video_width(self):
        return self.width

    def get_video_height(self):
        return self.height

    def get_video_duration(self):
        return self.video_duration

    def get_frame_filepath(self):
        return self.frame_filepath

    def to_json(self):
        json_obj = json.dumps(self,default=lambda o: o.__dict__)
        print(json_obj)
        return json_obj

    def _google_analysis(self,file_path, video_time):
        with io.open(file_path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.face_detection(image=image)
        faces = response.face_annotations

        for face in faces:
            vertices = ([(vertex.x, vertex.y)
                        for vertex in face.bounding_poly.vertices])
            if len(vertices) != 0:
                width = vertices[1][0] - vertices[0][0]
                height = vertices[2][1] - vertices[1][1]
                interest_x = vertices[0][0] + (width/2)
                interest_y = vertices[0][1] + (height/2)
                self.coords_and_time.append({"x": interest_x, "y": interest_y,"sec": video_time})

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
                if(video_time == 3.0):
                    file_name = "frame_excerpt.jpg"
                    file_path = os.path.join("./", file_name)
                    cv2.imwrite(file_path, frame)
                    self.frame_filepath = file_path
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                face = face_cascade.detectMultiScale(gray, 1.3, 5)
                if(len(face) != 0):
                    # print("Haarcascade succesful")
                    for (x,y,w,h) in face:
                        # cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
                        interest_x = int(x+(w/2))
                        interest_y = int(y+(h/2))
                        self.coords_and_time.append({"x": interest_x, "y": interest_y,"sec": video_time})
                else:
                    # print("using google api...")
                    file_name = "frame_{}.jpg".format(int(video_time))
                    file_path = os.path.join("./", file_name)
                    cv2.imwrite(file_path, gray)
                    self._google_analysis(file_path, video_time)

                # cv2.imshow('frame', vis)
                # press esc to quit
                # k = cv2.waitKey(30) & 0xff
                # if k == 27:
                #     break
            else:
                break
        self.vide_duration = video_time

def main():
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0

    print(__doc__)
    app = VideoAnalysis(video_src)
    app.run()
    app.to_json()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
