#!/usr/bin/env python3
"""
분할 파일 내 링크 경로 수정 스크립트
- 타 문서 링크: ./파일명#anchor → ../../파일명.md#anchor
- 자기 문서 앵커: 해당 앵커가 포함된 분할 파일로 재매핑
- .md 확장자 추가 (GitHub preview 호환)
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
KO_DIR = BASE_DIR / "ko"
DIVIDED_DIR = BASE_DIR / "docs"

# 원본 파일 목록 수집 (확장자 없는 stem)
ORIGINAL_STEMS = set()
for f in KO_DIR.iterdir():
    if f.suffix == ".md":
        ORIGINAL_STEMS.add(f.stem)


def build_anchor_map():
    """각 분할 폴더별로, 앵커 → 분할파일명 매핑 생성"""
    anchor_map = {}  # { folder_stem: { anchor: split_filename } }

    for folder in DIVIDED_DIR.iterdir():
        if not folder.is_dir():
            continue
        folder_stem = folder.name
        anchor_map[folder_stem] = {}

        for md_file in folder.glob("*.md"):
            # index 파일(원본명과 동일) 제외
            if md_file.stem == folder_stem:
                continue

            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            # 헤더에서 앵커 추출
            for line in content.split("\n"):
                match = re.match(r"^(#{1,6})\s+(.+)$", line)
                if match:
                    header_text = match.group(2).strip()
                    # GitHub 스타일 앵커 생성
                    anchor = header_text.lower()
                    anchor = re.sub(r"[^\w가-힣\s\-]", "", anchor)
                    anchor = anchor.strip().replace(" ", "-")
                    anchor = re.sub(r"-+", "-", anchor)
                    anchor_map[folder_stem][anchor] = md_file.name

    return anchor_map


def fix_links_in_file(filepath, folder_stem, anchor_map):
    """단일 파일의 링크를 수정"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    changes = []

    # Root-relative 경로(/Download/, /TOAST/ 등)를 언어 코드(ko) 포함 절대 URL로 변환
    # 한국어 문서(ko/)만 대상이므로 `ko` 삽입.
    # 판별 기준: 경로의 "첫 번째 세그먼트"가 언어 코드인지 확인 (중간·끝의 언어 코드는 서비스 내부 라우팅)
    # - Download 페이지:  /Download/...          → /ko/Download/...
    # - 가이드 페이지:    /TOAST/ko/toast-sdk/... → /ko/TOAST/ko/toast-sdk/... (언어코드 2번)
    ABS_PATH_PATTERNS = ["/Download/", "/TOAST/", "/Game/", "/Compute/", "/Storage/"]
    BASE_URL = "https://docs.nhncloud.com"
    LANG_CODES = ["ko", "en", "ja"]

    def first_segment_is_lang(path):
        parts = path.strip("/").split("/")
        return bool(parts) and parts[0] in LANG_CODES

    def replace_root_relative(m):
        path = m.group(1)
        if any(path.startswith(p) for p in ABS_PATH_PATTERNS):
            if first_segment_is_lang(path):
                new_url = BASE_URL + path
            else:
                new_url = BASE_URL + "/ko" + path
            changes.append(f"  root상대→절대URL: {path} → {new_url}")
            return f"]({new_url})"
        return m.group(0)

    content = re.sub(
        r"(?<!!)\]\((/[^)#\s]*(?:#[^)]*)?)\)",
        replace_root_relative,
        content,
    )

    # 링크 패턴: [text](./path) or [text](./path#anchor)
    # 이미지 링크 제외 (![으로 시작)
    def replace_link(match):
        full_match = match.group(0)
        prefix = match.group(1)  # ] or !]... 부분은 아래에서 처리
        path = match.group(2)

        # 이미지 링크는 건드리지 않음
        if "![" in full_match[:5]:
            return full_match

        # ./image/ 링크는 건드리지 않음
        if path.startswith("./image/"):
            return full_match

        # 같은 폴더 내 분할 파일 참조는 건드리지 않음 (index 파일의 링크)
        if path.startswith(f"./{folder_stem}-"):
            return full_match

        # ./파일명 또는 ./파일명/ 또는 ./파일명#anchor 패턴 분석
        # 앵커 분리
        if "#" in path:
            file_part, anchor = path.split("#", 1)
        else:
            file_part = path
            anchor = None

        # ./ 제거, 끝의 / 제거
        file_part = file_part.lstrip("./").rstrip("/")

        # 원본 파일인지 확인
        if file_part not in ORIGINAL_STEMS:
            return full_match

        # 자기 문서 앵커인 경우: 분할 파일로 재매핑 시도
        if file_part == folder_stem and anchor:
            folder_anchors = anchor_map.get(folder_stem, {})
            if anchor in folder_anchors:
                target_file = folder_anchors[anchor]
                new_path = f"./{target_file}#{anchor}"
                changes.append(f"  자기참조: {path} → {new_path}")
                return f"]({new_path})"

        # 타 문서 링크: ../파일명.md#anchor (docs/{기능명}/ → docs/ 까지 1단계)
        new_path = f"../{file_part}.md"
        if anchor:
            new_path += f"#{anchor}"

        changes.append(f"  타문서: {path} → {new_path}")
        return f"]({new_path})"

    # 이미지가 아닌 링크만 처리: ](./...) 패턴
    # 이미지 링크는 ![...](...) 형태이므로 ] 앞에 !가 없는 것만 처리
    # 정규식: (?<!\!) 로 이미지 제외
    content = re.sub(
        r"(?<!!)\]\((\./[^)]+)\)",
        lambda m: replace_link_wrapper(m, folder_stem, anchor_map, changes),
        content,
    )

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def replace_link_wrapper(match, folder_stem, anchor_map, changes):
    """링크 교체 래퍼"""
    path = match.group(1)

    # ./image/ 링크는 건드리지 않음
    if path.startswith("./image/"):
        return match.group(0)

    # 같은 폴더 내 분할 파일 참조는 건드리지 않음
    if path.startswith(f"./{folder_stem}-"):
        return match.group(0)

    # 앵커 분리
    if "#" in path:
        file_part, anchor = path.split("#", 1)
    else:
        file_part = path
        anchor = None

    # ./ 제거, 끝의 / 제거
    file_part = file_part.lstrip("./").rstrip("/")

    # 원본 파일인지 확인
    if file_part not in ORIGINAL_STEMS:
        return match.group(0)

    # 자기 문서 앵커인 경우: 분할 파일로 재매핑
    if file_part == folder_stem and anchor:
        folder_anchors = anchor_map.get(folder_stem, {})
        if anchor in folder_anchors:
            target_file = folder_anchors[anchor]
            new_path = f"./{target_file}#{anchor}"
            changes.append(f"  자기참조: {path} → {new_path}")
            return f"]({new_path})"

    # 타 문서 링크: ../파일명.md#anchor (docs/{기능명}/ → docs/ 까지 1단계)
    new_path = f"../{file_part}.md"
    if anchor:
        new_path += f"#{anchor}"

    changes.append(f"  타문서: {path} → {new_path}")
    return f"]({new_path})"


def main():
    print("앵커 맵 생성 중...")
    anchor_map = build_anchor_map()

    total_changes = 0
    files_changed = 0

    for folder in sorted(DIVIDED_DIR.iterdir()):
        if not folder.is_dir():
            continue

        folder_stem = folder.name
        for md_file in sorted(folder.glob("*.md")):
            changes = fix_links_in_file(md_file, folder_stem, anchor_map)
            if changes:
                files_changed += 1
                total_changes += len(changes)
                print(f"\n{md_file.relative_to(DIVIDED_DIR)} ({len(changes)}개 수정)")
                for c in changes[:5]:
                    print(c)
                if len(changes) > 5:
                    print(f"  ... 외 {len(changes) - 5}개")

    print(f"\n{'='*60}")
    print(f"총 {files_changed}개 파일에서 {total_changes}개 링크 수정 완료")


if __name__ == "__main__":
    main()
