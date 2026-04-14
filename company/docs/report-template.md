# 完成报告模板 v1.0

> 2026-04-13 retro 团队全票通过 · 员工报完成必须套用此模板 · 缺项 TroiBot 拒收

---

## 使用规则

- **所有** IN_REVIEW / DONE 状态切换，Assignee 在 #company 发报告时必须包含全部 5 节
- 缺任何一节 → TroiBot 直接拒收，不走 review
- TroiBot 收到后**必须** `git diff <commit>` 独立核查，不靠口头承诺

---

## 模板

```
## [任务 ID] 完成报告

### 1. Commit
- SHA: <完整 hash 或 7 位前缀>
- Branch: <branch-name>
- Message: <first line of commit message>

### 2. Files Changed
- path/to/File1.swift (+42 -17)
- path/to/File2.swift (+8 -0)
- ...

### 3. 测试证据
命令：
    xcodebuild test -scheme InnerRoom ...

输出尾巴（粘贴原文，不要转述）：
    Test Suite 'All tests' passed at 2026-04-13 12:34:56
        Executed 70 tests, with 0 failures (0 unexpected)

或附 screenshot / log 文件（如 UI 改动不好跑 test）

### 4. Scope Inventory 对照
（派活人给的清单逐项对照；没有 Scope Inventory 的任务可省略此节）

| 清单项 | 决定 | 实际处理 |
|---|---|---|
| SanctuaryView.swift:234 | 改 | ✅ commit 包含 |
| ConfessionView.swift:189 | 改 | ✅ commit 包含 |
| IntercessionView.swift:56 | 不改（业务逻辑不同）| ⏭️ 未动 |

### 5. 已知残留风险 / 待办
- （若无写 "无"）
- 例如："P4-8 键盘遮挡在 iPhone SE 上可能还有 2px 重叠，等真机验证"
```

---

## 反面例子（拒收）

> "我改完了，测试都过了，应该没问题。"

**为什么拒收**：没 commit hash、没文件清单、没测试输出、没 scope 对照。
"应该没问题" = 不合格。

## 正面例子

> 见 2026-04-11 Task R/S/T 完成报告格式（并行流水线 20-30 分钟闭环那几次）
