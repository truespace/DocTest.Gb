---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.30.0, 신규, 버그수정, 기능추가, Login, Mapping, IdP"
section: "2.30.0 (2021.11.23)"
order: 67
---

### 2.30.0 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > Add Mapping Forcibly](../../ios-authentication.md#add-mapping-forcibly)
* 특정 IdP로 매핑 시도 후 **TCGB_ERROR_AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)** 에러가 발생했을 때, 해당 IdP로 계정을 변경할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > Change Login with ForcingMappingTicket](../../ios-authentication.md#change-login-with-forcingmappingticket)

#### 버그 수정
* loginForLastLoggedInProvider 로그인 이후, 특정 IdP에서 로그아웃 또는 탈퇴 기능이 동작하지 않는 버그를 수정하였습니다.
