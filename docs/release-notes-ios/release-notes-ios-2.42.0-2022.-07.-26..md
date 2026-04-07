---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.42.0, 버그수정, 기능개선, 기능추가, 변경"
section: "2.42.0 (2022. 07. 26.)"
order: 51
---

### 2.42.0 (2022. 07. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 매핑 실패 시 반환되는 ForcingMappingTicket VO 클래스에 유저의 현재 상태를 알 수 있도록 필드가 추가되었습니다.
    * **TCGBForcingMappingTicket.mappedUserValid**
    * mappedUserValid에 저장된 값의 의미는 아래를 참고해 주세요.
        * [Game > Gamebase > API 가이드 > API v1.3 가이드 > Others > Mamber Vaild Code](../api-guide.md#member-valid-code)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame iOS SDK (1.7.0)

#### 버그 수정
* 잘못된 AppID로 Gamebase를 초기화했을 때 콜백이 호출되지 않는 버그를 수정하였습니다.
* 한게임 IdP로 로그인한 상태에서 GamebaseEventHandler의 **kTCGBIdPRevoked** 이벤트가 발생하지 않는 버그를 수정하였습니다.
