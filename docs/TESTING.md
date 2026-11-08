# 国际化升级审计与测试

测试日期为 2026-11-08（UTC+8）。基线是 `07ce8d4363da12b40440181f19194f4631a6f26d`。测试在 Windows、Python 3 本地工作目录中运行，验证本次 PR 工作树。基线包含 33 个技能、32 份参考库，未发现仓库测试目录或 Actions 流程。本次构建为 38 个技能、35 份参考库。

| 审计对象 | 风险与处理 |
|---|---|
| 既有中文工作流与 Claude Code | 保留所有旧技能目录和调用名。英文规则独立，扩展审稿、记忆、连续性与投稿的相关入口。插件清单与版本未改 |
| 英文工作流 | 旧规则的固定句长比例和转折间隔容易覆盖作者选择。把类型、原创／改编／翻译、母语化编辑和关系张力拆分，供旧英文入口调用 |
| CLI 配置 | 旧版只持有一个模型。兼容原字段及环境变量，命名配置从指定环境变量取密钥，切换需要确认，服务失败不自动改派 |
| 知识库与分发 | 生成文件分别来自 `skills/` 与 `references/`。构建时重写有效的本地文档链接，并校验生成内容。README 数量与实际文件对应 |
| 平台资料 | 可核查事实与待核实字段分别列出。Radish 移为历史平台，平台政策不作为类型规则。后续可以导入 Grok 的独立研究结果供人工复核 |

从仓库根目录执行：

| 检查 | 结果 |
|---|---|
| `python -X utf8 tools/build_exports.py` | 退出码 0。构建 38 个技能、35 份参考库 |
| `python -X utf8 -m unittest discover -s tests -v` | 退出码 0。13 个离线测试通过。首轮 Mock 流未正确实现测试使用的迭代协议，调整为使用上下文返回的迭代器后重跑通过 |
| `python -X utf8 -m py_compile cli/webnovel.py cli/providers.py integrations/grokbot/handoff.py tools/build_exports.py` | 退出码 0 |
| `python -X utf8 cli/webnovel.py --list` | 退出码 0。返回 38 个技能，不请求 API |

测试覆盖旧配置与 `WN_MODEL`、xAI Responses 与兼容 Chat 的模拟流、用量及费用估算、拒绝与未完成流、脱敏错误、切换确认、Ollama 模型列表、双模型相同输入、交接导入与拒绝覆盖、技能元数据和导出链接。详细断言见 [测试代码](../tests/test_international.py)。

[两个英文原创示例](../references/english-genre-profiles.md)和[中文改编示例](../references/bilingual-adaptation.md)用于人工复测。改编示例保留返还金额、收款人、退婚未公开、哥哥知情而未婚夫不知情。创作质量与模型实际遵循档案的程度仍需真人盲评。本轮未调用真实 xAI、Claude 或 Ollama 服务，未验证账户模型、账单、Claude Code 安装或平台账号后台。Grok Bot 的真实研究结果待单独交接。
