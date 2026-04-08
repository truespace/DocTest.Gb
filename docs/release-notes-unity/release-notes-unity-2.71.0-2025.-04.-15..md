---
source: release-notes-unity.md
section: "2.71.0 (2025. 04. 15.)"
order: 15
split: true
created_date_time: 20260408_191848
keyword: Unity, Initialize, Error, Android, iOS, Release Notes, 2.71.0
---

### 2.71.0 (2025. 04. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* '게임 공지' 신규 기능이 추가되었습니다.
    * Gamebase.GameNotice.OpenGameNotice(GamebaseCallback.ErrorDelegate callback)
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unity SDK 사용 가이드 > 공지 > 게임 공지](../unity-ui.md#gamenotice)

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.
* (iOS) ViewController 설정 로직을 개선하여 초기화 실패 오류를 방지합니다.

#### 버그 수정

* macOS 15.4에서 크래시가 발생하는 이슈를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.71.0](../release-notes-android.md#2710-2025-04-15)
* [Gamebase iOS SDK 2.71.0](../release-notes-ios.md#2710-2025-04-15)
