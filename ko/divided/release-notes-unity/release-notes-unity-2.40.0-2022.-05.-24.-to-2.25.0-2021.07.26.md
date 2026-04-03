---
source: release-notes-unity.md
section: "2.40.0 (2022. 05. 24.)-to-2.25.0 (2021.07.26)"
order: 3
created_date: 2026-04-03
---

### 2.40.0 (2022. 05. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.40.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.5)
* (Standalone) 아래 약관 API를 지원하도록 변경되었습니다.
    * Gamebase.Terms.QueryTerms
    * Gamebase.Terms.UpdateTerms

#### 기능 개선/변경
* 한글이 유니코드로 표시되는 현상이 개선되었습니다.
* (iOS) bitcode 지원하도록 수정되었습니다.

#### 버그 수정
* (Android) OpenContact API 호출 시 Configuration.additionalParameters가 적용되지 않는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.40.0](../../release-notes-android.md#2400-2022-05-24)
* [Gamebase iOS SDK 2.40.0](../../release-notes-ios.md#2400-2022-05-24)

### 2.39.0 (2022. 05. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.39.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.4)

#### 버그 수정
* 초기화 전에 GetLaunchingInformations() API를 호출 시 JsonException이 발생하지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.39.0](../../release-notes-android.md#2390-2022-05-10)
* [Gamebase iOS SDK 2.39.0](../../release-notes-ios.md#2390-2022-05-10)

### 2.38.0 (2022. 05. 03.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.38.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.3)

#### 기능 개선/변경
* Display Language의 중국어 번체(zh-TW) 언어셋에서 어색한 문장이 수정되었습니다.

#### 버그 수정
* (Android) API Level 24 미만에서 특정 API 호출 시 오류가 발생하지 않도록 수정되었습니다.
    * Gamebase.Purchase.RequestActivatedPurchases()
    * Gamebase.Purchase.RequestItemListOfNotConsumed()

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.38.0](../../release-notes-android.md#2380-2022-05-03)
* [Gamebase iOS SDK 2.38.0](../../release-notes-ios.md#2380-2022-05-03)

### 2.37.0 (2022. 04. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.37.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 고객 센터 URL 뒤에 파라미터를 추가할 수 있도록 다음 필드가 추가되었습니다.
    * GamebaseRequest.Contact.Configuration.additionalParameters

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.37.0](../../release-notes-android.md#2370-2022-04-26)
* [Gamebase iOS SDK 2.37.0](../../release-notes-ios.md#2370-2022-04-26)

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

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 외부 SDK 업데이트: TOAST Unity SDK(0.25.1)
* 약관이 표시되었는지를 알 수 있는 API가 추가되었습니다.
    * Gamebase.Terms.IsShowingTermsView()
* 웹뷰에서 내비게이션 바를 숨길 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Webview.GamebaseWebViewConfiguration.isNavigationBarVisible
* (Android) 웹뷰에서 폰트 사이즈를 고정할 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Webview.GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 약관 창에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Terms.GamebaseTermsConfiguration.enableFixedFontSize
* Setting Tool
    * (Android) Amazon 스토어가 추가되었습니다.
    * (Android) Huawei 스토어가 추가되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.35.0](../../release-notes-android.md#2350-2022-03-29)
* [Gamebase iOS SDK 2.35.0](../../release-notes-ios.md#2350-2022-03-29)

### 2.34.1 (2022. 03. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.1/GamebaseSDK-Unity.zip)

#### 기능 추가
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * Gamebase.Push.QueryNotificationAllowed()

#### 버그 수정
* iOS에서 GamebaseWebViewConfiguration의 isBackButtonVisible 설정이 적용되지 않는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.34.0](../../release-notes-android.md#2340-2022-02-22)
* [Gamebase iOS SDK 2.34.1](../../release-notes-ios.md#2341-2022-03-15)

### 2.34.0 (2022. 02. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 공통 약관 API 호출 후 약관 UI가 표시되었는지 여부를 알 수 있는 VO 클래스가 추가되었습니다.
    * **GamebaseResponse.Terms.ShowTermsViewResult**

#### 기능 개선/변경
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드가 deprecated되었습니다.
    * **GamebaseConfiguration.enableKickoutPopup**
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.34.0](../../release-notes-android.md#2340-2022-02-22)
* [Gamebase iOS SDK 2.34.0](../../release-notes-ios.md#2340-2022-02-22)

### 2.33.0 (2022.01.25)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.33.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 공통 약관 창의 설정을 변경할 수 있는 신규 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > UI > Terms > showTermsView](../../unity-ui.md#showtermsview)

#### 기능 개선/변경
* 오류 코드 추가 및 변경
    * GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode.SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.33.0](../../release-notes-android.md#2330-20220125)
* [Gamebase iOS SDK 2.33.0](../../release-notes-ios.md#2330-20220125)

### 2.32.0 (2021.12.28)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* GamebaseEventHandler의 GamebaseEventCategory에 **GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED** 타입이 추가되었습니다.
    * 이 이벤트의 활용 방법은 다음 문서를 참고하시기 바랍니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../../unity-etc.md#server-push)
* Gamebase Access Token이 만료되어 로그인이 필요할 때 동작하는 **GamebaseEventCategory.LOGGED_OUT** GamebaseEventHandler category가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../../unity-etc.md#logged-out)
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.32.0](../../release-notes-android.md#2320-20211228)
* [Gamebase iOS SDK 2.32.0](../../release-notes-ios.md#2320-20211228)

### 2.31.0 (2021.12.14)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.31.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.0)
* Standalone 점검 팝업 창에서 점검 시간 표시 여부를 동적으로 설정할 수 있도록 변경되었습니다.
* Setting Tool
    * PAYCO IDP가 추가되었습니다.
    * 기존 SettingTool을 완전히 삭제한 후 재설치해야 합니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.31.0](../../release-notes-android.md#2310-20211214)
* [Gamebase iOS SDK 2.31.0](../../release-notes-ios.md#2310-20211214)

### 2.30.0 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Mapping > Add Mapping Forcibly](../../unity-authentication.md#add-mapping-forcibly)
* Gamebase.AddMapping() 호출 후 AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302) 에러가 발생했을 때, 해당 계정으로 로그인을 할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Mapping > Change Login with ForcingMappingTicket](../../unity-authentication.md#change-login-with-forcingmappingticket)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.30.0](../../release-notes-android.md#2300-20211123)
* [Gamebase iOS SDK 2.30.0](../../release-notes-ios.md#2300-20211123)

### 2.29.0 (2021.11.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.29.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Unity SDK(0.23.5)
* Setting Tool
    * 2.0.0이 새로 배포되었습니다.
    * 기존 Setting Tool을 완전히 삭제한 후 재설치해야 합니다.
    * 변경된 내용 및 사용 방법은 아래 가이드를 확인하십시오.
        * [Game > Gamebase > Unity SDK 사용 가이드 > 시작하기 > Specification of Setting Tool](../../unity-started.md#specification-of-setting-tool)

#### 버그 수정
* GamebaseDisplayLanguageCode 핀란드어 오타 수정
    * Finish → Finnish

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.29.0](../../release-notes-android.md#2290-20211109)
* [Gamebase iOS SDK 2.29.0](../../release-notes-ios.md#2290-2021109)

### 2.28.1 (2021.10.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.28.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* (Android) DisplayLanguage 설정을 하지 않을 경우 잘못된 값으로 설정되는 문제가 수정되었습니다.
* (Standalone) 이전 프레임에서 시간이 오래 걸릴 경우 발생하는 Timeout 오류가 수정되었습니다.

### 2.28.0 (2021.09.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.28.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* Kakaogame 인증 추가
* '결제 어뷰징 자동 해제' 기능이 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > GraceBan](../../unity-authentication.md#graceban)
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용 정지가 됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 AuthToken.member.graceBanInfo API 값을 확인하고, null이 아닌 유효한 GraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.28.0](../../release-notes-android.md#2280-20210928)
* [Gamebase iOS SDK 2.28.0](../../release-notes-ios.md#2280-20210928)

### 2.27.1 (2021.09.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* Display Language 기능이 개선되었습니다.
    * 기본 언어코드가 **en** 이었으나, Gamebase 콘솔에서 설정한 기본언어가 반영되도록 개선하였습니다.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > App > 언어 설정](../../oper-app.md#language-settings)

#### 버그 수정
* '등록되지 않은 게임 버전' 에러 팝업 창이 영어로만 표시되는 버그를 수정하였습니다.
* 점검 팝업 창에 중국어가 표시되지 않는 버그를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.27.1](../../release-notes-android.md#2271-20210914)
* [Gamebase iOS SDK 2.27.1](../../release-notes-ios.md#2271-20210914)

### 2.27.0 (2021.08.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Unity SDK(0.23.2)
* ONE Store V16 스토어 추가

#### 버그 수정
* Unity SDK 2.25.0에서 잘못 추가된 파일 제거
    * 경로: Assets/Gamebase/Toast/IAP/Plugins

### 2.26.0 (2021.08.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.26.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* Display Language 기능이 개선되었습니다.
    * Display Language 언어셋에 중국어 간체(zh-CN), 중국어 번체(zh-TW), 태국어(th)가 추가되었습니다.
* ShowTermsView API 호출 후 생성할 수 있는 PushConfiguration 객체의 생성 기준이 다음과 같이 변경되었습니다.
    * 변경 전
        * 약관 항목 중에 **Push 수신** 항목이 존재하는 경우에만 null이 아닌 유효한 PushConfiguration이 반환되었습니다.
        * 유저가 주간, 야간 홍보성 Push 수신에 모두 거부한 경우 PushConfiguration.pushEnabled는 false로 생성되었습니다.
    * 변경 후
        * 약관 UI가 표시되었다면 항상 null이 아닌 유효한 PushConfiguration이 반환됩니다.
        * ShowTermsView가 반환하는 PushConfiguration 객체의 pushEnabled 값은 항상 true입니다.
    * 변경되지 않고 동일한 점
        * 이미 약관에 동의하여 약관 UI가 표시되지 않았다면 PushConfiguration은 null로 반환됩니다.

#### 버그 수정
* Push 언어 설정은 별다른 보조 처리가 없이 단말기의 언어코드를 그대로 적용되어, Push 콘솔에서 전송한 메시지의 언어코드가 일치하지 않는 문제를 수정하였습니다.

### 2.25.0 (2021.07.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.25.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 월 결제 한도 기능 추가
    * 월 결제 한도를 넘는 경우 **PURCHASE_LIMIT_EXCEEDED(4007)** 에러가 발생합니다.

#### 기능 개선/변경
* Push 항목이 존재하는 약관에서 PushConfiguration 객체 보장
    * 약관 UI에서 Push 수신 동의를 하지 않을 경우 Gamebase.Terms.ShowTermsView API 호출 결과로 생성되는 PushConfiguration이 null이었으나, 약관에 Push 항목이 존재한다면 PushConfiguration 객체가 항상 반환되도록 변경되었습니다.
    * Push 수신 거부 시 PushConfiguration 객체는 (푸시 동의 여부 = false, 광고성 푸시 동의 여부 = false, 야간 광고성 푸시 동의 여부 = false)로 생성됩니다.
    * 약관에 Push 항목이 존재하지 않는다면 PushConfiguration 객체는 null입니다.
* Unity 최소 지원 버전 변경: 2018.4.0f1
* 외부 SDK 업데이트: TOAST Unity SDK(0.23.0)
