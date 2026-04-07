---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "2.33.0 (2022.01.25)"
section: "2.33.0 (2022.01.25)"
order: 38
---

### 2.33.0 (2022.01.25)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.33.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* '결제 어뷰징 자동 해제' 기능이 추가되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 인증 > GraceBan](../../unreal-authentication.md#graceban)
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용이 정지됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 AuthToken.member.graceBanInfo API 값을 확인하고, null이 아닌 유효한 GraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 인증 > Mapping > Add Mapping Forcibly](../../unreal-authentication.md#add-mapping-forcibly)
* Gamebase.AddMapping() 호출 후 AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302) 에러가 발생했을 때, 해당 계정으로 로그인을 할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 인증 > Mapping > Change Login with ForcingMappingTicket](../../unreal-authentication.md#change-login-with-forcingmappingticket)
* GamebaseEventHandler의 GamebaseEventCategory에 **GamebaseEventCategory::ServerPushAppKickOutMessageReceived** 타입이 추가되었습니다.
    * 이 이벤트의 활용 방법은 다음 문서를 참고하시기 바랍니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../../unreal-etc.md#server-push)
* GamebaseEventHandler의 GamebaseEventCategory에 **GamebaseEventCategory::LoggedOut** 타입이 추가되었습니다.
    * Gamebase Access Token이 만료되어 로그인이 필요할 때 동작합니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../../unreal-etc.md#logged-out)
* 공통 약관 창의 설정을 변경할 수 있는 신규 API가 추가되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > UI > Terms > showTermsView](../../unreal-ui.md#showtermsview)

#### 기능 개선/변경
* 오류 코드 추가 및 변경
    * GamebaseErrorCode::UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode::SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.33.0](../../release-notes-android.md#2330-20220125)
* [Gamebase iOS SDK 2.33.0](../../release-notes-ios.md#2330-20220125)
