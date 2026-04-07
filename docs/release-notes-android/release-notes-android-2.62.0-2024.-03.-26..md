---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.62.0 (2024. 03. 26.)"
section: "2.62.0 (2024. 03. 26.)"
order: 28
---

### 2.62.0 (2024. 03. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 초기화 후 반환되는 LaunchingInfo VO에서 테스트 단말기임을 알 수 있도록 필드가 추가되었습니다.
    * **launchingInfo.user.testDevice**

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.9.0)
* Preference를 복사해서 사용할 수 없도록 내부 로직이 개선되었습니다.
* gamebase-sdk-base 모듈이 gamebase-sdk 단일 모듈로 통합되었습니다.
