#!/usr/bin/env python3
"""
링크 수정 v2: 기존 ../../ 경로를 ../ 로 수정하고 추가 문제를 해결합니다.
- ../../파일명.md → ../파일명.md (경로 깊이 수정)
- ((https://...) → (https://...) (괄호 중복 수정)
- 확장자/접두어 누락 보완
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
KO_DIR = BASE_DIR / "ko"

ORIGINAL_STEMS = set()
for f in KO_DIR.iterdir():
    if f.suffix == ".md":
        ORIGINAL_STEMS.add(f.stem)


def fix_file(filepath):
    """단일 파일의 링크 수정"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # 1. ../../파일명.md → ../파일명.md (경로 깊이 수정)
    def fix_depth(m):
        path = m.group(1)
        # 파일명 추출
        fname = path.replace("../../", "")
        new_path = f"../{fname}"
        changes.append(f"  깊이수정: {path} → {new_path}")
        return f"]({new_path})"

    content = re.sub(
        r"\]\(\.\./\.\./([^)]+\.md(?:#[^)]*)?)\)",
        fix_depth,
        content,
    )

    # 2. 괄호 중복 수정: ((https://...) → (https://...)
    def fix_double_paren(m):
        url = m.group(1)
        changes.append(f"  괄호수정: (({url} → ({url}")
        return f"]({url})"

    content = re.sub(
        r"\]\(\((https?://[^)]+)\)",
        fix_double_paren,
        content,
    )

    # 3. 원본 파일명 참조 (접두어/확장자 없음): (ios-started#anchor) → (../ios-started.md#anchor)
    def fix_bare_ref(m):
        full = m.group(0)
        path = m.group(1)

        # 이미 ./ 또는 ../ 로 시작하면 스킵
        if path.startswith("./") or path.startswith("../"):
            return full
        # http/절대경로는 스킵
        if path.startswith("http") or path.startswith("/") or path.startswith("#"):
            return full
        # 이미지 경로는 스킵
        if "image/" in path:
            return full

        # 파일명#앵커 분리
        if "#" in path:
            file_part, anchor = path.split("#", 1)
        else:
            file_part = path
            anchor = None

        file_part = file_part.rstrip("/")

        # 원본 파일명인지 확인
        if file_part in ORIGINAL_STEMS:
            new_path = f"../{file_part}.md"
            if anchor:
                new_path += f"#{anchor}"
            changes.append(f"  참조수정: {path} → {new_path}")
            return f"]({new_path})"

        return full

    # 이미지가 아닌 링크에서만 처리
    content = re.sub(
        r"(?<!!)\]\(([^)]+)\)",
        fix_bare_ref,
        content,
    )

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def main():
    print("링크 수정 v2 시작 (경로 깊이 + 추가 수정)...")
    total_changes = 0
    files_changed = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            changes = fix_file(md_file)
            if changes:
                files_changed += 1
                total_changes += len(changes)
                if len(changes) <= 3:
                    print(f"\n{md_file.relative_to(DOCS_DIR)} ({len(changes)}개)")
                    for c in changes:
                        print(c)
                else:
                    print(f"\n{md_file.relative_to(DOCS_DIR)} ({len(changes)}개)")
                    for c in changes[:3]:
                        print(c)
                    print(f"  ... 외 {len(changes)-3}개")

    print(f"\n{'='*60}")
    print(f"총 {files_changed}개 파일에서 {total_changes}개 링크 수정 완료")


if __name__ == "__main__":
    main()
