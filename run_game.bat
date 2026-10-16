@echo off
title Coliseum of Iron
echo ========================================================
echo   COLISEUM OF IRON // 3D GLADIATOR COMBAT ENGINE
echo ========================================================
echo Starting local game server...
python run_game.py
if errorlevel 1 (
    echo.
    echo Opening index.html directly in default browser...
    start index.html
)
pause
