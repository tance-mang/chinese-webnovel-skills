# 网文工坊许可范围

当前公开仓库以根目录 [MIT 许可证](LICENSE) 为默认许可。此次提交只补充授权说明与待审草案，WSC-1.0 的生效版本和日期尚未确定，**当前没有模块采用 WSC-1.0**。

## 历史基线与来源核查

- 以 [提交 `07ce8d4`](https://github.com/tance-mang/chinese-webnovel-skills/tree/07ce8d4363da12b40440181f19194f4631a6f26d) 作为此次整理前的 MIT 快照。该快照的许可证见[历史原文](LICENSES/MIT-HISTORICAL.txt)。主线中 `LICENSE` 的可见路径历史始于 [`4edca5b`](https://github.com/tance-mang/chinese-webnovel-skills/commit/4edca5bb54270089db5d12d7e1cebdfd16984054)，截至基线只有该次修改。核查时没有发现 Git 标签或 GitHub Release，版本号以仓库文件和提交为据。
- 基线可见的 37 个提交均关联 GitHub 账号 `tance-mang`。提交记录反映署名和修改历史，不能单独证明素材来源或重新授权的权利。启用新许可前，须逐项确认来源、权利人和书面授权依据。
- 此前按 MIT 获得的材料仍可依 MIT 使用、修改、分发和销售，分发时保留版权与许可声明。未来若同一包包含 MIT 内容和受限新增内容，应分别标明边界，既有 MIT 许可继续适用。

## 模块范围表

| 文件或模块 | 当前适用范围 | 核查依据与后续要求 |
|---|---|---|
| `skills/**` | 仓库提供的 Skill、提示词和脚本按 MIT | 包括 Word 导出脚本。拟限制的新增内容须另列路径与首发版本 |
| `references/**` | 仓库自有说明与示例按 MIT | `case-studies.md` 涉及作品拆解，`sensitive-words.md` 有平台发布页提示整理。素材库范例和外部资料的原始权利仍需查证，仓库许可不替第三方授权 |
| `templates/**` | 仓库提供的空白模板按 MIT | 作者填入的稿件、档案与素材依各自权利处理 |
| `cli/**`、`tools/**` | 仓库脚本及其文档按 MIT | `openai` 和 `python-docx` 由使用环境安装，属于外部依赖，适用各自发行版本的条款 |
| `exports/**` | 当前公开指令、生成器输出和使用说明按 MIT，引用的第三方材料保留各自权利 | 两份 `knowledge-*.md` 分别合并 `skills/` 与 `references/`。混合许可发布前须按输入来源拆分或标明产物范围 |
| `.claude-plugin/**`、仓库配置、README、变更日志及许可说明 | 当前公开项目文件按根许可 | 插件清单声明 MIT。若未来单独发受限包，须用对应的包清单和授权说明 |
| `LICENSE`、`LICENSES/MIT-HISTORICAL.txt` | 当前许可原文与历史副本 | 历史副本逐字保留 |
| `LICENSES/WSC-1.0.txt` | 待审许可文本 | 仅供审阅。没有生效范围、日期或发布版本 |

外部平台、作品、商标、字体和用户上传材料的权利由各自权利人和条款决定。公开仓库里的文字说明不改变这些权利。

## 分发检查

截至基线，仓库没有 GitHub Actions 工作流或 Release 打包流程。当前入口包括 GitHub 仓库及 Claude Code marketplace、从仓库运行的 CLI、由 `tools/build_exports.py` 生成并单独上传的知识库文件。整仓分发已带根 `LICENSE`，单独再分发 Skill、CLI 或知识库文件时，应一并保留 MIT 的版权与许可声明。导出脚本目前不为产物附加许可证，使用说明已补上这一点。

启用 WSC 之前，先列清新增模块的路径、许可与来源，再检查插件/marketplace 声明、单文件导出、压缩包及安装说明。现有导出脚本会汇总目录里的全部内容，受限模块应放在独立包或生成器明确排除的目录，直到混合分发方案通过审核。首个生效版本由维护者另行决定并记录。
