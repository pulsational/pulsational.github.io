# 自启项登记表 Autostart Registry v1.0

> 2026-04-13 retro 团队全票通过 · 任何自动启动机制动手前必须登记 + Boss approve
> 动机：ToniBot 擅装 LaunchAgent + 残留 CompanyTerminal 登录项导致 Boss 重启被 CRITICAL 轰炸

---

## 登记范围（以下任一必登）

- `~/Library/LaunchAgents/*.plist`（launchd user agent）
- `/Library/LaunchDaemons/*.plist`（system daemon，基本别碰）
- `RunAtLoad=true` / `KeepAlive=true` 任一设置
- System Settings → General → Login Items 里的任何条目
- `osascript ... login items add`
- `brew services start <x>`（持久化的那种）
- macOS Helper app（包含 `LSUIElement=true` 且在 login items 里注册）
- cron / launchd 定时任务（含 `StartInterval` / `StartCalendarInterval`）

---

## 流程

1. **动手前**：填写下方"当前登记"表格 + 在 #company @Boss 说明目的和触发条件
2. **等 Boss approve**（明确文字 "ok" / "go ahead"，不是沉默）
3. approve 后再执行 `launchctl load` / 添加登录项 / 等
4. **无登记 = 无权执行**
5. Reviewer / TroiBot 发现未登记的自启项 → 立即 `launchctl unload` 停用 + 上报 Boss

---

## 当前登记（2026-04-13 初始盘点）

| 文件 / 条目 | 类型 | 属主 | 用途 | RunAtLoad | Boss approved | 备注 |
|---|---|---|---|---|---|---|
| `~/Library/LaunchAgents/com.company.bots.plist.disabled` | LaunchAgent | 旧 company_start | 启动 Discord 三人组 | **disabled** | ❌ 已停用 | 04-10 事故后 Boss 要求手动启动，保留 `.disabled` 文件仅为历史备份；不要 rename 回 `.plist` |
| Login Item: Dropbox | System login item | macOS app | Dropbox 同步 | 是 | ✅ 系统默认，Boss 保留 | 无需公司层面管理 |

---

## 历史已移除（审计留痕）

| 文件 / 条目 | 移除日期 | 移除原因 |
|---|---|---|
| `com.tonibot.usvisa-*.plist` (×2) | 2026-04-10 | ToniBot 未登记擅装，Boss 重启被 CRITICAL 轰炸；违反本登记制度（制度前试点） |
| `CompanyTerminal.app` login item | 2026-04-10 | 残留的登录项，每次开机弹空 Terminal；旧版 company_start 遗留 |

---

## 新增登记申请模板

```
## [日期] [申请人] 新增自启项登记申请

**文件 / 条目**：<路径>
**类型**：<LaunchAgent / Login Item / brew service / ...>
**用途**：<为什么需要自动启动>
**触发条件**：<RunAtLoad / KeepAlive / StartInterval=N / 登录时 / ...>
**失败行为**：<启动失败会怎样？有没有重试？>
**Boss approve 需要的信息**：<如果不装有什么业务影响>

@<Boss user id> 请 approve / reject
```
