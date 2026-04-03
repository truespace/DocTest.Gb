---
source: release-notes-ios.md
section: "2.80.0 (2026. 02. 13.)-to-2.53.0 (2023. 07. 25.)"
order: 1
created_date: 2026-04-03
---

## Game > Gamebase > 릴리스 노트 > iOS

### 2.80.0 (2026. 02. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 26.0으로 변경되었습니다.
* 결제 요청 시 Ask to Buy 등으로 결제가 지연되면 **TCGB_ERROR_PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 kTCGBPurchaseUpdated 이벤트 기능이 확장되었습니다.
    * App Store 프로모션 상품 구매 완료 또는 Ask to Buy 등으로 지연된 결제가 완료되었을 때 이벤트를 수신할 수 있습니다.
* 내부 로직 개선
* 아래 API가 deprecated되었습니다.
    * **+[TCGBPurchase setPromotionIAPHandler:]**

### 2.79.0 (2026. 01. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.79.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 내부 로직 개선
* 아래 API가 deprecated되었습니다.
    * **+[TCGBConfiguration setStoreCode:]**
    * **-[TCGBPurchase setStoreCode:]**
    * **TCGBPurchase.storeCode**

### 2.77.0 (2025. 12. 09.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.77.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 결제 관련 내부 로직 개선
* 아래 API가 deprecated되었습니다.
    * **+[TCGBPurchase requestItemListAtIAPConsoleWithCompletion:]**

### 2.75.0 (2025. 09. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Kakaogame iOS SDK (3.20.0)

### 2.73.1 (2025. 08. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Facebook iOS SDK (18.0.0)

#### 버그 수정
* Twitter 로그인 시 오류가 발생하는 버그를 수정했습니다.

### 2.73.0 (2025. 07. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 16.0으로 변경되었습니다. 

#### 버그 수정
* 로그인 후 updateTerms 호출 시, 동의한 약관 정보가 저장되지 않는 버그를 수정하였습니다.

### 2.72.1 (2025. 07. 01.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* iOS 14 특정 기기에서 GameCenter 로그인 시 크래시가 발생하는 버그를 수정하였습니다.

### 2.72.0 (2025. 06. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.17.2)
        * 내부 로직 개선
    * LINE iOS SDK (5.11.2)
        * bitcode 설정 제거
        * Xcode 16 컴파일러 경고 수정
* 내부 로직 개선

#### 버그 수정
* LINE IdP의 Region 추가 정보 대응이 되지 않아 매핑 및 loginForLastLoggedInProvider 로그인 관련 동작에서 발생하는 문제를 수정했습니다. 

