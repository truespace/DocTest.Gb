## Game > Gamebase > iOS SDK 사용 가이드 > 결제

### List Purchasable Items

아이템 목록을 조회하려면 다음 API를 호출합니다. 콜백으로 반환되는 배열(array) 안에는 각 아이템들에 대한 정보가 담겨 있습니다.

```objectivec
- (void)viewDidLoad {
    [TCGBPurchase requestItemListPurchasableWithCompletion:^(NSArray *purchasableItemArray, TCGBError *error) {
        if (error != nil) {
            // To Request Item List Failed cause of the error
            return;
        }

        NSMutableArray *itemArrayMutable = [[NSMutableArray alloc] init];
        [purchasableItemArray enumerateObjectsUsingBlock:^(id  _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
            TCGBPurchasableItem *item = (TCGBPurchasableItem *)obj;

            [itemArrayMutable addObject:item];
        }];
    }];
}
```


**VO**

```objectivec
@interface TCGBPurchasableItem : NSObject

// Gamebase 콘솔에 등록된 상품 ID
// requestPurchase API로 상품을 구매할 때 사용
@property (nonatomic, strong) NSString *gamebaseProductId;

// 상품 가격
@property (assign) float price;

// 통화 코드
@property (nonatomic, strong) NSString *currency;

// Gamebase 콘솔에 등록된 상품 이름
@property (nonatomic, strong) NSString *itemName;

// 스토어 코드 ("AS")
@property (nonatomic, strong) NSString *marketId;

// Apple 스토어 콘솔에 등록된 상품 ID
@property (nonatomic, strong) NSString *marketItemId;

// 상품 타입
// UNKNOWN: 인식 불가능한 타입. Gamebase SDK를 업데이트하거나 Gamebase 고객 센터로 문의하세요.
// CONSUMABLE: 소비성 상품
// AUTO_RENEWABLE: 구독성 상품
// CONSUMABLE_AUTO_RENEWABLE: 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'
@property (nonatomic, strong) NSString *productType;

// 통화 기호가 포함된 현지화 된 가격 정보
@property (nonatomic, strong) NSString *localizedPrice;

// 스토어 콘솔에 등록된 현지화된 상품 이름
@property (nonatomic, strong) NSString *localizedTitle;

// 스토어 콘솔에 등록된 현지화된 상품 설명
@property (nonatomic, strong) NSString *localizedDescription;

// Gamebase 콘솔에서 해당 상품의 '사용 여부'
@property (nonatomic, assign, getter=isActive) BOOL active;

// itemSeq로 상품을 구매하는 Legacy API용 아이템 식별자
@property (assign) long itemSeq;

@end
```
