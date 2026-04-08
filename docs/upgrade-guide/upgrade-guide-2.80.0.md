---
source: upgrade-guide.md
section: "2.80.0"
order: 2
split: true
created_date_time: 20260408_191848
keyword: XCode, iOS, Unreal, Upgrade Guide, 2.80.0
---

## 2.80.0

### iOS

* Xcode 최소 지원 버전이 16.0에서 26.0으로 변경되었습니다.
* **+[TCGBPurchase setPromotionIAPHandler:]** API가 deprecated되었습니다.

### Unreal

* (iOS) Project Settings에서 활성화한 기능에 따라 Info.plist에 필요한 항목이 자동으로 추가됩니다.
    * `AdditionalPlistData`로 직접 관리하려면 [iOS Settings](../unreal-started.md#ios-settings)에서 **Disable Auto Info.plist Update**를 활성화하세요.
