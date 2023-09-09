import cv2
import numpy as np

img = cv2.imread("2222825.png")

img_szed = cv2.resize(img,(5,5))

img_re_linear = cv2.resize(img,None,fx=5.5,fy=5.5,interpolation=cv2.INTER_LINEAR)

img_re_cubic = cv2.resize(img,None,fx=5.5,fy=5.5,interpolation=cv2.INTER_CUBIC)

cv2.imshow("linear",img_re_linear)
cv2.imshow("cubic",img_re_cubic)
cv2.imshow("original",img)

cv2.waitKey()
cv2.destroyAllWindows()