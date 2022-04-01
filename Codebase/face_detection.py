'''Face Detection using pre-trained models in OpenCV
Two main classifiers are - HaarCascades and Local Binary Patterns which are more advanced HaarCascades and are less prone to noise
OpenCV has repo of all type of haarcascades - https://github.com/opencv/opencv/tree/4.x/data/haarcascades
We will use the frontalface_default classifier as we want to do face detection'''

# Step 1 open the xml file and click Raw
# Step 2 copy the xml contents from the raw file
# Step 3 create a new file in your current directory with name hhaar_face.xml and paste the contents in it. The classifier is now ready


# haarcascades dont need color, they just look at edges and detect if a face is present or not.

import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #haarcascade doesnt care about color, it only needs edges
cv.imshow('Grayscale', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')  #the xml file will be read in and stored in haar_cascade variable

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=2) #minNeighbors is number of neighbors a rectangle should have to be called a face
#faces_rect will be a list of rectangular cooridnates of the detected faces
#haarcascade is very susceptible to noise and can easily misclassify. To reduce this we can increase minNeighbors and scaleFactor parameters. If already overclassifying then reduce minNeighbors

print(f'Number of faces detected = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', img)  # Show detected faces




cv.waitKey(0)