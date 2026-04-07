#!/usr/bin/env python3
"""
문서 분할 스크립트
DIVIDE_RULES.md 규칙에 따라 마크다운 파일을 분할합니다.
- 20KB 이상: 무조건 분할
- 10KB 이상: 5KB 이하로 나눌 수 있으면 분할
- 5KB 이상: 문단 구조가 나누기 쉬우면 분할 (독립적 섹션이 2개 이상)
- 5KB 미만: 분할하지 않음
"""

import re
import hashlib
import shutil
import urllib.request
import ssl
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).parent
DIVIDED_DIR = BASE_DIR.parent / "docs"
TODAY = date.today().isoformat()
EXCLUDE_FILES = {"DIVIDE_RULES.md", "divide_docs.py", "fix_links.py", "gen_history.py"}

THRESHOLD_MUST = 20 * 1024       # 20KB: 무조건 분할
THRESHOLD_COND = 10 * 1024       # 10KB: 조건부 분할
THRESHOLD_OPT  = 5 * 1024        # 5KB: 선택적 분할
MAX_SECTION_SIZE = 5 * 1024      # 조건부 분할 시 섹션 최대 크기


def get_md_files():
    files = []
    for f in sorted(BASE_DIR.iterdir()):
        if f.suffix == ".md" and f.name not in EXCLUDE_FILES and not f.name.startswith("HISTORY_STRUCTURE"):
            files.append(f)
    return files


def parse_sections_with_hierarchy(content):
    """h2/h3 섹션을 계층 구조로 파싱"""
    lines = content.split("\n")
    result = {'breadcrumb': None, 'preamble_lines': [], 'h2_sections': []}
    in_code_block = False
    current_h2 = None
    current_h3 = None
    breadcrumb_found = False

    def flush_h3():
        nonlocal current_h3
        if current_h3 and current_h2:
            current_h2['h3_sections'].append(current_h3)
            current_h3 = None

    def flush_h2():
        nonlocal current_h2
        flush_h3()
        if current_h2:
            result['h2_sections'].append(current_h2)
            current_h2 = None

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block

        is_h2 = not in_code_block and line.startswith("## ") and not line.startswith("### ")
        is_h3 = not in_code_block and line.startswith("### ") and not line.startswith("#### ")

        if is_h2:
            if not breadcrumb_found and ">" in line:
                breadcrumb_found = True
                result['breadcrumb'] = line
                result['preamble_lines'].append(line)
                continue
            flush_h2()
            h2_name = re.sub(r"^##\s*", "", line).strip()
            current_h2 = {'header': line, 'name': h2_name, 'lines': [line], 'own_lines': [line], 'h3_sections': []}
        elif is_h3:
            if current_h2 is None:
                flush_h2()
                current_h2 = {'header': None, 'name': None, 'lines': [], 'own_lines': [], 'h3_sections': []}
            flush_h3()
            h3_name = re.sub(r"^###\s*", "", line).strip()
            current_h3 = {'header': line, 'name': h3_name, 'lines': [line]}
            current_h2['lines'].append(line)
        else:
            if current_h3:
                current_h3['lines'].append(line)
                if current_h2:
                    current_h2['lines'].append(line)
            elif current_h2:
                current_h2['lines'].append(line)
                current_h2['own_lines'].append(line)
            else:
                result['preamble_lines'].append(line)

    flush_h2()
    return result


def sanitize_name(name):
    name = re.sub(r"[^\w가-힣\s.\-]", "", name)
    name = name.strip().replace(" ", "-")
    name = re.sub(r"-+", "-", name)
    if len(name) > 60:
        name = name[:60].rstrip("-")
    return name


def extract_images(content):
    return re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", content)


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


def generate_image_filename(url):
    parsed_name = url.split("/")[-1].split("?")[0]
    if parsed_name and "." in parsed_name:
        return parsed_name
    return f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.png"


def handle_images(content, filepath, image_dir):
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
    return images_map


def update_image_paths(content, images_map):
    for original_url, local_filename in images_map.items():
        content = content.replace(f"]({original_url})", f"](./image/{local_filename})")
    return content


