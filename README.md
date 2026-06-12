<div align="center">

# 网文工坊 · WebNovel Studio

**中文网络小说全流程写作工具**
Claude Code 插件 · 也可用于 ChatGPT / DeepSeek / Gemini / Kimi 等任意大模型

选题 → 灵感 → 大纲 → 黄金开篇 → 金手指 → 人设 → 正文扩写 → 爽点打脸 → 节奏标注 → 追读诊断 → 去AI味 → 投稿过稿 → 平台趋势

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet)](https://code.claude.com)
[![Skills](https://img.shields.io/badge/skills-30-brightgreen)](#-30-个技能)
[![Version](https://img.shields.io/badge/version-0.26.0-blue)](CHANGELOG.md)
[![Models](https://img.shields.io/badge/AI-Claude·ChatGPT·DeepSeek·Gemini·Kimi-orange)](#-支持哪些-ai不止-claude)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-success)](#-参与贡献)

**简体中文** | [English](README.en.md)

</div>

---

> 一句话：让用 Claude 写中文网文的作者，从"零散复制 Prompt"升级到"一套懂网文商业逻辑的专业工具"。
> 男频女频双线全覆盖，适配 起点 / 番茄 / 晋江 / UC / 知乎盐选 / Webnovel(起点国际)，含同人合规与全品类题材库。

## 📑 目录

- [为什么用它](#-为什么用它)
- [安装](#-安装)
- [27 个技能](#-27-个技能)
- [典型流程](#-典型流程)
- [知识库](#-知识库)
- [项目结构](#-项目结构)
- [致谢](#-致谢)
- [更新日志](#-更新日志)
- [参与贡献](#-参与贡献)
- [许可证](#-许可证)

## ✨ 为什么用它

- **专为中文网文调校**：不是通用写作工具套壳，是按起点/番茄的爽点逻辑、打脸四拍、追读节奏写的。
- **吃 Claude 超长上下文**：200K token 装得下整本大纲 + 全书人设，写到几十万字不忘设定、不断伏笔。
- **全流程覆盖**：从"一个灵感"到"投稿过稿"，14 个技能各管一段。
- **数据化思维**：钩子/爽点/修饰词可视化标注、追读诊断、平台趋势——帮作者看见数据，不只是码字。
- **新手友好**：内置可选的写作教学陪练，想学就开，专心写就关。
- **中英双语文档**：英文不好的看中文，海外用户看英文。
- **不止 Claude**：一套方法论，可用于 ChatGPT / DeepSeek / Gemini / Kimi / 豆包 / 通义 / 智谱 / 文心 等任意大模型，见 [exports/SETUP.md](exports/SETUP.md)。
- **不止中文**：内置英文出海模块（Wattpad / Royal Road / Webnovel），写得像本地作者不像翻译腔 → `english` 技能。
- **不止插件**：可独立**终端运行**，接你自己的任意 API（DeepSeek / Kimi / 硅基 / OpenRouter / 本地 Ollama），见 [cli/](cli/)。

> 适合：海外华人网文作者、国内出海作者、用 Claude Code / VSCode 码字的写手、想学写网文的新人。

## 🚀 安装

> 前置：已安装 [Claude Code](https://code.claude.com)（CLI 或 VSCode / JetBrains 插件均可）。

在 Claude Code 里依次输入：

```text
/plugin marketplace add tance-mang/chinese-webnovel-skills
/plugin install webnovel@webnovel-studio
```

装好后重启会话。验证：输入 `/webnovel:idea` 看到技能即成功。


## 🌐 支持哪些 AI（不止 Claude）

方法论与模型无关——**任何能设系统提示词或建自定义智能体的 AI 都能用**。本仓库自带导出（`exports/`：`instructions.md` + 两个 `knowledge-*.md`）：

| AI | 怎么用 | 适合 |
|---|---|---|
| **Claude**（原生最佳） | Claude Code 插件，`/webnovel:xxx` | 海外、长篇、全流程 |
| **DeepSeek** | 网页传知识库+粘指令 / API 设 system | 国内主力码字，中文质量高 |
| **Gemini** | 建 Gem / AI Studio 设 system instructions | 海外、整本设定 |
| **Kimi** | 传文件+粘指令 / Kimi+ 智能体 | 喂整本参考 |
| **ChatGPT** | Custom GPT（粘指令+传知识库文件）| 习惯 ChatGPT 的 |
| **豆包/通义/智谱/文心** | 各家"创建智能体"，指令+知识库 | 国内日常、免梯子 |

详细分步（每家怎么配）见 **[exports/SETUP.md](exports/SETUP.md)**。
> 海外用 Claude/ChatGPT/Gemini，国内用 DeepSeek/Kimi/豆包——**一套方法论，哪个顺手用哪个**。加了新技能后跑 `python tools/build_exports.py` 重新生成导出即可同步。

## 📖 30 个技能

> 多数技能支持"**平台 + 频道 + 题材**"参数，如 `/webnovel:outline 番茄 男频 都市战神`、`/webnovel:idea 晋江 女频 古言宅斗`，自动适配平台节奏和题材套路。
> 写作**默认第一人称「我」**（更沉浸、像写亲身经历，尤其知乎/女频/短篇），动笔前会说明，需要第三人称随时切。

| 技能 | 命令 | 干什么 |
|---|---|---|
| 💡 灵感成稿 | `/webnovel:spark` | 随手记灵感；一个灵感→大纲→初稿，可设字数和章节数 |
| 🎯 选题立意 | `/webnovel:idea` | 定频道/题材，给爆款选题 + 一句话卖点 + 黄金三章 |
| 🏷️ 网文起名 | `/webnovel:title` | 起书名/改名：带关键词+爽点+钩子，专治"太AI/太文艺/烂大街" |
| 🗺️ 大纲设计 | `/webnovel:outline` | 全书主线 / 卷纲 / 章纲，含伏笔总表 |
| 🪝 钩子设计 | `/webnovel:hook` | 开篇钩、章尾断章、付费节点钩 |
| ⚙️ 金手指 | `/webnovel:goldfinger` | 系统/签到/空间/模拟器…有门槛有代价的外挂 |
| 👤 人物设定 | `/webnovel:character` | 主角/反派/CP 人设卡，含成长弧光 |
| 🪪 角色起名 | `/webnovel:name` | 给角色起名/改名：贴时代有记忆点，专治"叶辰苏念"烂大街 |
| ✍️ 正文扩写 | `/webnovel:expand` | 把章纲写成可发布正文，控节奏控字数 |
| 🔥 爽点打脸 | `/webnovel:shuangdian` | 三段式爽感闭环 + 打脸四拍 + 爽点升级 |
| 🌱 温暖现实 | `/webnovel:warmth` | 温暖治愈/现实向短篇：不狗血不说教不鸡汤，小冲突+生活细节+温暖余味 |
| 💬 对话台词 | `/webnovel:dialogue` | 写/改对话、金句、打脸装13台词，去AI对话腔，人物声音区分 |
| 🏷️ 正文标注 | `/webnovel:annotate` | 标出钩子/爽点/高潮/修饰词 + 出节奏数据表 |
| 🩺 追读诊断 | `/webnovel:review` | 六维体检：钩子/爽点/伏笔/人设/节奏/人味（读者留存视角）|
| 🧭 连贯检查 | `/webnovel:continuity` | 长篇逻辑+时间线：行为/因果/资源/身份/伤势/战力前后矛盾，揪出来给改法（防百万字失忆）|
| 🧹 去AI味 | `/webnovel:deslop` | 去AI腔/翻译腔、无缘无故的修辞、不搭的引用，改成真人手感 |
| 📊 AI味评分 | `/webnovel:aidetect` | AI味量化检测：比喻密度/连续同句式/句长波动/段落分布/情绪词重复 → 指数(0–10)+扣分定位 |
| 😢 情绪描写 | `/webnovel:emotion` | 把"我很心疼/我好痛苦"演出来，让读者自己感受（show don't tell）|
| 🫀 人味/失控感 | `/webnovel:human` | 治深层AI味：加非理性行为/情绪不完整/不闭环，让稿子像"情绪记录"不像"说明书" |
| 🌍 英文出海 | `/webnovel:english` | 写/改英文网文(Wattpad/Royal Road/Webnovel)，像本地作者不像翻译腔 |
| 🎬 剧本 | `/webnovel:script` | 写竖屏短剧/影视剧本、小说改剧本，正规格式，只写能拍的，每集强卡点 |
| ✅ 校对过审 | `/webnovel:proofread` | 错别字(的地得/在再)+敏感违禁词检查，像番茄后台标红+给"原词→建议词"一键替换 |
| 📮 投稿过稿 | `/webnovel:submission` | 按平台签约标准体检三章 + 书名简介标签 |
| 📈 平台趋势 | `/webnovel:trends` | 联网实时调研平台流行题材/热门标签/榜单 |
| 🔥 网络热梗 | `/webnovel:slang` | 联网搜当下抖音/小红书/微博热梗 + 按题材人物判断用得不突兀 |
| 🎓 写作教学 | `/webnovel:coach` | 学写小说（选择性开启，新手友好，讲原理） |
| 🎭 同人创作 | `/webnovel:fanfic` | 同人写作 + 版权合规检测（角色数/引用比例/平台政策） |
| 🔬 拆书对标 | `/webnovel:deconstruct` | 拆解平台爆款的结构套路，提炼可复用模板（学结构不抄字） |
| 🗄️ 创作档案 | `/webnovel:memory` | 记忆系统：存大纲/人设/伏笔/进度/投稿记录，跨会话续写，像 git 做快照 |
| 📄 修改草稿 | `/webnovel:draft` | 导出"供修改的 Word 草稿"：目录+第X章左对齐+【修改】红字建议，命名《书名》修改N不覆盖原文 |

> 技能也可由 Claude 按语境自动触发——直接说"帮我写个修真文开头"，它会自己调 `hook`。
> 教学（coach）只在你主动调用时出现，不会打扰正常码字。

## 🧭 典型流程

<details>
<summary><b>从一个灵感到初稿</b></summary>

```text
/webnovel:spark      → 记下灵感，或直接孵化成大纲+初稿（设定字数/章节数）
/webnovel:annotate   → 看初稿节奏数据
/webnovel:review     → 体检，按报告改
```
</details>

<details>
<summary><b>从零开新书（精写）</b></summary>

```text
/webnovel:idea       → 选定选题（频道+金手指+卖点）
/webnovel:goldfinger → 细化金手指
/webnovel:character  → 立主角和反派
/webnovel:outline    → 全书主线 + 第一卷卷纲 + 黄金三章章纲
/webnovel:hook       → 打磨第一章开篇钩
/webnovel:expand     → 写第 1 章正文
/webnovel:annotate   → 标注节奏，定点优化
/webnovel:review     → 体检前三章
```
</details>

<details>
<summary><b>投稿前 / 救稿</b></summary>

```text
/webnovel:trends     → 查目标平台当下流行什么
/webnovel:submission → 按签约标准体检三章 + 写简介标签
/webnovel:review     → 数据掉了？诊断追读为什么掉
```
</details>

<details>
<summary><b>新手学习</b></summary>

```text
/webnovel:coach      → 问写作问题 / 拆解套路 / 带教学改稿
```
</details>

## 📚 知识库

技能共享的 30 个参考库（`references/`），也是本插件的"网文 know-how"：

| 库 | 内容 |
|---|---|
| `hook-library.md` | 钩子库：开篇/章尾/付费节点，男女频各 6 例实战 |
| `trope-library.md` | 23 个爽点套路元素 + 触发机制 + 部署 |
| `goldfinger-types.md` | 金手指 10 大流派 + 四要素 + 防烂尾 |
| `title-library.md` | 网文起名库：男女频起名套路 + 关键词池 + 反AI起名清单 |
| `name-library.md` | 角色起名库：姓氏池 + 按题材/身份起名 + 反派宗门命名 + 避坑 |
| `genre-library.md` | 全品类题材库：九大板块（悬疑/心理/都市/系统流/玄幻/女频/历史古代架空/灵异/小众）|
| `fanfic-guide.md` | 同人合规：各平台政策 + 版权红线 + 公版 IP + 安全改写 |
| `xiushi-ci.md` | 修饰词库：短平快爽文的"味儿"词 |
| `dialogue-library.md` | 台词库：去AI对话腔 + 打脸/装13/反派/虐甜台词 + 金句 + 人物声音 |
| `anti-ai-checklist.md` | 去AI味(表面)：无缘无故修辞/不搭引用/语域/重复/极端词/句号当顿号/装饰符号 |
| `human-texture.md` | 人味/失控感(深层)：5种"像AI"感受 + 非理性/情绪不完整/不闭环 + 说明书vs情绪记录 |
| `ai-detector.md` | AI味量化：比喻密度/连续同句式/句长波动/段落分布/情绪词重复 八项指标+阈值+评分公式+定位 |
| `sentence-rhythm.md` | 句式节奏：长短句交错/偶尔长句/省略号破折号换行做呼吸/情绪话说一半（治"太顺"）|
| `dark-style.md` | 暗黑/灰度风格 + 爽文版vs高级暗黑版双版本输出 |
| `english-webfic.md` | 英文出海：Wattpad/RoyalRoad/Webnovel + 英文vs中文逻辑 + 英文钩子/排版/情绪/AI破绽 |
| `script-format.md` | 剧本格式：竖屏短剧/影视，只写能拍的，场景标题/台词/卡点 + 小说改剧本 |
| `show-emotion.md` | 情绪外显库：11 种情绪→神态/动作/生理/潜台词对照，演出来别喊 |
| `pov-guide.md` | 人称视角：默认第一人称(沉浸/像亲历) + 第三人称切换 + 知乎沉浸式 |
| `manuscript-format.md` | 稿件排版与改稿规范：Word输出/命名不覆盖/目录/第X章左对齐/【修改】标记/字数 |
| `warm-realism.md` | 温暖现实库：温度藏细节/先冷后暖/余味/反鸡汤 + 人物/情节/结局模板 |
| `slang-guide.md` | 网络热梗使用：不突兀6铁律 + 长青vs过气 + 按平台/题材(梗靠实时搜) |
| `case-studies.md` | 爆款拆解案例：结构/钩子/虐点/爽点/手法（学结构不抄字）|
| `submission-guide.md` | 投稿过稿经验：各平台签约标准 |
| `sensitive-words.md` | 校对过审：错别字高频对(的地得/及急/账帐) + 敏感违禁9大类自查 + 替换思路(启发式非平台词库)|
| `platform-profiles.md` | 番茄/晋江/起点/UC/知乎盐选/Webnovel 调性 + 男女频偏好 + 同人政策 |
| `length-standards.md` | 篇幅字数标准：番茄官方/全网通用/文学出版三套，短中长篇签约&分发门槛+怎么选篇幅 |
| `channel-guide.md` | 男频女频分流（底层爽点/剧情主线/开篇逻辑）|
| `writing-craft.md` | 网文写作基本功（教学用） |
| `project-memory.md` | 创作档案规范：文件结构 + 伏笔/进度/时间线/战力/语言指纹格式 + git 快照 |
| `continuity-check.md` | 连贯性/逻辑：六条逻辑链(行为/因果/资源/身份/伤势/战力)+时间线核对+长篇失忆三临界点 |

## 📂 项目结构

```
chinese-webnovel-skills/
├── .claude-plugin/
│   ├── plugin.json          # 插件清单
│   └── marketplace.json     # 插件市场清单
├── skills/                  # 30 个技能（draft 含 build_docx.py 生成 Word）
├── references/              # 30 个知识库
├── templates/               # 设定总纲 / 投稿记录 / 进度 模板
│   ├── book-bible-template.md
│   ├── submission-log-template.md
│   └── progress-template.md
├── exports/                 # 跨模型导出（通用）
│   ├── SETUP.md             # 各家 AI 怎么配（Claude/ChatGPT/DeepSeek/Gemini…）
│   ├── instructions.md      # 通用指令（智能体/系统提示词）
│   └── knowledge-*.md       # 技能+知识库文件（上传为知识库）
├── tools/build_exports.py   # 一键重新生成导出
├── cli/                     # 终端版：独立运行，接任意 API
│   ├── webnovel.py          # python webnovel.py
│   └── config.example.json  # 复制成 config.json 填 key
├── README.md                # 中文（本文件）
├── README.en.md             # English
├── CHANGELOG.md             # 更新日志
├── PUBLISHING.md            # 上架发布指南
├── LICENSE                  # MIT
└── .gitignore
```

## 🙏 致谢

- **方法论种子**：核心钩子范例与爽点套路来自作者本人的写作素材《小说写作逻辑》。
- 构建于 [Claude Code](https://code.claude.com) 公开的插件机制之上。
- 感谢开源社区与广大网文作者的创作智慧。

> 本项目所有技能与知识库均为**原创自研**，未包含或复制任何第三方项目的代码或受版权保护内容。采用 MIT 许可证开源。

## 📝 更新日志

完整记录见 [CHANGELOG.md](CHANGELOG.md)。

- **v0.26.0** — 校对过审(proofread)：错别字(的地得/在再/做作)+敏感违禁词9大类检查，像番茄后台"标红+一键替换"给"原词→建议词"；接入 submission（敏感词为启发式安全网，非平台确切词库）。**终端版 CLI 增强**：自动存稿不丢稿(默认txt/可选md·word、命名不覆盖、显示路径)、创作记录类git回溯(/history)、学习模式开关(/coach)、过审接进CLI(/proofread)，存稿偏好可 /set 不写死
- **v0.25.0** — 长篇四引擎补强：连贯检查(continuity 逻辑+时间线：行为/因果/资源/身份/伤势/战力) + AI味量化评分(aidetect：比喻密度/连续同句式/句长波动/段落分布/情绪词重复→指数0–10+定位) + 篇幅字数标准库 + 记忆系统增强(势力/战力/时间线/语言指纹)
- **v0.24.0** — 剧本(script)：竖屏短剧/影视剧本、小说改剧本，正规剧本格式，只写能拍的，每集强卡点
- **v0.23.0** — 终端版 CLI(独立运行接任意API：DeepSeek/Kimi/Ollama…) + 中文标点规范(省略号……/少用破折号/不滥用【】)
- **v0.22.0** — 英文出海(english)：Wattpad/Royal Road/Webnovel，写得像本地作者不像翻译腔（中文卖剧情爽点，英文卖情绪钩子）
- **v0.21.0** — Word 正文每段首行缩进 2 字符（firstLineChars=200，跟字号走）
- **v0.20.0** — 句式节奏(长短句交错/停顿标点/情绪话说一半，治"太顺") + 暗黑风格与"爽文版/暗黑版"双版本输出
- **v0.19.0** — 人味/失控感(human)：治深层AI味——非理性行为/情绪不完整/不闭环/私货，让稿子像"情绪记录"不像"说明书"；review 升六维
- **v0.18.0** — 网络热梗(slang)：联网搜当下抖音/小红书/微博热梗 + 6条铁律让梗用得不突兀不过气
- **v0.17.0** — 不用装饰符号(✦✨◆★)；draft 的 Word 章节标题改纯黑(去掉默认蓝色)
- **v0.16.0** — 去AI味深化：重复修辞/句式、同义反复(他非常生气他怒了)、极端词滥用、莫名陈述句、句号当顿号、段落过度对仗
- **v0.15.0** — 温暖现实(warmth)：温暖治愈/现实向短篇，不狗血不说教不鸡汤，温度藏细节、先冷后暖、留余味
- **v0.14.0** — 修改草稿(draft)：导出"供修改的Word草稿"，目录+第X章左对齐+【修改】红字建议+命名修改N不覆盖原文+短篇字数留余地
- **v0.13.0** — 多模型定位：导出通用化(exports/)，新增 DeepSeek/Gemini/Kimi/豆包/通义/智谱/文心 分步教程，不只 Claude
- **v0.12.0** — 人称视角：默认第一人称(更沉浸、像写亲身经历)，可切第三人称，动笔前表明；知乎盐选沉浸式强化
- **v0.11.0** — 情绪描写(emotion)：把"我很心疼"演出来，让读者自己感受（show don't tell）+ 情绪外显对照库
- **v0.10.0** — 去AI味升级(无缘无故修辞/跨度大引用/语域一致) + 番茄黄金300字与5类钩子 + 虐点设计 + 爆款拆解案例
- **v0.9.0** — 跨模型导出：ChatGPT Custom GPT(指令+知识库) + 通用系统提示词，`tools/build_exports.py` 一键生成
- **v0.8.0** — 对话台词(dialogue)：去AI对话腔、金句、打脸装13台词、人物声音区分
- **v0.7.0** — 角色起名(name)：贴时代有记忆点，专治角色名太AI/烂大街(叶辰苏念林婉儿)
- **v0.6.0** — 网文起名(title)：带关键词+爽点+钩子，专治书名太AI/太文艺/烂大街
- **v0.5.0** — 创作档案记忆系统(memory)：存大纲/人设/伏笔/进度、跨会话续写、git 快照、投稿拒因记录
- **v0.4.0** — 同人创作合规(fanfic)、拆书对标(deconstruct)、全品类题材库、五平台详版(修正芒果→UC/知乎)、平台题材参数化
- **v0.3.0** — 灵感成稿(spark)、写作教学(coach)、双语文档、致谢
- **v0.2.0** — 正文标注(annotate)、投稿(submission)、平台趋势(trends)、修饰词库、男频全覆盖
- **v0.1.0** — 首发，9 技能 + 5 知识库

## 🤝 参与贡献

欢迎 PR 和 Issue：

- 补充 `references/` 知识库（更多套路、平台数据、范例）
- 新增/优化技能
- 改进双语文档、翻译

改技能：编辑 `skills/<名字>/SKILL.md`，frontmatter 的 `description` 决定 Claude 何时自动触发。
本地校验：仓库根目录运行 `claude plugin validate .`。

## 📜 许可证

[MIT](LICENSE) © 2026 tance-mang。技能内的写作方法论可自由使用、修改、二次分发。

<div align="center">

**写得开心，订阅长虹** 🎉

[⬆ 回到顶部](#网文工坊--webnovel-studio)

</div>
