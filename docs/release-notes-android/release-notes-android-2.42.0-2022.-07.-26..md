---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.42.0, 버그수정, 기능개선, 변경"
section: "2.42.0 (2022. 07. 26.)"
order: 52
---

### 2.42.0 (2022. 07. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.5.2)
* ForcingMappingTicket VO 클래스에 매핑 유저 상태를 나타내는 mappedUserValid 필드가 추가되었습니다.
* Gamebase Adapter 버전이 Gamebase 버전과 일치하지 않는 경우 런타임 예외가 발생할 수 있으므로, 초기화가 실패하도록 변경되었습니다.

#### 버그 수정
* LDPlayer에서 Naver 웹 로그인에 실패하는 현상이 수정되었습니다.
* OS 버전이 낮아 Twitter 로그인에 실패하는 경우 크래시가 발생하는 문제가 수정되었습니다.
