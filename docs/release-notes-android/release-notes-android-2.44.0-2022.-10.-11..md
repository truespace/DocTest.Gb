---
source: release-notes-android.md
section: "2.44.0 (2022. 10. 11.)"
order: 49
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Alert, Error, RegisterPush, Release Notes, 2.44.0
---

### 2.44.0 (2022. 10. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Android SDK(1.2.0), TOAST Gamebase IAP Android SDK(0.21.0), Google Play Services Auth(20.0.3)
* Android 13 OS에서 registerPush 호출 시 자동으로 알림 허용 권한을 요청하는 팝업을 표시합니다.
* Google 로그인 시 silentSignIn API를 활용하도록 내부 로직을 개선했습니다.

#### 버그 수정
* Hangame IdP 로그인 시 유효한 타사 IdP를 이용한 뒤 유효하지 않은 타사 IdP로 다시 시도하면 오류가 발생하지 않고 이전 IdP로 로그인을 시도하여 크래시가 발생하는 문제를 수정했습니다.
