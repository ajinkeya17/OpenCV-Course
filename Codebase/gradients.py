import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)


# 1.) Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# 2.) Sobel - computes gradient in x and y direction
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Combined Sobel', combined_sobel)


# 3.) Canny Edge Detection
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)





cv.waitKey(0)


