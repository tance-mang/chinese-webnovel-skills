# 网文工坊 · 终端版（独立运行，接任意 API）

不依赖 Claude，在你电脑终端直接跑，接**你自己的 API key**（DeepSeek / Kimi / 硅基流动 / OpenRouter / 通义 / OpenAI / 本地 Ollama，任意 OpenAI 兼容接口）。

## 一、装（一次）

需要 Python 3.9+，然后装一个依赖：
```bash
pip install openai
```

## 二、配 API（三选一）

**方式 A：配置文件（推荐）**
把 `config.example.json` 复制成 `config.json`，填你的 key：
```json
{
  "base_url": "https://api.deepseek.com/v1",
  "api_key": "sk-你的key",
  "model": "deepseek-chat"
}
```
各家服务商的 base_url 和 model，`config.example.json` 里都列好了，照抄即可。

**方式 B：环境变量**
```bash
# Windows PowerShell
$env:WN_API_KEY="sk-你的key"
$env:WN_BASE_URL="https://api.deepseek.com/v1"
$env:WN_MODEL="deepseek-chat"
```

**方式 C：什么都不配**，直接跑，它会问你要 key。

## 三、用

```bash
# 进入对话模式（像聊天一样）
python webnovel.py

# 一次性
python webnovel.py "用 hook 写个修真文开头，番茄男频"

# 列出全部技能
python webnovel.py --list

# 加载完整技能+知识库（需大上下文模型，能力最全）
python webnovel.py --full
```

进对话模式后，直接说人话或点名技能：
```
你 > 用 title 起书名，番茄女频系统推理
你 > 把这段去掉AI味：……
你 > english 用 Native Mode 写个 Wattpad 开头
```
输入 `exit` 退出。

## 四、哪个 API 适合写网文
- **国内主力**：DeepSeek（中文质量高、便宜、访问稳）。
- **长上下文/喂整本**：Kimi。
- **白嫖**：硅基流动（注册送额度）、OpenRouter 的 `:free` 模型。
- **断网/免费**：本地 Ollama（`ollama run qwen2.5:14b`，base_url 填 `http://localhost:11434/v1`）。
- **海外**：OpenAI / 直接用 Claude。

## 五、它和插件什么关系
- **同一套方法论**：CLI 读的是 `../exports/instructions.md` + 知识库，和 Claude 插件同源。
- 你给插件加了新技能后，跑一次仓库根目录的 `python tools/build_exports.py` 重新生成导出，CLI 立刻同步。
- 想随处可用：把仓库放在固定目录，给 `webnovel.py` 配个快捷命令/别名即可。

> 注意：`config.json`（含你的 key）已被 `.gitignore` 排除，不会上传。
