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

#some initial variables
##################################
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
div_dict = {
            "area_1": 0,
            "area_2": 0,
            "area_3": 0
            }
###################################
# ---------- Helper funcs ------- #
###################################
def google_faces_coords(path, final_x_coords):
    print("using google api...")
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    # print('Faces:')

    for face in faces:
        # print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        # print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        # print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = ([vertex.x
                    for vertex in face.bounding_poly.vertices])

        # I want to print -> face bounds: (69,57),(505,57),(505,564),(69,564)
        # print('face bounds: {}'.format(','.join(vertices)))
        # print(vertices)
        if len(vertices) != 0:
            width = vertices[1] - vertices[0]
            interest_x = vertices[0] + (width/2)
            final_x_coords.append(int(interest_x))
            if interest_x < 426:
                div_dict["area_1"] += 1
            if interest_x > 426 and interest_x < 852:
                div_dict["area_2"] += 1
            else:
                div_dict["area_3"] += 1

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

    #divide the window in three sections
    cv2.line(frame, (div, 0), (div,height), (0,255,0), 5)
    cv2.line(frame, (div*2, 0), (div*2,height), (0,255,0), 5)

    #if for seconds have passed we record track of face
    if counter % 120 == 30:
        # our first attempt is to use haarcascades
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        if(len(face) != 0):
            print("Haarcascade succesful")
            for (x,y,w,h) in face:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                interest_x = int(x+(w/2))
                x_coords.append(interest_x)
                if interest_x < 426:
                    div_dict["area_1"] += 1
                if interest_x > 426 and interest_x < 852:
                    div_dict["area_2"] += 1
                else:
                    div_dict["area_3"] += 1
                # print(face)
        else:
            # we try to find a face with google API
            file_name = "frame_{}.jpg".format(counter-30)
            file_path = os.path.join(images_path, file_name)
            cv2.imwrite(file_path, gray)
            # print(file_path)
            google_faces_coords(file_path,x_coords)

    # this will help us know in what second of the video we are
    counter += 1
    cv2.imshow('frame', frame)
    #press esc to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
print (x_coords)
print (div_dict)
plot_res(div_dict)
