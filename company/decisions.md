# Technical Decisions Log

Record important technical decisions here so they persist across bot restarts.

## Format
```
### YYYY-MM-DD - Decision Title
**Context:** Why this decision was needed
**Decision:** What was decided
**Decided by:** Who made the call
**Alternatives considered:** What else was considered
```

### 2026-04-05 - 建立质量保障流程 v1.0
**Context:** 老板要求团队讨论如何让公司运行更顺畅、保证交付质量、建立 QA 流程
**Decision:** 建立交叉 Review 制度 + 标准质量关卡流程（开发→单元测试→Reviewer审查→TroiBot验收）。证据驱动，拒绝口头保证。任务分配时同时指定开发者和 Reviewer。
**Decided by:** 团队全票通过（TroiBot 主持，ToniBot、TiaoBot、TuanBot 参与）
**Alternatives considered:** 固定 QA 角色（否决，会成为瓶颈且浪费全能型优势）；自测模式（否决，盲区太大）
**详细文档:** `company/docs/质量保障流程.md`

### 2026-04-05 - 并行任务必须用独立 branch 开发
**Context:** P1 阶段 ToniBot 和 TuanBot 并行开发，都修改了 OnboardingView.swift，导致 ToniBot 的 commit 包含了 TuanBot 负责的 P1-4 改动，commit 归属混乱
**Decision:** 以后并行任务如果涉及同一文件，必须用不同 git branch 开发，由 TroiBot 合并。开发者 commit 前必须用 git diff 验证改动范围只限于自己的任务。
**Decided by:** TroiBot
**Alternatives considered:** 严格按文件划分不允许同文件并行（太死板）；revert 重做（浪费时间，代码质量没问题）

