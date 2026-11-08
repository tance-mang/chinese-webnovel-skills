---
name: grok-write
description: 使用 Grok API 写小说、续写、翻译或改稿。适用于作者要接入 xAI、查看可用模型、用指定本地资料写作，或把结果另存为待改草稿。
---

# 用 Grok 写小说

使用 [Grok 写作入口](../../cli/README.md#grok-快速开始)。程序写作使用 xAI API，Grok Bot 做研究或评审时使用[手动交接](../../integrations/grokbot/README.md)。若作者没有 API Key，可准备本地任务文件，由作者在有权使用的 Grok 聊天里手动执行。

1. 核对作者已选的模型、语言、任务范围、篇幅，以及允许发送的原稿或设定。未配置模型时先执行 `python cli/webnovel.py --grok --models`。密钥只从本机环境变量读取。
2. 选择 `original`、`continue`、`adapt`、`translate` 或 `revise`。写作要求放 `--prompt-file`，可选材料用 `--source-file`。长篇只附当前章节所需的作者确认内容。实质改编沿用已确认决策，其余列为待定。
3. 写入新的 `--output` 文件，作为待作者采用的草稿。简述范围、稿件位置与缺失材料。续写核对上章衔接、角色知情与伏笔。只把作者采纳的内容写进正式档案。

连接失败、额度不足或拒绝时报告原因。作者明确重新选择前保持当前模型和书稿。投稿走 `submission`，并对照当日平台政策记录生成、辅助与翻译的实际用法。
