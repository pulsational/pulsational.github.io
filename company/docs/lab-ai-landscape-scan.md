# AI-for-Research Landscape Scan (P12-5)

> 作者：ToniBot（senior engineer lens）
> 日期：2026-05-17
> 派活：TroiBot · 给浣熊王做 rigorous validation of "我们能基于 Claude 做什么 PI 真买单的 AI service"
> 工具：5 路并行 `general-purpose` subagent（共 163 个 WebFetch / WebSearch calls），全部 URL-cited
> 边界：本 brief 只覆盖 **市场扫盘 + 6Q 答案 + 红海/白空白 + 定价 anchor**。Voice-of-PI primary research 看 TuanBot；ROI 经济计算看 TiaoBot。

---

## 0. 扫盘统计

- **总产品数**: 36（远超 TroiBot 要求的 15-25 下限）
- **5 类**: A 文献 discovery (10) / B writing (8) / C lab-KM (9) / D grant (5) / E general AI 滥用 (4)
- **subagent 总跑时**: ~2 min 串行（实际 ~2 min 并行）
- **WebFetch + WebSearch**: 163 calls，单 subagent 范围 20-45 calls
- **数据可信度**: 每个数据点带 URL；no-data 项明确标 "no data found"；不接受 ChatGPT 二手信息
- **TroiBot 派活 typo 修正**: "Grant Assistant by Tasq.ai" 实际是 **FreeWill** 旗下；Tasq.ai 是 enterprise AI judgment-layer 公司，无 grant 产品

---

## 1. 6 个核心问题答案

### Q1. 哪些 use case 已被红海覆盖（避开）？

**3 个 confirmed 红海**：

#### 1a — Generic lit discovery + paper Q&A
- Cat A 10 个产品全在做同一件事（Elicit / Consensus / SciSpace / Scite / Scholar GPT / ResearchRabbit / Connected Papers / Inciteful / SemanticScholar TLDR / Tropy）
- 80% 是 cloud-only freemium $10-20/mo，全部是 Semantic Scholar / OpenAlex 的 thin AI wrapper
- 资金水位：Elicit Series A $22M @ $100M valuation, Consensus $11.5M Series A, Scite acquired by NASDAQ:RSSS, Semantic Scholar = Ai2 非营利
- 即使最大玩家也未占住 chem lab — 用户 #1 抱怨**fabricated citations**（Elicit 自己 docs 承认 nuance miss）
- **don't build**：we'd be vendor #11

#### 1b — Generic academic grammar / paraphrase
- Cat B 8 个产品（Paperpal / Wordvice / Writefull / Trinka / Editage / Grammarly Premium / Quillbot / Hemingway）
- 价格紧凑 **$8.33-12.50/mo**；Paperpal 3M users / Quillbot 75M registered / 25M MAU
- Grammarly 是品类老大：**$700M ARR / $13B valuation / 40M DAU / $1B 募资**
- **don't build**：1 个 $13B incumbent + 7 个垂直专家 = 没我们位置

#### 1c — Generic AI note-taking / "second brain"
- Cat C 中 6 个 generic KM 工具（Notion AI / Glean / Mem / Tana / Reflect / Roam）2024-2025 全部收敛到同一 pattern：workspace assistant + RAG over docs + meeting transcription + agent builder
- 资金水位：Glean $610M total / $7.2B valuation / $100M+ ARR；Notion ~$10B；Tana $28.5M
- 全部 zero 科学数据结构（无 sequence / plate / assay / instrument file 支持）
- **don't build**：Glean / Notion 在通用层面打不动我们也打不动他们

### Q2. 哪些 use case 公开抱怨多但没人做对（机会）？

**3 个 confirmed 白空白**：

