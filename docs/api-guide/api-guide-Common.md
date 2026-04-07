---
source: api-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Server API, isSuccessful, Common"
section: Common
order: 3
---

## Common

#### HTTP Header

API 호출 시 HTTP Header에 다음 항목들을 설정해야 합니다.

| Name | Required | Value |
| --- | --- | --- |
| Content-Type | Required | application/json; charset=UTF-8 |
| X-Secret-Key | Required | SecretKey 설명 참고 |
| X-TCGB-Transaction-Id | Optional | TransactionId 설명 참고 |

#### API Response

모든 API 요청에 대한 응답으로 **HTTP 200 OK**를 전달합니다. API 요청 성공 유무는 Response Body의 Header 항목을 참고하여 판단할 수 있습니다.

**[Request]**

```
Content-Type: application/json
X-TCGB-Transaction-Id: 88a1ae42-6b1d-48c8-894e-54e97aca07fq
X-Secret-Key: IgsaAP
GET https://api-gamebase.nhncloudservice.com
```

**[Response]**

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
X-TCGB-Transaction-Id: 88a1ae42-6b1d-48c8-894e-54e97aca07fq
```

```json
{
    "header" : {
    	"transactionId": "88a1ae42-6b1d-48c8-894e-54e97aca07fq",
        "isSuccessful" : true,
        "resultCode": 0,
        "resultMessage" : "Success."
    }
}
```

| Key | Type | Description |
| --- | --- | --- |
| transactionId | String | API 요청 시 HTTP Header에 설정한 값.<br>해당 값을 전달하지 않으면 Gamebase 내부적으로 생성된 값을 반환 |
| isSuccessful | boolean | 성공 여부 |
| resultCode | int | 응답 코드<br>성공 시 0, 실패 시 오류 코드 반환 |
| resultMessage | String | 응답 메시지 |

#### API Version

API 응답 결과의 특정 변수 타입이 변경될 때 API 버전이 변경됩니다. 즉, 신규 API가 추가되거나 응답 결과에 신규 변수가 추가되어도 API 버전은 변경되지 않습니다.

> [주의]
> API 응답 결과에 신규 변수가 추가되어도 JSON 파싱 오류가 발생하지 않도록, 사용하는 JSON 라이브러리의 옵션을 추가해 주시기 바랍니다.

<br>
<br>
