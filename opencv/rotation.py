import cv2
import numpy as np

img = cv2.imread("2222825.png")

h,w = img.shape[:2]

# matrix = cv2.getRotationMatrix2D( (x_coordinate_of_center_of_rotn , y_coordinate_of_center_of_rotn ) , angle in deg, scale )
matrix = cv2.getRotationMatrix2D((w/2,h/2),10,1)

translated = cv2.warpAffine(img,matrix,(w,h))

cv2.imshow("img",translated)
cv2.waitKey()
cv2.destroyAllWindows()