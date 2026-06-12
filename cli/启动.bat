@echo off
chcp 65001 >nul
title 网文工坊 · 终端版
cd /d "%~dp0"

echo ============================================
echo            网文工坊 · 终端版
echo ============================================
echo.

REM 1) 检查 Python
where python >nul 2>&1
if errorlevel 1 (
  echo [缺 Python] 你还没装 Python。
  echo   请到 https://www.python.org/downloads/ 下载安装，
  echo   安装第一屏务必勾选 "Add Python to PATH"，装完重新双击本文件。
  echo.
  pause
  exit /b
)

REM 2) 检查依赖 openai，没有就自动装
python -c "import openai" >nul 2>&1
if errorlevel 1 (
  echo [首次运行] 正在安装依赖 openai，请稍候...
  python -m pip install openai
  echo.
)

REM 3) 启动（首次会问你要 API Key，没有就直接回车，弄到 key 再来）
python webnovel.py

echo.
echo （已退出。关闭本窗口即可；下次双击本文件就能再用。）
pause
