---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.45.0, 신규, 버그수정, 기능개선, 변경, Purchase"
section: "2.45.0 (2022. 12. 27.)"
order: 46
---

### 2.45.0 (2022. 12. 27.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.45.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: NHN Cloud Android SDK (1.4.0), Payco Android SDK (1.5.9), Hangame Android SDK (1.6.2)
* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Deprecated API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity,
                                                       GamebaseDataCallback<List<PurchasableReceipt>>);
        
        // New API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity,
                                                       PurchasableConfiguration,
                                                       GamebaseDataCallback<List<PurchasableReceipt>>);

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **PurchasableConfiguration.setAllStores(true)**로 설정해야 합니다.

            // Deprecated API
            Gamebase.Purchase.requestActivatedPurchases(Activity,
                                                        GamebaseDataCallback<List<PurchasableReceipt>>);

            // New API
            Gamebase.Purchase.requestActivatedPurchases(Activity,
                                                        PurchasableConfiguration,
                                                        GamebaseDataCallback<List<PurchasableReceipt>>);

#### 버그 수정

* 앱 실행 시 간헐적으로 ConcurrentModification 예외가 발생하는 문제를 수정했습니다.
* Hangame thirdIdP 로그인 후 Gamebase.getAuthProviderUserID() 호출 시 NullPointerException이 발생하는 오류를 수정했습니다.
