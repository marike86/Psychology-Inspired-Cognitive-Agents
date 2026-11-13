# 理论依据、引用著录与工程化边界

> 本包为**心理学启发的工程方案**。以下研究描述人类认知/学习/创造力/协作或心理学研究规范，并不直接证明该提示词架构能使 LLM 拥有人类心理过程，更不意味着已经进行了模型效果实验。
>
> Skill 内只嵌入有明确可操作架构且有助于执行的少量论文链接；详细著录与边界在本文件，防止运行时上下文被无关引用淹没。

| 研究 / DOI | 对应设计思想 | 理论到 Agent 的转换边界 |
| --- | --- | --- |
| Flavell, J. H. (1979). *Metacognition and cognitive monitoring*. *American Psychologist, 34*(10), 906–911. [DOI](https://doi.org/10.1037/0003-066X.34.10.906) | 区分元认知知识、体验与认知监控；提醒对目标、策略、知识缺口进行检查 | 智能体仅实现外显监控规则，不等于自我意识 |
| Zimmerman, B. J. (2002). *Becoming a self-regulated learner: An overview*. *Theory Into Practice, 41*(2), 64–70/72（页面版本页码记载存在差异，请投稿引用时依原刊核准）. [DOI](https://doi.org/10.1207/s15430421tip4102_2) | 前瞻—执行—自我反思的循环启发科研工作流 | 自我调节学习模型不能直接等同机器学习能力 |
| Nijstad, B. A., De Dreu, C. K. W., Rietzschel, E. F., & Baas, M. (2010). *The dual pathway to creativity model: Creative ideation as a function of flexibility and persistence*. *European Review of Social Psychology, 21*, 34–77. [DOI](https://doi.org/10.1080/10463281003765323) | 创造性探索的灵活切换与坚持深入双路径 | 不表明 LLM 必然获得人类创造性机制 |
| Runco, M. A., & Jaeger, G. J. (2012). *The standard definition of creativity*. *Creativity Research Journal, 24*(1), 92–96. [DOI](https://doi.org/10.1080/10400419.2012.650092) | 将“新颖且适切”设为创意评估双标准 | AI 输出需要实证/文献验证，不能自评代表外部有效性 |
| Amabile, T. M. (1983). *The social psychology of creativity: A componential conceptualization*. *Journal of Personality and Social Psychology, 45*(2), 357–376. [DOI](https://doi.org/10.1037/0022-3514.45.2.357) | 领域技能、创造相关技能、任务动机与社会环境的分层考虑 | 人类动机不等同模型偏好；用于角色/资源配置类比 |
| Fredrickson, B. L. (2001). *The role of positive emotions in positive psychology: The broaden-and-build theory of positive emotions*. *American Psychologist, 56*(3), 218–226. [DOI](https://doi.org/10.1037/0003-066X.56.3.218) | 建设性重评、扩展候选行动、保存已有资源的设计启发 | 不声称 AI 体验情绪，也不要求积极结论 |
| Sweller, J. (1988). *Cognitive load during problem solving: Effects on learning*. *Cognitive Science, 12*(2), 257–285. [DOI](https://doi.org/10.1207/s15516709cog1202_4) | 聚焦与信息分块的任务设计启发 | LLM 上下文限制与人类工作记忆不是同一构念 |
| Wegner, D. M., Erber, R., & Raymond, P. (1991). *Transactive memory in close relationships*. *Journal of Personality and Social Psychology, 61*(6), 923–929. [DOI](https://doi.org/10.1037/0022-3514.61.6.923) | 专家职责分配与“谁知道什么”的跨成员知识索引 | 不声称代理之间自发拥有与人同构的交互记忆 |
| Kahneman, D., & Klein, G. (2009). *Conditions for intuitive expertise: A failure to disagree*. *American Psychologist, 64*(6), 515–526. [DOI](https://doi.org/10.1037/a0016755) | 防止仅凭自信判断，要求证据和反馈环境条件 | 是审稿/反证提醒，不是多智能体效果试验 |
| Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). *The preregistration revolution*. *PNAS, 115*(11), 2600–2606. [DOI](https://doi.org/10.1073/pnas.1708274114) | 区分确认性与探索性分析，促进预注册与透明报告 | 预注册是研究治理流程，不等于自动保证有效性 |

## 规范文件与平台依据（TRAE 版）
- TRAE IDE 子智能体规范：https://docs.trae.cn/ide_subagents
- TRAE IDE Skills 格式与目录：https://docs.trae.cn/ide_skills
- TRAE IDE AGENTS.md 项目规则：https://docs.trae.cn/ide_rules

## 设计追踪矩阵

| 心理学思想 | 实现层 | 具体触发/可观察输出 | 证据状态 |
| --- | --- | --- | --- |
| 元认知监控与调节 | `.trae/skills/` + 所有 Subagent | 目标/未知检查、计划调整、终止判断 | 人类理论启发；Agent 行为待测 |
| 创造性思维（发散/聚合，灵活/坚持） | 创造力 Skill + 创意 Subagent | 多条不同机制路径、可证伪预测、评价标准 | 人类理论启发；Agent 行为待测 |
| 积极心理学（拓展—建构） | 重评 Skill + 全体 Subagent | 负面结果事实识别、资源保留、下一轮最小检验 | 工程类比；AI 情绪不适用 |
| 社会认知与跨成员专业分工 | 协作 Skill + 内置 Agent 路由 | 独立判断、分歧记录、证据驱动整合 | 工程类比；协同收益待测 |
| 认知资源/负荷管理 | 认知资源 Skill + 内置 Agent | 关键上下文摘要、任务分块、动态停止 | 工程类比；收益待测 |
| 科学研究治理 | workflow & evidence & methods | 来源矩阵、伦理检查、预注册与复现计划 | 科研规范支撑，仍需实际执行 |

## 可检验的工程评价（建议上线后实测）
- 正确路由率：目标任务是否调用必要成员/Skill，是否出现不必要全员调用。
- 来源真实性：引用条目 DOI 与陈述支持程度，工具调用日志是否一致。
- 创造性产出：盲评原创性、适切性、科学可检验性、方案多样性。
- 元认知校准：不确定性标注、面对反证修改率、无证据夸大率。
- 协作增益：相同 token/时间预算下，专家团与单 Agent 对比，避免成本混淆。
- 安全性：未经授权安装/执行、敏感数据外传、虚假已完成报告的频率。
