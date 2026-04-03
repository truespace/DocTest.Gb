# 문서 분할 규칙
1. 대상 원본 파일의 크기와 문자수를 통해서 파일 분할 여부를 판단한다.
    - 분할 기준: **파일 크기 30KB 이상** 또는 **문자수 15,000자 이상** (둘 중 하나라도 초과 시 분할)
    - 이 기준은 LLM이 단일 문서를 학습할 때 맥락 유지와 집중도가 적절한 크기를 기반으로 한다.
2. 대상 원본이 기준보다 작아도 관리를 위해서 index 파일을 생성한다.
    - index 파일의 이름은 원본 파일의 이름과 동일해야 한다.
    - 이 경우 분할은 하지 않고, index 파일이 원본 파일 1개만 참조하는 형태가 된다.
3. index 파일은 다음과 같은 규칙을 갖는다.
    - index 파일은 원본 파일과 동일한 디렉터리의 하위 `divided/` 폴더에 직접 생성한다.
        - 예: `원본경로/divided/aos-authentication.md`
    - index 파일은 frontmatter를 포함하여 생성하며, 이는 index 파일과 index 파일이 관리하는 분할된 파일들의 정보 변경을 확인하기 위한 용도로 사용된다.
    - index 파일의 내용은 테이블로 관리된다.
    - index 파일에 생성된 분할된 파일을 가리키는 순서는 원본 가이드 문서의 내용 순서와 동일해야 한다.
4. 분할된 파일은 `divided/{기능명}/` 폴더에 생성된다.
    - `{기능명}`은 원본 파일명(확장자 제외)으로 설정한다.
        - 예: `원본경로/divided/aos-authentication/aos-authentication-Login.md`
    - 분할 기준 헤더 레벨:
        - 문서에 h1이 1개뿐인 경우: h2를 기준으로 분할한다.
        - 문서에 h1이 여러 개인 경우: h1을 기준으로 분할한다.
        - h2 기준으로 분할 가능한 섹션이 1개 이하인 경우: h3을 기준으로 폴백한다.
    - 소규모 섹션 그룹핑:
        - 분할 후 개별 섹션이 지나치게 작을 경우 (평균 4,000자 미만 & 10개 초과), 인접 섹션을 그룹핑하여 약 12,000자 단위로 병합한다.
    - 생성된 파일의 이름은 분할 기준 헤더명을 포함하여 설정한다.
        - 예:
            - 원본 파일명 : Gamebase-Authenticated.md
            - 분할 파일명(2개로 분할) :
                - Gamebase-Authenticated-Login.md
                - Gamebase-Authenticated-Logout.md
    - 분할된 파일에는 frontmatter를 포함하여 생성한다.
    - 분할된 파일의 내용은 변경되지 않아야 하며, 파일 분할 시 맥락이 최대한 끊기지 않도록 한다.
5. 분할된 파일에 포함된 링크는 GitHub markdown 파일 preview에서 동작하도록 다음 규칙에 따라 경로를 재조정해야 한다.
    - **타 문서 링크**: 원본 파일 기준 상대경로(`./파일명#anchor`)를 분할 파일 위치 기준으로 변환한다.
        - 변환 규칙: `./파일명#anchor` → `../../파일명.md#anchor`
        - 분할 파일은 `divided/{기능명}/` 하위에 위치하므로 원본 디렉터리까지 2단계 상위(`../../`)로 올라가야 한다.
    - **자기 문서 앵커 링크**: 같은 원본에서 분할된 파일 내 앵커를 참조하는 경우, 해당 앵커가 포함된 분할 파일로 재매핑한다.
        - 변환 규칙: `./원본파일명#anchor` → `./분할파일명.md#anchor`
    - 파일 경로에 `.md` 확장자를 추가해야 한다. (GitHub preview 호환)
