---
source: api-guide.md
section: "Purchase(IAP)"
order: 9
created_date: 2026-04-03
---

## Purchase(IAP)

#### Consume

Google Play Store, App Store, ONEStore 등 스토어 결제가 정상으로 완료되었다면 유저에게 아이템 지급 및 서버 내부적으로 이력을 기록한 후에, Gmaebase에 결제 소비를 알립니다. 결제 1건당 1번만 결제를 소비할 수 있으며 결제 상태가 정상이 아니면 소비되지 않습니다.

> [참고]
> 상품 등록 시 상품 유형이 일회성(CONSUMABLE) 또는 소비성 구독(CONSUMABLE_AUTO_RENEWABLE) 아이템 결제에 대해서만 소비(consume) 처리됩니다.
> 결제 1건당 1번 소비 가능하며, 결제 소비를 하지 않은 결제는 IAP에서는 아이템을 지급하지 않은 것으로 간주합니다.

소비(consume)하지 않은 결제 내역은 SDK 및 서버의 미소비 결제 내역 조회 API를 통해 조회할 수 있습니다. API를 통해 미소비 결재 내역이 존재하더라도, 게임 서버 내부적으로 아이템 지급에 대한 이력을 가지고 있다면 게임 서버 내부 지급 이력을 우선으로 판단하면 됩니다.
(네트워크 장애 등으로 API timeout이 발생하면 Gamebase에서는 지급이 완료되지만, 게임 서버에서는 API 응답 실패로 유저에게 아이템이 지급되지 않을 수 있음)

> [참고]
> 게임 내부적으로 아이템 지급 이력을 모두 관리할 수 없다면 해당 API의 request timeout을 10초 이상으로 하고, API timout 발생시 만이라도 이력을 기록하여 중복 지급 혹은 미지급 이슈에 대한 방안이 필요함

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.3/apps/{appId}/consume |

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
| paymentSeq | String | Required | 결제 번호 |
| accessToken | String | Required  | 결제 인증 토큰(로그인 인증 토큰이 아님) |

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
        "productSeq": 1000292,
        "marketId": "GG",
        "gamebaseProductId": "tap_prod_001",
        "payload": "additional info"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Object | 결제 기본 정보 |
