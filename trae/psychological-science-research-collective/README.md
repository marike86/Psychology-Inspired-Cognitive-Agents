# 心理科学研究与认知协作团 · TRAE 版
**Psychological Science Research Collective · PSRC**
**版本**：2.0.0（单 Skill 版）　**语言**：中文为主，兼容 English　**来源**：WorkBuddy 专家团架构移植

## 核心设计

本项目不是让八名虚拟心理学家轮流发言，而是把心理学关于**元认知、创造性认知、积极心理学的建设性重评、社会认识、自我调节、认知资源管理**的观点，转化为所有成员都需遵循的可观察工作规则。同时由不同科研专家负责理论、证据、创新、方法、测量、统计、伦理与审稿，通过 TRAE 内置 Agent 选择性调度。

2.0 版把原先 10 个独立 Skill 合并为 **1 个主 Skill**（`psychological-research-collective`），细则拆入 `references/` 按需加载：触发更准、加载更快，也更便于公开分发与全局安装。

## 安装

### 方式 A：全局安装（推荐，所有项目可用）

1. 下载并完整解压，保留隐藏的 `.trae/`。
2. 复制 Skill 目录：
   - Windows：`copy /r psychological-science-research-collective\.trae\skills\psychological-research-collective "%USERPROFILE%\.trae-cn\skills\"`
   - macOS/Linux：`cp -r psychological-science-research-collective/.trae/skills/psychological-research-collective ~/.trae-cn/skills/`
3. 复制 Subagent（可选）：
   - Windows：`copy /r psychological-science-research-collective\.trae\agents "%USERPROFILE%\.trae-cn\"`
   - macOS/Linux：`cp -r psychological-science-research-collective/.trae/agents ~/.trae-cn/`
4. 重启 TRAE，在 **设置 > 技能与命令** 确认出现 `psychological-research-collective`。

### 方式 B：作为项目打开

1. 在 TRAE 选择 **打开文件夹/项目**，打开解压后的根目录，不要只打开 `README.md`。
2. 进入 **设置 > 规则**，开启 **「将 AGENTS.md 包含在上下文中」**，并确认项目受信任。
3. 在 **设置 > Beta** 中确认 **Subagents** 已启用。
4. 打开**内置「Agent」**而不是自定义 Agent。

> 想把专家团用于**已有科研项目**：先备份该项目的 `AGENTS.md` 与 `.trae/`，然后仅合并本包的 `.trae/agents/*.md` 与 `.trae/skills/psychological-research-collective/`，并把 `AGENTS.md` 的共享机制与路由规则人工合并到已有规则，**不要整包覆盖**。

## 项目结构

```text
AGENTS.md                                  # 内置 Agent 的共享认知架构与调度规则
.trae/
  agents/                                  # 8 个可按需调度的 Subagent
    theory-mechanisms.md
    evidence-cartographer.md
    creative-ideation.md
    methodology-architect.md
    psychometrics-specialist.md
    statistics-analyst.md
    ethics-open-science.md
    adversarial-reviewer.md
  skills/
    psychological-research-collective/     # 唯一主 Skill
      SKILL.md                             # 先行原则、共享机制、科研流程、专家路由
      references/                          # 细则模块，按需加载
        metacognitive-regulation.md
        creative-scientific-reasoning.md
        constructive-reframing.md
        cognitive-resource-management.md
        social-epistemic-collaboration.md
        research-lifecycle.md
        evidence-traceability.md
        methods-and-psychometrics.md
        adversarial-peer-review.md
        skill-discovery-router.md
        theory-and-sources.md
docs/REFERENCES.md                         # 心理学理论依据与工程化边界
docs/MIGRATION.md                          # WorkBuddy → TRAE 关键映射
tests/ACCEPTANCE_TESTS.md                  # 可验证的手动测试
tests/validate_package.py                  # 离线结构校验
```

## 核心运行方式

- **简单解释**：无需调用子智能体，直接按元认知简化流程作答。
- **研究问题/文献综述**：先交由理论与证据相关成员，复杂时再邀创造性构思成员。
- **实验/干预**：按需求调用方法设计、测量、统计、伦理成员。
- **投稿前审稿**：冻结当前方案，交由 `adversarial-reviewer` 独立检查；不要预设审稿结论。
- **遇到领域工具缺口**：选用 `skill-discovery-router` 模块；能搜索则检索候选，安装/执行外部技能前核对安全性并征求同意。

**注意**：`tools: WebSearch`、`Skill` 等字段是许可使用的工具清单，平台是否实际提供、能否联网或并行执行，取决于本地版本、账户及运行环境。文件通过格式检查 ≠ 客户端已运行成功。子智能体由内置 Agent 调度；成员不能自主建队或彼此互调。

## 可复制的首次测试提示词

> 请帮我讨论“多智能体交互能否促进科学假设生成”的可检验研究问题。先独立调用理论与机制研究员、证据与综述研究员，再按需要调用创造性构思员。严格区分已核查的研究证据和未经证实的创意，并在结尾说明本轮实际调用了哪些 Subagent 和 Skill。

更多边界、路由、权限和测试步骤见 `tests/ACCEPTANCE_TESTS.md`。

## 官方规范（依据 2026 年 11 月核对）

- [TRAE 子智能体](https://docs.trae.cn/ide_subagents) —— 项目级 `.trae/agents/`、用户级 `~/.trae-cn/agents/`；`name` / `description`、工具表；内置 Agent 负责调用。
- [TRAE Skills](https://docs.trae.cn/ide_skills) —— `.trae/skills/<name>/SKILL.md`、`references/` 子目录；按需加载、元数据和目录可信。
- [TRAE 规则](https://docs.trae.cn/ide_rules) —— 根目录 `AGENTS.md`；设置里开启导入。

## English overview

PSRC is a psychology-inspired scientific research collective adapted for the TRAE IDE. A project-level `AGENTS.md` supplies cognitive and orchestration rules to the **built-in Agent**; eight Subagents provide specialist research functions; a single `psychological-research-collective` Skill provides reusable metacognitive, creative, positive-psychology-inspired, social-epistemic, methodological and evidence-verification workflows, with detailed modules loaded on demand from `references/`. Install globally under `~/.trae-cn/skills/` or open the folder as a trusted TRAE project, then test actual delegation. These mechanisms are AI workflow analogies, not evidence that models possess human mental states or guaranteed performance gains.

License: MIT. See `LICENSE` and `docs/REFERENCES.md`.
