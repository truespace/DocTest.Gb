---
source: release-notes-android.md
section: "2.65.0 (2024. 06. 11.)"
order: 24
split: true
created_date_time: 20260408_191848
keyword: Android, Purchase, ImageNotice, Gradle, Release Notes, 2.65.0
---

### 2.65.0 (2024. 06. 11.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 이미지 공지 기능에 신규 타입이 추가되었습니다.
    * `롤링 팝업` 타입이 추가되었습니다.
    * 기존의 이미지 공지는 `개별 팝업` 타입으로 표기됩니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.0), Hangame Android SDK(1.13.0)
    * Google billing client version 6.2.1이 적용되었습니다.
    * Android OS 4.4(API Level 19) 단말기에서 결제하려면 추가 설정이 필요합니다.
        * 자세한 내용은 [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Root level build.gradle](../aos-started.md#root-level-buildgradle) 가이드를 참고하시기 바랍니다.
* 내부 로직 개선
