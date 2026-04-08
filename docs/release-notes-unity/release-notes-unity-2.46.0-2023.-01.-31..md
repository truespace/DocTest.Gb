---
source: release-notes-unity.md
section: "2.46.0 (2023. 01. 31.)"
order: 44
split: true
created_date_time: 20260408_191848
keyword: Unity, Login, WebView, Initialize, Error, Android, iOS, Release Notes, 2.46.0
---

### 2.46.0 (2023. 01. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.46.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (WebGL) Google 로그인 기능이 추가되었습니다.
* (Android) 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드를 재지원합니다.
    * GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 웹뷰에서 컷아웃(노치) 영역을 비롯한 모든 이용 가능한 스크린 공간을 사용하여 렌더링할 수 있는 설정이 추가되었습니다.
    * GamebaseWebViewConfiguration.renderOutsideSafeArea
* (Android) IAP 구독 상태를 조회할 수 있는 RequestSubscriptionsStatus API가 추가되었습니다.

#### 버그 수정
* (Standalone) 초기화 시 간헐적으로 ReflectionTypeLoadException 오류가 발생하는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.46.0](../release-notes-android.md#2460-2023-01-31)
* [Gamebase iOS SDK 2.46.0](../release-notes-ios.md#2460-2023-01-31)
