---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "2.80.0 (2026. 02. 13.)"
section: "2.80.0 (2026. 02. 13.)"
order: 3
---

### 2.80.0 (2026. 02. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-Unity.zip)

#### 기능 개선
* (Android, iOS) 결제 요청 시 느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우, 신규로 추가된 **PURCHASE_PENDING(4008)** 오류가 발생하게 됩니다.
* (Android, iOS) Gamebase Event Handler의 GamebaseEventCategory.PURCHASE_UPDATED 이벤트 기능이 확장되었습니다.
    * 앱이 실행 중일 때 GamebaseEventHandler를 통해 Pending 결제(느린 결제, 부모 동의 등) 완료 이벤트를 제공 받을 수 있습니다.

#### 버그 수정
* (Windows, macOS) WebView를 닫은 후 다시 열었을 때 기존 창으로 뒤로 가기가 가능하던 문제를 수정했습니다.
* (Windows, macOS) WebView 내비게이션에 상단 웹뷰가 가려지던 문제를 수정했습니다.
* (Android) 게임 공지 배경이 투명하게 표시되던 문제를 수정했습니다.
