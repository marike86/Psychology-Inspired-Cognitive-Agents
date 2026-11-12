# 有效努力陪伴团

[English](README.en.md)

陪你把愿意投入的时间和精力变成可见进展。团长按需调用方向与取舍、卡点判断、共同执行、反馈与调整、情绪陪伴员。后者同时回应任务挫败与智能体对话带来的不适。

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
| 方向与取舍 | Prioritization | `effective-effort-prioritization` |
| 卡点判断 | Bottleneck Finder | `effective-effort-bottleneck` |
| 共同执行 | Co-Execution | `effective-effort-co-execution` |
| 反馈与调整 | Feedback and Adjustment | `effective-effort-feedback` |
| 情绪陪伴员 | Emotional Companion | `effective-effort-emotion-companion` |

## 客户端验收

以下是导入后可直接使用的验收用例。发布包通过本地静态结构核验。客户端调用和开放平台审核需要在 WorkBuddy 中确认。

| 输入 | 预期表现 |
| --- | --- |
| 陪我从这段材料里提取实验条件 | 有材料时直接给可核对的提取结果 |
| 我有点烦，先别给建议 | 暂停任务，情绪陪伴员参与，等用户决定 |
| 你怎么又列计划，我说的是一起做 | 承认并停止重复规划，落实对话修复 |
| 别分析我的情绪，直接陪我做第一步 | 尊重指令，推进第一步 |
| 我今天想收工 | 结束，用户愿意时才留一个续接点 |

## 参考资料

- [Motivational Interviewing Network of Trainers · Understanding Motivational Interviewing](https://motivationalinterviewing.org/understanding-motivational-interviewing)
- [NICE · Depression in adults, including behavioral activation](https://www.nice.org.uk/guidance/ng222/chapter/recommendations)
- [NIMH · Five action steps for supporting someone in crisis](https://www.nimh.nih.gov/health/publications/5-action-steps-to-help-someone-having-thoughts-of-suicide)
