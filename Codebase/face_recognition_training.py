import os
import cv2 as cv
import numpy as np

people = []

for i in os.listdir(r'C:\Users\Atul\Downloads\OpenCV_course\opencv-course-master\Resources\Faces\train'):
    people.append(i)  #each folder in the faces folder corresponds to one person ben affleck,mindy,etc and name of folder is person's name so we store target variables

DIR = r'C:\Users\Atul\Downloads\OpenCV_course\opencv-course-master\Resources\Faces\train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')  #calling haarcascade detector

# Creating the training set
features = []
labels = []

def create_train():  #loop over all folders in the training folder and then loop over all images within and store in training set. Within each image detect only the face and crop it out using haarcascade face detector
    for person in people:
        path = os.path.join(DIR, person)   #to get path for folder of each person
        label = people.index(person)  #text classes need to be converted to numerical categories

        for img in os.listdir(path):
            img_path = os.path.join(path, img)  #create path for each image in each person's folder

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h ,x:x+w]   #cropping out just the face from the image
                
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training data created -------------')


features = np.array(features, dtype='object')  #all pixels of each image are flattened out to a single row of all pixel values for an image
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()  #instantiating out in-built face recognizer model

# Train recognizer on features list and labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')  # OpenCv allows us to save our trained model as a yaml which can be reused in other files instead of going through the entire training process again
np.save('features.npy', features)
np.save('labels.npy', labels)

