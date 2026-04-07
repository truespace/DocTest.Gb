---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.58.0, 버그수정, 기능개선, 변경, Logger"
section: "2.58.0 (2023. 11. 28.)"
order: 32
---

### 2.58.0 (2023. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.58.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Kakaogame Android SDK(3.17.5)
* Twitter API 서버 인증서 갱신으로 인해 Twitter Adapter minSdkVersion을 21로 상향
* 내부 로직 개선

#### 버그 수정
* Gamebase.Logger.report(String message, ...) API의 message에 빈 문자열을 넣어도 크래시가 발생하지 않도록 방어 코드를 추가했습니다.
