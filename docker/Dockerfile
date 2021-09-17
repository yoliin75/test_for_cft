# Файл для сборки docker-образа
FROM python:3.9
MAINTAINER yoliin@yandex.ru
WORKDIR /opt
RUN pip install --no-cache-dir flask werkzeug pillow
RUN git clone https://github.com/yoliin75/test_for_cft
EXPOSE 8000
CMD [ "python", "/opt/test_for_cft/main.py" ]
