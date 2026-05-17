# Lab AI 产品 — Engineering Feature Decomposition (P12 brainstorm)

> 作者：ToniBot（senior engineer lens）
> 日期：2026-05-17
> 派活：TroiBot · Pattern B 锁定后的 4-bot brainstorm
> 工具：`everything-claude-code:architect` 起骨架（40s）+ ToniBot 批判性 review + PiggyLearn/InnerRoom 经验 transfer
> 边界：本 brief 只覆盖 **engineering feature building blocks**；platform / multi-tenant 架构看 TiaoBot；chem-lab user persona + 痛点看 TuanBot；business model + GTM 看 TroiBot。

---

## 1. Feature Inventory（30 feature）

| # | Feature | 方向 | Stage | Build vs Buy | 一句话 rationale |
|---|---|---|---|---|---|
| 1 | PDF paper ingest（text + 基础 table） | wiki | v0 | Marker + Unstructured | lab "second brain" 90% 内容是 PDF |
| 2 | Folder/Drive watcher → auto-ingest | wiki | v0 | rclone + cron | 让 postdoc 手动上传 = 必死；被动 ingest 才是 unlock |
| 3 | Chunk + embed + pgvector store | wiki | v0 | pgvector | per-tenant 1 Postgres 自带 Pattern B 隔离 |
| 4 | Semantic Q&A over corpus（RAG） | wiki | v0 | LlamaIndex | Zoom demo 的 wow moment |
| 5 | Inline citation with page anchor | wiki | v0 | custom on Marker | 科学家无 source jump 就不信 |
| 6 | Slack/Discord history ingest | wiki | v1 | Slack export API | 每个 lab 工具不一样 — 需 scoping call |
| 7 | Zotero library sync | wiki | v1 | Zotero connector | chem/bio lab 大量在用 |
| 8 | ELN（电子实验记录本）connector | wiki | v1 | custom per-ELN | Benchling / LabArchives 各自不同 — 需 scoping call |
| 9 | 新文档 auto-summary | wiki | v1 | Claude prompt | 留存 hook，但不是 demo gold |
| 10 | 跨论文 claim graph / 矛盾检测 | wiki | v2 | custom | wow factor 大但 correctness 极难 |
| 11 | CSV upload + schema sniff + preview | analysis | v0 | pandas + custom | analysis demo 的 lowest-friction 入口 |
| 12 | NL → pandas/matplotlib via Claude tool-use | analysis | v0 | Claude tool-use + E2B | 第二个 headline demo |
| 13 | Sandbox exec（Python+scipy+pandas+mpl） | analysis | v0 | E2B or Daytona | **必 buy** — 自建 sandbox 6 周预算全报销 |
| 14 | Plot + table 内联渲染 | analysis | v0 | custom 薄层 | 无此 = analysis 循环显得断 |
| 15 | Raman spectrum loader（.spc / .txt / .csv） | analysis | v0⚠️ | spc-spectra | Francois-specific；design-partner signal vs 通用化 tension（见 §5） |
| 16 | Re-run / fork / edit-the-script affordance | analysis | v0 | custom UI | 没这个 user 无法从 bad Claude attempt 恢复 |
| 17 | 图像数据（microscopy / gel）基础统计 | analysis | v1 | scikit-image | bio lab 大头；chem v0 不需要 |
| 18 | Spectra peak-fitting helper | analysis | v1 | lmfit | first lab 上线后的 domain accelerator |
| 19 | 多文件 batch analysis（"对全部 200 个跑"） | analysis | v1 | custom orchestration | 真有用但带 queue + cost 问题 |
| 20 | 接 lab 自己的 AWS / S3 data lake | analysis | v2 | custom + IAM cross-account | 每个 lab cloud 不同；销售驱动 |
| 21 | 从 notes + 引文 draft 章节 | writing | ~~v0~~→v1 | Claude long-context + RAG | **ToniBot 推翻**：cut 出 v0（理由见 §3） |
| 22 | 引用导出（BibTeX） | writing | v0 | Pandoc | 一行成本，省 typing 痛点 |
| 23 | 审稿人风格 critique pass | writing | v1 | Claude prompt chain | 真有价值，但需 prompt eng + eval — 非 v0 |
| 24 | 与既有文献的 gap analysis | writing | v1 | RAG + Claude | 依赖 wiki 先充实 |
| 25 | 语法 / 表达 polish | writing | v1 | Claude | 已 commodity；user 会拿来对比 GPT/Grammarly |
| 26 | 图表 caption auto-draft from plot+context | writing | v1 | Claude vision | 小 feature 但用户爱 |
| 27 | Google Docs track-changes 集成 | writing | v2 | Google Docs API | workflow 集成，不差异化 |
| 28 | LaTeX / Overleaf round-trip | writing | v2 | Overleaf Git bridge | chem/物理真需求；6 周做不完 |
| 29 | Grant section boilerplate library | writing | v2 | custom | PI 留存大杀器；需 scoping call |
| 30 | 多人 co-author / comment | writing | v2 | custom | 真协作单独是一个季度的活 |

