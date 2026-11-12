# Release v1.0.0 — Psychological Science Research Collective

**版本 / Version:** `v1.0.0`  
**平台 / Platforms:** 腾讯 WorkBuddy Expert Team、TRAE IDE  
**语言 / Languages:** 中文 / English

## 发行附件 / Release assets

将以下**两个 ZIP**作为 GitHub Release `v1.0.0` 的附件上传。它们是不同平台的独立安装/提交包，不能互换。

| Asset | 内容 |
| --- | --- |
| `psychological-science-research-team-workbuddy-v1.0.0.zip` | WorkBuddy 主理人 + 8 专家、10 Skills、头像、`.codebuddy-plugin/plugin.json`、安装与提交检查清单 |
| `psychological-science-research-collective-TRAE-v1.0.0.zip` | TRAE `AGENTS.md`、8 项目 Subagents、10 Skills、参考文献、迁移说明、6 项验收测试 |

### 设计重点

1. **心理学启发的智能体认知机制**：元认知、创造性认知、建设性重评、认知资源管理、社会认识协作。
2. **心理学科研任务适配**：理论、文献、研究创意、实验/干预设计、心理测量、统计、伦理与独立审稿。
3. **按需 Skill 调度**：先识别能力缺口，检索与审查，按权限调用；无授权或无工具时如实说明。
4. **可检查的过程**：区分已验证的来源与假设，记录实际工具/成员调用，不伪造科研证据。

### 安装与验证

- WorkBuddy：解压附件，检查作者信息与 `SUBMISSION_CHECKLIST.md`；按腾讯 WorkBuddy 官方专家团流程提交。
- TRAE：解压并用 TRAE 打开文件夹根目录；确保隐藏 `.trae/` 未丢失，按 `tests/ACCEPTANCE_TESTS.md` 测试。

**范围说明：** 两个包已进行静态验证，尚未完成真实客户端端到端测试；心理学理论属于 Agent 工作流的设计依据，不代表人类心理能力已在模型中被实证复现。

## 与仓库 README 的关系

`README.md` 是项目主页与文件结构清单；两个 ZIP 安装包应放在此 Release 的 **Assets** 中。GitHub 自动生成的 Source code 压缩包不是平台交付件。

---
See the repository [README](../README.md) for the full file-tree overview.

## 发布操作 / Publishing on GitHub

1. 打开仓库 **Releases** 页面，选择 **Draft a new release**。
2. 选择 **Choose a tag → Create new tag: `v1.0.0`**，目标分支 `main`。
3. 标题填写 `v1.0.0 — Psychological Science Research Collective (WorkBuddy + TRAE)`。
4. 发行说明可复制本文档上方的内容。
5. 在 **Attach binaries by dropping them here or selecting them** 中添加下面两个 ZIP，上传完成后选择 **Publish release**。
6. 返回 Release 页核对两个 Assets 均可下载，并检查文件名与 SHA-256。

### 校验和 / SHA-256

```text
a1aab13a9db4fc483313612bfa304a9bf379396bc8fbb5cc4812749ab8036ad6  psychological-science-research-team-workbuddy-v1.0.0.zip
0da9e6e04d8629f9fbc65f2f41dd9da036ac3d82feb7b3bc153ca539c37040cc  psychological-science-research-collective-TRAE-v1.0.0.zip
```
