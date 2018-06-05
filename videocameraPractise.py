import numpy as np 
import cv2

#Video capture starts
cap = cv2.VideoCapture(0)

while(True):

    #Checking if it is correct or not
    ret, frame = cap.read()

    #Converting the frame to grey
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #A frame is an image and a video is a collection of related images so here we are displaying each frame and hence the video
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Releasing the window
cap.release()
cv2.destroyAllWindows()