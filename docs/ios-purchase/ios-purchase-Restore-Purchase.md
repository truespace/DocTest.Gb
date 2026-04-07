---
source: ios-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Restore Purchase"
section: "Restore Purchase"
order: 9
---

### Restore Purchase

사용자의 App Store 계정으로 구매한 내역을 기준으로 구매 내역을 복원하여 콘솔에 반영합니다.
구매한 구독 상품이 조회되지 않거나 활성화되지 않을 경우 사용합니다.
만료된 결제 건을 포함해 복원된 결제 건이 결과로 반환됩니다.
자동 갱신형 소비성 구독 상품의 경우 반영되지 않은 구매 내역이 있다면 복원 후 미소비 구매 내역에서 조회할 수 있습니다.

**API**

```objectivec
+ (void)requestRestoreWithCompletion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
```

**Example**

```objectivec
- (void)viewDidLoad {
    [TCGBPurchase requestRestoreWithCompletion:^(NSArray<TCGBPurchasableReceipt *> *purchasableReceiptArray, TCGBError *error) {
        if (error != nil) {
            // To Requesting Restore Failed cause of the error
            return;
        }

        // Should Deal With This Restored Items.
    }];
}
```
