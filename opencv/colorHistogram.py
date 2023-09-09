import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("2222825.png")
b,g,r = cv2.split(img)

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img)
v = cv2.equalizeHist(v)
merged_hsv = cv2.merge((h,s,v))
bgr_enhanced = cv2.cvtColor(merged_hsv,cv2.COLOR_HSV2BGR)

cv2.imshow("i",img)
cv2.imshow("bgr_enhanced",bgr_enhanced)


hist = cv2.calcHist([b],[0],None,[256],[0,255])
plt.plot(hist)
hist = cv2.calcHist([g],[0],None,[256],[0,255])
plt.plot(hist)
hist = cv2.calcHist([r],[0],None,[256],[0,255])
plt.plot(hist)


plt.show()
cv2.waitKey()
cv2.destroyAllWindows()