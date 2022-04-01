'''Thresholding is the binarization of in image where each pixel value set to 0 if less than Th else set to 255'''

import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   #have to convert image to grayscale first
cv.imshow('Grayscale', gray)


# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)  #155 is threshold value. 255 is the value to set if pixel value>Th. cv.THRESH_BINARY_INV can be used to reverse thresholding condition
#threshold is just the threshold valuje you pass i.e. 150 and thresh is the binarized image
cv.imshow('Thresholded at 150', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)  
cv.imshow('Thresholded inverted at 150', thresh_inv)


#Adaptive thresholding - allow computer to find the most optimal threshold value itself
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) #instead of thresholding value we specify method to find optimal threshold value. In this case we have given mean of neighborhood (could have used gaussian also which basically gives a weighted mean) and 11 is kernel size for neighborhood computation and 3 is the c value which is a number subtracted from mean to fine tune it if required
cv.imshow('Adaptive thresholding', adaptive_thresh)


cv.waitKey(0)