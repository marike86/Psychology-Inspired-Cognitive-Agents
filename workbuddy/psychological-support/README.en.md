# Psychological Support Team

[简体中文](README.md)

A person-centered lead and 15 selectable AI perspectives for listening, exploring one issue or comparing approaches. Qualified human professionals handle diagnosis, medication and clinical treatment.

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

## Client acceptance checks

Use these cases after import. The package passed local static checks. Verify live member calls and platform review in WorkBuddy.

| Input | Expected behavior |
| --- | --- |
| Just listen today | The lead listens without delegating |
| Compare attachment and mentalization, then ask me one question | Both members are actually called and the lead distinguishes the views and asks one question |
| Use individual EFT only | The lead keeps the requested approach until the user changes it |
| Keep this with the lead | The lead responds without delegation |
| Summarize | The lead separates what was clarified from what remains open |

## References

- [APA · Approaches to psychotherapy](https://www.apa.org/topics/psychotherapy/approaches)
- [APA PsycTherapy · Featured approaches](https://www.apa.org/pubs/databases/psyctherapy/approaches.aspx)
- [Anna Freud · Mentalization-Based Treatment](https://www.annafreud.org/training/health-and-social-care/mentalization-based-treatments-mbt/mentalization-based-treatment-adults/about-mbt/)
- [International Society for Emotion Focused Therapy](https://www.iseft.org/about-us)
- [Gilbert · Introducing compassion-focused therapy](https://doi.org/10.1192/apt.bp.107.005264)
- [Dulwich Centre · Externalising the problem](https://dulwichcentre.com.au/courses/aboriginal-narrative-practice-course/lessons/03-externalising/)
- [Solution-Focused Therapy Institute · What is SFBT?](https://solutionfocused.net/what-is-solution-focused-therapy/)
- [NIMH · Five action steps for supporting someone in crisis](https://www.nimh.nih.gov/health/publications/5-action-steps-to-help-someone-having-thoughts-of-suicide)
