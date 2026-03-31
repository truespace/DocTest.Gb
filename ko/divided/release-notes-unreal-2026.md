## Game > Gamebase > 릴리스 노트 > Unreal

### 2.81.0 (2026. 03. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.81.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.80.0](./release-notes-android/#2800-2026-02-13)
* [Gamebase iOS SDK 2.80.0](./release-notes-ios/#2800-2026-02-13)

### 2.80.0 (2026. 02. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 결제 요청 시 느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우, 신규로 추가된 **PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 GamebaseEventCategory.PURCHASE_UPDATED 이벤트 기능이 확장되었습니다.
    * 앱이 실행 중일 때 GamebaseEventHandler를 통해 Pending 결제(느린 결제, 부모 동의 등) 완료 이벤트를 제공 받을 수 있습니다.
* (iOS) Project Settings의 설정에 따라 Info.plist에 필요한 항목이 자동으로 추가되도록 개선되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > iOS Settings](./unreal-started/#ios-settings)
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.80.0](./release-notes-android/#2800-2026-02-13)
* [Gamebase iOS SDK 2.80.0](./release-notes-ios/#2800-2026-02-13)

### 2.79.0 (2026. 01. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.79.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.79.0](./release-notes-android/#2790-2026-01-27)
* [Gamebase iOS SDK 2.79.0](./release-notes-ios/#2790-2026-01-27)

### 2.78.0 (2026. 01. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.78.0/GamebaseSDK-Unreal.zip)

####  기능 추가

* 언리얼 엔진 지원 버전이 변경되었습니다.
    * 4.27 ~ 5.7

#### 기능 개선/변경

* 내부 로직을 개선했습니다.

#### 버그 수정
* (Windows) Payload를 포함한 RequestPurchase API 호출 시 Payload가 콘솔에 전송되지 않는 문제를 수정했습니다.
* (Windows) NHNWebView를 이용한 웹뷰 노출 관련 기능을 처음 노출 시 High DPI 관련 설정 여부에 따라 DPI가 높은 환경에서 프로그램 창이 줄어드는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.78.0](./release-notes-android/#2780-2025-12-23)
* [Gamebase iOS SDK 2.77.0](./release-notes-ios/#2770-2025-12-09)
