import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Original', img)

'''Most common functions used in every computer vision project'''

# 1. Converting to grayscale. 

'''Normal image is 3 channel RBG so we may convert it to grayscale to see intensity distribution of pixels'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # function to change color scale and we specify the color scale conversion i.e. RGB to gray
cv.imshow('Gray',gray)


# 2. Blurring an image

'''To remove certain noise from image. Bad lighting issues,camera sesnor issues,etc'''
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)  #(3,3) is the size of the blurring kernel. It has to be odd always.
cv.imshow('Blur', blur)


# 3. Creating Edge Cascade

'''To detect edges in image - points of sudden pixel intensity change'''
canny = cv.Canny(img, 125, 175)  #number of edges can be reduced by increasing blur on imahge
cv.imshow('Canny Edges', canny)


# 4. Dilating an image using a Structuring element
dilated = cv.dilate(canny, (7,7), iterations = 3)  #the strucuring element will be canny and (3,3) is kernel size
cv.imshow('Dilated', dilated)


# 5. Eroding 
eroded = cv.erode(dilated, (7,7), iterations = 3)  # to erorde the dilated image to get back the edge cascade image
cv.imshow('Eroded', eroded)  


# 6. Resizing image
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)  #resizes img to (500,500) and ignoring the aspect ratio. interpolation is set to cv.INTER_AREA if we are downsizing image and if we are upsizing then use cv.INTER_LINEAR or cv.INTER_CUBIC
cv.imshow('Resized image', resized)


# 7. Cropping image
cropped = img[50:200, 200:400]  #since img is just an array of pixel values can directly use slicing operations
cv.imshow('Cropped', cropped)

cv.waitKey(0)