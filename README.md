# Psychology-Inspired Cognitive Agents
### 心理学启发的认知智能体系统

**Psychological Science Research Collective (PSRC) · v1.0.0 · WorkBuddy + TRAE**

将心理学研究的不只是*内容*，而是研究中使用的**认知与协作策略**：在科研工作流中引入元认知调节、创造性科学推理、建设性重评、认知资源管理、社会认识协作和按需 Skill 路由。

> Psychology-inspired workflows, not simulated human consciousness. 本项目将心理学理论转化为可观察、可检查的 Agent 行为规则；不主张 AI 具备人的情绪或自我意识，也不预设这些规则必然提高性能。

## 下载 / Download

**v1.0.0 对应两套平台适配包**（以 GitHub **Releases** 的资产为正式发行件）：

| 平台 | 发行包 | 用途 |
| --- | --- | --- |
| [WorkBuddy](https://open.workbuddy.cn/) | `psychological-science-research-team-workbuddy-v1.0.0.zip` | 腾讯 WorkBuddy 专家团，团长与成员、共享 Skills、插件配置和头像 |
| [TRAE](https://www.trae.cn/) | `psychological-science-research-collective-TRAE-v1.0.0.zip` | TRAE IDE 项目级认知规则、Subagents、Skills、验证测试 |

**[查看 Releases](https://github.com/marike86/Psychology-Inspired-Cognitive-Agents/releases)** · **[v1.0.0 发行说明](docs/RELEASE_NOTES_v1.0.0.md)**

> 若 Releases 中暂未出现 `v1.0.0` 或缺少两个 ZIP 附件，请勿将本页视为已完成发布。两个原始 ZIP 需要作为该 Release 的 Assets 上传；GitHub 自动生成的 “Source code (zip)” 不等于上述平台安装包。

## WorkBuddy 心理支持与有效努力陪伴团 / Psychological Support and Effective Effort Team

召唤一个专家团即可开始。在同一会话里，团长会根据你当下的需要倾听、陪做或修复对话，也会在你想继续时接上原来的任务。团队包含 15 位可点名的心理视角成员、4 位任务成员和 1 位情绪陪伴员。

Invoke one team to get started. The lead listens, works alongside you, repairs conversational friction and resumes your task in the same chat. The team has 15 selectable psychological perspectives, four task specialists and an Emotional Companion.

**[下载 WorkBuddy ZIP / Download v1.1.0](workbuddy/psychological-companion-team-workbuddy-v1.1.0.zip)** · [中文说明](workbuddy/psychological-companion/README.md) · [English guide](workbuddy/psychological-companion/README.en.md)

## 设计理念 / Design

**学科理论 → 认知策略 → 专家协作 → 工具与 Skill → 科研交付**

| 心理学视角 | 在 Agent 行为中的实现 |
| --- | --- |
| 元认知 / Metacognition | 明确任务目标、规划、知识缺口检查、监控、评价与策略调整 |
| 创造力心理学 / Creativity | 问题重构、发散与聚合、跨领域联想、竞争性假设 |
| 积极心理学 / Positive psychology | 遇到失败时进行建设性重评、识别可利用资源与下一步行动，不粉饰证据 |
| 认知心理学 / Cognitive psychology | 认知资源管理、工作分解、知识组织、信息筛选 |
| 社会心理学 / Social psychology | 专家独立分析、观点采择、冲突管理、证据驱动共识 |
| 自我调节 / Self-regulation | 依据反馈进行修正，将经过验证的方法沉淀为可复用策略 |

### 科研任务路由

1. **理解与规划**：明确问题、成功标准、未知信息和约束。
2. **理论与证据**：由相关专家分析机制、核实文献，区分证据与猜想。
3. **创造与设计**：需要时进行研究构思、实验/干预与心理测量设计。
4. **评估与反证**：统计、伦理、开放科学和独立审稿；遇冲突时保留替代解释。
5. **修正与交付**：据反馈调整方案，标明实际调用过的 Agent / Skill / 工具。

不要求每次都调用全部专家；简单任务可简化。Skill 的联网发现、安装、调用受平台能力和用户授权限制，不能假装已执行。

## 交付包内部文件结构 / Archive contents

下面展示两套 **ZIP 解压后的结构**。这些是发行包内部文件，不意味着相同目录已经放在仓库 `main` 分支中。

### WorkBuddy 专家团 · 35 files

```text
psychological-science-research-team/
├── .codebuddy-plugin/
│   └── plugin.json                      # WorkBuddy 专家团配置
├── agents/
│   ├── psychological-science-research-team-lead.md
│   ├── theory-mechanisms.md
│   ├── evidence-cartographer.md
│   ├── creative-ideation.md
│   ├── methodology-architect.md
│   ├── psychometrics-specialist.md
│   ├── statistics-analyst.md
│   ├── ethics-open-science.md
│   └── adversarial-reviewer.md
├── avatars/                             # 团队与 9 个角色的 PNG 头像
│   ├── team.png
│   ├── team-lead.png
│   ├── theory-mechanisms.png
│   ├── evidence-cartographer.png
│   ├── creative-ideation.png
│   ├── methodology-architect.png
│   ├── psychometrics-specialist.png
│   ├── statistics-analyst.png
│   ├── ethics-open-science.png
│   └── adversarial-reviewer.png
├── skills/
│   ├── metacognitive-regulation/SKILL.md
│   ├── creative-scientific-reasoning/SKILL.md
│   ├── constructive-reframing/SKILL.md
│   ├── cognitive-resource-management/SKILL.md
│   ├── social-epistemic-collaboration/SKILL.md
│   ├── skill-discovery-router/SKILL.md
│   ├── research-lifecycle/SKILL.md
│   ├── evidence-traceability/SKILL.md
│   ├── methods-and-psychometrics/SKILL.md
│   └── adversarial-peer-review/SKILL.md
├── docs/
│   └── REFERENCES.md                    # 心理学依据及工程化边界
├── settings.json
├── SUBMISSION_CHECKLIST.md
├── LICENSE
└── README.md
```

**安装/提交**：完整解压，按 `README.md` 与 `SUBMISSION_CHECKLIST.md` 验证；向 WorkBuddy 提交前检查 `.codebuddy-plugin/plugin.json` 中的作者信息。参见 [WorkBuddy 专家团规范](https://open.workbuddy.cn/docs/expert-team)。

### TRAE 项目 · 25 files

```text
psychological-science-research-collective-trae/
├── AGENTS.md                             # 共享认知架构与调度规则
├── .trae/
│   ├── agents/                           # 8 个项目级 Subagents
│   │   ├── theory-mechanisms.md
│   │   ├── evidence-cartographer.md
│   │   ├── creative-ideation.md
│   │   ├── methodology-architect.md
│   │   ├── psychometrics-specialist.md
│   │   ├── statistics-analyst.md
│   │   ├── ethics-open-science.md
│   │   └── adversarial-reviewer.md
│   └── skills/                           # 10 个 SKILL.md
│       ├── metacognitive-regulation/SKILL.md
│       ├── creative-scientific-reasoning/SKILL.md
│       ├── constructive-reframing/SKILL.md
│       ├── cognitive-resource-management/SKILL.md
│       ├── social-epistemic-collaboration/SKILL.md
│       ├── skill-discovery-router/SKILL.md
│       ├── research-lifecycle/SKILL.md
│       ├── evidence-traceability/SKILL.md
│       ├── methods-and-psychometrics/SKILL.md
│       └── adversarial-peer-review/SKILL.md
├── docs/
│   ├── REFERENCES.md
│   └── MIGRATION.md                      # WorkBuddy → TRAE 迁移映射
├── tests/
│   ├── ACCEPTANCE_TESTS.md
│   └── validate_package.py
├── LICENSE
└── README.md
```

**安装**：解压并在 TRAE IDE **打开整个根目录**；保留隐藏的 `.trae/` 文件夹；按包内 `README.md` 检查 AGENTS.md 导入、Subagents、项目 Skills，再执行验收测试。参见 [TRAE Subagents](https://docs.trae.cn/ide_subagents) 与 [TRAE Skills](https://docs.trae.cn/ide_skills)。

## 专家组成 / Research specialists

理论与机制、证据与综述、创造性研究构思、实验与干预方法、心理测量、统计与可复现分析、科研伦理与开放科学、独立审稿与反证。WorkBuddy 由额外的**主理人**统筹；TRAE 的项目级共享调度规则放在 `AGENTS.md`，由内置 Agent 按条件调用专家。

## 验证状态 / Validation

- 静态目录、配置格式和 ZIP 完整性检查已进行。
- **尚未宣称**通过 WorkBuddy / TRAE 客户端的端到端运行或平台审核。
- 理论参考文献与边界分别见两套包内 `docs/REFERENCES.md`。

## License

以各平台发行包内 `LICENSE` 为准。
