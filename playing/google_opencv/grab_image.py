import numpy as np
import cv2
import os
import sys

# grabs the first webcam available
# if want to use video file, insert path instead of number
cap = cv2.VideoCapture(0)
count = 0
# file_name = os.path.join(os.path.dirname(__file__), sys.argv[1])
# img = cv2.imread(file_name, cv2.IMREAD_COLOR)
if cap.isOpened():
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #cast it to int
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #cast it to int

print (height, width)
width = int(width/3)
print (width)
#draw a line from top to bottom dividing the frame in 3


while(True):
    # ret is bool indicating if something was returned
    # # frame is each frame captured
    ret, frame = cap.read()
    print(frame)
    print (ret)
    cv2.line(frame, (width, 0), (width,height), (0,255,0), 5)
    cv2.line(frame, (width*2, 0), (width*2,height), (0,255,0), 5)
    # #Note how OpenCV reads colors as Blue Green Red instead of RGB
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # if count % 120 == 30:
    #     cv2.imwrite(os.path.join(path, "frame%d.jpg"%(count-30)), gray)
    # count += 1

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
