# WorkBuddy → TRAE 移植说明

## 为什么不是重命名 ZIP
- WorkBuddy 使用 `.codebuddy-plugin/plugin.json`、`settings.json` 与团队主理人文件描述团队协作；TRAE IDE 不以这些清单部署专家团。
- TRAE IDE 的项目级 Subagent 使用 `.trae/agents/<name>.md` 且要求 `name` / `description` frontmatter；由**内置 Agent** 根据匹配自动调用，成员不彼此调用。
- 主理人的思考方式、专家调度和科研流程改写为根级 `AGENTS.md`，受 32 KB 规则大小限制（包括其它 Rule）；不是把原 WorkBuddy lead 原样当成一个可调用主智能体。
- WorkBuddy 共享 `skills/` 转为 TRAE 的 `.trae/skills/<name>/SKILL.md`；2.0 版进一步合并为单主 Skill `psychological-research-collective`，细则置于其 `references/`。
- 移除了 WorkBuddy 特有的 `TeamCreate` / `SendMessage`，明确不声明虚构的专家协作和外部 Skill 安装。

## 1.0 → 2.0 的合并映射

| 1.0 的 10 个独立 Skill | 2.0 主 Skill 中的位置 |
| --- | --- |
| `metacognitive-regulation` | `references/metacognitive-regulation.md` |
| `creative-scientific-reasoning` | `references/creative-scientific-reasoning.md` |
| `constructive-reframing` | `references/constructive-reframing.md` |
| `cognitive-resource-management` | `references/cognitive-resource-management.md` |
| `social-epistemic-collaboration` | `references/social-epistemic-collaboration.md` |
| `research-lifecycle` | `references/research-lifecycle.md` |
| `evidence-traceability` | `references/evidence-traceability.md` |
| `methods-and-psychometrics` | `references/methods-and-psychometrics.md` |
| `adversarial-peer-review` | `references/adversarial-peer-review.md` |
| `skill-discovery-router` | `references/skill-discovery-router.md` |
| —（原 `docs/REFERENCES.md`） | `references/theory-and-sources.md` |

合并理由：单 Skill 的 `description` 承载统一触发语义，避免 10 个 Skill 互相竞争触发；细则改为按需读取 `references/`，运行时上下文更干净。8 个 Subagent 保持独立定义，其内部 Skill 指针已改指主 Skill 的对应模块。

## 能力差异

| 需求 | TRAE 实现 | 限制 |
| --- | --- | --- |
| 心理学启发的共同认知规则 | 项目根 `AGENTS.md`；Subagent 中同步简要机制 | 属于 prompt/流程类比，不是人类真实心理能力 |
| 科研专业分工 | 8 个 Subagent（项目级或用户级） | 只能由 TRAE 内置 Agent 调度 |
| Skill 按需加载 | 1 个主 Skill + `references/` 模块 | 依赖启用、信任、模型与工具支持 |
| 外部技能发现 | `skill-discovery-router` 模块指导，若安装 `find-skills` 可搜索 | 本包没有自动安装外部依赖，也不保证可联网 |
| 同行独立审查 | `adversarial-reviewer` 子智能体 | 真正的独立程度、是否调用要在执行日志确认 |
| 对外发布 | 可分享项目 ZIP 或 Git 仓库 | 不是 WorkBuddy 的“专家团市场上架包” |

## 注意事项

- 不要把 `.codebuddy-plugin/plugin.json`、`settings.json` 复制到 TRAE 项目中以为能识别。
- 请在 TRAE 的 **Agent** 模式启动，而不是在一个无法调用 Subagents 的自定义智能体里强行指定专家团队。
- 当 Subagent 不识别时检查设置 > Beta、项目路径、名称合法性、description 语义、目录信任及重复角色名。
- 需全项目生效时把 `.trae/agents/*.md` 复制到用户级 `%userprofile%/.trae-cn/agents/`（Windows）或 `~/.trae-cn/agents/`（macOS/Linux）；Skill 对应复制到 `~/.trae-cn/skills/`。
