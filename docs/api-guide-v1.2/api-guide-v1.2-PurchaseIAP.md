---
source: api-guide-v1.2.md
split: true
created_date_time: 20260406_141859
keyword: "Server API, Purchase, Consume, Error, IAP, isSuccessful, requestPurchase"
section: Purchase(IAP)
order: 9
---

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
