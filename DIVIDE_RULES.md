# 문서 분할 규칙

## 사전 수행 단계 (분할 전 확인)

분할 작업 전에 `docs/` 폴더에 기존 분할 결과물이 존재하는지 확인한다. 존재할 경우, 전체 재분할 대신 **변경분만 반영**하는 증분 업데이트를 수행한다.

1. **기존 분할 파일 존재 여부 확인**
    - `docs/` 폴더에 원본 파일에 대응하는 index 파일과 분할 파일이 이미 존재하는지 확인한다.
    - 존재하지 않을 경우: 아래 분할 규칙(규칙 1~)에 따라 신규 분할을 수행한다.
    - 존재할 경우: 아래 증분 업데이트 절차를 따른다.

2. **원본 변경 내용 감지**
    - 원본 문서(`ko/` 폴더)와 기존 분할 파일의 내용을 비교하여 변경된 부분만 식별한다.
    - 변경이 없는 파일은 분할 파일을 그대로 유지한다.

3. **변경분 적용**
    - 변경된 내용만 대상 분할 파일에 반영한다.
    - 분할 파일의 기존 구조(파일명, 순서, 이미지 주석 등)는 변경이 필요한 부분 외에는 유지한다.

4. **Timestamp 처리**
    - 내용이 변경된 파일: `created_date_time`을 현재 시각으로 갱신한다.
    - 내용이 변경되지 않은 파일: 기존 `created_date_time`을 유지한다.

5. **FrontMatter 반영**
    - 변경된 내용이 frontmatter 항목에 영향을 줄 경우에만 해당 항목을 갱신한다.
        - 새로운 키워드가 추가되어야 할 경우: 기존 keyword 목록 끝에 추가한다.
        - 더 이상 해당하지 않는 키워드가 있을 경우: 해당 키워드를 삭제한다.
        - **keyword의 기존 순서는 변경하지 않는다.**
    - `source`, `section`, `order`, `split` 등 구조적 필드는 원본의 구조가 변경된 경우에만 갱신한다.

---

## 분할 규칙

1. 대상 원본 파일의 크기와 문자수를 통해서 파일 분할 여부를 판단한다.
    - 분할 기준: 
        - **파일 크기 20KB 이상**: 무조건 나누어야함.
        - **파일 크기 10KB 이상**: 5KB 이하로 header통해서 나눌 수 있다면 나누어야함.
        - **파일 크기 5KB 이상**: 나누지 않아도 되나, 문서의 문단 구조가 나누기 쉬운 구조(기능의 내용이 연결성이 없는 경우)라면 나누는 것을 추천. 
    - 이 기준은 LLM이 단일 문서를 학습할 때 맥락 유지와 집중도가 적절한 크기를 기반으로 한다.
2. 대상 원본이 기준보다 작아도 관리를 위해서 index 파일을 생성한다.
    - index 파일의 이름은 원본 파일의 이름과 동일해야 하며, frontmatter를 포함해야한다.
    - 이 경우 분할은 하지 않고, index 파일이 분할 대상이 되는 파일 처럼 폴더를 만들고 동일한 구조로 복사한 후 참조하는 형태가 된다.
    - 분할되지 않더라도 frontmatter를 포함하여 생성한다.
3. index 파일은 다음과 같은 규칙을 갖는다.
    - index 파일은 프로젝트 루트의 `docs/` 폴더에 직접 생성한다.
        - 예: `docs/aos-authentication.md`
    - index 파일은 frontmatter를 포함하여 생성하며, 이는 index 파일과 index 파일이 관리하는 분할된 파일들의 정보 변경을 확인하기 위한 용도로 사용된다.
    - index 파일의 내용은 테이블로 관리된다.
    - index 파일에 생성된 분할된 파일을 가리키는 순서는 원본 가이드 문서의 내용 순서와 동일해야 한다.
