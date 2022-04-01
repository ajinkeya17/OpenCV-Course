'''distribution of pixel intensity. Can be computed for both RGB and Grayscale images'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)


# 1.) Grayscale Histogram

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256]) 
#[0] is list of channels for which to compute histogram but since grayscale we just pass 0. 
#None is the mask argument so if we want to find hist for specific part of img then pass a mask
#[256] is number of bins
#[0,256] range of all possible pixel values

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



# 2.) Color Histogram

blank = np.zeros(img.shape[:2], dtype='uint8') #size of mask should always be same as image

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) # our mask is a circle

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])  #computing histogram for specific masked region. set as None if want for whole image
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)