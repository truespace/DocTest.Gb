#!/usr/bin/env python3
"""릴리스 노트/버전형 분할 문서의 증분 업데이트 헬퍼.
 - shift: 기존 분할 파일의 frontmatter `order`를 k만큼 증가
 - reindex: docs/{name}/ 하위 파일을 order 순으로 정렬하여 index 재생성
"""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).parent
TS = "20260616_110448"

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm

def shift(name, k):
    k = int(k)
    folder = ROOT / "docs" / name
    for f in folder.glob(f"{name}-*.md"):
        text = f.read_text(encoding="utf-8")
        def repl(m):
            return f"order: {int(m.group(1)) + k}"
        new = re.sub(r"order:\s*(\d+)", repl, text, count=1)
        if new != text:
            f.write_text(new, encoding="utf-8")
    print(f"shifted {name} by {k}")

def reindex(name):
    folder = ROOT / "docs" / name
    src = ROOT / "ko" / f"{name}.md"
    src_bytes = len(src.read_bytes())
    src_chars = len(src.read_text(encoding="utf-8"))
    rows = []
    for f in folder.glob(f"{name}-*.md"):
        text = f.read_text(encoding="utf-8")
        fm = parse_fm(text)
        order = int(fm.get("order", "0"))
        section = fm.get("section", "").strip().strip('"')
        size = len(f.read_bytes())
        rows.append((order, f.name, section, size))
    rows.sort(key=lambda r: r[0])
    out = []
    out.append("---")
    out.append(f"source: {name}.md")
    out.append(f"source_size_bytes: {src_bytes}")
    out.append(f"source_char_count: {src_chars}")
    out.append(f"split_count: {len(rows)}")
    out.append(f"created_date_time: {TS}")
    out.append("---")
    out.append("")
    out.append(f"# {name}")
    out.append("")
    out.append("| 순서 | 파일명 | 섹션명 | 크기 |")
    out.append("|------|--------|--------|------|")
    for order, fname, section, size in rows:
        out.append(f"| {order} | [{fname}](./{name}/{fname}) | {section} | {size:,} bytes |")
    out.append("")
    (ROOT / "docs" / f"{name}.md").write_text("\n".join(out), encoding="utf-8")
    # 연속성 검증
    orders = [r[0] for r in rows]
    assert orders == list(range(1, len(rows) + 1)), f"order 불연속: {orders[:5]}..."
    print(f"reindexed {name}: {len(rows)} files, order 1..{len(rows)} OK")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "shift":
        shift(sys.argv[2], sys.argv[3])
    elif cmd == "reindex":
        reindex(sys.argv[2])
