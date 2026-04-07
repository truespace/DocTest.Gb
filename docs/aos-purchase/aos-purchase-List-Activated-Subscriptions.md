---
source: aos-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Purchase, Subscription, Error, IAP, setAllStores, requestActivatedPurchases, isSuccess, getMessage"
section: "List Activated Subscriptions"
order: 8
---

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
