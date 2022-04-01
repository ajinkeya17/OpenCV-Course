'''Color spaces is space of color channels such as BGR(default), RGB, grayscale, HSV, etc.
By default openCV reads in images in BGR format(not RGB) but openCV automatically corrects that and displays it as RGB but if you display these images in other apps like atplotlib then there will be inversion of colors as they would treat all images to be RGB by default. So convert BGR images to RGB in openCV only if you want to use them with external libraries like matplotlib'''

import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Original', img)


# 1.) BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #grayscale helps understand pixel intensity
cv.imshow('Gray', gray)


# 2.) BGR to HSV(Hue Saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3.) BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# 4.) BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)   #this will show an inverted color scheme as we have converted to rgb but opencv still thinks it is bgr by default so it will invert it again and display to us bgr. So use this only if you want to display images using external libraries such as matplotlib

# 5.) HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

cv.waitKey(0)