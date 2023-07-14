@echo off

cd server

python manage.py makemessages -a -e=django-html,py

cd ..