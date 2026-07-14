# Change Log

> 작업: `ko/` 원본 변경분에 대한 `docs/` 증분 업데이트 (DIVIDE_RULES.md 규칙 기준)
> 작업 일시: 2026-07-14
> Timestamp: `20260714_114945`

---

## 1. 대상 원본 변경 감지 (`ko/` 6개)

| 원본 | 변경 요약 | 처리 |
|------|-----------|------|
| `quick-guide.md` | **파일 제거(삭제)** | 분할 결과물 삭제하지 않고 **제거 표시** |
| `ios-push.md` | Error Handling 문구/문의 URL 변경 | 인플레이스 수정 |
| `release-notes-android.md` | 2.81.0 (2026.06.23) 신규 | 분할파일 1개 신규 |
| `release-notes-unity.md` | 2.81.4 (2026.07.14) 신규, 2.81.3 문구 수정 | 신규 1개 + 수정 1개 |
| `release-notes-unreal.md` | 2.81.1 (2026.06.23) 신규 | 분할파일 1개 신규 |
| `upgrade-guide.md` | 2.81.4 신규 | 분할파일 1개 신규 |

## 2. 원본 제거 파일 처리 (핵심)

`ko/quick-guide.md`가 원본에서 제거되었으나, **분할 결과물은 삭제하지 않고 "제거됨"으로 표시**하여 이력을 보존.

- `docs/quick-guide/quick-guide.md`
    - frontmatter에 `removed: true`, `removed_date_time: 20260714_114945` 추가, `created_date_time` 갱신
    - 본문 상단에 `> [주의] ... 제거되었습니다 (제거일: 2026-07-14)` 안내 삽입, 기존 내용 유지
- `docs/quick-guide.md` (index)
    - frontmatter `removed: true`/`removed_date_time` 추가
    - 안내 blockquote + 테이블 설명에 `제거됨(2026-07-14)` 표기

## 3. 신규 분할 파일 (4개)

| 파일 | order |
|------|-------|
| `docs/release-notes-android/release-notes-android-2.81.0-2026.-06.-23..md` | 1 |
| `docs/release-notes-unity/release-notes-unity-2.81.4-2026.-07.-14..md` | 1 |
| `docs/release-notes-unreal/release-notes-unreal-2.81.1-2026.-06.-23..md` | 1 |
| `docs/upgrade-guide/upgrade-guide-2.81.4.md` | 1 |

## 4. 순서/breadcrumb 재정렬 (규칙 3)

신규 버전은 원본 최상단이므로 기존 `order`를 +1 시프트하고 index `순서`를 재생성(`rn_update.py`). breadcrumb은 신규 최상단 파일로 이동, 기존 1순위 파일에서 제거.

| index | 분할 수 | order 검증 |
|-------|---------|------------|
| `release-notes-android.md` | 134 → 135 | 1..135 OK |
| `release-notes-unity.md` | 138 → 139 | 1..139 OK |
| `release-notes-unreal.md` | 46 → 47 | 1..47 OK |
| `upgrade-guide.md` | 61 → 62 | 1..62 OK |

## 5. 인플레이스 수정

- `docs/ios-push/ios-push-Error-Handling.md`: NOT_SUPPORTED/EXTERNAL_LIBRARY 문구를 "확인하세요"로, UNKNOWN 오류 안내를 `[고객지원 > 문의하기](https://www.nhncloud.com/kr/support/inquiry)`로 변경. index 크기/timestamp 갱신.
- `docs/release-notes-unity/release-notes-unity-2.81.3-...md`: MacOS→macOS, Log&Crash→Log & Crash Search 등 문구 정정.

## 6. FrontMatter/Timestamp (규칙 4·5)

- 내용 변경/신규 파일: `created_date_time` → `20260714_114945`.
- 순서만 시프트된(내용 무변경) 파일: 기존 `created_date_time` 유지.

## 7. 히스토리 스냅샷

- `history/HISTORY_STRUCTURE_20260714_115327.md` — 디렉터리 114, 전체 1,548, index 67, 분할 1,059, 이미지 421. (제거 파일은 유지되므로 분할 수 감소 없음)

## 8. 검증 결과 (규칙 9)

- ✅ 신규/수정 파일 frontmatter 필수 필드 완전
- ✅ 릴리스 노트 상호 참조 링크 `../release-notes-{plat}.md#anchor` 포맷, 대상 heading/anchor 존재
- ✅ folder별 breadcrumb 정확히 1개(각 1순위 파일)
- ✅ index `순서` 연속성(1..N) 통과
- ✅ quick-guide 제거 표시(index+분할파일) 확인, 파일 미삭제