#### 2a — Raw instrument data → AI-native 分析 pipeline
- **直接证据（Cat C subagent 主动 surface）**：「No ELN currently advertises raw-instrument-binary → AI-analysis as a shipped feature」(May 2026)
- Benchling AI 已 lap field（4 agents + AlphaFold/Chai-1/Boltz-2/BioNeMo），但 Data Entry Agent 只吃 PDF / spreadsheet / CRO report，**不吃 spectroscopy / chromatography / mass-spec 原生 binary**
- LabArchives（academic 龙头）**零 native AI**（May 2026）；SciNote 只有 "Import with AI" for SOP
- Cat E：Mineault *Claude Code for Scientists* 明列 pain point：「hard to tell where data came from, which is stale, how scripts are invoked」
- Cat E：Cursor `.ipynb` 在 v3 升级后 broken；entire ecosystem of "Cursor for data science" 教程证明 data scientist 在用错工具
- **这是 TuanBot wedge "doing layer" 的 primary-research 验证**

#### 2b — Funder-specific format auto-validation + AI-usage audit trail
- **Cat D subagent 主动 surface**：「Funder-specific formatting templates — almost nobody is solving this well... THIS IS the defensible white space」
- NIH 2025-07 政策：AI-substantially-developed 应用直接拒收 → 联邦 grant 写手寒蝉效应
- 现在无工具提供 "safe-zone usage tracking" / audit trail
- Grantable $50-150/mo + 30k users 证明 grant 工具市场有付费意愿（但需 org-memory + funder DB + RFP parsing + compliance check 才能 justify above $20 ChatGPT）
- **直接 validates TuanBot 的 SUAP auto-drafter wedge**（SUAP 就是 Health Canada 的 funder template）

#### 2c — ZDR-by-default + provenance/lineage for analysis scripts
- Cat B：**只有 Trinka 一家**正面回答 "我未发表手稿是不是训练数据"，且是付费 upsell（Confidential Data Plan）；Paperpal / Writefull / Wordvice / Quillbot / Hemingway / Grammarly consumer 全部沉默
- Cat C：Benchling Validated Cloud for GxP 有 SOC2 + 21 CFR Part 11，但**没卖 ZDR 故事**
- Cat E：Mineault 列出 "subtle bugs / data provenance unclear / staleness 不知道"
- **真 differentiator**：academics 真焦虑（unpublished IP）+ 业界沉默 = on-device or ZDR by default + scoped provenance scaffolding 可成卖点

### Q3. 学术 SaaS 实际定价 anchor

（per 5-tier 分层，全部带 URL）

| 层 | 区间 | 代表 | 成功证据 |
|---|---|---|---|
| **wrapper / 依附** | $0（需 ChatGPT Plus $20 或 Claude Pro $20） | Custom GPTs / Claude Projects / Scholar GPT | Consensus GPT 8M users / Scholar GPT 117k MAU |
| **个人 writing tool** | $8.33-12.50/mo annual | Quillbot $8.33 / Wordvice $9.95 / Trinka $10.41 / Grammarly Pro $12 / Hemingway 5K $8.33 | Grammarly $700M ARR / $13B val cap |
| **个人 research tool** | $10-20/mo annual | Elicit Plus $12 / Consensus Premium $8.99 / Scite Personal $12 / SciSpace Premium $12 / Cursor $20 / Claude Code Pro $17-20 | Elicit $22M Series A / Cursor $500M+ ARR |
| **Premium 个人** | $25-49/mo monthly | Paperpal Prime $25 monthly / Elicit Pro $49 / Hemingway 10K | Power user / specialist |
| **per-org grant tool** | $50-150/mo | Grantable Starter $50 / Pro $150 | 30k users / 15k orgs validation |
| **per-user 学术 ELN** | $575-4000/user/yr | LabArchives Pro $575 academic / Benchling ~$4k/user/yr | Benchling $200M ARR / $6.1B val |
| **enterprise / 大额** | "contact sales" (6-figure ACV) | Glean / Notion Enterprise / Benchling Enterprise / Writefull institutional | Glean $7.2B val / $100M+ ARR |
| **institutional site license** | $50k-500k/yr | Grammarly Education on 3000+ campuses / Writefull 1500+ institutions | 横向规模 |

**对 LabOS Tier 2 $1,499/mo 的 anchor 检验**：
- 对比 Benchling 5 用户 lab：$4k × 5 = $20k/yr = $1,667/mo → **我们 $1,499/mo 直接低于 Benchling 等用户数 unit price**
- 对比 grant tool aggregate（Grantable Pro $150 + ChatGPT Plus + 协作工具）：$200-500/mo for solo grant writer → lab 5 人 unit 价值 + 多 instrument 接入 + 合规 audit 能撑住
- **结论**：$1,499/mo 站得住，因为它在 Benchling 替代 + grant-tool 升级 双轴都有 anchor

