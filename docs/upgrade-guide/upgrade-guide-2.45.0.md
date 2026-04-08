---
source: upgrade-guide.md
section: "2.45.0"
order: 32
split: true
created_date_time: 20260408_191848
keyword: Purchase, Consume, RequestItemListOfNotConsumed, Android, iOS, Upgrade Guide, 2.45.0
---

## 2.45.0

### Android, iOS, Unity

* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Unity: Deprecated API
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
        // Unity: New API
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                       GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
        // Android: Deprecated API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity activity,
                                                       GamebaseDataCallback<List<PurchasableReceipt>> callback);
        // Android: New API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity activity,
                                                       PurchasableConfiguration configuration,
                                                       GamebaseDataCallback<List<PurchasableReceipt>> callback);
        // iOS: Deprecated API
        + (void)requestItemListOfNotConsumedWithCompletion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
        // iOS: New API
        + (void)requestItemListOfNotConsumedWithConfiguration:(TCGBPurchasableConfiguration *)configuration
                                                   completion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **PurchasableConfiguration.allStores**를 **true**로 설정해야 합니다.

            // Unity: Deprecated API
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
            // Unity: New API
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                        GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
            // Android: Deprecated API
            Gamebase.Purchase.requestActivatedPurchases(Activity activity,
                                                        GamebaseDataCallback<List<PurchasableReceipt>> callback);
            // Android: New API
            Gamebase.Purchase.requestActivatedPurchases(Activity activity,
                                                        PurchasableConfiguration configuration,
                                                        GamebaseDataCallback<List<PurchasableReceipt>> callback);
            // iOS: Deprecated API
            + (void)requestActivatedPurchasesWithCompletion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
            // iOS: New API
            + (void)requestActivatedPurchasesWithConfiguration:(TCGBPurchasableConfiguration *)configuration
                                                    completion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
