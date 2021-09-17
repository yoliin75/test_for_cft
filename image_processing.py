# -*- coding: utf-8 -*-
### Модуль проверки пикселей в изображении ###
# Загрузка модуля для работы с изображениями
from PIL import Image
# Функция проверки пикселей в изображении
def ImageProcessing(img_file):
    # Чтение загруженного изображения
    im = Image.open(img_file)
    # Формирую массив пикселей из изображения
    pix = im.load()
    # Определяю размер изображения
    x, y = im.size
    # Объявляю счетчики для пикселей
    count_black = 0
    count_white = 0
    # Проверяю на RGB
    if isinstance(pix[0,0], tuple):
        code_black = (0, 0, 0)
        code_white = (255, 255, 255)
    elif isinstance(pix[0,0], int):
        code_black = 0
        code_white = 255
    else:
        return u'Цветовая схема неопределена'
    # Выполняю проход по всем пикселям
    for i in range(0, x):
        for j in range(0, y):
            # Пиксел с кодом 0x00 соответствует черному цвету
            if pix[i,j] == code_black:
                count_black += 1
            # Пиксел с кодом 0xFF соответствует белому цвету
            if pix[i,j] == code_white:
                count_white += 1
    # Объявляю переменную для вывода результата
    res_message = ''
    # Провожу сравнение результатов
    if count_black > count_white:
         res_message = u'Черных пикселей больше, чем белых. Кол-во черных равно {}, кол-во белых равно {}'.format(count_black, count_white)
    else:
        if count_black != count_white:
            res_message = u'Белых пикселей больше, чем черных. Кол-во белых равно {}, кол-во черных равно {}'.format(count_white, count_black)
        else:
            res_message = u'Белых и черных пикселей одинаковое количество. Кол-во и белых и черных равно {}'.format(count_black)

    return res_message
