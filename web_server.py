# Загрузка модуля по работе с веб-сервером
from flask import Flask, render_template, request
import os
from image_processing import ImageProcessing

# Функция запуска веб-сервера и веб-формы
def WebStart():
    # Объявляю класс сервера
    app = Flask('__name__')
    # Определяю полный путь к каталогу веб-сервера
    #app_path = os.path.dirname(os.path.abspath(__name__))
    #app_path = os.path.dirname(os.path.realpath(__file__))
    #app_path = os.getcwd()
    #print(app_path)
    app_path = os.path.dirname(__file__)
    #print(os.path.realpath(__file__))
    # Определяю полный путь до файла с изображением для обработки
    photo_path = os.path.join(app_path, '/static/photo.jpg')

    # Описываю веб-каталог для загрузки изображения на первой странице
    @app.route('/', methods=['POST', 'GET'])
    def root():
        return render_template('index.html')

    # Описываю веб-каталог для вывода изображения и данных на второй странице
    @app.route('/upload', methods=['POST', 'GET'])
    def Upload():
        app_path = os.path.dirname(os.path.abspath(__file__))
        photo_path = '/'.join([app_path, 'static/photo.jpg'])
        # Переменная для передачи сообщения об ошибке загрузки изображения
        err_message =''
        # Переменная для передачи сообщения о результате загрузки изображения
        res_message =''
        # Проверка обрабатываемого запроса
        if request.method == 'POST':
            # Проверка загружаемого файла по типу
            fd = request.files['file']
            if (fd.mimetype == 'image/jpeg'):
                # Сохранение изображения в спец каталог с перезаписью предыдущего файла
                fd.save(photo_path)
                #res_message = ImageProcessing('C:/WBuild/CFT/TestJob/ImageProcessing/static/photo.jpg')
                res_message = ImageProcessing(os.path.realpath(photo_path))
                #res_message='sdfsd'
                pass
            else:
                err_message = 'Ошибка загрузки. Некорректное изображение'
        return render_template('upload.html', err_message = err_message, res_message = res_message)
    # Запуск веб-сервера с указанными параметрами
    app.run(host='localhost', port=8000)
