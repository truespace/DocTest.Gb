---
source: api-guide-v1.0.md
section: "Others"
order: 9
created_date: 2026-04-03
---

## Others

### Support

API 호출 실패 원인에 대한 문의 사항이 있을 경우, **API 호출 URL(HTTP body가 있는 경우는 body와 함께)과 그에 대한 응답 결과**를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다.



##### API 호출 예시

```
GET https://api-gamebase.cloud.toast.com/tcgb-launching/v1.0/apps/C3JmSctU/maintenances/under-maintenance
```

##### API 실패 응답 결과

```json
{
  "header": {
    "transactionId": "18a1ae42-6b1d-54c8-894e-54e97bca07fq",
    "resultCode": -4010002,
    "resultMessage": "Gamebase product appKey is invalid, appId:C3JmSctU",
    "traceError": {
      "trackingTime": 1489726350287,
      "throwPoint": "gateway",
      "uri": "/tcgb-launching/v1.0/apps/C3JmSctU/maintenances/under-maintenance"
    },
    "isSuccessful": false
  }
}

```
