'''Smoothing/Blurring is done when an img has a lot of noise such as camera sensors,lighting issues,etc'''


import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

# 1.) Averaging - Each pixel is replaced by the average value of all pixels in the kernel window i.e. for a 3*3 kernel the centre pixel will be replaced by avg of other 8 surrounding pixels
average = cv.blur(img, (3,3)) #will implement averaging blur with a kernel of3*3. Increasing kernel size will increase blur
cv.imshow('Average Blur', average)


# 2.) GaussianBlur - similar to averaging operation but the surrounding pixels given a weight so weighted avg calculated. It gives less blurring than Averaging Blur but is more natural.
gauss = cv.GaussianBlur(img, (3,3), 0)   #0 is s.d. in x direction
cv.imshow('Gaussian Blurred', gauss)


# 3.) Median Blur - Instead of averaging it replaces pixel with median of its surrounding. 
# It provided more blur than above two methods and  is effective to reduce SALT&PEPPER NOISE. 
# It is not effective with higher kernel sizes such as 5*5 or 7*7
median = cv.medianBlur(img, 3) # kernel size is just 3 as automaticallly understands 3*3
cv.imshow('Median Blur', median)


# 4.) Bilateral Blurring - most effective blurring
#other blurring methods dont see if they are removing edges or not but Bilateral blurring does blurring but RETAINS edges as well
bilateral = cv.bilateralFilter(img, 10, 20, 20) #10 is diamter of neighborhood, 20 is sigma color (higher value indicates more colors in neighborhood), 20 is sigma space (higher value means pixel farther from centre will influence blurring more)
cv.imshow('Bilateral blurring', bilateral)

cv.waitKey(0)