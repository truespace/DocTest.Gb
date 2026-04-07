---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v1.12.1, 버그수정, 기능개선, 기능추가, 변경, Maintenance, Guest, IdP, IAP"
section: "1.12.1 (2018.08.09)"
order: 123
---

### 1.12.1 (2018.08.09) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* IAP SDK 최신버전 적용 (1.5.0)
* Gamebase 점검페이지에서 점검시간을 단말기 설정 국가시간에 맞추어 노출하도록 개선
* 점검페이지를 외부 페이지로 사용할 때 Console에 입력한 점검 정보를 사용할 수 있도록 기능 추가
* IdP 매핑된 사용자의 Guest 매핑시도시 에러 발생(TCGB_ERROR_AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP)
* 인증 API 중복 호출 시 에러 발생(AUTH_ALREADY_IN_PROGRESS_ERROR)
* 오류 코드 추가: Gamecenter 로그인 거부(TCGB_ERROR_IOS_GAMECENTER_DENIED)
    
#### 버그수정

* NAVER 로그인 시 프로필 정보 조회 실패로 인해 로그인이 불가능한 버그 수정: 프로필 정보 조회 실패하더라도 로그인은 성공하도록 변경