4. 분할된 파일은 `docs/{기능명}/` 폴더에 생성된다.
    - `{기능명}`은 원본 파일명(확장자 제외)으로 설정한다.
        - 예: `docs/aos-authentication/aos-authentication-Login.md`
    - 분할 기준 헤더 레벨:
        - 문서에 h1이 1개뿐인 경우: h2를 기준으로 분할한다.
        - 문서에 h1이 여러 개인 경우: h1을 기준으로 분할한다.
        - 문서에 h2사이즈가 크고, h3를 많이 포함하고 있는 경우, h3를 기준으로 분할한다.
        - 나뉘어진 문서는 나뉘어진 기준의 "기능명"을 사용해서, 나뉘어진 파일에 `-{기능명}`을 누적해서 붙인다.
            - 예) 나눌 파일명: "a.md", h1.기능명: "f1", h2.기능명: "f2", h3.기능명: "f3"
                - h1. 로 나뉜경우 : "a-f1.md"
                - h2. 로 나뉜경우 : "a-f1-f2.md"
                - h3. 로 나뉜경우 : "a-f1-f2-f3.md"
    - 생성된 파일의 이름은 분할 기준 헤더명을 포함하여 설정한다.
        - 예:
            - 원본 파일명 : Gamebase-Authenticated.md
            - 분할 파일명(2개로 분할) :
                - Gamebase-Authenticated-Login.md
                - Gamebase-Authenticated-Logout.md
    - 분할된 파일에는 frontmatter를 포함하여 생성한다.
    - 분할된 파일의 내용은 변경되지 않아야 하며, 파일 분할 시 맥락이 최대한 끊기지 않도록 한다.

5. frontmatter 에는 공통적으로 다음과 같은 항목을 포함한다.
    - source : 원본 파일명
    - split: 분할여부(분할:true, 미분할:false)
    - created_date_time: {YYYYMMDD_HHMMSS}
    - keyword: 문서의 내용을 기반으로 다음 카테고리에서 해당하는 항목을 한 단어 단위로 추출하여 설정한다. 모든 문서에 공통되는 내용(가이드, SDK 사용 가이드 등)은 제외한다.
        - **플랫폼/OS**: Android, iOS, Unity, Unreal, Console 등
        - **개발환경**: Gradle, CocoaPods, XCode, Java, Kotlin, Swift, C++, C# 등
        - **Gamebase 기능**: Login, Logout, Mapping, Withdraw, Purchase, Consume, Push, WebView, Alert, Analytics, Logger, Initialize 등
        - **세부 API명**: LoginForLastLoggedInProvider, RequestPurchase, ShowTermsView 등
        - **릴리스 노트**: 버전(v2.6.0 등), 변경유형(신규, 버그수정, 기능개선 등)
        - keyword는 쉼표(`,`)로 구분하며, 문서 1개당 최소 3개 ~ 최대 10개로 설정한다.
6. 분할된 파일에 포함된 링크는 GitHub markdown 파일 preview에서 동작하도록 다음 규칙에 따라 경로를 재조정해야 한다.
    - **타 문서 링크**: 원본 파일 기준 상대경로(`./파일명#anchor`)를 분할 파일 위치 기준으로 변환한다.
        - 변환 규칙: `./파일명#anchor` → `../../파일명.md#anchor`
        - 분할 파일은 `docs/{기능명}/` 하위에 위치하므로 원본 디렉터리까지 2단계 상위(`../../`)로 올라가야 한다.
    - **자기 문서 앵커 링크**: 같은 원본에서 분할된 파일 내 앵커를 참조하는 경우, 해당 앵커가 포함된 분할 파일로 재매핑한다.
        - 변환 규칙: `./원본파일명#anchor` → `./분할파일명.md#anchor`
    - 파일 경로에 `.md` 확장자를 추가해야 한다. (GitHub preview 호환)
    - **Root-relative 링크 변환**: 원본에서 `/`로 시작하는 링크는 사실상 원본 사이트(`docs.nhncloud.com`)의 root-relative URL이다. 분할 파일은 원본 사이트 컨텍스트를 벗어나므로, GitHub preview 등 외부 환경에서 정상 동작하도록 절대 URL로 변환해야 한다. 본 프로젝트는 한국어 문서(`ko/`)만 대상으로 하므로 언어 코드 `ko`를 삽입한다.
        - **판별 기준**: URL 경로의 **첫 번째 세그먼트**가 언어 코드(`ko`, `en`, `ja`)인지 확인한다. 첫 세그먼트가 언어 코드가 아니면 `/ko/`를 prefix로 추가한다. (경로 중간·끝의 언어 코드는 서비스 내부 라우팅이므로 prefix 생략 근거가 되지 않는다)
        - **Download 페이지 포맷**: `docs.nhncloud.com/{언어코드}/Download/{anchor}`
            - 변환: `/Download/#game-gamebase` → `https://docs.nhncloud.com/ko/Download/#game-gamebase`
        - **가이드 페이지 포맷**: `docs.nhncloud.com/{언어코드}/{서비스카테고리}/{서비스명}/{언어코드}/페이지명`
            - 가이드 페이지는 **언어 코드가 경로에 2번** 등장한다 (앞: 사이트 언어, 중간: 서비스 내부 언어).
            - 변환: `/TOAST/ko/toast-sdk/push-android/#firebase-cloud-messaging` → `https://docs.nhncloud.com/ko/TOAST/ko/toast-sdk/push-android/#firebase-cloud-messaging`
            - 이미 첫 세그먼트에 언어코드가 있는 경우(예: `/ko/Game/Gamebase/ko/Overview/`)는 그대로 유지한다.
        - 대상 경로 패턴: `/Download/`, `/TOAST/`, `/Game/`, `/Compute/`, `/Storage/` 등 `/`로 시작하는 사이트 내부 절대경로
        - 이유: root-relative 링크(`/`로 시작)는 GitHub preview에서 `github.com/Download/...`로 해석되어 404가 발생한다. 언어 코드를 포함한 절대 URL로 변환해야 원본 사이트로 올바르게 이동한다.
