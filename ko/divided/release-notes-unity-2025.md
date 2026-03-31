## Game > Gamebase > 릴리스 노트 > Unity

### 2.77.0 (2025. 12. 09.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.77.0/GamebaseSDK-Unity.zip)

####  기능 추가
* (WebGL) 브라우저 로그인 지원

#### 기능 개선
* Gamebase.Purchase.RequestItemListAtIAPConsole() API가 deprecated되었습니다.
  * Gamebase.Purchase.RequestItemListPurchasable() API 사용을 권장합니다.

#### 버그 수정
* (WebGL) 게스트 로그인 실패 문제를 수정했습니다.

### 2.76.0 (2025. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.76.0/GamebaseSDK-Unity.zip)

####  기능 추가
* 가장 최근 게시된 게임 공지의 게시 시간을 제공하기 위해 launching.app.gameNotice.latestNoticeTimeMillis 필드를 추가했습니다.
* (Android) 미국 텍사스, 유타, 루이지애나 등 특정 관할권의 연령 확인 관련 법률 준수를 지원하기 위해 Google Play Age Signals 기반의 연령 확인 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 참고사항 > Age Signals Support](./unity-etc/#age-signals-support) 

### 2.75.1 (2025. 10. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* (Windows) AdditionalInfo가 null인 경우 발생하던 예외를 수정했습니다.
* (macOS) GamebaseUtil에서 발생하던 DllNotFoundException 문제를 수정했습니다.

### 2.75.0 (2025. 09. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (Windows) Mapping 기능 추가

#### 기능 개선/변경
* (Android) Google Play의 16KB 페이지 제약 대응
* 내부 로직을 개선하였습니다.

### 2.74.0 (2025. 08. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.74.0/GamebaseSDK-Unity.zip)

#### 버그 수정
* (iOS) ChangeLogin 시 발생하던 크래시 이슈를 수정했습니다.
* (macOS) GamebaseUtil에서 발생하던 DllNotFoundException 문제를 수정했습니다.

#### 기타
* 최소 지원 버전이 Unity 2022.3.10으로 상향되었습니다.

### 2.73.2 (2025. 07. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.2/GamebaseSDK-Unity.zip)

#### 기능 개선
* (Standalone) 로그인 IDP 추가 지원: Twitter, Apple, Line

#### 지원 종료
* 아마존 앱스토어 지원이 종료됩니다.

### 2.73.1 (2025. 07. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* (iOS) 빌드 오류 수정
* (macOS) 웹뷰 어댑터 빌드 오류 수정

### 2.73.0 (2025. 07. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.0/GamebaseSDK-Unity.zip)

#### 기능 추가

#### 기능 개선/변경
* (Windows, macOS) IdP 로그인 시 웹뷰에서 외부 브라우저로 변경했습니다.
    * 지원 브라우저
        * Windows: 모든 브라우저
        * macOS: Chrome, Safari, Firefox, Whale

* 외부 브라우저 로그인 취소 API를 추가했습니다.
    * 진행 중인 외부 브라우저 로그인 요청 중 IdP를 변경하고 싶을 때 기존 요청을 취소하기 위함.
    * CancelLoginWithExternalBrowser()

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.73.0](./release-notes-android/#2730-2025-07-15)
* [Gamebase iOS SDK 2.73.0](./release-notes-ios/#2730-2025-07-15)

### 2.72.0 (2025. 06. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (Windows) 업데이트 팝업에 자세히 보기 버튼을 추가하였습니다.
* (Windows) 이용 정지 팝업에 고객 센터 링크를 추가하였습니다.

#### 기능 개선/변경

* (Windows) 내부 로직을 개선하였습니다.

#### 버그 수정

* (Windows) 점검 상태로 갱신되지 않던 문제를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.72.0](./release-notes-android/#2720-2025-06-24)
* [Gamebase iOS SDK 2.72.0](./release-notes-ios/#2720-2025-06-24)

### 2.71.1 (2025. 06. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.1/GamebaseSDK-Unity.zip)

#### 버그 수정

* (macOS) GamebaseUtil의 DllNotFoundException 문제를 수정했습니다.

### 2.71.0 (2025. 04. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* '게임 공지' 신규 기능이 추가되었습니다.
    * Gamebase.GameNotice.OpenGameNotice(GamebaseCallback.ErrorDelegate callback)
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unity SDK 사용 가이드 > 공지 > 게임 공지](./unity-ui/#gamenotice)

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.
* (iOS) ViewController 설정 로직을 개선하여 초기화 실패 오류를 방지합니다.

#### 버그 수정

* macOS 15.4에서 크래시가 발생하는 이슈를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.71.0](./release-notes-android/#2710-2025-04-15)
* [Gamebase iOS SDK 2.71.0](./release-notes-ios/#2710-2025-04-15)

### 2.70.1 (2025. 03. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.1/GamebaseSDK-Unity.zip)

#### 버그 수정

* (Android) ShowWebView, ShowTermsView 호출 시 Configuration이 없으면 크래시가 발생하는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.70.1](./release-notes-android/#2701-2025-03-13)
* [Gamebase iOS SDK 2.70.0](./release-notes-ios/#2700-2025-03-11)

### 2.70.0 (2025. 03. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (Android) 'GPGS 자동 로그인' 기능 연동 시 유저에게 GPGS 로그인을 앱 설치 후 한번만 물어보는 초기화 옵션을 추가했습니다.
  * GamebaseRequest.GamebaseConfiguration enableGPGSSignInCheck
    * 기본 설정은 true로, 유저가 GPGS 로그인을 거부하더라도 Gamebase 초기화 때 GPGS 로그인 창을 다시 표시합니다.
    * false로 설정하면 앱 최초 실행 시에만 GPGS 로그인 창이 한번 표시됩니다.
* GamebaseWebView에 내비게이션 바 타이틀과 아이콘 틴트 컬러 설정 옵션을 추가했습니다.
    * WebView.Configuration navigationTitleColor
    * WebView.Configuration navigationIconTintColor

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.70.0](./release-notes-android/#2700-2025-03-11)
* [Gamebase iOS SDK 2.70.0](./release-notes-ios/#2700-2025-03-11)

#### Setting Tool (v3.0.0)

* 사용 목적에 맞게 사용자 친화적인 UX로 개선했습니다.
* 직관적인 기능 제공으로 설정 및 업데이트가 더 쉬워졌습니다.
* 배포 시 유연하게 업데이트할 수 있도록 개선했습니다.

### 2.69.0 (2025. 1. 21.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* RequestLastLoggedInProvider API 추가
* (Android) WebView Cutout color 기능 추가
* (Windows, macOS) X(Twitter) 로그인 지원

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.
* WebView 색상 설정 관련 코드 개선
    * Configuration 내부에 필드 추가
        * WebView.Configuration navigationColor
        * Community.Configuration backgroundColor
        * ImageNotice.Configuration backgroundColor

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.69.0](./release-notes-android/#2690-2025-01-21)
* [Gamebase iOS SDK 2.69.0](./release-notes-ios/#2690-2025-01-21)
