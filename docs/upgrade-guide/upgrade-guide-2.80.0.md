---
source: upgrade-guide.md
section: "2.80.0"
order: 4
split: true
created_date_time: 20260616_110448
keyword: XCode, iOS, Unreal, Upgrade Guide, 2.80.0, Android
---

## 2.80.0

### Android

* Gamebase Android SDK 2.80.0은 다음 이슈가 발생합니다.
    * Pending 이벤트 관련 로직이 IAP 서버에 부하를 주는 문제가 존재합니다.
    * 이슈가 해결된 Gamebase Android SDK 2.80.1을 사용하세요.

### iOS

* Xcode 최소 지원 버전이 16.0에서 26.0으로 변경되었습니다.
* **+[TCGBPurchase setPromotionIAPHandler:]** API가 deprecated되었습니다.

### Unreal

* (iOS) Project Settings에서 활성화한 기능에 따라 Info.plist에 필요한 항목이 자동으로 추가됩니다.
    * `AdditionalPlistData`로 직접 관리하려면 [iOS Settings](../unreal-started.md#ios-settings)에서 **Disable Auto Info.plist Update**를 활성화하세요.
