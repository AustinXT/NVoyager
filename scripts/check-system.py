#!/usr/bin/env python3
"""只读校验品牌系统骨架、方法入口及投放目录登记，不判定内容质量或发布授权。"""

import re
import sys
from pathlib import Path

SKILLS = ("mz-init", "mz-research", "mz-proto", "mz-evolve")
REQUIRED = (
    "README.md", "CLAUDE.md", ".gitignore", ".python-version",
    "plugin.json", "42plugin.json", "state/board.md", "state/changelog.md",
    ".42cog/intent.md", ".42cog/real.md", ".42cog/cog.md", ".42cog/meta.md",
    "content/README.md", "specs/README.md", "specs/style/README.md",
    "skills/README.md", "scripts/check-tools.sh", "scripts/check-manifests.py",
    "scripts/test-check-system.py",
    ".github/workflows/validate.yml",
)
CAMPAIGN_RE = re.compile(r"[0-9]{8}-[a-z0-9]+(?:-[a-z0-9]+)*")
CAMPAIGN_FILES = ("README.md", "core.md", "sources.md", "review.md")


def check(root: Path) -> list[str]:
    errors = []

    def safe(path: Path) -> bool:
        try:
            relative = path.relative_to(root)
            cursor = root
            for part in relative.parts:
                cursor = cursor / part
                if cursor.is_symlink():
                    errors.append(f"检查输入不可是软链接：{relative}")
                    return False
            if not path.resolve().is_relative_to(root.resolve()):
                errors.append(f"检查输入越出项目范围：{relative}")
                return False
        except (OSError, ValueError) as exc:
            errors.append(f"无法确认路径范围：{path.name}，{exc}")
            return False
        return True

    def text(relative: str) -> str:
        path = root / relative
        if not safe(path) or not path.is_file():
            return ""
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative} 无法读取：{exc}")
            return ""

    for relative in REQUIRED:
        path = root / relative
        if safe(path) and not path.is_file():
            errors.append(f"缺少文件：{relative}")

    version = text(".python-version").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        errors.append(".python-version 必须是精确的 Python 版本号")

    intent = text(".42cog/intent.md")
    section = re.search(r"^## 收敛方向（唯一）\s*\n(.*?)(?=^## |\Z)", intent, re.M | re.S)
    if not section or not section.group(1).strip() or "待 AI 起草" in section.group(1):
        errors.append("意向书的收敛方向为空或仍是初始化占位符")
    for heading in ("## 不做什么", "## 作品区与验证闭环", "## 下一步"):
        if heading not in intent:
            errors.append(f"意向书缺少段落：{heading}")

    for name in SKILLS:
        relative = f"skills/{name}/SKILL.md"
        skill = text(relative)
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", skill, re.S)
        if not frontmatter:
            errors.append(f"{relative} 缺少 frontmatter")
            continue
        fields = frontmatter.group(1)
        if not re.search(rf"^name: {re.escape(name)}\s*$", fields, re.M):
            errors.append(f"{relative} 的 name 与目录名不一致")
        if not re.search(r"^description: \S.+$", fields, re.M):
            errors.append(f"{relative} 缺少非空 description")
        if "## 放行" not in skill:
            errors.append(f"{relative} 缺少放行判据")

    cog = text(".42cog/cog.md")
    content = root / "content"
    if safe(content) and content.is_dir():
        for directory in sorted(content.iterdir()):
            if not safe(directory) or not directory.is_dir():
                continue
            if not CAMPAIGN_RE.fullmatch(directory.name):
                errors.append(f"投放目录命名不合规：content/{directory.name}")
            pointer = f"content/{directory.name}/"
            rows = []
            for line in cog.splitlines():
                if not line.startswith("|"):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) != 5:
                    continue
                location = cells[2].strip("`")
                if location in (pointer, f"../{pointer}"):
                    rows.append(cells)
            if not rows:
                errors.append(f"实体表未登记投放目录：{pointer}")
            elif len(rows) != 1 or not all(rows[0]):
                errors.append(f"投放实体必须恰好有一行，含五个非空字段：{pointer}")
            for filename in CAMPAIGN_FILES:
                path = directory / filename
                if not safe(path):
                    continue
                try:
                    if not path.is_file() or not path.read_bytes().strip():
                        errors.append(f"投放缺少非空文件：{pointer}{filename}")
                except OSError as exc:
                    errors.append(f"投放文件无法读取：{pointer}{filename}，{exc}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = check(root)
    if errors:
        for error in errors:
            print(f"✗ {error}")
        print(f"\n{len(errors)} 个规则错误。")
        return 1
    print("✓ 系统骨架、四步方法与投放目录规则通过；不代表事实、风格或平台接入已验证。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
