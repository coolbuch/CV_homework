import numpy as np
from io import StringIO
filename = "figure6.txt"
img = []
size = 0

with open(filename, 'r') as file:  # Открываем файл на чтение
    size = float(file.readline())
    file.readline()
    img = np.loadtxt(StringIO(file.read())) # Загружаем массив в img


yArr, xArr = np.where(img == 1) # В массивы yArr, xArr передаются координаты всех y и x соответственно
if len(xArr) == 0:
    print("figures didnt find")
else:
    w = np.max(xArr) - np.min(xArr)   # Находим максимальную ширину фигуры
    print(round(size / w, 6))

# figure1.txt  0.5 mm / px
# figure2.txt 0.125 mm / px
# figure3.txt 0.65 mm / px
# figure4.txt 1 mm / px
# figure5.txt figures didnt find
# figure6.txt 0.166667 mm / px