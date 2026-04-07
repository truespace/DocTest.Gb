---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.75.0, 기능개선, 변경, 제거, Purchase, Push"
section: "2.75.0 (2025. 09. 23.)"
order: 7
---

### 2.75.0 (2025. 09. 23.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
 
* 외부 SDK 업데이트: NHN Cloud Android SDK(1.12.0), PAYCO Android SDK(1.5.17), Weibo Android SDK(13.10.5)
* Google Play의 16KB 페이지 제약 대응을 위한 외부 SDK 업데이트
    * NHN Cloud SDK / Weibo SDK 업데이트
    * 16KB 미대응 gamebase-adapter-auth-weibo-v4 모듈 제거
* 미사용 모듈 제거
    * gamebase-adapter-purchase-amazon, gamebase-adapter-push-adm
* 내부 로직 개선
