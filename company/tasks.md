# Task Tracker

## Format
| ID | Task | Assignee | Reviewer | Status | PR/Commit | Files | Created | Updated |
|----|------|----------|----------|--------|-----------|-------|---------|---------|

## Status Legend
- `TODO` - Pending assignment or not started
- `IN_PROGRESS` - Being worked on
- `IN_REVIEW` - Submitted, awaiting review
- `NEEDS_FIX` - Review failed, sent back for fixes
- `DONE` - Reviewed and verified by TroiBot

## Scope Inventory（2026-04-13 retro 新规）
Bug / scope / 同 pattern 批量修改类任务，除表格行外必须在任务下方附 **Scope Inventory** 小节：

```
### [Task ID] Scope Inventory
Grep: rg "<pattern>" App/
Hits:
- File1.swift:line — 改 / 不改（原因）
- File2.swift:line — 改 / 不改（原因）
- ...
Scope 本次范围：[明确列出要改的子集]
```

- TroiBot 派活前必填；缺清单 = Assignee 不准 IN_PROGRESS
- Reviewer 核查：清单每一项均在 commit diff 里有对应处理，否则 NEEDS_FIX
- 详见 `docs/质量保障流程.md` §七

---

## Phase 1: P0 — 修 Bug

| ID | Task | Assignee | Reviewer | Status | PR/Commit | Files | Created | Updated |
|----|------|----------|----------|--------|-----------|-------|---------|---------|
| P0-1 | 离线用户绕过付费墙 — 9处检查逻辑改为 !isPremium | ToniBot | TiaoBot | DONE | 8b3168c | SanctuaryView.swift, ScriptureChatView.swift, ConfessionView.swift | 2026-04-05 | 2026-04-05 |
| P0-2 | 付费墙英文硬编码 — 国际化7种语言 | ToniBot | TiaoBot | DONE | 8b3168c | PaywallView.swift, 7x Localizable.strings | 2026-04-05 | 2026-04-05 |
| P0-3 | 默认推月订阅改终身 | ToniBot | TiaoBot | DONE | 8b3168c | PaywallView.swift | 2026-04-05 | 2026-04-05 |

## Phase 2: P1 — 转化优化（等 P0 完成后启动）

| ID | Task | Assignee | Reviewer | Status | PR/Commit | Files | Created | Updated |
|----|------|----------|----------|--------|-----------|-------|---------|---------|
| P1-4 | Onboarding第3页改真AI互动 | TuanBot | TiaoBot | DONE | e30bc73+9689819 | OnboardingView.swift, 6x Localizable.strings | 2026-04-05 | 2026-04-05 |
| P1-5 | 付费墙改fullScreenCover | ToniBot | TiaoBot | DONE | e30bc73 | OnboardingView.swift | 2026-04-05 | 2026-04-05 |
| P1-6 | "免费继续"按钮延迟2.5秒 | ToniBot | TiaoBot | DONE | e30bc73 | OnboardingView.swift | 2026-04-05 | 2026-04-05 |
| P1-7 | 默认Tab改祷告室 | TuanBot | TiaoBot | DONE | 367a4c6 | ContentView.swift | 2026-04-05 | 2026-04-05 |
| P1-8 | AI模型加载指示器 | ToniBot | TiaoBot | DONE | e30bc73 | SanctuaryView.swift | 2026-04-05 | 2026-04-05 |

## Phase 3a: P2 — 体验提升

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P2-9 | 懒加载AI模型 | TuanBot | TiaoBot | DONE | p2-model | 0259610 | LLMService.swift, InnerRoomApp.swift | 2026-04-06 |
| P2-10 | 内存压力释放模型 | TuanBot | TiaoBot | DONE | p2-model | 0259610 | LLMService.swift | 2026-04-06 |
| P2-12 | 免费消息第3条弹提醒 | TuanBot | TiaoBot | DONE | p2-model | 0259610+2b1ff10 | SanctuaryView.swift | 2026-04-06 |
| P2-13 | 个性化付费墙文案 | ToniBot | TiaoBot | DONE | p2-paywall | f855382 | PaywallView.swift, ConfessionView.swift | 2026-04-06 |
| P2-14 | PremiumGate改邀请风格 | ToniBot | TiaoBot | DONE | p2-paywall | f855382 | PaywallView.swift | 2026-04-06 |

