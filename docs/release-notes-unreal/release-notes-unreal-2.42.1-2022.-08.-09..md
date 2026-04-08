---
source: release-notes-unreal.md
section: "2.42.1 (2022. 08. 09.)"
order: 33
split: true
created_date_time: 20260408_191848
keyword: Unreal, Mapping, WebView, XCode, Android, iOS, Release Notes, 2.42.1
---

### 2.42.1 (2022. 08. 09.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.1/GamebaseSDK-Unreal.zip)

#### 기능 추가
* FGamebaseForcingMappingTicket 클래스에 매핑 유저 상태를 나타내는 mappedUserValid 필드가 추가되었습니다.
* [iOS 설정 툴](../unreal-started.md#ios-settings)에서 Xcode의 경로를 지정할 수 있도록 **Xcode Path** 설정이 추가되었습니다.

#### 기능 개선/변경
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드는 더 이상 사용하지 않습니다.
    * **FGamebaseConfiguration.bEnableKickoutPopup**
* FGamebaseConfiguration 내 일부 필드에 기본값이 추가되었습니다.
    * bEnableLaunchingStatusPopup의 기본값이 true로 설정되었습니다.
    * bEnableBanPopup의 기본값이 true로 설정되었습니다.
* 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드는 더 이상 사용되지 않습니다.
    * **FGamebaseWebViewConfiguration.enableFixedFontSize**
* FGamebaseWebViewConfiguratio 내 일부 필드에 기본값이 추가되었습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다.
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.42.1](../release-notes-android.md#2421-2022-07-26)
* [Gamebase iOS SDK 2.42.1](../release-notes-ios.md#2421-2022-08-09)
