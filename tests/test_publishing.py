# SPDX-License-Identifier: MIT
"""Offline checks for the guide's navigation and attribution assets."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog", ROOT / "scripts/check_catalog.py")
assert SPEC and SPEC.loader
CAT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CAT)
DOCS = ("README.md", "README.en.md", "ATTRIBUTION.md", "CONTRIBUTING.md",
        "docs/START_HERE.md", "docs/MAINTENANCE.md", "docs/PUBLISHING.md")
LEGACY_ANCHORS = set("commercial ecosystem platforms mcu rust autosar virtualization middleware dds vehicle-data networks bus-tools diagnostics modeling simulation verification ota secure-boot orchestration supply-chain safety hmi adas ev related".split())


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class PublishingTests(unittest.TestCase):
    def test_readme_counts_match_catalog(self):
        text = read("README.md")
        result = CAT.check_catalog(text, ROOT)
        self.assertTrue(result["ok"], result)
        counts = re.search(r"\*\*(\d+) 项资源，分为 (\d+) 类\*\*", text)
        self.assertIsNotNone(counts)
        self.assertEqual(tuple(map(int, counts.groups())),
                         (result["resource_count"], result["category_count"]))

    def test_legacy_anchors_preserved(self):
        self.assertTrue(LEGACY_ANCHORS <= set(CAT.ANCHOR.findall(read("README.md"))))

    def test_document_links_resolve(self):
        for doc in DOCS:
            current = ROOT / doc
            for target in CAT.LINK.findall(CAT.without_fences(read(doc))):
                with self.subTest(document=doc, link=target):
                    parts = urlsplit(target)
                    if parts.scheme or parts.netloc:
                        continue
                    path = (current.parent / unquote(parts.path)).resolve() if parts.path else current
                    self.assertTrue(path.is_relative_to(ROOT))
                    self.assertTrue(path.is_file(), str(path))
                    if parts.fragment:
                        anchors = CAT.ANCHOR.findall(CAT.without_fences(path.read_text(encoding="utf-8")))
                        self.assertIn(unquote(parts.fragment), anchors)

    def test_reader_tables_are_two_columns(self):
        for doc in ("README.md", "README.en.md", "docs/START_HERE.md"):
            for line in read(doc).splitlines():
                if line.startswith("|"):
                    self.assertEqual(line.count("|"), 3, (doc, line))

    def test_brand_and_source_are_visible(self):
        for doc in ("README.md", "README.en.md", "ATTRIBUTION.md", "docs/START_HERE.md"):
            self.assertIn("ComfortUni（适宇科技）", read(doc))
        self.assertIn("https://github.com/yzy-comfortuni/awesome-sdv", read("ATTRIBUTION.md"))

    def test_code_license_preserves_original_notice(self):
        data = (ROOT / "LICENSE-CODE").read_bytes()
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        self.assertEqual(blob, "7280964079286233d6e863ad8f74720037acb0f0")
        self.assertEqual(data, (ROOT / "scripts/LICENSE").read_bytes())
        self.assertEqual(data, (ROOT / "tests/LICENSE").read_bytes())

    def test_content_license_and_historical_boundary(self):
        self.assertIn("Creative Commons Attribution 4.0 International Public License", read("LICENSE"))
        self.assertIn("bc4d96068e3d76d61bc59e7d0b73367e2cbfd943", read("ATTRIBUTION.md"))
        self.assertIn("不撤回旧版本材料已经获得的 MIT 授权", read("ATTRIBUTION.md"))

    def test_citation_fields_without_claiming_full_schema_validation(self):
        text = read("CITATION.cff")
        for field in ("cff-version: 1.2.0", "type: dataset", "authors:",
                      "license: CC-BY-4.0", "ComfortUni（适宇科技）"):
            self.assertIn(field, text)
        self.assertNotIn("doi:", text)

    def test_pending_metadata_is_well_formed(self):
        metadata = json.loads(read(".github/repository-metadata.json"))
        self.assertEqual(metadata["repository"], "yzy-comfortuni/awesome-sdv")
        topics = metadata["topics"]
        self.assertLessEqual(len(topics), 20)
        self.assertEqual(len(topics), len(set(topics)))
        for topic in topics:
            self.assertRegex(topic, r"^[a-z0-9-]{1,50}$")
        self.assertLessEqual(len(metadata["description"]), 350)
        self.assertIn("尚未应用", read("docs/PUBLISHING.md"))


if __name__ == "__main__":
    unittest.main()
