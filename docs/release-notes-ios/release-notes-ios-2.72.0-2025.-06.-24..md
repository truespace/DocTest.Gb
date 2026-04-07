---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, XCode, v2.72.0, 버그수정, 기능개선, 기능추가, 변경, 제거"
section: "2.72.0 (2025. 06. 24.)"
order: 8
---

### 2.72.0 (2025. 06. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.17.2)
        * 내부 로직 개선
    * LINE iOS SDK (5.11.2)
        * bitcode 설정 제거
        * Xcode 16 컴파일러 경고 수정
* 내부 로직 개선

#### 버그 수정
* LINE IdP의 Region 추가 정보 대응이 되지 않아 매핑 및 loginForLastLoggedInProvider 로그인 관련 동작에서 발생하는 문제를 수정했습니다.
