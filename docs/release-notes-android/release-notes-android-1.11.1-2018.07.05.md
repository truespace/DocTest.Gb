---
source: release-notes-android.md
section: "1.11.1 (2018.07.05)"
order: 117
split: true
created_date_time: 20260408_191848
keyword: Android, Login, Release Notes, 1.11.1
---

### 1.11.1 (2018.07.05)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.11.1
    * (공통)Guest로그인 후 AddMapping 성공 시, loginForLastLoggedInPrivder를 하게되면, AddMapping 성공한 IdP계정을 사용하여 로그인하도록 변경
    
#### 버그수정
* [SDK] 1.11.1
    * (공통)점검 해제 후 후속 API 진행(login/push/purchase 등)이 되지 않던 버그 수정
    * (Android)Gamebase.addObserver()를 통해 ObserverMessage를 수신하였을 경우, ObserverMessage.data.code의 타입이 int가 아니라 String인 버그를 수정
