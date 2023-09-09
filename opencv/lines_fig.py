import cv2
import numpy as np

canvas = np.zeros((500,500,3))

cv2.line(canvas,(0,0),(100,100),(0,255,0),2,cv2.LINE_4)
cv2.line(canvas,(0,20),(120,120),(0,255,0),2,cv2.LINE_AA)

# rectangle
cv2.rectangle(canvas,(200,200),(250,270),(255,0,0),-1)

# circle
cv2.circle(canvas,(250,250),10,(0,0,255),5)

# arrowed line
cv2.arrowedLine(canvas,(400,400),(400,500),(255,255,255),tipLength=0.5)

cv2.imshow('winname',canvas)
cv2.waitKey()