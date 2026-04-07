---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v2.30.0, 신규, 기능추가, 변경, Login, Mapping, IdP"
section: "2.30.0 (2021.11.23)"
order: 62
---

### 2.30.0 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Mapping > Add Mapping Forcibly](../../unity-authentication.md#add-mapping-forcibly)
* Gamebase.AddMapping() 호출 후 AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302) 에러가 발생했을 때, 해당 계정으로 로그인을 할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Mapping > Change Login with ForcingMappingTicket](../../unity-authentication.md#change-login-with-forcingmappingticket)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.30.0](../../release-notes-android.md#2300-20211123)
* [Gamebase iOS SDK 2.30.0](../../release-notes-ios.md#2300-20211123)
