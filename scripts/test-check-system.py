#!/usr/bin/env python3
"""在独立的临时夹具中验证规则的正常与拒绝分支，不修改项目输入。"""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_system", ROOT / "scripts/check-system.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SystemCheckTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / "_tmp/20261009-init-tests"
        base.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="case-", dir=base)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.fixture(self.root)

    def fixture(self, root, skip=()):
        paths = (*MODULE.REQUIRED, *(f"skills/{name}/SKILL.md" for name in MODULE.SKILLS))
        for relative in paths:
            if relative in skip:
                continue
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)

    def campaign(self, name="20261009-test", register=False, omit=()):
        directory = self.root / "content" / name
        directory.mkdir()
        for filename in MODULE.CAMPAIGN_FILES:
            if filename not in omit:
                (directory / filename).write_text("测试夹具，非实际作品。\n", encoding="utf-8")
        if register:
            path = self.root / ".42cog/cog.md"
            with path.open("a", encoding="utf-8") as stream:
                stream.write(f"\n| 测试投放 | 单次主题投放 | `../content/{name}/` | 测试作者 | 测试渠道的输入 |\n")
        return directory

    def test_healthy(self):
        self.assertEqual(MODULE.check(self.root), [])

    def test_empty_direction(self):
        path = self.root / ".42cog/intent.md"
        path.write_text("## 收敛方向（唯一）\n\n## 不做什么\n\n## 作品区与验证闭环\n\n## 下一步\n", encoding="utf-8")
        self.assertTrue(any("收敛方向为空" in error for error in MODULE.check(self.root)))

    def test_unpinned_python(self):
        (self.root / ".python-version").write_text("3.14\n", encoding="utf-8")
        self.assertTrue(any("精确的 Python" in error for error in MODULE.check(self.root)))

    def test_empty_skill(self):
        (self.root / "skills/mz-proto/SKILL.md").write_text("", encoding="utf-8")
        self.assertTrue(any("frontmatter" in error for error in MODULE.check(self.root)))

    def test_unregistered_campaign(self):
        self.campaign()
        self.assertTrue(any("实体表未登记" in error for error in MODULE.check(self.root)))

    def test_registered_campaign(self):
        self.campaign(register=True)
        self.assertEqual(MODULE.check(self.root), [])

    def test_invalid_campaign_name(self):
        self.campaign(name="test-final", register=True)
        self.assertTrue(any("命名不合规" in error for error in MODULE.check(self.root)))

    def test_empty_campaign_file(self):
        directory = self.campaign(register=True)
        (directory / "core.md").write_text("", encoding="utf-8")
        self.assertTrue(any("非空文件" in error for error in MODULE.check(self.root)))

    def test_reference_in_wrong_column(self):
        self.campaign()
        with (self.root / ".42cog/cog.md").open("a", encoding="utf-8") as stream:
            stream.write("\n| 另一投放 | 说明 | `../content/20261009-other/` | 测试作者 | 引用 content/20261009-test/ |\n")
        self.assertTrue(any("实体表未登记" in error for error in MODULE.check(self.root)))

    def test_duplicate_entity(self):
        self.campaign(register=True)
        with (self.root / ".42cog/cog.md").open("a", encoding="utf-8") as stream:
            stream.write("\n| 重复投放 | 说明 | `../content/20261009-test/` | 测试作者 | 测试渠道 |\n")
        self.assertTrue(any("恰好有一行" in error for error in MODULE.check(self.root)))

    def test_empty_entity_field(self):
        self.campaign()
        with (self.root / ".42cog/cog.md").open("a", encoding="utf-8") as stream:
            stream.write("\n| 测试投放 | 说明 | `../content/20261009-test/` | | 测试渠道 |\n")
        self.assertTrue(any("非空字段" in error for error in MODULE.check(self.root)))

    def test_linked_campaign_file(self):
        directory = self.campaign(register=True, omit=("core.md",))
        target = self.root / "outside.md"
        target.write_text("无敏感信息的测试目标。\n", encoding="utf-8")
        (directory / "core.md").symlink_to(target)
        self.assertTrue(any("软链接" in error for error in MODULE.check(self.root)))

    def test_linked_content_root(self):
        other = self.root / "second-fixture"
        self.fixture(other, skip=("content/README.md",))
        (other / "content").symlink_to(self.root / "content", target_is_directory=True)
        self.assertTrue(any("软链接" in error for error in MODULE.check(other)))

    def test_linked_metadata_file(self):
        other = self.root / "second-fixture"
        self.fixture(other, skip=(".42cog/intent.md",))
        (other / ".42cog/intent.md").symlink_to(self.root / ".42cog/intent.md")
        self.assertTrue(any("软链接" in error for error in MODULE.check(other)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
