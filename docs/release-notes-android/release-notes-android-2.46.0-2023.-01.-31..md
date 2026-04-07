---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.46.0, 기능개선, 기능추가, 변경, Purchase"
section: "2.46.0 (2023. 01. 31.)"
order: 45
---

### 2.46.0 (2023. 01. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.46.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 구독 상태를 조회할 수 있는 API가 추가되었습니다.
    * Gamebase.Purchase.requestSubscriptionsStatus(Activity, PurchasableConfiguration, GamebaseDataCallback&lt;List&lt;PurchasableSubscriptionStatus&gt;&gt;)
    * PurchasableConfiguration.Builder.setIncludeExpiredSubscriptions(boolean) API로 만료된 구독 상태도 조회할 수 있습니다.
* 웹뷰에서 SafeArea를 무시하고 Cutout 영역에도 렌더링할 수 있는 옵션을 추가했습니다.
    * GamebaseWebViewConfiguration.Builder.setRenderOutsideSafeArea(boolean)

#### 기능 개선/변경
* 외부 SDK 업데이트: Kakaogame SDK (3.14.14)