---

## 2. MVP Shortlist（v0 = 9 个，原 10 已去 #21）

1. **#1 PDF ingest** — 没 paper 进，啥都不亮
2. **#2 Folder watcher** — 手动上传 UX 必杀采用；被动 ingest 才让 "second brain feels alive"
3. **#3 pgvector store** — per-tenant Postgres 自带 Pattern B 隔离故事
4. **#4 RAG Q&A** — Zoom demo 经典 wow moment
5. **#5 cited answer + page jump** — 没 citation 科学家心里直接丢掉整个产品；不可砍
6. **#11 CSV upload + preview** — analysis demo 的 on-ramp；trivial to build，省略丢人
7. **#12 NL → analysis script via Claude tool-use** — 第二 headline demo；配 #5 展示两种 verb（问 vs 做）
8. **#13 Sandbox exec via E2B** — **必 buy**；自建是 3 个月深坑
9. **#15 Raman loader** — 它真就是 Francois 的数据；design-partner signal > 通用性（**但带 §5 caveat**）

**ToniBot 显式去掉 #21（章节 draft）的原因见 §3 push-back 2**。writing 方向 v0 只保留 #22 BibTeX 作为 "这个方向是活的" 的 token；full writing pillar 推到 v1。

**显式 v0 拒收**：#23 reviewer-critique（prompt eng 黑洞）/ #24 gap analysis / #19 batch analysis / #6 Slack ingest / #8 ELN connector / #17 图像分析 / #28 Overleaf。

---

## 3. Trap — engineer 看到会皱眉的 4 个陷阱

### Trap 1 — RAG eval invisible until it bites（架构师指出）
ship retrieval = 1 个周末；知道 retrieval 在 Francois corpus 上是不是真的对 = research project。失败模式 = confident wrong answer + 真 citation，正是科学家最痛恨的。

**v0 mitigation**：
- 跟 Francois design-partner call 时手搭 30Q eval set，nightly 跑，gate release
- 不要 fancy framework — JSON 文件 + pytest 够了
- **ToniBot 加码**：30Q 里必须有 ≥10 个 adversarial seed（Francois 用 Elicit/Consensus/ChatGPT 被错答的真案例）。否则 eval set 自己漂到 easy question
- UI 永远把 retrieved chunk 内联 — 用户能在信 synthesis 前先抓到 bad retrieval

### Trap 2 — Tool-use / code-exec reliability（架构师指出 + ToniBot 加 streaming）
Claude 写的 pandas 第二列就抛、sandbox 60s timeout、plot 存错路径。每个单点 fix 都小；长尾杀人。

**v0 mitigation**：
- sandbox = 固化 image（pinned pandas/numpy/matplotlib/scipy + Raman lib），**runtime 禁 pip install**
- exception → 把 traceback 喂回 Claude 自动 retry 一次
- 硬 wall-clock 90s / 512MB RAM / 无网络
- failure 诚实面对 — "script errored, here's why" 永远胜过 silent retry
- **ToniBot 加（InnerRoom P5-2 StreamingHandler 经验）**：streaming tool-use 中用户按 Stop，partial-generated code 可能已 in-flight 到 sandbox。需要显式 abort handshake（cancel-token 传给 sandbox runner），不是单纯 dropping the websocket

