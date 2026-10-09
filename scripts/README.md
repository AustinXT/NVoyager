# scripts · 确定性验证

| 命令 | 检查什么 | 不证明什么 |
|---|---|---|
| `bash scripts/check-tools.sh` | 通用工具、专属清单与 Python 精确版本；缺必需项非零退出，可选项单列 | 不安装，不验证登录态或平台可用性 |
| `python3 -I scripts/check-manifests.py` | 插件清单格式与技能布局 | 不安装或发布插件 |
| `python3 -I scripts/check-system.py` | 系统文件、方法 frontmatter、投放命名与实体登记、必备文件 | 不证明内容真实、风格合格、人审通过或获准发布 |
| `python3 -I scripts/test-check-system.py` | 检测脚本的正常及失败分支 | 不替代真实投放验收 |

验证脚本只依赖 Python 标准库；运行时唯一锁定正本为 `../.python-version`。CI 使用该版本，不复制一份版本号。

规则脚本不擅自修改输入；能用规则判对错的事在这里判，内容好坏按意向和人定标判断。执行既有脚本前先审阅其内容。

初始化阶段不复制博客的 Hugo 构建、关联项目的 Astro 站点或公众号发布依赖；既有技术边界见 `../docs/research/001_existing-project-reference.md`。
