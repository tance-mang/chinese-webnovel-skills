#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网文工坊 · 终端版
独立于 Claude 运行，接任意 OpenAI 兼容 API（DeepSeek / Kimi / 硅基流动 / OpenRouter / 本地 Ollama / OpenAI ...）。

用法：
  python webnovel.py                      # 进入对话模式
  python webnovel.py "用 hook 写个修真开头"   # 一次性
  python webnovel.py --full               # 加载完整技能+知识库(需大上下文模型)
  python webnovel.py --list               # 列出所有技能

配置（三选一）：
  1) 环境变量：WN_API_KEY / WN_BASE_URL / WN_MODEL
  2) cli/config.json（复制 config.example.json 改）
  3) 启动后按提示填
依赖：pip install openai
"""
import os
import sys
import json
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
EXPORTS = os.path.join(HERE, "..", "exports")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_config():
    cfg = {}
    p = os.path.join(HERE, "config.json")
    if os.path.exists(p):
        try:
            cfg = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            print("[警告] config.json 解析失败：", e)
    cfg["base_url"] = os.environ.get("WN_BASE_URL", cfg.get("base_url") or "https://api.deepseek.com/v1")
    cfg["api_key"] = os.environ.get("WN_API_KEY", cfg.get("api_key") or "")
    cfg["model"] = os.environ.get("WN_MODEL", cfg.get("model") or "deepseek-chat")
    if not cfg["api_key"]:
        cfg["api_key"] = input("请输入 API Key（DeepSeek/Kimi/OpenAI 等）：").strip()
    return cfg


def build_system_prompt(full=False):
    parts = [read(os.path.join(EXPORTS, "instructions.md"))]
    if full:
        parts.append("\n\n# 技能工作流（详细）\n" + read(os.path.join(EXPORTS, "knowledge-skills.md")))
        parts.append("\n\n# 知识库（详细）\n" + read(os.path.join(EXPORTS, "knowledge-references.md")))
    else:
        parts.append("\n\n> 提示：如需某技能的完整工作流或知识库细节，按你已知的网文写作方法执行；"
                     "用 --full 启动可加载全部 26 技能 + 25 知识库的完整内容。")
    return "\n".join(parts)


def list_skills():
    txt = read(os.path.join(EXPORTS, "knowledge-skills.md"))
    print("可用技能（在对话里直接说需求或点名技能）：")
    for line in txt.splitlines():
        if line.startswith("## 技能："):
            print("  -", line.replace("## 技能：", "").strip())


def chat_stream(client, model, messages):
    """流式输出，返回完整回复。"""
    full = []
    resp = client.chat.completions.create(model=model, messages=messages, stream=True, temperature=0.8)
    for chunk in resp:
        delta = chunk.choices[0].delta.content if chunk.choices and chunk.choices[0].delta else None
        if delta:
            print(delta, end="", flush=True)
            full.append(delta)
    print()
    return "".join(full)


def main():
    ap = argparse.ArgumentParser(description="网文工坊 终端版")
    ap.add_argument("prompt", nargs="*", help="一次性输入；留空进入对话模式")
    ap.add_argument("--full", action="store_true", help="加载完整技能+知识库")
    ap.add_argument("--model", help="覆盖模型名")
    ap.add_argument("--list", action="store_true", help="列出所有技能")
    args = ap.parse_args()

    if args.list:
        list_skills()
        return

    try:
        from openai import OpenAI
    except ImportError:
        print("缺少依赖，请先运行： pip install openai")
        sys.exit(1)

    cfg = load_config()
    if args.model:
        cfg["model"] = args.model
    client = OpenAI(base_url=cfg["base_url"], api_key=cfg["api_key"])
    system = build_system_prompt(full=args.full)
    messages = [{"role": "system", "content": system}]

    print(f"网文工坊 终端版 | 模型 {cfg['model']} @ {cfg['base_url']}"
          + ("  [完整知识库]" if args.full else ""))

    if args.prompt:
        messages.append({"role": "user", "content": " ".join(args.prompt)})
        try:
            chat_stream(client, cfg["model"], messages)
        except Exception as e:
            print("\n[错误]", e)
        return

    print("进入对话模式。输入内容回车发送；输入 exit / quit 退出。\n")
    while True:
        try:
            user = input("你 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见。")
            break
        if user.lower() in ("exit", "quit", "退出"):
            break
        if not user:
            continue
        messages.append({"role": "user", "content": user})
        print("工坊 > ", end="", flush=True)
        try:
            reply = chat_stream(client, cfg["model"], messages)
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("\n[错误]", e)
            messages.pop()


if __name__ == "__main__":
    main()
