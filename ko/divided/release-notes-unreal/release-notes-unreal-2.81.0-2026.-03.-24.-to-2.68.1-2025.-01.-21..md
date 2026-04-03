---
source: release-notes-unreal.md
section: "2.81.0 (2026. 03. 24.)-to-2.68.1 (2025. 01. 21.)"
order: 1
created_date: 2026-04-03
---

## Game > Gamebase > 릴리스 노트 > Unreal

### 2.81.0 (2026. 03. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.81.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.80.0](../../release-notes-android.md#2800-2026-02-13)
* [Gamebase iOS SDK 2.80.0](../../release-notes-ios.md#2800-2026-02-13)

### 2.80.0 (2026. 02. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 결제 요청 시 느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우, 신규로 추가된 **PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 GamebaseEventCategory.PURCHASE_UPDATED 이벤트 기능이 확장되었습니다.
    * 앱이 실행 중일 때 GamebaseEventHandler를 통해 Pending 결제(느린 결제, 부모 동의 등) 완료 이벤트를 제공 받을 수 있습니다.
* (iOS) Project Settings의 설정에 따라 Info.plist에 필요한 항목이 자동으로 추가되도록 개선되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > iOS Settings](../../unreal-started.md#ios-settings)
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.80.0](../../release-notes-android.md#2800-2026-02-13)
* [Gamebase iOS SDK 2.80.0](../../release-notes-ios.md#2800-2026-02-13)

### 2.79.0 (2026. 01. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.79.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.79.0](../../release-notes-android.md#2790-2026-01-27)
* [Gamebase iOS SDK 2.79.0](../../release-notes-ios.md#2790-2026-01-27)

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

* [Gamebase Android SDK 2.78.0](../../release-notes-android.md#2780-2025-12-23)
* [Gamebase iOS SDK 2.77.0](../../release-notes-ios.md#2770-2025-12-09)

### 2.76.0 (2025. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.76.0/GamebaseSDK-Unreal.zip)

####  기능 추가

* 가장 최근 게시된 게임 공지의 게시 시간을 제공하기 위해 `FGamebaseLaunchingInfo::FApp::FGameNotice::LatestNoticeTimeMillis` 필드를 추가했습니다.
* (Android) 미국 텍사스, 유타, 루이지애나 등 특정 관할권의 연령 확인 관련 법률 준수를 지원하기 위해 Google Play Age Signals 기반의 연령 확인 API가 추가되었습니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 참고사항 > Age Signals Support](../../unreal-etc.md#age-signals-support)
* (Windows) Steam 인증 시 Steamworks SDK가 로드되지 않은 경우 외부 브라우저를 통한 로그인을 지원합니다.

#### 기능 개선/변경

* `IGamebasePurchase::RequestItemListAtIAPConsole()` API가 deprecated되었습니다.
    * `IGamebasePurchase::RequestItemListPurchasable()` API를 사용하세요.
* 내부 로직을 개선했습니다.

#### 버그 수정
* (Windows) Google 결제 시 브라우저 로그인 상태에 따라 결제 완료 후 결과가 게임에 전달되지 않는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.76.0](../../release-notes-android.md#2760-2025-11-28)
* [Gamebase iOS SDK 2.75.0](../../release-notes-ios.md#2750-2025-09-23)

### 2.75.0 (2025. 11. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* (Windows) 이미지 공지, 게임 공지 출력 시 고정 크기에서 화면 해상도 비율로 출력되도록 수정되었습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* (Windows) 이미지 공지, 게임 공지 클릭 시 엔진 UI 포커스 문제로 클릭을 여러번 해야 반영되는 문제가 수정되었습니다.
* (Windows) 결제 완료 시 지표 전송에 SetGameUserData API 호출 정보가 포함되도록 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.75.1](../../release-notes-android.md#2751-2025-10-17)
* [Gamebase iOS SDK 2.75.0](../../release-notes-ios.md#2750-2025-09-23)

### 2.74.0 (2025. 08. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.74.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* (Windows) 계정 매핑 기능이 추가되었습니다.

#### 기능 개선/변경

* (Windows) 게임 공지 출력 시 엔진의 DPI에 영향을 받지 않도록 수정되었습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* (Windows) 계정 상태가 변경되었을 때 간헐적으로 크래시가 발생되는 로직이 수정되었습니다.
* (Windows) Twitter 로그인 시 간헐적으로 'Something went wrong' 오류가 발생하지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.73.1](../../release-notes-android.md#2731-2025-08-12)
* [Gamebase iOS SDK 2.73.1](../../release-notes-ios.md#2731-2025-08-12)

### 2.73.1 (2025. 07. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.1/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* (Android) Amazon Appstore가 서비스 중단되어 스토어 설정 및 푸시 설정 기능이 제거되었습니다.
* (Windows) 로그 전송 시 재시도 로직이 개선되었습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* 컴파일러 환경에 따라 빌드 오류가 발생하는 로직이 수정되었습니다.
* (Windows) 로그 전송 시 특정 문자가 포함된 데이터를 전송할 때 발생하던 오류가 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.73.0](../../release-notes-android.md#2730-2025-07-15)
* [Gamebase iOS SDK 2.73.0](../../release-notes-ios.md#2730-2025-07-15)

### 2.73.0 (2025. 07. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* (Windows) SDK를 사용하지 않는 IdP의 경우 외부 브라우저 로그인으로 진행되도록 변경되었습니다.
    * 외부 브라우저 로그인 진행 중 로그인을 취소할 수 있는 API가 추가되었습니다.
        * CancelLoginWithExternalBrowser
        * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
            * [Game > Gamebase > Unreal SDK 사용 가이드 > 인증 > Login > Login with IdP > Cancel Login with External Browser](../../unreal-authentication.md#cancel-login-with-external-browser)
* (Windows) Steam 로그인 시 Steamworks 초기화 실패 여부 메시지를 추가하여 원인을 파악하기 쉽도록 변경했습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* Epic Games 관련 기능을 사용하지 않을 때는 EOSSDK 모듈이 포함되지 않도록 수정되었습니다.
* (Windows) 콘솔에서 설정되지 않은 스토어를 사용할 때 크래시가 발생하지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.73.0](../../release-notes-android.md#2730-2025-07-15)
* [Gamebase iOS SDK 2.73.0](../../release-notes-ios.md#2730-2025-07-15)

### 2.72.0 (2025. 06. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* EpicGames 인증이 추가되었습니다.
* (Windows) 이용 정지 팝업에 고객 센터 링크를 추가하였습니다.

#### 기능 개선/변경

* 내부 로직을 개선했습니다.

#### 버그 수정

* (Windows) 외부 브라우저 로그인 시 응답 시 게임스레드로 전달하도록 수정되었습니다.
* (Windows) 성능이 느린 PC에서 외부 브라우저 로그인이 실패하는 문제가 수정되었습니다.
* (Windows) 디바이스 정보를 가져오는 과정이 정상적으로 이루어지지 않는 경우 크래시가 발생하는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.72.0](../../release-notes-android.md#2720-2025-06-24)
* [Gamebase iOS SDK 2.72.0](../../release-notes-ios.md#2720-2025-06-24)

### 2.71.1 (2025. 4. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.1/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* (Windows) 결제 API 오류 발생 시 디버깅을 돕기 위해 상세 오류 메시지를 보강했습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* (Windows) FGamebaseConfiguration 내 DisplayLanguageCode 적용 시 점검 언어 값을 잘못 가져오는 문제가 수정되었습니다.
* (Windows) 인증 과정 중 일부 실패 케이스에서 재인증이 불가능했던 문제가 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.71.1](../../release-notes-android.md#2711-2025-04-29)
* [Gamebase iOS SDK 2.71.0](../../release-notes-ios.md#2710-2025-04-15)

### 2.71.0 (2025. 4. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* '게임 공지' 신규 기능이 추가되었습니다.
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > UI > GameNotice](../../unreal-ui.md#gamenotice)
* (Windows) Google Play Games 지원을 위한 Google 결제 기능이 추가되었습니다.
    * [Windows 설정 툴](../../unreal-started.md#windows-settings) 내 Windows Store 설정에 `Google Play Store`가 추가되었습니다.

#### 기능 개선/변경

* (Windows) 시스템 설정에서 '지역 > 국가 또는 지역'을 바탕으로 CountryCode를 생성하도록 수정했습니다.
    * 변경 전에는 엔진에서 제공하는 `FInternationalization::Get().GetDefaultCulture()`를 통해 '지역 > 사용지역 언어' 정보를 가져왔습니다.

#### 버그 수정

* (Windows) WebView를 열고 프로그램 종료 시 크래시가 발생하지 않도록 수정했습니다.
* (Windows) 엔진에 포함된 Steamworks 모듈을 에디터에서 사용할 수 없으므로 Steam 인증 및 결제 기능을 에디터에서 사용할 수 없도록 수정했습니다.
* (Windows) 로그 전송 필터링이 정상적으로 동작하지 않는 문제가 수정되었습니다.
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.71.0](../../release-notes-android.md#2710-2025-04-15)
* [Gamebase iOS SDK 2.71.0](../../release-notes-ios.md#2710-2025-04-15)

### 2.70.0 (2025. 3. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* 로그인 시 IdP 서버로부터 오류가 발생했음을 나타내는 신규 오류 코드가 추가되었습니다.
    * AUTH_AUTHENTICATION_SERVER_ERROR(3012)
* WebView에 내비게이션 바 타이틀과 아이콘 틴트 컬러 설정 옵션을 추가했습니다.
    * `FGamebaseWebViewConfiguration::NavigationBarTitleColor`
    * `FGamebaseWebViewConfiguration::NavigationBarIconTintColor`
* (Android) 'GPGS 자동 로그인' 기능 연동 시 유저에게 GPGS 로그인을 앱 설치 후 한번만 물어보는 초기화 옵션을 추가했습니다.
    * `FGamebaseConfiguration::bEnableGPGSSignInCheck`
    * 기본 설정은 true로, 유저가 GPGS 로그인을 거부하더라도 Gamebase 초기화 때 GPGS 로그인 창을 다시 표시합니다.
    * false로 설정하면 앱 최초 실행 시에만 GPGS 로그인 창이 한번 표시됩니다.

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 버그 수정

* (Windows) 로그인 시 FGamebaseVariantMap로 추가 정보를 받는 경우 크래시가 발생하지 않도록 수정했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.70.0](../../release-notes-android.md#2700-2025-03-11)
* [Gamebase iOS SDK 2.70.0](../../release-notes-ios.md#2700-2025-03-11)

### 2.69.1 (2025. 3. 4.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.1/GamebaseSDK-Unreal.zip)

#### 기능 추가

* 론칭 정보에서 약관 정보를 확인할 수 있도록 추가했습니다.
    * FGamebaseLaunchingInfo::FApp::FTermsService

#### 기능 개선/변경

* API 호출 시 매개변수로 전달 받는 `UGamebaseJsonObject`를 `FGamebaseVariantMap(TMap<FName, FVariant>)`으로 변경했습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* (Windows) 게스트 로그인 시 UUID 발급 과정 오류로 인해 모두 동일한 값이 생성되는 문제를 수정했습니다.
* (Windows) Line IDP 로그인 시 region 설정이 동작하지 않는 문제를 수정했습니다.
* (Windows) 킥아웃 시 ServerPushAppKickOut 이벤트 발생과 팝업이 노출되지 않는 문제를 수정했습니다.
* (Windows) 심볼 생성 시 엔진의 Build Configuration이 Development가 아닌 경우 오류가 발생하는 문제를 수정했습니다.
* (Android) 환경에 따라 RegisterPush가 동작하지 않는 문제를 수정했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.69.0](../../release-notes-android.md#2690-2025-01-21)
* [Gamebase iOS SDK 2.69.0](../../release-notes-ios.md#2690-2025-01-21)

### 2.69.0 (2025. 2. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* `RequestLastLoggedInProvider` 비동기 API를 추가했습니다.
    * `GetLastLoggedInProvider` 동기 API가 타이밍상 정상적인 값을 반환하지 못할 때가 있습니다.
    * (Android) GPGS의 Auto Login 기능을 사용 시 GPGS 서버에서 데이터를 획득하는 시간이 필요하므로 Gamebase 초기화 직후 GetLastLoggedInProvider() 동기 API를 호출하면 정상적인 값을 획득할 수 없습니다.
        이때 RequestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;) 비동기 API는 정확한 값을 보장합니다.
        Auto Login을 사용하지 않는다면 GetLastLoggedInProvider() 동기 API를 사용해도 무방합니다.
* (Android) GPGS v2 인증 추가되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Android Settings](../../unreal-started.md#android-settings)
* (Android) `FGamebaseWebViewConfiguration::CutoutColor` 필드를 추가했습니다.
    * GamebaseWebView의 `FGamebaseWebViewConfiguration::bRenderOutSideSafeArea` 필드를 **false**로 설정한 경우, cutout 영역에 자동으로 padding 여백을 추가합니다.
    * CutoutColor 필드는 이렇게 추가된 padding 영역의 색을 설정할 수 있습니다.
    * RenderOutsideSafeArea 필드를 false로 설정했지만 CutoutColor 필드는 설정하지 않는 경우에는 웹 페이지 'body'의 'background-color' 값으로 자동으로 padding 영역의 색상을 결정합니다.

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 버그 수정

* 약관 조회 결과 API인 FGamebaseQueryTermsResult가 수정되었습니다.
    * TermsCountryType의 값이 설정되지 않는 문제를 수정했습니다.
    * bPushEnabled, bAdAgreement, bAdAgreementNight가 제거되었습니다.
* (Android) Windows 환경에서 빌드 시 포스트 빌드 프로세스에서 오류가 발생하지 않도록 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.69.0](../../release-notes-android.md#2690-2025-01-21)
* [Gamebase iOS SDK 2.69.0](../../release-notes-ios.md#2690-2025-01-21)

### 2.68.1 (2025. 01. 21.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.1/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.
* (Windows) WebView 플러그인을 옵션으로 선택할 수 있도록 변경되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Windows Settings > WebView 플러그인 안내](../../unreal-started.md#windows-settings)
* (Windows) 크래시 로그 전송 시 프로젝트 바이너리 경로에 심벌 파일을 압축한 파일이 생성되도록 추가되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > Logger > Crash Reporter](../../unreal-logger.md#crash-reporter)

#### 버그 수정
* (Windows) 내부 로그 전송 시 크래시가 발생할 수 있는 로직이 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.68.0](../../release-notes-android.md#2680-2024-11-26)
* [Gamebase iOS SDK 2.68.1](../../release-notes-ios.md#2681-2024-12-10)
