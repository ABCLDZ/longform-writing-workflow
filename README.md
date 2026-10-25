# 长风 · 中文长文写作 Skill

把问题、资料或已有稿件整理成有依据、自然可读的中文文章。适合公众号、行业观察和知识型写作，也可只精修一段、检查一个标题或规划配图。

核心是五个判断：读者要理解什么、证据支持到哪里、结构需要多深、修改是否保持原意、标题承诺能否兑现。材料足够且用户明确要成稿时，直接完成；局部任务按指定范围结束。

作者：ABCLDZ。版本：2.0.1。采用 [MIT 许可](LICENSE)。

**不限定 Codex。** 这是面向支持 `SKILL.md` 的 AI 工具的写作方法，提供通用版和 WorkBuddy 版。国内工具如 WorkBuddy 可按下方步骤安装；其他工具按自身的 Skill 导入方式使用，不依赖特定模型品牌。

[下载发布包](https://github.com/ABCLDZ/longform-writing-workflow/releases/latest) · [使用示例](examples/quick-start.md)

## 能做什么

| 任务 | 交付 |
| --- | --- |
| 从主题和资料写稿 | 标题和完整正文，按需简述重要缺口 |
| 检查已有文章 | 区分事实、推断和假设，保留有依据的部分 |
| 精修全文或一段 | 改善理解，同时核对主体、数字、条件和判断强度 |
| 生成或评价标题 | 检查普通读者理解出的主张能否被正文兑现 |
| 构思配图 | 与正文一致的视觉方案；实际生成由宿主另行执行 |

这是指导 AI 执行任务的文本 Skill。它没有自带模型、联网服务、API 或后台程序，也不需要额外安装其他 Skill。运行仍需支持读取 Skill 的 AI 宿主。不能联网时可处理提供的材料，但不会把外部事实核验记为完成。

## 选择安装方式

| 工具 | 使用哪个包 | 安装方式 |
| --- | --- | --- |
| WorkBuddy | `longform-writing-workflow-workbuddy-v2.0.1.zip` | 技能页面中“添加技能 → 上传技能” |
| Codex | `longform-writing-workflow-v2.0.1.zip`，或仓库里的 Skill 目录 | 复制到项目或用户的 `.agents/skills` |
| 其他支持 `SKILL.md` 的 AI 工具 | 通用包或仓库里的 Skill 目录 | 按宿主的本地 Skill 导入规则操作，保留支持文件 |

方法文本相同，WorkBuddy 包补齐其官方文档中的中文/英文展示字段和示例；通用包保留标准入口与可选的 Codex 显示配置。两者都是独立 Skill，不是 WorkBuddy 专家包。这里只提供 GitHub 下载，不表示已在任何工具的技能市场上架。

### WorkBuddy（国内工具示例）

1. 从 [Releases](https://github.com/ABCLDZ/longform-writing-workflow/releases/latest) 下载名称带 `workbuddy` 的 ZIP，无需下载整个仓库。
2. 打开 WorkBuddy 的“专家·技能·连接器”，选择“技能”。
3. 点击“添加技能 → 上传技能”，选择下载的 ZIP。
4. 在“已安装”中确认长风已启用，新建对话并按下面的通用示例调用。

入口依据 [WorkBuddy 官方使用说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)，包内展示字段依据 [官方 Skill 结构](https://open.workbuddy.cn/docs/skill)，核对日期为 2026-10-26。不同版本界面可能有变化。本版已按文档检查结构，尚未实机完成 WorkBuddy 导入和调用；若导入失败，请记录版本及报错，不把结构检查视为平台验收。

### Codex

下载并解压仓库，或克隆到本地。在**你希望使用它的项目目录**下，将本仓库的 `skills/longform-writing-workflow/` 整个目录复制到：

```text
.agents/skills/longform-writing-workflow/
```

复制后应能看到 `.agents/skills/longform-writing-workflow/SKILL.md`，以及同级的 `references/`、`templates/`、`agents/`。不要只复制入口文件。

需要跨项目使用时，可复制到用户目录 `~/.agents/skills/longform-writing-workflow/`。已有同名目录时先检查差异，避免覆盖自己的修改。Codex 通常自动检测更新，若没有出现可重启。

目录与调用方式依据 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)，核对日期为 2026-10-26。

### 其他支持 Skill 的工具

导入通用包或完整 Skill 目录，保留 `references/` 与 `templates/`；`agents/openai.yaml` 仅供支持它的宿主读取，核心写作方法不依赖该配置。安装成功后通过宿主的技能选择器或对话指定技能。调用符号、加载目录及是否接受 ZIP 由宿主决定，不能把 Codex 的 `$` 语法照搬到所有工具。

本仓库没有逐一验证其他工具。普通聊天网页若不能读取 Skill 目录及其引用文件，不能仅靠粘贴一个名称完成安装。

## 开始使用

在 WorkBuddy 或其他工具中，先选择或启用已安装的 Skill，再输入：

```text
请使用已安装的“长风 / longform-writing-workflow”技能。
把下面的资料写成一篇面向普通从业者的中文文章，给一个标题和完整正文。
资料不足以支持的结论不要补造。
[粘贴资料]
```

Codex 可显式输入：

```text
使用 $longform-writing-workflow。
把下面的资料写成一篇面向普通从业者的中文文章，给一个标题和完整正文。
资料不足以支持的结论不要补造。
[粘贴资料]
```

局部任务也可以直接说：

```text
使用 $longform-writing-workflow，只精修下面这一段。
保留数字、来源、时间、条件和判断强度，只给改稿。
[粘贴段落]
```

不必先填表、提供历史文章或走完全部阶段。更多可复制的虚构材料练习见 [使用示例](examples/quick-start.md)。

## 文件结构

```text
skills/longform-writing-workflow/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── evidence-and-structure.md
│   ├── editing.md
│   ├── titles.md
│   ├── visual-brief.md
│   └── provenance.md
└── templates/work-note.md
```

入口按实际任务读取支持文件；简单任务无需加载全部细则。工作记录模板可按需使用。

## 使用边界

事实核查依赖提供的材料及宿主的检索能力。不同工具、模型与版本的运行表现可能不同；WorkBuddy 安装包按官方文档适配，尚未完成实机导入和调用验证。配图功能提供方案，实际生成图片需要宿主具备相应能力。

## 维护与重新打包

唯一的方法源位于 `skills/longform-writing-workflow/`。修改后可用 Python 3.10+（仅标准库）生成两种 ZIP 及 SHA-256 清单：

```text
python scripts/build_packages.py --output-dir .local/releases
```

WorkBuddy 专用元数据由脚本生成，写作正文及支持文件从同一源目录读取，无需维护两套方法。输出目录不应放在 Skill 源目录内。

## 许可

作者：ABCLDZ。Skill 文本、示例和打包脚本以 [MIT 许可](LICENSE) 提供，允许使用、修改和再分发，包括商业使用。请保留版权与许可声明。