def fm_index(source_name, source_size, source_chars, split_count):
    return f"""---
source: {source_name}
source_size_bytes: {source_size}
source_char_count: {source_chars}
split_count: {split_count}
created_date: {TODAY}
---
"""


def fm_section(source_name, section_name, order):
    return f"""---
source: {source_name}
section: "{section_name}"
order: {order}
created_date: {TODAY}
---
"""


def decide_split_strategy(parsed, size):
    """분할 전략 결정"""
    h2s = parsed['h2_sections']

    if len(h2s) <= 1:
        if h2s and len(h2s[0]['h3_sections']) > 1:
            return 'h3'
        elif not h2s:
            return 'none'
        if len(h2s[0]['h3_sections']) <= 1:
            return 'none'
        return 'h3'

    # h2가 여러개일 때, 개별 h2가 너무 큰지 확인
    large_h2_count = 0
    for h2 in h2s:
        h2_size = len("\n".join(h2['lines']).encode('utf-8'))
        if h2_size > THRESHOLD_COND and len(h2['h3_sections']) > 1:
            large_h2_count += 1

    if large_h2_count > len(h2s) // 2:
        return 'h3'

    return 'h2'


def build_split_sections(parsed, strategy):
    """전략에 따라 분할 섹션 목록 생성"""
    sections = []
    preamble = parsed['preamble_lines']

    if strategy == 'h2':
        for h2 in parsed['h2_sections']:
            sections.append({'display_name': h2['name'], 'lines': h2['lines']})
    elif strategy == 'h3':
        for h2 in parsed['h2_sections']:
            h2_prefix = h2['name'] if h2['name'] else None
            if h2['h3_sections']:
                for i, h3 in enumerate(h2['h3_sections']):
                    display = f"{h2['name']} > {h3['name']}" if h2_prefix else h3['name']
                    lines = []
                    if i == 0:
                        lines.extend(h2['own_lines'])
                    lines.extend(h3['lines'])
                    sections.append({
                        'display_name': display,
                        'h2_name': h2['name'],
                        'h3_name': h3['name'],
                        'lines': lines,
                    })
            else:
                sections.append({'display_name': h2['name'], 'lines': h2['lines']})

    if sections and preamble:
        sections[0]['lines'] = preamble + sections[0]['lines']

    return sections


def check_conditional_split(sections):
    """10KB 조건부: 모든 섹션이 5KB 이하인지 확인"""
    for sec in sections:
        sec_size = len("\n".join(sec['lines']).encode('utf-8'))
        if sec_size > MAX_SECTION_SIZE:
            return False
    return True


def make_filename(stem, section, strategy):
    """분할 파일명 생성 (헤더 누적 규칙)"""
    if strategy == 'h3' and section.get('h2_name'):
        h2_part = sanitize_name(section['h2_name'])
        h3_part = sanitize_name(section['h3_name'])
        return f"{stem}-{h2_part}-{h3_part}.md"
    else:
        name_part = sanitize_name(section['display_name'])
        return f"{stem}-{name_part}.md"


def create_nosplit(filepath, folder, name, size, chars, reason):
    """미분할 처리: 폴더 생성 + 원본 복사 + index"""
    shutil.copy2(filepath, folder / name)
    # 복사된 파일에 frontmatter 추가
    with open(folder / name, "r", encoding="utf-8") as f:
        original_content = f.read()
    if not original_content.startswith("---"):
        fm = f"""---
source: {name}
split: false
created_date: {TODAY}
---

"""
        with open(folder / name, "w", encoding="utf-8") as f:
            f.write(fm + original_content)

    index_content = fm_index(name, size, chars, 0)
    index_content += f"\n# {filepath.stem}\n\n"
    index_content += "| 순서 | 파일명 | 설명 |\n"
    index_content += "|------|--------|------|\n"
    index_content += f"| 1 | [{name}](./{filepath.stem}/{name}) | 원본 파일 ({reason}) |\n"
    with open(DIVIDED_DIR / name, "w", encoding="utf-8") as f:
        f.write(index_content)


