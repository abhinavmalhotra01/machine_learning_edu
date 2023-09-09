import cv2
import numpy as np

canvas = np.zeros((500,500,3))

# required points we need to join
pts= np.array([[250,5],[220,80],[280,80],[400,400],[200,200]],np.int32)
# reshape the points to shape (number_vertex , 1 , 2)
pts=pts.reshape((-1,1,2))
# draw this polygon
# here boolean tru and false determine if the fig is closed
cv2.polylines(canvas,[pts],True,(0,255,0),3)

cv2.imshow('winname',canvas)
cv2.waitKey()