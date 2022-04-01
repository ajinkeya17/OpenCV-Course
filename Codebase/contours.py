'''Contours are boundaries of objects - curves or lines that outline objects. Mathematically they are NOT same as Edges but for practical purposes they can be considered similar
Useful for shape analysis, object detection,etc use cases
Contours are found on the binarized/black and white version of image so either use edge detected version of image or do thresholding operation and pass that to contour function but always prefer to use edge detected version'''



import cv2 as cv
from cv2 import GaussianBlur
import numpy as np

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   #grayscale of image
cv.imshow('Grayscale', gray)

blur = GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)  #blur image before finding edges
cv.imshow('Blurred image', blur)

canny = cv.Canny(blur, 125, 175)     #edges of image
cv.imshow('Canny', canny)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  
#mode parameter can be cv.RETR_TREE if want all hierarchial contours, cv.RETR_EXTERNAL if want external/outer contour, cv.RETR_LIST if want all contours in image
#contour approximation paramater. cv.CHAIN_APPROX_NONE will do nothing and keep all contours, cv.CHAIN_APPROX_SIMPLE will condense contours and retain only those that make sense
#cv.findContours will look at the structuring element or the edges found in the image and returns two values. 
#contours will be a list of all contour coordinates and hierarchies refers to hierarchial repr of contours


#to display the contours

blank = np.zeros(img.shape, dtype='uint8')  #create a blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1)  # -1 means to draw all contorues of color red and thickness 1
cv.imshow('Contours drawn', blank)  # will be almost identical to the edge detected image



print(f'Number of contours found is {len(contours)}')


cv.waitKey(0)