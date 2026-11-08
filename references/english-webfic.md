# 英文网文出海库（English Web Fiction）

> 出海写英文不是把中文翻译过去。常见读法仍是：**中文网文卖「剧情爽点」，英文连载常卖「情绪钩子」**。
> 这是类型偏好，不是「所有英文都必须短句 + 强钩」的硬规则。完本言情、慢热、LitRPG 结算段可以更长。
> 目标：让英文读起来像目标平台上的作品，而不是「中国网文翻译腔」。供 `english` 调用。
> 已核验的平台政策与类型差异，细节见 `integrations/grokbot/overseas-research.md`（查阅日 2026-11-08）。投稿前再打开官方页。

---

## 〇−、三条路径（先选路径，再套偏好）

| 路径 | 做什么 | 不做什么 |
|---|---|---|
| **original** | 按目标类型直接写英文 | 不要先用中文思维写完再逐句对译 |
| **adapt** | 保住核心因果和人物动机，用英文重讲。文化层可选：保留中国 / 混合 / 转目标文化 | 不要擅自改核心动机 |
| **translate** | 保住事实与叙述声音，优先自然英语 | 不要借「翻译」改情节 |

入口说明在 `skills/english`。`globalize` / `intimacy` 本轮没有独立技能，草案只在研究报告里。

---

## 〇、默认偏好：Native English Webnovel Mode

> 写英文连载时**默认**用这一套叙事习惯。它改的是叙事思维，作者可以按类型关掉其中几条：
>
> - **默认按目标类型的英文习惯输出，不是中文逐句翻译。**
> - **连载优先动作、对话、冲突、悬念；少空解释、少空抒情、少文学化堆砌。**
> - **提高人物真实感和口语化表达。**
> - **让读者待在事件里，而不是旁听作者讲故事。**

### 十条偏好（可配置，不是全英文硬规则）

1. **避免翻译腔**：情绪用动作或身体反应，不直译中式比喻。
   ❌ `Her heart felt like it was cut by knives.` / `Flames of anger burned in his chest.`
   ✅ `My chest tightened.` / `He clenched his jaw.` / `She looked away.`
2. **Show > Tell（偏好）**：少解释情绪。❌ `She was sad/nervous/angry.` ✅ `Her hands shook.` `She stared at the floor.` `He slammed the door.`
3. **句长按类型，不再锁 70/20/10**。连载爽文可以多短句；Contemporary / KDP Romance 允许中长句。避免的是连续同构长句，不是「长句」本身。
   > 短句示例（连载紧张段）：`I stopped. / The room was empty. / Too empty. / Then I heard breathing behind me.`
4. **少文学堆砌**：`moonlight danced`、`crystal tears`、`breathtaking beauty` 这类空词少用，改成跟场面有关的动作或一个感官。
5. **推进是偏好区间，不是每 200 字配额**。连载忌讳无信息的风景清单；慢热和完本允许生活场景，只要关系或信息有增量。
6. **钩子强度按平台和类型调**。章节开头不必永远禁止环境；Wattpad / Royal Road 连载通常希望早点出事，KDP 完本看整本弧线。
7. **对话像在场的人**：❌ `I am extremely disappointed in your behavior.` ✅ `What the hell was that?` 口语强于书面，仍要符合人物身份。
8. **需要口语节奏时**可以用 `Maybe.` `Fine.` `Seriously?` `No way.` `Wait.` `Damn.` 不要每段都甩。
9. **少用空副词**：`slowly / carefully / suddenly / angrily` 能改成动作就改。偶尔保留没有问题。
10. **连载章尾可以留拉力**。不要把「每章必须悬崖」写成唯一收束。心理惊悚和慢热用具体未解问题，不用 `Little did she know`。

### 句长与钩子：按类型配置

第 3、5、6、10 条是连载网文的**默认偏好**。禁止把「70% 短句 / 每 200 词一个转折 / 每段一个钩子」写成唯一正确答案。作者可以覆盖。

