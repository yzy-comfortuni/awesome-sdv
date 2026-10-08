#!/usr/bin/env python3
"""Offline checks for this repository's deliberately simple Markdown format."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

TAGS = {"开源", "标准", "文档", "生态", "商业", "清单"}
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"
ENTRY = re.compile(r"^- \[([^\]]+)\]\(([^\s()]+)\) — \*\*([^*]+)\*\*。(.+)$")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s()]+)\)")
ANCHOR = re.compile(r'<a id="([a-z0-9-]+)"></a>')


def without_fences(text: str) -> str:
    """Ignore fenced examples; preserve line numbers for error messages."""
    result: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if fence is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            fence = stripped[0]
            result.append("")
        elif fence and stripped.startswith(fence * 3):
            fence = None
            result.append("")
        else:
            result.append("" if fence else line)
    return "\n".join(result)


def canonical_url(url: str) -> str:
    parts = urlsplit(url)
    path = parts.path.rstrip("/")
    # GitHub owner/repository names are case-insensitive; file paths are not.
    if parts.netloc.lower() == "github.com" and len(path.strip("/").split("/")) <= 2:
        path = path.lower()
    return parts._replace(scheme=parts.scheme.lower(), netloc=parts.netloc.lower(), path=path).geturl()


def check_catalog(text: str, root: Path) -> dict:
    root = root.resolve()
    clean = without_fences(text)
    errors: list[str] = []
    anchors = ANCHOR.findall(clean)
    for anchor, count in Counter(anchors).items():
        if count > 1:
            errors.append(f"duplicate anchor: {anchor}")
    categories: dict[str, int] = {}
    types: Counter[str] = Counter()
    entries: list[dict[str, str]] = []
    seen: set[str] = set()
    if clean.count(START) != 1 or clean.count(END) != 1 or clean.find(START) >= clean.find(END):
        errors.append("catalog markers must occur once, in start/end order")
    else:
        body = clean.split(START, 1)[1].split(END, 1)[0]
        category: str | None = None
        for line in body.splitlines():
            if line.startswith("## "):
                category = line[3:].strip()
                if category in categories:
                    errors.append(f"duplicate category: {category}")
                categories.setdefault(category, 0)
            elif line.startswith("- "):
                match = ENTRY.fullmatch(line)
                if not match:
                    errors.append(f"malformed entry: {line[:100]}")
                    continue
                name, url, tag, description = match.groups()
                if category is None:
                    errors.append(f"entry outside a category: {name}")
                    continue
                parts = urlsplit(url)
                if parts.scheme != "https" or not parts.netloc or parts.username or parts.password:
                    errors.append(f"entry requires a public HTTPS URL: {name}")
                if tag not in TAGS:
                    errors.append(f"unknown type: {tag}")
                if not description.strip():
                    errors.append(f"empty description: {name}")
                key = canonical_url(url)
                if key in seen:
                    errors.append(f"duplicate resource URL: {url}")
                seen.add(key)
                categories[category] += 1
                types[tag] += 1
                entries.append({"name": name, "url": url, "type": tag, "category": category})
        for title, count in categories.items():
            if count == 0:
                errors.append(f"empty category: {title}")
        if not entries:
            errors.append("catalog has no entries")
    for target in LINK.findall(clean):
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            continue
        if not parts.path:
            if unquote(parts.fragment) not in anchors:
                errors.append(f"missing explicit anchor: {target}")
            continue
        path = (root / unquote(parts.path)).resolve()
        if not path.is_relative_to(root):
            errors.append(f"local link escapes repository: {target}")
        elif not path.is_file():
            errors.append(f"missing local file: {target}")
        elif parts.fragment:
            target_anchors = ANCHOR.findall(without_fences(path.read_text(encoding="utf-8")))
            if unquote(parts.fragment) not in target_anchors:
                errors.append(f"missing explicit file anchor: {target}")
    return {
        "ok": not errors,
        "resource_count": len(entries),
        "category_count": len(categories),
        "types": dict(sorted(types.items())),
        "categories": categories,
        "errors": errors,
        "external_http_checked": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true", help="Print the complete JSON result")
    args = parser.parse_args()
    try:
        report = check_catalog((args.root / "README.md").read_text(encoding="utf-8"), args.root)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f"Unable to check catalog: {exc}\n")
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if report["ok"] else "FAIL"
        print(f"{status}: {report['resource_count']} resources; {report['category_count']} categories")
        for error in report["errors"]:
            print(f"ERROR: {error}")
        print("Offline validation only; external HTTP links were not tested.")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
