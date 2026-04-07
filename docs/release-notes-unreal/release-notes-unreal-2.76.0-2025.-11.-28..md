---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, v2.76.0, 버그수정, 기능개선, 기능추가, 변경"
section: "2.76.0 (2025. 11. 28.)"
order: 5
---

### 2.76.0 (2025. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.76.0/GamebaseSDK-Unreal.zip)

####  기능 추가

* 가장 최근 게시된 게임 공지의 게시 시간을 제공하기 위해 `FGamebaseLaunchingInfo::FApp::FGameNotice::LatestNoticeTimeMillis` 필드를 추가했습니다.
* (Android) 미국 텍사스, 유타, 루이지애나 등 특정 관할권의 연령 확인 관련 법률 준수를 지원하기 위해 Google Play Age Signals 기반의 연령 확인 API가 추가되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 참고사항 > Age Signals Support](../unreal-etc.md#age-signals-support)
* (Windows) Steam 인증 시 Steamworks SDK가 로드되지 않은 경우 외부 브라우저를 통한 로그인을 지원합니다.

#### 기능 개선/변경

* `IGamebasePurchase::RequestItemListAtIAPConsole()` API가 deprecated되었습니다.
    * `IGamebasePurchase::RequestItemListPurchasable()` API를 사용하세요.
* 내부 로직을 개선했습니다.

#### 버그 수정
* (Windows) Google 결제 시 브라우저 로그인 상태에 따라 결제 완료 후 결과가 게임에 전달되지 않는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.76.0](../release-notes-android.md#2760-2025-11-28)
* [Gamebase iOS SDK 2.75.0](../release-notes-ios.md#2750-2025-09-23)
