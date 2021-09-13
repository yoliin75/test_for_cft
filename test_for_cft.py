# Проверка тикселей в изображении
from PIL import Image
im = Image.open('im.jpg') # чтение изображения
#im.show() # отображение изображения
pix = im.load() # Выгружаем значения пикселей
x,y = im.size # Размер изображения
count_black = 0
count_white = 0
for i in range(0, x):
    for j in range(0, y):
        if pix[i,j] == 0 : count_black += 1
        if pix[i,j] == 255 : count_white += 1
if count_black > count_white: print('Черных пикселей больше, чем белых, кол-во черных = ' + str(count_black))
else:
    if count_black != count_white: print('Белых пикселей больше, чем черных, кол-во белых = ' + str(count_white))
    else: print('Белых и черных пикселей одинаковое количество')
