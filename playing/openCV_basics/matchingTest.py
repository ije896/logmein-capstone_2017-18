import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('controller.jpg',0)
img2 = cv2.imread('josue_controller.jpg', 0)

orb = cv2.ORB_create();

# key points and descriptors
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# BF matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Here we create matches of the descriptors, then we sort them based on their distances.
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

# we draw the matches
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
