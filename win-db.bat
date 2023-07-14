@echo off

cls

cd server
python manage.py makemigrations
python manage.py migrate
cd ..