---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "2.35.0 (2022. 03. 29.)"
section: "2.35.0 (2022. 03. 29.)"
order: 56
---

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 외부 SDK 업데이트: TOAST Unity SDK(0.25.1)
* 약관이 표시되었는지를 알 수 있는 API가 추가되었습니다.
    * Gamebase.Terms.IsShowingTermsView()
* 웹뷰에서 내비게이션 바를 숨길 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Webview.GamebaseWebViewConfiguration.isNavigationBarVisible
* (Android) 웹뷰에서 폰트 사이즈를 고정할 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Webview.GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 약관 창에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Terms.GamebaseTermsConfiguration.enableFixedFontSize
* Setting Tool
    * (Android) Amazon 스토어가 추가되었습니다.
    * (Android) Huawei 스토어가 추가되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.35.0](../../release-notes-android.md#2350-2022-03-29)
* [Gamebase iOS SDK 2.35.0](../../release-notes-ios.md#2350-2022-03-29)
