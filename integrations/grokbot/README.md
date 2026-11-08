# Grok Bot 手动交接

此工具在本机创建任务包、校验回传结构并生成待审建议。没有自动上传或触发，作者自行把任务包交给 Grok Bot。Grok Bot 会话与 CLI 里使用的 xAI 文本 API 分开配置。

从仓库根目录运行。`brief.md` 是 UTF-8 任务说明。默认不包含书稿，作者可用 `--excerpt chapter-excerpt.txt` 明确选择可外发片段。

```sh
python integrations/grokbot/handoff.py export research brief.md task.md
python integrations/grokbot/handoff.py import task.md result.json review.json
```

也可导出 `task.json`。将任务包与以下结果格式交给评审模型，把实际任务包里的 `task_id` 原样带回。

```json
{
  "schema": 1,
  "task_id": "任务包中的 task_id",
  "findings": [
    {
      "observation": "发现或英文片段的问题位置",
      "suggestion": "建议、查阅日期和待核查项",
      "sources": []
    }
  ]
}
```

平台研究用官方页面 URL 填写 `sources`，区分政策、经验和推测。创作建议可留空。导入仅校验结构、任务 ID 和链接形式，来源内容仍由作者复核。输出全为待作者确认，原始章节不在写入路径中，任何已有输出文件也不会被覆盖。
