# 更新日志 · Changelog

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。
All notable changes are documented here. This project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.6.0] - 2026-06-05

### 新增 Added
- 🏷️ **title（网文起名）**：生成/优化书名，强制"题材关键词 + 爽点 + 钩子"，专治 AI 起名通病（抽象文艺 / 烂大街 / 无关键词）。给安全款+大胆款多个候选并说明点击率逻辑。
- 📚 **title-library.md**：起名库——男女频起名套路公式、按题材的关键词池、反 AI 起名 6 原则、起名自检清单、反例对照。

### 变更 Changed
- `idea` 接入起名库，开书卡的书名候选不再平庸；并修正其平台枚举（移除七猫，改 番茄/晋江/起点/UC/知乎/Webnovel）。
- 技能总数 17 → 18，知识库 11 → 12。

---

## [0.5.0] - 2026-06-05

### 新增 Added
- 🗄️ **memory（创作档案 / 记忆系统）**：在书的文件夹维护持久化档案（设定/人物/大纲/伏笔/灵感/进度/投稿记录），跨会话回顾"写到哪了"，支持 git 版本快照（像 git 一样可回滚看历史）。
- 📚 **project-memory.md**：创作档案规范，定义文件结构与伏笔/进度/投稿记录格式。
- 📄 **templates/submission-log-template.md**：投稿记录模板，专门记"为什么没过"+ 高频拒因归纳。
- 📄 **templates/progress-template.md**：进度模板，一键续写。

### 变更 Changed
- `submission` 接入投稿记录：投稿前读历史**高频拒因**避免重犯，投稿后追加记录，累计 3 次以上的拒因标签视为系统性问题。
- 技能总数 16 → 17，知识库 10 → 11。

---

## [0.4.0] - 2026-06-05

### 新增 Added
- 🎭 **fanfic（同人创作 + 版权检测）**：结合各平台同人政策给创作方案，自动校验角色数/原文引用比例/平台能否变现/OOC 红线。
- 🔬 **deconstruct（拆书对标爆款）**：拆解平台爆款的开篇/金手指/爽点/节奏结构，提炼可复用模板，严守"学结构不抄字"。
- 📚 **genre-library.md**：全品类题材库九大板块（悬疑/心理/都市/系统流/玄幻仙侠/女频/历史古代架空/灵异/年代乡土/小众），补全架空历史、中国古代等。
- 📚 **fanfic-guide.md**：同人合规库（各平台政策、版权红线、公版 IP、安全改写、海外蓝海）。

### 变更 Changed
- 🔧 **修正"芒果"**：移除误加的短剧平台"芒果"，`platform-profiles.md` 重写为 **番茄/晋江/起点/UC/知乎盐选/Webnovel** 详版，含男女频精准偏好、篇幅、同人政策。
- `channel-guide.md` 增补"底层爽点 / 剧情主线 / 开篇逻辑"三行男女频对照。
- 选型技能（idea/outline/spark）接入题材库，支持"平台 + 频道 + 题材"参数。
- 技能总数 14 → 16，知识库 8 → 11。

---

## [0.3.0] - 2026-06-05

### 新增 Added
- 💡 **spark（灵感成稿）**：灵感速记到灵感本；一个灵感一键孵化成大纲与初稿，支持设定总字数/单章字数并自动分章节。
- 🎓 **coach（写作教学）**：面向新手的写作陪练，讲原理、拆套路、带教学改稿。**选择性开启**，只在主动调用时出现。
- 📚 **writing-craft.md**：网文写作基本功教学库（六大基本功 + 新手十大错误）。
- 🌐 **双语文档**：新增英文 `README.en.md`，中英互相切换。
- 🙏 **致谢与参考**章节：透明列出方法论种子与研究借鉴的开源项目。

### 变更 Changed
- README 重写为 GitHub 规范版（徽章、目录、可折叠流程、致谢、贡献指南）。
- 作者与仓库地址更新为 `tance-mang`。
- 技能总数 12 → 14，知识库 7 → 8。

---

## [0.2.0] - 2026-06-05

### 新增 Added
- 🏷️ **annotate（正文标注）**：行内标注钩子/爽点/高潮/打脸/伏笔/修饰词，输出单章节奏数据表。
- 📮 **submission（投稿过稿）**：按平台签约标准体检三章，生成书名/简介/标签。
- 📈 **trends（平台趋势）**：联网实时调研平台流行题材、热门标签、榜单。
- 📚 **xiushi-ci.md**：修饰词库（短平快爽文的强化词/围观反应词/拟声/短句）。
- 📚 **submission-guide.md**：各平台投稿与过稿经验库。

### 变更 Changed
- `hook-library.md` 男频开篇范例扩充至 6 例（玄幻/都市/系统/历史/末世），男女频平衡。
- 平台库扩展更多平台调性。（注：v0.4 修正——移除短剧平台"芒果"，改用 UC / 知乎盐选）
- 竞品对比改为真实数据（chinese-novelist 1.9k★、oh-story 1.1k★），不再宣称"赛道空白"。

---

## [0.1.0] - 2026-06-05

### 新增 Added
- 首发 9 个技能：idea / outline / hook / goldfinger / character / expand / shuangdian / review / deslop。
- 5 个知识库：hook-library / trope-library / goldfinger-types / platform-profiles / channel-guide。
- 方法论种子来自作者《小说写作逻辑》（6 个开篇钩 + 23 个爽点套路）。
- 插件清单、市场清单、MIT 许可证、book-bible 模板、发布指南。
- 通过 `claude plugin validate` 校验。

[0.3.0]: https://github.com/tance-mang/chinese-webnovel-skills/releases/tag/v0.3.0
[0.2.0]: https://github.com/tance-mang/chinese-webnovel-skills/releases/tag/v0.2.0
[0.1.0]: https://github.com/tance-mang/chinese-webnovel-skills/releases/tag/v0.1.0