### 2.71.0 (2025. 04. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* '게임 공지' 신규 기능이 추가되었습니다.
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다. 
        * [Game > Gamebase > iOS SDK 사용 가이드 > UI > GameNotice > Open GameNotice](../../ios-ui.md#open-gamenotice)

#### 기능 개선/변경
* storeCode를 nil로 설정하여 Gamebase 초기화를 호출했을 때 예외가 발생하는 대신 **TCGB_ERROR_INVALID_PARAMETER(3)** 에러를 리턴하도록 동작을 변경했습니다. 

### 2.70.0 (2025. 03. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 로그인 시 IdP 서버로부터 오류가 발생했음을 나타내는 신규 오류 코드가 추가되었습니다.
    * TCGB_ERROR_AUTH_AUTHENTICATION_SERVER_ERROR(3012)
* TCGBWebViewConfiguration에 내비게이션 바 타이틀 색상과 아이콘 색상을 설정할 수 있는 옵션을 추가했습니다.
    * **TCGBWebViewConfiguration.navigationBarTitleColor**
    * **TCGBWebViewConfiguration.navigationBarIconTintColor**

### 2.69.0 (2025. 01. 21.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * PAYCO iOS SDK (1.5.13)
        * iOS 18에서 정상적인 PAYCO 간편로그인 이용을 위한 openURL 관련 함수 수정
    * Hangame iOS SDK (1.17.1)
        * 내부 로직 개선
    * Weibo iOS SDK (3.4.0)
        * iOS 18 최적화
* completion block이 main thread에서 실행되도록 수정하였습니다.

#### 버그 수정
* SceneDelegate를 사용하는 앱에서 NAVER 로그인 취소 시 callback이 오지 않는 버그를 수정하였습니다.
* Gamebase 콘솔에 LINE old clientId를 설정하지 않았을 때 LINE 로그인에 실패하는 버그를 수정하였습니다.

### 2.68.1 (2024. 12. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.1/GamebaseSDK-iOS.zip)

#### 버그 수정  
* Swift 파일에서 Gamebase SDK를 import할 때 발생하는 오류를 수정하였습니다.

### 2.68.0 (2024. 11. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.5)
    * Hangame iOS SDK (1.17.0)
* Google 로그인 방식을 기존 OAuth 2.0에서 OpenID Connect로 변경하였습니다.
* 내부 로직 개선

### 2.67.0 (2024. 10. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Steam 인증이 추가되었습니다.
* Twitter 인증 방식을 OAuth 2.0으로 변경하여 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](../../oper-app.md#6-twitter)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * PAYCO iOS SDK (1.5.12)
        * PAYCO SDK가 Dynamic Framework로 변경되었습니다.
    * NAVER iOS SDK (4.2.3)
        * Xcode 16과 iOS 18 환경에서 정상 동작하도록 수정되었습니다.
    * Hangame iOS SDK (1.16.2)
        * Apple Silicon Mac에서 로그인이 실패하는 버그가 수정되었습니다.
* Gamebase SDK가 외부 SDK의 리소스를 포함하지 않도록 수정하였습니다.
* 내부 로직 개선

#### 버그 수정  
* 시스템 팝업 창 위에 Gamebase 론칭 팝업 창이 표시될 때 화면이 검게 변하는 버그를 수정하였습니다.

### 2.66.3 (2024. 09. 13.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.4)
        * iOS 18에서 앱이 포그라운드(foreground) 상태일 때 Notification이 중복 수신되지 않도록 수정되었습니다.

### 2.66.2 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.3)
        * 앱 스토어 심사에서 PrivacyInfo manifest 관련 경고 메일이 오지 않도록 수정되었습니다.
* 아래 필드가 deprecated되었습니다.
    * **TCGBWebViewConfiguration.orientationMask**
* 콘솔에 등록되지 않은 IdP로 로그인을 시도할 경우 TCGB_ERROR_AUTH_IDP_LOGIN_INVALID_IDP_INFO(3202) 오류가 발생하도록 수정했습니다.
* 롤링 이미지 공지의 웹뷰 내부에서 오류가 발생한 경우 기존의 성공 콜백 호출 대신 실패 콜백이 호출되도록 수정했습니다.
* 내부 로직 개선

### 2.66.0 (2024. 07. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Facebook iOS SDK (17.0.2)
    * Hangame iOS SDK (1.15.0)
* 앱 추적을 허용하지 않아도 Hangame-Facebook 로그인이 가능하도록 수정하였습니다.

### 2.65.1 (2024. 06. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 표시할 이미지 공지가 없는 경우 오류 대신 성공 콜백이 호출되도록 변경하였습니다.

#### 버그 수정  
* 등록된 이미지 공지가 없을 경우 빈 공지 화면이 노출되는 문제를 수정하였습니다.

### 2.65.0 (2024. 06. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 이미지 공지 기능에 신규 타입이 추가되었습니다.
    * `롤링 팝업` 타입이 추가되었습니다.
    * 기존의 이미지 공지는 `개별 팝업` 타입으로 표기됩니다.

#### 기능 개선/변경
* 앱 추적을 허용하지 않아도 Facebook 로그인이 가능하도록 수정하였습니다.
* 외부 SDK 업데이트
    * Facebook iOS SDK (17.0.1)
        * Facebook SDK가 Dynamic Framework로 변경되었습니다.
* Weibo iOS SDK의 PrivacyInfo.xcprivacy 파일이 수정되었습니다.
* 내부 로직 개선

### 2.64.0 (2024. 05. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.64.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * PAYCO iOS SDK (1.5.11)
    * Kakaogame iOS SDK (3.19.0)
* TCGBPushConfiguration.displayLanguageCode를 빈 문자열로 설정한 경우 Gamebase의 displayLanguageCode를 사용하도록 수정하였습니다.
* 내부 로직 개선

### 2.63.1 (2024. 05. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.63.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.13.1)
* 내부 로직 개선

### 2.63.0 (2024. 04. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.63.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Google iOS SDK (7.1.0)
    * Facebook iOS SDK (17.0.0)
    * Weibo iOS SDK (3.3.8)
* 내부 로직 개선

### 2.62.0 (2024. 03. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Gamebase와 Gamebase Adapter SDK에 Privacy manifest와 서명을 적용했습니다.
* Gamebase 초기화 후 반환되는 LaunchingInfo VO에서 테스트 단말기임을 알 수 있도록 필드가 추가되었습니다.
    * **launchingInfo.user.testDevice**

#### 기능 개선/변경
* Xcode 최소 지원 버전이 15.0으로 변경되었습니다. 
* iOS 최소 지원 버전이 12.0으로 변경되었습니다.
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.1)
    * LINE iOS SDK (5.11.0)
        * LINE 인증 최소 지원 버전이 13.0으로 변경되었습니다.
    * NAVER iOS SDK (4.2.1)
    * PAYCO iOS SDK (1.5.10)
    * Hangame iOS SDK (1.12.0)
