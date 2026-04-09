---
source: aos-purchase.md
section: "Retry Transaction Flow"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Purchase, Consume, Error, RequestItemListOfNotConsumed
---

### Retry Transaction Flow

![retry transaction flow](./image/purchase_retry_transaction_flow_2.19.0.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Sequence Diagram
    내용: 결제 재처리 흐름도
    구성: 미소비 결제 건에 대한 재처리 흐름을 나타내는 시퀀스 다이어그램
    Keyword: Sequence Diagram, Retry Transaction Flow
-->

* 스토어 결제에는 성공했으나 오류가 발생해 정상 종료되지 못하는 경우가 있습니다.
* **requestItemListOfNotConsumed**를 호출하여 재처리를 동작시켜 미지급된 아이템이 있으면 [Consume Flow](./aos-purchase-Consume-Flow.md#consume-flow) 를 진행하세요.
* 재처리는 다음과 같은 시점에 호출할 것을 권장합니다.
    * 로그인 완료 후.
    * 결제 전.
    * 게임 내 상점(또는 로비) 진입시.
    * 유저 프로필 또는 우편함 확인시.
