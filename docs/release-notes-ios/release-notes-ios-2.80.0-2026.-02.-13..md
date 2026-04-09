---
source: release-notes-ios.md
section: "2.80.0 (2026. 02. 13.)"
order: 1
split: true
created_date_time: 20260408_184906
keyword: iOS, Purchase, Error, XCode, Release Notes, 2.80.0
---

## Game > Gamebase > 릴리스 노트 > iOS

### 2.80.0 (2026. 02. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 26.0으로 변경되었습니다.
* 결제 요청 시 Ask to Buy 등으로 결제가 지연되면 **TCGB_ERROR_PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 kTCGBPurchaseUpdated 이벤트 기능이 확장되었습니다.
    * App Store 프로모션 상품 구매 완료 또는 Ask to Buy 등으로 지연된 결제가 완료되었을 때 이벤트를 수신할 수 있습니다.
* 내부 로직 개선
* 아래 API가 deprecated되었습니다.
    * **+[TCGBPurchase setPromotionIAPHandler:]**
