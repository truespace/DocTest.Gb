---
source: upgrade-guide.md
section: "2.42.1"
order: 36
split: true
created_date_time: 20260408_184906
keyword: WebView, XCode, iOS, Unity, Upgrade Guide, 2.42.1
---

## 2.42.1

### Unity
    
#### Changed/Deprecated APIs
* FGamebaseWebViewConfiguration에서 enableFixedFontSize 필드는 더 이상 지원하지 않습니다.
* GamebaseWebViewConfiguration 일부 필드에 기본값이 추가되어 값을 설정하지 않은 경우 기존과 다르게 동작할 수 있습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다

### Unreal

* (iOS) [iOS 설정 툴](../unreal-started.md#ios-settings)에서 Xcode의 경로를 변경할 수 있도록 **Xcode Path** 설정이 추가되었습니다.
    * 변경하지 않는 경우 기본값으로 설정됩니다(기본값: /Applications/Xcode.app).

#### Changed/Deprecated APIs
* FGamebaseConfiguration의 enableKickoutPopup 속성을 더 이상 지원하지 않습니다.
* FGamebaseConfiguration 일부 필드에 기본값이 추가되어 값을 설정하지 않은 경우 기존과 다르게 동작할 수 있습니다.
    * enableLaunchingStatusPopup의 기본값이 true로 설정되었습니다.
    * enableBanPopup의 기본값이 true로 설정되었습니다.
* FGamebaseWebViewConfiguration에서 enableFixedFontSize 필드는 더 이상 지원하지 않습니다.
* FGamebaseWebViewConfiguration 일부 필드에 기본값이 추가되어 값을 설정하지 않은 경우 기존과 다르게 동작할 수 있습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255으로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다.
