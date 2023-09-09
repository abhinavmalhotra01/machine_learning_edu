import cv2
import numpy as np

img = cv2.imread("2222825.png")
sizeOfKernel = 15

kernel = np.zeros((sizeOfKernel,sizeOfKernel))
kernel[int((sizeOfKernel-1)/2),:] = np.ones(sizeOfKernel)
# zeroes ki matrix bnayi aur fir , center row ko 1 ki val dedi

kernel=kernel/sizeOfKernel  #normal

output = cv2.filter2D(img,-1,kernel)

# horizontally dizzy img
cv2.imshow('1',output)
cv2.waitKey()
cv2.destroyAllWindows()