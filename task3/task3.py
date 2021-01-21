import numpy as np
from skimage.measure import label
import skimage.morphology as morph



def findByMasks(image, masks):
    img = np.copy(image)
    arr = []
    for mask in masks:
        bin = morph.binary_opening(img, mask)
        lb = label(bin)
        #writeToFile(lb)
        img = img - bin
        arr.append(lb.max())
    return arr

def writeToFile(arr):
    file = open("img.txt", 'w')
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            file.write(str(arr[i, j]))
        file.write('\n')
    file.close()

masks = [
    np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]),
    np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]]),
    np.array([[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]),
    np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]),
    np.array([[1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]),
]

img = np.load("ps.npy")

findings = findByMasks(img, masks)
summ = 0
for elem in findings:
    summ += elem
print("Count of elements: ", summ, '\n')
for mask, foundCount in zip(masks, findings):
    print('Found such elements:', foundCount)
    print(mask)
    print('\n')

#Вывод
#Count of elements:  500

#Found such elements: 92
#[[1 1 1 1 1 1]
# [1 1 1 1 1 1]
# [1 1 1 1 1 1]
# [1 1 1 1 1 1]]

#Found such elements: 96
#[[1 1 1 1 1 1]
# [1 1 1 1 1 1]
# [1 1 0 0 1 1]
# [1 1 0 0 1 1]]

#Found such elements: 95
#[[1 1 0 0 1 1]
# [1 1 0 0 1 1]
# [1 1 1 1 1 1]
# [1 1 1 1 1 1]]

#Found such elements: 94
#[[1 1 1 1]
# [1 1 1 1]
# [1 1 0 0]
# [1 1 0 0]
# [1 1 1 1]
# [1 1 1 1]]

#Found such elements: 123
#[[1 1 1 1]
# [1 1 1 1]
# [0 0 1 1]
# [0 0 1 1]
# [1 1 1 1]
# [1 1 1 1]]
