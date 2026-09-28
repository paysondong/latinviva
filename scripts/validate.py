#!/usr/bin/env python3
"""Validate self-contained skill packages locally; no network or model calls."""

from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    references = 0

    def check(condition, message):
        if not condition:
            errors.append(message)

    for path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "node_modules"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        check(all(line == line.rstrip() for line in text.splitlines()),
              f"{path.relative_to(ROOT)}: trailing whitespace")
        check("[TODO" not in text, f"{path.relative_to(ROOT)}: unfinished scaffold")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            references += 1
            boundary = ROOT
            if path.is_relative_to(ROOT / "skills"):
                boundary = ROOT / "skills" / path.relative_to(ROOT / "skills").parts[0]
            destination = (path.parent / unquote(parsed.path)).resolve()
            check(destination.is_relative_to(boundary),
                  f"{path.relative_to(ROOT)}: reference leaves package: {target}")
            check(destination.is_file(), f"{path.relative_to(ROOT)}: missing reference: {target}")

    catalog = json.loads((ROOT / "catalog/skills.json").read_text(encoding="utf-8"))
    ids = [item["id"] for item in catalog]
    check(len(ids) == len(set(ids)), "catalog: duplicate IDs")
    actual = {entry.parent.name for entry in (ROOT / "skills").glob("*/SKILL.md")}
    check(set(ids) == actual, "catalog and skill directories differ")
    for item in catalog:
        entry = (ROOT / item["entry"]).resolve()
        check(entry.is_relative_to(ROOT / "skills"), f"{item['id']}: entry outside skills")
        check(entry.is_file(), f"{item['id']}: missing entry")
        if not entry.is_file() or not entry.is_relative_to(ROOT / "skills"):
            continue
        text = entry.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        check(frontmatter is not None, f"{item['id']}: missing frontmatter")
        if frontmatter:
            name = re.search(r"^name:\s*(.+)$", frontmatter[1], re.M)
            description = re.search(r"^description:\s*(.+)$", frontmatter[1], re.M)
            check(name is not None and name[1].strip() == item["id"],
                  f"{item['id']}: name mismatch")
            check(description is not None and len(description[1].strip()) > 20,
                  f"{item['id']}: missing description")
        check(item["status"] in {"draft", "released"}, f"{item['id']}: unknown status")
        if item["status"] == "released":
            check(bool(item.get("version")) and bool(item.get("compatibility")),
                  f"{item['id']}: release needs version and tested compatibility")

    # This repository is for skill packages, not website or application source.
    for forbidden in ("design", "website", "frontend", "backend", "dist", "node_modules"):
        check(not (ROOT / forbidden).exists(), f"Unexpected directory in skills repository: {forbidden}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(catalog)} skill packages and {references} local references.")
    print("No model or network calls; host-tool behaviour validation remains separate.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (OSError, ValueError, KeyError) as error:
        print(f"Validation could not finish: {error}", file=sys.stderr)
        sys.exit(1)
