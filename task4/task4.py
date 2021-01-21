import cv2
import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

def writeToFile(arr):
    file = open("img.txt", 'w')
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            file.write(str(arr[i, j]))
        file.write('\n')
    file.close()

def analyzeImage(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, threshold_image = cv2.threshold(gray_image, 120, 255, 0)
    labeled = measure.label(threshold_image)
    regions = measure.regionprops(labeled)
    arr = []
    for region in regions:
        if (region.eccentricity > 0.95 and region.filled_area > 200):
            arr.append(region.filled_area)
    arr = np.array(arr)
    #print(arr[arr > np.std(arr)], np.std(arr))
    #plt.imshow(labeled)
    #plt.show()
    if (len(arr) != 0):
        return len(arr[arr > np.std(arr)])
    else:
        return 0

sum = 0
for i in range(1,13):
   sum += analyzeImage("images/img ("+str(i)+").jpg")

print("There are ",sum, "pencils on the images")

#
#cv2.imshow("Image", threshold_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()