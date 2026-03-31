## Game > Gamebase > 릴리스 노트 > iOS

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

### 2.52.0 (2023. 06. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.4.0)
    * Weibo iOS SDK (3.3.3)
* 아래 API가 deprecated되었습니다.
    * **+[TCGBGamebase countryCode]**
    * **+[TCGBGamebase countryCodeOfUSIM]**
    * **+[TCGBGamebase carrierCode]**
    * **+[TCGBGamebase carrierName]**
    * **+[TCGBUtil countryCode]**
    * **+[TCGBUtil usimCountryCode]**
    * **+[TCGBUtil carrierCode]**
    * **+[TCGBUtil carrierName]**
* SDK 내부 로직 개선

### 2.51.0 (2023. 05. 30.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.51.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.3.1)
    * PAYCO iOS SDK (1.5.8)
* SDK 내부 로직 개선

### 2.49.2 (2023. 04. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.2/GamebaseSDK-iOS.zip)

#### 버그 수정
* 누락되었던 이전 버전의 변경 사항을 적용하였습니다.
    * 로그인 후 외부 인증 IdP의 인증 정보를 얻지 못하는 버그 수정

### 2.49.1 (2023. 04. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* 로그인 후 외부 인증 IdP의 인증 정보를 얻지 못하는 버그를 수정하였습니다.

### 2.49.0 (2023. 04. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.5)

### 2.48.0 (2023. 03. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.48.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 14.1로 변경되었습니다. 
* iOS 최소 지원 버전이 11.0으로 변경되었습니다.
* armv7, armv7s, i386 아키텍처 지원을 중단하였습니다.
* 더 이상 bitcode를 지원하지 않습니다.
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.3.0)
    * PAYCO iOS SDK (1.5.6)
* DNS 장애를 대비한 Gamebase 서버 예비 도메인 적용

#### 버그 수정
* 특정 상황에서 킥아웃 이벤트가 동작하지 않는 버그를 수정하였습니다.
* 웹뷰 커스텀 스킴 콜백이 호출되지 않는 버그를 수정하였습니다.

### 2.47.0 (2023. 02. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.47.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.4)

### 2.46.0 (2023. 01. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.46.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.2)
    * Kakaogame iOS SDK (3.14.14)
* SDK 내부 로직 개선