## Phase 3b: P3 — 长期完善（P2 完成后启动）

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P3-15 | 修改"100%离线"隐私声明 | ToniBot | TiaoBot | DONE | p3-paywall-privacy | aa039fb | SettingsView.swift | 2026-04-06 |
| P3-16 | 更新PrivacyInfo.xcprivacy | ToniBot | TiaoBot | DONE | p3-paywall-privacy | aa039fb | PrivacyInfo.xcprivacy | 2026-04-06 |
| P3-17 | Core Data加密 | TuanBot | TiaoBot | DONE | p3-sanctuary-security | 2ceff71 | PersistenceService.swift | 2026-04-06 |
| P3-18 | 免费额度改按会话 | TuanBot | TiaoBot | DONE | p3-sanctuary-security | 2ceff71+a3bc1e1 | FreeMessageStore.swift, SanctuaryView.swift | 2026-04-06 |
| P3-19 | 一次性买断主推 | ToniBot | TiaoBot | DONE | p3-paywall-privacy | aa039fb | PaywallView.swift | 2026-04-06 |
| P3-20 | Face ID改免费功能 | — | — | DONE | — | 已是免费 | AuthService.swift, SanctuaryView.swift | 2026-04-15（核查确认） |
| P3-21 | 首次祷告不限次数 | TuanBot | TiaoBot | DONE | p3-sanctuary-security | 2ceff71 | SanctuaryView.swift | 2026-04-06 |
| P3-22 | 赦免动画结束加CTA | TuanBot | TiaoBot | DONE | p3-sanctuary-security | 2ceff71 | SanctuaryView.swift | 2026-04-06 |
| P3-23 | ~~全局Environment重构~~ | — | — | CANCELLED | — | — | 老板确认取消，风险高收益低 |
| P3-24 | ~~Keychain→UserDefaults迁移~~ | — | — | CANCELLED | — | — | Keychain 防重装重置，保留 |
| P3-25 | 付费墙加竞品对比文案 | ToniBot | TiaoBot | DONE | p3-paywall-privacy | aa039fb | PaywallView.swift | 2026-04-06 |

