# skills · 品牌系统方法

## 四步接力

`mz-init（方向）→ mz-research（依据）→ mz-proto（第一件作品与定标）→ mz-evolve（放量与护栏）`

四步是循环，不是一次走完的流水线。放行判据各住在对应 `SKILL.md`，不在本文件重复。

| 入口 | 使用场景 | 文件 |
|---|---|---|
| `mz-init` | 初始化、接续、核对平台登记 | [SKILL.md](mz-init/SKILL.md) |
| `mz-research` | 选第一个主题、比较渠道、盘点依据 | [SKILL.md](mz-research/SKILL.md) |
| `mz-proto` | 用人的样本定标，再做适配 | [SKILL.md](mz-proto/SKILL.md) |
| `mz-evolve` | 复盘投放、控制维护负担 | [SKILL.md](mz-evolve/SKILL.md) |

常用入口先保持 research 与 proto 两个，init 与 evolve 按需使用。方法草稿已落盘不等于方法已通过跨谱系评审，实际状态见 `../state/board.md`。

## 如何使用

这些是当前项目的方法文件，尚未安装成当前会话的 slash command。可直接说「按 `skills/mz-research/SKILL.md` 分析首个主题」，让 AI 读取后执行；打包安装前不声称 `/mz-research` 已注册。

如果环境已有 `aias-meta-*` 技能，可用它们生成对应步骤的通用骨架，再应用本项目方法的边界与判据，不复制整套通用模板。

## 打包与依赖

- 根 `plugin.json`：本包身份，不代表已发布或已授权开源。
- 根 `42plugin.json`：本项目实际安装的外部插件；目前为空，不把全局可用工具冒充项目依赖。
- 项目上下文引用以项目根为基准；单独拎走一份 SKILL.md 不构成完整方法包。
- 本地校验：`python3 -I scripts/check-manifests.py`、`python3 -I scripts/check-system.py`；有 `42plugin` 时另做 `42plugin __ validate skills/<name>`。
- `.claude/workflows/` 是初始化模板生成的可选编排，不自动运行；没有用户明确的多智能体编排请求时不调用 Workflow。
