---
source: aos-authentication.md
section: "Error Handling"
order: 9
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Logout, Mapping, Withdraw, Initialize
---

## Error Handling

| Category       | Error                                    | Error Code | Description                              |
| -------------- | ---------------------------------------- | ---------- | ---------------------------------------- |
| Auth           | INVALID\_MEMBER                          | 6          | 잘못된 회원에 대한 요청입니다.                        |
|                | BANNED\_MEMBER                           | 7          | 제재된 회원입니다.                               |
|                | AUTH\_USER\_CANCELED                     | 3001       | 로그인이 취소되었습니다.                            |
|                | AUTH\_NOT\_SUPPORTED\_PROVIDER           | 3002       | 지원하지 않는 인증 방식입니다.                        |
|                | AUTH\_NOT\_EXIST\_MEMBER                 | 3003       | 존재하지 않거나 탈퇴한 회원입니다.                      |
|                | AUTH\_EXTERNAL\_LIBRARY\_INITIALIZATION\_ERROR | 3006 | 외부 인증 라이브러리 초기화에 실패하였습니다. |
|                | AUTH\_EXTERNAL\_LIBRARY\_ERROR           | 3009       | 외부 인증 라이브러리 오류입니다.<br/>상세 오류를 확인하세요. |
|                | AUTH\_ALREADY\_IN\_PROGRESS\_ERROR       | 3010       | 이전 인증 프로세스가 완료되지 않았습니다. |
|                | AUTH\_INVALID\_GAMEBASE\_TOKEN           | 3011       | Gamebase Access Token이 유효하지 않아 로그아웃되었습니다.<br/>로그인을 다시 시도하세요. |
|                | AUTH\_AUTHENTICATION\_SERVER\_ERROR      | 3012       | 인증 서버로부터 오류가 발생했습니다. |
| TransferAccount| SAME\_REQUESTOR                          | 8          | 발급한 TransferAccount를 동일한 단말기에서 사용했습니다. |
|                | NOT\_GUEST\_OR\_HAS\_OTHERS              | 9          | 게스트가 아닌 계정에서 이전을 시도했거나, 계정에 게스트 이외의 IdP가 연동되어 있습니다. |
|                | AUTH_TRANSFERACCOUNT_EXPIRED             | 3041       | TransferAccount의 유효기간이 만료됐습니다. |
|                | AUTH_TRANSFERACCOUNT_BLOCK               | 3042       | 잘못된 TransferAccount를 여러번 입력하여 계정 이전 기능이 잠겼습니다. |
|                | AUTH_TRANSFERACCOUNT_INVALID_ID          | 3043       | TransferAccount의 Id가 유효하지 않습니다. |
|                | AUTH_TRANSFERACCOUNT_INVALID_PASSWORD    | 3044       | TransferAccount의 Password가 유효하지 않습니다. |
|                | AUTH_TRANSFERACCOUNT_CONSOLE_NO_CONDITION | 3045      | TransferAccount 설정이 되어있지 않습니다. <br/> NHN Cloud Gamebase Console에서 먼저 설정해주세요. |
|                | AUTH_TRANSFERACCOUNT_NOT_EXIST           | 3046       | TransferAccount가 존재하지 않습니다. TransferAccount를 먼저 발급받아주세요. |
|                | AUTH_TRANSFERACCOUNT_ALREADY_EXIST_ID    | 3047       | TransferAccount가 이미 존재합니다. |
|                | AUTH_TRANSFERACCOUNT_ALREADY_USED        | 3048       | TransferAccount가 이미 사용되었습니다. |
| Auth (Login)   | AUTH\_TOKEN\_LOGIN\_FAILED               | 3101       | 토큰 로그인에 실패했습니다.                          |
|                | AUTH\_TOKEN\_LOGIN\_INVALID\_TOKEN\_INFO | 3102       | 토큰 정보가 유효하지 않습니다.                        |
|                | AUTH\_TOKEN\_LOGIN\_INVALID\_LAST\_LOGGED\_IN\_IDP | 3103       | 최근에 로그인한 IdP 정보가 없습니다.                   |
| IdP Login      | AUTH\_IDP\_LOGIN\_FAILED                 | 3201       | IdP 로그인에 실패했습니다.                         |
|                | AUTH\_IDP\_LOGIN\_INVALID\_IDP\_INFO     | 3202       | IdP 정보가 유효하지 않습니다. (Console에 해당 IdP 정보가 없습니다.) |
| Add Mapping    | AUTH\_ADD\_MAPPING\_FAILED               | 3301       | 매핑 추가에 실패했습니다.                           |
|                | AUTH\_ADD\_MAPPING\_ALREADY\_MAPPED\_TO\_OTHER\_MEMBER | 3302       | 이미 다른 멤버에 매핑돼 있습니다.                      |
|                | AUTH\_ADD\_MAPPING\_ALREADY\_HAS\_SAME\_IDP | 3303       | 이미 같은 IdP에 매핑돼 있습니다.                     |
|                | AUTH\_ADD\_MAPPING\_INVALID\_IDP\_INFO   | 3304       | IdP 정보가 유효하지 않습니다. (Console에 해당 IdP 정보가 없습니다.) |
|                | AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP    | 3305       | 게스트 IdP로는 AddMapping이 불가능합니다. |
| Add Mapping Forcibly | AUTH_ADD_MAPPING_FORCIBLY_NOT_EXIST_KEY         | 3311       | 강제 매핑 키(ForcingMappingKey)가 존재하지 않습니다. <br/>ForcingMappingTicket을 다시 한번 확인해주세요. |
|                      | AUTH_ADD_MAPPING_FORCIBLY_ALREADY_USED_KEY      | 3312       | 강제 매핑 키(ForcingMappingKey)가 이미 사용되었습니다. |
|                      | AUTH_ADD_MAPPING_FORCIBLY_EXPIRED_KEY           | 3313       | 강제 매핑 키(ForcingMappingKey)의 유효기간이 만료되었습니다. |
|                      | AUTH_ADD_MAPPING_FORCIBLY_DIFFERENT_IDP         | 3314       | 강제 매핑 키(ForcingMappingKey)가 다른 IdP에 사용되었습니다. <br/>발급 받은 ForcingMappingKey는 같은 IdP에 강제 매핑을 시도 하는데 사용됩니다. |
|                      | AUTH_ADD_MAPPING_FORCIBLY_DIFFERENT_AUTHKEY     | 3315       | 강제 매핑 키(ForcingMappingKey)가 다른 계정에 사용되었습니다. <br/>발급 받은 ForcingMappingKey는 같은 IdP 및 계정에 강제 매핑을 시도 하는데 사용됩니다. |
| Remove Mapping | AUTH\_REMOVE\_MAPPING\_FAILED            | 3401       | 매핑 삭제에 실패했습니다.                           |
|                | AUTH\_REMOVE\_MAPPING\_LAST\_MAPPED\_IDP | 3402       | 마지막에 매핑된 IdP는 삭제할 수 없습니다.                |
|                | AUTH\_REMOVE\_MAPPING\_LOGGED\_IN\_IDP   | 3403       | 현재 로그인되어 있는 IdP입니다.                      |
| Logout         | AUTH\_LOGOUT\_FAILED                     | 3501       | 로그아웃에 실패했습니다.                            |
| Withdrawal     | AUTH\_WITHDRAW\_FAILED                   | 3601       | 탈퇴에 실패했습니다.                              |
|                | AUTH\_WITHDRAW\_ALREADY\_TEMPORARY\_WITHDRAW | 3602   | 이미 임시 탈퇴를 요청한 유저입니다.                    |
|                | AUTH\_WITHDRAW\_NOT\_TEMPORARY\_WITHDRAW | 3603       | 임시 탈퇴를 요청한 유저가 아닙니다.                     |
| Not Playable   | AUTH\_NOT\_PLAYABLE                      | 3701       | 플레이할 수 없는 상태입니다(점검 또는 서비스 종료 등).         |
| Auth(Unknown)  | AUTH\_UNKNOWN\_ERROR                     | 3999       | 알수 없는 오류입니다.(정의되지 않은 오류입니다).             |

* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [Entire Error Codes](../error-code.md#client-sdk)

**AUTH_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 외부 인증 라이브러리에서 오류가 발생했을 때 반환됩니다.
* 외부 인증 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```java
Gamebase.login(activity, provider, new GamebaseDataCallback<AuthToken>() {
    @Override
    public void onCallback(AuthToken data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            Log.d(TAG, "Login successful");
            ...
        } else {
            Log.e(TAG, "Login failed");

            // Gamebase Error Info
            int errorCode = exception.getCode();
            String errorMessage = exception.getMessage();

            if (errorCode == GamebaseError.AUTH_EXTERNAL_LIBRARY_ERROR) {
                // Third Party Detail Error Info
                int moduleErrorCode = exception.getDetailCode();
                String moduleErrorMessage = exception.getDetailMessage();

                ...
            }
        }
    }
});
```

* 상세 오류 코드는 각각의 외부 인증 라이브러리의 Developer 페이지를 참고하시기 바랍니다.
