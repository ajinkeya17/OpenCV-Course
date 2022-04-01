import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = np.load('features.npy', allow_pickle=True)  #reading in saved feature array
labels = np.load('labels.npy') #reading in saved label array

people=[]
for i in os.listdir(r'C:\Users\Atul\Downloads\OpenCV_course\opencv-course-master\Resources\Faces\train'):
    people.append(i) #names of people in list corresponding to target labels


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')  #loading the trained model

img =cv.imread(r'C:\Users\Atul\Downloads\OpenCV_course\opencv-course-master\Resources\Faces\val\elton_john\3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person to be recognized', gray)

#Detect face in image
faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]  #extracting out the faces from the image which is to be tested

    label, confidence = face_recognizer.predict(faces_roi)  #do prediction which will return label and the confidence of prediction
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0 , (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Prediction', img)

cv.waitKey(0)