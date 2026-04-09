---
source: release-notes-android.md
section: "2.41.0 (2022. 07. 05.)"
order: 55
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Logout, WebView, Release Notes, 2.41.0
---

### 2.41.0 (2022. 07. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.31.1), Hangame Android SDK(1.4.6)
* 웹뷰에 등록한 커스텀 스킴 이벤트가 동작할 때 자동으로 웹뷰가 종료됩니다.
    * 커스텀 스킴 이벤트가 동작하더라도 웹뷰를 유지하려면 **GamebaseWebViewConfiguration.Builder.enableAutoCloseByCustomScheme(false)** API를 호출하세요.

#### 버그 수정
* Hangame IdP 로그아웃 후 로그인을 바로 시도하면 간헐적으로 크래시가 발생하거나 로그인에 실패하는 문제를 수정했습니다.
