import cv2 as cv
import numpy as np

'''Drawing on image'''

blank = np.zeros((500,500,3), dtype='uint8')  # create a blank/dummy image first with dimension 500*500 and 3 color channels. unit8 is dtype of an image

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0,255,0  #turn certain pixels green, can do 0,0,255 for red,etc
cv.imshow('Green',blank)



# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2) , (0,0,255), thickness = 2) #will create a rectangle from origin to centre with color red and thickness of lines as 2. use thickness=cv.FILLED to fill fill in the rectangle
cv.imshow('Rectangle', blank)


# 3. Draw a Circle
cv.circle(blank, (blank.shape[0]//2,blank.shape[1]//2) , 40, (0,0,255), thickness=-1)  #circle at centre of image created with radius 40 and color red and thickness 3
cv.imshow('Circle', blank)


# 4. Draw a Line
cv.line(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2) , (255,255,255), thickness = 2) #will create a line from origin to centre with color red and thickness of lines as 2. 
cv.imshow('Line', blank)


# 5. Write text on image
cv.putText(blank, 'Hello', org=(225,225), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale= 1.0, color=(255,255,255), thickness = 2) 
cv.imshow('Text', blank)

cv.waitKey(0)  # to keep image displayed indefinitely otherwise will close instantly