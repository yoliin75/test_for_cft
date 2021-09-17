#!/bin/sh
# Запуск контейнера
docker run -p 58000:8000 -d -it --name image_processing image_processing:2.0
