'''By default all RGB and BGR images have 3 color channels R,B and G. OpenCV allows us to split and merge these 3 components'''


import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Original', img)

#Splitting color channels
b,g,r = cv.split(img)

# these 3 images will be shown as grayscale images highlighting pixel intensity so suppose in blue image wherever it is white it means higher blue channel pixel concentration such as sky wheras wherever black it means low concentration of blue pixels such as in trees where green pixels more
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)  # will be (x,y,3) where 3 means 3 color channels
print(b.shape) # will be just (x,y)
print(g.shape)
print(r.shape)


#merging color channels
merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)



# to display the individual color channel images in their actual colors instead of grayscale
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue channel', blue)
cv.imshow('Green channel', green)
cv.imshow('Red channel',red)

cv.waitKey(0)