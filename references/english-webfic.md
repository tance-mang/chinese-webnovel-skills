# 英文网文出海库（English Web Fiction）

> 出海写英文不是把中文翻译过去——**中文网文卖"剧情爽点"，英文网文卖"情绪钩子"**。
> 中文读者愿意看你解释为什么爽；英文读者要被**直接扔进故事**，自己感受。
> 目标：让 AI 写的英文读起来像当地作者，而不是"中国网文翻译腔"。供 `english` 调用。

---

## 〇、总开关：Native English Webnovel Mode（默认）

> 写英文时**默认开启**这一条——它改的是**叙事思维**，比几十条零散规则都重要：
>
> - **默认按欧美母语网文风格输出，不是中文翻译过去。**
> - **优先动作、对话、冲突、悬念；降低解释、降低抒情、降低文学化描写。**
> - **提高人物真实感和口语化表达。**
> - **让读者沉浸在事件中，而不是旁观作者讲故事。**
>
> 区别：不是"中文思维→翻译成英文"，而是"英文读者本来就会这样表达"。

### 十条核心规则（Native English）
1. **禁止翻译腔**：情绪用动作/身体反应，不直译中式比喻。
   ❌ `Her heart felt like it was cut by knives.` / `Flames of anger burned in his chest.`
   ✅ `My chest tightened.` / `He clenched his jaw.` / `She looked away.`
2. **Show > Tell**：不解释情绪。❌ `She was sad/nervous/angry.` ✅ `Her hands shook.` `She stared at the floor.` `He slammed the door.`
3. **句长 70/20/10**：70% 短句、20% 中句、10% 长句，避免连续长句。
   > `I stopped. / The room was empty. / Too empty. / Then I heard breathing behind me.`
4. **禁止文学堆砌**：避免 `moonlight danced`、`crystal tears`、`breathtaking beauty`、`cold smile` —— 直接写动作。
5. **每 200 字必须推进**：新信息/新冲突/新秘密/新反转/新危险，禁止无意义描写。
6. **钩子优先**：章节开头不要环境描写，开头给 危险/秘密/死亡/身份反转/禁忌关系/倒计时/悬念。
7. **对话像真人**：❌ `I am extremely disappointed in your behavior.` ✅ `What the hell was that?` —— 口语 > 书面。
8. **母语短句节奏**：多用 `Maybe.` `Fine.` `Seriously?` `No way.` `Wait.` `Damn.` 增加真实感。
9. **减少副词**：避免 `slowly / carefully / suddenly / angrily`，用动作表达。
10. **每章结尾留钩**：读完让读者想"再看一章"。
    > `The message appeared. / WELCOME BACK, PLAYER. / Level 1 begins.`

---

## ⓪+ 中国爽文 vs 英文爽文（结构差异，最易忽略）

| | 中文爽文 | 英文爽文 |
|---|---|---|
| 结构 | **情绪 → 爽点**（直接给爽） | **谜团 → 情绪 → 爽点**（先制造疑问再给爽） |
| 例 | "前男友后悔了" → 直接爽 | 前男友**为什么**后悔？他隐瞒了什么？那晚发生了什么？→ 先疑问，再爽 |

> 英文读者要先被"为什么"勾住，再给情绪和爽点。**先埋谜，后给糖。**

### 爽感包装：身份碾压 vs 个人成长
- **中文爱"身份碾压"**：首富、战神、龙王、神医（一出场就高位）。
- **英文爱"个人成长"**：**Survivor（幸存者）/ Underdog（弱者逆袭）/ Outcast（被排挤者）/ Chosen One（被选中者）**（从低到高、自己挣来）。
- 同样是爽，**包装方式不同**：英文要让读者陪主角"挣"，而不是开局就赢。

---

## 一、英文平台速览

| 平台 | 受众/频道 | 爆款题材 | 变现 | 上手 |
|---|---|---|---|---|
| **Wattpad** | 女性为主，13–30，情绪阅读 | Romance、Bad Boy、Billionaire、Mafia、Werewolf、Fake Dating | 签约/付费(门槛不低) | ⭐最易上手：免费注册、不要银行卡、直接发 |
| **Royal Road** | 男性为主 | LitRPG、系统、升级、Progression、无限流、奇幻、穿越、DnD/RPG | 引流 Patreon 赚钱 | 男频强，英文网文圈很有名 |
| **Webnovel** | 阅文国际版，中国作者多 | 系统、神豪、重生、签到、校园、都市（=英文版番茄）| 签约体系成熟 | 爽文/升级流/系统流接受度高 |
| **Radish** | 偏女性付费 | 言情、总裁、狼人；短篇/连载 | 付费阅读 | 短平快 |
| **Amazon KDP** | 电子书读者 | 完结作品 | 版税最高 70% | 适合完结、**不适合日更模式** |