| 场景 | 句长与段落 | 钩子 | 平台注意 |
|---|---|---|---|
| **Wattpad Romance** | 短段和对话换行常见。Contemporary 允许生活场景和中长句；慢热不要用假钩子充节奏 | 章末可以有拉力。钩子过密会显假 | Mature 下可以写服务故事的成人亲密；禁止把色情本身当故事目的 |
| **Royal Road LitRPG** | 战斗用短句。规则、升级和结算可以写完整。状态栏只贴跟当前场面有关的信息 | 连载章末拉力通常更强，仍不要机械地每段一个钩 | **性内容不得作为核心或卖点；erotica 禁止**；AI 须按平台规则标注 |
| **KDP Romance** | 完本电子书，场景可以写全，中长句正常。不要为了「短」砍掉关系推进 | 服务整本情绪弧。章末钩子弱于日更连载 | **AI-generated 文本、图像、翻译必须披露**；大幅编辑后仍要披露。AI-assisted 不必 |

类型惯例（Dark / Contemporary / Slow Burn / Thriller / LitRPG / Progression）和中英改编原则的展开，见研究报告「类型风格档案」「中英叙事差异」。那是编辑归纳，标成经验，不是平台法律。

---

## ⓪+ 中国爽文 vs 英文爽文（结构差异，最易忽略）

| | 中文爽文 | 英文爽文连载（常见读法） |
|---|---|---|
| 结构 | **情绪 → 爽点**（直接给爽） | **谜团 → 情绪 → 爽点**（先制造疑问再给爽） |
| 例 | "前男友后悔了" → 直接爽 | 前男友**为什么**后悔？他隐瞒了什么？那晚发生了什么？→ 先疑问，再爽 |

> 这条主要服务于英文爽文连载。Slow Burn、心理惊悚、KDP 完本不要机械套用。

### 爽感包装：身份碾压 vs 个人成长

- **中文爽文常见「身份碾压」**：首富、战神、龙王、神医（一出场就高位）。
- **不少英文爽文读者更认「个人成长」**：**Survivor（幸存者）/ Underdog（弱者逆袭）/ Outcast（被排挤者）/ Chosen One（被选中者）**（从低到高、自己挣来）。
- 同样是爽，包装可以不同。LitRPG / Progression 仍可以有明确的等级提升，只是升级要有代价和场面，不要开局说明书。

---

## 一、英文平台速览（现行）

| 平台 | 受众/频道 | 常见题材 | 变现 | 上手与政策提示 |
|---|---|---|---|---|
| **Wattpad** | 女性为主，13–30，情绪阅读 | Romance、Bad Boy、Billionaire、Mafia、Werewolf、Fake Dating | 签约/付费（门槛不低） | 免费注册即可发。成人内容须故事驱动，禁止无剧情色情。竞赛对生成式 AI 更严，不等于全站总禁 |
| **Royal Road** | 男性向连载社区为主 | LitRPG、系统、升级、Progression、无限流、奇幻 | 常引流 Patreon | **性内容不得当卖点，erotica 禁止**；AI 须标注。见下文 |
| **Webnovel** | 阅文国际版，中英作者都有 | 系统、神豪、重生、签到、校园、都市 | 签约体系成熟 | 公开 AI 披露条款**待核实**，不要假设可以不披露。独家合同以作者文本为准 |
| **Amazon KDP** | 电子书读者，类目决定类型 | 完结作品（Romance / Thriller / Fantasy 等） | 版税依定价与渠道，最高可见 70% | 适合完结，不是日更社区。**AI-generated 必须披露** |

> 新人连载通常先看 **Wattpad**（女性向言情）和 **Webnovel**（系统/升级，最接近番茄的连载感）。男频 LitRPG 看 **Royal Road**。完本卖书看 **KDP**。
> Inkitt、Tapas 的成人内容与 AI 规则和上表不同（Tapas 禁止 AI 生成内容上架）。本轮不把它们写成默认投稿推荐。对照表在研究报告。

