import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('josue.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('josue_gray.png',img)
