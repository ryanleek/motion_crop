import cv2
import numpy as np

cap = cv2.VideoCapture('./videos/test.mp4') #load video
count1 = 0 #counts number of frames

#capture two frames
rval, frame1 = cap.read()
rval, frame2 = cap.read()

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)  #difference of two frames
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)    #convert diff into greyscale

    blur = cv2.GaussianBlur(gray, (5,5), 0) #blur image to reduce noise
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #set threshold
    dilated = cv2.dilate(thresh, None, iterations=3) #fill holes in the thresholded image
    
    #find contour
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    count2 = 0  #counts number of motions in a frame 

    #further implementation(removing, rectangle)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)    #values of contour

        if cv2.contourArea(contour) < 7000:    #to remove small unnecessary contours, (modify number for better results)
            continue
        
        filename = "test{}-{}.jpg".format(count1,count2)

        motion = frame1[y:y+h, x:x+w]
        cv2.imwrite(filename, motion)

        count2 += 1
        #cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)   #draw rectangle on frame1

    count1 += 1

    #show results
    #cv2.imshow("feed", frame1)  
    
    #change to next frame
    frame1 = frame2 
    rval, frame2 = cap.read()

    #incase of error
    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()