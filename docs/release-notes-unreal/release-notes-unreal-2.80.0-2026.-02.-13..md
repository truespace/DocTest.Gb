---
source: release-notes-unreal.md
section: "2.80.0 (2026. 02. 13.)"
order: 2
split: true
created_date_time: 20260408_191848
keyword: Unreal, Purchase, Error, Android, iOS, Release Notes, 2.80.0
---

### 2.80.0 (2026. 02. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 결제 요청 시 느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우, 신규로 추가된 **PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 GamebaseEventCategory.PURCHASE_UPDATED 이벤트 기능이 확장되었습니다.
    * 앱이 실행 중일 때 GamebaseEventHandler를 통해 Pending 결제(느린 결제, 부모 동의 등) 완료 이벤트를 제공 받을 수 있습니다.
* (iOS) Project Settings의 설정에 따라 Info.plist에 필요한 항목이 자동으로 추가되도록 개선되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > iOS Settings](../unreal-started.md#ios-settings)
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.80.0](../release-notes-android.md#2800-2026-02-13)
* [Gamebase iOS SDK 2.80.0](../release-notes-ios.md#2800-2026-02-13)
