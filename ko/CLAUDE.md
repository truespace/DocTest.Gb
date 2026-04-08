# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Gamebase 서비스의 가이드 문서를 작은 단위로 나누어서 관리하도록 만든 **문서 저장소**입니다. 한국어 문서(`ko/`)만을 대상으로 작업하며, 다른 언어의 문서는 사용하지 않습니다. 문서 분리 규칙은 `DIVIDE_RULES.md` 파일을 기준으로 합니다.

## Repository Structure

```
DocTest.Gb/
├── ko/                                    # 원본 문서 (67개 .md + 스크립트)
│   ├── CLAUDE.md
│   ├── DIVIDE_RULES.md                    # 분할 규칙 문서
│   ├── divide_docs.py                     # 분할 스크립트
│   ├── fix_links.py                       # 링크 수정 스크립트
│   ├── gen_history.py                     # 히스토리 생성 스크립트
│   ├── aos-authentication.md              # 원본 가이드 문서들
│   ├── aos-etc.md
│   ├── aos-initialization.md
│   ├── ...                                # (총 67개 원본 .md)
│   └── upgrade-guide.md
│
├── docs/                                  # 분할 결과물 (1,114개 .md + 418개 이미지)
│   ├── aos-authentication.md              # index 파일 (67개)
│   ├── aos-etc.md
│   ├── ...
│   │
│   ├── aos-authentication/                # 분할된 파일 폴더 (46개 분할 + 21개 미분할)
│   │   ├── aos-authentication-Login.md
│   │   ├── aos-authentication-Logout.md
│   │   ├── aos-authentication-Mapping.md
│   │   ├── ...                            # (9개 분할 파일)
│   │   └── image/                         # 이미지 로컬 저장
│   │       ├── login_for_last_logged_in_provider_flow_2.19.0.png
│   │       └── ...
│   │
│   ├── aos-logger/                        # 미분할 예시 (원본 1개만 복사)
│   │   └── aos-logger.md
│   │
│   ├── oper-app/                          # 대형 분할 예시
│   │   ├── oper-app-App.md
│   │   ├── oper-app-Client.md
│   │   ├── ...                            # (7개 분할 파일)
│   │   └── image/                         # (92개 이미지)
│   │
│   └── ...                                # (총 67개 하위 폴더)
│
└── history/                               # 분할 이력 스냅샷
    ├── HISTORY_STRUCTURE_20260403_144621.md
    ├── HISTORY_STRUCTURE_20260406_141859.md
    └── HISTORY_STRUCTURE_20260406_143532.md
```

### File Naming Convention

- **`{platform}-{feature}.md`** — Platform SDK guides (platforms: `aos`, `ios`, `unity`, `unreal`; features: `started`, `authentication`, `initialization`, `purchase`, `push`, `logger`, `ui`, `etc`)
- **`api-guide.md` / `api-guide-v1.x.md`** — Server API reference (versioned)
- **`oper-{feature}.md`** — Console operation guides (analytics, app, purchase, push, coupon, ban, member, etc.)
- **`console-{store}-guide.md`** — Store/platform integration guides (google, apple, amazon, steam, epicgames, etc.)
- **`release-notes-{platform}.md`** — Release notes per platform
- **`error-code.md`** — Comprehensive error code reference
- **`upgrade-guide.md`** — SDK upgrade migration guide

## Markdown Conventions

- Main heading uses `##` (H2), not `#`: `## Game > Gamebase > {Section Title}`
- Subsections use `###` and deeper
- Images in `ko/` (원본) are hosted externally on CDN (`static.toastoven.net` or `kr1-api-object-storage.nhncloudservice.com`)
- Images in `docs/` (분할 결과물) are downloaded to each document's `image/` subfolder and referenced via relative paths
- Notes use blockquote syntax: `> [참고]` (Korean for "Note")
- Warnings use: `> [주의]`
- Code blocks use language-specific syntax highlighting (Java, Swift, Objective-C, C#, C++, curl)
- Internal cross-references use relative paths without `.md` extension: `[링크텍스트](./filename)`

## When Editing Documentation

- 문서 분할/수정 시 반드시 `DIVIDE_RULES.md`의 규칙을 따른다.
- Maintain consistent heading hierarchy (`##` as top-level within each file)
- Preserve the breadcrumb-style main heading format: `## Game > Gamebase > ...`
- In `ko/` (원본): keep image URLs pointing to the existing CDN hosts
- In `docs/` (분할): images must be in local `image/` folders with relative paths
- When updating platform guides, consider whether parallel changes are needed in other platform files (aos/ios/unity/unreal often have matching sections)
