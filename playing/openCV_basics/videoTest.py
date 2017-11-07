import numpy as np
import cv2

# grabs the first webcam available
# if want to use video file, insert path instead of number
cap = cv2.VideoCapture(0)

while(True):
    # ret is bool indicating if something was returned
    # frame is each frame captured
    ret, frame = cap.read()

    #Note how OpenCV reads colors as Blue Green Red instead of RGB
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