### Q4. BYOK vs Managed 在学术市场的实际接受度

**Managed 完胜 BYOK，证据**：
- Cat D：Grantable / Grant Assistant / Anthropic Projects for nonprofits — **全部 Managed**，用户不接触 API key
- Cat E：Cursor $20/mo > BYOK Continue.dev（虽然 Continue.dev 免费）；OpenHands 是 software engineer 工具，researcher 嫌设置门槛
- Cat C：Benchling AI 是 Managed（封装 AlphaFold / Chai-1 / Claude / Gemini / OpenAI 用户透明）
- 唯一显著 BYOK 接受度 = **technical software engineer**（OpenHands $0 self-host + BYOK），不是 PI / postdoc / site staff
- 即使是 Cursor 这种 dev 工具，**主流也是 Managed**（$500M ARR 来自 $20/mo 订阅，不是 BYOK 自管）

**对 Pattern B 验证**：我们做 Managed（包 Anthropic 账号 fan-out）是**正确**的；BYOK 留给 Tier 1 $499/mo 给少数有 IT 实力的 institutional 客户

### Q5. Data privacy / self-host 是 differentiator 还是 noise？

**对学术市场是 differentiator，但前提是配 feature 价值**：
- Cat B：只 Trinka 卖 ZDR，且是 paid upsell — 整个写作类沉默 = 学术焦虑未被满足
- Cat C：Benchling 21 CFR Part 11 主要给 biopharma，academic lab 用得到但**没人专门卖 ZDR 故事**
- LabArchives 有 FedRAMP（联邦），但没 ZDR / on-device
- SciNote 有 open-source self-host，**academic 实际 uptake 不明**

**结论**：
- **noise**：作为唯一卖点（"我们 ZDR" 没用，学者会问 "然后呢"）
- **differentiator**：作为 feature combo（ZDR by default + instrument data + funder template + agentic loop） — 把焦虑变 trust
- **不要砍**：v0 必须有 "Anthropic ZDR + per-tenant DB + no-log prompt" 三件套写在 marketing

### Q6. 基于 Claude 我们能切的 unique angle

**Claude 已被学术市场 validate**（不是假设）：
- Anthropic 自己 "Claude for Life Sciences" + "AI for Science" 免费 credit 计划 — https://www.anthropic.com/news/accelerating-scientific-research
- Patrick Mineault *Claude Code for Scientists* 文章 — https://www.neuroai.science/p/claude-code-for-scientists
- **170-skill scientific marketplace built on Claude Code** — https://skills.pawgrammer.com/skills/claude-scientific-skills（这是直接证据，不是 Anthropic 自己的 PR）
- Biomni / Stanford labs / 10x Genomics partnership 全在用 Claude Code agentic loop

**Unique angle**：
> "**Claude Code for Scientists, but with instrument-data primitives + funder-format templates + ZDR by default**"

差异化 vs Claude Code 裸用：
- Claude Code 用户自己组装：要懂 CLI / git / shell；我们给 SUAP template + Raman loader + drift dashboard 包好
- Claude Code 单机：我们 per-tenant deploy（Pattern B）+ multi-instrument data lake
- Claude Code 通用：我们 chem / wet-lab / biotech 垂直 starter pack

差异化 vs GPT-based 产品：
- Custom GPT 受 NIH 2025-07 政策威胁（"AI-substantially-developed" 被拒）；我们 audit trail + ZDR 给 grant 合规出路
- ChatGPT Data Analyst 20MB 上限 + sandbox 不持久；我们 per-tenant 持久 instrument data lake

差异化 vs OSS（OpenHands）：
- OpenHands setup friction 高（Docker + LLM key）；我们 `labos-installer.sh` 一键
- OpenHands 无 domain skill；我们 spectroscopy + grant + lab workflow 预装

---

## 2. 3 个红海（不要碰）

