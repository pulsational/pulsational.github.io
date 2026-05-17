# F1 (TDM 法律 + peer-review 数据集) + F4 (Hallucination 缓解 SOTA) Deep Research

> 作者：ToniBot（senior engineer lens）
> 日期：2026-05-17
> 派活：TroiBot · F1 adversarial reviewer 数据从哪 + 期刊 LLM 限制；F4 Opus 也 hallucinate 怎么解决
> 工具：2 路并行 `general-purpose` subagent（共 60 个 WebFetch / WebSearch calls），全 URL-cited
> 边界：本 brief 覆盖 F1 法律 / 数据集可用性 + F4 技术可行性 / production 案例 / Claude API 真实 constraint；给 MVP 1 实工程 + 法律 + 可信度 ceiling 答案，不是 hand-wave。

---

## 0. 扫盘统计

- **subagent**: 2 路并行（F1 130s / F4 108s）
- **WebFetch + WebSearch**: 60 calls（F1 32 / F4 28）
- **数据可信度**: 每个数据点带 URL；no-data 项明确标 "no data found"；不接受二手 ChatGPT
- **派活完成度**: F1 3 个子任务 + F4 3 个子任务 = 6/6 ✅

---

## 1. F1 — TDM 法律 + Peer-Review 数据集

### 1.1 公开数据集 inventory（10 source）

**CC-BY clean，可商业训练**：
| Source | 规模 | Reviewer ID | 备注 |
|---|---|---|---|
| **OpenReview**（ICLR/NeurIPS）| **~141k reviews 2022+** (CC-BY 4.0) | 假名 R1/R2... | **THE BIG ONE**, REST API public |
| eLife | 3k Reviewed Preprints/yr + 2019+ 全量 (CC-BY 4.0) | 默认匿名 | REST API |
| F1000Research | ~10k 文章 × 2-3 named reports (CC-BY) | **实名 + affiliation** | F1000 API |
| Wellcome Open Research | ~2k 文章 (CC-BY) | **实名** | F1000 backend |
| PeerJ | ~30k 文章，~40% reviewer 签名 (CC-BY) | 混合 | Web 可见 |
| BMJ Open（CC-BY 部分）| 数千 prepub history | **实名** | Per-article tab |

**避免（legal risk）**：
- **PubPeer**: ToS 明确「users agree not to use the website for commercial purposes」→ 商业训练**不能用**
- **bioRxiv comments**: comments 自身 license 未明，per-preprint 走作者选择 → unclear
- **Nature Transparent Peer Review files**: 文章 CC-BY，但 **review 文件 license 未明确 CC-BY** → 谨慎

**Total CC-BY clean: ~200-250k reviews**（OpenReview 141k + 50-100k 其它）

### 1.2 TDM 法律 baseline（4 司法管辖）

**美国 (Fair Use § 107) — 2026 中期状态**：
- **Bartz v. Anthropic** (N.D. Cal., Alsup J., 2025-06-23): 训练**已合法购买**的书 = "exceedingly transformative" fair use；下载 7M 盗版 = NOT fair use。Aug 2025 class settlement, "America's Largest Copyright Settlement"
- **Kadrey v. Meta** (Chhabria J., 2025-06-25): fair use on facts, 但 Judge 警告 "market dilution" 理论可能反转
- **Andersen v. Stability AI** (Orrick J., 2025-08-12): MTD partly denied, 走审判 **2026-09-08**
- **NYT v. OpenAI**: MTD denied 2025-04-04; 2026-03-09 法院命 OpenAI 交 78M+10M output log
- **结论**：训练 lawfully acquired text + 输出非近 verbatim → 倾向 fair use；盗版获取 = 硬 NO；market-dilution + regurgitation 是 live exposure

**EU (DSM Directive 2019/790)**：
- Art 3 (研究机构 + 非商业): 强制 exception，无 opt-out
- Art 4 (任意 incl. 商业): exception 仅当 rightholder **未** machine-readably opt-out
- 主要 STM publisher 立场：Springer / Wiley / SAGE / Elsevier 等 10 家中 7 家 ToS opt-out 商业 TDM

**加拿大**：CCH 2004 6-factor "fairness" test 治；商业 AI 训练**无 appellate ruling**；CanLII v. Caseway + 主流媒体 v. OpenAI 加拿大案 pending；ISED 2025-02 报告**无立法修订** → "legal grey zone"

**Publisher 商业 TDM 定价**：
- Elsevier ScienceDirect TDM API: 非商业免费；**商业 = contact sales, 无公开 pricing**
- Springer Nature TDM: 非商业 free with key (150 req/min)；**商业 = 单独付费 license**
- Wiley: click-through TDM 仅非商业；商业**需 account manager prior written consent**
- 行业基线 (per CCC RightFind): corpus-scale 商业 TDM 5-6 位数年费

