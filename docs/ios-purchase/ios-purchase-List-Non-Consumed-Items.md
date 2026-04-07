---
source: ios-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "List Non-Consumed Items"
section: "List Non-Consumed Items"
order: 7
---

### List Non-Consumed Items

아이템을 구매했지만, 정상적으로 아이템이 소비(배송, 지급)되지 않은 미소비 결제 내역을 요청합니다.<br/>
미결제 내역이 있는 경우에는 게임 서버(아이템 서버)에 요청하여, 아이템을 배송(지급)하도록 처리해야 합니다..

* 정상적으로 결제가 완료되지 못한 경우 재처리의 역할도 하므로 다음 상황에서 호출해 주세요.
    * 게임 유저에게 지급되지 못한 아이템이 남아 있는지 확인
        * 로그인 완료 후
        * 게임 내 상점(또는 로비) 진입 시
        * 유저 프로필 또는 우편함 확인 시
    * 재처리가 필요한 아이템이 있는지 확인
        * 결제 전
        * 결제 실패 후

**API**

```objectivec
+ (void)requestItemListOfNotConsumedWithConfiguration:(TCGBPurchasableConfiguration *)configuration
                                           completion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
```

#### Required 파라미터

* configuration: TCGBPurchasableConfiguration으로 미소비 결제 내역 조회에 대한 설정을 변경할 수 있습니다.
* completion: 미소비 결제 내역 조회 결과를 사용자에게 콜백으로 알려줍니다.

**Example**

```objectivec
- (void)viewDidLoad {
    TCGBPurchasableConfiguration *configuration = [[TCGBPurchasableConfiguration alloc] init];

    [TCGBPurchase requestItemListOfNotConsumedWithConfiguration:configuration completion:^(NSArray<TCGBPurchasableReceipt *> *purchasableReceiptArray, TCGBError *error) {
        if (error != nil) {
            // To Requesting Non-consumed Item List Failed cause of the error
            return;
        }

        // Should Deal With This Non-consumed Items.
        // Send this item list to the game(item) server for consuming item
    }];
}
```
