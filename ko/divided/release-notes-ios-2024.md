## Game > Gamebase > 릴리스 노트 > iOS

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
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](./oper-app/#6-twitter)

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