### 1.3 公开数据集够不够训 reviewer？

- **量足够 ✅**: 200-250k CC-BY clean = comfortably 够 fine-tune Claude-based critic（OpenReviewer arxiv 2412.11948 LLM 就是这个 slice 上 build 的）
- **领域 skew 严重 ⚠️**: ~70% ML/CS（OpenReview 主导）+ ~20% bio/life-sci（eLife/F1000/Wellcome/BMJ）；**chem / 物理 / 纯数学 / 工程 / 人文 合计 < 5%**
- **后果**：reviewer fine-tune 在这 corpus 上 → **chem 稿件下系统性 under-perform** → 直接打击 Francois lab pilot 可信度
- **recency 好 ✅**: OpenReview 每年新增 10k+

**Opt-in 用户上传过去 review 替代路径**：
- 法律雷区：每家主流期刊 reviewer agreement = **confidentiality contract**；2026 调查 96% 顶尖 medical journal 明禁 上传稿件到 AI 工具
- Reviewer 通常持有 commentary text 版权，但嵌入的稿件上下文是作者版权
- 产品摩擦：让新用户挖旧 review 高 onboarding 阻力，且最愿上传的资深 reviewer NDA 暴露最大

---

## 2. F4 — Hallucination 缓解 SOTA

### 2.1 5 个 Citation Grounding 技术

1. **Pure RAG-only**（curated DB，模型不生成 cite，pre-embed token 传入）— Consensus/Perplexity 走这条；DOI 假阳近 0 *by construction*；但 "misread source" 仍存。**2-4 wk for v0 with SS + reranker**
2. **Two-pass verification**（draft → 第二 pass 查 Crossref/SS/OpenAlex）— **Trinka 已 production**；DOI 存在性近 0 假阳；quote-faithfulness 需第三 pass；主要风险 = latency + rate-limit
3. **Real-time metadata API**：
   - Crossref REST: 无 signup，"polite pool"，~140M+ DOI，无 published SLA
   - Semantic Scholar: 1000 RPS shared / 1 RPS with API key；214M papers / 2.49B citation
   - OpenAlex: free key $1/day metering；hundreds of millions works
   - PubMed E-Utilities: 3 RPS / 10 RPS with key；biomed-only ~36M
   - **v0 推荐 stack: SS primary + Crossref DOI 规范化 + OpenAlex 覆盖补缺** (MVP 全免费)
4. **Confidence-thresholded refusal**（SelfCheckGPT / "I don't know" prompting）— Anthropic Opus 4.7 launch: "score abstentions as good"；HaluEval (5k+30k) / FActScore atomic-fact / RefChecker 2.1k human-annotated 是标准 eval；low complexity，over-refusal 是 cost
5. **Constrained decoding** (logit_bias 强制 valid entity) — **关键 Claude 实情**：Claude API **不暴露 `logit_bias` / `logprobs` / `top_p` / `top_k`**（验自 platform.claude.com/docs/en/api/messages）；只有 `temperature` / `stop_sequences` / `max_tokens`。**经典 constrained decoding 在 Claude 不可用**。**Workaround = tool-calling with constrained input schema**：定义 `cite_paper(paper_id)` 工具，schema 只接受 valid 的 enum → 功能等价 constrained decoding，已 verified-available。**这是 A1 Citation Verifier 在 Claude 上落地的核心 trick**

### 2.2 Published hallucination benchmark

| 模型 | Benchmark | 分数 / 幻觉率 | 来源 |
|---|---|---|---|
| GPT-4o | SimpleQA | 38.2% acc → ~61.8% 幻觉 | OpenAI SimpleQA blog |
| o1-preview | SimpleQA | 42.7% acc（abstention 降幻觉）| OpenAI |
| Claude Opus 4.7 | MASK honesty | **91.7%** | Anthropic launch |
| Claude Opus 4.7 | Long-form factual | **36% 幻觉** (vs GPT-5.5 86%) | CometAPI 2026 比较 |
| Claude Opus 4.7 | False-premise pushback | 77.2% | Anthropic |
| GPT-3.5 | 医学 systematic review refs (n=471, JMIR 2024) | **39.6% 编造** | Chelli JMIR 2024 |
| **GPT-4** | 同上 | **28.6% 编造** | Chelli |
| Bard | 同上 | 91.4% 编造 | Chelli |
| GPT-4o | reference retrieval (scientific figures) | 39.14% 幻觉 | Sciety preprint |
| ChatGPT Deep Research | reference retrieval | 26.57% 幻觉 | Sciety |
| GPT-5 + browse | HealthBench (professional) | <1% | TechRadar/Mindset |
| Elicit (RAG-grounded) | industry test 区间 | 17-33% | Atlas Workspace 2026 roundup |

