import cv2
import numpy as np

img = cv2.imread("images/img (8).jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
scale_percent = 20 # Процент от изначального размера
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(gray_image, 127, 255, 0)

cv2.imshow("Image", threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()