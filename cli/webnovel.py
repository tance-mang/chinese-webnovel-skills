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

对话模式里输入 /help 看全部命令（存稿/换格式/学习模式/校对过审/历史回溯）。

配置（三选一）：
  1) 环境变量：WN_API_KEY / WN_BASE_URL / WN_MODEL
  2) cli/config.json（复制 config.example.json 改）
  3) 启动后按提示填
存稿偏好（书名/格式/目录/自动记录）写在 config.json，可在对话里用 /set 改，不写死。
依赖：pip install openai   （存 Word 另需：pip install python-docx）
"""
import os
import sys
import json
import argparse
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
EXPORTS = os.path.join(HERE, "..", "exports")
CONFIG_PATH = os.path.join(HERE, "config.json")

# 仅这些是“存稿偏好”，会被 /set 持久化进 config.json（绝不写 api_key）
PREF_KEYS = ("book", "output_dir", "save_format", "auto_log")
SAVE_FORMATS = ("txt", "md", "docx")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_config():
    cfg = {}
    if os.path.exists(CONFIG_PATH):
        try:
            cfg = json.load(open(CONFIG_PATH, encoding="utf-8"))
        except Exception as e:
            print("[警告] config.json 解析失败：", e)
    # API（环境变量优先）
    cfg["base_url"] = os.environ.get("WN_BASE_URL", cfg.get("base_url") or "https://api.deepseek.com/v1")
    cfg["api_key"] = os.environ.get("WN_API_KEY", cfg.get("api_key") or "")
    cfg["model"] = os.environ.get("WN_MODEL", cfg.get("model") or "deepseek-chat")
    # 存稿偏好（给默认值，不写死——都能在对话里 /set 改）
    cfg["book"] = cfg.get("book") or "未命名"
    cfg["output_dir"] = cfg.get("output_dir") or os.path.join(os.getcwd(), "output")
    fmt = (cfg.get("save_format") or "txt").lower()
    cfg["save_format"] = fmt if fmt in SAVE_FORMATS else "txt"
    cfg["auto_log"] = cfg.get("auto_log", True)
    if not cfg["api_key"]:
        print("\n还没配 API Key。终端版是个壳，需要接一个 AI 才能写作")
        print("（DeepSeek / Kimi / 硅基流动 / OpenRouter 等任意一家，有免费额度，去哪弄见 cli/README.md「第四步」）。")
        print("拿到后两种填法：① 把 config.example.json 复制成 config.json 填进去（一劳永逸）；② 现在直接粘贴下面：")
        cfg["api_key"] = input("  粘贴 API Key（还没有就直接回车，等接好 AI 再来）：").strip()
        if not cfg["api_key"]:
            print("（已跳过。配好 key 再运行 python webnovel.py 即可。）")
            sys.exit(0)
    return cfg


def save_prefs(cfg):
    """把存稿偏好写回 config.json，保留其它字段（含 api_key 原样，不新增）。"""
    data = {}
    if os.path.exists(CONFIG_PATH):
        try:
            data = json.load(open(CONFIG_PATH, encoding="utf-8"))
        except Exception:
            data = {}
    for k in PREF_KEYS:
        data[k] = cfg.get(k)
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print("[警告] 偏好保存失败：", e)
        return False


def build_system_prompt(full=False):
    parts = [read(os.path.join(EXPORTS, "instructions.md"))]
    if full:
        parts.append("\n\n# 技能工作流（详细）\n" + read(os.path.join(EXPORTS, "knowledge-skills.md")))
        parts.append("\n\n# 知识库（详细）\n" + read(os.path.join(EXPORTS, "knowledge-references.md")))
    else:
        parts.append("\n\n> 提示：如需某技能的完整工作流或知识库细节，按你已知的网文写作方法执行；"
                     "用 --full 启动可加载全部技能 + 知识库的完整内容。")
    return "\n".join(parts)


COACH_DEPTHS = {
    "1": "用【速查清单】式：每次产出后只列 3-5 个要点（钩子/爽点/节奏/人设），最快。",
    "2": "用【详细讲解】：每次产出后讲清‘为什么这么写’的原理 + 1 个例子，通俗不堆术语。",
    "3": "用【边写边教】：先正常写，再回过头拆解这段为什么这么处理、哪里还能更好。",
}


def coach_addendum(depth):
    return ("\n\n【学习模式已开启】你现在兼任网文写作教练，面向新手：" + COACH_DEPTHS.get(depth, COACH_DEPTHS["2"]) +
            " 指出可改进处并鼓励作者动手。作者输入 /coach off 即回到正常写作模式。")


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


# ---------- 存稿 / 回溯 ----------

def sanitize(name):
    bad = '\\/:*?"<>|'
    return "".join("_" if c in bad else c for c in (name or "")).strip() or "未命名"


def book_dir(cfg):
    return os.path.join(cfg["output_dir"], sanitize(cfg["book"]))


def unique_path(path):
    """文件已存在就自增 _2/_3…，绝不覆盖（不丢稿）。"""
    if not os.path.exists(path):
        return path
    root, ext = os.path.splitext(path)
    i = 2
    while os.path.exists(f"{root}_{i}{ext}"):
        i += 1
    return f"{root}_{i}{ext}"


def write_text_file(path, title, text, fmt):
    if fmt == "docx":
        try:
            from docx import Document
        except ImportError:
            print("[提示] 未装 python-docx，本次改存 .txt（装 Word 支持：pip install python-docx）")
            return write_text_file(os.path.splitext(path)[0] + ".txt", title, text, "txt")
        doc = Document()
        if title:
            doc.add_heading(title, level=1)
        for line in text.split("\n"):
            doc.add_paragraph(line)
        doc.save(path)
    else:
        body = (("# " + title + "\n\n") if (fmt == "md" and title) else
                ((title + "\n\n") if title else "")) + text
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
    return path


def save_chapter(cfg, text, name=None):
    """把正文存进 书文件夹/正文/，按当前格式，命名不覆盖，返回绝对路径。"""
    name = sanitize(name) if name else "第" + datetime.datetime.now().strftime("%m%d_%H%M") + "章"
    folder = os.path.join(book_dir(cfg), "正文")
    os.makedirs(folder, exist_ok=True)
    path = unique_path(os.path.join(folder, f"{name}.{cfg['save_format']}"))
    write_text_file(path, name, text, cfg["save_format"])
    log_history(cfg, "save", path, len(text))
    return os.path.abspath(path)


def append_session_log(cfg, role, text):
    """自动记录：每轮都进 创作记录/对话记录.txt，永不丢。"""
    if not cfg.get("auto_log"):
        return
    folder = os.path.join(book_dir(cfg), "创作记录")
    os.makedirs(folder, exist_ok=True)
    p = os.path.join(folder, "对话记录.txt")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(p, "a", encoding="utf-8") as f:
        f.write(f"\n----- {role} · {ts} -----\n{text}\n")


def log_history(cfg, action, path, wordcount):
    """创作记录索引（类 git 的可回溯清单）：时间/动作/文件/字数。"""
    folder = os.path.join(book_dir(cfg), "创作记录")
    os.makedirs(folder, exist_ok=True)
    p = os.path.join(folder, "history.tsv")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(p, "a", encoding="utf-8") as f:
        f.write(f"{ts}\t{action}\t{os.path.abspath(path)}\t{wordcount}\n")


def show_history(cfg):
    p = os.path.join(book_dir(cfg), "创作记录", "history.tsv")
    if not os.path.exists(p):
        print("(还没有存稿记录。用 /save 存一章试试)")
        return
    print(f"《{cfg['book']}》创作记录（可回溯，文件都在：{os.path.abspath(book_dir(cfg))}）：")
    for line in read(p).splitlines():
        cols = line.split("\t")
        if len(cols) == 4:
            ts, act, path, wc = cols
            print(f"  {ts} | {act} | {wc}字 | {os.path.basename(path)}")


HELP = """命令一览（直接输文字=继续写；命令以 / 开头）：
  /help              本帮助
  /save [章名]        把【上一条回复】存成正文文件（不覆盖、存完显示路径）
  /book <书名>        设置当前书名（决定存到哪个书文件夹）
  /set format txt|md|docx   选存稿格式（默认 txt）
  /set dir <路径>     选存到哪个目录
  /set autolog on|off 自动记录每轮对话(永不丢) 开/关
  /config            看当前设置（书名/目录/格式/模型）
  /history           看创作记录、回溯写过什么（类 git）
  /proofread         校对上一条回复：错别字+敏感词，给 原词→建议词
  /coach [off]       学习模式 开/关
  /list              列出全部技能
  exit / quit / 退出  离开
