import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


#bitwise_AND
bitwise_and = cv.bitwise_and(rectangle,circle)  #will return instersection of both images
cv.imshow('Bitwise AND', bitwise_and)

#bitwise_OR
bitwise_or = cv.bitwise_or(rectangle,circle)  #will return union of both images
cv.imshow('Bitwise OR', bitwise_or)

#bitwise_XOR
bitwise_xor = cv.bitwise_xor(rectangle,circle)  #will return non-instersecting region of both images
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise_NOT
bitwise_not = cv.bitwise_not(rectangle)  #will return inversion of image
cv.imshow('Bitwise NOT', bitwise_not)


cv.waitKey(0)