def process_file(filepath):
    stem = filepath.stem
    name = filepath.name
    size = filepath.stat().st_size
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    chars = len(content)

    folder = DIVIDED_DIR / stem
    folder.mkdir(parents=True, exist_ok=True)

    # 분할 여부 판단 (새 3단계 기준)
    parsed = parse_sections_with_hierarchy(content)
    strategy = decide_split_strategy(parsed, size)

    if strategy == 'none':
        reason = "분할 가능 섹션 부족"
        create_nosplit(filepath, folder, name, size, chars, reason)
        return {"name": name, "split": False, "size": size, "chars": chars, "sections": 0, "strategy": "-", "reason": reason}

    sections = build_split_sections(parsed, strategy)

    if len(sections) <= 1:
        reason = "분할 결과 1개"
        create_nosplit(filepath, folder, name, size, chars, reason)
        return {"name": name, "split": False, "size": size, "chars": chars, "sections": 0, "strategy": "-", "reason": reason}

    # 3단계 분할 기준 적용
    if size >= THRESHOLD_MUST:
        # 20KB 이상: 무조건 분할
        do_split = True
        split_reason = "20KB↑ 무조건"
    elif size >= THRESHOLD_COND:
        # 10KB 이상: 5KB 이하로 나눌 수 있으면 분할
        do_split = check_conditional_split(sections)
        split_reason = "10KB↑ 조건부" if do_split else None
    elif size >= THRESHOLD_OPT:
        # 5KB 이상: 독립적 섹션 2개 이상이면 분할
        do_split = len(sections) >= 2
        split_reason = "5KB↑ 선택적" if do_split else None
    else:
        do_split = False
        split_reason = None

    if not do_split:
        reason = f"분할 기준 미충족 ({size // 1024}KB)"
        create_nosplit(filepath, folder, name, size, chars, reason)
        return {"name": name, "split": False, "size": size, "chars": chars, "sections": 0, "strategy": "-", "reason": reason}

    print(f"  -> 전략: {strategy} | {split_reason} | {len(sections)}개 섹션")

    # 이미지 처리
    image_dir = folder / "image"
    image_dir.mkdir(exist_ok=True)
    images_map = handle_images(content, filepath, image_dir)

    # 분할 파일 생성
    split_files_info = []
    for idx, section in enumerate(sections, 1):
        split_filename = make_filename(stem, section, strategy)
        section_content = "\n".join(section["lines"])
        section_content = update_image_paths(section_content, images_map)

        display_name = section.get("display_name", f"Section-{idx}")
        full_content = fm_section(name, display_name, idx)
        full_content += "\n" + section_content.strip() + "\n"

        with open(folder / split_filename, "w", encoding="utf-8") as f:
            f.write(full_content)

        file_size = (folder / split_filename).stat().st_size
        split_files_info.append({
            "order": idx, "filename": split_filename,
            "section": display_name, "size": file_size,
        })

    # 빈 이미지 폴더 삭제
    if image_dir.exists() and not any(image_dir.iterdir()):
        image_dir.rmdir()

    # index 파일 생성
    index_content = fm_index(name, size, chars, len(split_files_info))
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
        "name": name, "split": True, "size": size, "chars": chars,
        "sections": len(split_files_info), "strategy": strategy,
        "reason": split_reason,
    }


def main():
    print("=" * 60)
    print("문서 분할 시작 (새 기준: 20KB/10KB/5KB)")
    print("=" * 60)

    DIVIDED_DIR.mkdir(exist_ok=True)
    results = []

    for filepath in get_md_files():
        size = filepath.stat().st_size
        print(f"\n처리 중: {filepath.name} ({size:,} bytes)")
        result = process_file(filepath)
        results.append(result)
        if result["split"]:
            print(f"  -> {result['sections']}개 분할 완료 [{result['strategy']}]")
        else:
            print(f"  -> 미분할 ({result.get('reason', '')})")

    print(f"\n{'=' * 60}")
    print("분할 결과 요약")
    print("=" * 60)
    split_count = sum(1 for r in results if r["split"])
    nosplit_count = sum(1 for r in results if not r["split"])
    total_sections = sum(r["sections"] for r in results if r["split"])
    print(f"총 파일 수: {len(results)}")
    print(f"분할된 파일: {split_count} ({total_sections}개 섹션)")
    print(f"미분할 파일: {nosplit_count}")


if __name__ == "__main__":
    main()