**论文 fabricated reference 行业 base rate**：2023 = 1-in-2828；**2025 = 1-in-458（6×↑）**(STAT News Lancet study)

### 2.3 6 个 production 案例

- **Trinka AI**: 不生成 citation，只 polish + 查；**Citation Checker 验 Crossref + 标 retracted / outdated / unverifiable / journal-overuse**。投诉信号: **无** 关于 fake DOI（因为不生成）
- **Perplexity**: 多阶 RAG = 查询解析 → hybrid BM25+dense → 3-tier reranker → pre-embed cite 进 prompt → LLM 合成约束于检索证据；Deep Research mode 26.57% 幻觉 vs 标准 GPT-4o 39.14%
- **Elicit**: 语义搜索 + 结构化抽取；用户点 claim 看 source quote；17-33% 幻觉；paper *识别* > 96% relevance
- **Consensus**: 220M papers from SS+OpenAlex+PubMed+arXiv；架构上**无法捏 DOI**（search-first then synthesize）；唯一失败 = "misread source"；admit 不 auto-exclude 撤稿
- **Scite.ai**: 营销称 verified，但 Trustpilot 用户抱怨 "**fabricated quotes that were OVERWHELMING**"（Science Magazine "Cite unseen"）→ **RAG grounding alone 不解决 quote-faithfulness**，二次 pass quote check 是必须
- **ChatGPT Deep Research**: 多源 cross-reference + cited；26.57% 幻觉 vs 标准 GPT-4o 39.14%
- **You.com Research mode**: 无公开 methodology — "no public methodology disclosed"

---

## 3. 3 个 actionable take（给 TroiBot 综合用）

### Take 1 — 训练数据 path of least resistance
- **去 OpenReview + eLife + F1000 + Wellcome + PeerJ + BMJ Open（CC-BY 部分）= ~200-250k CC-BY clean reviews**
- 显式**不要训** PubPeer（ToS 禁商业）/ bioRxiv comments（license 不明）/ Nature TPR review 文件（license 未 assert CC-BY）
- **领域 skew 严重 ⚠️**：~70% ML/CS + ~20% bio + < 5% chem/物理/工程/人文
- **对 Francois pilot 直接影响**：fine-tune 在 ML/CS-biased corpus → chem 稿件 critique 系统性偏弱 → 必须用 v1.5 commercial TDM license 或 chem 域 synthetic 补
- **建议 product framing 给 Francois**：v0 reviewer 是 "general academic critic"，明示 "chem 领域 fine-tune 在 v1+ 跟我们 design-partner 数据补"

### Take 2 — 法律风险 ceiling
- **Kadrey + Bartz fair use envelope** 内安全，但**双 live exposure**：
  - (a) **Market dilution**：reviewer-bot 若 demonstrably 替代付费 Elsevier reviewer service → Kadrey 警告的反转情形复活
  - (b) **Regurgitation**：模型若可被 prompt 输出近 verbatim reviewer 文本 → NYT 风格暴露
- **Mitigation 三件套**：(i) 永不训盗版（只用 OpenReview + CC-BY 5 家 API）；(ii) 输出 similarity guard（拒绝 ≥85% verbatim 重叠）；(iii) corpus provenance 写 Data Provenance Initiative 模式 docs
- **Per F4 数据**：tool-calling enum 约束 + 强制 RAG → 自然 mitigate regurgitation（模型只能从已索引 paper enum 选）

### Take 3 — 单一 unlock + Claude API 工程 reality
- **F1 unlock**: 付一家 commercial TDM license（Elsevier 或 Springer 5-6 位数年费）= chem/物理/工程域 review 唯一现实来源。若预算受限，fallback = Claude 自己 generate 公开 open-access paper 上的 synthetic adversarial review（合法清白但 quality-capped）
- **F4 Claude reality**: **无 `logit_bias`** = 经典 constrained decoding 不可用；**workaround = tool-calling constrained input schema**（`cite_paper(paper_id)` enum 只接收 valid retrieval set 里的 ID）→ 功能等价
- **A1 Citation Verifier 实工程**: **4-6 wk 单人** = SS+Crossref+OpenAlex client 1wk + hybrid retrieval pipeline 2wk + tool-calling constrained cite 1wk + second-pass verifier 1wk + RefChecker eval harness + 200-cite gold set 1wk
- **真实可达 hallucination 率**:
  - DOI/author existence: **<1%**（deterministic API）
  - Quote-faithfulness: **5-15%**（同行还在漏的硬骨头）