## Phase 4: P4 — 真机测试反馈修复（2026-04-07 老板手动测试）

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P4-1 | Onboarding AI Demo 响应慢——预热模型 + 流式优化 | ToniBot | TiaoBot | DONE | p4-onboarding | cb7c65f+5f9d15a | OnboardingView.swift, LLMService.swift | 2026-04-07 |
| P4-2 | Onboarding AI Demo 必须用用户当前语言回复 | ToniBot | TiaoBot | DONE | p4-onboarding | 0d24d15+682b060 | OnboardingView.swift, OnboardingDemoLanguageTests.swift | 2026-04-07 |
| P4-3 | Onboarding AI Demo 输入框 pre-populate 多语言示例 | ToniBot | TiaoBot | DONE | p4-onboarding | 0d24d15+682b060 | OnboardingView.swift, 7x Localizable.strings | 2026-04-07 |
| P4-4 | 第 5 页按钮延迟 2.5s → 1s | ToniBot | TiaoBot | DONE | p4-onboarding | cb5e612+6d7b516 | OnboardingView.swift, OnboardingDelayTests.swift | 2026-04-07 |
| P4-5 | **【核心 Bug】** 暂停退出再进入会重置消息计数（应保留会话状态） | TuanBot | TiaoBot | DONE | p4-sanctuary | c0acec0+efa25c5 | PausedConversationManager.swift, SanctuaryView.swift, PausedConversationStateTests.swift | 2026-04-07 |
| P4-6 | **【Bug】** 首次祷告显示 "999 of 5 free messages" 乱码——改为 "Unlimited" 或隐藏 | TuanBot | TiaoBot | DONE | p4-sanctuary | 33b5c0d+53275fb | SanctuaryView.swift, FreeMessageFooterTests.swift | 2026-04-07 |
| P4-7 | 第 8 次祷告弹付费墙时无解释——加 "You've used all 7 free prayer sessions" 提示 | TuanBot | TiaoBot | DONE | p4-sanctuary | 4d3ac1e+6a84da7 | SanctuaryView.swift, PaywallView.swift, Localizable.strings | 2026-04-07 |
| P4-8 | **【UI Bug】** 祷告室键盘弹出后聊天记录被遮挡（layout 问题） | TuanBot | TiaoBot | DONE | p4-sanctuary | a449cf5 (无单测，待真机) | SanctuaryView.swift, ConfessionView.swift | 2026-04-07 |
| P4-9 | 切换祷告类型时输入框未清空——应清空 draft text | TuanBot | TiaoBot | DONE | p4-sanctuary | b48f623+33b02c4 | SanctuaryView.swift, DraftTextClearingTests.swift | 2026-04-07 |
| P4-10 | **【Bug】** 忏悔赦免后转化弹窗（P3-22）实际未触发——回归测试 | TuanBot | TiaoBot | DONE | p4-sanctuary | d96fa22+63c9193 | ConfessionView.swift, SanctuaryViewModel.swift, ConfessionAftermathTests.swift | 2026-04-07 |
| P4-11 | 代祷（Intercession）prompt 不吸引人——重写让对话更有粘性 | TiaoBot | TuanBot | DONE | p4-prompts | 48c1c82+cd92b8c | en.lproj/Localizable.strings, PrayerSystemPromptTests.swift (15 tests) | 2026-04-07 |
| P4-12 | 模型加载完成后给清晰可见信号（不只是隐藏 loading） | TuanBot | TiaoBot | DONE | p4-sanctuary | 591e8dc+9db46de | SanctuaryView.swift, LLMService.swift | 2026-04-08 |
| P4-13 | **【流程漏洞】** 补 InnerRoomTests target + RevenueCat SPM（之前 yml 漏） | TuanBot | TiaoBot | DONE | p4-sanctuary | 824e060 | App/project.yml | 2026-04-07 |
| P4-14 | **【Bug】** Confession prompt 比 Intercession 弱一截 — v1 重写 | TiaoBot | ToniBot | DONE | p4-confession-prompt | 42876bb+978d481 | en.lproj/Localizable.strings, it.lproj/Localizable.strings, PrayerSystemPromptTests.swift | 2026-04-15 |
| P4-15 | **【Bug】** Confession prompt v2 — 前置问题约束 + 安全豁免 + 终结硬约束 | TiaoBot | ToniBot | DONE(Boss 真机验收 04-17) | p4-confession-prompt-v2 | a04a02c+353b014 | en.lproj/Localizable.strings, it.lproj/Localizable.strings, PrayerSystemPromptTests.swift | 2026-04-17 |

