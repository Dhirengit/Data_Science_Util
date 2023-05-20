import cv2
import numpy as np


path = "images/baby_lion.jpg"
kernel = np.ones((5,5),np.uint8)
print("kernel", kernel)

img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imgCanny = cv2.Canny(imgBlur, 100, 150)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Image", img)
cv2.imshow("GrayScale", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Eroded", imgEroded)

cv2.waitKey(0)