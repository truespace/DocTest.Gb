---
source: ios-purchase.md
section: "Purchase Items"
order: 5
split: true
created_date_time: 20260408_191848
keyword: iOS, Purchase, Error, Console
---

### Purchase Items

구매하고자 하는 아이템의 gamebaseProductId를 이용해 다음의 API를 호출해 구매를 요청합니다. <br/>
gamebaseProductId는 일반적으로는 스토어에 등록한 아이템의 ID와 동일하지만, Gamebase 콘솔에서 변경할 수도 있습니다.

게임 유저가 구매를 취소하는 경우 **TCGB_ERROR_PURCHASE_USER_CANCELED** 오류가 반환됩니다. 취소 처리를 해 주시기 바랍니다.

**API**

```objectivec
+ (void)requestPurchaseWithGamebaseProductId:(NSString *)gamebaseProductId 
                              viewController:(UIViewController *)viewController
                                  completion:(void(^)(TCGBPurchasableReceipt *purchasableReceipt, TCGBError *error))completion;
```

**Example**

```objectivec
- (void)purchasingItem:(NSString *)gamebaseProductId {
    [TCGBPurchase requestPurchaseWithGamebaseProductId:gamebaseProductId viewController:self completion:^(TCGBPurchasableReceipt *purchasableReceipt, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == YES) {
            // To Purchase Item Succeeded
        } else if (error.code == TCGB_ERROR_PURCHASE_USER_CANCELED) {
            // User Canceled Purchasing Item
        } else if (error) {
            // To Purchase Item Failed cause of the error
        }
    }];
}
```

**VO**

```objectivec
@interface TCGBPurchasableReceipt : NSObject

// 구매한 아이템의 상품 ID
@property (nonatomic, strong) NSString *gamebaseProductId;

// 구매한 상품의 가격
@property (assign)            float price;

// 통화 코드
@property (nonatomic, strong) NSString *currency;

// 결제 식별자
// purchaseToken 과 함께 'Consume' 서버 API를 호출하는데 사용
// Consume API: https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
// 주의: Consume API 는 게임 서버에서 호출하세요!
@property (nonatomic, strong) NSString *paymentSeq;

// 결제 식별자
// paymentSeq 와 함께 'Consume' 서버 API를 호출하는데 사용
// Consume API: https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
// 주의: Consume API 는 게임 서버에서 호출하세요!
@property (nonatomic, strong) NSString *purchaseToken;

// Apple 스토어 콘솔에 등록된 상품 ID
@property (nonatomic, strong) NSString *marketItemId;

// 상품 타입
// UNKNOWN: 인식 불가능한 타입. Gamebase SDK를 업데이트하거나 Gamebase 고객 센터로 문의하세요.
// CONSUMABLE: 소비성 상품
// AUTO_RENEWABLE: 구독성 상품
// CONSUMABLE_AUTO_RENEWABLE: 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'
@property (nonatomic, strong) NSString *productType;

// 상품을 구매한 User ID
// 상품을 구매하지 않은 User ID 로 로그인 한다면 구매한 아이템을 획득할 수 없습니다.
@property (nonatomic, strong) NSString *userId;

// 스토어의 결제 식별자
@property (nonatomic, strong, nullable) NSString *paymentId;

// 구독이 종료되는 시각 (epoch time)
@property (nonatomic, assign) long expiryTime;

// 상품 구매 시간 (epoch time)
@property (nonatomic, assign) long purchaseTime;

// requestPurchase API 호출 시 payload 로 전달했던 값
// 이 필드는 예를 들어 동일한 User ID 로 구매 했음에도 게임 채널, 캐릭터 등에 따라 상품 구매 및 지급을 구분하고자 하는 경우 등
// 게임에서 필요로 하는 다양한 추가 정보를 담기 위한 목적으로 활용할 수 있습니다.
@property (nonatomic, strong, nullable) NSString *payload;

// 구독 상품은 갱실 될때마다 paymentId가 변경됩니다.
// 이 필드는 맨 처음 구독 상품을 결제 했을 때의 paymentId 를 알려줍니다.
// 스토어에 따라, 결제 서버 상태에 따라 값이 존재하지 않을 수 있으므로 항상 유요한 값을 보장하지는 않습니다.
@property (nonatomic, strong, nullable) NSString *originalPaymentId;

// itemSeq로 상품을 구매하는 Legacy API용 식별자
@property (assign)            long itemSeq;

// sandbox 결제 여부
@property (nonatomic, assign) BOOL sandboxPayment;

// 프로모션 결제 여부
@property (nonatomic, assign) BOOL promotionPayment;

// 스토어 코드 (ex. "AS")
@property (nonatomic, strong) NSString *storeCode;

@end
```
