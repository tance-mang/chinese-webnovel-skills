<div align="center">

# WebNovel Studio · 网文工坊

**A full-workflow toolkit for writing Chinese web fiction**
Claude Code plugin · also works with ChatGPT / DeepSeek / Gemini / Kimi and any LLM

Idea → Spark → Outline → Killer opening → Golden-finger → Characters → Prose → Face-slap beats → Rhythm annotation → Retention diagnosis → De-slop → Submission → Platform trends

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet)](https://code.claude.com)
[![Skills](https://img.shields.io/badge/skills-31-brightgreen)](#-31-skills)
[![Version](https://img.shields.io/badge/version-0.27.0-blue)](CHANGELOG.md)
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
- [24 Skills](#-24-skills)
- [Typical workflows](#-typical-workflows)
- [Knowledge base](#-knowledge-base)
- [Project structure](#-project-structure)
- [Credits](#-credits)
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
- **Not Claude-only**: export to ChatGPT (Custom GPT) and other LLMs (Gemini/DeepSeek/Kimi…) — see [exports/SETUP.md](exports/SETUP.md).

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

## 🌐 Supported AIs (not Claude-only)

The methodology is model-agnostic — any AI with a system prompt or custom-agent feature works. This repo ships exports (`exports/`):
- **Claude** (native): the Claude Code plugin, `/webnovel:xxx`
- **DeepSeek / Gemini / Kimi / ChatGPT / Doubao / Qwen / GLM / ERNIE**: paste `exports/instructions.md` as the system prompt or custom-agent instructions, and upload the two `knowledge-*.md` files as knowledge
- **Stay in sync**: after adding skills, run `python tools/build_exports.py` to regenerate

See **[exports/SETUP.md](exports/SETUP.md)**. One methodology, works across Claude / ChatGPT / Chinese models.

## 📖 31 Skills

> Most skills accept a "**platform + channel + genre**" argument, e.g. `/webnovel:outline 番茄 男频 都市战神`, auto-adapting pacing and tropes.

| Skill | Command | What it does |
|---|---|---|
| 💡 Spark → Draft | `/webnovel:spark` | Jot down inspirations; grow one spark into outline → draft with target word count & chapter split |
| 🎯 Premise | `/webnovel:idea` | Pick channel/genre, hit premises + one-line selling point + golden three chapters |
| 🏷️ Title | `/webnovel:title` | Book titles with keyword + payoff + hook; kills "too AI / too literary / generic" names |
| 🗺️ Outline | `/webnovel:outline` | Whole-book / volume / chapter outlines with a foreshadowing tracker |
| 🪝 Hooks | `/webnovel:hook` | Opening hooks, chapter-end cliffhangers, paywall hooks |
| ⚙️ Golden-finger | `/webnovel:goldfinger` | System/sign-in/space/simulator cheats with thresholds & costs |
| 🌍 Worldbuilding | `/webnovel:world` | World-first for strong-setting genres: power/factions/politics/economy/geography/history + world-state that changes by chapter, prevents setting drift |
| 👤 Characters | `/webnovel:character` | Protagonist/villain/CP sheets with growth arcs |
| 🪪 Char names | `/webnovel:name` | Name/rename characters: era-fit, memorable; kills generic AI names |
| ✍️ Prose | `/webnovel:expand` | Turn chapter outlines into publishable prose, controlled pace & length |
| 🔥 Payoff & face-slap | `/webnovel:shuangdian` | Three-stage payoff loop + four-beat face-slap + escalation |
| 💬 Dialogue | `/webnovel:dialogue` | Write/fix dialogue, punchlines, face-slap lines; de-AI dialogue; distinct character voices |
| 🌱 Warmth | `/webnovel:warmth` | Warm, realistic short fiction: no melodrama/preaching/clichés — small conflict + life detail + warm aftertaste |
| 🏷️ Annotate | `/webnovel:annotate` | Mark hooks/payoffs/climax/modifiers + a rhythm data table |
| 🩺 Diagnose | `/webnovel:review` | Six-axis checkup: hooks/payoffs/foreshadowing/characters/pacing/human-texture (reader-retention lens) |
| 🧭 Continuity | `/webnovel:continuity` | Long-form logic + timeline: behavior/causality/resources/identity/injury/power-level contradictions → caught & fixed (anti-amnesia) |
| 🧹 De-slop | `/webnovel:deslop` | Remove AI-ese, gratuitous rhetoric, incongruous allusions → real feel |
| 📊 AI-score | `/webnovel:aidetect` | Quantified AI-slop scan: metaphor density / repeated sentence patterns / length variance / paragraph spread / emotion-word repetition → index (0–10) + located deductions |
| 😢 Emotion | `/webnovel:emotion` | Show emotion via action/detail instead of "I'm so heartbroken" (show don't tell) |
| ✅ Proofread | `/webnovel:proofread` | Typo check (Chinese homophone/near-shape errors) + sensitive/banned-content scan → "original → suggested" one-click-style replacements (heuristic, not a platform's exact wordlist) |
| 📮 Submission | `/webnovel:submission` | Checks against platform signing standards + title/blurb/tags |
| 📈 Trends | `/webnovel:trends` | Live web research of trending genres/tags/rankings per platform |
| 🔥 Slang | `/webnovel:slang` | Live-search current Douyin/RedNote/Weibo memes + rules to use them without feeling forced/dated |
| 🫀 Human texture | `/webnovel:human` | Deep de-AI: add irrational acts / unfinished emotion / loose ends so it reads like an "emotion log", not a "manual" |
| 🌍 English | `/webnovel:english` | Write/adapt for English platforms (Wattpad/Royal Road/Webnovel) — reads like a local author, not translationese |
| 🎬 Script | `/webnovel:script` | Vertical short-drama / film scripts & novel-to-script, proper screenplay format, only what the camera can capture, hard cliffhanger per episode |
| 🎓 Coach | `/webnovel:coach` | Learn to write (opt-in, beginner-friendly, explains the "why") |
| 🎭 Fan-fiction | `/webnovel:fanfic` | Fanfic writing + copyright compliance check (character count / quote ratio / platform policy) |
| 🔬 Deconstruct | `/webnovel:deconstruct` | Reverse-engineer hit novels' structure into reusable templates (learn structure, don't copy text) |
| 🗄️ Memory | `/webnovel:memory` | Persistent project memory: outline/characters/foreshadowing/progress/submission log, resume across sessions, git-like snapshots |
| 📄 Draft | `/webnovel:draft` | Export a "draft for revision" .docx: TOC + left-aligned chapter titles + 【修改】 red edit notes; names 《book》修改N, never overwrites original |

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

31 shared reference libraries (`references/`) — the web-novel know-how:

| File | Content |
|---|---|
| `hook-library.md` | Hooks: opening/chapter-end/paywall, 6 real examples each for 男频/女频 |
| `trope-library.md` | 23 payoff tropes + trigger mechanics + deployment |
| `goldfinger-types.md` | 10 golden-finger schools + four elements + anti-flop |
| `title-library.md` | Title craft: male/female naming formulas + keyword pools + anti-AI checklist |
| `name-library.md` | Character naming: surname pools + naming by genre/role + villain/sect names + pitfalls |
| `genre-library.md` | Full genre taxonomy: 9 blocks (mystery/psych/urban/system/xianxia/female/history-ancient-althist/horror/niche) |
| `fanfic-guide.md` | Fan-fiction compliance: per-platform policy + copyright lines + public-domain IP |
| `xiushi-ci.md` | Modifier-word library for punchy fast-paced prose |
| `dialogue-library.md` | Dialogue: de-AI speech + face-slap/flex/villain/angst-sweet lines + punchlines + character voices |
| `anti-ai-checklist.md` | Deep de-AI checklist: gratuitous rhetoric + incongruous allusions + register consistency + show-don't-tell |
| `human-texture.md` | Human texture (deep): 5 "feels like AI" symptoms + irrational acts / unfinished emotion / loose ends + manual vs emotion-log |
| `ai-detector.md` | Quantified AI-slop: 12 metrics (metaphor density / repeated sentence patterns / length variance / paragraph spread / emotion-word repetition / summary-sentence (show-tell) / action-dialogue-thought ratio / scenery audit / reading friction …) + thresholds + scoring + located output |
| `sentence-rhythm.md` | Sentence rhythm: mix short/long, occasional long sentence, ellipsis/dash/line-breaks for breathing, unfinished emotion (cures "too smooth") |
| `dark-style.md` | Dark/grayscale style + dual output (crowd-pleaser vs elevated-dark) |
| `english-webfic.md` | English web-fic: Wattpad/RoyalRoad/Webnovel + EN-vs-CN logic + English hooks/formatting/emotion/AI tells |
| `script-format.md` | Screenplay format: vertical short-drama/film, only what's filmable, scene headings/lines/cliffhangers + novel-to-script |
| `show-emotion.md` | Show-emotion library: 11 emotions → expression/action/physiology/subtext, show don't tell |
| `pov-guide.md` | POV: defaults to first person (immersive, like a personal account); switchable to third person |
| `manuscript-format.md` | Manuscript/revision format: Word output / non-overwriting naming / TOC / left-aligned chapters / 【修改】 marks / word counts |
| `warm-realism.md` | Warm realism: warmth in restraint / cold-then-warm / aftertaste / anti-cliché + character/plot/ending templates |
| `slang-guide.md` | Internet slang usage: 6 rules to avoid feeling forced + evergreen vs short-lived + by platform/genre (memes fetched live) |
| `case-studies.md` | Hit-novel breakdowns: structure/hooks/angst/payoff/technique (learn structure, don't copy) |
| `submission-guide.md` | Submission/signing standards per platform |
| `sensitive-words.md` | Proofread/censor: common Chinese typo pairs + 9 sensitive/banned categories + replacement strategy (heuristic, not a platform wordlist) |
| `platform-profiles.md` | Fanqie/Jinjiang/Qidian/UC/Zhihu/Webnovel profiles + channel prefs + fanfic policy |
| `length-standards.md` | Length standards: Fanqie-official / industry-wide / literary, signing & distribution thresholds + how to pick a length |
| `channel-guide.md` | Male- vs female-channel split |
| `writing-craft.md` | Web-novel fundamentals (for teaching) |
| `project-memory.md` | Project memory spec: file layout + foreshadowing/progress/timeline/power-level/speech-fingerprint formats + git snapshots |
| `continuity-check.md` | Continuity/logic: 7 logic chains (behavior/causality/resources/identity/injury/power/emotion) + timeline & world-state check + 3 long-form amnesia thresholds |
| `worldbuilding.md` | World-first (World Engine): world modules (power/factions/politics/economy/geography/history) + per-chapter world-state + character-world coupling + pre-chapter "four world questions" |

## 📂 Project structure

```
chinese-webnovel-skills/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # marketplace manifest
├── skills/                  # 31 skills (draft bundles build_docx.py for Word)
├── references/              # 31 knowledge libraries
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

## 🙏 Credits

- **Methodology seed**: the core hook examples and payoff tropes come from the author's own writing notes, *Novel Writing Logic*.
- Built on [Claude Code](https://code.claude.com)'s public plugin mechanism.
- Thanks to the open-source community and web-fiction authors everywhere.

> All skills and knowledge bases are **original work**. No third-party code or copyrighted content is included or copied. Open-sourced under the MIT License.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md).

- **v0.27.0** — novel QA-system upgrade: new **worldbuilding** (world: power/factions/politics/economy/geography/history + per-chapter world-state, prevents setting drift) + AI-slop detector expanded to **12 metrics** (added summary-sentence/show-tell, action-dialogue-thought ratio, scenery audit, reading friction) + **emotion continuity** tracking (no "just broke up, laughing next chapter"; stored in memory, checked by continuity) + chapter-outline "goal/obstacle/result/cost" (anti-treading-water) + review "continue-rate" prediction
- **v0.26.1** — zero-setup terminal deploy: one-click launchers (Windows: double-click `cli/启动.bat`; Mac: `cli/start.sh`, auto-installs deps) + a 4-step deploy guide in `cli/README.md` (install Python → download → launch → connect your AI) + friendly first-run when no key is set
- **v0.26.0** — proofread: Chinese typo check + sensitive/banned-content scan with "original → suggested" one-click-style replacements (like Fanqie's editor); wired into submission (sensitive scan is a heuristic safety net, not a platform's exact wordlist). **CLI upgrades**: auto-save so nothing is lost (default .txt, optional .md/.docx, no-overwrite naming, shows path), git-like creation log (/history), learning-mode toggle (/coach), proofread in CLI (/proofread); save prefs are configurable via /set, not hardcoded
- **v0.25.0** — long-form four-engine boost: continuity (logic + timeline: behavior/causality/resources/identity/injury/power) + aidetect (quantified AI-slop score 0–10 with located deductions) + length-standards library + memory upgrade (factions/power-levels/timeline/speech-fingerprint)
- **v0.24.0** — script (script): vertical short-drama / film scripts & novel-to-script, proper screenplay format, only what the camera can capture, hard cliffhanger per episode
- **v0.23.0** — standalone terminal CLI (any OpenAI-compatible API: DeepSeek/Kimi/Ollama…) + Chinese punctuation rules (…… ellipsis, fewer em-dashes, no 【】 in prose)
- **v0.22.0** — English export (english): write/adapt for Wattpad/Royal Road/Webnovel like a local author, not translationese
- **v0.21.0** — Word body paragraphs: 2-character first-line indent (firstLineChars=200)
- **v0.20.0** — sentence rhythm (uneven length / pause punctuation / unfinished lines, fixes "too smooth") + dark style & dual "shuangwen / dark" version output
- **v0.19.0** — human texture (deep de-AI): irrational acts / unfinished emotion / loose ends / bias — reads like an "emotion log" not a "manual"; review now 6-axis
- **v0.18.0** — slang: live-search current Douyin/RedNote/Weibo memes + 6 rules to use them without feeling forced or dated
- **v0.17.0** — no decorative symbols (✦✨◆★); draft's Word chapter titles set to plain black (no default blue)
- **v0.16.0** — deeper de-AI: repeated rhetoric/sentence patterns, redundant synonyms, intensifier overuse, random declarative filler, period-as-comma, over-parallel paragraphs
- **v0.15.0** — warmth: warm realistic short fiction (no melodrama/preaching/clichés; warmth in restraint, cold-then-warm, aftertaste)
- **v0.14.0** — draft: export a "draft-for-revision" .docx (TOC + left-aligned chapters + 【修改】 red notes + 《book》修改N non-overwriting naming + short-piece word ranges)
- **v0.13.0** — multi-model positioning: universal exports (`exports/`) + step-by-step setup for DeepSeek/Gemini/Kimi/Doubao/Qwen/GLM/ERNIE, not Claude-only
- **v0.12.0** — POV: defaults to first person (immersive, reads like a personal account), switchable to third, stated upfront; Zhihu immersion strengthened
- **v0.11.0** — emotion (show, don't tell): turn "I'm so heartbroken" into felt description + show-emotion library
- **v0.10.0** — deeper de-AI (gratuitous rhetoric / incongruous allusions / register consistency) + Fanqie golden-300-words & 5 hook types + angst design + hit-novel case studies
- **v0.9.0** — cross-model export: ChatGPT Custom GPT (instructions + knowledge files) + universal system prompt, via `tools/build_exports.py`
- **v0.8.0** — dialogue (dialogue): de-AI speech, punchlines, face-slap/flex lines, distinct character voices
- **v0.7.0** — character naming (name): era-fit & memorable, fixes generic AI character names
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
