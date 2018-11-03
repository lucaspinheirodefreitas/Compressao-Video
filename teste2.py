import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if(ret is True):
        color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        break
    cv2.imshow('frame',color)
    # cv2.imshow('frame',ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
