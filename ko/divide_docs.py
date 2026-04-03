#!/usr/bin/env python3
"""
문서 분할 스크립트
DIVIDE_RULES.md 규칙에 따라 마크다운 파일을 분할합니다.
- 30KB 이상 또는 15,000자 이상: h2 기준으로 분할 (h2 부족 시 h3 폴백)
- 기준 미만: index 파일만 생성 (원본 1개 참조)
- 소규모 섹션이 다수일 경우 그룹핑하여 분할
"""

import os
import re
import hashlib
import shutil
import urllib.request
import urllib.error
import ssl
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).parent
DIVIDED_DIR = BASE_DIR / "divided"
SIZE_THRESHOLD = 30 * 1024  # 30KB
CHAR_THRESHOLD = 15000
# 분할 후 각 파일의 목표 크기 (그룹핑 기준)
TARGET_CHARS = 12000
TODAY = date.today().isoformat()
EXCLUDE_FILES = {"DIVIDE_RULES.md", "divide_docs.py"}


def get_md_files():
    files = []
    for f in sorted(BASE_DIR.iterdir()):
        if f.suffix == ".md" and f.name not in EXCLUDE_FILES:
            files.append(f)
    return files


def needs_split(filepath):
    size = filepath.stat().st_size
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    char_count = len(content)
    return size >= SIZE_THRESHOLD or char_count >= CHAR_THRESHOLD, size, char_count, content


def parse_sections(content, header_level):
    """지정 헤더 레벨 기준으로 섹션 분리 (코드블록 내부 무시)
    header_level: 2 for ##, 3 for ###
    """
    header_prefix = "#" * header_level + " "
    lines = content.split("\n")
    sections = []
    current_section = {"header": None, "lines": []}
    in_code_block = False
    breadcrumb_found = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block

        is_target_header = (
            not in_code_block
            and line.startswith(header_prefix)
            and not line.startswith(header_prefix + "#")  # ##이 ###에 매치되지 않도록
        )

        if is_target_header:
            # breadcrumb 헤더 감지 (첫 번째 해당 레벨 헤더에 > 포함)
            if not breadcrumb_found and ">" in line:
                breadcrumb_found = True
                current_section["lines"].append(line)
                continue

            # 이전 섹션 저장
            if current_section["header"] is not None or current_section["lines"]:
                sections.append(current_section)
            current_section = {"header": line, "lines": [line]}
        else:
            current_section["lines"].append(line)

    # 마지막 섹션 저장
    if current_section["header"] is not None or current_section["lines"]:
        sections.append(current_section)

    return sections


def group_small_sections(preamble_lines, content_sections, target_chars):
    """소규모 섹션들을 목표 크기에 맞게 그룹핑"""
    if not content_sections:
        return []

    groups = []
    current_group = {
        "sections": [],
        "lines": [],
        "char_count": 0,
        "first_header": None,
        "last_header": None,
    }

    for section in content_sections:
        section_text = "\n".join(section["lines"])
        section_chars = len(section_text)
        header_name = re.sub(r"^#+\s*", "", section["header"] or "")

        # 현재 그룹이 비어있거나 추가해도 목표 이하인 경우
        if (
            current_group["char_count"] == 0
            or current_group["char_count"] + section_chars <= target_chars
        ):
            current_group["sections"].append(section)
            current_group["lines"].extend(section["lines"])
            current_group["char_count"] += section_chars
            if current_group["first_header"] is None:
                current_group["first_header"] = header_name
            current_group["last_header"] = header_name
        else:
            # 현재 그룹 저장, 새 그룹 시작
            groups.append(current_group)
            current_group = {
                "sections": [section],
                "lines": list(section["lines"]),
                "char_count": section_chars,
                "first_header": header_name,
                "last_header": header_name,
            }

    if current_group["sections"]:
        groups.append(current_group)

    # 그룹 이름 생성
    result = []
    for group in groups:
        if group["first_header"] == group["last_header"]:
            group_name = group["first_header"]
        else:
            group_name = f"{group['first_header']}-to-{group['last_header']}"
        result.append({
            "header": group_name,
            "lines": group["lines"],
        })

    return result


