---
source: release-notes-unity.md
section: "2.73.0 (2025. 07. 15.)"
order: 12
split: true
created_date_time: 20260408_184906
keyword: Unity, Login, WebView, Android, iOS, Release Notes, 2.73.0
---

### 2.73.0 (2025. 07. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.0/GamebaseSDK-Unity.zip)

#### 기능 추가

#### 기능 개선/변경
* (Windows, macOS) IdP 로그인 시 웹뷰에서 외부 브라우저로 변경했습니다.
    * 지원 브라우저
        * Windows: 모든 브라우저
        * macOS: Chrome, Safari, Firefox, Whale

* 외부 브라우저 로그인 취소 API를 추가했습니다.
    * 진행 중인 외부 브라우저 로그인 요청 중 IdP를 변경하고 싶을 때 기존 요청을 취소하기 위함.
    * CancelLoginWithExternalBrowser()

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.73.0](../release-notes-android.md#2730-2025-07-15)
* [Gamebase iOS SDK 2.73.0](../release-notes-ios.md#2730-2025-07-15)
