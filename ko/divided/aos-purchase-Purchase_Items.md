## Game > Gamebase > Android SDK 사용 가이드 > 결제

### Purchase Items

구매하고자 하는 아이템의 gamebaseProductId 를 이용해 다음의 API를 호출해 구매를 요청합니다.<br/>
gamebaseProductId 는 일반적으로는 스토어에 등록한 아이템의 id와 동일하지만, Gamebase 콘솔에서 변경할 수도 있습니다.

게임 유저가 구매를 취소하는 경우 **GamebaseError.PURCHASE_USER_CANCELED** 오류가 반환됩니다.
취소 처리를 해 주시기 바랍니다.

느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우에는 **GamebaseError.PURCHASE_PENDING** 오류가 반환됩니다.
이후에 결제가 정상적으로 완료되는 경우, GamebaseEventHandler에서 결제 완료 이벤트를 수신할 수 있습니다.
[Game > Gamebase > Android SDK 사용 가이드 > ETC > Gamebase Event Handler](./aos-etc/#purchase-updated)

**API**

```java
+ (void)Gamebase.Purchase.requestPurchase(@NonNull final Activity activity,
                                          @NonNull final String gamebaseProductId,
                                          @NonNull final GamebaseDataCallback<PurchasableReceipt> callback);
```

**Example**

```java
Gamebase.Purchase.requestPurchase(activity, gamebaseProductId, new GamebaseDataCallback<PurchasableReceipt>() {
    @Override
    public void onCallback(PurchasableReceipt receipt, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
        } else if(exception.getCode() == GamebaseError.PURCHASE_USER_CANCELED) {
            // User canceled.
        } else {
            // To Purchase Item Failed cause of the error
        }
    }
});
```

**VO**

```java
class PurchasableReceipt {
    // 구매한 아이템의 상품 ID입니다.
    @Nullable
    String gamebaseProductId;
    
    // Gamebase.Purchase.requestPurchase API 호출 시 payload로 전달했던 값입니다.
    // 스토어 서버 상태에 따라 정보가 유실되는 경우가 있으므로 사용을 권장하지 않습니다.
    @Nullable
    String payload;
    
    // 구매한 상품의 가격입니다.
    float price;
    
    // 통화 코드입니다.
    @NonNull
    String currency;
    
    // 결제 식별자입니다.
    // purchaseToken과 함께 'Consume' 서버 API를 호출하는 데 사용하는 중요한 정보입니다.
    //
    // Consume API : https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
    // 주의 : Consume API 는 게임 서버에서 호출하세요!
    @NonNull
    String paymentSeq;
    
    // 결제 식별자입니다.
    // paymentSeq 와 함께 'Consume' 서버 API를 호출하는데 사용하는 중요한 정보입니다.
    // Consume API 에서는 'accessToken' 라는 이름의 파라메터로 전달해야 합니다.
    //
    // Consume API : https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
    // 주의 : Consume API 는 게임 서버에서 호출하세요!
    @Nullable
    String purchaseToken;
    
    // Google, Apple 과 같이 스토어 콘솔에 등록된 상품 ID입니다.
    @NonNull
    String marketItemId;
    
    // 상품 타입으로, 다음 값들이 올 수 있습니다.
    // * UNKNOWN : 인식 불가능한 타입. Gamebase SDK 를 업데이트 하거나 Gamebase 고객 센터로 문의하세요.
    // * CONSUMABLE : 소비성 상품.
    // * AUTO_RENEWABLE : 구독형 상품.
    // * CONSUMABLE_AUTO_RENEWABLE : 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'.
    @NonNull
    String productType;
    
    // 상품을 구매했던 User ID.
    // 상품을 구매하지 않은 User ID 로 로그인 한다면 구매한 아이템을 획득할 수 없습니다.
    @NonNull
    String userId;
    
    // 스토어의 결제 식별자입니다.
    @Nullable
    String paymentId;
    
    // 상품을 구매했던 시각입니다.(epoch time)
    long purchaseTime;
    
    // 구독이 종료되는 시각입니다.(epoch time)
    long expiryTime;
    
    // Google 결제시 사용되는 값으로, 다음 값들이 올 수 있습니다.
    // 하지만 Google 서버에서 장애가 발생하여 Gamebase 결제 서버에서 일시적으로 검증 로직을 끄는 경우에는
    // null 로만 반환되므로 항상 유효한 값을 보장하지는 않음에 주의하시기 바랍니다.
    // * null : 일반 결제
    // * Test : 테스트 결제
    // * Promo : Promotion 결제
    @Nullable
    String purchaseType;
    
    // 구독 상품은 갱신될 때마다 paymentId가 변경됩니다.
    // 이 필드는 맨 처음 구독 상품을 결제 했을때의 paymentId 를 알려줍니다.
    // 스토어에 따라, 결제 서버 상태에 따라 값이 존재하지 않을 수 있으므로
    // 항상 유효한 값을 보장하지는 않습니다.
    @Nullable
    String originalPaymentId;
    
    // itemSeq 로 상품을 구매하는 Legacy API용 식별자입니다.
    long itemSeq;
    
    // 상품을 구매했던 Store Code.
    @NonNull
    public String storeCode;
}
```

**Response Example**

```json
{
    "gamebaseProductId": "my_product_001",
    "price": 1000.0,
    "currency": "KRW",
    "paymentSeq": "2021032510000001",
    "purchaseToken": "5U_NVCLKSDFKLJJ...",
    "marketItemId": "my_product_001",
    "productType": "CONSUMABLE",
    "userId": "AS@123456ABCDEFGHIJ",
    "paymentId": "GPA.1111-2222-3333-44444",
    "purchaseTime": 1616649225531,
    "expiryTime": 0,
    "itemSeq": 1000001
}
```
```json
{
    "gamebaseProductId": "my_subcription_product_001",
    "price": 1000.0,
    "currency": "KRW",
    "paymentSeq": "2021032510000001",
    "purchaseToken": "5U_NVCLKKLJLSDG...",
    "marketItemId": "my_subcription_product_001",
    "productType": "CONSUMABLE_AUTO_RENEWABLE",
    "userId": "AS@123456ABCDEFGHIJ",
    "paymentId": "GPA.1111-2222-3333-56789",
    "purchaseTime": 1617069916128,
    "expiryTime": 1617070323784,
    "purchaseType": "Test",
    "originalPaymentId": "GPA.1111-2222-3333-56789",
    "itemSeq": 1000002
}
```
