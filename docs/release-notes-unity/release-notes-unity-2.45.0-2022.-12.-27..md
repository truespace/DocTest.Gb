---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "2.45.0 (2022. 12. 27.)"
section: "2.45.0 (2022. 12. 27.)"
order: 45
---

### 2.45.0 (2022. 12. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.45.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Deprecated API 
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
         
        // New API 
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                       GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **GamebaseRequest.Purchase.PurchasableConfiguration.allStores**의 값을 **true**로 설정해야 합니다.

            // Deprecated API 
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
             
            // New API
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                        GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Unity SDK (0.27.1)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.45.0](../../release-notes-android.md#2450-2022-12-27)
* [Gamebase iOS SDK 2.45.0](../../release-notes-ios.md#2450-2022-12-27)
