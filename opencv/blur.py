import cv2
import numpy as np

img = cv2.imread("2222825.png")

#  form the filters
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kenerl_3 = np.ones((3,3),dtype=np.float32)/9.0  # 9.0 is for normalization
kernel_11 = np.ones((11,11),dtype=np.float32)/121.0


# apply filters

# cv2.filter2D ( img source , ddepth (-1 means original img size ) , kernel_matrix )
output1 = cv2.filter2D(img,-1,kernel_identity)
output2 = cv2.filter2D(img,-1,kenerl_3)
output3 = cv2.filter2D(img,-1,kernel_11)

cv2.imshow("1",output1)
cv2.imshow("2",output2)
cv2.imshow("3",output3)

cv2.waitKey()
cv2.destroyAllWindows()