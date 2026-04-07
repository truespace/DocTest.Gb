---
source: unity-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Purchase Flow"
section: "Purchase Flow"
order: 2
---

### Purchase Flow

아이템 구매는 크게 결제 Flow 와 Consume Flow, 재처리 Flow 로 나누어 볼 수 있습니다.
결제 Flow는 다음과 같은 순서로 구현하시기 바랍니다.

![purchase flow](./image/purchase_flow_001_2.10.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Diagram
    내용: 결제(Purchase) 처리 시퀀스 다이어그램
    구성: GameClient, GamebaseSDK, GameServer 3개의 액터 간 통신 흐름. requestItemListOfNotConsumed로 미소비 아이템 확인 후 Consume Flow 처리, requestPurchase로 결제 요청 및 콜백 수신, 이후 다시 requestItemListOfNotConsumed로 미소비 아이템 재확인하는 순서로 구성
    Keyword: Purchase Flow, 시퀀스 다이어그램, GameClient, GamebaseSDK, 결제, 미소비 아이템
-->

1. 이전 결제가 정상적으로 종료되지 못한 경우 재처리가 동작하지 않으면 결제가 실패합니다. 그러므로 결제 전에 **RequestItemListOfNotConsumed**를 호출하여 재처리를 동작시켜 미지급된 아이템이 있으면 Consume Flow 를 진행합니다.
2. 게임 클라이언트에서는 Gamebase SDK의 **RequestPurchase**를 호출하여 결제를 시도합니다.
3. 결제가 성공하였다면 **RequestItemListOfNotConsumed**를 호출하여 미소비 결제 내역을 확인한 후 지급할 아이템이 존재한다면 Consume Flow 를 진행합니다.