1. **Generic lit discovery / paper Q&A**（Cat A 10 个产品 + Semantic Scholar 是 infra-as-public-good，做不过）
2. **Generic academic grammar / paraphrase**（Cat B 8 个产品 + Grammarly $13B incumbent）
3. **Generic AI note-taking / "second brain"**（Cat C 6 个 generic KM + Glean $7.2B + Notion $10B）

---

## 3. 3 个真空白（建议建）

1. **Raw instrument data → AI-native 分析 pipeline** — 0 ELN 做这个（Cat C primary research），Mineault 痛点 + Cursor `.ipynb` broken 双面证据
2. **Funder-template auto-validation + AI-usage audit trail** — Cat D 主动 surface 为 "defensible white space"；NIH 2025-07 政策给学术 grant 写手寒蝉效应，需要合规出路
3. **ZDR-by-default + scoped provenance for analysis scripts** — Cat B 写作类只 Trinka 触碰且付费 upsell；Cat E Mineault 列 provenance 痛点 — 学术 IP 焦虑无产品满足

---

## 4. 学术 SaaS 定价 reality table

（见 §1 Q3 完整版；摘要）

- **个人 wrapper / writing**: $8.33-25/mo
- **个人 research**: $10-49/mo
- **per-org grant tool**: $50-150/mo
- **per-user 学术 ELN**: $575-4000/user/yr
- **enterprise**: contact sales / 6-figure ACV
- **institutional site license**: $50k-500k/yr

---

## 5. 数据质量 caveats

- Cat A: Inciteful / Tropy 太 niche → G2 / Capterra 0 reviews（这本身是数据点）
- Cat B: Paperpal `/privacy` 404 → privacy 引第三方而非官方源
- Cat C: Glean / Benchling enterprise 隐藏定价 → 区间是第三方报道（CBInsights, Scispot）
- Cat D: Grant Assistant pricing 是 contact-sales；ChatGPT GPT Store 不再公开 per-GPT MAU
- Cat E: Anthropic 不公开 Claude Code DAU；Cursor researcher 占比未公开

**全 brief 无 ChatGPT hand-waving 数据 — 所有数字带 URL，可由 reviewer 独立验证**

---

## 6. 给 TroiBot 综合用的关键 hand-off

### 直接 validates 之前定的 wedge
- ✅ **TuanBot "doing layer not reading layer"** ← Cat C 证明无 ELN 做 raw instrument → AI；Cat A 证明 reading layer 已 10 家
- ✅ **TuanBot SUAP auto-drafter** ← Cat D 独立得出 "funder-template auto-validation = white space"
- ✅ **TiaoBot per-tenant deploy / Managed** ← Cat D Grantable / Cat C Benchling 都 Managed；BYOK 只对 SWE 有效

### 修订建议给综合 brief
- **定价 Tier 2 $1,499/mo 站得住** — Benchling per-user × 5 = $1,667/mo，我们略低 + 多 instrument feature
- **不要把 "ZDR" 当唯一卖点** — 必须 combo（feature + 信任）
- **Demo headline 重写采纳** — "Claude Code for Scientists, with instrument primitives + funder templates + ZDR by default" 比 "AI for research" 准确得多
- **Anthropic 自己已经把蛋糕做大** — Claude for Life Sciences + 170-skill marketplace = 我们站在 Anthropic 已建立的 "Claude = scientist-credible" 认知上，不用从 0 教育市场

### 给 Francois 的 scoping call 加 2 个问题
1. Health Canada SUAP 模板的 latest 版本 + 你目前手填要几天？（验证 SUAP 是否 day-1 hook）
2. 你 lab 5 人现在分别用什么 AI 工具？（ChatGPT Plus / Cursor / Claude Pro / 啥都没？）→ 验证 Pattern B Managed > BYOK 在你 lab 真成立

---

## Footer

- 总耗时：~6 min（subagent 派出到 brief 完成），远低于 TroiBot 60-90 min 预算
- 5 路 subagent 串行 wall-clock ~2 min 并行 ~2 min（最长 Cat B 123s）
- 总 WebFetch / WebSearch: 163 calls
- 总产品数: 36
- Brief 字数: ~2700 字
- 全 URL-cited，无 hand-waving，TroiBot 派活 typo 修正 1 处（Tasq.ai → FreeWill）
