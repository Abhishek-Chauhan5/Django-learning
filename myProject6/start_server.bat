@echo off
cd /d "%~dp0"
echo Starting myProject6 on http://127.0.0.1:8006
python manage.py runserver 8006
