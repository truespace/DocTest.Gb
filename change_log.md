# Change Log

> 작업: `ko/` 원본 변경분에 대한 `docs/` 증분 업데이트 (DIVIDE_RULES.md 규칙 기준)
> 작업 일시: 2026-06-16
> Timestamp: `20260616_110448`

---

## 1. 대상 원본 변경 감지 (`ko/` 12개 중 문서 10개)

`.DS_Store`, `DIVIDE_RULES.md` 외 실제 가이드 문서 변경분을 식별하여 대응 분할 파일에만 반영.

| 원본 | 변경 요약 | 처리 |
|------|-----------|------|
| `aos-started.md` | Hangame 어댑터 1.17.3 → 1.17.4 | 분할 파일 인플레이스 수정 |
| `unity-started.md` | Unity 지원 버전 6000.3.10f1 → 6000.3.12f1 | 인플레이스 수정 |
| `ios-started.md` | `#### Game Center` entitlement 항목 추가 | 인플레이스 수정 |
| `api-guide.md` | `변경 사항`에 Push Wrapping 라인 추가, Push 토큰 API 5행 추가 | 인플레이스 수정 |
| `ios-push.md` | 테스트 텍스트/`서버 푸시 제공자` 섹션 삭제, NOT_SUPPORTED 에러행 추가 | 수정 + 분할파일 1개 삭제 |
| `console-galaxy-guide.md` | IAP Public Key/ISN 등 전면 개정 | 본문 교체 + 이미지 3개 신규 |
| `release-notes-android.md` | 2.80.2 / 2.80.1 신규, 2.79.0 문구 수정 | 분할파일 2개 신규 + 1개 수정 |
| `release-notes-ios.md` | 2.81.3 / 2.81.2 / 2.81.1 신규 | 분할파일 3개 신규 |
| `release-notes-unity.md` | 2.81.3 / 2.81.1 신규, 2.81.0 플랫폼별 변경 추가 | 분할파일 2개 신규 + 1개 수정 |
| `upgrade-guide.md` | 2.81.2 신규, 2.80.0 Android 항목 추가 | 분할파일 1개 신규 + 1개 수정 |

## 2. 신규 분할 파일 (8개)

| 파일 | order |
|------|-------|
| `docs/release-notes-android/release-notes-android-2.80.2-2026.-04.-28..md` | 1 |
| `docs/release-notes-android/release-notes-android-2.80.1-2026.-03.-30..md` | 2 |
| `docs/release-notes-ios/release-notes-ios-2.81.3-2026.-05.-27..md` | 1 |
| `docs/release-notes-ios/release-notes-ios-2.81.2-2026.-04.-28..md` | 2 |
| `docs/release-notes-ios/release-notes-ios-2.81.1-2026.-03.-30..md` | 3 |
| `docs/release-notes-unity/release-notes-unity-2.81.3-2026.-05.-27..md` | 1 |
| `docs/release-notes-unity/release-notes-unity-2.81.1-2026.-04.-28..md` | 2 |
| `docs/upgrade-guide/upgrade-guide-2.81.2.md` | 1 |

## 3. 삭제 분할 파일 (1개)

- `docs/ios-push/ios-push-Push-서버-푸시-제공자.md` — 원본에서 `### 서버 푸시 제공자` 섹션이 제거되어 삭제, index에서 행 제거(8→7).

## 4. 순서/breadcrumb 재정렬 (규칙 3)

신규 버전은 원본 순서상 최상단이므로, 각 문서의 기존 분할 파일 `order`를 신규 개수만큼 +시프트하고 index `순서`를 재생성하여 원본 순서와 일치시킴(`rn_update.py`로 결정론 처리). breadcrumb(`## Game > Gamebase > ...`)은 원본 구조상 첫 섹션에만 존재하므로, 신규 최상단 파일로 이동하고 기존 1순위 파일에서는 제거.

| index | 분할 수 변화 | order 범위 검증 |
|-------|--------------|------------------|
| `release-notes-android.md` | 132 → 134 | 1..134 OK |
| `release-notes-ios.md` | 141 → 144 | 1..144 OK |
| `release-notes-unity.md` | 136 → 138 | 1..138 OK |
| `upgrade-guide.md` | 60 → 61 | 1..61 OK |

## 5. 이미지 신규 (3개, console-galaxy-guide)

`docs/console-galaxy-guide/image/`에 다운로드 후 상대경로 참조 + `LLM_Image_DESC` 주석 추가.

| 파일 | 유형 |
|------|------|
| `galaxy_app_kr.png` | Seller Portal 바이너리(Package Name) 화면 |
| `2026_gamebase_galaxy_store_kr.png` | NHN Cloud 콘솔 외부 스토어 연동 입력 폼 |
| `galaxy_isn.png` | In App Purchase 실시간 서버 알림(ISN) 팝업 |

## 6. FrontMatter/Timestamp (규칙 4·5)

- 내용 변경 파일: `created_date_time` → `20260616_110448` 갱신.
- 순서만 시프트된(내용 무변경) 파일: 기존 `created_date_time` 유지.
- keyword: 신규 키워드는 기존 목록 끝에 추가(`console-galaxy-guide`에 IAP/Purchase/ISN, `upgrade-guide-2.80.0`에 Android, `release-notes-unity-2.81.0`에 Epicgames). 순서 변경 없음.

## 7. 히스토리 스냅샷

- `history/HISTORY_STRUCTURE_20260616_111756.md` — 디렉터리 114, 전체 1,544, index 67, 분할 1,055, 이미지 421.

## 8. 검증 결과 (규칙 9)

- ✅ 신규/수정 파일 frontmatter 필수 필드(source/split/created_date_time/keyword/section) 완전
- ✅ console-galaxy 이미지 3개 로컬 존재 + 상대경로 참조 + 주석 3개
- ✅ console-galaxy 미변환 외부 이미지 URL 0건
- ✅ 릴리스 노트 상호 참조 링크 `../release-notes-{plat}.md#anchor` 포맷, 대상 index 존재
- ✅ folder별 breadcrumb 정확히 1개(각 1순위 파일)
- ✅ index `순서` 연속성(1..N) 검증 통과
