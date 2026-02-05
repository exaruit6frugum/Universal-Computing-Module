@echo off
chcp 65001 > nul
title Сборка проекта

pyinstaller --onefile --distpath . --clean --name "Universal Computing Module" ../main.py

echo =========================================
echo         Cборка проекта завершена
echo =========================================
pause