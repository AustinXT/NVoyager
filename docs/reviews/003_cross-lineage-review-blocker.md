# 跨谱系方法评审 · 可用模型阻塞

日期：2026-10-09。

## 本次授权

用户明确允许使用 OpenCode＋GLM 评审脱敏四步方法及必要规约，不含账号、绝对路径、原始材料或未公开作品，并知悉外部服务可能留存输入。

范围是本次方法评审；不包括安装、改配置、自动切换厂商、平台操作或发布。

## 实际执行

- `opencode --version`：`v2.0.20`。
- `opencode run --help`、`opencode models --help`：核实原生命令与独立服务标志，没有读取认证配置文件。
- `opencode models`：正常退出但没有返回任何模型条目。
- `opencode models --standalone`：同样正常退出，无模型条目；排除仅依据默认后台清单就猜测 GLM 型号。
- 查阅官方 CLI 与模型文档：模型应从实际可用清单选择，不臆造 provider/model ID。

文档来源：
- https://opencode.ai/v2/docs/cli/commands
- https://opencode.ai/v2/docs/models

## 结果与边界

**未执行跨谱系评审。** 当前没有清单中可供选择的 GLM 入口，不能验证现有 GLM 配置可用，也不据此断言 CLI 未安装或用户从未配置过服务。

未运行 `opencode run`，未外发方法材料；未安装工具、修改配置或改用其他厂商。已按「不可用即停止报告」处理。

## 下一步

用户先在 OpenCode 中解决模型入口可用性，或提供可用 GLM provider/model 标识及其可用性确认；后续仍限脱敏方法评审，不默认扩大外发范围。取得实际评审结果、修复 P0／P1／P2 至零后再决定方法放行。

## 后续接续

本文件保留前次限定授权下的阻塞事实，不代表后续模型可用性。用户随后明确授权配置 OpenCode，主选 GLM-5.3[1M]、备选 MiniMax-M3；实际连通性与评审结果见 `004_cross-lineage-method-review.md`。