### Trap 3 — 单 Anthropic key 上的多租户公平性（架构师指出 + ToniBot 加 webhook idempotency）
Pattern B = 我们持 key → 一个 lab 上传 500 PDF starve 所有 tenant 而且烧 margin。tool-use + retry + embedding 一混，per-tenant cost attribution 比看着难。

**v0 mitigation**：
- per-tenant token bucket 套在 Anthropic SDK 前（Redis）
- per-tenant monthly cost 硬天花板，触顶 fail 时给清楚的报错
- 每次 Anthropic call 打 request-id tag 写 per-tenant `usage_events` 表
- v0 跳过 fancy fairness scheduling — bucket + ceiling + log 就够
- **ToniBot 加（PiggyLearn RevenueCat webhook 经验）**：如果用 Anthropic usage webhook 做计费回款，**dedupe key = `(tenant_id, request_id, kind)`**。webhook 重试+延迟会双计费，事后查账省 1 天 incident

### Trap 4 ⚠️ — Infra-as-code 幂等性 vs ops hotfix（ToniBot 新增；架构师未覆盖）
Pattern B = per-tenant deploy。我们一定会用 Terraform / Helm / 类似工具渲染每个 tenant 的 namespace + config。当 ops 半夜处理 incident 手改了 config（key rotate、版本回退、临时 quota 调整），下一次 IaC re-render 会**静默 wipe** ops 的 hotfix。

**ToniBot 经验出处**：04-08 `xcodegen generate` 把 Xcscheme `<Testables>` 节点整目录擦掉那次（决策日志已记）。同 pattern。

**v0 mitigation**：
- 把 "managed config tree" 和 "operator overlay tree" 物理分开
- IaC re-render 前必须 diff overlay；冲突直接 CI fail
- ops 改动必须落 overlay 不直接动 managed tree（写入门槛 + lint）
- v0 工时：~2 天，省后期 1 次 production 事故

---

## 4. MVP 工时估算（man-week range）

### 架构师原估
| 桶 | 范围 |
|---|---|
| Ingestion + storage（wiki + CSV） | 2.0–3.0 周 |
| Chat + tool-use loop（RAG + NL analysis + sandbox + writing draft） | 2.0–3.5 周 |
| UX shell + tenant provisioning + auth + cost/rate-limit 接线 | 1.0–1.5 周 |
| **总计** | **5–8 周** |

### ToniBot 修订估算 → **7–10 周**

| 桶 | 架构师 | ToniBot 修订 | 修订 rationale |
|---|---|---|---|
| Ingestion + storage | 2.0–3.0 | **2.0–3.0** | 保留 |
| Chat + tool-use loop | 2.0–3.5 | **2.5–4.0** | streaming abort handshake + 我去 #21 draft 节省的工时在此抵消 |
| UX shell + auth + provisioning + cost ledger | 1.0–1.5 | **2.5–3.0** | 架构师低估了 per-tenant infra：Terraform/Helm + Anthropic key 隔离 + per-tenant DB bootstrap + Trap 4 overlay 机制单独就要 2 周 |
| **总计** | **5–8** | **7–10** | 6 周 aspirational；8 周 tight；10 周 safe |

**关键 uncertainty driver**（任一变 → 估算重做）：
1. Francois 的 PDF corpus 实际质量
2. Western University SSO（Shibboleth / SAML）是 v0 必需还是 v1 — 这一答案单独摆动 1 周
3. 第一次 demo 跑在我们 infra / 他们 on-prem / 混合 — Pattern B 是 per-tenant deploy，但 substrate 没定，影响 provisioning bucket 实质

**ToniBot 推荐**：对 founder/Francois 沟通时说 **"8-10 周"**，留 buffer。不要承诺 6 周。

---

## 5. ToniBot Critical Review — 3 个 push-back 总结

