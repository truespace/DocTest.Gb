---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.44.1 (2022. 10. 25.)"
section: "2.44.1 (2022. 10. 25.)"
order: 48
---

### 2.44.1 (2022. 10. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.1/GamebaseSDK-Android.zip)

#### 기능 추가
* Android 13 이상의 OS에서 registerPush API를 호출했을 때 Push 권한 요청 팝업이 자동으로 뜨지 않도록 할 수 있는 **PushConfiguration.Builder.enableRequestNotificationPermission(boolean)** API가 추가되었습니다.

#### 기능 개선/변경
* Facebook Android SDK 13.2.0 이상에서는 Facebook Client Token 설정이 필요합니다.
    * Gamebase Android SDK 2.44.1 이상부터는 Gamebase Console의 additionalInfo에 다음과 같이 **facebook_client_token** 필드를 추가하는 경우 Facebook Client Token이 클라이언트 SDK에 자동으로 적용됩니다.

            { "facebook_permission": [...], "facebook_client_token": "a01234bc56de7fg89012hi3j45k67890" }

#### 버그 수정
* Android 6.0(M, API Level 23) 단말기에서 **Gamebase.Push.registerPush** API를 호출하면 **IllegalArgumentException** 예외가 발생하는 버그를 수정했습니다.