6. 문서에 포함된 이미지(외부 URL 및 로컬 경로 모두 포함)는 각 문서가 생성된 하위 `image/` 폴더 안에 복사하며, 이미지 경로는 상대 경로로 재조정되어야 한다. (링크 유효성 확인)
    - 외부 URL 이미지: 다운로드하여 `image/` 폴더에 저장
    - 로컬 이미지: `image/` 폴더로 복사
    - 이미지가 Diagram일 경우에는 mermaid 포맷으로 생성하여 주석을 추가
    - 이미지가 Diagram이 아닐 경우에는 이미지 안의 내용을 확인하여 주석을 추가
7. 분할 작업 후 `divided/` 폴더 구조의 스냅샷을 `HISTORY_STRUCTURE_{날짜}_{시간}.md` 파일로 생성한다.
    - 파일명 형식: `HISTORY_STRUCTURE_YYYYMMDD_HHMMSS.md`
    - 파일 위치: 원본 파일과 동일한 디렉터리 (예: `ko/HISTORY_STRUCTURE_20260403_144621.md`)
    - 파일 내용:
        - frontmatter: 생성일시, 디렉터리/파일 수 등 통계 정보
        - 통계 테이블: 디렉터리, 전체 파일, index 파일, 분할 파일, 이미지 파일 수
        - 폴더 구조: 트리 형태로 `divided/` 하위 전체 구조를 표시 (파일 크기 포함)
    - 분할 작업이 수행될 때마다 새로운 스냅샷 파일을 생성하여 변경 이력을 추적한다.


## 분할 내역

> 최종 분할일: 2026-04-03 | 총 67개 파일 | 분할 34개 (210개 섹션) | index만 33개

### 분할된 파일 (34개)

| 파일명 | 크기 | 문자수 | 분할 수 | 비고 |
|--------|------|--------|---------|------|
| Overview.md | 24,801 bytes | 16,717 chars | 8 | h2 기준 |
| aos-authentication.md | 69,946 bytes | 55,958 chars | 9 | h2 기준 |
| aos-etc.md | 46,396 bytes | 37,159 chars | 7 | h3 폴백 |
| aos-purchase.md | 30,785 bytes | 23,345 chars | 3 | h3 폴백 + 그룹핑 |
| aos-started.md | 33,449 bytes | 28,321 chars | 6 | h2 기준 |
| aos-ui.md | 37,601 bytes | 29,288 chars | 9 | h2 기준 |
| api-guide-v1.0.md | 30,536 bytes | 25,148 chars | 9 | h2 기준 |
| api-guide-v1.2.md | 45,228 bytes | 36,860 chars | 4 | h2 기준 + 그룹핑 |
| api-guide.md | 83,982 bytes | 66,415 chars | 12 | h2 기준 |
| error-code.md | 29,375 bytes | 24,017 chars | 2 | h2 기준 |
| ios-authentication.md | 49,693 bytes | 38,997 chars | 9 | h2 기준 |
| ios-etc.md | 35,016 bytes | 29,186 chars | 7 | h3 폴백 |
| ios-purchase.md | 21,729 bytes | 15,739 chars | 2 | h3 폴백 + 그룹핑 |
| ios-ui.md | 30,840 bytes | 24,984 chars | 8 | h2 기준 |
| oper-app.md | 68,817 bytes | 46,285 chars | 7 | h2 기준 |
| oper-operation.md | 29,969 bytes | 16,067 chars | 5 | h2 기준 |
| oper-purchase.md | 26,176 bytes | 15,062 chars | 5 | h2 기준 |
| release-notes-android.md | 92,084 bytes | 65,174 chars | 6 | h3 폴백 + 그룹핑 |
| release-notes-console.md | 44,888 bytes | 24,984 chars | 3 | h3 폴백 + 그룹핑 |
| release-notes-ios.md | 66,748 bytes | 48,254 chars | 5 | h3 폴백 + 그룹핑 |
| release-notes-unity.md | 88,139 bytes | 65,535 chars | 6 | h3 폴백 + 그룹핑 |
| release-notes-unreal.md | 44,682 bytes | 31,782 chars | 3 | h3 폴백 + 그룹핑 |
| release-notes.md | 72,513 bytes | 46,153 chars | 4 | h3 폴백 + 그룹핑 |
| unity-authentication.md | 63,277 bytes | 51,109 chars | 9 | h2 기준 |
| unity-etc.md | 54,721 bytes | 46,551 chars | 9 | h3 폴백 |
| unity-initialization.md | 20,013 bytes | 15,783 chars | 7 | h3 폴백 |
| unity-purchase.md | 30,648 bytes | 23,444 chars | 2 | h3 폴백 + 그룹핑 |
| unity-ui.md | 29,953 bytes | 24,385 chars | 8 | h2 기준 |
| unreal-authentication.md | 60,710 bytes | 49,398 chars | 9 | h2 기준 |
| unreal-etc.md | 46,990 bytes | 40,058 chars | 9 | h3 폴백 |
| unreal-purchase.md | 31,341 bytes | 24,197 chars | 3 | h3 폴백 + 그룹핑 |
| unreal-started.md | 20,544 bytes | 15,356 chars | 4 | h2 기준 |
| unreal-ui.md | 27,871 bytes | 22,917 chars | 8 | h2 기준 |
| upgrade-guide.md | 47,958 bytes | 34,377 chars | 3 | h2 기준 + 그룹핑 |

