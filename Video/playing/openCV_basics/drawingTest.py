import cv2
import numpy as np

img = cv2.imread('josue.jpg', cv2.IMREAD_COLOR)
# start drawing
# where, start coordinates, end coordiantes, color(bgr), line thickness
cv2.line(img,(0,0), (150,150),(255,255,255),15)

#draw rectangle
#where, top left coordinate, bottom right coord. , color, line thickness
cv2.rectangle(img, (15,25), (200,150),(0,0,255),15)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
