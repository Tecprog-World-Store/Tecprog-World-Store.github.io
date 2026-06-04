@echo off
setlocal
cd /d "%~dp0.."
python scripts\convertir_webp.py
endlocal
