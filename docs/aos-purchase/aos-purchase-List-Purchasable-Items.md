---
source: aos-purchase.md
section: "List Purchasable Items"
order: 6
split: true
created_date_time: 20260408_184906
keyword: Android, Purchase, Consume
---

### List Purchasable Items

아이템 목록을 조회하려면 다음 API를 호출합니다. 콜백으로 반환되는 배열(array) 안에는 각 아이템들에 대한 정보가 담겨 있습니다.

**API**

```java
+ (void)Gamebase.Purchase.requestItemListPurchasable(Activity activity, GamebaseDataCallback<List<PurchasableItem>> callback);
```

**Example**

```java
Gamebase.Purchase.requestItemListPurchasable(activity, new GamebaseDataCallback<List<PurchasableItem>>() {
    @Override
    public void onCallback(List<PurchasableItem> data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
        } else {
            // Failed.
            Log.e(TAG, "Request item list failed- "
                    + "errorCode: " + exception.getCode()
                    + "errorMessage: " + exception.getMessage());
        }
    }
});
```

**VO**

```java
class PurchasableItem {
    // Gamebase 콘솔에 등록된 상품 ID입니다.
    // Gamebase.Purchase.requestPurchase API로 상품을 구매할 때 사용됩니다.
    @Nullable
    String gamebaseProductId;
    
    // 상품의 가격입니다.
    float price;
    
    // 통화 코드입니다.
    @Nullable
    String currency;
    
    // Gamebase 콘솔에 등록된 상품 이름입니다.
    @Nullable
    String itemName;
    
    // Google, Apple 과 같이 스토어 콘솔에 등록된 상품 ID입니다.
    @NonNull
    String marketItemId;
    
    // 상품 타입으로, 다음 값들이 올 수 있습니다.
    // * UNKNOWN : 인식 불가능한 타입. Gamebase SDK 를 업데이트 하거나 Gamebase 고객 센터로 문의하세요.
    // * CONSUMABLE : 소비성 상품.
    // * AUTORENEWABLE : 구독형 상품.
    // * CONSUMABLE_AUTO_RENEWABLE : 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'.
    @NonNull
    String productType;
    
    // 통화 기호가 포함된 현지화 된 가격 정보입니다.
    @Nullable
    String localizedPrice;
    
    // 스토어 콘솔에 등록된 현지화된 상품 이름입니다.
    @Nullable
    String localizedTitle;
    
    // 스토어 콘솔에 등록된 현지화된 상품 설명입니다.
    @Nullable
    String localizedDescription;
    
    // Gamebase 콘솔에서 해당 상품의 '사용 여부'를 나타냅니다.
    boolean isActive;
    
    // itemSeq 로 상품을 구매하는 Legacy API용 식별자입니다.
    long itemSeq;
}
```

**Response Example**

```json
{
    "gamebaseProductId": "my_product_001",
    "price": 1000.0,
    "currency": "KRW",
    "itemName": "Consumable product for test",
    "marketItemId": "my_product_001",
    "productType": "CONSUMABLE",
    "localizedPrice": "₩1,000",
    "localizedTitle": "TEST PRODUCT 001",
    "localizedDescription": "Product for test 001",
    "isActive": true,
    "itemSeq": 1000001
}
```
