import cv2
import datetime


cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(datetime.datetime.now())
    frame = cv2.putText(frame,text,(0,30),font,1,(0,255,0),2,cv2.LINE_AA)
    frame = cv2.rectangle(frame,(244,154),(400,255),(0,0,255),1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
