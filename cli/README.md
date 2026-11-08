# 网文工坊 · 终端版（独立运行，接任意 API）

不依赖 Claude，在你电脑终端直接跑，接**你自己的 API key**（DeepSeek / Kimi / 硅基流动 / OpenRouter / 通义 / OpenAI / 本地 Ollama，任意 OpenAI 兼容接口）。

> 一句话：**终端版是个"壳"，你给它接一个 AI（填个 key），它就用本工坊的全套网文方法帮你写。** 不会写代码也能用，照下面四步走。

---

## 🟢 零基础部署（不会写代码 / 没用过 Claude 也能跑）

### 第一步：装 Python（只需一次）
到 <https://www.python.org/downloads/> 下载安装。**Windows 安装第一屏务必勾选“Add Python to PATH”**，否则后面找不到。（Mac 一般自带 python3，可跳过。）

### 第二步：下载本工具
- 会用 git：`git clone https://github.com/tance-mang/chinese-webnovel-skills.git`
- 不会 git：打开仓库页 → 绿色 **Code** 按钮 → **Download ZIP** → 解压到一个你找得到的文件夹。

### 第三步：启动（自动装依赖）
- **Windows**：进 `cli` 文件夹，**双击 `启动.bat`**。第一次会自动装依赖 `openai`，然后打开工坊。
- **Mac / Linux**：终端里 `cd` 到 `cli` 文件夹，运行 `bash start.sh`。
- （不想用脚本也行：终端里跑 `pip install openai` 再 `python webnovel.py`。）

### 第四步：接你的 AI（填一个 key）
第一次启动会问你要 **API Key**——这就是"接你用的 AI"。没有就先回车跳过，**有了再来**。哪里弄 key（都有免费额度，选一家）：
| 服务商 | 怎么拿 | 适合 |
|---|---|---|
| **硅基流动** | 注册送额度，控制台建 key | 新手白嫖，多模型 |
| **DeepSeek** | platform.deepseek.com 充一点点 | 中文网文质量高、便宜 |
| **OpenRouter** | 有 `:free` 免费模型 | 免费试 |
| **Kimi** | platform.moonshot.cn | 长上下文、喂整本 |

拿到 key 后，**两种填法二选一**：
1. 把 `cli/config.example.json` 复制成 `cli/config.json`，把 key 填进 `api_key`（一劳永逸，下次不再问）；
2. 直接在启动时**粘贴** key（临时用）。

搞定。以后写作就是：**双击 `启动.bat` → 说人话写**。

---

## 一、装（给会命令行的人，一次）

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

## 三点五、存稿 / 学习模式 / 校对 / 回溯（对话里的命令，/ 开头）

> 终端写的正文默认**不会丢**：每轮自动记到 `书/创作记录/对话记录.txt`；满意的章再 `/save` 存成正文文件，**存完会显示完整路径**，命名重复自动 `_2` 不覆盖。格式优先 **.txt**（记事本就能开，不用编辑器），也能换 word/md，**都可选、不写死**。

```
/help                  看全部命令
/mode                  四个入口菜单（不知道用啥先看这个）
/new /continue /optimize /submit   新建 / 继续写 / 优化 / 投稿（自动走流程、自动调技能）
/co [我写的一段]        共写·辅助：给一个短示范或续写片段，作者修改后可用 /save 保存当前回复
/director              共写·导演：填 目标/冲突/情绪/节奏，AI 出多版正文挑一个
/write [需求]           自动写：按章纲/需求直接出整段正文
/save 第1章             把上一条回复存成正文（不覆盖，显示路径）
/book 我的修真路        设当前书名（决定存哪个书文件夹）
/set format txt|md|docx 选存稿格式（默认 txt，word 需 pip install python-docx）
/set dir D:\我的小说     选存到哪个目录
/set autolog on|off     自动记录每轮(永不丢) 开/关
/config                看当前设置（书名/目录/格式/模型）
/history               看创作记录、回溯写过什么（类 git）
/proofread             校对上一条：错别字 + 敏感词，给 原词→建议词
/coach                 开学习模式（进入时选讲解方式）；/coach off 退出
/list                  列出全部技能
```

存稿目录结构（和插件 `memory` 档案一致，`continuity`/`review` 能直接读）：
```
output/《书名》/
├── 正文/第1章.txt        # /save 存的章节（你命名、不覆盖）
└── 创作记录/
    ├── 对话记录.txt       # 每轮自动记，永不丢
    └── history.tsv       # 存稿时间/文件/字数，回溯用
```

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

## 多模型配置与对照

已有的 `base_url`、`api_key`、`model` 或 `WN_*` 环境变量继续走 `legacy`。新配置把模型设在 `providers` 下，密钥只通过 `api_key_env` 指定的环境变量读取。复制 `config.example.json` 后，把模型占位符换成账号或 Ollama 中实际可用的模型 ID。xAI 使用 OpenAI Python SDK 的 Responses 接口，需要支持 `client.responses` 的版本，可用 `python -m pip install -U openai` 更新。兼容旧接口时在该配置里加 `"api_mode": "chat"`。

从 `cli/` 启动英文写作或本地化，可用 `python webnovel.py --full --provider xai` 或 `python webnovel.py --full --provider local`。把密钥先放入本机环境变量。xAI 默认读 `XAI_API_KEY`，本机 Ollama 无需真实密钥。[xAI 流式文档](https://docs.x.ai/developers/model-capabilities/text/streaming) · [Ollama 兼容接口](https://docs.ollama.com/api/openai-compatibility)

- `/provider` 列出配置。用 `/provider xai` 切换，确认后后续请求会发送当前会话。
- `/model 模型ID` 确认后覆盖当前模型。用 `/health xai` 检查配置模型是否出现在服务列表，此操作不生成内容。
- `/route edit 请润色这段英文……` 按 `routes` 的任务映射发出单次请求。
- `/compare xai,local 用这份设定写一段英文……` 把同一系统指令和这次输入分别交给两种模型。发送前需确认，不附会话正文，也不自动保存或采用结果。
- 服务回传用量时终端显示输入与输出 token。Chat 配置可选择 `"report_usage": true`；确认所用服务支持后开启。可填 `usd_input_per_million` 与 `usd_output_per_million` 得到估算，以实际账单为准。请求默认 90 秒，可按配置设 `timeout`，失败后手动重试或明确选用其他模型。

Grok Bot 的研究或评审请用[手动交接](../integrations/grokbot/README.md)。
