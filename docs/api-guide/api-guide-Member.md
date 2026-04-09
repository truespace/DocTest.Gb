---
source: api-guide.md
section: "Member"
order: 6
split: true
created_date_time: 20260408_184906
keyword: Server API, Login, Mapping, Withdraw, Alert, Authentication, Console
---

## Member

#### Get Member

단일 유저에 대해 상세 정보를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-member/v1.3/apps/{appId}/members/{userId} |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| userId | String | 조회 대상 유저 ID |

**[Request Parameter]**

| Name | Type | Required |  Value |
| --- | --- | --- | --- |
| includeMemberInfo | boolean | Optional | true or false (기본값은 true) 유저 단말기, OS 등의 상세 정보 포함 여부 |

**[Response Body]**
```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "member": {
        "userId": "String",
        "valid": "Y",
        "appId": "String",
        "regDate": "2019-08-27T17:41:05+09:00",
        "lastLoginDate": "2019-08-27T17:41:05+09:00",
        "authList": [
            {
                "userId": "String",
                "authSystem": "String",
                "idPCode": "String",
                "authKey": "String",
                "regDate": "2019-08-27T17:41:05+09:00"
            }
        ]
    },
    "temporaryWithdrawal": {
        "gracePeriodDate": "2020-04-18T09:12:01+09:00"
    },
    "memberInfo": {
        "deviceCountryCode": "String",
        "usimCountryCode": "String",
        "language": "String",
        "osCode": "String",
        "telecom": "String",
        "storeCode": "String",
        "network": "String",
        "deviceModel": "String",
        "osVersion": "String",
        "sdkVersion": "String",
        "clientVersion": "String"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| member | Object | 조회된 유저의 기본 정보 |
| member.userId | String | 유저 ID |
| member.valid | Enum | [유저 상태](#member-valid-code) |
| member.appId | String | appId |
| member.regDate | String | 유저가 계정을 생성한 시간 |
| member.lastLoginDate | String | 마지막으로 로그인한 시간 <br>처음 로그인한 유저 또는 탈퇴한 유저는 해당 값이 없음 |
| member.authList | Array[Object] | 유저 인증 IdP 관련 정보 |
| member.authList[].userId | String | 유저 ID |
| member.authList[].authSystem | String | Gamebase 내부적으로 사용되는 인증 시스템 <br>추후 유저 인증 시스템 지원 예정 |
| member.authList[].idPCode | String | [유저 인증 IdP](#identity-provider-code) |
| member.authList[].authKey | String | authSystem에서 발급된 유저 구분 값 |
| member.authList[].regDate | String | IdP 정보가 유저 계정과 매핑된 시간 |
| temporaryWithdrawal | Object | 탈퇴 유예 관련 정보 <br>valid 가 "T" 값에서만 제공 |
| temporaryWithdrawal.gracePeriodDate | String | 탈퇴 유예 만료 시간 ISO 8601 |
| memberInfo | Object | 유저에 대한 부가 정보<br>탈퇴한 유저는 해당 정보 없음 |
| memberInfo.deviceCountryCode | String | 유저 단말기의 국가 설정 |
| memberInfo.usmCountryCode | String | 유저 USIM의 국가 코드 |
| memberInfo.language | String | 유저 단말기 언어, ISO 639-1 |
| memberInfo.osCode | String | [OS 코드](#os-code) |
| memberInfo.telecom | String | 통신사 |
| memberInfo.storeCode | String | [스토어 코드](#store-code) |
| memberInfo.network | String | 네트워크 환경 <br>3g, WiFi 등|
| memberInfo.deviceModel | String | 유저 단말기의 모델명 |
| memberInfo.osVersion | String | 유저 단말기의 OS 버전 |
| memberInfo.sdkVersion | String | SDK 버전 |
| memberInfo.clientVersion | String | 클라이언트 버전 |

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Get Members

다수의 유저 정보를 간략히 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-member/v1.3/apps/{appId}/members |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Body]**

```json
["userId", "userId", "userId"]
```

| Type | Required | Value |
| --- | --- | --- |
| Array[String] | Required | 조회 대상 유저 ID |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "memberList": [
        {
            "userId": "String",
            "valid": "Y",
            "appId": "String",
            "regDate": "2019-08-27T17:41:05+09:00"
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| memberList | Array[Object] | 조회된 유저의 기본 정보 |
| memberList[].userId | String | 유저 ID |
| memberList[].valid | Enum | [유저 상태](#member-valid-code) |
| memberList[].appId | String | appId |
| memberList[].regDate | String | 계정 생성 시간 |

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Get IdP Information

유저 ID로 매핑된 IdP 정보를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-member/v1.3/apps/{appId}/auth/authKeys |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Body]**

```json
["userId", "userId", "userId"]
```

| Type | Required | Value |
| --- | --- | --- |
| Array[String] | Required | 조회 대상 유저 ID |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "result": {
        "String": [
            {
                "authKey": "String",
                "idPCode": "gbid",
                "authSystem": "String"
            }
        ]
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 조회된 유저의 기본 정보 <br>userId가 key, IdP 정보가 value인 object|
| authkey | String | authSystem에서 발급된 유저 구분 값 |
| IdPCode | String | [유저 인증 IdP](#identity-provider-code) |
| authSystem | String | Gamebase 내부적으로 사용되는 인증 시스템 <br>추후 유저 인증 시스템 지원 예정 |

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Get UserId Information with Auth key

유저 인증 키에 매핑된 유저 ID를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-member/v1.3/apps/{appId}/members/userIds/authKeys?authSystem={authSystem} |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| authSystem | String | Required | Gamebase 내부적으로 사용되는 인증 시스템 추후 유저 인증 시스템 지원 예정 현재는 gbid |

**[Request Body]**

```json
["authKey", "authKey", "authKey"]
```

| Type | Required | Value |
| --- | --- | --- |
| Array[String] | Required | authSystem에서 발급된 authKey |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "result": {
        "String": "String"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 조회된 유저의 기본 정보 authKey가 key이고, userId가 value인 object|

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Get UserId Information with IdP Id

IdP ID로 매핑된 유저 ID 정보를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-gateway/v1.3/apps/{appId}/idps/{idPCode}/members |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| idPCode | String | [유저 인증 IdP](#identity-provider-code) |

**[Request Body]**

```json
["idPId", "idPId", "idPId"]
```

| Type | Required | Value |
| --- | --- | --- |
| Array[String] | Required | 조회 대상 유저의 IdP ID <br> 조회 대상 리스트 크기는 최대 300 |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "result": {
        "idPId": "userId",
        "idPId": "userId",
        "idPId": "userId"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Map<String, String> | 조회된 유저의 ID 정보 <br>- IdP ID가 key, Gamebase userId 가 value<br>- 조회 요청한 IdP ID를 가지는 userId 정보가 없을 경우 응답 결과에 존재하지 않습니다. |

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Ban

유저들을 이용 정지 상태로 변경합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-gateway/v1.3/apps/{appId}/members/ban |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

없음

**[Request Body]**

```json
{
    "userIdList": [
        "userId-1", "userId-2"
    ],
    "banTypeCode": "TEMPORARY",
    "end": "2022-05-10T06:03:50.000+09:00",
    "templateCode": 0,
    "banReason": "string",
    "flags": "leaderboard",
    "banCaller": "APP_SERVER",
    "regUser": "GAME-SERVER"
}
```

| Key | Type | Description |
| --- | --- | --- |
| userIdList | Array[String] | 이용 정지 대상 유저 ID |
| banTypeCode | Enum | 이용 정지 타입. TEMPORARY or PERMANENT |
| end | String | 이용 정지 종료 시간(ISO 8601 표준 시간) <br>- TEMPORARY 타입일 때 필수 값 |
| templateCode | Integer | 이용 정지 시 표시될 메시지에 사용되는 템플릿의 템플릿 코드 <br>- 해당 값은 Console **이용 정지 > 템플릿** 상세 조회 화면에서 확인 가능 |
| banReason | String | 이용 정지 사유 |
| flags | String | 이용 정지 유저의 리더보드 데이터도 함께 삭제하기를 원한다면 'leaderboard'로 설정 |
| banCaller | String | 이용 정지 API를 호출한 주체로, 'APP_SERVER' 고정 값으로 설정 |
| regUser | String | Console 이용 정지 화면에서 표시할 이름 |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "failedUserIdList": ["userId-1"]
}
```

