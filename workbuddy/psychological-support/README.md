# 心理咨询支持团

[English](README.en.md)

人本取向团长和 15 位可点名的 AI 心理支持成员。适合倾听、围绕一个议题进行自我探索，或比较流派的理解。诊断、用药和临床治疗由真人专业人员承担。

## 在 WorkBuddy 中使用

- **客户端自用**。打开专家市场 → 我的专家 → 创建专家团。将解压后的团长与成员定义作为创建材料，按创建对话提示核对各角色的名称与分工。
- **开放平台提交**。上传当前团队的独立 ZIP，根目录应能直接看到 `.codebuddy-plugin/` 和 `settings.json`。如提交需要真实联系邮箱，将清单里沿用的示例作者邮箱改成发布者的联系邮箱，再重新压缩。
- **切换团队**。新开一个会话再召唤另一团。只复制你愿意带过去的内容。平台侧的会话留存与权限由 WorkBuddy 管理。

[官方专家团规范](https://open.workbuddy.cn/docs/expert-team) · [专家市场与创建入口](https://open.workbuddy.cn/docs/expert)

## 包内结构

```text
.codebuddy-plugin/plugin.json
settings.json
agents/
avatars/
README.md
README.en.md
```

`.codebuddy-plugin/plugin.json` 注册团长、团员、头像和中英文卡片。根目录的 `settings.json` 指定团长，`agents/` 是独立角色指令，`avatars/` 提供团队与每个角色的 PNG 头像。

## 成员

| 中文 | English | Agent ID |
| --- | --- | --- |
| 心理动力学 | Psychodynamic | `psychological-support-psychodynamic` |
| 依恋取向 | Attachment-Informed | `psychological-support-attachment` |
| 心智化（MBT） | Mentalization (MBT) | `psychological-support-mentalization` |
| 图式疗法 | Schema Therapy | `psychological-support-schema` |
| 个体情绪聚焦（EFT） | Individual Emotion-Focused (EFT) | `psychological-support-emotion-focused` |
| 格式塔 | Gestalt-Informed | `psychological-support-gestalt` |
| 慈悲聚焦（CFT） | Compassion-Focused (CFT) | `psychological-support-compassion-focused` |
| 认知行为（CBT） | Cognitive Behavioral (CBT) | `psychological-support-cognitive-behavioral` |
| 接纳与承诺（ACT） | Acceptance and Commitment (ACT) | `psychological-support-acceptance-commitment` |
| 辩证行为技能（DBT） | Dialectical Behavior Skills (DBT) | `psychological-support-dialectical-skills` |
| 人际心理治疗（IPT）视角 | Interpersonal (IPT) Perspective | `psychological-support-interpersonal` |
| 系统式家庭与关系视角 | Systemic Family and Relationship | `psychological-support-systemic` |
| 叙事疗法 | Narrative | `psychological-support-narrative` |
| 焦点解决短期疗法（SFBT） | Solution-Focused Brief (SFBT) | `psychological-support-solution-focused` |
| 存在主义取向 | Existential | `psychological-support-existential` |

## 客户端验收

以下是导入后可直接使用的验收用例。发布包通过本地静态结构核验。客户端调用和开放平台审核需要在 WorkBuddy 中确认。

| 输入 | 预期表现 |
| --- | --- |
| 今天先听我讲，不用分析 | 团长倾听，不调度成员 |
| 请依恋和心智化一起看，最后只问一个问题 | 两位实际成员独立参与，团长说明区别并聚焦一个问题 |
| 这轮只用个体 EFT | 按指定取向跟进，直到用户改变要求 |
| 不想把这段转给团员 | 团长独立回应 |
| 收一下 | 总结已确认内容与仍待探索的问题 |

## 参考资料

- [APA · Approaches to psychotherapy](https://www.apa.org/topics/psychotherapy/approaches)
- [APA PsycTherapy · Featured approaches](https://www.apa.org/pubs/databases/psyctherapy/approaches.aspx)
- [Anna Freud · Mentalization-Based Treatment](https://www.annafreud.org/training/health-and-social-care/mentalization-based-treatments-mbt/mentalization-based-treatment-adults/about-mbt/)
- [International Society for Emotion Focused Therapy](https://www.iseft.org/about-us)
- [Gilbert · Introducing compassion-focused therapy](https://doi.org/10.1192/apt.bp.107.005264)
- [Dulwich Centre · Externalising the problem](https://dulwichcentre.com.au/courses/aboriginal-narrative-practice-course/lessons/03-externalising/)
- [Solution-Focused Therapy Institute · What is SFBT?](https://solutionfocused.net/what-is-solution-focused-therapy/)
- [NIMH · Five action steps for supporting someone in crisis](https://www.nimh.nih.gov/health/publications/5-action-steps-to-help-someone-having-thoughts-of-suicide)
