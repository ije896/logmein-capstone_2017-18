import io
import os
from google.cloud import vision
from google.cloud.vision import types
import matplotlib.pyplot as plt
import sys
import numpy as np
import cv2

# initialize video source
if len(sys.argv) < 2:
    cap = cv2.VideoCapture(0)
elif len(sys.argv) > 2:
    print ("Usage: {}  video_path".format(sys.argv[0]))
else:
    cap = cv2.VideoCapture(sys.argv[1])

###############################
#some initial variables
###############################
counter = 1
# get vcap property
if cap.isOpened():
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #cast it to int
    div = int(width/3) #we will use this to divide the frame into sections
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #cast it to int

# haarcascade for face detection
# detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
images_path = "/Users/Josue/Desktop/FALL17/Capstone/logmein-capstone_2017-18/google_opencv/frames"
# Instantiates a client
client = vision.ImageAnnotatorClient()
x_coords = []
#dict to keep track of overall area usage
div_dict = {
            "area_1": 0,
            "area_2": 0,
            "area_3": 0
            }
#dict to keep track user doesn't cross area time threshold
alpha_dict = {
            "area_1": 0,
            "area_2": 0,
            "area_3": 0
            }
# tracker to know if current coord belongs to last area registered
last_area = ""
current_area = ""
alpha1 = 0
alpha2 = 0
alpha3 = 0
###################################
# ---------- Helper funcs ------- #
###################################


def plot_res(dict):
    plt.bar(range(len(dict)), dict.values(), align='center')
    plt.xticks(range(len(dict)), list(dict.keys()))
    plt.show()
###################################
# ------------ Main ------------- #
###################################

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output = cv2.flip(frame,1)
    overlay1 = cv2.flip(frame,1)
    overlay2 = cv2.flip(frame,1)
    overlay3 = cv2.flip(frame,1)

    #if for seconds have passed we record track of face
    if counter % 120 == 30:
        # our first attempt is to use haarcascades
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        if(len(face) != 0):
            print("Haarcascade succesful")
            for (x,y,w,h) in face:
                # cv2.rectangle(output,(x,y),(x+w,y+h),(255,0,0),2)
                interest_x = int(x+(w/2))
                x_coords.append(interest_x)

                if interest_x <= div:
                    if current_area == '':
                        current_area = "area_3"
                        last_area = current_area
                    else:
                        current_area = "area_3"
                    if current_area == last_area:
                        alpha_dict[current_area] += 0.25
                        alpha3 = alpha_dict[current_area]
                    else:
                        current_area, last_area = "", ""
                        alpha_dict["area_1"], alpha1 = 0, 0
                        alpha_dict["area_2"], alpha2 = 0, 0
                        alpha_dict["area_3"], alpha3 = 0, 0
                    div_dict["area_3"] += 1

                elif interest_x > div and interest_x <= (div*2):
                    if current_area == '':
                        current_area = "area_2"
                        last_area = current_area
                    else:
                        current_area = "area_2"
                    if current_area == last_area:
                        alpha_dict[current_area] += 0.25
                        alpha2 = alpha_dict[current_area]
                    else:
                        current_area, last_area = "", ""
                        alpha_dict["area_1"], alpha1 = 0, 0
                        alpha_dict["area_2"], alpha2 = 0, 0
                        alpha_dict["area_3"], alpha3 = 0, 0
                    div_dict["area_2"] += 1

                else:
                    if current_area == '':
                        current_area = "area_1"
                        last_area = current_area
                    else:
                        current_area = "area_1"
                    if current_area == last_area:
                        alpha_dict[current_area] += 0.25
                        alpha1 = alpha_dict[current_area]
                    else:
                        current_area, last_area = "", ""
                        alpha_dict["area_1"], alpha1 = 0, 0
                        alpha_dict["area_2"], alpha2 = 0, 0
                        alpha_dict["area_3"], alpha3 = 0, 0
                    div_dict["area_1"] += 1


        else:
            # we try to find a face with google API
            file_name = "frame_{}.jpg".format(counter-30)
            file_path = os.path.join(images_path, file_name)
            cv2.imwrite(file_path, gray)
            # google_faces_coords(file_path,x_coords,alpha1,alpha2,alpha3,current_area, last_area, not_Google)
            print("using google api...")
            with io.open(file_path, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            response = client.face_detection(image=image)
            faces = response.face_annotations

            for face in faces:
                vertices = ([vertex.x
                            for vertex in face.bounding_poly.vertices])

                if len(vertices) != 0:
                    width = vertices[1] - vertices[0]
                    interest_x = vertices[0] + (width/2)
                    x_coords.append(int(interest_x))

                    if interest_x <= div:
                        if current_area == '':
                            current_area = "area_3"
                            last_area = current_area
                        else:
                            current_area = "area_3"
                        if current_area == last_area:
                            alpha_dict[current_area] += 0.25
                            alpha3 = alpha_dict[current_area]
                        else:
                            current_area, last_area = "", ""
                            alpha_dict["area_1"], alpha1 = 0, 0
                            alpha_dict["area_2"], alpha2 = 0, 0
                            alpha_dict["area_3"], alpha3 = 0, 0
                        div_dict["area_3"] += 1

                    elif interest_x > div and interest_x <= (div*2):
                        if current_area == '':
                            current_area = "area_2"
                            last_area = current_area
                        else:
                            current_area = "area_2"
                        if current_area == last_area:
                            alpha_dict[current_area] += 0.25
                            alpha2 = alpha_dict[current_area]
                        else:
                            current_area, last_area = "", ""
                            alpha_dict["area_1"], alpha1 = 0, 0
                            alpha_dict["area_2"], alpha2 = 0, 0
                            alpha_dict["area_3"], alpha3 = 0, 0
                        div_dict["area_2"] += 1

                    else:
                        if current_area == '':
                            current_area = "area_1"
                            last_area = current_area
                        else:
                            current_area = "area_1"
                        if current_area == last_area:
                            alpha_dict[current_area] += 0.25
                            alpha1 = alpha_dict[current_area]
                        else:
                            current_area, last_area = "", ""
                            alpha_dict["area_1"], alpha1 = 0, 0
                            alpha_dict["area_2"], alpha2 = 0, 0
                            alpha_dict["area_3"], alpha3 = 0, 0
                        div_dict["area_1"] += 1
    # this will help us know in what second of the video we are
    counter += 1

    cv2.rectangle(overlay1, (0,0), (div,60), (0,0,230), -1)
    cv2.rectangle(overlay2, (div,0), (div*2,60), (0,0,230), -1)
    cv2.rectangle(overlay3, (div*2,0), (div*3,60), (0,0,230), -1)
    #apply overlay
    #fourth arg is beta, 5th is gamma (scalar added to the weighted sum)
    cv2.addWeighted(overlay1, alpha1,output, 1 - alpha1, 0, output)
    cv2.addWeighted(overlay2, alpha2,output, 1 - alpha2, 0, output)
    cv2.addWeighted(overlay3, alpha3,output, 1 - alpha3, 0, output)

    #divide the window in three sections
    cv2.line(output, (div, 0), (div,height), (0,255,0), 3)
    cv2.line(output, (div*2, 0), (div*2,height), (0,255,0), 3)


    cv2.imshow('frame', output)
    #press esc to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
print (x_coords)
print (div_dict)
plot_res(div_dict)
