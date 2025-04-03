#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка Python зависимостей
pip install -r requirements.txt

# Сборка фронтенда
cd frontend
npm install
npm run build
cd ..

# Сборка бэкенда
python manage.py collectstatic --no-input
python manage.py migrate 