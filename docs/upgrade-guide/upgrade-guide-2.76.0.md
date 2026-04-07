---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.76.0, Android, Unreal"
section: 2.76.0
order: 5
---

## 2.76.0

### Android

* **Gamebase.Purchase.requestItemListAtIAPConsole()** API가 deprecated되었습니다.
    * **Gamebase.Purchase.requestItemListPurchasable()** API를 사용하세요.
* 미국 텍사스, 유타, 루이지애나와 같은 관할권의 특정 연령 확인 법률에 따른 준수를 위해 추가된 연령 확인 API는 Play Age Signals 라이브러리 버전이 베타(0.0.1-beta02) 상태이므로 항상 예외가 발생합니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Age Signals Support](../../aos-etc.md#age-signals-support)
    * 향후 정상 동작을 위해서는 Play Age Signals 라이브러리 버전이 0.0.2로 업데이트된 Gamebase Android SDK 2.78.0을 사용하세요.

### Unreal

* `IGamebasePurchase::RequestItemListAtIAPConsole()` API가 deprecated되었습니다.
    * `IGamebasePurchase::RequestItemListPurchasable()` API를 사용하세요.
