import numpy as np
from skimage.measure import label, regionprops
import skimage.morphology as morph
import matplotlib.pyplot as plt
import cv2

figures = {
    "circle" : 0,
    "square" : 0,
}
sqColors = {}
ciColors = {}
img = cv2.imread("balls_and_rects.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, gray = cv2.threshold(gray, 90, 255, 0)
labeled = label(gray)
regions = regionprops(labeled)
for region in regions:
    if (region.extent == 1):
        figures["square"] += 1
        if (str(img[int(region.centroid[0]), int(region.centroid[1])] [0]) not in sqColors.keys()):
            sqColors[str(img[int(region.centroid[0]), int(region.centroid[1])][0])] = 1
        else:
            sqColors[str(img[int(region.centroid[0]), int(region.centroid[1])] [0])] += 1
    else:
        figures["circle"] += 1
        if (str(img[int(region.centroid[0]), int(region.centroid[1])] [0]) not in ciColors.keys()):
            ciColors[str(img[int(region.centroid[0]), int(region.centroid[1])] [0])] = 1
        else:
            ciColors[str(img[int(region.centroid[0]), int(region.centroid[1])] [0])] += 1

print("Squares + Circles = ", figures["square"] + figures["circle"], " Where squares: ", figures["square"], "; circles: ", figures["circle"])
print("Figures by color:")
print("---Squares---")
for key in sqColors:
    print(key," : ", sqColors[key], " pc")
print("---Circles---")
for key in ciColors:
    print(key," : ", ciColors[key], " pc")

#Вывод
#Squares + Circles =  257  Where squares:  135 ; circles:  122
#Figures by color:
#---Squares---
#35  :  32  pc
#10  :  22  pc
#110  :  29  pc
#150  :  13  pc
#55  :  17  pc
#75  :  22  pc
#---Circles---
#10  :  17  pc
#110  :  29  pc
#35  :  19  pc
#150  :  23  pc
#75  :  22  pc
#55  :  12  pc
