'''Face Detection using pre-trained models in OpenCV
Two main classifiers are - HaarCascades and Local Binary Patterns which are more advanced and are less prone to noise
OpenCV has repo of all type of haarcascades - https://github.com/opencv/opencv/tree/4.x/data/haarcascades
We will use the frontalface_default classifier as we want to do face detection'''

# Step 1 open the xml file and click Raw
# Step 2 copy the xml contents from the raw file
# Step 3 create a new file in your current directory with name hhaar_face.xml and paste the contents in it. The classifier is now ready

# Haarcascades are not the best face detection as they are very prone to noise but they are used as a first choice due to simple implementation. Dlibs face recognizer is more effective for practical cv projects

# haarcascades dont need color, they just look at edges and detect if a face is present or not.

import cv2 as cv

capture = cv.VideoCapture(0) # a capture variable has to be created first and if want to use computer's webcam then pass in integer such as 0,1 or 2 else pass path of video file if stored on system

while True:     #unlike photos a video has to be read in frame by frame so a while loop used
    isTrue, img = capture.read()   #capture.read() will read in video frame by frame. isTrue is a boolean which will tell if frame read in successfully ot not and frame variable will hold the actual frame


    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #haarcascade doesnt care about color, it only needs edges

    haar_cascade = cv.CascadeClassifier('haar_face.xml')  #the xml file will be read in and stored in haar_cascade variable

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=2) #minNeighbors is number of neighbors a rectangle should have to be called a face
    #faces_rect will be a list of rectangular cooridnates of the detected faces
    #haarcascade is very susceptible to noise and can easily misclassify. To reduce this we can increase minNeighbors and scaleFactor parameters. If already overclassifying then reduce minNeighbors

    print(f'Number of faces detected = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow('Detected faces', img)  # Show detected faces

    if cv.waitKey(20) & 0xFF==ord('d'):  #to prevent video from streaming indefinitely we put this condition to close it by pressing key 'd'
        break

capture.release()  #releasing the capture pointer
cv.destroyAllWindows()  #destroy all windows








cv.waitKey(0)