import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("2222825.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); 
# converted to grayScale 

hist = cv2.calcHist([img],[0],None,[256],[0,255])
plt.plot(hist)

img_hist = cv2.equalizeHist(img)
hist = cv2.calcHist([img_hist],[0],None,[256],[0,255])
plt.plot(hist)

cv2.imshow("img",img)
cv2.imshow("img with histo",img_hist)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()