---
source: api-guide.md
section: "Coupon"
order: 8
split: true
created_date_time: 20260408_191848
keyword: Server API, Consume, Coupon, Error, Console
---

## Coupon

#### Check Validation And Consume Coupon

콘솔에서 발급된 쿠폰 코드의 유효성 검증 및 쿠폰 상태를 변경합니다. 유효한 쿠폰이면 소비 상태로 변경하고, 응답 결과로 지급할 아이템 정보를 반환합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| POST | /tcgb-gateway/v1.3/apps/{appId}/members/{userId}/coupons/{couponCode}?storeCode={storeCode} |

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
| storeCode | String | Optional | 콘솔에서 특정 스토어에서 설치한 앱에 대해서만 쿠폰 사용이 가능하도록 설정하였다면, 스토어 코드를 전달해야 함<br>- 전체 스토어인 경우 ALL 또는 파라미터 생략 가능<br>- [스토어 코드](#store-code) |

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

[오류 코드](../error-code.md#server)

<br>

#### Get Coupon Information by Coupon Code

입력된 쿠폰 코드를 바탕으로, 콘솔에 등록된 해당 쿠폰의 기본 정보를 조회합니다.

**[Method, URI]**

| Method | URI |
| --- | --- |
| GET | /tcgb-gateway/v1.3/apps/{appId}/coupons/codes/{couponCode}

**[Request Header]**

공통 사항 확인

**[Path Variable]**

| Name | Type | Value |
| --- | --- | --- |
| appId | String | NHN Cloud 프로젝트 ID |
| couponCode | String | 쿠폰 코드 |

**[Request Parameter]**

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
        ],
        "type": "KEYWORD",
        "couponCode": "XMAS",
        "startDate": "2025-12-21T00:00:00+09:00",
        "endDate": "2025-12-31T23:59:59+09:00"
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| result | Object | 쿠폰 상세 정보 |
| result.title | String | 쿠폰 이름 |
| result.benefits | Array[Object] | 지급할 아이템 목록 |
| result.benefits.itemId | String | 아이템 ID |
| result.benefits.amount | Integer | 아이템 개수 |
| result.type | Enum | 쿠폰 타입 (KEYWORD, SERIAL) |
| result.couponCode | String | 쿠폰 코드 |
| result.startDate | String | 유효 시작 시각 (ISO 8601) |
| result.endDate | String | 유효 종료 시각 (ISO 8601) |

**[Error Code]**

[오류 코드](../error-code.md#server)

<br>
<br>
