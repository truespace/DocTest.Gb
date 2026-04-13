#!/usr/bin/env python3
"""
분할 문서 검증 스크립트
규칙 9에 따라 하이퍼링크, 이미지 경로, 이미지 주석, frontmatter를 검증합니다.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"

# Root-relative 경로 패턴 (원본 사이트 기준 — 절대 URL로 변환 필요, 규칙 6 참조)
ROOT_RELATIVE_PATTERNS = ["/Download/", "/TOAST/", "/Game/", "/Compute/", "/Storage/"]
EXTERNAL_URL_PATTERNS = ["http://", "https://", "mailto:"]

errors = []
warnings = []


def validate_hyperlinks():
    """하이퍼링크 유효성 검증"""
    print("1. 하이퍼링크 유효성 검증...")
    link_pattern = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
    count = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            # 코드블록 내 링크 제외를 위한 처리
            code_block_ranges = []
            for cb_match in re.finditer(r"```[\s\S]*?```", content):
                code_block_ranges.append((cb_match.start(), cb_match.end()))

            def in_code_block(pos):
                for start, end in code_block_ranges:
                    if start <= pos <= end:
                        return True
                return False

            for match in link_pattern.finditer(content):
                # 코드블록 내 링크는 스킵
                if in_code_block(match.start()):
                    continue

                link_text = match.group(1)
                link_path = match.group(2)
                count += 1

                # C++ 람다/콜백 문법 오탐 스킵
                if "const " in link_path or "FGamebase" in link_path or "FString" in link_path:
                    continue

                # 외부 URL은 스킵
                if any(link_path.startswith(p) for p in EXTERNAL_URL_PATTERNS):
                    continue

                # Root-relative 경로는 변환 누락 오류로 기록 (언어 코드 포함 절대 URL로 변환되어 있어야 함)
                if any(link_path.startswith(p) for p in ROOT_RELATIVE_PATTERNS):
                    rel_path = md_file.relative_to(DOCS_DIR)
                    errors.append(f"[root-relative 미변환] {rel_path}: [{link_text}]({link_path}) → https://docs.nhncloud.com/ko{link_path} 로 변환 필요")
                    continue

                # 앵커 전용 링크
                if link_path.startswith("#"):
                    continue

                # 앵커 분리
                if "#" in link_path:
                    file_part = link_path.split("#")[0]
                else:
                    file_part = link_path

                if not file_part:
                    continue

                # 상대 경로 해석
                resolved = (md_file.parent / file_part).resolve()
                if not resolved.exists():
                    rel_path = md_file.relative_to(DOCS_DIR)
                    errors.append(f"[링크 깨짐] {rel_path}: [{link_text}]({link_path}) → 파일 없음: {file_part}")

                # .md 확장자 확인 (파일 링크인 경우)
                if file_part and not file_part.endswith("/") and not file_part.startswith("./image/"):
                    if not file_part.endswith(".md") and "." not in file_part.split("/")[-1]:
                        rel_path = md_file.relative_to(DOCS_DIR)
                        warnings.append(f"[.md 누락] {rel_path}: [{link_text}]({link_path})")

    print(f"   검사한 링크: {count}개")


def validate_image_paths():
    """이미지 경로 유효성 검증"""
    print("2. 이미지 경로 유효성 검증...")
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    count = 0
    broken = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            for match in img_pattern.finditer(content):
                alt_text = match.group(1)
                img_path = match.group(2)
                count += 1

                # 외부 URL은 스킵
                if any(img_path.startswith(p) for p in EXTERNAL_URL_PATTERNS):
                    warnings.append(f"[외부 이미지] {md_file.relative_to(DOCS_DIR)}: {img_path}")
                    continue

                # 상대 경로 해석
                resolved = (md_file.parent / img_path).resolve()
                if not resolved.exists():
                    rel_path = md_file.relative_to(DOCS_DIR)
                    errors.append(f"[이미지 깨짐] {rel_path}: ![{alt_text}]({img_path}) → 파일 없음")
                    broken += 1

    print(f"   검사한 이미지: {count}개, 깨진 이미지: {broken}개")


def validate_image_annotations():
    """이미지 주석 완전성 검증"""
    print("3. 이미지 주석 완전성 검증...")
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    count = 0
    missing = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            matches = list(img_pattern.finditer(content))
            descs = [m.start() for m in re.finditer(r"<!-- LLM_Image_DESC", content)]

            count += len(matches)
            if len(matches) != len(descs):
                rel_path = md_file.relative_to(DOCS_DIR)
                errors.append(f"[주석 누락] {rel_path}: 이미지 {len(matches)}개, 주석 {len(descs)}개")
                missing += len(matches) - len(descs)

    print(f"   검사한 이미지: {count}개, 누락 주석: {missing}개")


def validate_frontmatter():
    """frontmatter 완전성 검증"""
    print("4. frontmatter 완전성 검증...")
    required_fields = ["source", "split", "created_date_time", "keyword"]
    count = 0
    incomplete = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            count += 1
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.startswith("---"):
                rel_path = md_file.relative_to(DOCS_DIR)
                errors.append(f"[frontmatter 없음] {rel_path}")
                incomplete += 1
                continue

            end = content.find("---", 3)
            if end == -1:
                rel_path = md_file.relative_to(DOCS_DIR)
                errors.append(f"[frontmatter 불완전] {rel_path}")
                incomplete += 1
                continue

            fm_text = content[3:end]
            fm_keys = set()
            for line in fm_text.strip().split("\n"):
                if ":" in line:
                    key = line.split(":")[0].strip()
                    fm_keys.add(key)

            missing_fields = [f for f in required_fields if f not in fm_keys]
            if missing_fields:
                rel_path = md_file.relative_to(DOCS_DIR)
                errors.append(f"[필드 누락] {rel_path}: {', '.join(missing_fields)}")
                incomplete += 1

    print(f"   검사한 파일: {count}개, 불완전: {incomplete}개")


def main():
    print("=" * 60)
    print("문서 검증 시작")
    print("=" * 60)

    validate_hyperlinks()
    validate_image_paths()
    validate_image_annotations()
    validate_frontmatter()

    print(f"\n{'=' * 60}")
    print("검증 결과")
    print("=" * 60)

    if errors:
        print(f"\n[오류] {len(errors)}개:")
        for e in errors:
            print(f"  ❌ {e}")
    else:
        print("\n✅ 오류 없음")

    if warnings:
        print(f"\n[경고] {len(warnings)}개:")
        for w in warnings[:20]:
            print(f"  ⚠️  {w}")
        if len(warnings) > 20:
            print(f"  ... 외 {len(warnings) - 20}개")
    else:
        print("\n✅ 경고 없음")

    print(f"\n{'=' * 60}")
    total_issues = len(errors)
    if total_issues == 0:
        print("검증 통과: 모든 항목 정상")
    else:
        print(f"검증 실패: {total_issues}개 오류 발견")

    return total_issues


if __name__ == "__main__":
    import sys
    sys.exit(main())
