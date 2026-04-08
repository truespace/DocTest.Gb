---
source: release-notes-ios.md
section: "2.1.0 (2019.02.26)"
order: 117
split: true
created_date_time: 20260408_191848
keyword: iOS, Login, Release Notes, 2.1.0
---

### 2.1.0 (2019.02.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.1.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* TransferKey API 삭제
    * issueTransferKey: TransferKey 발급
    * requestTransfer: TransferKey 검증
        
#### 버그수정

* Gamecenter를 Gamebase가 아닌 다른 로직에의해 로그인 한 후, Gamebase를 통하여 Gamecenter로그인을 시도할 때, 반응이 없는 버그 수정
