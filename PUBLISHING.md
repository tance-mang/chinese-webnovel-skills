# 上架与发布指南

把插件推到 GitHub，让全世界的中文网文作者一行命令就能装。

---

## 一、推到 GitHub

```bash
# 在仓库根目录
git init
git add .
git commit -m "feat: 网文工坊 v0.1 — 中文网文写作 Claude 插件"

# 在 GitHub 新建一个名为 chinese-webnovel-skills 的空仓库（不要勾选 README）
git branch -M main
git remote add origin https://github.com/tance-mang/chinese-webnovel-skills.git
git push -u origin main
```

> 注意：`config.json`、`/output/`、书稿目录已在 `.gitignore` 里排除，不会泄露你的密钥和稿子。

---

## 二、让别人安装

仓库 public 后，任何人在 Claude Code 里：

```text
/plugin marketplace add tance-mang/chinese-webnovel-skills
/plugin install webnovel@webnovel-studio
```

`marketplace add` 后面跟的是 `GitHub用户名/仓库名`，Claude Code 会自动找 `.claude-plugin/marketplace.json`。

---

## 三、上 Claude Plugin Hub（第三方发现站）

[claudepluginhub.com](https://www.claudepluginhub.com) 会自动收录公开的 Claude Code 插件仓库。提高被发现的概率：

1. **仓库 topics** 加上：`claude-code`、`claude-code-plugin`、`claude-code-skills`、`webnovel`、`chinese`、`fiction-writing`
2. **README 开头**讲清楚是什么、给谁用、怎么装（已写好）
3. **仓库描述**一句话写清楚关键词，例：`Chinese web-novel writing skills for Claude Code — outline, hooks, golden-finger, 爽点, 追读诊断`
4. 也可以去 [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) 提 PR 收录自己

---

## 四、版本管理

- 改了内容想让用户更新 → 编辑 `.claude-plugin/plugin.json` 的 `version`（如 `0.1.0` → `0.2.0`），再 push。
- 用户侧：`/plugin update webnovel`。
- 如果你想"每次 push 都让用户拿到最新"，可以把 `plugin.json` 和 marketplace 里的 `version` 都删掉，Claude Code 会用 git commit SHA 当版本（适合快速迭代期）。

---

## 五、发布前自检清单

- [ ] `claude plugin validate` 通过（manifest 和 frontmatter 无语法错）
- [ ] `/plugin marketplace add ./`（本地路径）能装上、技能能触发
- [ ] README 的安装命令里用户名/仓库名正确
- [ ] `.gitignore` 确认排除了 `config.json` 和书稿
- [ ] LICENSE 里的作者名是你
- [ ] plugin.json / marketplace.json 里的 `author` 和 `repository` 改成你的

---

## 六、推广建议（海外中文网文作者）

- **小红书 / 公众号**：发"用 Claude 写网文的插件"教程引流。
- **Discord / Reddit r/noveltranslations、r/ClaudeAI**：海外华人作者聚集地。
- **Webnovel 作者群 / 番茄作者圈**：直接给目标用户。
- **做一个 demo**：用插件写一段爽文开头录屏，比文字说明有说服力。

---

> 上架不是终点，根据真实作者反馈迭代 `references/` 知识库，才是护城河。
