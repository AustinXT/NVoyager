# 智能时代蛮子

个人品牌内容营销项目，覆盖博客、微信公众号、小红书和 B站。平台身份与关联项目的唯一登记在 [项目身份](.42cog/meta.md)，本仓库负责品牌内容与跨平台协同，不取代既有博客或公众号后台。

## 开始使用

1. 方向与排除项：[意向书](.42cog/intent.md)。方向已由负责人确认，仍会随研究修订。
2. 当前进度、评审门槛与下一步：[状态板](state/board.md)。
3. 四步方法：[skills/README.md](skills/README.md)。方法文件已创建，不等于当前会话已安装同名 slash command，也不等于已通过生产放行。
4. 作品组织：[认知模型](.42cog/cog.md)；产出命名与文件契约：[规约](specs/README.md)。

## 本地检查

```bash
bash scripts/check-tools.sh
python3 -I scripts/check-manifests.py
python3 -I scripts/check-system.py
python3 -I scripts/test-check-system.py
```

只检查、不安装、不发布。Python 精确版本以 `.python-version` 为准，规则脚本仅依赖标准库；最小 CI 位于 `.github/workflows/validate.yml`，只有推送后才可能在远程运行。

可选素材工具已检查命令存在，账号权限、发布接口和关联项目构建并未验证。只读参考结论见 [既有项目参考](docs/research/001_existing-project-reference.md)。

## 六组目录

| 组 | 位置 | 作用 |
|---|---|---|
| 开工手册与规约 | `CLAUDE.md`、`.42cog/`、`specs/`、`.gitignore` | 协议、身份与标准 |
| 真相源与参考 | `vault/{raw,truth}/`、`notes/`、`resources/` | 原始材料、核验事实和只读参考 |
| 脚本与扩展 | `skills/`、`scripts/`、`plugin.json`、`42plugin.json` | 方法与确定性验证 |
| 作品 | `content/` | 一次主题投放一个目录，目前没有作品 |
| 状态与文档 | `state/`、`docs/` | 接续点、研究、评审和里程碑 |
| 过程材料 | `_build/`、`_tmp/`、`_archive/` | 可重建或临时材料，默认不入库 |

`hi.md` 是你为某件作品自由写的意向手稿，想写时自己创建；AI 只读，不代建空模板。日记式手稿可放 `notes/YYYYMMDD.md`。

## 授权与备份

每步先说明、完成后简报。具体放权边界在 `CLAUDE.md`；配置 remote 不等于取得提交、推送、上传草稿或发布授权。

远程地址见项目身份。未提交或未推送的内容没有远程副本；忽略的大媒体、参考材料与过程目录另需备份，即使将来推送也不会自动受保护。空目录不会被 Git 保存，后续按实际需要重建。
