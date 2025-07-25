# -*- coding: utf-8 -*-
"""face_detection _with_opencv.ipynb

Automatically generated by Colab.

Original file is located at
    x

# RoadMap
- OpenCV
- Face Detection
"""

# !pip install opencv-python

# import opencv package
import cv2
imagePath='donald.jpg'

img = cv2.imread(imagePath)
img

img.shape

# convert image into grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image

gray_image.shape

# Load the classifier
# Haar Cascade

face_classifer = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_classifer.empty():
    print("Error loading cascade classifier. Check the path to the XML file.")
else:
    print("Cascade classifier loaded successfully.")

face = face_classifer.detectMultiScale(
    gray_image,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize=(40, 40)
)

# Drawing a bounding box
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

img_rgb =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

import matplotlib.pyplot as plt
plt.imshow(img_rgb)

# Real Time Face detection
import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

#access te webcam
video_capture = cv2.VideoCapture(0)

# identify face in the webcam
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifer.detectMultiScale(
        gray_image,
        scaleFactor= 1.1,
        minNeighbors= 5,
        minSize=(40, 40)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return faces

while True:
    result, video_frame = video_capture.read()
    if result is False:
        break

    faces = detect_bounding_box(video_frame)
    cv2.imshow("Face Detection Project", video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# These lines should be OUTSIDE the while loop
video_capture.release()
cv2.destroyAllWindows()


