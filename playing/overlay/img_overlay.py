import numpy as np
import cv2

image = cv2.imread('frame_720.jpg')

for alpha in np.arange(0,1.1,0.05)[::-1]:
    # in order to apply a transparent overlay we need to make
    # two copies of the input image
    overlay = image.copy()
    output = image.copy()

    cv2.rectangle(overlay, (0,0), (243,60), (0,0,230), -1)
    #apply overlay
    #fourth arg is beta, 5th is gamma (scalar added to the weighted sum)
    cv2.addWeighted(overlay, alpha,output, 1 - alpha, 0, output)

    print("alpha ={}, beta ={}".format(alpha, 1-alpha))
    cv2.imshow("Output", output)
    cv2.waitKey(0)
