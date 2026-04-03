---
source: aos-purchase.md
section: "List Non-Consumed Items-to-Event by Purchase"
order: 2
created_date: 2026-04-03
---

### List Non-Consumed Items

* 아직 소비되지 않은 일회성 상품(CONSUMABLE)과 소비성 구독 상품(CONSUMABLE_AUTO_RENEWABLE) 정보를 조회합니다.
* 미결제 내역이 있는 경우에는 게임 서버(아이템 서버)에 요청하여, 아이템을 배송(지급)하도록 처리해야 합니다.
* 정상적으로 결제가 완료되지 못한 경우 재처리의 역할도 하므로 다음 상황에서 호출해 주세요.
    * 게임 유저에게 지급되지 못한 아이템이 남아 있는지 확인
    	* 로그인 완료 후
    	* 게임 내 상점(또는 로비) 진입시
    	* 유저 프로필 또는 우편함 확인시
    * 재처리가 필요한 아이템이 있는지 확인
    	* 결제 전
    	* 결제 실패 후

**PurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                                    |
| ------------------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| newBuilder()                    | **M**                      | Configuration 객체 생성을 위한 Builder를 생성합니다.                                |
| build()                         | **M**                      | 설정을 마친 Builder를 Configuration 객체로 변환합니다.                                |
| setAllStores(boolean allStores) | O                          | 동일한 UserID로 다른 스토어에서 구매한 미소비 내역도 반환합니다.<br/>기본값은 **false**입니다. |

**API**

```java
+ (void)Gamebase.Purchase.requestItemListOfNotConsumed(@NonNull final Activity activity,
                                                       @NonNull final PurchasableConfiguration configuration,
                                                       @NonNull final GamebaseDataCallback<List<PurchasableReceipt>> callback);
```

**Example**

```java
final PurchasableConfiguration configuration = PurchasableConfiguration.newBuilder().build();
Gamebase.Purchase.requestItemListOfNotConsumed(activity, configuration, new GamebaseDataCallback<List<PurchasableReceipt>>() {
    @Override
    public void onCallback(List<PurchasableReceipt> data, GamebaseException exception) {
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

### List Activated Subscriptions

현재 사용자 ID 기준으로 활성화된 구독 목록을 조회합니다.
결제가 완료된 구독 상품(자동 갱신형 구독, 자동 갱신형 소비성 구독 상품)은 만료되기 전까지 계속 조회할 수 있습니다.
구독 수명 주기 처리는 다음 문서를 참조하시기 바랍니다.
[NHN Cloud > SDK 사용 가이드 > IAP > Android > Google Play Store 구독(정기 결제) 기능 > 구독 수명 주기 처리](https://docs.nhncloud.com/en/TOAST/en/toast-sdk/iap-android/#subscription-lifecycle-handling)

> <font color="red">[주의]</font><br/>
>
> 현재 구독 상품은 Android의 경우 Google Play 스토어만 지원합니다.
>

**PurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                               |
| ------------------------------- | -------------------------- | ------------------------------------------------------------------------- |
| newBuilder()                    | **M**                      | Configuration 객체 생성을 위한 Builder를 생성합니다.                            |
| build()                         | **M**                      | 설정을 마친 Builder를 Configuration 객체로 변환합니다.                           |
| setAllStores(boolean allStores) | O                          | 동일한 UserID로 다른 스토어에서 구매한 구독도 반환합니다.<br/>기본값은 **false**입니다.  |

**API**

```java
+ (void)Gamebase.Purchase.requestActivatedPurchases(@NonNull final Activity activity,
                                                    @NonNull final PurchasableConfiguration configuration,
                                                    @NonNull final GamebaseDataCallback<List<PurchasableReceipt>> callback);
```

**Example**

```java
final PurchasableConfiguration configuration = PurchasableConfiguration.newBuilder()
        .setAllStores(true)
        .build();
