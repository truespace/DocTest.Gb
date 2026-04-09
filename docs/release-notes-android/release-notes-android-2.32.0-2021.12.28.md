---
source: release-notes-android.md
section: "2.32.0 (2021.12.28)"
order: 64
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Logout, Push, WebView, Release Notes, 2.32.0
---

### 2.32.0 (2021.12.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.0/GamebaseSDK-Android.zip)

#### 기능 추가
* GamebaseEventHandler의 GamebaseEventCategory에 **GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED** 타입이 추가되었습니다.
    * 이 이벤트의 활용 방법은 다음 문서를 참고하시기 바랍니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../aos-etc.md#server-push)
* Gamebase Access Token이 만료되어 로그인이 필요할 때 동작하는 **GamebaseEventCategory.LOGGED_OUT** GamebaseEventHandler category가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../aos-etc.md#logged-out)

#### 기능 개선/변경
* 웹뷰 URL이 **onestore://**로 시작하는 ONE store 딥링크가 동작하도록 웹뷰를 개선했습니다.

#### 버그 수정
* Gamebase Android SDK 2.31.0에서 로그아웃을 호출해도 IdP 로그아웃은 호출되지 않아 IdP 계정을 변경할 수 없는 버그를 수정했습니다.