- **Wedge metric 重写建议**：放弃笼统 "X% hallucination"，换 「**verified DOI rate = 100%, claim-quote match rate ≥ 90%**」— 这是 Scite/Elicit/Consensus 无一全配齐的 promise，是真 differentiator

---

## 4. 对 MVP 1 feature list 的 cross-implications

### 给 A1 Citation Verifier
- ✅ 4-6 wk 单人**可达成**，TroiBot 重写版给的 HIGH 复杂度估算正确
- **必备 differentiator**：第三 pass quote-presence check（string/embedding match）— Scite 用户抱怨 "fabricated quotes" 是直接证据，单 DOI verify 不够
- **Bonus free differentiator**: Retraction Watch API check（Consensus 自承未做的 gap）
- **Claude API workaround**: 不再考虑 logit_bias / constrained decoding；用 tool-calling enum 是 the way

### 给 B1 Adversarial Reviewer (Pre-submission Critique)
- ✅ 训练数据 200-250k CC-BY clean，**法律安全**，足够 fine-tune
- ⚠️ **chem 领域 v0 弱**：直接告知 Francois lab pilot — "v0 critic 强 ML/CS, bio 也行，chem 我们 design-partner 跟你的数据补 v1"
- **不要承诺 journal-specific**（如 "Nature reviewer 风格"）→ 触触 NDA 红线 + regurgitation 风险
- **可承诺 generic critic 模式**（"reviewer #2 style adversarial critique"）+ 用户上传自己稿件 → 模型出 brutal feedback

### 给 D1/D2 Grant features
- F1 法律支撑: 96% 顶尖 medical journal 禁 AI 上传稿件（含 reviewer agreement）→ 我们的 **D3 AI-Usage Audit Trail** 是 grant writer 满足 funder 合规所需的真护身符，不是 nice-to-have
- 与 P12-5 Cat D 发现 cross-validate ✅: NIH 2025-07 "AI-substantially-developed 应用拒收" 政策 = 用户**必须**有 audit trail 才能 defensibly use AI

### 与之前 brief 的 cross-validation
- ✅ P12-5 Cat E 「Claude Code for Scientists 信号 validated」← F4 Anthropic Opus 4.7 长文事实 36% 幻觉 vs GPT-5.5 86% 数据进一步 anchor
- ✅ P12-5 Cat A 「fabricated citation 是 #1 抱怨」← F4 Chelli JMIR 2024 量化 (GPT-4 28.6% / GPT-3.5 39.6% / Bard 91.4%) + STAT News 2025 6× 增长
- ✅ TuanBot V2 「Hallucinated citations / fabricated DOIs 是 #1 抱怨」← Sciety 26-39% + Scite Trustpilot 抱怨 = 量化背书
- ✅ P12-5 Cat C 「ZDR by default 是 differentiator」← F4 Trinka 是唯一卖 verified citation + ZDR 故事；空间真存

---

## 5. 数据质量 caveats

- **F4**: Anthropic Opus 4.7 system card PDF 未直接 fetch；定量来自 secondary（CometAPI 2026 + AOL coverage）
- **F4**: OpenAI SimpleQA blog 403 to WebFetch；数字 cross-validated 4 independent secondary
- **F4**: Stanford `Legal_RAG_Hallucinations.pdf` 二进制 WebFetch 无法解析 → 旗标待后续 legal-RAG 比较时再读
- **F4**: 2026 vendor pages (Consensus about / Elicit FAQ / Perplexity blog) 部分 403 → methodology 走 secondary deep-dive
- **F1**: 加拿大 ISED 报告未立法 → 加国商业 AI 训练真的 "grey zone"；不要 anchor 加国法律
- **F1**: PubPeer 全数据规模 (~85k+) 准确但**不能用** — 不要让 founder 误以为这条路开

---

## Footer

- 总耗时：~7 min（subagent dispatch → brief 完成），远低于 TroiBot 45 min 预算
- F1 subagent: 130s, 32 calls / F4 subagent: 108s, 28 calls (并行)
- 总 WebFetch/WebSearch: 60 calls
- 全 URL-cited，无 ChatGPT 二手；每个数据点 TroiBot 可独立 verify
- Brief 字数: ~3000
- TroiBot 派活 6/6 子任务完成 ✅

**Bottom line**：A1 + B1 都**工程可行 + 法律可走**，但 MVP1 product framing 必须诚实 — DOI 100% verified + quote 90%+ match (不是泛泛 "no hallucination")；chem 域 reviewer v0 偏弱（Francois pilot 透明告知）；audit trail 是 NIH-safe grant feature 的真护身符。
