---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "2.32.0 (2021.12.28)"
section: "2.32.0 (2021.12.28)"
order: 60
---

### 2.32.0 (2021.12.28)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* GamebaseEventHandler의 GamebaseEventCategory에 **GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED** 타입이 추가되었습니다.
    * 이 이벤트의 활용 방법은 다음 문서를 참고하시기 바랍니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../../unity-etc.md#server-push)
* Gamebase Access Token이 만료되어 로그인이 필요할 때 동작하는 **GamebaseEventCategory.LOGGED_OUT** GamebaseEventHandler category가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../../unity-etc.md#logged-out)
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.32.0](../../release-notes-android.md#2320-20211228)
* [Gamebase iOS SDK 2.32.0](../../release-notes-ios.md#2320-20211228)