| result.price | Float | 결제 가격 |
| result.currency | String  | 결제 통화  |
| result.productSeq | Long | 아이템 번호<br>콘솔에서 상품 등록 시, 외부 스토어 아이템에 대해 자동 생성된 값 |
| result.marketId | String | [스토어 코드](#store-code) |
| result.gamebaseProductId | String | Gamebase 상품 아이디<br>콘솔에서 상품 등록 시, 사용자 입력 값 |
| result.payload | String | SDK에서 설정한 추가 정보 |

> [참고]
> 클라이언트에서 사용하는 SDK 버전 및 결제 API에 따라 응답 결과에 gamebaseProductId 값이 존재합니다.

> [참고]
> 게임 서버에서는 아이템 번호 또는 스토어 코드와 Gamebase 상품 아이디로 지정한 상품(아이템)을 지급할 수 있지만, 1개의 스토어 아이템 아이디에 N개의 Gamebase 상품을 등록한 경우 스토어 코드와 Gamebase 상품 아이디로 지급해야 합니다.

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

#### List Consumables

결제가 완료되었지만 아직 소비(consume)되지 않은, 미소비 결제 내역을 조회할 수 있습니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.3/apps/{appId}/consumable |

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
    "marketIds": ["GG", "AS"],
    "userId": "QXG774PMRZMWR3BR"
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| marketId | String | Optional | [스토어 코드](#store-code)<br>- **deprecated** 예정으로 *marketIds* 사용 |
| marketIds | Array | Optional | [스토어 코드](#store-code)<br>- 빈 값(혹은 null)인 경우 전체 스토어 대상으로 조회<br> - 단, AMAZON 스토어가 포함된 전체 스토어를 조회할 경우 명시적으로 조회할 **모든 스토어**를 나열해야 함 |
| userId | String | Required | 유저 ID  |

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
            "paymentSeq": "2020060210364966",
            "productSeq": 1000312,
            "currency": "KRW",
            "price": 2500.0,
            "marketId": "AS",
            "accessToken": "ja5SBJBfr7rYUdjFr6dRe7gKnkX0r7EKPvuK6CIUBBekc1rE9CVbMKVCNuw6ZtwmcpDRXrToR9l26NF9zub6ol",
            "paymentId" : "Store Reference Key",
            "gamebaseProductId": "gamebase_prod_001",
            "purchaseTime": "2020-06-02T13:38:56+09:00",
            "payload": "additional info",
            "isTestPurchase" : false
        },
        {
            "paymentSeq": "2016122110023125",
            "productSeq": 1000292,
            "currency": "KRW",
            "price": 1000.0,
            "marketId": "AS",
            "accessToken": "7_3zXyNJub0FNLed3m9XRAAXsSxLWq698t8QyTzk3NeeSoytKxtKGjldTc1wkSktgzjsfkVTKE50DoGihsAvGQ",
            "paymentId" : "Store Reference Key",
            "gamebaseProductId": "gamebase_prod_002",
            "purchaseTime": "2020-06-02T13:37:42+09:00",
            "isTestPurchase" : false
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 결제 기본 정보 |
| result[].paymentSeq | String |  Gamebase에서 발급된 결제 번호 / 결제 Transaction ID |
| result[].productSeq | Long | 아이템 번호<br>콘솔에서 상품 등록 시, 외부 스토어 아이템에 대해 자동 생성된 값 |
| result[].currency  | String | 결제 통화  |
| result[].price | Float | 결제 가격 |
| result[].accessToken | String | 결제 인증 토큰 |
| result[].paymentId | String | 스토어에서 발급된 결제 ID |
| result[].marketId | String | [스토어 코드](#store-code) |
| result[].gamebaseProductId | String | Gamebase 상품 아이디<br>콘솔에서 상품 등록 시, 유저 입력 값 |
| result[].purchaseTime | String | 결제 발생 일시 |
| result[].payload | String | SDK에서 설정한 추가 정보<br>Amazon 스토어는 해당 값이 누락될 수 있음 |
| result[].isTestPurchase | boolean | 테스트 결제 여부 |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

#### Get Payment Transaction

클라이언트 SDK를 통해 획득한 미소비 결제 내역이 유효한지를 확인할 수 있습니다.
(서버에서 아이템 지급(consume) API를 호출하기 전에, 결제 번호(paymentSeq)와 결제 인증 토큰(accessToken)의 유효성 검사를 원한다면 해당 API 호출)

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-inapp/v1.3/apps/{appId}/payment/transaction?accessToken={accessToken} |

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |

**[Request Parameter]**

| Name | Type | Required |  Value |
| --- | --- | --- | --- |
| accessToken | String | Required | 결제 인증 토큰(purchaseToken) |

**[Request Body]**

없음

**[Response Body]**

```json
{
    "header": {
        "resultCode": 0,
        "resultMessage": "SUCCESS",
        "isSuccessful": true
    },
    "result": {
        "paymentSeq": "2022041110385239",
        "productSeq": 1003150,
        "currency": "EUR",
        "price": 2.29,
        "marketId": "AS",
        "accessToken": "-Fr8Y7_dvv5qhdd6qVHbs7gKnkX0r7EKPvuK6CI-UBBekc1rE9CVbMKVCNuw6ZtwkBGlzeIHg6DdjaRVeaW7GYlPF4vRa50L8umB6tdBvk8",
        "paymentId" : "Store Reference Key",
        "paymentToken" : "19062709124410111299",
        "productType": "CONSUMABLE",
        "userId": "AS@QW4M1GM7W97YJDCN",
        "gamebaseProductId": "qa_ksw_prod_as_001",
        "purchaseTime": "2022-04-11T16:47:01+09:00",
        "payload" : "string",
        "isTestPurchase": true,
        "isConsumable": false
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Object |  결제 정보 |
| result.paymentSeq | String | Gamebase에서 발급된 결제 번호 |
| result.productSeq | Long | 아이템 번호<br>콘솔에서 상품 등록 시, 외부 스토어 아이템에 대해 자동 생성된 값 |
| result.currency  | String | 결제 통화  |
| result.price | Float | 결제 가격 |
| result.marketId | String | [스토어 코드](#store-code) |
| result.accessToken | String | 결제 인증 토큰 |
| result.paymentId | String | 스토어에서 발급된 결제 ID |
| result.paymentToken | String | 스토어에서 발급된 결제 토큰으로 ONEStore 결제 건에만 존재함<br>- ONEStore V5: purchaseId<br> - ONEStore V6,7: purchaseToken |
| result.productType | String  | 상품(아이템) 유형<br>- 일회성: CONSUMABLE<br>- 소비성 구독: CONSUMABLE_AUTO_RENEWABLE<br>- 구독: AUTO_RENEWABLE |
| result.userId | String  | 유저 ID  |
| result.gamebaseProductId | String | Gamebase 상품 아이디<br>콘솔에서 상품 등록 시, 유저 입력 값 |
| result.purchaseTime | String | 결제 발생 일시 |
| result.payload | String | SDK에서 설정한 추가 정보<br>Amazon 스토어는 해당 값이 누락될 수 있음 |
| result.isTestPurchase | boolean | 테스트 결제 여부<br>- true: 테스트 결제 |
| result.isConsumable | boolean | 소비 API 호출 가능 여부<br>- true: 현재 미소비 상태로 소비 API 호출 가능함 |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

### List Active Subscriptions

사용자가 현재 구독 중인 결제를 조회할 수 있습니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.3/apps/{appId}/active-subscriptions |

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
    "marketIds": [
        "GG",
        "AS"
    ],
    "packageName": "com.nhncloud.gamebase",
    "userId": "QXG774PMRZMWR3BR",
    "includeInactiveGoogleStatuses" : [
        "ON_HOLD"
    ]
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| marketId | String | Optional | [스토어 코드](#store-code)<br>- **deprecated** 예정으로 *marketIds* 사용 |
| marketIds | Array[String] | Optional | [스토어 코드](#store-code)<br>- 빈 값(혹은 null)인 경우 전체 스토어 대상으로 조회 |
| packageName | String | Required | 콘솔에 등록한 스토어 앱 ID |
| userId | String | Required | 유저 ID |
| includeInactiveGoogleStatuses | Array[String] | Optional | 응답 결과에 포함할 **구글 구독 비활성 상태**<br>- 현재 'ON_HOLD' 상태만 지원 |

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
            "marketId": "GG",
            "userId": "QXG774PMRZMWR3BR",
            "paymentSeq": "2020052810364755",
            "accessToken": "NczL3n4TumMF8n9oRR5l8zXDyMXRVjxSRks0Lk1Saob2A9rdAupqjZSrQ0-hb2GOSFwTx5uDDchH8EB-EkWGGQ",
            "productSeq": 1001221,
            "productId": "money_100",
            "productType": "AUTO_RENEWABLE",
            "originalPaymentId": "GPA.3302-8679-7228-41195",
            "paymentId": "GPA.3302-8679-7228-41195",
            "linkedPaymentId": "GPA.3358-3220-2629-70624",
            "price": 1000.0,
            "currency": "KRW",
            "gamebaseProductId": "gamebase_renewal_001",
            "payload" : "additional info",
            "purchaseTime": "2020-06-02T13:38:56+09:00",
            "expiryTime": "2020-06-02T13:48:56+09:00",
            "renewTime" : "2020-06-02T13:50:56+09:00",
            "isTestPurchase" : false,
            "referenceStatus" : "PURCHASED"
        }
    ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 결제 기본 정보 |
| result[].marketId  | String  | [스토어 코드](#store-code) |
| result[].userId | String  | 유저 ID  |
| result[].paymentSeq | String  | 결제 번호 |
| result[].accessToken | String | 결제 인증 토큰 |
| result[].productSeq | Long | 아이템 번호<br>콘솔에서 상품 등록 시, 외부 스토어 아이템에 대해 자동 생성된 값 |
| result[].productId | String | 스토어에 등록된 상품(아이템) 식별자 |
| result[].productType | String  | 상품(아이템) 유형<br>구독: AUTO_RENEWABLE |
| result[].currency  | String  | 결제 통화 |
| result[].price | Float | 결제 가격 |
| result[].originalPaymentId | String | 최초 스토어 결제 ID |
| result[].paymentId | String | 최근 갱신된 스토어 결제 ID |
| result[].linkedPaymentId | String | 구독 취소/재구매 시 원거래의 결제 ID<br>Google Play 스토어만 지원 |
| result[].gamebaseProductId | String | Gamebase 상품 아이디<br>콘솔에서 상품 등록 시, 사용자 입력 값 |
| result[].payload | String | SDK에서 설정한 추가 정보 |
| result[].purchaseTime | String | 최근 갱신된 시간 |
| result[].expiryTime | String | 구독 만료 시간 |
| result[].renewTime | String | RENEWED/RECOVERED 발생 시간 |
| result[].isTestPurchase | boolean | 테스트 결제 여부 |
| result[].referenceStatus | String | 결제 시스템(인앱 결제, 외부 결제)이 제공하는 [결제 참조 상태](#store-reference-status)<br>현재 Google Play 스토어만 지원 |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

### Cancel Subscriptions

구독 중인 상품에 대해 갱신 시점에 더 이상 갱신이 되지 않고, 현재 구독 만료까지 유지합니다.

> [참고]
> 현재 Google Play 스토어만 지원합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.3/apps/{appId}/subscriptions/cancel |

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
    "paymentSeq": "2022112110400545",
    "accessToken": "NczL3n4TumMF8n9oRR5l8zXDyMXRVjxSRks0Lk1Saob2A9rdAupqjZSrQ0-hb2GOSFwTx5uDDchH8EB-EkWGGQ"
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| paymentSeq | String | Required | 결제 번호 |
| accessToken | String | Required | 결제 인증 토큰 |

**[Response Body]**

```json
{
    "header": {
        "isSuccessful": true,
        "resultCode": 0,
        "resultMessage": "SUCCESS"
    }
}
```

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

### Revoke Subscriptions

현재 구독 중인 상품에 대해 즉시 구독을 취소하고 환불을 진행합니다.

> [참고]
> 현재 Google Play 스토어만 지원합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.3/apps/{appId}/subscriptions/revoke |

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
    "paymentSeq": "2022112110400545",
    "accessToken": "NczL3n4TumMF8n9oRR5l8zXDyMXRVjxSRks0Lk1Saob2A9rdAupqjZSrQ0-hb2GOSFwTx5uDDchH8EB-EkWGGQ"
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| paymentSeq | String | Required | 결제 번호 |
| accessToken | String | Required | 결제 인증 토큰 |

**[Response Body]**

```json
{
    "header": {
        "isSuccessful": true,
        "resultCode": 0,
        "resultMessage": "SUCCESS"
    }
}
```

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>

### Get Subscriptions Status

구독 상품에 대해 현재 상태를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-inapp/v1.3/apps/{appId}/subscriptions/status |

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
  "payments": [
    {
      "paymentSeq": "2023082410408370",
      "accessToken": "Yk3sMxc-JSaGLLY0X-DnajXDyMXRVjxSRks0Lk1SaoaO7RD7VRjZcs8OTm8lOQVFoP71pgjAb_INjl0Y5KN8_A"
    },
    {
      "paymentSeq": "2023082410408383",
      "accessToken": "qEP1ZeV_ORmJdlNr9xDm9DXDyMXRVjxSRks0Lk1SaoaPiqPX4dG6UstXeWUt1NujyQAwH8BWQJueaPRfmnRyeg"
    }
  ]
}
```

| Name | Type | Required | Value |
| --- | --- | --- | --- |
| payments | Array[Object] | 구독 결제 정보. 최대 10개까지 입력 |
| payments[].paymentSeq | String | Required | 결제 번호 |
| payments[].accessToken | String | Required | 결제 인증 토큰 |

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
      "userId": "QXG774PMRZMWR3BR",
      "paymentSeq": "2023082410408389",
      "accessToken": "uddRuwkHm9nFIHjvVuDS2jXDyMXRVjxSRks0Lk1SaoaPiqPX4dG6UstXeWUt1NujyQAwH8BWQJueaPRfmnRyeg",
      "paymentId": "GPA.3333-7714-3477-48799..5",
      "originalPaymentId": "GPA.3333-7714-3477-48799",
      "purchaseTime": "2022-05-16T09:59:27+09:00",
      "expiryTime": "2023-08-24T12:48:45+09:00",
      "renewTime": "2023-08-24T12:48:45+09:00",
      "referenceStatus": "REPURCHASED"
    },
    {
      "userId": "QXG774PMRZMWR3BR",
      "paymentSeq": "2023082410408381",
      "accessToken": "SFkxJL2sk8NlbsPe8ivVGDXDyMXRVjxSRks0Lk1SaoaO7RD7VRjZcs8OTm8lOQVFoP71pgjAb_INjl0Y5KN8_A",
      "paymentId": "GPA.3395-4426-6912-10820..5",
      "originalPaymentId": "GPA.3395-4426-6912-10820",
      "purchaseTime": "2022-05-16T09:59:27+09:00",
      "expiryTime": "2023-08-24T12:48:45+09:00",
      "renewTime": "2023-08-24T12:48:45+09:00",
      "referenceStatus": "EXPIRED"
    }
  ]
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Array[Object] | 결제 기본 정보 |
| result[].userId | String  | 유저 ID  |
| result[].paymentSeq | String  | 결제 번호 |
| result[].accessToken | String | 결제 인증 토큰 |
| result[].paymentId | String | 최근 갱신된 스토어 결제 ID |
| result[].originalPaymentId | String | 최초 스토어 결제 ID |
| result[].purchaseTime | String | 최근 갱신된 시간 |
| result[].expiryTime | String | 구독 만료 시간 |
| result[].renewTime | String | RENEWED/RECOVERED 발생 시간 |
| result[].referenceStatus | String | 결제 시스템(인앱 결제, 외부 결제)이 제공하는 [결제 참조 상태](#store-reference-status)<br>현재 Google Play 스토어만 지원 |

**[Error Code]**

[오류 코드](../../error-code.md#server)

<br>
<br>
