import cv2 as cv

'''Reading Images'''

# img = cv.imread('Resources/Photos/cat_large.jpg')  #function to read in img as a matrix of pixels

# cv.imshow('Cat',img)

# cv.waitKey(0)


'''Reading Videos'''

# capture = cv.VideoCapture('Resources/Videos/dog.mp4') # a capture variable has to be created first and if want to use computer's webcam then pass in integer such as 0,1 or 2 else pass path of video file if stored on system

# while True:     #unlike photos a video has to be read in frame by frame so a while loop used
#     isTrue, frame = capture.read()   #capture.read() will read in video frame by frame. isTrue is a boolean which will tell if frame read in successfully ot not and frame variable will hold the actual frame
#     cv.imshow('Video', frame)   #each frame once captured is displayed

#     if cv.waitKey(20) & 0xFF==ord('d'):  #to prevent video from streaming indefinitely we put this condition to close it by pressing key 'd'
#         break

# capture.release()  #releasing the capture pointer
# cv.destroyAllWindows()  #destroy all windows




