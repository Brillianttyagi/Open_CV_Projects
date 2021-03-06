import cv2
import numpy as np
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        text = str(x)+","+str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,text,(x,y),font,1,(0,0,255),2)
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red  = img[x,y,2]
        text = str(blue)+','+str(green)+","+str(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,text,(x,y),font,1,(0,0,255),2)
        cv2.imshow('image',img)
        

img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()