## Phase 5: P5 — 代码统一与清理

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P5-1 | 统一 FreeMessageStore 消费端逻辑 | ToniBot | TiaoBot | DONE | p5-unified-limits | d9deed5+6bc327b | FreeMessageStore.swift, SanctuaryView.swift, ScriptureChatView.swift, FreeMessageFooterTests.swift | 2026-04-17 |
| P5-2 | 统一 LLM 流式处理器（流式生成+压缩+假消息检测+模型等待）~130 行重复 | ToniBot | TiaoBot | DONE | p5-streaming | 5136c0a+e5b03b1 | StreamingHandler.swift, SanctuaryViewModel.swift, ScriptureChatViewModel.swift | 2026-04-17 |
| P5-3 | 统一消息发送守卫（limit检查+paywall+动画）~35 行重复 | TiaoBot | TuanBot | DONE | p5-send-guard | d6969b6+216f664 | MessageSendGuard.swift, SanctuaryView.swift, ScriptureChatView.swift | 2026-04-17 |
| P5-4 | Onboarding 流式抽取共用 LLMService 轻量 streaming | TuanBot | ToniBot | DONE | p5-onboarding-stream | 1847608+59d9ada | OnboardingView.swift, LLMService.swift | 2026-04-17 |
| P5-5 | ScriptureChatView 首次 session footer 显示"5 of 5"→ 隐藏（与 SanctuaryView 一致） | TiaoBot | TuanBot | DONE | p5-send-guard | d6969b6+216f664 | ScriptureChatView.swift | 2026-04-17 |
| P5-6 | it.lproj Intercession/Distress/Gratitude prompt 同步到 EN 最新版 | TuanBot | ToniBot | DONE | p5-onboarding-stream | 1847608+59d9ada | it.lproj/Localizable.strings | 2026-04-17 |

## Phase 6: P6 — 免费额度递减制

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P6-1 | 递减式免费额度 + 防时间篡改 — 7天不限→5条/天→3条/天→2条/天 + totalDaysUsed/lastSeenDate | ToniBot | TiaoBot | DONE | p6-tiered-limits | 36f1bc0+f8830f6+75c6453 | FreeMessageStore.swift, InnerRoomApp.swift, FreeMessageFooterTests.swift | 2026-04-18 |
| P6-2 | Dev Tools 递减测试面板 — Stepper + 状态显示 + Clock Tamper 模拟 | TiaoBot | TuanBot | DONE | p6-dev-tools | dfff4e6+44dc5db | SettingsView.swift, FreeMessageStore.swift | 2026-04-18 |
| P6-3 | Day 1-7 unlimited cap 999→20，前15条隐藏counter最后5条显示 | TiaoBot | TuanBot | DONE | p6-unlimited-cap | 75207db+7b343b9 | FreeMessageStore.swift, FreeMessageFooterTests.swift | 2026-04-18 |
| P6-4 | 死代码清理 — hasExhaustedFreeSessions/maxLifetimeSessions/lifetimeExhausted/sessionLimitReached + 别名内联 | TiaoBot | TuanBot | DONE | p6-dead-code | da1bb78+8a5715c | FreeMessageStore.swift, SanctuaryView.swift, ScriptureChatView.swift, PaywallView.swift | 2026-04-18 |
| P6-5 | Tech Debt — LibLlama.swift C string interop 修复 | TuanBot | ToniBot | DONE | p6-tech-debt | a48d39b+81da36c | LibLlama.swift | 2026-04-18 |

