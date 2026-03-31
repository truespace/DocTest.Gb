## Game > Gamebase > 릴리스 노트 > iOS

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
        * [Game > Gamebase > iOS SDK 사용 가이드 > UI > GameNotice > Open GameNotice](./ios-ui/#open-gamenotice)

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
