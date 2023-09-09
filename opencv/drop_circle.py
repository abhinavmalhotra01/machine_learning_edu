import cv2
import numpy as np

def draw_cirlce(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img,(x,y),10,(0,255,0),3)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("img")
cv2.setMouseCallback("img",draw_cirlce)
while(True):
    cv2.imshow("img",img)
    if(cv2.waitKey(20)==ord('q')):
        break
cv2.destroyAllWindows()