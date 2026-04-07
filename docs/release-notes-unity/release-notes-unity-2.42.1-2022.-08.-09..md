---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v2.42.1, 기능개선, 기능추가, 변경"
section: "2.42.1 (2022. 08. 09.)"
order: 49
---

### 2.42.1 (2022. 08. 09.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.1/GamebaseSDK-Unity.zip)

#### 기능 추가
* ForcingMappingTicket 클래스에 매핑 유저 상태를 나타내는 mappedUserValid 필드가 추가되었습니다.

#### 기능 개선/변경
* 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드는 더 이상 사용되지 않습니다.
    * **GamebaseWebViewConfiguration.enableFixedFontSize**
* GamebaseWebViewConfiguration의 기본값이 추가되었습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.42.1](../release-notes-android.md#2421-2022-07-26)
* [Gamebase iOS SDK 2.42.1](../release-notes-ios.md#2421-2022-08-09)