| Key | Type | Description |
| --- | --- | --- |
| failedUserIdList | Array[String] | 이용 정지 등록에 실패한 유저 ID |

**[Error Code]**

[오류 코드](../error-code.md#server)

</br>

#### Ban Histories

유저 이용 정지 이력을 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-member/v1.3/apps/{appId}/members/bans |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| begin | String | Required | 이용 정지 이력 조회 시작 시간(ISO 8601 표준 시간, UTF-8 Encoding 필요) <br>예: yyyy-MM-dd'T'HH:mm:ss.SSSXXX |
| end | String | Required | 이용 정지 이력 조회 종료 시간(ISO 8601 표준 시간, UTF-8 Encoding 필요) <br>begin ~ end 사이 시간에 이용 정지가 되었다면 조회 결과에 존재 |
| page | String | Optional | 조회하고자 하는 페이지. 0부터 시작 |
| size | String | Optional | 페이지당 데이터 개수 |
| order | String | Optional | 조회 데이터 정렬 방법. ASC or DESC |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "pagingInfo": {
        "first": true,
        "last": true,
        "numberOfElements": 0,
        "page": 0,
        "size": 0,
        "totalElements": 0,
        "totalPages": 0
    },
    "result": [
        {
            "userId": "String",
            "banCaller": "CONSOLE",
            "banReason": "String",
            "banType": "TEMPORARY",
            "beginDate": "2019-08-27T17:41:05+09:00",
            "endDate": "2019-08-28T17:41:05+09:00",
            "flags": "String",
            "name": "String",
            "templateCode": 0
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| pagingInfo | Object | 조회된 페이징 정보 |
| pagingInfo.first | boolean | 첫 번째 페이지이면 true |
| pagingInfo.last | boolean | 마지막 페이지이면 true |
| pagingInfo.numberOfElements | int | 전체 데이터 수 |
| pagingInfo.page | int | 페이지 번호 |
| pagingInfo.size | int | 페이지당 데이터 개수 |
| pagingInfo.totalElements | int | 전체 데이터 수 |
| pagingInfo.totalPages | int | 전체 페이지 수 |
| result | Array[Object] | 조회된 이용 정지 내역 |
| result.userId | String | 유저 ID |
| result.banCaller | String | 이용 정지 호출 주체 |
| result.banReason | String | 이용 정지 사유 |
| result.banType | String | 이용 정지 타입. TEMPORARY or PERMANENT |
| result.beginDate | Long | 이용 정지 시작 시간 |
| result.endDate | Long | 이용 정지 종료 시간<br>PERMANENT 타입인 경우 해당 값은 존재하지 않음 |
| result.flags | String | 콘솔에서 이용 정지 등록 시 리더보드 삭제를 선택한 경우 'leaderboard'로 반환 |
| result.name | String | 콘솔에서 등록한 템플릿 이름 |
| result.templateCode | Long | 콘솔에서 등록한 이용 정지 템플릿 코드 값 |


**[Error Code]**

[오류 코드](../error-code.md#server)

</br>

#### Get Ban Members

이용 정지 상태인 유저를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-member/v1.3/apps/{appId}/members/bans/current |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| page | String | Optional | 조회하고자 하는 페이지. 0부터 시작 |
| size | String | Optional | 페이지당 데이터 개수 |
| order | String | Optional | 조회 데이터 정렬 방법. ASC or DESC |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "pagingInfo": {
        "first": true,
        "last": true,
        "numberOfElements": 0,
        "page": 0,
        "size": 0,
        "totalElements": 0,
        "totalPages": 0
    },
    "result": [
        {
            "userId": "String",
            "banCaller": "CONSOLE",
            "banReason": "String",
            "banType": "TEMPORARY",
            "beginDate": "2019-08-27T17:41:05+09:00",
            "endDate": "2019-08-28T17:41:05+09:00",
            "flags": "String",
            "name": "String",
            "templateCode": 0
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| pagingInfo | Object | 조회된 페이징 정보 |
| pagingInfo.first | boolean | 첫 번째 페이지이면 true |
| pagingInfo.last | boolean | 마지막 페이지이면 true |
| pagingInfo.numberOfElements | int | 전체 데이터 수 |
| pagingInfo.page | int | 페이지 번호 |
| pagingInfo.size | int | 페이지당 데이터 개수 |
| pagingInfo.totalElements | int | 전체 데이터 수 |
| pagingInfo.totalPages | int | 전체 페이지 수 |
| result | Array[Object] | 조회된 이용 정지 내역 |
| result.userId | String | 유저 ID |
| result.banCaller | String | 이용 정지 호출 주체 |
| result.banReason | String | 이용 정지 사유 |
| result.banType | String | 이용 정지 타입. TEMPORARY or PERMANENT |
| result.beginDate | Long | 이용 정지 시작 시간 |
| result.endDate | Long | 이용 정지 종료 시간<br>PERMANENT 타입인 경우 해당 값은 존재하지 않음 |
| result.flags | String | 콘솔에서 이용 정지 등록 시 리더보드 삭제를 선택한 경우 'leaderboard'로 반환 |
| result.name | String | 콘솔에서 등록한 템플릿 이름 |
| result.templateCode | Long | 콘솔에서 등록한 이용 정지 템플릿 코드 값 |


**[Error Code]**

[오류 코드](../error-code.md#server)

</br>

#### Ban Release

유저들을 이용 정지 해제 상태, 즉 정상 상태로 변경합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| DELETE | /tcgb-gateway/v1.3/apps/{appId}/members/ban |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

없음

**[Request Body]**

```json
{
    "userIdList": [
        "userId-1", "userId-2"
    ],
    "banReleaseReason": "string",
    "banReleaseCaller": "APP_SERVER",
    "releaseUser": "GAME-SERVER"
}
```

| Key | Type | Description |
| --- | --- | --- |
| userIdList | Array[String] | 이용 정지 해제 대상 유저 ID |
| banReleaseReason | String | 이용 정지 해제 사유 |
| banReleaseCaller | String | 이용 정지 해제 API를 호출한 주체로, 'APP_SERVER' 고정 값으로 설정 |
| releaseUser | String | Console 이용 정지 해제 화면에서 표시할 이름 |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "failedUserIdList": ["userId-1"]
}
```

| Key | Type | Description |
| --- | --- | --- |
| failedUserIdList | Array[String] | 이용 정지 해제에 실패한 유저 ID |

**[Error Code]**

[오류 코드](../error-code.md#server)

</br>

#### Ban Release Histories

유저 이용 정지 해제 이력을 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-member/v1.3/apps/{appId}/members/bans/release |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| begin | String | Required | 이용 정지 해제 이력 조회 시작 시간(ISO 8601 표준 시간, UTF-8 Encoding 필요) <br>예: yyyy-MM-dd'T'HH:mm:ss.SSSXXX |
| end | String | Required | 이용 정지 해제 이력 조회 종료 시간(ISO 8601 표준 시간, UTF-8 Encoding 필요) <br>begin ~ end 사이 시간에 이용 정지가 해제 되었다면 조회 결과에 존재 |
| page | String | Optional | 조회하고자 하는 페이지. 0부터 시작 |
| size | String | Optional | 페이지당 데이터 개수 |
| order | String | Optional | 조회 데이터 정렬 방법. ASC or DESC |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "pagingInfo": {
        "first": true,
        "last": true,
        "numberOfElements": 0,
        "page": 0,
        "size": 0,
        "totalElements": 0,
        "totalPages": 0
    },
    "result": [
        {
            "userId": "String",
            "banCaller": "CONSOLE",
            "banReason": "String",
            "banType": "TEMPORARY",
            "beginDate": "2019-08-27T17:41:05+09:00",
            "endDate": "2019-08-29T17:41:05+09:00",
            "flags": "String",
            "name": "String",
            "templateCode": 0,
            "releaseCaller": "CONSOLE",
            "releaseDate": "2019-08-30T18:41:05+09:00",
            "releaseReason": "String"
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| pagingInfo | Object | 조회된 페이징 정보 |
| pagingInfo.first | boolean | 첫 번째 페이지이면 true |
| pagingInfo.last | boolean | 마지막 페이지이면 true |
| pagingInfo.numberOfElements | int | 전체 데이터 수 |
| pagingInfo.page | int | 페이지 번호 |
| pagingInfo.size | int | 페이지당 데이터 개수 |
| pagingInfo.totalElements | int | 전체 데이터 수 |
| pagingInfo.totalPages | int | 전체 페이지 수 |
| result | Array[Object] | 조회된 이용 정지 정보 |
| result.userId | String | 유저 ID |
| result.banCaller | String | 이용 정지 호출 주체 |
| result.banReason | String | 이용 정지 사유 |
| result.banType | String | 이용 정지 타입. TEMPORARY or PERMANENT |
| result.beginDate | String | 이용 정지 시작 시간 |
| result.endDate | String | 이용 정지 종료 시간 |
| result.flags | String | 콘솔에서 이용 정지 등록 시 리더보드 삭제를 선택한 경우 'leaderboard'로 반환 |
| result.name | String | 콘솔에서 등록한 템플릿 이름 |
| result.templateCode | Long | 콘솔에서 등록한 이용 정지 템플릿 코드 값 |
| result.releaseCaller | String | 이용 정지 해제 주체 |
| result.releaseReason | String | 이용 정지 해제 사유 |
| result.releaseDate | String | 이용 정지 해제 시간 |


**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Validate TransferAccount

게스트 계정 이전을 위해 발급 받은 ID 및 PASSWORD의 유효성 검사를 수행합니다. 유효한 TransferAccount인 경우 발급 받은 userId 정보를 반환합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-gateway/v1.3/apps/{appId}/members/transfer-account |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

없음

**[Request Body]**

```json
{
    "account": {
        "id": "198704206255",
        "password": "Zw548q7zE"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| account.id | String | 유효성 검증을 수행할 ID |
| account.password | String | 유효성 검증을 수행할 PASSWORD |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "member": {
        "userId": "String",
        "valid": "Y",
        "appId": "String",
        "regDate": "2019-08-27T17:41:05+09:00",
        "lastLoginDate": "2019-08-27T17:41:05+09:00"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| member | Object | 조회된 유저의 기본 정보 |
| member.userId | String | 유저 ID |
| member.valid | Enum | [유저 상태](#member-valid-code) |
| member.appId | String | appId |
| member.regDate | String | 유저가 계정을 생성한 시간 |
| member.lastLoginDate | String | 마지막으로 로그인한 시간 <br>처음 로그인한 유저는 해당 값이 없음 |

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>

#### Withdraw

유저 계정을 탈퇴 처리합니다.

> [참고]
> SDK의 탈퇴 API를 사용하지 않고 서버 탈퇴 API를 사용하여 계정 탈퇴를 구현한 경우, 클라이언트에서는 탈퇴 성공 후 SDK의 logout API를 호출하여 캐시되어 있는 토큰 등의 데이터 삭제가 필요합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| DELETE | /tcgb-gateway/v1.3/apps/{appId}/members/{userId}?regUser={regUser} |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| userId | String | 탈퇴 대상 유저 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| regUser | String | Required | 탈퇴를 요청한 시스템 혹은 운영자 정보로 공백 없이 입력 <br> - 해당 정보는 Console > '멤버' 페이지의 '탈퇴 이력' 화면에서 확인 가능 |

**[Request Body]**

없음

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    }
}
```

**[Error Code]**

[오류 코드](../error-code.md#server)

</br>

#### Withdraw Histories

특정 기간 동안 탈퇴한 유저들을 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-member/v1.3/apps/{appId}/logs/withdrawal |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| begin | String | Required | 이력 조회 시작 시간(ISO 8601 표준 시간, UTF-8 Encoding 필요) <br>**최근 1년 이내의 데이터만 제공** |
| end | String | Required | 이력 조회 종료 시간(ISO 8601 표준 시간, UTF-8 Encoding 필요) <br>예) yyyy-MM-dd'T'HH:mm:ss.SSSXXX / 2021-09-11T00%3a00%3a00%2b09%3a00 |
| page | String | Optional | 조회하고자 하는 페이지. 0부터 시작 |
| size | String | Optional | 페이지당 데이터 개수 |
| order | String | Optional | 조회 데이터 정렬 방법. ASC or DESC |
| eventLogType | Enum | Optional | [탈퇴 이벤트 발생 경로](#withdrawal-event-type) |
| includePending | boolean | Optional | 탈퇴 진행 중인 중간 상태값 포함 여부 <br> - false(기본값) 설정 시, 최종 탈퇴가 완료된 로그만 필터링하여 제공 <br> - eventLogType이 입력된 경우 해당 값이 우선 적용 됨 |

**[Response Body]**

```json
{
    "header": {
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "transactionId": "String",
        "isSuccessful": true
    },
    "pagingInfo": {
        "totalPages": 1,
        "totalElements": 2,
        "numberOfElements": 2,
        "first": true,
        "last": true,
        "page": 0,
        "size": 100
    },
    "result": [
        {
            "userId": "String",
            "date": "2022-03-27T17:40:00+09:00",
            "type": "WAA",
            "regUser": null
        },
        {
            "userId": "String",
            "date": "2022-03-27T17:41:05+09:00",
            "type": "WACS",
            "regUser": "String"
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| pagingInfo | Object | 조회된 페이징 정보 |
| pagingInfo.first | boolean | 첫 번째 페이지이면 true |
| pagingInfo.last | boolean | 마지막 페이지이면 true |
| pagingInfo.numberOfElements | int | 전체 데이터 수 |
| pagingInfo.page | int | 페이지 번호 |
| pagingInfo.size | int | 페이지당 데이터 개수 |
| pagingInfo.totalElements | int | 전체 데이터 수 |
| pagingInfo.totalPages | int | 전체 페이지 수 |
| result | Array[Object] | 조회된 탈퇴 유저 내역 |
| result.userId | String | 유저 ID |
| result.date | String | 탈퇴 일시 |
| result.type | Enum | [탈퇴 이벤트 발생 경로](#withdrawal-event-type)|
| result.regUser | String | 탈퇴 API를 호출한 주체<br>- 해당 값이 **null** 이면 client SDK에서 호출됨 |

**[Error Code]**

[오류 코드](../error-code.md#server)

</br>

#### SIWA Account Webhook

**Sign In with Apple (SIWA)** 유저의 계정 상태 변경을 Apple 서버로부터 알림 받아 처리하는 Webhook API입니다.
이 Webhook의 URI를 Apple Developer Site의 Sign In with Apple 서비스 설정에 등록해야 합니다. 

> [참고]
> 해당 API는 Apple 서버가 직접 호출하므로 헤더에 별도의 인증 키(Secret Key) 설정이 필요하지 않습니다.
</br>

##### 지원 이벤트 및 처리 로직
해당 Webhook 이벤트는 동의 철회(consent-revoked)와 계정 삭제(account-delete) 두 가지를 지원하며, 이벤트에 따라 다음과 같이 처리됩니다.

- 동의 철회(consent-revoked)
    - 처리: 유저의 계정은 유지되지만, 현재 발급된 Gamebase Access Token은 즉시 만료됩니다.
- 계정 삭제(account-delete)
    - 처리: 유저의 계정은 즉시 탈퇴 처리됩니다.
    - 탈퇴된 계정은 **Withdraw Histories** API에서 **eventLogType=WAAI** 파라미터로 조회할 수 있습니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-gateway/v1.3/apps/{appId}/webhooks/apple/notifications |


**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

</br>
</br>
