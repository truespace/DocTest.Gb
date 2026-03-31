## Game > Gamebase > iOS SDK 사용 가이드 > 인증

## Error Handling

| Category       | Error                                    | Error Code | Description                              |
| -------------- | ---------------------------------------- | ---------- | ---------------------------------------- |
| Auth           | TCGB\_ERROR\_INVALID\_MEMBER             | 6          | 잘못된 회원에 대한 요청입니다.                        |
|                | TCGB\_ERROR\_BANNED\_MEMBER              | 7          | 제재된 회원입니다.                               |
|                | TCGB\_ERROR\_AUTH\_USER\_CANCELED        | 3001       | 로그인이 취소되었습니다.                            |
|                | TCGB\_ERROR\_AUTH\_NOT\_SUPPORTED\_PROVIDER | 3002       | 지원하지 않는 인증 방식입니다.                        |
|                | TCGB\_ERROR\_AUTH\_NOT\_EXIST\_MEMBER    | 3003       | 존재하지 않거나 탈퇴한 회원입니다.                      |
|                | TCGB\_ERROR\_AUTH\_EXTERNAL\_LIBRARY\_INITIALIZATION\_ERROR    | 3006       |  외부 인증 라이브러리 초기화에 실패하였습니다.                      |
|                | TCGB\_ERROR\_AUTH\_EXTERNAL\_LIBRARY\_ERROR | 3009       | 외부 인증 라이브러리 오류입니다.<br/>상세 오류를 확인하십시오.  |
|                | TCGB\_ERROR\_AUTH\_INVALID\_GAMEBASE\_TOKEN | 3011       | Gamebase Access Token이 유효하지 않아 로그아웃되었습니다.<br/>로그인을 다시 시도하십시오. |
|                | AUTH\_AUTHENTICATION\_SERVER\_ERROR | 3012       | 인증 서버로부터 오류가 발생했습니다.  |
| Auth (Login)   | TCGB\_ERROR\_AUTH\_TOKEN\_LOGIN\_FAILED  | 3101       | 토큰 로그인에 실패했습니다.                          |
|                | TCGB\_ERROR\_AUTH\_TOKEN\_LOGIN\_INVALID\_TOKEN\_INFO | 3102       | 토큰 정보가 유효하지 않습니다.                        |
|                | TCGB\_ERROR\_AUTH\_TOKEN\_LOGIN\_INVALID\_LAST\_LOGGED\_IN\_IDP | 3103       | 최근에 로그인한 IdP 정보가 없습니다.                   |
| IdP Login      | TCGB\_ERROR\_AUTH\_IDP\_LOGIN\_FAILED    | 3201       | IdP 로그인에 실패하였습니다.                        |
|                | TCGB\_ERROR\_AUTH\_IDP\_LOGIN\_INVALID\_IDP\_INFO | 3202       | IdP 정보가 유효하지 않습니다. (Console에 해당 IdP 정보가 없습니다.) |
|                | TCGB\_ERROR\_AUTH\_IDP\_LOGIN\_EXTERNAL\_AUTHENTICATION\_REQUIRED | 3203       | Gamebase 로그인 요청 전에 먼저 IdP 로그인이 되어 있어야 합니다. |
| Add Mapping    | TCGB\_ERROR\_AUTH\_ADD\_MAPPING\_FAILED  | 3301       | 매핑 추가에 실패했습니다.                           |
|                | TCGB\_ERROR\_AUTH\_ADD\_MAPPING\_ALREADY\_MAPPED\_TO\_OTHER\_MEMBER | 3302       | 이미 다른 멤버에 매핑돼 있습니다.                      |
|                | TCGB\_ERROR\_AUTH\_ADD\_MAPPING\_ALREADY\_HAS\_SAME\_IDP | 3303       | 이미 같은 IdP에 매핑돼 있습니다.                     |
|                | TCGB\_ERROR\_AUTH\_ADD\_MAPPING\_INVALID\_IDP\_INFO | 3304       | IdP 정보가 유효하지 않습니다. (Console에 해당 IdP 정보가 없습니다.) |
|                | TCGB\_ERROR\_AUTH\_ADD\_MAPPING\_CANNOT\_ADD\_GUEST\_IDP | 3305  | 게스트 IdP로는 AddMapping이 불가능합니다. |
| Remove Mapping | TCGB\_ERROR\_AUTH\_REMOVE\_MAPPING\_FAILED | 3401       | 맵핑 삭제에 실패했습니다.                           |
|                | TCGB\_ERROR\_AUTH\_REMOVE\_MAPPING\_LAST\_MAPPED\_IDP | 3402       | 마지막에 맵핑된 IdP는 삭제할 수 없습니다.                |
|                | TCGB\_ERROR\_AUTH\_REMOVE\_MAPPING\_LOGGED\_IN\_IDP | 3403       | 현재 로그인되어 있는 IdP입니다.                     |
| Logout         | TCGB\_ERROR\_AUTH\_LOGOUT\_FAILED        | 3501       | 로그아웃에 실패했습니다.                            |
| Withdrawal     | TCGB\_ERROR\_AUTH\_WITHDRAW\_FAILED      | 3601       | 탈퇴에 실패했습니다.                              |
|                | TCGB\_ERROR\_AUTH\_WITHDRAW\_ALREADY\_TEMPORARY\_WITHDRAW | 3602   | 이미 임시 탈퇴를 요청한 유저입니다.                    |
|                | TCGB\_ERROR\_AUTH\_WITHDRAW\_NOT\_TEMPORARY\_WITHDRAW | 3603       | 임시 탈퇴를 요청한 유저가 아닙니다.                     |
| Not Playable   | TCGB\_ERROR\_AUTH\_NOT\_PLAYABLE         | 3701       | 플레이할 수 없는 상태입니다 (점검 또는 서비스 종료 등).        |
| Auth(Unknown)  | TCGB\_ERROR\_AUTH\_UNKNOWN\_ERROR        | 3999       | 알수 없는 오류입니다. (정의되지 않은 오류입니다.)            |




* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    - [오류 코드](./error-code/#client-sdk)


**TCGB\_ERROR\_AUTH\_EXTERNAL\_LIBRARY\_ERROR**

* 이 오류는 외부 인증 라이브러리에서 오류가 발생했을 때 반환됩니다.
* 외부 인증 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```objectivec
TCGBError *tcgbError = error; // TCGBError object via callback

NSInteger detailErrorCode = [error detailErrorCode];
NSString *detailErrorMessage = [error detailErrorMessage];

// If you use **description** method, you can get entire information of this object by JSON Format
NSLog(@"TCGBError: %@", [tcgbError description]);
```

* 상세 오류 코드는 각각의 외부 인증 라이브러리의 Developer 페이지를 참고하시기 바랍니다.
