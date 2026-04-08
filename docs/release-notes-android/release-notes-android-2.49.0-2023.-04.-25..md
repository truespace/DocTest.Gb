---
source: release-notes-android.md
section: "2.49.0 (2023. 04. 25.)"
order: 42
split: true
created_date_time: 20260408_191848
keyword: Android, Release Notes, 2.49.0
---

### 2.49.0 (2023. 04. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-Android.zip)

```
최소 지원 버전이 Android 4.4 이상으로 상향되었습니다.(minSdk 16 -> 19)
```

#### 기능 개선/변경
* 내부 지표 개선

#### 버그 수정
* 다음 adapter를 빌드에 포함하는 경우 불필요한 READ_PHONE_STATE 권한이 추가되는 버그를 수정했습니다.
    * gamebase-adapter-auth-facebook
    * gamebase-adapter-auth-hangame
    * gamebase-adapter-auth-line
    * gamebase-adapter-purchase-google
    * gamebase-adapter-purchase-onestore
    * gamebase-adapter-purchase-onestore-external
    * gamebase-adapter-purchase-onestore-v16
    * gamebase-adapter-purchase-onestore-v19
    * gamebase-adapter-push-adm
    * gamebase-adapter-push-fcm
