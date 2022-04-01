'''Allows us to focus/extract specific parts of image and remove unwanted parts'''

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)


blank = np.zeros(img.shape[:2], dtype='uint8') #size of mask should always be same as image

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) # our mask is a circle

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image', masked)


cv.waitKey(0)