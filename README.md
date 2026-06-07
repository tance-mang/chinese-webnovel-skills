<div align="center">

# 网文工坊 · WebNovel Studio

**中文网络小说全流程写作 Claude Code 插件**

选题 → 灵感 → 大纲 → 黄金开篇 → 金手指 → 人设 → 正文扩写 → 爽点打脸 → 节奏标注 → 追读诊断 → 去AI味 → 投稿过稿 → 平台趋势

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet)](https://code.claude.com)
[![Skills](https://img.shields.io/badge/skills-18-brightgreen)](#-18-个技能)
[![Version](https://img.shields.io/badge/version-0.6.0-blue)](CHANGELOG.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-success)](#-参与贡献)

**简体中文** | [English](README.en.md)

</div>

---

> 一句话：让用 Claude 写中文网文的作者，从"零散复制 Prompt"升级到"一套懂网文商业逻辑的专业工具"。
> 男频女频双线全覆盖，适配 起点 / 番茄 / 晋江 / UC / 知乎盐选 / Webnovel(起点国际)，含同人合规与全品类题材库。

## 📑 目录

- [为什么用它](#-为什么用它)
- [安装](#-安装)
- [18 个技能](#-18-个技能)
- [典型流程](#-典型流程)
- [知识库](#-知识库)
- [项目结构](#-项目结构)
- [竞品对比](#-竞品对比真实不吹空白)
- [致谢与参考](#-致谢与参考)
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

> 适合：海外华人网文作者、国内出海作者、用 Claude Code / VSCode 码字的写手、想学写网文的新人。

## 🚀 安装

> 前置：已安装 [Claude Code](https://code.claude.com)（CLI 或 VSCode / JetBrains 插件均可）。

在 Claude Code 里依次输入：

```text
/plugin marketplace add tance-mang/chinese-webnovel-skills
/plugin install webnovel@webnovel-studio
```

装好后重启会话。验证：输入 `/webnovel:idea` 看到技能即成功。


## 📖 18 个技能

> 多数技能支持"**平台 + 频道 + 题材**"参数，如 `/webnovel:outline 番茄 男频 都市战神`、`/webnovel:idea 晋江 女频 古言宅斗`，自动适配平台节奏和题材套路。

| 技能 | 命令 | 干什么 |
|---|---|---|
| 💡 灵感成稿 | `/webnovel:spark` | 随手记灵感；一个灵感→大纲→初稿，可设字数和章节数 |
| 🎯 选题立意 | `/webnovel:idea` | 定频道/题材，给爆款选题 + 一句话卖点 + 黄金三章 |
| 🏷️ 网文起名 | `/webnovel:title` | 起书名/改名：带关键词+爽点+钩子，专治"太AI/太文艺/烂大街" |
| 🗺️ 大纲设计 | `/webnovel:outline` | 全书主线 / 卷纲 / 章纲，含伏笔总表 |
| 🪝 钩子设计 | `/webnovel:hook` | 开篇钩、章尾断章、付费节点钩 |
| ⚙️ 金手指 | `/webnovel:goldfinger` | 系统/签到/空间/模拟器…有门槛有代价的外挂 |
| 👤 人物设定 | `/webnovel:character` | 主角/反派/CP 人设卡，含成长弧光 |
| ✍️ 正文扩写 | `/webnovel:expand` | 把章纲写成可发布正文，控节奏控字数 |
| 🔥 爽点打脸 | `/webnovel:shuangdian` | 三段式爽感闭环 + 打脸四拍 + 爽点升级 |
| 🏷️ 正文标注 | `/webnovel:annotate` | 标出钩子/爽点/高潮/修饰词 + 出节奏数据表 |
| 🩺 追读诊断 | `/webnovel:review` | 五维体检：钩子/爽点/伏笔/人设/节奏 |
| 🧹 去AI味 | `/webnovel:deslop` | 把"AI腔/翻译腔"改成真人网文手感 |
| 📮 投稿过稿 | `/webnovel:submission` | 按平台签约标准体检三章 + 书名简介标签 |
| 📈 平台趋势 | `/webnovel:trends` | 联网实时调研平台流行题材/热门标签/榜单 |
| 🎓 写作教学 | `/webnovel:coach` | 学写小说（选择性开启，新手友好，讲原理） |
| 🎭 同人创作 | `/webnovel:fanfic` | 同人写作 + 版权合规检测（角色数/引用比例/平台政策） |
| 🔬 拆书对标 | `/webnovel:deconstruct` | 拆解平台爆款的结构套路，提炼可复用模板（学结构不抄字） |
| 🗄️ 创作档案 | `/webnovel:memory` | 记忆系统：存大纲/人设/伏笔/进度/投稿记录，跨会话续写，像 git 做快照 |

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

技能共享的 8 个参考库（`references/`），也是本插件的"网文 know-how"：

| 库 | 内容 |
|---|---|
| `hook-library.md` | 钩子库：开篇/章尾/付费节点，男女频各 6 例实战 |
| `trope-library.md` | 23 个爽点套路元素 + 触发机制 + 部署 |
| `goldfinger-types.md` | 金手指 10 大流派 + 四要素 + 防烂尾 |
| `title-library.md` | 网文起名库：男女频起名套路 + 关键词池 + 反AI起名清单 |
| `genre-library.md` | 全品类题材库：九大板块（悬疑/心理/都市/系统流/玄幻/女频/历史古代架空/灵异/小众）|
| `fanfic-guide.md` | 同人合规：各平台政策 + 版权红线 + 公版 IP + 安全改写 |
| `xiushi-ci.md` | 修饰词库：短平快爽文的"味儿"词 |
| `submission-guide.md` | 投稿过稿经验：各平台签约标准 |
| `platform-profiles.md` | 番茄/晋江/起点/UC/知乎盐选/Webnovel 调性 + 男女频偏好 + 同人政策 |
| `channel-guide.md` | 男频女频分流（底层爽点/剧情主线/开篇逻辑）|
| `writing-craft.md` | 网文写作基本功（教学用） |
| `project-memory.md` | 创作档案规范：文件结构 + 伏笔/进度/投稿记录格式 + git 快照 |

## 📂 项目结构

```
chinese-webnovel-skills/
├── .claude-plugin/
│   ├── plugin.json          # 插件清单
│   └── marketplace.json     # 插件市场清单
├── skills/                  # 18 个技能（每个一个 SKILL.md）
├── references/              # 12 个知识库
├── templates/               # 设定总纲 / 投稿记录 / 进度 模板
│   ├── book-bible-template.md
│   ├── submission-log-template.md
│   └── progress-template.md
├── README.md                # 中文（本文件）
├── README.en.md             # English
├── CHANGELOG.md             # 更新日志
├── PUBLISHING.md            # 上架发布指南
├── LICENSE                  # MIT
└── .gitignore
```

## 🆚 竞品对比（真实，不吹"空白"）

中文小说 Claude 插件已有真实玩家，本插件差异化是**唯一做"网文商业写作细分模块 + 数据诊断"的**：

| 项目 | 体量 | 定位 | 缺什么（本插件补上） |
|---|---|---|---|
| [PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) | 1.9k★ | 1 个大而全对话式 skill | 无细分模块、无爽点/钩子/金手指/投稿/数据诊断 |
| [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1.1k★ | 通用网文全流程(扫榜/拆文/封面) | 无金手指专项、无追读数据诊断、女频为主 |
| [yuzhoujishu/novel-writing](https://github.com/yuzhoujishu/novel-writing) | 数百★ | 通用小说 7 命令 | 通用文学，无网文商业逻辑 |

**本插件独家**：金手指专项 · 单章节奏标注(钩子/爽点/修饰词可视化) · 追读数据诊断 · 投稿过稿 · 平台趋势实时调研 · 灵感一键成稿 · 男女频全覆盖 · 写作教学。

> 不是"第一个"，是"最懂网文商业写作的那个"。各插件可共存混用。

## 🙏 致谢与参考

本项目为**原创 Prompt 工程**，未复制以下任何项目的代码；列出用于致谢与透明：

- **方法论种子**：核心钩子范例（6 例）与爽点套路（23 个）来自作者自己的写作素材《小说写作逻辑》。
- **插件规范参考**：[Claude Code 官方插件文档](https://code.claude.com/docs/en/plugins-reference) —— manifest 与技能格式。
- **同类项目研究（用于差异化定位，非抄袭）**：
  - [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) —— 网文全流程思路
  - [PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) —— 中文长篇创作
  - [yuzhoujishu/novel-writing](https://github.com/yuzhoujishu/novel-writing) —— 通用小说技能结构
  - [YILING0013/AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator) —— "设定→目录→章节→定稿"分阶段流程启发

感谢这些开源项目推动了 AI 网文创作生态。

## 📝 更新日志

完整记录见 [CHANGELOG.md](CHANGELOG.md)。

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
