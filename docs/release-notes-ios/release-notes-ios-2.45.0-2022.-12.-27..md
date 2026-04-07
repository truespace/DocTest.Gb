---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.45.0, 신규, 기능개선, 기능추가, 변경, Purchase"
section: "2.45.0 (2022. 12. 27.)"
order: 43
---

### 2.45.0 (2022. 12. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.45.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 어떤 스토어에 대한 결제 영수증인지 알 수 있도록 다음 필드가 추가되었습니다.
    * **TCGBPurchasableReceipt.storeCode**
* 결제 API 호출 시 추가 설정을 할 수 있는 **TCGBPurchasableConfiguration** VO를 추가하였습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 결제 > TCGBPurchasableConfiguration](../../ios-purchase.md#tcgbpurchasableconfiguration)
* **TCGBPurchasableConfiguration**을 파라미터로 받는 신규 미소비 내역 조회 API를 추가하였습니다.
    * **[TCGBPurchase requestItemListOfNotConsumedWithConfiguration:completion:]**
* **TCGBPurchasableConfiguration**을 파라미터로 받는 신규 활성화 구독 조회 API를 추가하였습니다.
    * **[TCGBPurchase requestActivatedPurchasesWithConfiguration:completion:]**

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.2.0)
    * Hangame iOS SDK (1.8.0)
* 아래 API가 deprecated되었습니다.
    * **+[TCGBPurchase requestItemListOfNotConsumedWithCompletion:]**
    * **+[TCGBPurchase requestActivatedPurchasesWithCompletion:]**
* SDK 내부 로직 개선
