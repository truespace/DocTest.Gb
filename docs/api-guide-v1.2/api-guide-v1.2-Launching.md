---
source: api-guide-v1.2.md
split: true
created_date_time: 20260406_141859
keyword: Launching
section: Launching
order: 5
---

## Launching

#### Get Simple Launching

Console 화면에서 설정한 서버 주소, 설치 URL 등의 클라이언트 설정 정보 및 현재 점검 상태/시간/ 메시지 등 클라이언트 앱 기동시 제공되는 Launching 정보들에 대해 서버에서 간략히 확인할수 있습니다.
현재 점검 설정 여부만을 확인하고 싶다면, [Check Maintenance] API를 사용하면 됩니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-launching/v1.2/apps/{appId}/launching/simple |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| osCode | Enum | true | OS 코드 <br>- AOS, IOS, WEB, WINDOWS |
| storeCode | Enum | true | 스토어 코드 <br>- GG: Google<br>- ONESTORE<br>- AS: AppStore |
| clientVersion | String | true | 콘솔에서 설정한 클라이언트 버전 |

**[Response Body]**

##### 정상
```json
{
    "header": {
        "resultCode": 0,
        "resultMessage": "String",
        "isSuccessful": true
    },
    "launchingData": {
        "status": {
            "code": 200,
            "message": "String"
        },
        "app": {
            "storeCode": "String",
            "accessInfo": {
                "serverAddress": "String",
                "csInfo": "String"
            },
            "relatedUrls": {
                "termsUrl": "String",
                "csUrl": "String",
                "punishRuleUrl": "String",
                "personalInfoCollectionUrl": "String"
            },
            "install": {
                "url": "String"
            }
        }
    }
}
```

##### 점검
```json
{
    "header": {
        "resultCode": 0,
        "resultMessage": "String",
        "isSuccessful": true
    },
    "launchingData": {
        "status": {
            "code": 303,
            "message": "String"
        },
        "app": {
            "storeCode": "String",
            "accessInfo": {
                "serverAddress": "String",
                "csInfo": "String"
            },
            "relatedUrls": {
                "termsUrl": "String",
                "csUrl": "String",
                "punishRuleUrl": "String",
                "personalInfoCollectionUrl": "String"
            },
            "install": {
                "url": "String"
            }
        },
        "maintenance": {
            "typeCode": "String",
            "beginDate": "2018-05-23T10:44:00+09:00",
            "endDate": "2022-01-01T10:44:00+09:00",
            "url": null,
            "reason": "String",
            "message": "String"
        }
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| status | Object | 현재 클라이언트 상태를 나타내는 정보 |
| status.code | int | 클라이언트 상태코드 <br><br>정상: 200 <br>업데이트 권장: 201, 업데이트 필수: 300 <br>서비스 종료: 302 <br>점검 중: 303 |
| status.message | String | 클라이언트 상태 메시지 |
| app | Object | 앱의 정보 |
| app.storeCode | String | 앱 스토어코드 <br>"GG", "AS" 등 |
| app.accessInfo | Object | 콘솔 앱 화면에서 설정한 정보 |
| app.accessInfo.serverAddress | String | 서버 주소<br>클라이언트에서 설정한 서버 주소의 우선순위가 높음. <br>클라이언트 서버 주소 미설정시, 앱 화면에서 설정한 서버 주소가 전달됨. |
| app.accessInfo.csInfo | String | 고객 센터 정보 |
| app.relatedUrls | Object | 앱 내에서 사용할 인앱 URL |
| app.relatedUrls.termsUrl | String | 이용약관 |
| app.relatedUrls.csUrl| String | 고객센터 |
| app.relatedUrls.punishRuleUrl | String | 이용 정지 규정 |
| app.relatedUrls.personalInfoCollectionUrl | String | 개인 정보동의 |
| app.install | Object | 앱 설치 정보 |
| app.install.url | String | 설치 URL |
| maintenance | Object | 점검 정보 |
| maintenance.typeCode | String | 점검 타입 코드 <br>APP: 게임에서 설정한 점검 <br>SYSTEM: Gamebase 시스템에서 설정한 점검 |
| maintenance.beginDate | Date | 점검 시작 시간 ISO 8601 |
| maintenance.endDate | Date | 점검 종료 시간 ISO 8601 |
| maintenance.url | String | 점검 URL |
| maintenance.reason | String | 점검 사유 |
| maintenance.message | String | default 점검 사유 메시지 |

<br>
<br>
