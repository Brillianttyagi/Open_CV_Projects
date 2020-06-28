import cv2
import numpy as np
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        
        cv2.circle(img,(x,y),10,(0,255,0),-1)
        prev.append((x,y))
        if len(prev)>=2:
            cv2.line(img,prev[-2],prev[-1],(255,0,0),20)
        cv2.imshow('image',img)



prev = []
img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()