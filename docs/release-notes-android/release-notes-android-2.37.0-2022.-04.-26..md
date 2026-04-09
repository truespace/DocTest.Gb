---
source: release-notes-android.md
section: "2.37.0 (2022. 04. 26.)"
order: 59
split: true
created_date_time: 20260408_184906
keyword: Android, Purchase, Release Notes, 2.37.0
---

### 2.37.0 (2022. 04. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.37.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 고객 센터 URL 뒤에 파라미터를 추가할 수 있도록 다음 필드가 추가되었습니다.
    * **ContactConfiguration.Builder.setAdditionalParameters(Map&lt;String, String&gt;)**

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Gamebase IAP Android SDK(0.18.3)
* Amazon Appstore 결제 데이터에서 userId, gamebaseProductId가 누락될 시 userId, gamebaseProductId를 자동으로 채우도록 개선되었습니다.
