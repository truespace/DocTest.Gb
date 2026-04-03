---
source: api-guide-v1.2.md
section: "Maintenance-to-Leaderboard"
order: 3
created_date: 2026-04-03
---

## Maintenance

#### Check Maintenance Set

현재 점검이 설정되어 있는지 여부를 확인합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-launching/v1.2/apps/{appId}/maintenances/under-maintenance |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

없음

**[Response Body]**

```json
{
    "header": {
        "transactionId": "String",
        "resultCode": 0,
        "resultMessage": "String",
        "isSuccessful": true
    },
    "appId": "",
    "underMaintenance": true,
    "maintenances": [
        {
            "typeCode": "APP",
            "beginDate": "2017-01-01T12:10:00+07:00",
            "endDate": "2017-02-01T12:17:00+07:00",
            "url": "http://url.info",
            "message": "maintenance message",
            "targetStores": [
                "GG",
                "AS",
                "ONESTROE"
            ]
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| underMaintenance | boolean | 현재 점검 설정 여부 |
| maintenances | Object | 점검이 설정되어 있다면 점검 기본 정보 |
| maintenances.typeCode | Enum | APP: 게임에서 설정한 점검 <br>SYSTEM: Gamebase 시스템에서 설정한 점검 |
| maintenances.beginDate | String | 점검 시작 시간. ISO 8601 |
| maintenances.endDate | String | 점검 종료 시간. ISO 8601 |
| maintenances.url | String | 상세 점검 URL |
| maintenances.message | String | 점검 메시지 |
| maintenances.targetStores | Array[Enum] | 특정 클라이언트에 대해서만 점검을 설정했을 때 점검 설정된 클라이언트의 스토어 코드<br>- GG: Google<br>- ONESTORE<br>- AS: AppStore |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>
<br>

## Coupon

#### Check Validation And Consume Coupon

콘솔에서 발급된 쿠폰 코드의 유효성 검증 및 쿠폰 상태를 변경합니다. 유효한 쿠폰이면 소비 상태로 변경하고, 응답 결과로 지급할 아이템 정보를 반환합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-gateway/v1.2/apps/{appId}/members/{userId}/coupons/{couponCode}?storeCode={storeCode} |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| userId | String | 쿠폰을 사용할 userId |
| couponCode | String | 쿠폰 코드 |

**[Request Parameter]**

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| storeCode | String | optional | 콘솔에서 특정 스토어만 사용 가능하도록 쿠폰을 발급 받았다면, 스토어 코드를 전달해야 함<br>전체 스토어인 경우 ALL 또는 파라미터 생략<br>- GG: Google<br>- ONESTORE: ONE store<br>- AS: AppStore |

**[Response Body]**

```json
{
    "header": {
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "result": {
        "title": "Coupon Title",
        "benefits": [
            {
                "itemId": "heart",
                "amount": 10
            },
            {
                "itemId": "diamond",
                "amount": 20
            }
        ]
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Object | 쿠폰 정보 |
| result.title | String | 쿠폰 이름 |
| result.benefits | Array[Object] | 지급할 아이템 정보 |
| result.benefits.itemId | String | 아이템 ID |
| result.benefits.amount | Integer | 아이템 개수 |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>
<br>

## Purchase(IAP)

#### Consume

Google Play Store, App Store, ONEStore 등 스토어 결제가 정상으로 완료되었다면 유저에게 아이템 지급 및 서버 내부적으로 이력을 기록한 후에, Gmaebase에 결제를 소비를 알립니다. 결제 1건당 1번만 결제를 소비할 수 있으며 결제 상태가 정상이 아니면 소비되지 않습니다.

> [참고]
> 상품 등록 시 상품 유형이 일회성(CONSUMABLE)인 아이템 결제에 대해서만 소비(consume) 처리됩니다.
> 결제 1건당 1번 소비 가능하며, 결제 소비를 하지 않은 결제는 IAP에서는 아이템을 지급하지 않은 것으로 간주합니다.

소비(consume)하지 않은 결제 내역은 SDK 및 서버의 미소비 결제 내역 조회 API를 통해 조회할 수 있습니다. API를 통해 미소비 결재 내역이 존재하더라도, 게임 서버 내부적으로 아이템 지급에 대한 이력을 가지고 있다면 게임 서버 내부 지급 이력을 우선으로 판단하면 됩니다.
(네트워크 장애 등으로 API timeout이 발생하면 Gamebase에서는 지급 완료 처리가 되었지만, API 응답 실패로 게임 서버에서는 실제로 유저에게는 아이템 지급이 안될 수 있음)

> [참고]
> 게임 내부적으로 아이템 지급 이력을 모두 관리할 수 없다면 해당 API의 request timeout을 10초 이상으로 하고, API timout 발생시 만이라도 이력을 기록하여 중복 지급 혹은 미지급 이슈에 대한 방안이 필요함

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.2/apps/{appId}/consume |

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
    "paymentSeq": "2019091931571201",
    "accessToken": "90fD1bs1guXwY6aZ7rseEKYW_6gMCISjDASgten4MD6O7XZD7VRjZcs8OTm8lOQVFTegoY4WK78P2WQCMm7cx"
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| paymentSeq | String | mandatory | 결제 번호 |
| accessToken | String | mandatory  | 결제 인증 토큰(로그인 인증 토큰이 아님) |

> [참고]
> 클라이언트에서 requestPurchase API 호출 시 응답으로 오는 purchaseToken 값이 accessToken으로 사용


**[Response Body]**

```json
{
    "header": {
        "isSuccessful": true,
        "resultCode": 0,
        "resultMessage": "SUCCESS"
    },
    "result": {
        "price": 1500.0,
        "currency": "KRW",
        "productSeq": 12345
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Object | 결제 기본 정보 |
| result.price | Float | 결제 가격 |
| result.currency  | String  | 결제 통화  |
| result.productSeq | Long | 결제 아이템 번호(콘솔에 등록된 아이템 고유 번호) |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

#### List Consumables

결제가 완료되었지만 아직 소비(consume)되지 않은, 미소비 결제 내역을 조회할 수 있습니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.2/apps/{appId}/consumable |

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
    "marketId": "GG",
    "userChannel": "GF",
    "userKey": "QXG774PMRZMWR3BR"
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| marketId | String | mandatory | 스토어 코드<br>GG: Google, AS: Apple, ONESTORE: 원스토어 |
| userChannel | String | mandatory  | 유저 채널<br>현재는 미구현 상태로 항상 `GF`값을 설정  |
| userKey | String | mandatory  | 유저 ID  |

**[Response Body]**

```json
{
    "header": {
        "isSuccessful": true,
        "resultCode": 0,
        "resultMessage": "success"
    },
    "result": [
        {
            "paymentSeq": "2016122110023124",
            "productSeq": 1000292,
            "currency": "KRW",
            "price": 1000.0,
            "accessToken": "oJgM1EfDRjnQY7yqhWCUVgAXsSxLWq698t8QyTzk3NeeSoytKxtKGjldTc1wkSktgzjsfkVTKE50DoGihsAvGQ"
        },
        {
            "paymentSeq": "2016122110023125",
            "productSeq": 1000292,
            "currency": "KRW",
            "price": 1000.0,
            "accessToken": "7_3zXyNJub0FNLed3m9XRAAXsSxLWq698t8QyTzk3NeeSoytKxtKGjldTc1wkSktgzjsfkVTKE50DoGihsAvGQ"
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 결제 기본 정보 |
| result[].paymentSeq | String  |  결제 번호 |
| result[].productSeq | Long | 결제 아이템 번호(콘솔에 등록된 아이템 고유 번호) |
| result[].currency  | String  | 결제 통화  |
| result[].price | Float | 결제 가격 |
| result[].accessToken | String | 결제 인증 토큰 |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

### List Active Subscriptions

유저가 현재 구독 중인 결제를 조회할 수 있습니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.2/apps/{appId}/active-subscriptions |

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
    "marketId": "GG",
    "packageName": "com.toast.gamebase",
    "userChannel": "GF",
    "userKey": "QXG774PMRZMWR3BR"
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| marketId | String | mandatory | 스토어 코드<br>GG: Google, AS: Apple, ONESTORE: 원스토어 |
| packageName | String | mandatory | 콘솔에 등록한 앱의 packageName |
| userChannel | String | mandatory  | 유저 채널<br>현재는 미구현 상태로 항상 `GF`값을 설정  |
| userKey | String | mandatory  | 유저 ID  |

**[Response Body]**

```json
{
    "header": {
        "isSuccessful": true,
        "resultCode": 0,
        "resultMessage": "SUCCESS"
    },
    "result": [
        {
            "channel": "GF",
            "userId": "string",
            "paymentSeq": "2018102610330423",
            "appId": "com.toast.gamebase",
            "productId": "subs_p1w",
            "productType": "AUTO_RENEWABLE",
            "productSeq": 1002904,
            "currency": "KRW",
            "price": 1000.0,
            "paymentId": "GPA.3375-2193-1175-57698",
            "originalPaymentId": "GPA.3375-2193-1175-57698",
            "purchaseTimeMillis": 1540522998289,
            "expiryTimeMillis": 1541134994548
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 결제 기본 정보 |
| result[].channel  | String  | 유저 채널  |
| result[].userId  | String  | 유저 ID  |
| result[].paymentSeq | String  |  결제 번호 |
| result[].appId | String  |  패키지 이름 |
| result[].productId | String  |  스토어에 등록된 상품(아이템) 식별자 |
| result[].productType | String  |  상품(아이템) 타입<br>구독: AUTO_RENEWABLE |
| result[].productSeq | Long | 결제 아이템 번호(콘솔에 등록된 아이템 고유 번호) |
| result[].currency  | String  | 결제 통화  |
| result[].price | Float | 결제 가격 |
| result[].paymentId | String | 최근 갱신된 스토어 결제 번호 |
| result[].originalPaymentId | String | 최초 스토어 결제 번호 |
| result[].purchaseTimeMillis | Long | 최근 갱신된 시간 |
| result[].expiryTimeMillis | Long | 구독 만료 시간 |


**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>
<br>

## Leaderboard

Gamebase는 NHN Cloud Leaderboard 서비스의 서버 API에 대해 **Wrapping** 기능을 제공합니다. Wrapping 기능을 사용하면 사용자 서버에서 일관된 인터페이스로 NHN Cloud 서비스들을 사용할 수 있습니다.


#### Wrapping API
| API | Method | Wrapping URI | Leaderboard URI |
| --- | --- | --- | --- |
| Factor에 등록된 사용자 수 조회 | GET | /tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/user-count | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/user-count |
| 단일 사용자 점수/순위 조회 | GET | /tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/users?userId={userId} | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users?userId={userId} |
| 다수 사용자 점수/순위 조회 | POST | /tcgb-leaderboard/v1.2/apps/{appId}/get-users | /leaderboard/v2.0/appkeys/{appKey}/get-users |
| 일정 범위의 전체 점수/순위 조회 | GET | /tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/users?start={start}&size={size} | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users?start={start}&size={size} |
| 단일 사용자 점수 등록 | POST | /tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/users/{userId}/score | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users/{userId}/score |
| 단일 사용자 점수/ExtraData 등록 | POST | /tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/users/{userId}/score-with-extra | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users/{userId}/score-with-extra |
| 다수 사용자 점수 등록 | POST | /tcgb-leaderboard/v1.2/apps/{appId}/scores | /leaderboard/v2.0/appkeys/{appKey}/scores |
| 다수 사용자 점수/ExtraData 등록 | POST | /tcgb-leaderboard/v1.2/apps/{appId}/scores-with-extra | /leaderboard/v2.0/appkeys/{appKey}/score-with-extra |
| 단일 사용자 Leaderboard정보 삭제 | DELETE | /tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/users | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users |


**해당 API에 대한 상세 설명은 다음 링크를 참고하시기 바랍니다.**


[Leaderboard Guide]((https://docs.nhncloud.com/ko/Game/Leaderboard/ko/api-guide/)

##### API 호출 예시

```
Content-Type: application/json
X-TCGB-Transaction-Id: 88a1ae42-6b1d-48c8-894e-54e97aca07fq
X-Secret-Key: IgsaAP

GET https://api-gamebase.cloud.toast.com/tcgb-leaderboard/v1.2/apps/{appId}/factors/{factor}/user-count
```

<br>