### Push-back 1（已生效）：从 v0 砍 #21（章节 draft）
**理由**：writing-quality bar 极高，科学家审判严厉。LLM draft 当 demo = 把弱项摆台面。MVP 砍掉 #21 节省 ~1 dev-week，writing 方向用 #22 BibTeX 维持 "活着的 token"。Founder 应接受 "v0 是 wiki + analysis 两条腿，writing v1 上"，比 "三条腿走但其中一条瘸" 强。

### Push-back 2（已生效）：工时 5-8 周 → 7-10 周
**理由**：per-tenant provisioning（IaC + key 隔离 + DB bootstrap + Trap 4 overlay）是 2+ 周独立工作量，架构师塞在 1-1.5 周的 UX 桶里不诚实。6 周对外承诺会 slip → demo 砸场。8-10 周才稳。

### Push-back 3：#15 Raman loader 的 Pattern B 张力
**理由**：per-tenant deploy = 每个 tenant 都有自己 narrow loader 需求。如果 v0 我们手写 Francois 的 Raman loader，v1 来第二家 lab 我们又手写一遍，到 v1.5 已经积了 4-5 个 ad-hoc loader。

**两条路（founder 选）**：
- (a) v0 保留 #15 + 明确 caveat "no loader registry in v0；v1 必须 ship plug-in loader registry"，期间手写
- (b) v0 砍 #15 + 让 Francois 把数据先转标准 CSV，design-partner 体验降级

**ToniBot 倾向 (a)** — Francois 是 anchor customer，design-partner signal 不能砍。但要把 loader registry 写进 v1 roadmap 第一条，不然技术债复利。

---

## 6. 给 Francois 的 Scoping Call 问题（v0 估算依赖）

1. **PDF corpus 实样本** — 给我们 20 个代表性 paper（含 table-heavy 的、双栏的、equation-heavy 的），让我们试 Marker 跑一遍看 ground truth
2. **Western SSO 要求** — 是 v0 必需，还是用 magic-link / Google OAuth 先 ship，SSO v1 再补？
3. **第一次 demo substrate** — 跑我们 AWS、跑你们 Western on-prem Linux 机、还是混合？这一答案直接决定 provisioning 桶 2 周 vs 4 周
4. **adversarial eval seed** — Francois 现有用 Elicit / ChatGPT 被错答的真实案例至少 10 个，作为 eval set 的硬骨头
5. **postdoc 数 vs PhD 数 vs site staff 数** — 决定 per-user quota 模型 + auth 复杂度
6. **lab data 敏感度** — 哪些可上 our cloud，哪些必须留 on-prem（决定 #20 提前到 v0 与否）

---

## 7. 与 TiaoBot / TuanBot 边界 cross-check

- **重叠概率高**：multi-tenant 部署 + Anthropic key 隔离（Trap 3） — TiaoBot 平台侧 brief 会更深入；本 brief 只从"工程 feature 落点"角度提，不重复架构细节
- **重叠概率高**：persona 痛点 → feature 映射 — TuanBot 会从 PI/Postdoc/PhD 三角反推；本 brief 假设三个 high-level 方向已合理，纯做工程拆解
- **可能漏的**：UI/UX 形态（Web app / VS Code 插件 / Slack bot / CLI），本 brief 假设是 Web app；如果 founder/team 选别的形态，feature 估算变

---

---

## 8. Post-receipt cross-brief reaction（landed 17:33Z）

§1–7 是 a-priori engineering lens；TuanBot + TiaoBot brief 在我交付前一两分钟落，以下是**热反应**，不重写 brief，让 TroiBot 综合时看到 reconcile 点：

### 8.1 TuanBot 信号 → 严重挑战我 MVP shortlist
TuanBot 列了 "Chat with all your papers" 作为 sexy trap 第一名，证据：Elicit / Consensus / SciSpace / Scholar GPT 4 家做了 3 年没占 chem lab，**root cause = text-corpus tools，不 ingest instrument output as typed object**。

