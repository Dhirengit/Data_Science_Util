import cv2
import  numpy as np

img1 = cv2.imread("images/baby_lion.jpg")
img2 = cv2.imread("images/road.jpg")
print("Original",img1.shape, img2.shape)

img1 = cv2.resize(img1, (0,0), None, 0.5,0.5)
img2 = cv2.resize(img2, (0,0), None, 0.5,0.5)
print("Reshape",img1.shape, img2.shape)


hor = np.hstack((img1,img2))
# vert = np.vstack((img1,img2))

# cv2.imshow("Vertical Stack", vert)
cv2.imshow("Horizontal Stack", hor)



cv2.waitKey(0)