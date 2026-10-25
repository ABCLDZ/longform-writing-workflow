#!/usr/bin/env python3
"""Build reproducible generic and WorkBuddy Skill archives (Python 3.10+)."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile


def build(output_dir):
    root = Path(__file__).resolve().parents[1]
    source = root / "skills" / "longform-writing-workflow"
    output_dir = output_dir.resolve()
    if output_dir == source or source in output_dir.parents:
        raise ValueError("Output directory must be outside the Skill source directory")
    text = (source / "SKILL.md").read_text(encoding="utf-8")
    match = re.fullmatch(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not match:
        raise ValueError("Expected YAML frontmatter and a Markdown body")
    header, body = match.groups()
    # Read the small, fixed manifest schema maintained by this repository.
    name = re.search(r"(?m)^name: ([a-z0-9-]+)$", header).group(1)
    version = re.search(r'(?m)^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$', header).group(1)
    author = re.search(r"(?m)^  author: ([A-Za-z0-9-]+)$", header).group(1)
    license_bytes = (root / "LICENSE").read_bytes()
    if (source / "LICENSE").read_bytes() != license_bytes:
        raise ValueError("Root and Skill LICENSE files must match")
    fields = {
        "name": name,
        "display_name": "长风·证据与读者导向写作",
        "display_name_en": "Gale Evidence-led Article Writing",
        "description": "Draft and revise Chinese articles from supplied materials; check evidence, meaning and headline promises.",
        "description_zh": "从主题、资料或已有稿件完成中文文章写作与精修，按证据和读者需要选择结构，检查事实、推理、表达及标题。",
        "description_en": "Draft grounded Chinese articles, preserve meaning during editing, and review headline promises.",
        "examples_zh": ["用这些资料直接写一篇中文文章，不要补造案例。", "只精修这一段，保留数字、条件与判断强度。", "只检查这个标题能否被正文支持。"],
        "examples_en": ["Write a Chinese article from these materials without inventing cases.", "Edit only this passage and preserve its conditions and certainty.", "Review only this headline against the article."],
        "version": version,
        "author": author,
    }
    workbuddy_header = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for variant in ("generic", "workbuddy"):
        suffix = "-workbuddy" if variant == "workbuddy" else ""
        archive = output_dir / f"{name}{suffix}-v{version}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for path in sorted(source.rglob("*")):
                if not path.is_file():
                    continue
                relative = path.relative_to(source).as_posix()
                if relative.startswith("agents/") and variant == "workbuddy":
                    continue
                payload = path.read_bytes()
                if relative == "SKILL.md" and variant == "workbuddy":
                    payload = ("---\n" + workbuddy_header + "\n---\n" + body).encode("utf-8")
                entry = zipfile.ZipInfo(f"{name}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                bundle.writestr(entry, payload)
        outputs.append(archive)
    checksums = "".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in outputs)
    (output_dir / "SHA256SUMS.txt").write_text(checksums, encoding="utf-8", newline="\n")
    return outputs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    for output in build(args.output_dir):
        print(output)
