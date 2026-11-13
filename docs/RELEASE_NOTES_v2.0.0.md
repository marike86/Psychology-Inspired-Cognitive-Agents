# Release v2.0.0 — Psychological Science Research Collective

**版本 / Version:** `v2.0.0`
**平台 / Platforms:** 腾讯 WorkBuddy Expert Team、TRAE IDE
**语言 / Languages:** 中文 / English

## 本版要点 / What's new

**TRAE 侧：10 个独立 Skill 合并为 1 个主 Skill。**

原 v1.0.0 的 TRAE 包把元认知调节、创造性科学推理、建设性重评、认知资源管理、社会认识协作等拆成 10 个平级 `SKILL.md`。多个平级 Skill 的 `description` 会互相竞争触发，且每次都要各自加载一次完整正文。v2.0 改为：

- 唯一主 Skill `psychological-research-collective` —— 承载先行原则、5 类共享认知机制、P0–P5 科研流程、8 位专家路由与能力缺口协议；
- 原 10 个 Skill 的正文**全部保留**为 `references/` 下的细则模块（另加 `theory-and-sources.md`），按需读取，内容未删减；
- 8 个 Subagent 的 Skill 指针改指主 Skill 的对应模块，调度边界说明同步更新。

合并后触发语义更统一、运行时上下文更干净，也便于全局安装（`~/.trae-cn/skills/`）与公开分发。逐项映射见 TRAE 包内 `docs/MIGRATION.md`。

## 发行附件 / Release assets

将以下**两个 ZIP**作为 GitHub Release `v2.0.0` 的附件上传。它们是不同平台的独立安装/提交包，不能互换。

| Asset | 内容 |
| --- | --- |
| `psychological-science-research-team-workbuddy-v2.0.0.zip` | WorkBuddy 主理人 + 8 专家、11 Skills、头像、`.codebuddy-plugin/plugin.json`、安装与提交检查清单 |
| `psychological-science-research-collective-TRAE-v2.0.0.zip` | TRAE `AGENTS.md`、8 项目 Subagents、**1 个主 Skill + 11 个 `references/` 模块**、参考文献、迁移说明、6 项验收测试 |

### 校验和 / SHA-256

```text
b2eec8cc25899c047cfcb41030504295b9b2a7fcb62ad0ec53437ee0a0ec5a81  psychological-science-research-team-workbuddy-v2.0.0.zip
17a666b032d45da847c21e988e0a69f00c4bc1cb9d0e4e83ba62133828b5e0b2  psychological-science-research-collective-TRAE-v2.0.0.zip
```

### 安装与验证

- WorkBuddy：解压附件，检查作者信息与 `SUBMISSION_CHECKLIST.md`；按腾讯 WorkBuddy 官方专家团流程提交。
- TRAE：解压并用 TRAE 打开文件夹根目录；确保隐藏 `.trae/` 未丢失，按 `tests/ACCEPTANCE_TESTS.md` 测试。

**范围说明：** 两个包已进行静态验证，尚未完成真实客户端端到端测试；心理学理论属于 Agent 工作流的设计依据，不代表人类心理能力已在模型中被实证复现。

## 与仓库的关系

`README.md` 是项目主页与文件结构清单；两个 ZIP 安装包应放在本 Release 的 **Assets** 中。GitHub 自动生成的 Source code 压缩包不是平台交付件。

v2.0 起，仓库 `main` 分支同时收录 TRAE 发行包的可读源码 `trae/psychological-science-research-collective/`，便于直接查阅与二次修改。

---

See the repository [README](../README.md) for the full file-tree overview.

## 发布操作 / Publishing on GitHub

1. 打开仓库 **Releases** 页面，选择 **Draft a new release**。
2. 选择 **Choose a tag → Create new tag: `v2.0.0`**，目标分支 `main`。
3. 标题填写 `v2.0.0 — Psychological Science Research Collective (WorkBuddy + TRAE)`。
4. 发行说明可复制本文档上方的内容。
5. 在 **Attach binaries by dropping them here or selecting them** 中添加下面两个 ZIP，上传完成后选择 **Publish release**。
6. 返回 Release 页核对两个 Assets 均可下载，并检查文件名与 SHA-256。
