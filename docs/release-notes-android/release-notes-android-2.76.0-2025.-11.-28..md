---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.76.0, 기능개선, 기능추가, 변경, Purchase"
section: "2.76.0 (2025. 11. 28.)"
order: 5
---

### 2.76.0 (2025. 11. 28.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.76.0/GamebaseSDK-Android.zip)

#### 기능 추가

* 미국 텍사스, 유타, 루이지애나와 같은 관할권의 특정 연령 확인 법률에 따른 준수 의무를 충족하는 데 도움이 되도록 Google Play Age Signals 기반의 연령 확인 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Age Signals Support](../../aos-etc.md#age-signals-support)
    * Play Age Signals 라이브러리 버전이 베타(0.0.1-beta02) 상태이므로 API는 항상 예외가 발생합니다.
        * 정상 동작을 위해서는 Play Age Signals 라이브러리 0.0.2 버전이 적용된 Gamebase Android SDK 2.78.0을 사용하세요.

#### 기능 개선/변경

* **Gamebase.Purchase.requestItemListAtIAPConsole()** API가 deprecated되었습니다.
    * **Gamebase.Purchase.requestItemListPurchasable()** API를 사용하세요.
