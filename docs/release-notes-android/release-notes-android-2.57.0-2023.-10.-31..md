---
source: release-notes-android.md
section: "2.57.0 (2023. 10. 31.)"
order: 33
split: true
created_date_time: 20260408_184906
keyword: Android, Login, WebView, Logger, Release Notes, 2.57.0
---

### 2.57.0 (2023. 10. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.57.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Naver Login Android SDK(5.8.0)

#### 기능 추가
* Exception을 Log & Crash Search로 전송할 수 있는 API가 추가되었습니다.

        Gamebase.Logger.report(String message, Throwable throwable);
        Gamebase.Logger.report(String message, Throwable throwable, Map<String, String> userFields);

#### 버그 수정
* Gamebase WebView close() 시에 간헐적으로 EmptyStackException이 발생하는 버그를 수정했습니다.