Gamebase.Purchase.requestActivatedPurchases(activity, configuration, new GamebaseDataCallback<List<PurchasableReceipt>>() {
    @Override
    public void onCallback(List<PurchasableReceipt> data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
        } else {
            // Failed.
            Log.e(TAG, "Request subscription list failed- "
                    + "errorCode: " + exception.getCode()
                    + "errorMessage: " + exception.getMessage());
        }
    }
});
```

### List Status of Subscriptions

현재 사용자 ID 기준으로 구입한 구독 상품의 상태를 조회할 수 있습니다.
결제가 완료된 구독 상품(자동 갱신형 구독, 자동 갱신형 소비성 구독 상품)은 만료되기 전까지 계속 조회할 수 있습니다.
**PurchasableConfiguration.setIncludeExpiredSubscriptions(true)** API로 만료된 구독 상품의 상태도 조회할 수 있습니다.
구독 상태 코드는 다음 문서를 참조하시기 바랍니다.
[NHN Cloud > SDK 사용 가이드 > IAP > Android > NHN Cloud IAP Class Reference > IapSubscriptionStatus.StatusCode](https://docs.nhncloud.com/en/TOAST/en/toast-sdk/iap-android/#iapsubscriptionstatusstatuscode)

> <font color="red">[주의]</font><br/>
>
> * 구독 상태 코드는 아래 가이드를 따라 구독 이벤트 설정을 해야 정상적으로 반환됩니다.
>     * [Game > Gamebase > 스토어 콘솔 가이드 > Google 콘솔 가이드 > Google 시스템 내 실시간 구독 정보 이벤트 전파 설정](../../console-google-guide.md#google_1)
>     * 이벤트 설정을 하지 않은 상태에서 구매한 구독 상품의 상태 코드는 항상 0(PURCHASED)이 반환됩니다.
> * 현재 구독 상품은 Google Play 스토어만 지원합니다.

**PurchasableConfiguration**

| API                                             | Mandatory(M) / Optional(O) | Description                              |
|-------------------------------------------------|----------------------------|------------------------------------------|
| newBuilder()                                    | **M**                      | Configuration 객체 생성을 위한 Builder를 생성합니다.  |
| build()                                         | **M**                      | 설정을 마친 Builder를 Configuration 객체로 변환합니다. |
| setIncludeExpiredSubscriptions(boolean include) | O                          | 만료된 구독 상품을 포함합니다.<br/>기본값은 **false**입니다. |

**API**

```java
+ (void)Gamebase.Purchase.requestSubscriptionsStatus(@NonNull final Activity activity,
                                                     @NonNull final PurchasableConfiguration configuration,
                                                     @NonNull final GamebaseDataCallback<List<PurchasableSubscriptionStatus>> callback);
```

**Example**

```java
final PurchasableConfiguration configuration = PurchasableConfiguration.newBuilder()
        .setIncludeExpiredSubscriptions(true)
        .build();
Gamebase.Purchase.requestSubscriptionsStatus(activity, configuration, new GamebaseDataCallback<List<PurchasableSubscriptionStatus>>() {
    @Override
    public void onCallback(List<PurchasableSubscriptionStatus> data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
        } else {
            // Failed.
            Log.e(TAG, "Request status of subscription list failed- "
                    + "errorCode: " + exception.getCode()
                    + "errorMessage: " + exception.getMessage()
                    + "errorDetail: " + exception.toString());
        }
    }
});
```

**VO**

```java
class PurchasableSubscriptionStatus {
    // 구매한 아이템의 상품 ID입니다.
    @Nullable
    String gamebaseProductId;
    
    // 구독 상태 코드입니다.
    //
    // IapSubscriptionStatus.StatusCode : https://docs.nhncloud.com/en/TOAST/en/toast-sdk/iap-android/#iapsubscriptionstatusstatuscode
    public int statusCode;
    
    // 구독 상태 코드에 대한 설명입니다.
    @NonNull
    public String statusDescription;
    
    // 구매한 상품의 가격입니다.
    float price;
    
    // 통화 코드입니다.
    @NonNull
    String currency;
    
    // 결제 식별자입니다.
    // purchaseToken과 함께 'Consume' 서버 API를 호출하는 데 사용하는 중요한 정보입니다.
    //
    // Consume API: https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
    // 주의: Consume API는 게임 서버에서 호출하세요!
    @NonNull
    String paymentSeq;
    
