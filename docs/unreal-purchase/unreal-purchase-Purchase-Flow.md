---
source: unreal-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Purchase, Consume, RequestItemListOfNotConsumed, RequestPurchase"
section: "Purchase Flow"
order: 2
---

### Purchase Flow

아이템 구매는 크게 결제 Flow 와 Consume Flow, 재처리 Flow 로 나누어 볼 수 있습니다.
결제 Flow는 다음과 같은 순서로 구현하시기 바랍니다.

![purchase flow](./image/purchase_flow_001_2.10.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Diagram
    내용: 결제(Purchase) 흐름 시퀀스 다이어그램
    구성: GameClient, GamebaseSDK, GameServer 간의 상호작용을 보여주는 시퀀스 다이어그램. requestItemListOfNotConsumed로 재처리 확인 후, requestPurchase로 결제 시도, 성공 후 다시 requestItemListOfNotConsumed를 호출하여 미소비 아이템 처리(Consume Flow)를 진행하는 과정
    Keyword: 결제, Purchase, 시퀀스다이어그램, GameClient, GamebaseSDK, Consume
-->

1. 이전 결제가 정상적으로 종료되지 못한 경우 재처리가 동작하지 않으면 결제가 실패합니다. 그러므로 결제 전에 **RequestItemListOfNotConsumed**를 호출하여 재처리를 동작시켜 미지급된 아이템이 있으면 Consume Flow 를 진행합니다.
2. 게임 클라이언트에서는 Gamebase SDK의 **RequestPurchase**를 호출하여 결제를 시도합니다.
3. 결제가 성공했다면 **RequestItemListOfNotConsumed**를 호출하여 미소비 결제 내역을 확인한 후 지급할 아이템이 존재한다면 Consume Flow 를 진행합니다.
