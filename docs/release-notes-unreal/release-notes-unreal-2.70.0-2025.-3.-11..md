---
source: release-notes-unreal.md
section: "2.70.0 (2025. 3. 11.)"
order: 13
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Initialize, Error, Android, iOS, Release Notes, 2.70.0
---

### 2.70.0 (2025. 3. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* 로그인 시 IdP 서버로부터 오류가 발생했음을 나타내는 신규 오류 코드가 추가되었습니다.
    * AUTH_AUTHENTICATION_SERVER_ERROR(3012)
* WebView에 내비게이션 바 타이틀과 아이콘 틴트 컬러 설정 옵션을 추가했습니다.
    * `FGamebaseWebViewConfiguration::NavigationBarTitleColor`
    * `FGamebaseWebViewConfiguration::NavigationBarIconTintColor`
* (Android) 'GPGS 자동 로그인' 기능 연동 시 유저에게 GPGS 로그인을 앱 설치 후 한번만 물어보는 초기화 옵션을 추가했습니다.
    * `FGamebaseConfiguration::bEnableGPGSSignInCheck`
    * 기본 설정은 true로, 유저가 GPGS 로그인을 거부하더라도 Gamebase 초기화 때 GPGS 로그인 창을 다시 표시합니다.
    * false로 설정하면 앱 최초 실행 시에만 GPGS 로그인 창이 한번 표시됩니다.

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 버그 수정

* (Windows) 로그인 시 FGamebaseVariantMap로 추가 정보를 받는 경우 크래시가 발생하지 않도록 수정했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.70.0](../release-notes-android.md#2700-2025-03-11)
* [Gamebase iOS SDK 2.70.0](../release-notes-ios.md#2700-2025-03-11)
