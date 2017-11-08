import cv2
import numpy as np

cap = cv2.VideoCapture(0)
counter = 0
alpha = 0

if cap.isOpened():
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #cast it to int
    div = int(width/3) #we will use this to divide the frame into sections
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #cast it to int


while True:
    ret, frame = cap.read()
    output = frame.copy()
    overlay = frame.copy()

    #divide the window in three sections
    cv2.line(output, (div, 0), (div,height), (0,255,0), 2)
    cv2.line(output, (div*2, 0), (div*2,height), (0,255,0), 2)

    cv2.rectangle(overlay, (0,0), (div,60), (0,0,230), -1)
    cv2.rectangle(overlay, (div,0), (div*2,60), (0,0,230), -1)
    cv2.rectangle(overlay, (div*2,0), (div*3,60), (0,0,230), -1)
    if(counter % 120 == 30):
        alpha += 0.1
    #apply overlay
    #fourth arg is beta, 5th is gamma (scalar added to the weighted sum)
    cv2.addWeighted(overlay, alpha,output, 1 - alpha, 0, output)


    cv2.imshow('frame', output)
    counter += 1
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
