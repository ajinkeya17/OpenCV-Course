
'''Rescaling and Resizing done to reduce computational burden on system. Rescaling means changing the height and width of video frames
Good practice to downscale the height and/or width of video since most cameras wont support going above the default scale'''

import cv2 as cv

'''function used to resize/rescale images/videos'''

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  #function which will resize the frame according to dimensions parameter



'''Resizing images'''

img = cv.imread('Resources/Photos/cat.jpg')
resized_img = rescaleFrame(img)
cv.imshow('Original cat', img)
cv.imshow('Resized cat', resized_img)



'''Rescaling videos'''

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Original Video', frame)
    cv.imshow('Rescaled Video',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


