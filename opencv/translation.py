import cv2
import numpy as np

img = cv2.imread("2222825.png")

matrix = np.float32([[1,0,100],[0,1,50]])

# translated = cv2.warpAffine ( img_source , translation_matrix , final_img_size after translation)
translated = cv2.warpAffine(img,matrix,(img.shape[1]+100,img.shape[0]+100))

cv2.imshow("img",translated)
cv2.waitKey()
cv2.destroyAllWindows()