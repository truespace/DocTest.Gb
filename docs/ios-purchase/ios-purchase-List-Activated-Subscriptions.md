---
source: ios-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "List Activated Subscriptions"
section: "List Activated Subscriptions"
order: 8
---

### List Activated Subscriptions

현재 사용자 ID 기준으로 활성화된 구독 목록을 조회합니다.
결제가 완료된 구독 상품(자동 갱신형 구독, 자동 갱신형 소비성 구독 상품)은 만료되기 전까지 계속 조회할 수 있습니다.

**API**

```objectivec
+ (void)requestActivatedPurchasesWithConfiguration:(TCGBPurchasableConfiguration *)configuration
                                        completion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
```

#### Required 파라미터

* configuration: TCGBPurchasableConfiguration으로 활성화된 구독 목록 조회에 대한 설정을 변경할 수 있습니다.
* completion: 활성화된 구독 목록 조회 결과를 사용자에게 콜백으로 알려줍니다.

**Example**

```objectivec
- (void)viewDidLoad {
    TCGBPurchasableConfiguration *configuration = [[TCGBPurchasableConfiguration alloc] init];

    [TCGBPurchase requestActivatedPurchasesWithConfiguration:configuration completion:^(NSArray<TCGBPurchasableReceipt *> *purchasableReceiptArray, TCGBError *error) {
        if (error != nil) {
            // To Requesting Activated Item List Failed cause of the error
            return;
        }

        // Should Deal With This Activated Items.
    }];
}
```
