"""Regression tests use synthetic fixtures, not live external websites."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_catalog.py"
SPEC = importlib.util.spec_from_file_location("check_catalog", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

BASE = '''# Test
[Section](#section)
<!-- catalog:start -->
<a id="section"></a>
## Section
- [Example](https://github.com/owner/repo) — **开源**。用于测试。
<!-- catalog:end -->
'''


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def check(self, text):
        return MODULE.check_catalog(text, self.root)

    def test_valid(self):
        report = self.check(BASE)
        self.assertTrue(report["ok"], report)
        self.assertEqual(report["resource_count"], 1)
        self.assertEqual(report["category_count"], 1)
        self.assertFalse(report["external_http_checked"])

    def test_duplicate_url(self):
        text = BASE.replace(MODULE.END, '- [Other](https://github.com/OWNER/REPO/) — **开源**。重复。\n' + MODULE.END)
        self.assertIn("duplicate resource URL", " ".join(self.check(text)["errors"]))

    def test_case_sensitive_file_paths(self):
        self.assertNotEqual(MODULE.canonical_url("https://github.com/a/b/blob/main/README.md"), MODULE.canonical_url("https://github.com/a/b/blob/main/readme.md"))

    def test_unknown_type(self):
        self.assertFalse(self.check(BASE.replace("开源", "未经核实"))["ok"])

    def test_empty_description(self):
        self.assertFalse(self.check(BASE.replace("用于测试。", ""))["ok"])

    def test_missing_marker(self):
        self.assertFalse(self.check(BASE.replace(MODULE.START, ""))["ok"])

    def test_repeated_marker(self):
        self.assertFalse(self.check(BASE + MODULE.START)["ok"])

    def test_reversed_markers(self):
        text = BASE.replace(MODULE.START, "TEMP").replace(MODULE.END, MODULE.START).replace("TEMP", MODULE.END)
        self.assertFalse(self.check(text)["ok"])

    def test_empty_category(self):
        text = BASE.replace(MODULE.END, "## Empty\n" + MODULE.END)
        self.assertFalse(self.check(text)["ok"])

    def test_no_entries(self):
        text = "\n".join(line for line in BASE.splitlines() if not line.startswith("- "))
        self.assertFalse(self.check(text)["ok"])

    def test_entry_without_category(self):
        self.assertFalse(self.check(BASE.replace("## Section\n", ""))["ok"])

    def test_missing_anchor(self):
        self.assertFalse(self.check(BASE.replace("](#section)", "](#missing)"))["ok"])

    def test_duplicate_anchor(self):
        self.assertFalse(self.check(BASE + '<a id="section"></a>')["ok"])

    def test_missing_local_file(self):
        self.assertFalse(self.check(BASE + "[Missing](missing.md)")["ok"])

    def test_existing_local_file(self):
        (self.root / "notes.md").write_text("# Notes\n", encoding="utf-8")
        self.assertTrue(self.check(BASE + "[Notes](notes.md)")["ok"])

    def test_local_file_fragment(self):
        (self.root / "notes.md").write_text('<a id="notes"></a>\n', encoding="utf-8")
        self.assertTrue(self.check(BASE + "[Notes](notes.md#notes)")["ok"])
        self.assertFalse(self.check(BASE + "[Notes](notes.md#missing)")["ok"])

    def test_path_traversal(self):
        self.assertFalse(self.check(BASE + "[Outside](../file.md)")["ok"])

    def test_ignore_fenced_examples(self):
        self.assertTrue(self.check(BASE + "\n```md\n[Not a link](missing.md)\n```\n")["ok"])

    def test_require_https(self):
        self.assertFalse(self.check(BASE.replace("https://", "http://"))["ok"])

    def test_reject_embedded_credentials(self):
        self.assertFalse(self.check(BASE.replace("github.com", "user:password@github.com"))["ok"])

    def test_duplicate_category(self):
        text = BASE.replace(MODULE.END, "## Section\n" + MODULE.END)
        self.assertFalse(self.check(text)["ok"])


if __name__ == "__main__":
    unittest.main()