    // 결제 식별자입니다.
    // paymentSeq와 함께 'Consume' 서버 API를 호출하는 데 사용하는 중요한 정보입니다.
    // Consume API에서는 'accessToken' 이라는 이름의 파라미터로 전달해야 합니다.
    //
    // Consume API: https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
    // 주의: Consume API는 게임 서버에서 호출하세요!
    @NonNull
    String purchaseToken;
    
    // Google, Apple과 같이 스토어 콘솔에 등록된 상품 ID입니다.
    @NonNull
    String marketItemId;
    
    // 상품 타입으로, 다음 값들이 올 수 있습니다.
    // * UNKNOWN: 인식 불가능한 타입. Gamebase SDK를 업데이트하거나 Gamebase 고객 센터로 문의하세요.
    // * CONSUMABLE: 소비성 상품.
    // * AUTO_RENEWABLE: 구독형 상품.
    // * CONSUMABLE_AUTO_RENEWABLE: 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'.
    @NonNull
    String productType;
    
    // 상품을 구매했던 User ID.
    // 상품을 구매하지 않은 User ID로 로그인하면 구매한 아이템을 획득할 수 없습니다.
    @NonNull
    String userId;
    
    // 상품을 구매했던 Store Code.
    @NonNull
    public String storeCode;
    
    // 스토어의 결제 식별자입니다.
    @Nullable
    String paymentId;
    
    // 상품을 구매했던 시각입니다.(epoch time)
    long purchaseTime;
    
    // 구독이 종료되는 시각입니다.(epoch time)
    long expiryTime;
    
    // Google 결제 시 사용되는 값으로, 다음 값들이 올 수 있습니다.
    // Google 서버에서 장애가 발생하여 Gamebase 결제 서버에서 일시적으로 검증 로직을 종료하는 경우
    // null로만 반환되므로 항상 유효한 값을 보장하지 않을 수 있습니다.
    // * null: 일반 결제
    // * Test: 테스트 결제
    // * Promo: Promotion 결제
    @Nullable
    String purchaseType;
    
    // 구독 상품은 갱신될 때마다 paymentId가 변경됩니다.
    // 이 필드는 구독 상품을 최초 결제했을 때의 paymentId를 알려줍니다.
    // 스토어 및 결제 서버 상태에 따라 값이 존재하지 않을 수 있으므로
    // 항상 유효한 값을 보장하지는 않습니다.
    @Nullable
    String originalPaymentId;
    
    // itemSeq로 상품을 구매하는 Legacy API용 식별자입니다.
    long itemSeq;
    
    // Gamebase.Purchase.requestPurchase API 호출 시 payload로 전달했던 값입니다.
    // 스토어 서버 상태에 따라 정보가 유실되는 경우가 있으므로 사용을 권장하지 않습니다.
    @Nullable
    String payload;
}
```

**Response Example**

```json
{
    "gamebaseProductId": "my_subcription_product_002",
    "statusCode": 13,
    "statusDescription": "EXPIRED",
    "userId": "AS@123456ABCDEFGHIJ",
    "storeCode": "GG",
    "currency": "KRW",
    "expiryTime": 1675012345678,
    "itemSeq": 1000003,
    "marketItemId": "my_subcription_product_002",
    "originalPaymentId": "GPA.1111-2222-3333-56789",
    "paymentId": "GPA.1111-2222-3333-56789",
    "paymentSeq": "2021032510000002",
    "price": 1000.0,
    "productType": "CONSUMABLE_AUTO_RENEWABLE",
    "purchaseTime": 1675001234567,
    "purchaseToken": "kfetTfGk4...",
    "purchaseType": "Test"
}
```

### Event by Purchase

Promotion 코드를 입력해 상품을 획득했거나 Pending 결제(느린 결제, 부모 동의 등)가 완료되었을 때 GamebaseEventHandler를 통해 이벤트를 받아 처리할 수 있습니다.
GamebaseEventHandler로 프로모션 결제 및 지연 결제 이벤트를 처리하는 방법은 아래 가이드를 확인하세요.
[Game > Gamebase > Android SDK 사용 가이드 > ETC > Gamebase Event Handler](../../aos-etc.md#purchase-updated)
