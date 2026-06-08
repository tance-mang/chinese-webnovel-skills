# -*- coding: utf-8 -*-
"""
把 skills/ + references/ 编译成跨模型可用的导出文件。
用法：python tools/build_exports.py
产出（exports/chatgpt/）：
  - knowledge-skills.md       所有技能工作流（上传为 Custom GPT 知识库）
  - knowledge-references.md   所有知识库（上传为 Custom GPT 知识库）
  - instructions.md           Custom GPT 指令（已存在则不覆盖，见说明）
源不变，导出随时重建，保证 ChatGPT 版和 Claude 版同步。
"""
import os, re, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def strip_frontmatter(text):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.S)
    if not m:
        return None, None, text
    fm = m.group(1)
    name = re.search(r'name:\s*(\S+)', fm)
    desc = re.search(r'description:\s*(.+)', fm)
    return (name.group(1) if name else None,
            desc.group(1).strip() if desc else None,
            m.group(2).strip())

def build_skills():
    out = ["# 网文工坊 · 技能工作流合集（知识库）\n",
           "> 本文件由 tools/build_exports.py 自动生成。每个技能=一段写作工作流。\n",
           "> 用户描述需求或点名技能时，按对应技能的工作流执行。\n"]
    files = sorted(glob.glob(os.path.join(ROOT, 'skills', '*', 'SKILL.md')))
    for f in files:
        name, desc, body = strip_frontmatter(read(f))
        out.append(f"\n\n{'='*60}\n## 技能：{name}\n**触发场景**：{desc}\n\n{body}")
    return '\n'.join(out), len(files)

def build_references():
    out = ["# 网文工坊 · 知识库合集\n",
           "> 本文件由 tools/build_exports.py 自动生成。供各技能调用的网文 know-how。\n"]
    files = sorted(glob.glob(os.path.join(ROOT, 'references', '*.md')))
    for f in files:
        out.append(f"\n\n{'='*60}\n{read(f)}")
    return '\n'.join(out), len(files)

def main():
    skills_md, nskills = build_skills()
    refs_md, nrefs = build_references()
    outdir = os.path.join(ROOT, 'exports', 'chatgpt')
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'knowledge-skills.md'), 'w', encoding='utf-8') as f:
        f.write(skills_md)
    with open(os.path.join(outdir, 'knowledge-references.md'), 'w', encoding='utf-8') as f:
        f.write(refs_md)
    # 版本号
    try:
        ver = json.load(open(os.path.join(ROOT, '.claude-plugin', 'plugin.json'), encoding='utf-8')).get('version', '?')
    except Exception:
        ver = '?'
    print(f"[OK] 导出完成 v{ver}: {nskills} 技能 + {nrefs} 知识库")
    print(f"  -> exports/chatgpt/knowledge-skills.md")
    print(f"  -> exports/chatgpt/knowledge-references.md")
    print("  指令文件 exports/chatgpt/instructions.md 为手写，未覆盖。")

if __name__ == '__main__':
    main()