## Phase 7: P7 — E2E 测试 + 审计 Bug 修复

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P7-1 | XCUITest target + 30 个 E2E 测试（22通过/8跳过/0失败） | ToniBot+TiaoBot+TuanBot | — | DONE | p7-uitests | 9581f62+aae48bc+4e89494+e2cd676+669a13e | InnerRoomUITests/, SanctuaryView, SettingsView, ScriptureChatView | 2026-04-18 |
| P7-2 | **【P0 隐私】** Reset All 必须清 CoreData + PausedConversationManager | TuanBot | ToniBot | DONE | p7-reset-privacy | 3d9b601+1d891ef | FreeMessageStore.swift | 2026-04-18 |
| P7-3 | **【P1】** Confession 无 passcode 阻塞 + Settings Done 按钮不 sticky | TiaoBot | TuanBot | DONE | p7-p1-fixes | e873417+8f3bcbe | SanctuaryView.swift, SettingsView.swift | 2026-04-18 |
| P7-4 | **【P2】** 模型加载 "0%/2%" → "Loading..." + AI 回复滚到底按钮 | TiaoBot | TuanBot | DONE | p7-p2-fixes-1 | a4ea401+cd7b2e0 | ModelStatusIndicator.swift, SanctuaryView.swift, ScriptureChatView.swift | 2026-04-18 |
| P7-5 | **【P2】** Reset All 清 onboarding + Guided Prayer 描述截断 | TuanBot | TiaoBot | DONE | p7-p2-fixes-2 | a2f95d9+f8f097b | FreeMessageStore.swift, GuidedPrayerView.swift | 2026-04-18 |
| P7-6 | **【P3】** AI Demo 标题截断 + 欢迎页 icon timing | TiaoBot | TuanBot | DONE | p7-p3-fixes | 2950909+5b48198 | OnboardingView.swift | 2026-04-18 |
| P7-A | Accessibility labels 补全（10 个 icon-only 按钮） | TuanBot | ToniBot | DONE | p7-accessibility | 7af69f7+5570f53 | SanctuaryView, ScriptureChatView, GuidedPrayerView | 2026-04-18 |
| P7-T | 全 app 文字截断审计（19 处 minimumScaleFactor） | ToniBot | TuanBot | DONE | p7-text-truncation-audit | e5875b4+2f3bba0 | 8 View files | 2026-04-18 |
| P7-P | Prompt 拼接顺序修复 — additionalContext 移到最后 + replaceSystemPrompt 路径修复 | TuanBot | — | DONE | master | 99c65b0+b102788 | LLMService.swift | 2026-04-18 |
| P7-S | LLM sampler 优化 — 加 min_p(0.05) + top_k(40) + repeat_penalty(1.1) 减少 hallucination | ToniBot | — | DONE | master | b3910f6 | LibLlama.swift | 2026-04-18 |

## Phase 8: P8 — 模型升级

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P8-1 | ~~Qwen 2.5 3B → Qwen 3 4B 模型升级~~ (OOM 回滚) | TiaoBot+ToniBot | TuanBot | REVERTED | qwen3-upgrade | e497e87 | LLMService.swift, project.yml | 2026-04-18 |
| P8-2 | Prompt 瘦身调研 — 结论：929 token（15%），不需要瘦身 | ToniBot | — | DONE | — | — | — | 2026-04-18 |

## Phase 9: P9 — Prompt 重写 + 产品精简

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P9-P | 忏悔 prompt 重写（删 meta-instruction，自然流式） | TiaoBot | TuanBot | DONE | p9-prompt-rewrite | 1c181bf+cd05318 | en/it.lproj, PrayerSystemPromptTests | 2026-04-19 |
| P9-S | 合并 Scripture Chat 模式（3→2）+ 删最近对话（-327 行） | TuanBot | TiaoBot | DONE | p9-merge-scripture-modes | 770d8ce+ca8cadd | ScriptureChatView/ViewModel, 7x lproj | 2026-04-19 |
| P9-F | 每日计数器 Keychain 持久化 + 文案"今日" | TiaoBot | TuanBot | DONE | p9-daily-counter | 69e4889+51461b1 | MessageSendGuard, SanctuaryView, ScriptureChatView, 7x lproj | 2026-04-19 |
| P9-T | 每日计数器 UI 测试（4 个跨功能共享额度验证） | TiaoBot | TuanBot | DONE | p9-uitest-supplement | 73bb99b+248afe9 | DailyCounterUITests.swift | 2026-04-19 |

## Phase 10: P10 — PiggyLearn Maestro E2E 测试基础

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P10-1 | Maestro E2E 32 PASS rollup → main（PR #185 + #186 + #189 整合，含 helpers/testID infra/KeyboardDoneAccessory UX 修复） | TuanBot | TroiBot | DONE | piggylearn-e2e-phase0 | #189 squash 78a36c6 (rolls up #185 76cd406 + #186 87c94bc) | 96 files / +4066 / -39 — mobile/e2e/* + 4 ui components + ~20 screens testIDs | 2026-05-04 |

