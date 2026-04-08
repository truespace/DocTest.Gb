---
source: release-notes-unreal.md
section: "2.49.0 (2023. 04. 11.)"
order: 31
split: true
created_date_time: 20260408_191848
keyword: Unreal, Consume, WebView, Error, RequestItemListOfNotConsumed, XCode, Android, iOS, Release Notes, 2.49.0
---

### 2.49.0 (2023. 04. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.
 
        // Deprecated API
        void RequestItemListOfNotConsumed(const FGamebasePurchasableReceiptListDelegate& onCallback);
        // New API
        void RequestItemListOfNotConsumed(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableReceiptListDelegate& onCallback);
 
* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **FGamebasePurchasableConfiguration.allStores**를 **true**로 설정해야 합니다.
 
            // Deprecated API
            void RequestActivatedPurchases(const FGamebasePurchasableReceiptListDelegate& onCallback);
            // New API
            void RequestActivatedPurchases(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableReceiptListDelegate& onCallback);

* (Android) IAP 구독 상태를 조회할 수 있는 RequestSubscriptionsStatus API가 추가되었습니다.
* (Android) 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드를 재지원합니다.
    * GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 웹뷰에서 컷아웃(노치) 영역을 비롯한 모든 이용 가능한 스크린 공간을 사용하여 렌더링할 수 있는 설정이 추가되었습니다.
    * GamebaseWebViewConfiguration.renderOutsideSafeArea

#### 기능 개선/변경
* Unreal의 최소 지원 버전이 4.26으로 변경되었습니다.
* (iOS) Xcode 14.1에서 빌드 시 오류가 발생되는 이슈가 수정되었습니다.
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.48.0](../release-notes-android.md#2480-2023-03-28)
* [Gamebase iOS SDK 2.49.0](../release-notes-ios.md#2490-2023-04-11)
