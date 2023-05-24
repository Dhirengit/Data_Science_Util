import cv2
import numpy as np


circles = np.zeros((4,2), np.int)
counter = 0


def mousePoints(event, x,y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        circles[counter] = x,y
        counter += 1
        print(circles)


img = cv2.imread("images/nature.jpg")

while True:

    print("counter", counter)
    if counter == 4:
        width, height = 250,350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0], [width, 0],[0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img, matrix,(width,height))
        cv2.imshow("Output Images", imgOutput)

    for i in range(0,4):
        cv2.circle(img, (int(circles[i][0]), int(circles[i][1])),5,(0,0,255), cv2.FILLED)


    cv2.imshow("Original Images", img)
    cv2.setMouseCallback("Original Images", mousePoints)
    # cv2.imshow("Output Images", imgOutput)

    cv2.waitKey(1)