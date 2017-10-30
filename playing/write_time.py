import numpy as np
import cv2
import sys

try:
    video_src = sys.argv[1]
except:
    video_src = 0

# initialize some variables
cap = cv2.VideoCapture(video_src)
font = cv2.FONT_HERSHEY_SIMPLEX
coordinates_time = []
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detectMultiScale(image, rejectLevels, levelWeights[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize[, outputRejectLevels]]]]]]) → objects
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)
    upper_body = upper_body_cascade.detectMultiScale(gray, 1.3, 5)
    # get time in seconds
    time = cap.get(cv2.CAP_PROP_POS_MSEC)*0.001
    # #img, text, coordinates(x,y) top, font, size, color, thicknes, type of line
    cv2.putText(frame,"Time: "+ str(time)[:4],(10,30), font, 0.5, (0,0,255), 1, cv2.LINE_AA)

    # for (x,y,w,h) in faces:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = frame[y:y+h, x:x+w]

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    #use esc to quit
    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
