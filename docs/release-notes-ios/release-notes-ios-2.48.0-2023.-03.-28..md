---
source: release-notes-ios.md
section: "2.48.0 (2023. 03. 28.)"
order: 40
split: true
created_date_time: 20260408_184906
keyword: iOS, WebView, XCode, Release Notes, 2.48.0
---

### 2.48.0 (2023. 03. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.48.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 14.1로 변경되었습니다. 
* iOS 최소 지원 버전이 11.0으로 변경되었습니다.
* armv7, armv7s, i386 아키텍처 지원을 중단하였습니다.
* 더 이상 bitcode를 지원하지 않습니다.
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.3.0)
    * PAYCO iOS SDK (1.5.6)
* DNS 장애를 대비한 Gamebase 서버 예비 도메인 적용

#### 버그 수정
* 특정 상황에서 킥아웃 이벤트가 동작하지 않는 버그를 수정하였습니다.
* 웹뷰 커스텀 스킴 콜백이 호출되지 않는 버그를 수정하였습니다.
