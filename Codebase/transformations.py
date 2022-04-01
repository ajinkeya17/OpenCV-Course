'''Most common image transformation operations applied on images'''

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Original', img)


# 1. Translation - shifting image along x and/or y axis

def translate(img, x, y):   # x & y are number of pixels by which you want to shift the image along each axis
    transMAT = np.float32([[1,0,x], [0,1,y]])  #create translation matrix
    dimensions = (img.shape[1], img.shape[0])  #imensions of image
    return cv.warpAffine(img, transMAT, dimensions)

 # -x -->left
 # -y --? up
 # +x --> right
 # +y --> down   

translated = translate(img, 100, 100) #shift image right by 100 pixels and down by 100 pixels
cv.imshow('Translated', translated)



# 2. Rotating image about a point by an angle

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)  #if rotation point not specified then assume to be centre

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) # always rotate the original image itself, dont rotate a rotated image otherwise will get varied background orientations
cv.imshow('Rotated', rotated)


# 3.Resizing

resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)  #resizes img to (500,500) and ignoring the aspect ratio. interpolation is set to cv.INTER_AREA if we are downsizing image and if we are upsizing then use cv.INTER_LINEAR or cv.INTER_CUBIC
cv.imshow('Resized image', resized)


# 4. Flipping 

flip = cv.flip(img, -1) #flipping codes. 0 -> flip vertically  1-> flipping horizontally  -1 -> flipping both horizontally and vertically
cv.imshow('Flipped', flip)


# 5. Cropping
cropped = img[50:200, 200:400]  #since img is just an array of pixel values can directly use slicing operations
cv.imshow('Cropped', cropped)



cv.waitKey(0)
