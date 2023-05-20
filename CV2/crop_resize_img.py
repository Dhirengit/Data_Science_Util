import cv2

path = "images/road.jpg"

img = cv2.imread(path)
print("shape", img.shape)

width, height = 400,400
imgResize = cv2.resize(img, (width, height))
print("imgResize Shape", imgResize.shape)

imgCropped = img[200:720,310:380]


imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.imshow("Image Cropped Resize",imgCropResize)

cv2.waitKey(0)