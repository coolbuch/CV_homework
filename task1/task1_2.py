#import numpy as np
#from io import StringIO

#def openFile(filename):
#    with open(filename, 'r') as file:
from io import StringIO
import numpy as np

def read(filename):
    with open(filename, 'r') as file:
        size = float(file.readline())
        file.readline()
        img = np.loadtxt(StringIO(file.read()))
    return img

img1 = read('img1.txt')
img2 = read('img2.txt')
x1 = 0
y1 = 0
x2 = 0
y2 = 0

for y in range(img1.shape[0]):
    for x in range(img1.shape[1]):
        if (img1[y,x] == 1):   # Находим первую единицу на первой "картинке"
            x1 = x
            y1 = y
            break

for y in range(img2.shape[0]):
    for x in range(img2.shape[1]):
        if (img2[y,x] == 1):   # Находим первую единицу на второй "картинке"
            x2 = x
            y2 = y
            break

print(x2 - x1, y2 - y1)

# img2 смещено относительно img1 на (10, -4)