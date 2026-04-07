---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.77.0, Common, iOS, Unity"
section: 2.77.0
order: 4
---

## 2.77.0

### Common

* Apple 계정을 revoke했을 때 발생하는 GamebaseEventHandler의 IdP Revoked 이벤트의 권장 가이드를 변경하였습니다.
    * 유저에게 IdP가 사용 중지된 것을 알리고, 탈퇴 대신 로그아웃 후 다시 로그인할 수 있도록 변경하시기 바랍니다.

### iOS

* **+[TCGBPurchase requestItemListAtIAPConsoleWithCompletion:]** API가 deprecated되었습니다.
    * **+[TCGBPurchase requestItemListPurchasableWithCompletion:]** API를 사용하세요.

### Unity

* **Gamebase.Purchase.RequestItemListAtIAPConsole():** API가 deprecated되었습니다.
    * **Gamebase.Purchase.RequestItemListPurchasable()** API를 사용하세요.
