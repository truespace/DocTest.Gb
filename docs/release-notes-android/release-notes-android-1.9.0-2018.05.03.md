---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v1.9.0, 신규, 버그수정, 기능추가, Guest"
section: "1.9.0 (2018.05.03)"
order: 119
---

### 1.9.0 (2018.05.03)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Transfer 기능 추가
    * guest 사용자가 매핑없이 새로운 기기로 이전할 수 있는 기능
    * (SDK공통)추가된 API 
        * Transfer Key 발급 API (IssueTransferKey)
        * 발급된 TransferKey를 사용하여 계정 이전을 요청하는 API (RequestTransfer)

#### 버그 수정
* [SDK] 1.9.0
    * (Android) Heartbeat 에서 잘못된 사용자로 판정되는 경우 이용 정지 팝업 창이 뜨지 않도록 수정(iOS 와 동일한 로직으로 수정)
