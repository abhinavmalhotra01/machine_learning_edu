import cv2
import numpy as np


img = cv2.imread("2222825.png")
img_bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# declaration of clahe
# clipLimit -> threshold of contrast limiting
clahe = cv2.createCLAHE(clipLimit=5)
final_img = clahe.apply(img_bw)

# ordinary thresholding the same img
# ordinary_img = cv2.threshold(img_bw,155,255,cv2.THRESH_BINARY)

# showing all the images
cv2.imshow("ordinary",img)
cv2.imshow("clahe",final_img)
cv2.waitKey()