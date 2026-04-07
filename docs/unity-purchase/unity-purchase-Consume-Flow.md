---
source: unity-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Purchase, Consume, IAP"
section: "Consume Flow"
order: 3
---

### Consume Flow

미소비 결제 내역 목록에 값이 있으면 다음과 같은 순서로 Consume Flow 를 진행하시기 바랍니다.

> <font color="red">[주의]</font><br/>
>
> 아이템이 중복 지급되는 일이 발생하지 않도록, 게임 서버에서 반드시 중복 지급 여부를 체크하시기 바랍니다.
>

![consume flow](./image/purchase_flow_002_2.64.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Diagram
    내용: 아이템 소비(Consume) 처리 시퀀스 다이어그램
    구성: GameClient, GameServer, GamebaseServer 3개의 액터 간 통신 흐름. GameClient가 GameServer에 consume 요청, GameServer가 GamebaseServer에 paymentSeq로 배달 여부 확인, purchaseToken 검증 후 유효하면 아이템 지급 및 GameDB 저장, 무효하면 에러 콜백 반환. 이미 배달된 아이템인 경우에도 에러 처리. 최종적으로 consume API 호출로 완료
    Keyword: Consume Flow, 시퀀스 다이어그램, purchaseToken, 아이템 지급, GamebaseServer
-->

1. 게임 클라이언트가 게임 서버에 결제 아이템에 대한 consume(소비)을 요청합니다.
    * UserID, paymentSeq, purchaseToken을 전달합니다.
2. 게임 서버는 게임 DB에 이미 동일한 paymentSeq로 아이템을 지급한 이력이 있는지 확인합니다.
    * 2-1. 아직 아이템을 지급하지 않았다면 Gamebase 서버의 Payment Transaction API를 호출하여 purchaseToken이 유효한지, 응답 필드의 paymentSeq와 일치하는지 검증합니다.
        * [Game > Gamebase > API 가이드 > Purchase(IAP) > Get Payment Transaction](../api-guide.md#get-payment-transaction)
        * purchaseToken이 서버 API 가이드 문서의 **accessToken**에 해당합니다.
    * 2-2. gamebaseProductId는 서버의 Payment Transaction API의 응답 필드에서 확인할 수 있습니다.
        * 클라이언트의 미소비 결제 내역 목록에도 gamebaseProductId가 존재하지만, 재처리 시에는 해당 값이 없을 수도 있으므로 서버의 Payment Transaction API로부터 획득한 gamebaseProductId 값을 사용하시기 바랍니다.
    * 2-3. Payment Transaction API 호출이 성공하여 purchaseToken이 정상이라고 확인되면 UserID에 gamebaseProductId에 해당하는 아이템을 지급합니다.
    * 2-4. 아이템 지급 후 게임 DB에 UserID, gamebaseProductId, paymentSeq, purchaseToken을 저장하여 중복 지급 방지 또는 재지급을 할 수 있도록 합니다.
3. 아이템 지급 여부와 무관하게 게임 서버는 더 이상 미소비 내역이 리턴되지 않도록 Gamebase 서버의 consume(소비) API를 호출하여 아이템 지급을 완료합니다.
    * [Game > Gamebase > API 가이드 > Purchase(IAP) > Consume](../api-guide.md#consume)
