import io
import os
from google.cloud import vision
from google.cloud.vision import types
import sys
import numpy as np
import cv2
import Image

# initialize video source
if len(sys.argv) < 2:
    cap = cv2.VideoCapture(0)
elif len(sys.argv) > 2:
    print ("Usage: {}  video_path".format(sys.argv[0])):
else:
    cap = cv2.VideoCapture(sys.argv[1])

#some initial variables
counter = 0
# get vcap property
if cap.isOpened():
    width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))  #cast it to int
    height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)) #cast it to int

# haarcascade for face detection
# detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BRG2GRAY)
    #haarcascade for face recognition
    face = face_cascade.detectMultiScale(gray, 1.3, 5)

    #draw some lines in the window
    cv2.line(frame, (width, 0), (width,height), (0,255,0), 5)
    cv2.line(frame, (width*2, 0), (width*2,height), (0,255,0), 5)

    cv2.imshow('frame', frame)
    
    #press esc to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
