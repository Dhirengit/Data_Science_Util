import cv2
import numpy as np

img = cv2.imread("images/Acards.jpg")

width, height = 250,350
pts1 = np.float32([[20,56],[188,55],[22,302],[188,301]])
pts2 = np.float32([[0,0], [width, 0],[0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width,height))

for i in range(0,4):
    cv2.circle(img, (int(pts1[i][0]), int(pts1[i][1])),5,(0,0,255), cv2.FILLED)

cv2.imshow("Original Images", img)
cv2.imshow("Output Images", imgOutput)

cv2.waitKey(0)