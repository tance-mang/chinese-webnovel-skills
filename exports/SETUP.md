# 在 ChatGPT / 其他大模型里用「网文工坊」

> Claude 插件格式装不进 ChatGPT，但方法论是通用的。下面教你把它搬到 ChatGPT 和别的模型。
> 所有文件由 `python tools/build_exports.py` 从 skills+references 自动生成，**改了插件重跑一次就同步**。

---

## 方式一：ChatGPT 做成 Custom GPT（推荐，需 ChatGPT Plus）

一次设置，以后像用一个"网文助手 App"。

1. ChatGPT 左下角 → **Explore GPTs** → 右上 **+ Create** → 切到 **Configure** 标签
2. **Name**：网文工坊　**Description**：中文网文写作助手
3. **Instructions**：把 [`chatgpt/instructions.md`](chatgpt/instructions.md) 全文**复制粘贴**进去
4. **Knowledge** → **Upload files**，上传这两个文件：
   - [`chatgpt/knowledge-skills.md`](chatgpt/knowledge-skills.md)（20 个技能工作流）
   - [`chatgpt/knowledge-references.md`](chatgpt/knowledge-references.md)（14 个知识库）
5. 保存（Create）。完成。

**怎么用**：进这个 GPT，直接说人话或点名技能：
- "用 title 帮我起书名，番茄女频系统流推理"
- "用 name 起个冷静侧写师女主的名字"
- "把这句对话改得不那么 AI：……"
- "帮我从这个灵感写个大纲：……"

---

## 方式二：ChatGPT 不开 Plus（用 Projects 或直接粘）

- **Projects**：建一个 Project → 在 Project 的"指令/Instructions"里粘 `instructions.md` → 把两个 knowledge 文件作为 Project 文件上传。
- **临时用**：新开对话，第一条消息粘 `instructions.md`，需要某个技能时再把 `knowledge-skills.md` 里那段贴进去。

---

## 方式三：延伸到其他模型（Gemini / DeepSeek / Kimi / 文心 / 通义）

方法论与模型无关，通吃：

- **能设系统提示词的**（API、DeepSeek/Kimi 网页的"系统设定"）：把 `instructions.md` 设为 system prompt。
- **支持传文件的**（Gemini、Kimi）：把两个 knowledge 文件作为附件/资料上传，再贴 `instructions.md`。
- **啥都不支持的**：新对话第一条贴 `instructions.md`，用到哪个技能就把对应段落贴进去。

> 国产模型在国内访问稳定，适合你在国内写；ChatGPT/Claude 适合海外。一套方法论，哪个顺手用哪个。

---

## 保持同步（重要）

你以后给 Claude 插件加了技能，**导出文件不会自动变**。重新生成一次：
```bash
python tools/build_exports.py
```
然后把新的 `knowledge-skills.md` / `knowledge-references.md` 重新上传到 Custom GPT（覆盖旧的）。指令 `instructions.md` 一般不用改，除非技能清单变了。

---

## 各方案对比

| | Claude Code 插件 | ChatGPT Custom GPT | 通用系统提示词 |
|---|---|---|---|
| 调用方式 | `/webnovel:xxx` 斜杠 | 说人话 / 点名技能 | 说人话 / 点名技能 |
| 自动读知识库 | ✅ 原生 | ✅ 上传后检索 | ⚠️ 需手动贴 |
| 跨会话记忆 | ✅ memory 技能 | ⚠️ 靠 GPT 记忆/手动 | ⚠️ 手动 |
| 适合 | Claude Code/VSCode | ChatGPT 用户 | 任何模型 |
