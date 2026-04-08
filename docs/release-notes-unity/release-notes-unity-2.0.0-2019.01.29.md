---
source: release-notes-unity.md
section: "2.0.0 (2019.01.29)"
order: 112
split: true
created_date_time: 20260408_191848
keyword: Unity, Login, Purchase, Release Notes, 2.0.0
---

### 2.0.0 (2019.01.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.0.0/GamebaseSDK-Unity.zip)
```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가
* [SDK] 2.0.0
    * (공통)Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK내부에서 자동 전송)
        * setGameUserData : 게임 로그인 이후 유저 레벨 정보 전송
        * traceLevelUpData : 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출