* 내부 로직 개선

### 2.61.0 (2024. 02. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.61.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.0)
* SDK 내부 로직 개선

### 2.60.1 (2024. 02. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.60.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* 특정 IdP로 로그인해도 GameCenter 계정으로 변경되는 버그를 수정하였습니다.

### 2.60.0 (2024. 01. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.60.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* SDK 내부 로직 개선

### 2.59.1 (2023. 12. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.59.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* Hangame 로그인 시 오류가 발생하는 버그를 수정하였습니다.

### 2.59.0 (2023. 12. 19.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.59.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NAVER iOS SDK (4.2.0)
        * NAVER iOS SDK가 xcframework로 변경되었습니다.
* 약관 창이 태블릿 환경에서 고정 크기로 표시되도록 수정하였습니다.
* Launching Status Code가 INTERNAL_SERVER_ERROR(500)일 때 오류 팝업 창을 표시하도록 수정하였습니다.

#### 버그 수정
* LINE 로그인 중복 호출 시 크래시가 발생하는 버그를 수정하였습니다.

### 2.58.0 (2023. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.58.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * PAYCO iOS SDK (1.5.9)
        * PAYCO iOS SDK가 xcframework로 변경되었습니다.
    * Kakaogame iOS SDK (3.17.5)
* 최상위 ViewController 획득 로직 개선
* Gamebase 론칭 팝업 창이 완전히 종료된 후에 초기화 콜백이 호출되도록 수정하였습니다.

### 2.57.0 (2023. 10. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.57.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Privacy manifest 파일을 추가하였습니다.
* Gamebase GameCenter 로그인 스펙이 변경되었습니다.
    * GameCenter 로그인 취소 후 재요청 시 오류 팝업 창이 뜨며 TCGB_ERROR_AUTH_IDP_LOGIN_EXTERNAL_AUTHENTICATION_REQUIRED(3203) 오류가 발생하도록 수정하였습니다.

### 2.55.2 (2023. 09. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.55.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Weibo iOS SDK (3.3.4)

#### 버그 수정
* 앱을 처음 설치하고 Weibo 로그인을 시도할 때 콜백이 정상적으로 작동하지 않는 버그를 수정하였습니다.

### 2.55.0 (2023. 09. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.55.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 사용자가 푸시 권한을 거부해도 토큰을 등록할 수 있도록 TCGBPushConfiguration.alwaysAllowTokenRegistration 필드 추가

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.6.2)

### 2.54.0 (2023. 08. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.54.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Gamebase SDK를 xcframework로 변경
* 외부 SDK 업데이트
    * Facebook iOS SDK (14.1.0)
    * Google iOS SDK (7.0.0)
* SDK 내부 로직 개선

### 2.53.0 (2023. 07. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.53.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.6)
* 아래 필드가 deprecated되었습니다.
    * **TCGBWebViewConfiguration.backgroundOpacity**
* iPad에서 [TCGBUtil showActionSheetWithTitle:message:blocks:] API 호출 시 ActionSheet이 화면 중앙에 오도록 수정하였습니다.
* 프로젝트에 추가하지 않은 인증 Adapter를 사용하는 경우 **TCGB_ERROR_AUTH_NOT_SUPPORTED_PROVIDER(3002)** 오류를 반환하도록 수정하였습니다.

#### 버그 수정
* 특정 상황에서 이용 정지 팝업 창이 표시되지 않는 버그를 수정하였습니다.
* Apple Silicon Mac에서 웹뷰가 정상적으로 표시되지 않는 버그를 수정하였습니다.
