---
source: release-notes-ios.md
section: "2.62.0 (2024. 03. 26.)"
order: 23
split: true
created_date_time: 20260408_191848
keyword: iOS, Initialize, Authentication, XCode, Release Notes, 2.62.0
---

### 2.62.0 (2024. 03. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Gamebase와 Gamebase Adapter SDK에 Privacy manifest와 서명을 적용했습니다.
* Gamebase 초기화 후 반환되는 LaunchingInfo VO에서 테스트 단말기임을 알 수 있도록 필드가 추가되었습니다.
    * **launchingInfo.user.testDevice**

#### 기능 개선/변경
* Xcode 최소 지원 버전이 15.0으로 변경되었습니다. 
* iOS 최소 지원 버전이 12.0으로 변경되었습니다.
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.1)
    * LINE iOS SDK (5.11.0)
        * LINE 인증 최소 지원 버전이 13.0으로 변경되었습니다.
    * NAVER iOS SDK (4.2.1)
    * PAYCO iOS SDK (1.5.10)
    * Hangame iOS SDK (1.12.0)
* 내부 로직 개선
