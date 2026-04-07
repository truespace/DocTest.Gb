#!/usr/bin/env python3
"""HISTORY_STRUCTURE 파일 생성 스크립트"""
import os
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR.parent / "docs"
HISTORY_DIR = BASE_DIR.parent / "history"


def build_tree(root, prefix=""):
    entries = sorted(
        [e for e in root.iterdir() if e.name != ".DS_Store"],
        key=lambda e: (not e.is_dir(), e.name),
    )
    lines = []
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        if entry.is_dir():
            lines.append(f"{prefix}{connector}{entry.name}/")
            extension = "    " if is_last else "│   "
            lines.extend(build_tree(entry, prefix + extension))
        else:
            size = entry.stat().st_size
            if size >= 1024:
                size_str = f"{size / 1024:.1f}KB"
            else:
                size_str = f"{size}B"
            lines.append(f"{prefix}{connector}{entry.name} ({size_str})")
    return lines


def main():
    now = datetime.now()
    filename = f"HISTORY_STRUCTURE_{now.strftime('%Y%m%d_%H%M%S')}.md"

    # 통계
    total_files = 0
    total_dirs = 0
    total_images = 0
    index_files = 0
    split_files = 0

    for root, dirs, files in os.walk(DOCS_DIR):
        dirs[:] = [d for d in dirs if d != ".DS_Store"]
        total_dirs += len(dirs)
        for f in files:
            if f == ".DS_Store":
                continue
            total_files += 1
            fp = Path(root) / f
            if fp.suffix in (".png", ".jpg", ".gif", ".jpeg", ".svg"):
                total_images += 1
            elif fp.parent == DOCS_DIR and fp.suffix == ".md":
                index_files += 1
            elif fp.suffix == ".md":
                split_files += 1

    tree_lines = build_tree(DOCS_DIR)

    content = f"""---
generated_date: "{now.strftime('%Y-%m-%d %H:%M:%S')}"
description: "docs/ 폴더 구조 스냅샷"
total_directories: {total_dirs}
total_files: {total_files}
index_files: {index_files}
split_files: {split_files}
image_files: {total_images}
---

# 문서 분할 구조 스냅샷

> 생성일시: {now.strftime('%Y-%m-%d %H:%M:%S')}

## 통계

| 항목 | 수량 |
|------|------|
| 디렉터리 | {total_dirs} |
| 전체 파일 | {total_files} |
| index 파일 | {index_files} |
| 분할 파일 | {split_files} |
| 이미지 파일 | {total_images} |

## 폴더 구조

```
docs/
{chr(10).join(tree_lines)}
```
"""

    HISTORY_DIR.mkdir(exist_ok=True)
    output_path = HISTORY_DIR / filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"생성 완료: {output_path.name}")
    print(f"  디렉터리: {total_dirs}, 파일: {total_files} (index: {index_files}, 분할: {split_files}, 이미지: {total_images})")


if __name__ == "__main__":
    main()
