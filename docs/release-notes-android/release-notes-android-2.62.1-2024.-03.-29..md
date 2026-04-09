---
source: release-notes-android.md
section: "2.62.1 (2024. 03. 29.)"
order: 27
split: true
created_date_time: 20260408_184906
keyword: Android, LoginForLastLoggedInProvider, Release Notes, 2.62.1
---

### 2.62.1 (2024. 03. 29.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.1/GamebaseSDK-Android.zip)

#### 버그 수정
* Android 7.0(API Level 24) 미만 단말기에서 Gamebase.loginForLastLoggedInProvider 호출이 항상 실패하고 Guest 계정이 유실되는 버그를 수정했습니다.
    * 이 문제는 Gamebase Android SDK 2.62.0에서만 발생합니다.
