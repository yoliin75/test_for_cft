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
    # Выполняю проход по всем пикселям
    for i in range(0, x):
        for j in range(0, y):
            # Пиксел с кодом 0x00 соответствует черному цвету
            if pix[i,j] == 0:
                count_black += 1
            # Пиксел с кодом 0xFF соответствует белому цвету
            if pix[i,j] == 255:
                count_white += 1
    # Объявляю переменную для вывода результата
    res_message = ''
    # Провожу сравнение результатов
    if count_black > count_white:
         res_message = 'Черных пикселей больше, чем белых. Кол-во черных равно {}'.format(count_black)
    else:
        if count_black != count_white:
            res_message = 'Белых пикселей больше, чем черных. Кол-во белых равно {}'.format(count_white)
        else:
            res_message = 'Белых и черных пикселей одинаковое количество. Кол-во и белых и черных равно {}'.format(count_black)
    return res_message
