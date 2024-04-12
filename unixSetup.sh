##!/usr/bin/env bash

docker-compose up -d

python3 src/GUI/gymDbGUI.py

docker-compose down