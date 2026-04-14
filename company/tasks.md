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
| P3-20 | Face ID改免费功能 | TuanBot | TiaoBot | TODO | p3-sanctuary-security | — | SanctuaryView.swift, ConfessionView.swift | 2026-04-06 |
| P3-21 | 首次祷告不限次数 | TuanBot | TiaoBot | DONE | p3-sanctuary-security | 2ceff71 | SanctuaryView.swift | 2026-04-06 |
| P3-22 | 赦免动画结束加CTA | TuanBot | TiaoBot | DONE | p3-sanctuary-security | 2ceff71 | SanctuaryView.swift | 2026-04-06 |
| P3-23 | ~~全局Environment重构~~ | — | — | CANCELLED | — | — | 老板确认取消，风险高收益低 |
| P3-24 | ~~Keychain→UserDefaults迁移~~ | — | — | CANCELLED | — | — | Keychain 防重装重置，保留 |
| P3-25 | 付费墙加竞品对比文案 | ToniBot | TiaoBot | DONE | p3-paywall-privacy | aa039fb | PaywallView.swift | 2026-04-06 |

## Phase 4: P4 — 真机测试反馈修复（2026-04-07 老板手动测试）

| ID | Task | Assignee | Reviewer | Status | Branch | PR/Commit | Files | Updated |
|----|------|----------|----------|--------|--------|-----------|-------|---------|
| P4-1 | Onboarding AI Demo 响应慢——预热模型 + 流式优化 | ToniBot | TiaoBot | IN_REVIEW | p4-onboarding | cb7c65f+5f9d15a | OnboardingView.swift, LLMService.swift | 2026-04-07 |
| P4-2 | Onboarding AI Demo 必须用用户当前语言回复 | ToniBot | TiaoBot | IN_REVIEW | p4-onboarding | 0d24d15+682b060 | OnboardingView.swift, OnboardingDemoLanguageTests.swift | 2026-04-07 |
| P4-3 | Onboarding AI Demo 输入框 pre-populate 多语言示例 | ToniBot | TiaoBot | IN_REVIEW | p4-onboarding | 0d24d15+682b060 | OnboardingView.swift, 7x Localizable.strings | 2026-04-07 |
| P4-4 | 第 5 页按钮延迟 2.5s → 1s | ToniBot | TiaoBot | IN_REVIEW | p4-onboarding | cb5e612+6d7b516 | OnboardingView.swift, OnboardingDelayTests.swift | 2026-04-07 |
| P4-5 | **【核心 Bug】** 暂停退出再进入会重置消息计数（应保留会话状态） | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | c0acec0+efa25c5 | PausedConversationManager.swift, SanctuaryView.swift, PausedConversationStateTests.swift | 2026-04-07 |
| P4-6 | **【Bug】** 首次祷告显示 "999 of 5 free messages" 乱码——改为 "Unlimited" 或隐藏 | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | 33b5c0d+53275fb | SanctuaryView.swift, FreeMessageFooterTests.swift | 2026-04-07 |
| P4-7 | 第 8 次祷告弹付费墙时无解释——加 "You've used all 7 free prayer sessions" 提示 | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | 4d3ac1e+6a84da7 | SanctuaryView.swift, PaywallView.swift, Localizable.strings | 2026-04-07 |
| P4-8 | **【UI Bug】** 祷告室键盘弹出后聊天记录被遮挡（layout 问题） | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | a449cf5 (无单测，待真机) | SanctuaryView.swift, ConfessionView.swift | 2026-04-07 |
| P4-9 | 切换祷告类型时输入框未清空——应清空 draft text | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | b48f623+33b02c4 | SanctuaryView.swift, DraftTextClearingTests.swift | 2026-04-07 |
| P4-10 | **【Bug】** 忏悔赦免后转化弹窗（P3-22）实际未触发——回归测试 | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | d96fa22+63c9193 | ConfessionView.swift, SanctuaryViewModel.swift, ConfessionAftermathTests.swift | 2026-04-07 |
| P4-11 | 代祷（Intercession）prompt 不吸引人——重写让对话更有粘性 | TiaoBot | TuanBot | IN_REVIEW | p4-prompts | 48c1c82+cd92b8c | en.lproj/Localizable.strings, PrayerSystemPromptTests.swift (15 tests) | 2026-04-07 |
| P4-12 | 模型加载完成后给清晰可见信号（不只是隐藏 loading） | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | 591e8dc+9db46de | SanctuaryView.swift, LLMService.swift | 2026-04-08 |
| P4-13 | **【流程漏洞】** 补 InnerRoomTests target + RevenueCat SPM（之前 yml 漏） | TuanBot | TiaoBot | IN_REVIEW | p4-sanctuary | 824e060 | App/project.yml | 2026-04-07 |