7. 문서에 포함된 이미지(외부 URL 및 로컬 경로 모두 포함)는 분할/미분할 여부에 관계없이 각 문서가 생성된 하위 `image/` 폴더 안에 복사하며, 이미지 경로는 상대 경로로 재조정되어야 한다. (링크 유효성 확인)
    - 외부 URL 이미지: 다운로드하여 `image/` 폴더에 저장
    - 로컬 이미지: `image/` 폴더로 복사
    - 이미지가 Diagram일 경우에는 mermaid 포맷으로 생성하여 주석을 추가
    - 이미지가 Diagram이 아닐 경우에는 이미지 안의 내용을 확인하여 주석을 추가
    - 주석의 추가는 이미지 링크 마크다운 아래에 다음과 같은 방식을 사용
        ```
        <!-- LLM_Image_DESC_{Timestamp}
            유형: {이미지의 유형}
            내용: {이미지가 어떤 내용을 포함하는지 간단요약}
            구성: {상세 내용 기술}
            Keyword: {검색을 위한 키워드 등록. ','로 구분}
        -->
        ```
8. 분할 작업 후 프로젝트 루트의 `history/` 폴더에 구조 스냅샷을 `HISTORY_STRUCTURE_{날짜}_{시간}.md` 파일로 생성한다.
    - 파일명 형식: `HISTORY_STRUCTURE_YYYYMMDD_HHMMSS.md`
    - 파일 위치: `history/` 폴더에 생성 (없으면 폴더 생성) (예: `history/HISTORY_STRUCTURE_20260403_144621.md`)
    - 파일 내용:
        - frontmatter: 생성일시, 디렉터리/파일 수 등 통계 정보
        - 통계 테이블: 디렉터리, 전체 파일, index 파일, 분할 파일, 이미지 파일 수
        - 폴더 구조: 트리 형태로 `docs/` 하위 전체 구조를 표시 (파일 크기 포함)
    - 분할 작업이 수행될 때마다 새로운 스냅샷 파일을 생성하여 변경 이력을 추적한다.
9. 분할 작업 완료 후 다음 항목에 대해 검증을 수행한다.
    - **하이퍼링크 유효성**: 모든 내부 상대경로 링크(`[text](path)`)가 실제 파일을 가리키는지 확인한다.
        - 분할 파일은 `docs/{기능명}/` 하위에 위치하므로, 같은 docs 내 다른 index 파일 참조 시 `../파일명.md#anchor` 형태여야 한다.
        - Root-relative 경로(`/Download/`, `/TOAST/` 등)가 남아있는 경우, 규칙 6에 따라 `https://docs.nhncloud.com/...` 절대 URL로 변환되었는지 확인한다.
        - `.md` 확장자 누락, 상대경로 깊이 오류(`../../` vs `../`) 등을 점검한다.
    - **이미지 경로 유효성**: 로컬 이미지 링크(`![alt](path)`)가 실제 파일을 가리키는지 확인한다.
    - **이미지 주석 완전성**: 모든 이미지 링크 하위에 `LLM_Image_DESC` 주석이 존재하는지 확인한다.
        - 누락된 경우 규칙 7의 주석 포맷에 따라 추가한다.
    - **frontmatter 완전성**: 모든 파일에 규칙 5의 필수 필드(`source`, `split`, `created_date_time`, `keyword`)가 포함되어 있는지 확인한다.
    - 검증 결과는 분할 작업 로그에 기록하며, 오류가 발견되면 즉시 수정한다.


