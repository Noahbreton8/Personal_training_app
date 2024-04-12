##!/usr/bin/env bash
docker build -t 3005final71 .

docker-compose up -d

python3 src/GUI/gymDbGUI.py

docker-compose down