> 新人最快上手：**Wattpad**（女性向言情/Romance）和 **Webnovel**（系统/升级，最像番茄）。

---

## 二、英文 vs 中文 底层逻辑（最重要）

| | 中文网文 | 英文网文 |
|---|---|---|
| 卖点 | 剧情**爽点** | 情绪**钩子** |
| 读者关注 | 世界观、爽感、文学性 | 人物、感情、情绪 |
| 节奏 | 可铺垫 | 前 100 词必须有事发生 |
| 解释 | 愿意看"为什么爽" | 讨厌解释，直接动作，自己理解 |
| 开头 | “血色残阳下，少女眸光冷冽。” | `I never expected my life to change that night.` / `The dead man opened his eyes.` |

> 一句话：**英文读者更喜欢被直接扔进故事里，让他自己感受**，而不是你告诉他该感受什么。

---

## 三、英文读者讨厌的 3 件事（AI 最容易翻车）

### 1. 长段落
英文一大段就弃书。要**短，非常短**。
- ❌ 一大段叙述 + 回忆 + 心理。
- ✅ `I looked outside. / Rain hit the window. / The memory came back.`

### 2. 解释
不要写"她之所以这么做是因为……"，直接动作。
- ❌ `She was angry because...`
- ✅ `She slammed the door.` （让读者自己理解）

### 3. 堆形容词
- ❌ `Her beautiful, gorgeous, stunning eyes...`
- ✅ `Her eyes stayed on me.` （简单）

---

## 四、英文排版（必须遵守）

- 章标题：`Chapter 1`（不是"第一章"）。
- 段落短、段间空行。
- **对话必须换行，一句一行**：
```
"Who are you?"

I froze.

"Answer me."
```
- ❌ 绝不把对话和动作挤在一行：`"Who are you?" I froze. "Answer me."`（阅读体验差）。

---

## 五、英文节奏：前 100 词有事发生
- ❌（中文式铺垫）女主起床→洗脸→吃饭→出门→撞见男主。
- ✅ 第一句直接开始：`The dead man opened his eyes.`

---

## 六、英文最爱的钩子（开篇第一句）

- **身份反转**：`My husband murdered me. Then I woke up three years earlier.`
- **危机/倒计时**：`The timer on my arm showed 00:59.`
- **秘密**：`Everyone in town knew the truth except me.`
- **禁忌关系**：`I accidentally married my enemy.`

---

## 七、英文情绪表达：用身体反应，不喊抽象
- ❌ `Her heart was breaking.`（≈ 心如刀割，英文很少这样写）
- ✅ `I couldn't breathe.` / `My hands shook.` / `My throat went tight.`
> 和中文的 show-don't-tell 一脉（见 `show-emotion.md`），但英文更偏**生理反应**、更克制。

---

## 八、AI 写英文最容易暴露的 3 个破绽

1. **太正式**：`Therefore... / However... / Furthermore...` → 像论文/学术。改口语连接或删。
2. **太工整/机械**：`He smiled. She smiled. He walked. She walked.` → 句式镜像、节奏机械。打破对称（见 `sentence-rhythm.md`）。
3. **过度文学**：`Moonlight danced gracefully upon the crystal lake...` → 网文读者直接跳。要直白、要快。

---

## 九、平台 × 题材速配
- **Wattpad**：Romance / Billionaire / Mafia / Werewolf / Enemies-to-Lovers / Fake Dating（女性向情绪流）。
- **Royal Road**：LitRPG / Progression / System / Dungeon / Cultivation（男频升级，可借中文套路）。
- **Webnovel**：System / Reborn / Urban / Sign-in / Campus（英文版番茄，中文套路直接迁）。
- **短篇/广告流（TikTok/Reels）**：强钩子、强反转、超短段落。

---

## 十、给中国作者的一句话
你的**反转意识、钩子意识、快节奏**很适合 Wattpad 短篇 / Webnovel / 短视频小说流。把"解释爽点"改成"直接扔进情绪"，就立刻接近当地作者，而不是翻译腔。

## 相关
- 英文写作/改写技能 → `skills/english`
- 去 AI 味（中英通用思路）→ `deslop`、`human`、`sentence-rhythm.md`、`show-emotion.md`
- 钩子结构（中英通用）→ `hook-library.md`
