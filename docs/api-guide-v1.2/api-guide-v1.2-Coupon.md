---
source: api-guide-v1.2.md
split: true
created_date_time: 20260406_141859
keyword: Coupon
section: Coupon
order: 8
---

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