### 已核验政策（查阅日 2026-11-08）

只写当日官方页已核对的结论。出处与可靠性分级见 `integrations/grokbot/overseas-research.md`。

**Royal Road**（https://www.royalroad.com/support/knowledgebase/114）

- 允许有限 mature content，**禁止把色情或性内容当作核心或主要卖点**。Sexual Content 标签不等于可以写 erotic fiction；**erotica 禁止**。性描写保持最小必要。
- Mature 措辞不得出现在标题、简介、章名等作品页可见处。封面严禁 NSFW。
- AI 必须按平台规则标注 **AI-Assisted** 或 **AI-Generated**。生成内容要作者审校。评论区互动不得用 AI。官方对「经双语审校的 AI 翻译可以不标 AI-Assisted」有单独表述，投稿前再读 KB 原文。

**Amazon KDP**（https://kdp.amazon.com/en_US/help/topic/G200672390 ，Artificial intelligence (AI) content）

- **AI-generated** 的文本、图像（含封面和内页）或翻译，必须向 Amazon 披露。
- **事后大幅编辑，仍然算 AI-generated，仍然必须披露。** 不得声称「润色过就不用披露」。
- **AI-assisted**（作者自己写，AI 做润色、校对、头脑风暴、查错）不必披露。
- 作者仍要满足内容指南和版权要求。Romance 与 pornography 的灰区以当日 Help 和类目实践为准，这里不编造执法案例。

---

## 一·史、历史平台（不再推荐新投）

### Radish — 已停运

- **状态**：官方于 **2025-12-31** 关闭 Radish app（「As of December 31st, 2025, the Radish app has officially closed.」）。关闭后已解锁章节不能再读。
- **出处**：https://radish.groovehq.com/help/radish-app-sunset （查阅 2026-11-08）。可靠性：官方帮助中心。展开说明见研究报告「历史平台」。
- **知识库动作**：移出可投平台。**不要推荐新投**，不要在选题里把它和 Wattpad 并列。
- **与 Tapas**：公告说明二者业务分开，**Tapas 不受这次关停影响**。阅读历史和作品**不能**自动迁到 Tapas。本库不自动改投，也不承诺迁移。作者若自己改去 Tapas，须另核 Tapas 当日规则（含禁止 AI 生成内容上架）。

---

## 二、英文 vs 中文 底层逻辑（连载常见读法）

| | 中文网文 | 英文网文连载 |
|---|---|---|
| 卖点 | 剧情**爽点** | 情绪**钩子**（强度按类型调） |
| 读者关注 | 世界观、爽感、设定讲解 | 人物、感情、场面里的规则 |
| 节奏 | 可铺垫 | 连载希望前段就有事；完本可以更慢 |
| 解释 | 愿意看「为什么爽」 | 更讨厌说明书，但仍要公平线索和术语一致 |
| 开头示例 | “血色残阳下，少女眸光冷冽。” | `I never expected my life to change that night.` / `The dead man opened his eyes.` |

> 一句话：英文连载读者通常希望先进入场面。类型不同，解释可以外置成 glossary，不必删掉动机。

---

## 三、英文连载里容易劝退的写法（按类型判断，不要一刀切）

### 1. 无信息的长段落

连载手机阅读怕一整屏风景和回忆。要短的是**不推进的段**，不是所有句子。

- ❌ 一大段叙述 + 回忆 + 心理，没有新信息。
- ✅ 紧张段：`I looked outside. / Rain hit the window. / The memory came back.`
- KDP Romance / Slow Burn 的关系场景可以更长，只要每段改变「知道 / 想要 / 害怕」之一。

### 2. 替读者总结

少写「她之所以这么做是因为……」。动作和后果通常够用。惊悚若使用不可靠叙述，隐瞒必须事后公平。

- ❌ `She was angry because...`（纯说明）
- ✅ `She slammed the door.`

