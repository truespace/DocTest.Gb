---
source: release-notes-ios.md
section: "2.71.0 (2025. 04. 15.)"
order: 9
split: true
created_date_time: 20260408_184906
keyword: iOS, Initialize, Error, Release Notes, 2.71.0
---

### 2.71.0 (2025. 04. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* '게임 공지' 신규 기능이 추가되었습니다.
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다. 
        * [Game > Gamebase > iOS SDK 사용 가이드 > UI > GameNotice > Open GameNotice](../ios-ui.md#open-gamenotice)

#### 기능 개선/변경
* storeCode를 nil로 설정하여 Gamebase 초기화를 호출했을 때 예외가 발생하는 대신 **TCGB_ERROR_INVALID_PARAMETER(3)** 에러를 리턴하도록 동작을 변경했습니다.
