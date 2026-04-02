# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Gamebase SDK documentation repository** for NHN's game platform. It is a pure Markdown documentation project with no build system, no CI/CD, and no dependencies. Content is written primarily in Korean and maintained across four language directories (`ko/`, `en/`, `ja/`, `zh/`) at the repository root.

The working directory `ko/` contains the Korean documentation. Other language directories mirror the same file structure.

## Repository Structure

All content is Markdown files organized by naming convention:

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
- Images are hosted externally on CDN (`static.toastoven.net` or `kr1-api-object-storage.nhncloudservice.com`), never stored in the repo
- Notes use blockquote syntax: `> [참고]` (Korean for "Note")
- Warnings use: `> [주의]`
- Code blocks use language-specific syntax highlighting (Java, Swift, Objective-C, C#, C++, curl)
- Internal cross-references use relative paths without `.md` extension: `[링크텍스트](./filename)`
- `README.md` is an auto-generated index table with file metadata (size, character count, image count) — not user-facing documentation

## Git Workflow

- Branch hierarchy: `master` <- `release` <- `beta` <- `alpha` <- feature branches
- Feature branches follow pattern: `alpha-client/{date}/{description}`
- Commit messages are typically in Korean
- Content is merged upward through the branch chain

## When Editing Documentation

- Maintain consistent heading hierarchy (`##` as top-level within each file)
- Preserve the breadcrumb-style main heading format: `## Game > Gamebase > ...`
- Keep image URLs pointing to the existing CDN hosts
- When updating platform guides, consider whether parallel changes are needed in other platform files (aos/ios/unity/unreal often have matching sections)
- When updating Korean docs, note that `en/`, `ja/`, `zh/` may need corresponding updates
