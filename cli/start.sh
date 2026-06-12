#!/usr/bin/env bash
# 网文工坊 · 终端版 一键启动（Mac / Linux）
# 用法：在终端里 cd 到本文件夹，运行：bash start.sh   （或 chmod +x start.sh 后 ./start.sh）
cd "$(dirname "$0")" || exit 1

echo "============================================"
echo "           网文工坊 · 终端版"
echo "============================================"

# 1) 检查 Python3
if ! command -v python3 >/dev/null 2>&1; then
  echo "[缺 Python] 还没装 Python3。"
  echo "  请到 https://www.python.org/downloads/ 安装后再运行本脚本。"
  exit 1
fi

# 2) 检查依赖 openai，没有就自动装
if ! python3 -c "import openai" >/dev/null 2>&1; then
  echo "[首次运行] 正在安装依赖 openai，请稍候..."
  python3 -m pip install openai
fi

# 3) 启动（首次会问你要 API Key，没有就直接回车，弄到 key 再来）
python3 webnovel.py
