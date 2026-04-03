---
source: release-notes-unity.md
section: "2.81.0 (2026. 03. 24.)-to-2.63.0 (2024. 04. 23.)"
order: 1
created_date: 2026-04-03
---

## Game > Gamebase > 릴리스 노트 > Unity

### 2.81.0 (2026. 03. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.81.0/GamebaseSDK-Unity.zip)

#### 기능 추가
- (Windows, macOS) 외부 브라우저 로그인 IDP에 Epicgames가 추가되었습니다.

### 2.80.1 (2026. 03. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* (iOS) GameCenter에서 AddMapping 수행 시 오류가 발생하던 문제를 수정했습니다.
* (Windows) WebView 오픈시, 타이틀 영역을 클릭하면 웹뷰가 닫히는 문제를 수정했습니다.

#### 기능 개선
* (Windows) WebView 내부 로직을 개선하였습니다.

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

### 2.79.0 (2026. 01. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.79.0/GamebaseSDK-Unity.zip)

#### 기능 개선
* (Windows, macOS) WebView barHeight이 설정되지 않았을 때 내비게이션이 보이지 않던 문제를 수정했습니다.
* (Windows, macOS) WebView isBackButtonVisible 설정 시 Close 버튼이 보이지 않던 문제를 수정했습니다.

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
    * [Game > Gamebase > Unity SDK 사용 가이드 > 참고사항 > Age Signals Support](../../unity-etc.md#age-signals-support) 

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
* [Gamebase Android SDK 2.73.0](../../release-notes-android.md#2730-2025-07-15)
* [Gamebase iOS SDK 2.73.0](../../release-notes-ios.md#2730-2025-07-15)

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
* [Gamebase Android SDK 2.72.0](../../release-notes-android.md#2720-2025-06-24)
* [Gamebase iOS SDK 2.72.0](../../release-notes-ios.md#2720-2025-06-24)

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
        * [Game > Gamebase > Unity SDK 사용 가이드 > 공지 > 게임 공지](../../unity-ui.md#gamenotice)

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.
* (iOS) ViewController 설정 로직을 개선하여 초기화 실패 오류를 방지합니다.

#### 버그 수정

* macOS 15.4에서 크래시가 발생하는 이슈를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.71.0](../../release-notes-android.md#2710-2025-04-15)
* [Gamebase iOS SDK 2.71.0](../../release-notes-ios.md#2710-2025-04-15)

### 2.70.1 (2025. 03. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.1/GamebaseSDK-Unity.zip)

#### 버그 수정

* (Android) ShowWebView, ShowTermsView 호출 시 Configuration이 없으면 크래시가 발생하는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.70.1](../../release-notes-android.md#2701-2025-03-13)
* [Gamebase iOS SDK 2.70.0](../../release-notes-ios.md#2700-2025-03-11)

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
* [Gamebase Android SDK 2.70.0](../../release-notes-android.md#2700-2025-03-11)
* [Gamebase iOS SDK 2.70.0](../../release-notes-ios.md#2700-2025-03-11)

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
* [Gamebase Android SDK 2.69.0](../../release-notes-android.md#2690-2025-01-21)
* [Gamebase iOS SDK 2.69.0](../../release-notes-ios.md#2690-2025-01-21)

### 2.68.1 (2024. 12. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 플랫폼별 변경 사항

* [Gamebase iOS SDK 2.68.1](../../release-notes-ios.md#2681-2024-12-10)

### 2.68.0 (2024. 11. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.0/GamebaseSDK-Unity.zip)

#### 지원 종료

* FacebookAdapter for Unity 지원이 종료됩니다.

#### 기능 추가

* (Android) GameActivity를 지원합니다.

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 버그 수정

* NHN Cloud Console에서 네트워크 인사이트 설정을 활성화하면 JSON 파싱 오류가 발생하는 현상이 개선되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.68.0](../../release-notes-android.md#2680-2024-11-26)
* [Gamebase iOS SDK 2.68.0](../../release-notes-ios.md#2680-2024-11-26)

### 2.67.0 (2024. 10. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (Android, iOS) Steam 인증 추가

#### 기능 개선/변경

* Unity 최소 지원 버전 변경: 2020.3.16f1
* 롤링 이미지 공지의 WebView 내부에서 exception이 발생한 경우, 실패 콜백이 호출되도록 변경되었습니다.
* 내부 로직을 개선하였습니다.

#### 버그 수정

* storeCodeStandalone 코드로 인해 발생하는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.67.0](../../release-notes-android.md#2670-2024-10-29)
* [Gamebase iOS SDK 2.67.0](../../release-notes-ios.md#2670-2024-10-29)

### 2.66.3 (2024. 09. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* Unity 최소 지원 버전 변경: 2020.3.0f1

### 2.66.3 (2024. 09. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-Unity.zip)

#### 버그 수정
* (iOS) iOS 12 에서 결제 후 크래시가 발생하는 문제를 수정했습니다.

### 2.66.2 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.2/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 아래 필드가 iOS에서 deprecated 되었습니다. Android에서만 사용할 수 있습니다.
    * `GamebaseWebViewConfiguration.orientation`

### 2.66.1 (2024. 07. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.1/GamebaseSDK-Unity.zip)

#### 기능 추가

* (macOS) 개인정보 보호 정책이 대응되었습니다.

#### 기능 개선

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.1](../../release-notes-android.md#2661-2024-07-23)
* [Gamebase iOS SDK 2.66.0](../../release-notes-ios.md#2660-2024-07-23)

### 2.66.0 (2024. 07. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (Android) GPGS V2 인증이 추가되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.0](../../release-notes-android.md#2660-2024-07-10)
* [Gamebase iOS SDK 2.65.1](../../release-notes-ios.md#2651-2024-06-25)

#### Setting Tool (v2.9.0)

* GPGS V2 인증이 추가되었습니다. (Android에 한함)

### 2.65.1 (2024. 06. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 표시할 이미지 공지가 없는 경우 오류 대신 성공 콜백이 호출되도록 변경하였습니다.

#### 버그 수정
* 등록된 이미지 공지가 없을 경우 빈 공지 화면이 노출되는 문제를 수정하였습니다.
* (macOS) UnityEditor에서 GamebaseUtils.bundle 파일이 참조되지 않는 오류를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.65.1](../../release-notes-android.md#2651-2024-06-25)
* [Gamebase iOS SDK 2.65.1](../../release-notes-ios.md#2651-2024-06-25)

### 2.65.0 (2024. 06. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 이미지 공지 기능에 신규 타입이 추가되었습니다.
    * 롤링 팝업 타입이 추가되었습니다.
    * 기존의 이미지 공지는 팝업 타입으로 표기됩니다.
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.65.0](../../release-notes-android.md#2650-2024-06-11)
* [Gamebase iOS SDK 2.65.0](../../release-notes-ios.md#2650-2024-06-11)

### 2.64.0 (2024. 05. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.64.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.64.0](../../release-notes-android.md#2620-2024-05-28)
* [Gamebase iOS SDK 2.64.0](../../release-notes-ios.md#2620-2024-05-28)

### 2.63.0 (2024. 04. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.63.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (MacOS) WebView 신규 지원

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.63.0](../../release-notes-android.md#2620-2024-04-23)
* [Gamebase iOS SDK 2.63.0](../../release-notes-ios.md#2620-2024-04-23)
