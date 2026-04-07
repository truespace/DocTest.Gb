---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.80.0, 버그수정, 기능개선, 변경, TermsView"
section: "2.80.0 (2026. 02. 13.)"
order: 1
---

## Game > Gamebase > 릴리스 노트 > Android

### 2.80.0 (2026. 02. 13.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 결제 요청 시 느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우, 신규로 추가된 **PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 GamebaseEventCategory.PURCHASE_UPDATED 이벤트 기능이 확장되었습니다.
    * 앱이 실행 중일 때 GamebaseEventHandler를 통해 Pending 결제(느린 결제, 부모 동의 등) 완료 이벤트를 제공 받을 수 있습니다.

#### 버그 수정

* 약관 창 사이즈가 간헐적으로 크게 보이는 이슈 수정
* 난독화 적용 시 알림 권한 자동 요청 팝업이 표시되지 않는 이슈 수정