## 분할 내역

> 최종 분할일: 2026-04-06 | 총 67개 파일 | 분할 46개 (1,026개 섹션) | 미분할 21개

### 분할된 파일 (46개)

| 파일명 | 크기 | 분할 수 | 전략 | 기준 |
|--------|------|---------|------|------|
| Overview.md | 24.2KB | 8 | h2 | 20KB↑ 무조건 |
| aos-authentication.md | 68.3KB | 9 | h2 | 20KB↑ 무조건 |
| aos-etc.md | 45.3KB | 7 | h3 | 20KB↑ 무조건 |
| aos-purchase.md | 30.1KB | 11 | h3 | 20KB↑ 무조건 |
| aos-push.md | 12.6KB | 6 | h3 | 10KB↑ 조건부 |
| aos-started.md | 32.7KB | 6 | h2 | 20KB↑ 무조건 |
| aos-ui.md | 36.7KB | 9 | h2 | 20KB↑ 무조건 |
| api-guide-v1.0.md | 29.8KB | 9 | h2 | 20KB↑ 무조건 |
| api-guide-v1.2.md | 44.2KB | 11 | h2 | 20KB↑ 무조건 |
| api-guide.md | 82.0KB | 12 | h2 | 20KB↑ 무조건 |
| console-apple-guide.md | 5.3KB | 4 | h2 | 5KB↑ 선택적 |
| console-for-aws.md | 5.1KB | 3 | h2 | 5KB↑ 선택적 |
| error-code.md | 28.7KB | 2 | h2 | 20KB↑ 무조건 |
| ios-authentication.md | 48.5KB | 9 | h2 | 20KB↑ 무조건 |
| ios-etc.md | 34.2KB | 7 | h3 | 20KB↑ 무조건 |
| ios-purchase.md | 21.2KB | 12 | h3 | 20KB↑ 무조건 |
| ios-push.md | 12.8KB | 7 | h3 | 10KB↑ 조건부 |
| ios-ui.md | 30.1KB | 8 | h2 | 20KB↑ 무조건 |
| oper-analytics.md | 22.8KB | 5 | h2 | 20KB↑ 무조건 |
| oper-app.md | 67.2KB | 7 | h2 | 20KB↑ 무조건 |
| oper-customer-service.md | 23.7KB | 6 | h2 | 20KB↑ 무조건 |
| oper-management.md | 6.3KB | 3 | h2 | 5KB↑ 선택적 |
| oper-operation.md | 29.3KB | 5 | h2 | 20KB↑ 무조건 |
| oper-purchase.md | 25.6KB | 5 | h2 | 20KB↑ 무조건 |
| oper-push.md | 20.1KB | 6 | h2 | 20KB↑ 무조건 |
| release-notes-android.md | 89.9KB | 132 | h3 | 20KB↑ 무조건 |
| release-notes-console.md | 43.8KB | 129 | h3 | 20KB↑ 무조건 |
| release-notes-ios.md | 65.2KB | 141 | h3 | 20KB↑ 무조건 |
| release-notes-unity.md | 86.1KB | 136 | h3 | 20KB↑ 무조건 |
| release-notes-unreal.md | 43.6KB | 46 | h3 | 20KB↑ 무조건 |
| release-notes.md | 70.8KB | 97 | h3 | 20KB↑ 무조건 |
| unity-authentication.md | 61.8KB | 9 | h2 | 20KB↑ 무조건 |
| unity-etc.md | 53.4KB | 9 | h3 | 20KB↑ 무조건 |
| unity-logger.md | 7.9KB | 6 | h3 | 5KB↑ 선택적 |
| unity-purchase.md | 29.9KB | 11 | h3 | 20KB↑ 무조건 |
| unity-push.md | 13.2KB | 6 | h3 | 10KB↑ 조건부 |
| unity-ui.md | 29.2KB | 8 | h2 | 20KB↑ 무조건 |
| unreal-authentication.md | 59.3KB | 9 | h2 | 20KB↑ 무조건 |
| unreal-etc.md | 45.9KB | 9 | h3 | 20KB↑ 무조건 |
| unreal-initialization.md | 13.5KB | 7 | h3 | 10KB↑ 조건부 |
| unreal-logger.md | 5.0KB | 5 | h3 | 5KB↑ 선택적 |
| unreal-purchase.md | 30.6KB | 11 | h3 | 20KB↑ 무조건 |
| unreal-push.md | 14.3KB | 6 | h3 | 10KB↑ 조건부 |
| unreal-started.md | 20.1KB | 4 | h2 | 20KB↑ 무조건 |
| unreal-ui.md | 27.2KB | 8 | h2 | 20KB↑ 무조건 |
| upgrade-guide.md | 46.8KB | 60 | h2 | 20KB↑ 무조건 |