### index만 생성된 파일 (33개)

| 파일명 | 크기 | 문자수 |
|--------|------|--------|
| aos-initialization.md | 18,228 bytes | 14,024 chars |
| aos-logger.md | 4,678 bytes | 4,066 chars |
| aos-push.md | 12,885 bytes | 10,425 chars |
| console-amazon-guide.md | 2,753 bytes | 1,783 chars |
| console-apple-guide.md | 5,463 bytes | 3,898 chars |
| console-epicgames-guide.md | 4,730 bytes | 3,148 chars |
| console-for-aws.md | 5,272 bytes | 3,150 chars |
| console-galaxy-guide.md | 879 bytes | 717 chars |
| console-google-guide.md | 19,972 bytes | 12,381 chars |
| console-huawei-guide.md | 4,140 bytes | 2,900 chars |
| console-mycard-guide.md | 1,118 bytes | 664 chars |
| console-onestore-guide.md | 1,188 bytes | 898 chars |
| console-steam-guide.md | 4,463 bytes | 2,819 chars |
| ios-initialization.md | 17,824 bytes | 13,468 chars |
| ios-logger.md | 3,763 bytes | 3,423 chars |
| ios-push.md | 13,129 bytes | 10,935 chars |
| ios-started.md | 17,318 bytes | 13,514 chars |
| oper-analytics.md | 23,384 bytes | 14,198 chars |
| oper-ban.md | 13,201 bytes | 7,385 chars |
| oper-coupon.md | 14,222 bytes | 7,865 chars |
| oper-customer-service.md | 24,287 bytes | 13,445 chars |
| oper-management.md | 6,455 bytes | 3,923 chars |
| oper-member.md | 14,346 bytes | 8,884 chars |
| oper-operating-indicator.md | 4,373 bytes | 2,491 chars |
| oper-push.md | 20,547 bytes | 11,820 chars |
| quick-guide.md | 1,159 bytes | 901 chars |
| release-notes-server-api.md | 4,747 bytes | 3,035 chars |
| unity-logger.md | 8,039 bytes | 7,305 chars |
| unity-push.md | 13,477 bytes | 11,289 chars |
| unity-started.md | 11,500 bytes | 8,830 chars |
| unreal-initialization.md | 13,790 bytes | 11,052 chars |
| unreal-logger.md | 5,169 bytes | 4,647 chars |
| unreal-push.md | 14,598 bytes | 12,412 chars |