"""


def print_config(cfg):
    print(f"当前设置：书名《{cfg['book']}》｜格式 .{cfg['save_format']}｜自动记录 {'开' if cfg['auto_log'] else '关'}")
    print(f"存稿目录：{os.path.abspath(book_dir(cfg))}")
    print(f"模型：{cfg['model']} @ {cfg['base_url']}")


def handle_command(line, cfg, client, messages, state):
    """返回 True 表示已处理掉这条命令（不发给模型）。"""
    parts = line.split()
    cmd = parts[0].lower()
    arg = line[len(parts[0]):].strip()

    if cmd == "/help":
        print(HELP)
    elif cmd == "/config":
        print_config(cfg)
    elif cmd == "/list":
        list_skills()
    elif cmd == "/book":
        if not arg:
            print("用法：/book 书名")
        else:
            cfg["book"] = arg
            save_prefs(cfg)
            print(f"当前书名设为《{cfg['book']}》，存稿目录：{os.path.abspath(book_dir(cfg))}")
    elif cmd == "/set":
        sp = arg.split(None, 1)
        key = sp[0].lower() if sp else ""
        val = sp[1].strip() if len(sp) > 1 else ""
        if key == "format" and val.lower() in SAVE_FORMATS:
            cfg["save_format"] = val.lower(); save_prefs(cfg); print(f"存稿格式设为 .{cfg['save_format']}")
        elif key == "dir" and val:
            cfg["output_dir"] = val; save_prefs(cfg); print(f"存稿目录设为：{os.path.abspath(book_dir(cfg))}")
        elif key == "autolog" and val.lower() in ("on", "off", "开", "关"):
            cfg["auto_log"] = val.lower() in ("on", "开"); save_prefs(cfg)
            print(f"自动记录已{'开启' if cfg['auto_log'] else '关闭'}")
        else:
            print("用法：/set format txt|md|docx ｜ /set dir <路径> ｜ /set autolog on|off")
    elif cmd == "/save":
        if not state.get("last_reply"):
            print("(还没有可保存的回复。先让我写点什么)")
        else:
            path = save_chapter(cfg, state["last_reply"], arg or None)
            print(f"✅ 已存：{path}")
    elif cmd == "/history":
        show_history(cfg)
    elif cmd == "/proofread":
        if not state.get("last_reply"):
            print("(没有可校对的内容。先写一段)")
        else:
            q = ("请用 proofread 技能校对下面这段网文：①错别字(按句意，给 原词→建议词) "
                 "②可能触发平台审核的敏感/违禁内容(标类别+替换建议，说明是启发式非平台确切词库)。"
                 "逐条列‘原句→建议’：\n\n" + state["last_reply"])
            messages.append({"role": "user", "content": q})
            print("工坊 > ", end="", flush=True)
            try:
                reply = chat_stream(client, cfg["model"], messages)
                messages.append({"role": "assistant", "content": reply})
                append_session_log(cfg, "校对", reply)
            except Exception as e:
                print("\n[错误]", e); messages.pop()
    elif cmd == "/coach":
        if arg.lower() == "off":
            if state.get("coach"):
                messages[0]["content"] = state["base_system"]
                state["coach"] = False
                print("已退出学习模式，回到正常写作。")
            else:
                print("当前不在学习模式。")
        else:
            print("进入学习模式。能教你：开篇钩子/爽点打脸/节奏呼吸/人设弧光/去AI味/投稿过稿 等。")
            print("怎么学？ 1) 速查清单(最快)  2) 详细讲解(原理+例子)  3) 边写边教")
            try:
                depth = input("选 1/2/3（回车默认2）：").strip() or "2"
            except (EOFError, KeyboardInterrupt):
                depth = "2"
            messages[0]["content"] = state["base_system"] + coach_addendum(depth)
            state["coach"] = True
            print(f"✅ 学习模式已开启（{COACH_DEPTHS.get(depth, COACH_DEPTHS['2'])[:12]}…）。说 /coach off 退出。")
    else:
        print(f"未知命令 {cmd}，输 /help 看全部命令。")
    return True


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

    state = {"base_system": system, "coach": False, "last_reply": ""}
    print_config(cfg)
    print("进入对话模式。直接说需求开写；输 /help 看命令（存稿/换格式/学习模式/校对/回溯），exit 退出。\n")
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
        if user.startswith("/"):
            handle_command(user, cfg, client, messages, state)
            continue
        messages.append({"role": "user", "content": user})
        append_session_log(cfg, "你", user)
        print("工坊 > ", end="", flush=True)
        try:
            reply = chat_stream(client, cfg["model"], messages)
            messages.append({"role": "assistant", "content": reply})
            state["last_reply"] = reply
            append_session_log(cfg, "工坊", reply)
        except Exception as e:
            print("\n[错误]", e)
            messages.pop()


if __name__ == "__main__":
    main()
