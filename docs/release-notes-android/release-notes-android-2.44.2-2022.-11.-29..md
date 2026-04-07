---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.44.2 (2022. 11. 29.)"
section: "2.44.2 (2022. 11. 29.)"
order: 47
---

### 2.44.2 (2022. 11. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.2/GamebaseSDK-Android.zip)

#### 기능 추가
* PurchasableReceipt VO 클래스에 'storeCode' 필드가 추가되었습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: Kotlin (1.7.20), Hangame Android SDK (1.6.1)
* Google '사전 출시 보고서'의 권고 사항을 반영하여 Gamebase 웹뷰를 수정했습니다.
    * 타이틀 바 사이즈 확대
    * 이미지 설명 문구 수정

#### 버그 수정
* PurchasableItem VO 클래스의 'itemName' 필드에 잘못 선언된 'deprecated' 어노테이션을 제거했습니다.
