# 既有项目参考 · 只读核查

日期：2026-10-09。范围：初始化模板与工具边界，不是首件选题研究。

## 来源与时效

- 博客本地检出：`/Users/nv/proj.xt.com/05Blog`，origin 与用户提供的博客仓库一致；核查时本地 HEAD 日期为 2026-01-14。
- 公众号关联项目：`/Users/nv/proj.xt.com/github-explorer`，核查时本地 HEAD 日期为 2026-08-09。
- 本次由只读探索核实项目文件，没有执行项目脚本、读取凭据、验证登录态或发布；本地状态不代表远端最新状态。

## 已确认的结构

| 对象 | 文件依据 | 可借鉴之处 |
|---|---|---|
| 博客 | `05Blog/config.toml`、`archetypes/post.md`、`CLAUDE.md` | Markdown 正文，标题、日期、摘要、标签等元数据，中文工作约定 |
| 博客来源标注 | `05Blog/layouts/partials/repost-source.html` | 原创、整理与转载分开记录，保留原文、作者和来源 |
| 博客构建 | `05Blog/.github/workflows/hugo.yml`、`.gitmodules` | Hugo 0.154.5 extended，FixIt 主题子模块；无需把主题 pnpm 工具链引入本项目 |
| 内容组织 | `github-explorer/CLAUDE.md`、`scripts/syndicate/README.md` | 过程与作品分离，核心内容与渠道适配分离，发布记录可追溯 |
| 公众号排版 | `github-explorer/ci/skills/md2wechat/SKILL.md`、`scripts/syndicate/render.py` | 已有 Markdown 排版和 HTML 渲染方法，可作为后续候选能力 |
| 公众号投递 | `github-explorer/scripts/wechat_publish.py`、`.github/workflows/auto-analyze.yml` | 代码含草稿投递，当前 CI 另经远端 runner；实际可用性和远端实现未核实 |
| 关联项目依赖 | `github-explorer/requirements-ci.txt`、`site/package-lock.json` | Python 排版链与 Astro 网站各有依赖管理，不是本项目的默认依赖 |

## 不照搬

- 博客 archetype 默认 `draft: false`；本项目规定默认草稿，避免确认前上线。
- 博客工作手册中的部分栏目与实际目录不同；以当前文件核实事实，不把旧文档描述当成已实现能力。
- 关联项目已有自动提交、投递的 CI；其历史授权不迁移到本项目。
- 博客现有品牌呈现为「夜航星」；用户本次确认的项目身份仍以 `.42cog/meta.md` 为正本，不据旧站名称自动改名，也不自动改旧站。
- 现有发布适配器或依赖文件存在，不证明账号接入仍可用。

## 本项目取舍

采用 Markdown 正本、单次投放单位、来源记录、人工确认和生成／发布分离。初始化只增加 Python 标准库验证，精确版本以 `.python-version` 为准；不安装 Hugo、Astro、Playwright、数据库或发布 SDK。

素材转换、排版、音视频处理只登记可选工具；是否复用具体脚本、是否接通账号与发布，另经 research 及授权确定。
