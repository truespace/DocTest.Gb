---
source: release-notes-unity.md
section: "1.9.0 (2018.05.03)"
order: 122
split: true
created_date_time: 20260408_191848
keyword: Unity, Mapping, Release Notes, 1.9.0
---

### 1.9.0 (2018.05.03)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* Transfer 기능 추가
    * guest 사용자가 매핑없이 새로운 기기로 이전할 수 있는 기능
    * (SDK공통)추가된 API 
        * Transfer Key 발급 API (IssueTransferKey)
        * 발급된 TransferKey를 사용하여 계정 이전을 요청하는 API (RequestTransfer)
* 이용 정지 등록시 사용자의 리더보드(랭킹) 데이터를 삭제할 수 있는 옵션 추가(TOAST Leaderboard를 사용하는 경우에 한함)
    * 이용 정지 등록 메뉴를 이용하거나 App Guard 연동 페이지에서 사용 가능
