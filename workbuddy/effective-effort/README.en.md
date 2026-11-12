# Effective Effort Companion Team

[简体中文](README.md)

Turn the time and energy you choose to spend into observable progress. The lead can call Prioritization, Bottleneck Finder, Co-Execution, Feedback and Adjustment, or the Emotional Companion. The companion addresses both task frustration and friction with the AI.

## Use in WorkBuddy

- **Personal use in the client.** Open Expert Market → My Experts → Create Expert Team. Provide the extracted lead and member definitions as creation materials and review the names and duties in the setup conversation.
- **Open Platform submission.** Upload this team's standalone ZIP with `.codebuddy-plugin/` and `settings.json` at the root. If submission requires a real contact, replace the sample author email in the manifest and rebuild the archive.
- **Switching teams.** Open a new conversation and invoke the other team. Copy only the information you want to carry over. WorkBuddy manages its own conversation retention and permissions.

[Official team specification](https://open.workbuddy.cn/docs/expert-team) · [Expert Market and team creation](https://open.workbuddy.cn/docs/expert)

## Package layout

```text
.codebuddy-plugin/plugin.json
settings.json
agents/
avatars/
README.md
README.en.md
```

`.codebuddy-plugin/plugin.json` registers the lead, members, avatars and bilingual card text. `settings.json` selects the lead. `agents/` contains individual role instructions, and `avatars/` contains team and role PNGs.

## Members

| 中文 | English | Agent ID |
| --- | --- | --- |
| 方向与取舍 | Prioritization | `effective-effort-prioritization` |
| 卡点判断 | Bottleneck Finder | `effective-effort-bottleneck` |
| 共同执行 | Co-Execution | `effective-effort-co-execution` |
| 反馈与调整 | Feedback and Adjustment | `effective-effort-feedback` |
| 情绪陪伴员 | Emotional Companion | `effective-effort-emotion-companion` |

## Client acceptance checks

Use these cases after import. The package passed local static checks. Verify live member calls and platform review in WorkBuddy.

| Input | Expected behavior |
| --- | --- |
| Extract the experimental conditions from this passage with me | Produce a verifiable extraction when the passage is supplied |
| I'm frustrated. Stop giving advice | Pause task progress, involve the Emotional Companion and wait for the user's preference |
| You keep planning. I asked you to work with me | Own the mismatch, stop replanning and apply the repair |
| Skip the emotion discussion and do the first step with me | Follow the user's instruction and start the first step |
| I'm done for today | Close. Leave a restart point if the user wants it |

## References

- [Motivational Interviewing Network of Trainers · Understanding Motivational Interviewing](https://motivationalinterviewing.org/understanding-motivational-interviewing)
- [NICE · Depression in adults, including behavioral activation](https://www.nice.org.uk/guidance/ng222/chapter/recommendations)
- [NIMH · Five action steps for supporting someone in crisis](https://www.nimh.nih.gov/health/publications/5-action-steps-to-help-someone-having-thoughts-of-suicide)
