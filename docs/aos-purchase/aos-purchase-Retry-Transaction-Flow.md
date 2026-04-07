---
source: aos-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Retry Transaction Flow"
section: "Retry Transaction Flow"
order: 4
---

### Retry Transaction Flow

![retry transaction flow](./image/purchase_retry_transaction_flow_2.19.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Flowchart
    내용: 결제 재처리(Retry Transaction) 플로우를 나타내는 순서도
    구성: Start에서 Gamebase.Purchase.RequestItemListOfNotConsumed() 호출 후, 미소비 아이템 존재 여부를 확인하는 분기. 미소비 아이템이 있으면(Yes) Consume Flow로 이동, 없으면(No) 성공 처리 후 다음 Flow로 진행
    Keyword: RetryTransaction, 재처리, 결제, 플로우차트, RequestItemListOfNotConsumed, Consume
-->

* 스토어 결제에는 성공했으나 오류가 발생해 정상 종료되지 못하는 경우가 있습니다.
* **requestItemListOfNotConsumed**를 호출하여 재처리를 동작시켜 미지급된 아이템이 있으면 [Consume Flow](./aos-purchase-Consume-Flow.md#consume-flow) 를 진행하세요.
* 재처리는 다음과 같은 시점에 호출할 것을 권장합니다.
    * 로그인 완료 후.
    * 결제 전.
    * 게임 내 상점(또는 로비) 진입시.
    * 유저 프로필 또는 우편함 확인시.