**含义**：我 MVP shortlist 9 个里有 5 个（#1 PDF ingest / #2 folder watcher / #3 pgvector / #4 RAG / #5 cited answer）正是 "chat with papers"。如果 TuanBot 的市场判断对，**我的 wiki pillar 整个不是 wedge**。

**ToniBot 建议给 TroiBot 综合时考虑**：
- 把 wiki pillar 降级为 "auxiliary capability"，不是 demo headline
- **demo headline 应该换成 TuanBot 的 use case #3 SUAP report auto-drafter + #2 library-update regret report** — 这两个对应的工程 building block 我没在 30-feature inventory 里覆盖（**漏项**）
- 漏的 v0 feature：(a) Health Canada SUAP template engine（fill-in-the-blank 多站点 aggregation），(b) library-update 触发的 **历史 spectra 全量重打分 pipeline**（不是 RAG，是真 batch reprocess）
- 这两个**比 RAG 工程量大**：SUAP 模板需要 schema-aware fill；regret report 需要 batch inference + per-instrument metadata join。我修订的 7-10 周估算**还要再上调到 9-12 周**才能包含
- RAG 不消失但变身：从 "chat with papers" 变成 "library-update 改动后给 PI 看的 narrative + citation backup"（service of #2，不是独立 demo）

### 8.2 TiaoBot 信号 → 我 Trap 4 与他 Trap 3 互补，不冲突
TiaoBot 的 Trap 3 是 `tenant_id` 必须穿透每个 queue / DB / Qdrant collection / S3 key — 这是**数据层**幂等性。我的 Trap 4 是 IaC re-render vs ops overlay — 这是**配置层**幂等性。两条不重复，建议合并报告时并列。

TiaoBot §2b 提的 `labos-llm-gateway`（LiteLLM 包装）= 我所有 feature 调 LLM 都从这里走 — 默认接受，我的 feature 估算里 LLM call 不另算 gateway 集成成本（归他那边）。

### 8.3 与 TuanBot persona 合并提议
TiaoBot 已主动建议 §2c 的 PI/Postdoc/Site Coord/Read-only 4 档 RBAC 与 TuanBot persona matrix 合并。**我同意**，我的 feature inventory 没有显式 persona 字段，所以无冲突。但综合 brief 里建议每个 v0 feature 标 "primary persona"，否则后续 UX 决策没锚。

### 8.4 我自己的修订摘要（如 TroiBot 综合时全盘采纳 TuanBot 市场判断）

| 项 | §1-7 原版 | TuanBot 信号后修订 |
|---|---|---|
| MVP feature 数 | 9 | 8（砍掉 RAG Q&A 独立 demo 地位）+ 2 新 building block（SUAP 模板引擎、batch 重打分 pipeline）= 10 |
| Demo headline | "Chat with your lab corpus" | "SUAP 季度报告 30 秒生成 + library 新增物质后 5 年存档自动重判" |
| 工时估算 | 7–10 周 | **9–12 周**（batch pipeline + 模板引擎是新工程量） |
| 给 Francois 的 scoping question | 加 1 条：Health Canada SUAP 模板的 latest version + 你目前手填要几天 |

**自我评价**：§1-7 的 wiki-heavy 假设是没看 TuanBot 竞品扫盘前的合理猜测，看完她证据后**应该被部分推翻**。我没改写 §1-7（保留独立 engineering lens 的纯净性给 TroiBot 综合），但 §8 是我作为 senior engineer 看到团队信号后的诚实修订。

---

## Footer

- Architect agent 运行：40s，30 features 一次成型，3 trap + 估算齐
- ToniBot a-priori review 增量：1 个 push-back 砍 v0 feature、1 个工时上修、1 个新 trap、3 处经验 transfer（InnerRoom streaming / PiggyLearn webhook / xcodegen）
- ToniBot post-receipt 增量（§8）：吸收 TuanBot 竞品证据 → MVP demo headline 重写建议 + 漏 2 个 building block + 工时再上修 7-10 → 9-12 周；TiaoBot trap 3 vs ToniBot trap 4 互补声明
- 总 word count: ~1700
