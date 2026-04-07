---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v2.36.0, 버그수정, 기능추가, 변경, Purchase, Push"
section: "2.36.0 (2022. 04. 12.)"
order: 55
---

### 2.36.0 (2022. 04. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.36.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.2)
* 결제 시 프로모션 여부를 알 수 있는 isPromotion 필드가 추가되었습니다.
    * GamebaseResponse.Purchase.PurchasableReceipt.isPromotion
* 결제 시 테스트 결제 여부를 알 수 있는 isTestPurchase 필드가 추가되었습니다.
    * GamebaseResponse.Purchase.PurchasableReceipt.isTestPurchase

#### 버그 수정
* 디바이스가 특정 문화권으로 설정되었을 때 결제 상품 가격 정보가 0으로 입력되는 오류가 수정되었습니다.
* (iOS) Push 알림 클릭 시 딥 링크가 동작하지 않는 오류가 수정되었습니다.
* (iOS) 프로젝트의 orientation이 Auto Rotation으로 설정되어 있고, 프로젝트 첫 신(scene)에 포함된 MonoBehaviour의 Awake에서 Gamebase API 호출 시 웹뷰 등의 UI 출력이 정상적으로 되지 않는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.36.0](../../release-notes-android.md#2360-2022-04-12)
* [Gamebase iOS SDK 2.36.0](../../release-notes-ios.md#2360-2022-04-12)