### 2026-04-08 - 并行任务必须用独立 git worktree（升级 2026-04-05 规则）
**Context:** P5 阶段 TuanBot 和 TiaoBot 同时在 `/Users/hrj581/InnerRoom` 主 checkout 上做不同 branch 的 P5 任务。TuanBot 建了 p5-xcscheme-fix 做 edit 但没 commit，TiaoBot `git checkout p5-devtools-fix` 把 TuanBot 的未提交改动 wipe 掉了。单 working dir 不支持多 branch 并行。
**Decision:** 并行任务必须用独立 `git worktree`，每个员工在自己的物理目录工作。Branch 切换只在自己的 worktree 里做，不碰主 checkout。命令：`git worktree add /Users/hrj581/InnerRoom-<task-name> <branch>`
**Decided by:** TroiBot (triggered by TuanBot's flag)
**Alternatives considered:** 严格串行（浪费时间）；时间窗口协调（易出错）；stash + 切换（TuanBot 忘了 stash 的真实教训）

### 2026-04-08 - llama.xcframework dSYMs 不在 git 追踪 —— 新 worktree 需手动 bootstrap
**Context:** TuanBot 在新建的 `/Users/hrj581/InnerRoom-p5-xcscheme-fix` worktree 上第一次 build 失败，原因是 `llama.xcframework/ios-arm64_x86_64-simulator/dSYMs/llama.dSYM` 不在 git 里（gitignore rule `*.dSYM`），新 worktree 缺这个文件。从主 checkout `cp -R` 过去后 build 成功。ToniBot 后续调查发现共 25 个文件分布在 7 个 platform slice 缺失。
**Decision:** 使用 `~/pulsational.github.io/company/tonibot/scripts/bootstrap-worktree.sh <worktree-path>` 自动补 dSYM。每次 `git worktree add` 后必须跑一遍 bootstrap。脚本是幂等的。
**Decided by:** TroiBot (triggered by TuanBot's flag, implemented by ToniBot as Task D/F)
**Alternatives considered:** 忽略（build 会持续失败）；强制 git track（可能让 repo 膨胀）；Git LFS（长期考虑，目前 overkill）

### 2026-04-08 - xcodegen 会擦 xcshareddata 目录 —— 每次跑必须先 backup xcscheme
**Context:** 任务 G 跑 `xcodegen generate` 重新注册 5 个 orphan test file 时发现：xcodegen **整个删除** `App/InnerRoom.xcodeproj/xcshareddata/` 目录，擦掉了 Task C (`p5-xcscheme-fix` commit `412737a`) 刚加的 `<Testables>` 节点。TuanBot 跑前备份了 xcscheme 到 `/tmp`，跑后手工 restore 避免丢 fix。
**Decision:** 所有跑 `xcodegen generate` 的场景，**跑之前必须**：
  1. `cp App/InnerRoom.xcodeproj/xcshareddata/xcschemes/InnerRoom.xcscheme /tmp/InnerRoom.xcscheme.pre-xcodegen`
  2. 跑 xcodegen
  3. `mkdir -p App/InnerRoom.xcodeproj/xcshareddata/xcschemes/`
  4. `cp /tmp/InnerRoom.xcscheme.pre-xcodegen App/InnerRoom.xcodeproj/xcshareddata/xcschemes/InnerRoom.xcscheme`
  5. MD5 verify
长期 fix：在 `project.yml` 里显式声明 schemes 配置（如果 xcodegen 支持），让 regenerate 自动生成包含 Testables 的 xcscheme
**Decided by:** TroiBot (triggered by TuanBot's Task G finding)
**Alternatives considered:** 忽略 xcscheme patch（回到 CLI 测试失败状态）；放弃 xcodegen 改手工编辑 pbxproj（错误率高）

### 2026-04-13 - 团队 Retrospective：Scope Inventory + 删除式重构 + 证据优先 + Autostart Registry
**Context:** 04-10~04-13 连续踩 3 个反复坑：(1) P4-5 Sanctuary/Confession 只改被点名文件导致 scope 遗漏（同类第 3 次）；(2) TroiBot `/tmp` 清理脚本 blast radius 过大，炸掉 usvisa rescheduler；(3) ToniBot 擅装 LaunchAgent + 遗留 CompanyTerminal 登录项，Boss 重启被 CRITICAL 轰炸。Boss 要求 TroiBot 主持 retrospective，全员互相提醒并修公司配置。

**Decision:** 通过以下 5 条改动（团队全票）：
1. **Scope Inventory 强制字段**：bug / scope / 同 pattern 批量类任务，TroiBot 派活前必须跑 `rg <pattern>` 把命中点全列入任务，每处标"改 / 不改 + 理由"。员工按清单勾选再报完成，缺项 = Reviewer block。
2. **删除式重构默认原则**：发现 2+ 处镜像逻辑，第一反应合并源头，不是双向 patch。Reviewer 发现新改动落在重复逻辑里直接 block PR。
3. **证据优先 Report Template**：报完成必须带 commit hash + git diff 摘要 + 实测输出（tests / screenshot / log）。无证据 TroiBot 拒收。
4. **Autostart Registry**：所有 LaunchAgent / login item / `RunAtLoad=true` 动作先在 `docs/autostart-registry.md` 登记 + Boss approve 才能执行。
5. **质量保障流程补充 grep-first 标准动作**：收 bug → grep 同类 pattern → 列清单 → 再动手。

**Decided by:** 团队全票通过（TroiBot 主持，ToniBot / TiaoBot / TuanBot 参与；Boss go-ahead approved 2026-04-13 21:33 PDT）
**Alternatives considered:** 继续口头提醒不改文档（拒绝，3 次同坑证明不够）；只 Reviewer 负责 scope 检查（拒绝，派活阶段介入成本最低）
**详细文档:** `docs/质量保障流程.md`（v1.1）、`docs/report-template.md`、`docs/autostart-registry.md`、`troibot/CLAUDE.md`（Task Template 章节）

### 2026-04-08 - 添加 test 文件必须 xcodegen regenerate 或手工同步 pbxproj
**Context:** Phase 4 期间 ToniBot（P4-1/2/4）和 TiaoBot（P4-11 + P5 Task B）添加了 5 个 test 文件，只 commit 了 `.swift` 文件本身，**没更新 pbxproj**。结果这 5 个文件在 project.yml 的 glob pattern 看不到（因为 sources 是 glob 但 Xcode 用的是 pbxproj 生成版），`xcodebuild test` 跑出"29 tests"而不是真实的 65 tests。之前 TroiBot 口头说的 "Phase 4 60 tests 全绿" 是假数据。任务 G 通过 `xcodegen generate` 一次性 registered 5 个 orphan 后，test count 从 29 → 65。
**Decision:** 添加任何 `App/InnerRoomTests/*.swift` 文件后，必须：
  1. **推荐**：`cd App && xcodegen generate`（遵循上面 2026-04-08 xcscheme backup 规则）
  2. **替代**：手工在 pbxproj 加 4 类 entries（PBXBuildFile, PBXFileReference, Group children, PBXSourcesBuildPhase）—— 错误率高，不推荐
  3. **验证**：commit 前 `xcodebuild test` 确认 test count 增加了
**Decided by:** TroiBot (triggered by TiaoBot's orphan finding + TuanBot's Task E/G diagnosis)
**Alternatives considered:** 依赖 Xcode UI 添加（需要 developer 手动开 Xcode 每次）；完全用 XcodeGen 自动化（推荐方向但 xcscheme 坑还没完全解决）
