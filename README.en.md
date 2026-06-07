<div align="center">

# WebNovel Studio · 网文工坊

**A Claude Code plugin for the full Chinese web-novel writing workflow**

Idea → Spark → Outline → Killer opening → Golden-finger → Characters → Prose → Face-slap beats → Rhythm annotation → Retention diagnosis → De-slop → Submission → Platform trends

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet)](https://code.claude.com)
[![Skills](https://img.shields.io/badge/skills-18-brightgreen)](#-18-skills)
[![Version](https://img.shields.io/badge/version-0.6.0-blue)](CHANGELOG.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-success)](#-contributing)

[简体中文](README.md) | **English**

</div>

---

> In one line: upgrade authors who write Chinese web novels with Claude from "copy-pasting scattered prompts" to "a professional toolkit that understands the commercial logic of web fiction."
> Covers both male-channel (男频) and female-channel (女频), tuned for Qidian / Fanqie / Jinjiang / UC / Zhihu / Webnovel (Qidian International), with fan-fiction compliance and a full genre library.

> **Note:** This plugin helps you write **in Chinese**. The novels it produces are Chinese web fiction. These docs are bilingual so non-Chinese and non-English speakers can both navigate the project.

## 📑 Table of Contents

- [Why use it](#-why-use-it)
- [Install](#-install)
- [18 Skills](#-18-skills)
- [Typical workflows](#-typical-workflows)
- [Knowledge base](#-knowledge-base)
- [Project structure](#-project-structure)
- [Comparison with similar projects](#-comparison-with-similar-projects)
- [Credits & references](#-credits--references)
- [Changelog](#-changelog)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Why use it

- **Built for Chinese web fiction**: not a generic writing wrapper — it follows the "爽点" (payoff) logic, the four-beat face-slap, and the retention pacing of Qidian/Fanqie.
- **Leverages Claude's long context**: 200K tokens hold a whole-book outline plus all character sheets, so settings and foreshadowing stay consistent across hundreds of thousands of words.
- **End-to-end**: 14 skills from "a single spark" to "passing editorial review."
- **Data-minded**: visual annotation of hooks/payoffs/modifiers, retention diagnosis, live platform trends — see the data, not just type.
- **Beginner-friendly**: an optional writing coach you can switch on to learn, off to just write.
- **Bilingual docs**: Chinese for non-English speakers, English for international users.

> For: overseas Chinese web-novel authors, mainland authors publishing abroad, anyone writing in Claude Code / VSCode, and newcomers learning the craft.

## 🚀 Install

> Prerequisite: [Claude Code](https://code.claude.com) installed (CLI or the VSCode / JetBrains extension).

In Claude Code, run:

```text
/plugin marketplace add tance-mang/chinese-webnovel-skills
/plugin install webnovel@webnovel-studio
```

Restart the session. Verify by typing `/webnovel:idea`.

**Local try-out** (before pushing to GitHub):
```text
/plugin marketplace add ./chinese-webnovel-skills
/plugin install webnovel@webnovel-studio
```

## 📖 18 Skills

> Most skills accept a "**platform + channel + genre**" argument, e.g. `/webnovel:outline 番茄 男频 都市战神`, auto-adapting pacing and tropes.

| Skill | Command | What it does |
|---|---|---|
| 💡 Spark → Draft | `/webnovel:spark` | Jot down inspirations; grow one spark into outline → draft with target word count & chapter split |
| 🎯 Premise | `/webnovel:idea` | Pick channel/genre, hit premises + one-line selling point + golden three chapters |
| 🏷️ Title | `/webnovel:title` | Book titles with keyword + payoff + hook; kills "too AI / too literary / generic" names |
| 🗺️ Outline | `/webnovel:outline` | Whole-book / volume / chapter outlines with a foreshadowing tracker |
| 🪝 Hooks | `/webnovel:hook` | Opening hooks, chapter-end cliffhangers, paywall hooks |
| ⚙️ Golden-finger | `/webnovel:goldfinger` | System/sign-in/space/simulator cheats with thresholds & costs |
| 👤 Characters | `/webnovel:character` | Protagonist/villain/CP sheets with growth arcs |
| ✍️ Prose | `/webnovel:expand` | Turn chapter outlines into publishable prose, controlled pace & length |
| 🔥 Payoff & face-slap | `/webnovel:shuangdian` | Three-stage payoff loop + four-beat face-slap + escalation |
| 🏷️ Annotate | `/webnovel:annotate` | Mark hooks/payoffs/climax/modifiers + a rhythm data table |
| 🩺 Diagnose | `/webnovel:review` | Five-axis checkup: hooks/payoffs/foreshadowing/characters/pacing |
| 🧹 De-slop | `/webnovel:deslop` | Turn "AI/translation-ese" into real web-novel feel |
| 📮 Submission | `/webnovel:submission` | Checks against platform signing standards + title/blurb/tags |
| 📈 Trends | `/webnovel:trends` | Live web research of trending genres/tags/rankings per platform |
| 🎓 Coach | `/webnovel:coach` | Learn to write (opt-in, beginner-friendly, explains the "why") |
| 🎭 Fan-fiction | `/webnovel:fanfic` | Fanfic writing + copyright compliance check (character count / quote ratio / platform policy) |
| 🔬 Deconstruct | `/webnovel:deconstruct` | Reverse-engineer hit novels' structure into reusable templates (learn structure, don't copy text) |
| 🗄️ Memory | `/webnovel:memory` | Persistent project memory: outline/characters/foreshadowing/progress/submission log, resume across sessions, git-like snapshots |

> Claude can also trigger skills by context — just say "write me a cultivation-novel opening" and it calls `hook`.
> The coach only appears when you invoke it; it won't interrupt normal writing.

## 🧭 Typical workflows

<details>
<summary><b>From one spark to a draft</b></summary>

```text
/webnovel:spark      → log a spark, or incubate it into outline + draft (set words/chapters)
/webnovel:annotate   → inspect the draft's rhythm data
/webnovel:review     → checkup, revise per report
```
</details>

<details>
<summary><b>Start a new book (crafted)</b></summary>

```text
/webnovel:idea       → lock a premise (channel + golden-finger + selling point)
/webnovel:goldfinger → refine the cheat
/webnovel:character  → build protagonist and villain
/webnovel:outline    → main line + volume 1 + golden-three-chapter outline
/webnovel:hook       → polish the opening hook
/webnovel:expand     → write chapter 1
/webnovel:review     → check the first three chapters
```
</details>

<details>
<summary><b>Before submission / rescue a book</b></summary>

```text
/webnovel:trends     → what's hot on the target platform now
/webnovel:submission → checkup vs signing standards + blurb & tags
/webnovel:review     → retention dropping? diagnose why
```
</details>

## 📚 Knowledge base

8 shared reference libraries (`references/`) — the web-novel know-how:

| File | Content |
|---|---|
| `hook-library.md` | Hooks: opening/chapter-end/paywall, 6 real examples each for 男频/女频 |
| `trope-library.md` | 23 payoff tropes + trigger mechanics + deployment |
| `goldfinger-types.md` | 10 golden-finger schools + four elements + anti-flop |
| `title-library.md` | Title craft: male/female naming formulas + keyword pools + anti-AI checklist |
| `genre-library.md` | Full genre taxonomy: 9 blocks (mystery/psych/urban/system/xianxia/female/history-ancient-althist/horror/niche) |
| `fanfic-guide.md` | Fan-fiction compliance: per-platform policy + copyright lines + public-domain IP |
| `xiushi-ci.md` | Modifier-word library for punchy fast-paced prose |
| `submission-guide.md` | Submission/signing standards per platform |
| `platform-profiles.md` | Fanqie/Jinjiang/Qidian/UC/Zhihu/Webnovel profiles + channel prefs + fanfic policy |
| `channel-guide.md` | Male- vs female-channel split |
| `writing-craft.md` | Web-novel fundamentals (for teaching) |
| `project-memory.md` | Project memory spec: file layout + foreshadowing/progress/submission-log formats + git snapshots |

## 📂 Project structure

```
chinese-webnovel-skills/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # marketplace manifest
├── skills/                  # 18 skills (one SKILL.md each)
├── references/              # 12 knowledge libraries
├── templates/               # book bible / submission log / progress
│   ├── book-bible-template.md
│   ├── submission-log-template.md
│   └── progress-template.md
├── README.md                # Chinese (primary)
├── README.en.md             # English (this file)
├── CHANGELOG.md
├── PUBLISHING.md
├── LICENSE                  # MIT
└── .gitignore
```

## 🆚 Comparison with similar projects

Chinese-novel Claude plugins already exist. This plugin is **the only one focused on commercial web-fiction sub-modules + data diagnosis**:

| Project | Size | Focus | What it lacks (we add) |
|---|---|---|---|
| [PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) | 1.9k★ | One big conversational skill | No sub-modules, no payoff/hook/golden-finger/submission/data diagnosis |
| [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1.1k★ | General full pipeline | No golden-finger module, no retention diagnosis, female-channel leaning |
| [yuzhoujishu/novel-writing](https://github.com/yuzhoujishu/novel-writing) | hundreds★ | Generic 7-command novel tool | Generic literature, no commercial web-fiction logic |

**Exclusive here**: golden-finger module · per-chapter rhythm annotation · retention diagnosis · submission review · live platform trends · spark-to-draft · full male/female coverage · writing coach.

> Not "the first" — "the one that best understands commercial web fiction." All plugins can coexist.

## 🙏 Credits & references

This is **original prompt engineering**; no code was copied from the projects below. Listed for transparency and thanks:

- **Methodology seed**: the core hook examples (6) and payoff tropes (23) come from the author's own writing notes, *Novel Writing Logic*.
- **Plugin spec**: [Claude Code official plugin docs](https://code.claude.com/docs/en/plugins-reference).
- **Peer projects studied (for differentiation, not copied)**: [oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode), [chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill), [novel-writing](https://github.com/yuzhoujishu/novel-writing), [AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator) (the "setting→TOC→chapter→finalize" stage model).

Thanks to these open-source projects for advancing the AI web-fiction ecosystem.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md).

- **v0.6.0** — title naming (title): keyword + payoff + hook, fixes "too AI / too literary / generic" book titles
- **v0.5.0** — project memory system (memory): store outline/characters/foreshadowing/progress, resume across sessions, git snapshots, submission-rejection log
- **v0.4.0** — fan-fiction compliance (fanfic), deconstruct, full genre library, 5-platform detailed profiles (fixed Mango → UC/Zhihu), platform/genre parameters
- **v0.3.0** — spark-to-draft, writing coach, bilingual docs, credits
- **v0.2.0** — annotate, submission, trends, modifier library, full male-channel coverage
- **v0.1.0** — initial release, 9 skills + 5 libraries

## 🤝 Contributing

PRs and issues welcome:

- Expand `references/` (more tropes, platform data, examples)
- Add/improve skills
- Improve bilingual docs and translations

To edit a skill, change `skills/<name>/SKILL.md`; the frontmatter `description` controls when Claude auto-triggers it.
Validate locally with `claude plugin validate .`. See [PUBLISHING.md](PUBLISHING.md).

## 📜 License

[MIT](LICENSE) © 2026 tance-mang. The writing methodology inside the skills is free to use, modify, and redistribute.

<div align="center">

**Happy writing, may your subscriptions soar** 🎉

[⬆ Back to top](#webnovel-studio--网文工坊)

</div>
