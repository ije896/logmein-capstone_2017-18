import numpy as np
import cv2
import os

# grabs the first webcam available
# if want to use video file, insert path instead of number
cap = cv2.VideoCapture(0)
count = 0
path = "/Users/Josue/Desktop/FALL17/Capstone/logmein-capstone_2017-18/google_opencv/frames"
while(True):
    # ret is bool indicating if something was returned
    # frame is each frame captured
    ret, frame = cap.read()
    #Note how OpenCV reads colors as Blue Green Red instead of RGB
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if count % 120 == 3:
        cv2.imwrite(os.path.join(path, "frame%d.jpg"%count), gray)
    count += 1

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
