##!/usr/bin/env bash
export QT_DEBUG_PLUGINS=1

docker build -t 3005final71 .

docker-compose up -d

python3 src/GUI/gymDbGUI.py

docker-compose down