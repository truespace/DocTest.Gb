---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "2.32.0 (2021.12.28)"
section: "2.32.0 (2021.12.28)"
order: 64
---

### 2.32.0 (2021.12.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* GamebaseEventHandler의 GamebaseEventCategory에 **kTCGBServerPushAppKickoutMessageReceived** 타입이 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../../ios-etc.md#server-push)
* GamebaseEventHandler의 GamebaseEventCategory에 **kTCGBLoggedOut** 타입이 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../../ios-etc.md#logged-out)

#### 기능 개선/변경
* 웹뷰 navigationBar의 기본 타이틀 색상이 **UIColor.whiteColor**로 변경되었습니다.

#### 버그 수정
* Hangame 로그아웃 호출 시, thirdIdP도 로그아웃되도록 수정하였습니다.
