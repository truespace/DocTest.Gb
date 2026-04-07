---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v2.38.0, 버그수정, 기능개선, 기능추가, 변경, Purchase"
section: "2.38.0 (2022. 05. 03.)"
order: 53
---

### 2.38.0 (2022. 05. 03.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.38.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.3)

#### 기능 개선/변경
* Display Language의 중국어 번체(zh-TW) 언어셋에서 어색한 문장이 수정되었습니다.

#### 버그 수정
* (Android) API Level 24 미만에서 특정 API 호출 시 오류가 발생하지 않도록 수정되었습니다.
    * Gamebase.Purchase.RequestActivatedPurchases()
    * Gamebase.Purchase.RequestItemListOfNotConsumed()

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.38.0](../release-notes-android.md#2380-2022-05-03)
* [Gamebase iOS SDK 2.38.0](../release-notes-ios.md#2380-2022-05-03)
