## Game > Gamebase > API v1.3 가이드

## Authentication

#### Token Authentication

로그인 유저에게 발급된 Gamebase Access Token이 유효한지를 검증합니다. Access Token이 정상이면 해당 유저의 정보를 리턴합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-gateway/v1.3/apps/{appId}/members/{userId}/tokens/{accessToken}?linkedIdP=false |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| userId | String | 로그인한 유저 아이디 |
| accessToken | String | 로그인한 유저에게 발급된 Gamebase Access Token |

**[Request Parameter]**

| Name | Type | Required |  Value |
| --- | --- | --- | --- |
| linkedIdP | boolean | Optional | true or false (기본값은 false) Access Token을 발급받을 때 사용된, IdP 관련 정보 포함 여부 |

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "String",
        "isSuccessful": true
    },
    "linkedIdP": {
        "idPCode": "String",
        "idPId": "String"
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
            },
            {
                "userId": "String",
                "authSystem": "String",
                "idPCode": "String",
                "authKey": "String",
                "regDate": "2019-08-27T17:41:05+09:00"
            }
        ],
        "temporaryWithdrawal": {
            "gracePeriodDate": "2020-04-18T09:12:01+09:00"
        }
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| linkedIdP | Object | 로그인한 유저가 사용한 IdP 정보 |
| linkedIdP.idPCode | String | [유저 인증 IdP](#identity-provider-code) |
| linkedIdP.idPId | String | IdP ID |
| member.userId | String | 유저 ID |
| member.lastLoginDate | String | 마지막으로 로그인한 시간 ISO 8601 <br>처음 로그인한 유저는 해당 값이 없음 |
| member.appId | String | appId |
| member.valid | String | [유저 상태](#member-valid-code)<br>로그인에 성공한 유저 값은 "Y" |
| member.regDate | String | 유저가 계정을 생성한 시간 |
| authList | Array[Object] | 유저 인증 IdP 관련 정보 |
| authList[].authSystem | String | Gamebase 내부적으로 사용되는 인증 시스템 <br>추후 유저 인증 시스템 지원 예정 |
| authList[].idPCode | String | [유저 인증 IdP](#identity-provider-code) |
| authList[].authKey | String | authSystem에서 IdP Id 별로 발급된 유저 구분 값 |
| temporaryWithdrawal | Object | 탈퇴 유예 관련 정보 <br>valid 가 "T" 값에서만 제공 |
| temporaryWithdrawal.gracePeriodDate | String | 탈퇴 유예 만료 시간 ISO 8601 |

**[Error Code]**

[오류 코드](./error-code/#server)

<br/>
#### Get IdP Token and Profiles

클라이언트에서 "Login with IdP"로 로그인 성공시 발급된 Gamebase Access Token으로, 로그인에 사용된 IdP의 Access Token 및 Profiles 정보를 조회합니다.

> [주의]
> IdP의 Access Token 유효시간은 IdP 별로 모두 다르고 일반적으로 짧습니다.
> 클라이언트에서 "Login as the Latest Login IdP"를 통해 로그인을 성공하고 이후 서버에서 해당 API를 호출한다면, 이미 IdP의 Access Token 이 만료되어, IdP 정보 획득에 실패 할수 있습니다.

<br/>

> [참고]
> IdP의 Access Token 만으로 정보를 획득 할 수 없는 IdP 들도 존재합니다.
> 예: appleid / iosgamecenter / kakaogame : Access Token으로 Server to Server에서 가져올 수 있는 정보가 없다.

<br/>

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-gateway/v1.3/apps/{appId}/members/{userId}/idps/{idPCode}?accessToken={accessToken} |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| userId | String | 로그인한 유저 아이디 |
| idPCode | String | [유저 인증 IdP](#identity-provider-code) |

**[Request Parameter]**

| Name | Type | Required |  Value |
| --- | --- | --- | --- |
| accessToken | String | Required | 로그인한 유저에게 발급된 Gamebase Access Token |

**[Response Body]**

```json
{
    "header": {
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "transactionId": "String",
        "isSuccessful": true
    },
    "idPProfile": {
        "sub": "String",
        "name": "String",
        "given_name": "String",
        "locale": "ko",
        "picture": "String"
    },
    "idPToken": {
        "idPCode": "google",
        "accessToken": "ya29.a0AfH6SMCF-MjD_-Eqi62Jm-51IPxnS6HpahqpxqbuaWZPXc68YMmW3sRdif4k7Dmp2Ppn1xzH-JQwPLDv4tMrDFAknG4m_lrHQt4J4En7DAG0bZV4z8uJZE1zYOXHp8"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| idPProfile | Map<String, Object> | 로그인한 유저가 사용한 IdP의 프로필<br>- IdP별로 모두 응답 형태(format)가 다르다 |
| idPToken | Object | 로그인한 유저가 사용한 IdP의 Access Token 정보 |
| idPToken.idPCode | String | [유저 인증 IdP](#identity-provider-code) |
| idPToken.accessToken | String | IdP Access Token |
<br>
<br>
