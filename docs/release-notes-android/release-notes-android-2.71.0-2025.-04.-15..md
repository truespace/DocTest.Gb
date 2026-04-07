---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.71.0, 신규, 기능개선, 기능추가, 변경, Notice"
section: "2.71.0 (2025. 04. 15.)"
order: 13
---

### 2.71.0 (2025. 04. 15.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-Android.zip)

#### 기능 추가

* '게임 공지' 신규 기능이 추가되었습니다.
    * Gamebase.GameNotice.openGameNotice(Activity activity, GamebaseCallback onCloseCallback);
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Android SDK 사용 가이드 > UI > GameNotice](../aos-ui.md#gamenotice)

#### 기능 개선/변경

* storeCode를 null로 설정하여 Gamebase 초기화를 호출했을 때 예외가 발생하는 대신 **INVALID_PARAMETER(3)** 에러를 리턴하도록 동작을 변경했습니다.
