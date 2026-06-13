# 在各家 AI 里用"网文工坊"

> 这套方法论**和模型无关**——任何能"设系统提示词"或"建自定义智能体"的 AI 都能用。
> Claude 是原生插件形态；其它模型用本目录的 3 个文件：
> - `instructions.md` —— 指令（智能体的"大脑" / 系统提示词）
> - `knowledge-skills.md` —— 21 个技能工作流（知识库）
> - `knowledge-references.md` —— 18 个知识库（知识库）
>
> 所有文件由 `python tools/build_exports.py` 自动生成，**改了插件重跑一次就同步**。

---

## 通用规律（看这一条基本就够）

| 你的 AI 支持… | 怎么用 |
|---|---|
| **建自定义智能体**（Custom GPT / Gemini Gem / 豆包/通义/智谱/文心 智能体） | 指令框粘 `instructions.md`，知识库上传两个 `knowledge-*.md`。一次配置，长期用。 |
| **只能设系统提示词**（API、部分网页的"系统设定"） | 系统提示词放 `instructions.md`；要用到的知识库段落按需贴。 |
| **啥都不支持，只能聊天** | 新对话第一条粘 `instructions.md`；支持传文件就把两个 `knowledge-*.md` 传上去，否则用到哪段贴哪段。 |

---

## 分平台具体步骤

### 🟣 Claude（原生，最佳）
Claude Code 里 `/plugin marketplace add tance-mang/chinese-webnovel-skills` + `/plugin install webnovel@webnovel-studio`。直接 `/webnovel:xxx`。

### 🟢 ChatGPT
- **Plus**：Explore GPTs → Create → Configure，指令粘 `instructions.md`，Knowledge 上传两个 `knowledge-*.md`。
- **免费**：用 Projects 或新对话粘指令。

### 🔵 DeepSeek（中文写作强，推荐）
- **网页 chat.deepseek.com**：新建对话，**上传**两个 `knowledge-*.md`，再把 `instructions.md` 作为第一条消息发出去。
- **API**：`system` 角色放 `instructions.md`，知识库随消息带上或检索。
- 国内访问稳定，写中文网文质量高。

### 🟡 Gemini（Google）
- **Gemini 网页 → Gems（自定义 Gem）**：新建 Gem，指令粘 `instructions.md`，上传两个 `knowledge-*.md`。用法同 Custom GPT。
- **Google AI Studio**：System instructions 字段放 `instructions.md`，可上传文件；免费额度大，适合长文。
- 需要梯子。

### 🟠 Kimi（月之暗面，长上下文）
- 网页传两个 `knowledge-*.md` 文件 + 粘 `instructions.md`；或用"Kimi+"建智能体。
- 超长上下文，适合整本大纲/全书设定常驻。

### 🔴 国产智能体（豆包 / 通义千问 / 智谱清言 / 文心一言）
这几家都有"创建 AI 智能体/智能体中心"：
- **人设/指令**：粘 `instructions.md`
- **知识库**：上传两个 `knowledge-*.md`
- 没有智能体功能的，就新对话粘指令 + 传文件。
- 优点：国内免实名梯子、访问稳。

---

## 哪个 AI 写网文更合适？

| AI | 特点 | 适合 |
|---|---|---|
| Claude | 超长上下文、长文连贯最稳、原生插件 | 海外、长篇、全流程 |
| DeepSeek | 中文网文质量高、便宜、国内稳 | 国内主力码字 |
| Gemini | 免费额度大、长上下文 | 海外、整本设定 |
| Kimi | 长上下文、传文件方便 | 喂整本参考 |
| 豆包/通义/智谱/文心 | 国内稳、有智能体 | 国内日常 |
| ChatGPT | 生态成熟、Custom GPT 好用 | 习惯 ChatGPT 的 |

> 海外用 Claude/ChatGPT/Gemini，国内用 DeepSeek/Kimi/豆包——**一套方法论，哪个顺手用哪个**。

---

## 保持同步
加了新技能后，跑 `python tools/build_exports.py` 重新生成，把新的两个 `knowledge-*.md` 重新上传到你的智能体即可。指令 `instructions.md` 一般不用动。
