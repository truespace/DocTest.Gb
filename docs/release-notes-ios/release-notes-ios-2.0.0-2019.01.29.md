---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.0.0, 버그수정, 기능개선, 기능추가, 변경, IAP"
section: "2.0.0 (2019.01.29)"
order: 118
---

### 2.0.0 (2019.01.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.0.0/GamebaseSDK-iOS.zip)

```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가

* Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK 내부에서 자동 전송)
    * setGameUserData: 게임 로그인 이후 유저 레벨 정보 전송
    * traceLevelUpData: 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출

#### 기능 개선/변경

* IAP SDK 업데이트
    * 결제 실패 시 간헐적으로 크래시가 발생하던 현상 수정

#### 버그수정

* iOS 12 이상의 시뮬레이터에서 debugMode On 상태로 Gamebase 초기화 시 크래시가 발생하던 현상 수정