### 3. 堆形容词

- ❌ `Her beautiful, gorgeous, stunning eyes...`
- ✅ `Her eyes stayed on me.`

---

## 四、英文排版（连载默认）

- 章标题：`Chapter 1`（不是「第一章」）。翻译路径里若作者要求保留中文章名结构，先问再改。
- 连载段落宜短、段间空行。完本不必把每句都拆成一行。
- **对话默认换行，一句一行**：

```
"Who are you?"

I froze.

"Answer me."
```

- 同一轮里把对话和动作挤成一行，阅读体验通常更差：`"Who are you?" I froze. "Answer me."`

---

## 五、节奏：连载希望前段有事，完本看整本

- ❌（只为凑字的铺垫）女主起床 → 洗脸 → 吃饭 → 出门 → 撞见男主，中间没有选择。
- ✅ 连载第一句就可以开始：`The dead man opened his eyes.`
- ✅ 慢热可以先给一个具体的关系事实，而不是假悬崖。

---

## 六、英文连载常用的开篇钩子

- **身份反转**：`My husband murdered me. Then I woke up three years earlier.`
- **危机/倒计时**：`The timer on my arm showed 00:59.`
- **秘密**：`Everyone in town knew the truth except me.`
- **禁忌关系**：`I accidentally married my enemy.`

这些是钩子菜单，不是每本书的义务。Royal Road 的标题和简介不要把 mature 内容写成卖点。

---

## 七、英文情绪表达：用身体反应，不喊抽象

- ❌ `Her heart was breaking.`（接近「心如刀割」，英文叙事里很少这样直说）
- ✅ `I couldn't breathe.` / `My hands shook.` / `My throat went tight.`

和中文的 show-don't-tell 同一方向（见 `show-emotion.md`）。英文连载更常写生理反应。这仍是偏好：必要时一个准确的情绪词可以留下。

---

## 八、AI 写英文时常见的三种痕迹

下列是编辑可观察的特征，**不能**当成「鉴定是否 AI 创作」的证据。

1. **太正式**：`Therefore... / However... / Furthermore...` → 像论文。改口语连接或删。
2. **太工整**：`He smiled. She smiled. He walked. She walked.` → 打破对称（见 `sentence-rhythm.md`）。
3. **空文学**：`Moonlight danced gracefully upon the crystal lake...` → 只留推动场面的细节。

---

## 九、平台 × 题材速配（现行）

- **Wattpad**：Romance / Billionaire / Mafia / Werewolf / Enemies-to-Lovers / Fake Dating（女性向情绪流）。
- **Royal Road**：LitRPG / Progression / System / Dungeon / Cultivation。性内容不可当卖点；AI 要标注。
- **Webnovel**：System / Reborn / Urban / Sign-in / Campus。AI 政策待核实；签约前读合同。
- **Amazon KDP**：完结本。AI-generated 文本 / 图像 / 翻译必须披露。
- **短篇/广告流（TikTok/Reels）**：强钩子、强反转、超短段落。这是广告体，不要反过来说服所有长篇。

**不要推荐 Radish。** 它已于 2025-12-31 关闭。

---

## 十、给中国作者的一句话

反转、钩子和快节奏适合 Wattpad 短篇、Webnovel 连载和短视频小说流。Royal Road 要守住「性内容不是卖点」和 AI 标签。KDP 要守住 AI-generated 披露。把「解释爽点」改成「场面里让人自己感到」，通常就离开了翻译腔；句有多短、钩有多密，按类型表调。

## 相关

- 英文写作 / 改编 / 翻译技能 → `skills/english`（original / adapt / translate）
- 海外研究交接（Grok Bot，不替代 Grok API）→ `integrations/grokbot/overseas-research.md`
- 去 AI 味（中英通用思路）→ `deslop`、`human`、`sentence-rhythm.md`、`show-emotion.md`
- 钩子结构（中英通用）→ `hook-library.md`