### 미분할 파일 (21개)

| 파일명 | 크기 | 미분할 사유 |
|--------|------|-------------|
| aos-initialization.md | 17.8KB | 10~20KB, 5KB이하 분할 불가 |
| aos-logger.md | 4.6KB | 5KB 미만 |
| console-amazon-guide.md | 2.7KB | 5KB 미만 |
| console-epicgames-guide.md | 4.6KB | 5KB 미만 |
| console-galaxy-guide.md | 0.9KB | 5KB 미만 |
| console-google-guide.md | 19.5KB | 10~20KB, 5KB이하 분할 불가 |
| console-huawei-guide.md | 4.0KB | 5KB 미만 |
| console-mycard-guide.md | 1.1KB | 섹션 부족 |
| console-onestore-guide.md | 1.2KB | 섹션 부족 |
| console-steam-guide.md | 4.4KB | 5KB 미만 |
| ios-initialization.md | 17.4KB | 10~20KB, 5KB이하 분할 불가 |
| ios-logger.md | 3.7KB | 5KB 미만 |
| ios-started.md | 16.9KB | 10~20KB, 5KB이하 분할 불가 |
| oper-ban.md | 12.9KB | 10~20KB, 5KB이하 분할 불가 |
| oper-coupon.md | 13.9KB | 10~20KB, 5KB이하 분할 불가 |
| oper-member.md | 14.0KB | 10~20KB, 5KB이하 분할 불가 |
| oper-operating-indicator.md | 4.3KB | 5KB 미만 |
| quick-guide.md | 1.1KB | 5KB 미만 |
| release-notes-server-api.md | 4.6KB | 5KB 미만 |
| unity-initialization.md | 19.5KB | 10~20KB, 5KB이하 분할 불가 |
| unity-started.md | 11.2KB | 10~20KB, 5KB이하 분할 불가 |

### 검증 이력

#### 2026-04-07 링크 및 이미지 주석 검증

**하이퍼링크 수정 (600개 / 225+ 파일)**

| 유형 | 수정 수 | 설명 |
|------|---------|------|
| `../../` → `../` 경로 깊이 수정 | 569 | `divided/`→`docs/` 경로 이동 후 상대경로 깊이 미갱신 |
| 상대 파일명 참조 수정 | 20 | `.md` 확장자 및 `../` 접두어 누락 보완 |
| `./Error-code/` 경로 수정 | 4 | `./Error-code/#...` → `../error-code.md#...` |
| 절대경로 → 외부 URL 변환 | 4 | `/Download/`, `/TOAST/` → `https://docs.nhncloud.com/...` |
| 괄호 중복 수정 | 1 | `((https://...)` → `(https://...)` |
| 오타 수정 | 1 | `aos-started/₩1#...` → `../aos-started.md#...` |

**이미지 주석 추가 (128개 / 15개 파일)**

| 파일 | 추가 수 | 내용 |
|------|---------|------|
| console-google-guide | +28 | Google Play Console 설정 스크린샷 |
| oper-member | +18 | 회원 관리 콘솔 화면 |
| oper-coupon | +13 | 쿠폰 관리 콘솔 화면 |
| console-epicgames-guide | +10 | Epic Games 스토어 설정 화면 |
| oper-ban | +10 | 이용 정지(밴) 콘솔 화면 |
| ios-started | +10 | iOS SDK 설정 (XCode, Framework 등) |
| console-huawei-guide | +8 | Huawei AppGallery 설정 화면 |
| unity-started | +7 | Unity SDK Setting Tool 화면 |
| console-amazon-guide | +6 | Amazon Appstore 콘솔 화면 |
| console-steam-guide | +5 | Steam 스토어 설정 화면 |
| oper-operating-indicator | +5 | 운영 지표 모니터링 화면 |
| aos-initialization | +3 | 초기화 플로우/점검 팝업 |
| unity-initialization | +2 | 점검 팝업/웹뷰 |
| ios-initialization | +2 | 점검 웹뷰 |
| console-mycard-guide | +1 | MyCard 스토어 설정 |

**검증 결과**: 깨진 링크 0개, 깨진 이미지 0개, 누락 주석 0개