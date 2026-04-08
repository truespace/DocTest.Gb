#!/usr/bin/env python3
"""
미분할 파일의 외부 이미지 URL을 로컬로 다운로드하고 경로를 수정합니다.
"""

import re
import ssl
import hashlib
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"


def generate_image_filename(url):
    parsed_name = url.split("/")[-1].split("?")[0]
    if parsed_name and "." in parsed_name:
        return parsed_name
    return f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.png"


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
        print(f"  [WARN] 다운로드 실패: {url} -> {e}")
        return False


def process_file(filepath):
    """파일 내 외부 이미지 URL을 로컬로 변환"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    img_pattern = re.compile(r"!\[([^\]]*)\]\((https?://[^)]+)\)")
    matches = list(img_pattern.finditer(content))

    if not matches:
        return 0

    # 이미지 디렉터리 생성
    image_dir = filepath.parent / "image"
    image_dir.mkdir(exist_ok=True)

    count = 0
    for match in matches:
        alt_text = match.group(1)
        url = match.group(2)

        local_name = generate_image_filename(url)
        dest = image_dir / local_name

        if not dest.exists():
            if download_image(url, dest):
                count += 1
            else:
                continue
        else:
            count += 1

        # URL을 로컬 경로로 변환
        content = content.replace(f"]({url})", f"](./image/{local_name})")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return count


def main():
    print("외부 이미지 로컬 다운로드 시작...")
    total = 0
    files_processed = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        for md_file in sorted(folder.glob("*.md")):
            with open(md_file, "r") as f:
                content = f.read()
            if "https://" not in content and "http://" not in content:
                continue
            if not re.search(r"!\[[^\]]*\]\(https?://", content):
                continue

            count = process_file(md_file)
            if count > 0:
                files_processed += 1
                total += count
                print(f"  {md_file.relative_to(DOCS_DIR)}: {count}개 이미지 로컬화")

    print(f"\n{'='*60}")
    print(f"총 {files_processed}개 파일에서 {total}개 이미지 로컬 다운로드 완료")


if __name__ == "__main__":
    main()