def sanitize_filename(name):
    name = re.sub(r"^#+\s*", "", name)
    # 특수문자 제거 (알파벳, 숫자, 한글, 하이픈, 점 허용)
    name = re.sub(r"[^\w가-힣\s.\-]", "", name)
    name = name.strip().replace(" ", "-")
    name = re.sub(r"-+", "-", name)
    # 파일명이 너무 길면 잘라냄
    if len(name) > 80:
        name = name[:80]
    return name


def extract_images(content):
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return re.findall(pattern, content)


def download_image(url, dest_path):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
            with open(dest_path, "wb") as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"  [WARN] 이미지 다운로드 실패: {url} -> {e}")
        return False


def update_image_paths(content, images_map):
    for original_url, local_filename in images_map.items():
        content = content.replace(f"]({original_url})", f"](./image/{local_filename})")
    return content


def generate_image_filename(url):
    parsed_name = url.split("/")[-1].split("?")[0]
    if parsed_name and "." in parsed_name:
        return parsed_name
    ext = ".png"
    hash_val = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"image_{hash_val}{ext}"


def create_frontmatter_index(source_name, source_size, source_chars, split_count):
    return f"""---
source: {source_name}
source_size_bytes: {source_size}
source_char_count: {source_chars}
split_count: {split_count}
created_date: {TODAY}
---
"""


def create_frontmatter_section(source_name, section_name, order):
    return f"""---
source: {source_name}
section: "{section_name}"
order: {order}
created_date: {TODAY}
---
"""


def handle_images(content, filepath, image_dir):
    """이미지 수집, 다운로드, 경로 맵 반환"""
    all_images = extract_images(content)
    images_map = {}
    for alt, url in all_images:
        if url not in images_map:
            local_name = generate_image_filename(url)
            images_map[url] = local_name
            dest = image_dir / local_name
            if not dest.exists():
                if url.startswith("http"):
                    download_image(url, dest)
                else:
                    src = filepath.parent / url
                    if src.exists():
                        shutil.copy2(src, dest)
                    else:
                        print(f"  [WARN] 로컬 이미지 없음: {src}")
    return images_map


def create_index_only(name, size, chars, reason="분할 기준 미만"):
    """index만 생성 (분할 없음) - divided/ 폴더에 직접 생성"""
    index_content = create_frontmatter_index(name, size, chars, 0)
    index_content += f"\n# {Path(name).stem}\n\n"
    index_content += "| 순서 | 파일명 | 설명 |\n"
    index_content += "|------|--------|------|\n"
    index_content += f"| 1 | [{name}](../{name}) | 원본 파일 ({reason}) |\n"
    with open(DIVIDED_DIR / name, "w", encoding="utf-8") as f:
        f.write(index_content)


