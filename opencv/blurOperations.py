import cv2 
import numpy as np

img = cv2.imread("2222825.png")
r,c = img.shape[:2]

# kernel blurring using filter2d
kernel_25 = np.ones((25,25),np.float32)/625.0
output_kernel = cv2.filter2D(img,-1,kernel_25)

# box filter and blur fn blurring
output_blur = cv2.blur(img,(25,25))
output_boxFilter = cv2.boxFilter(img,-1,(5,5),normalize=False) # boxFilter -> extra param of depth,normalize

# gaussian blur -> far better than averging out blurring -> plot guassian -> center pixel ki val change krte wqt , uske paas wale pixels ko zyada weight dega , door walo ko km 
output_gaus = cv2.GaussianBlur(img,(5,5),0) # contrast maintained

# median blur -> replace pixel val with the median of all values lying in kernel area -> used for reducing noise (best for reducing noise)
output_median = cv2.medianBlur(img,5) # one value -> because -> sq kernel bnta h khud hi

# bilateral filtering -> reduction of nose + preserving of edges -> only those pixels having intensity almost same as target pixel are considered
# both gaussian space and intensity are considered
output_bilateral = cv2.bilateralFilter(img,5,6,6)

cv2.imshow("0",img)
cv2.imshow("1",output_kernel)
cv2.imshow("2",output_blur)
cv2.imshow("3",output_boxFilter)
cv2.imshow("4",output_gaus)
cv2.imshow("5",output_median)
cv2.imshow("6",output_bilateral)

cv2.waitKey()
cv2.destroyAllWindows()