def process_file(filepath):
    """단일 파일 처리"""
    stem = filepath.stem
    name = filepath.name

    should_split, size, chars, content = needs_split(filepath)

    if not should_split:
        create_index_only(name, size, chars)
        return {"name": name, "split": False, "size": size, "chars": chars, "sections": 0}

    # 분할 파일용 하위 폴더 생성
    folder = DIVIDED_DIR / stem
    folder.mkdir(parents=True, exist_ok=True)

    # h2로 분할 시도
    sections = parse_sections(content, header_level=2)

    # preamble (breadcrumb 등) 분리
    preamble_lines = []
    content_sections = []

    if sections and sections[0]["header"] is None:
        preamble_lines = sections[0]["lines"]
        content_sections = sections[1:]
    else:
        content_sections = sections

    # h2로 분할 불가능한 경우 (1개 이하) -> h3 폴백
    used_level = "h2"
    if len(content_sections) <= 1:
        print(f"  -> h2 섹션 부족 ({len(content_sections)}개), h3으로 폴백")
        sections = parse_sections(content, header_level=3)

        preamble_lines = []
        content_sections = []
        if sections and sections[0]["header"] is None:
            preamble_lines = sections[0]["lines"]
            content_sections = sections[1:]
        else:
            content_sections = sections
        used_level = "h3"

    # 여전히 분할 불가능한 경우
    if len(content_sections) <= 1:
        create_index_only(name, size, chars, reason="분할 가능한 섹션 부족")
        return {"name": name, "split": False, "size": size, "chars": chars, "sections": len(content_sections)}

    # 소규모 섹션이 다수인 경우 그룹핑
    avg_chars = chars // len(content_sections)
    if avg_chars < TARGET_CHARS // 3 and len(content_sections) > 10:
        print(f"  -> 소규모 섹션 {len(content_sections)}개 감지, 그룹핑 적용")
        grouped = group_small_sections(preamble_lines, content_sections, TARGET_CHARS)
        # 그룹핑 결과를 content_sections 형태로 변환
        content_sections = [{"header": f"## {g['header']}", "lines": g["lines"]} for g in grouped]
        print(f"  -> {len(content_sections)}개 그룹으로 병합")

    # 이미지 처리
    image_dir = folder / "image"
    image_dir.mkdir(exist_ok=True)
    images_map = handle_images(content, filepath, image_dir)

    # 분할 파일 생성
    split_files_info = []
    for idx, section in enumerate(content_sections, 1):
        header_text = section["header"] or f"Section-{idx}"
        section_name = sanitize_filename(header_text)
        split_filename = f"{stem}-{section_name}.md"

        section_content = "\n".join(section["lines"])

        # preamble을 첫 번째 섹션에 포함
        if idx == 1 and preamble_lines:
            section_content = "\n".join(preamble_lines) + "\n" + section_content

        # 이미지 경로 업데이트
        section_content = update_image_paths(section_content, images_map)

        # frontmatter + 내용
        header_display = re.sub(r"^#+\s*", "", header_text)
        full_content = create_frontmatter_section(name, header_display, idx)
        full_content += "\n" + section_content.strip() + "\n"

        with open(folder / split_filename, "w", encoding="utf-8") as f:
            f.write(full_content)

        file_size = (folder / split_filename).stat().st_size
        split_files_info.append({
            "order": idx,
            "filename": split_filename,
            "section": header_display,
            "size": file_size,
        })

    # 빈 이미지 폴더 삭제
    if image_dir.exists() and not any(image_dir.iterdir()):
        image_dir.rmdir()

    # index 파일 생성 (divided/ 폴더에 직접)
    index_content = create_frontmatter_index(name, size, chars, len(split_files_info))
    index_content += f"\n# {stem}\n\n"
    index_content += "| 순서 | 파일명 | 섹션명 | 크기 |\n"
    index_content += "|------|--------|--------|------|\n"
    for info in split_files_info:
        index_content += (
            f"| {info['order']} "
            f"| [{info['filename']}](./{stem}/{info['filename']}) "
            f"| {info['section']} "
            f"| {info['size']:,} bytes |\n"
        )

    with open(DIVIDED_DIR / name, "w", encoding="utf-8") as f:
        f.write(index_content)

    return {
        "name": name,
        "split": True,
        "size": size,
        "chars": chars,
        "sections": len(split_files_info),
    }


def main():
    print("=" * 60)
    print("문서 분할 시작")
    print("=" * 60)

    DIVIDED_DIR.mkdir(exist_ok=True)

    files = get_md_files()
    results = []

    for filepath in files:
        should_split, size, chars, _ = needs_split(filepath)
        print(f"\n처리 중: {filepath.name} ({size:,} bytes / {chars:,} chars)")
        if should_split:
            print(f"  -> 분할 대상 (기준 초과)")
        else:
            print(f"  -> index만 생성 (기준 미만)")

        result = process_file(filepath)
        results.append(result)

        if result["split"]:
            print(f"  -> {result['sections']}개 섹션으로 분할 완료")
        else:
            print(f"  -> index 생성 완료 (분할 없음)")

    # 결과 요약
    print("\n" + "=" * 60)
    print("분할 결과 요약")
    print("=" * 60)
    split_count = sum(1 for r in results if r["split"])
    index_only = sum(1 for r in results if not r["split"])
    total_sections = sum(r["sections"] for r in results if r["split"])
    print(f"총 파일 수: {len(results)}")
    print(f"분할된 파일: {split_count} ({total_sections}개 섹션)")
    print(f"index만 생성: {index_only}")

    # 분할 내역 텍스트 생성
    print("\n--- 분할 내역 (DIVIDE_RULES.md 용) ---")
    print("| 파일명 | 크기 | 문자수 | 상태 |")
    print("|--------|------|--------|------|")
    for r in results:
        status = f"분할 ({r['sections']}개)" if r["split"] else "index만"
        print(f"| {r['name']} | {r['size']:,} bytes | {r['chars']:,} chars | {status} |")


if __name__ == "__main__":
    main()
