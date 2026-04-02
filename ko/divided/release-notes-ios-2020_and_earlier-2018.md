## Game > Gamebase > 릴리스 노트 > iOS

### 1.14.2 (2018.11.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Provider Profile 획득 메서드 호출 시, 반환하는 TCGBAuthProviderProfile 객체의 description 메서드의 JSON 문자열 구조 변경으로 인하여 Gamebase iOS SDK 1.14.0와 Unity Plugin 1.14.0 적용시 크래시가 발생될 수 있는 구조 수정

### 1.14.0 (2018.10.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Gamebase 웹뷰에서 파일첨부 기능 추가
    
#### 기능 개선/변경
* 이용 정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
* PAYCO iOS SDK 업데이트 (1.2.4)
* Remove API: Webview, Network, Launching
    * **[TCGBUtil showToastWithMessage:duration:]**
    * **[TCGBWebView showWebBrowserWithURL:viewController:]**
    * **[TCGBWebView showWebViewWithURL:viewController:configuration:]**
    * **[TCGBLaunching addObserverOnChangedStatusNotification:]**
    * **[TCGBLaunching removeObserverOnChangedStatusNotification:]**
    * **[TCGBLaunching addUpdateStatusNotification]**
    * **[TCGBLaunching removeUpdateStatusNotification]**
    * **[TCGBNetwork addObserverOnChangedNetworkStatusWithHandler:]**
    * **[TCGBNetwork removeObserverOnChangedNetworkStatusWithHandler:]**
* Deprecated API 
    * **[TCGBGamebase languageCode]**

### 1.13.0 (2018.09.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.13.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* App Store Promotion IAP를 지원하기 위한 API 추가

#### 기능 개선/변경

* IAP SDK 최신버전 적용 (iOS:1.6.0)
* authProviderProfileWithIDPCode api의 호출 결과의 구조가 1depth로 변경 (Android, Unity와 통일)
        
### 1.12.2 (2018.08.28) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Google Auth Adapter, Naver Auth Adapter의 Callback URL Scheme 설정 개선
    * 콘솔에 "url_scheme_ios_only" 값을 설정하지 않으면 Default URL Scheme을 설정 하도록 개선: Default URL Scheme을 사용하기 위해서는 XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.google 또는 tcgb.{Bundle ID}.naver 등록 필요
* Payco Auth Adapter 개선
    * URL Scheme 미설정으로 인해 의도치 않은 URL Scheme을 호출하던 문제 수정: 설정 방법이 변경되어 업데이트를 위해서는 반드시 URL Scheme 설정 필요 (XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.payco를 등록)

### 1.12.1 (2018.08.09) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* IAP SDK 최신버전 적용 (1.5.0)
* Gamebase 점검페이지에서 점검시간을 단말기 설정 국가시간에 맞추어 노출하도록 개선
* 점검페이지를 외부 페이지로 사용할 때 Console에 입력한 점검 정보를 사용할 수 있도록 기능 추가
* IdP 매핑된 사용자의 Guest 매핑시도시 에러 발생(TCGB_ERROR_AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP)
* 인증 API 중복 호출 시 에러 발생(AUTH_ALREADY_IN_PROGRESS_ERROR)
* 오류 코드 추가: Gamecenter 로그인 거부(TCGB_ERROR_IOS_GAMECENTER_DENIED)
    
#### 버그수정

* NAVER 로그인 시 프로필 정보 조회 실패로 인해 로그인이 불가능한 버그 수정: 프로필 정보 조회 실패하더라도 로그인은 성공하도록 변경    
    
### 1.12.0 (2018.07.24) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Gamebase 초기화 시 Debug Log에 사용중인 Adapter들의 버전 정보, 앱의 빌드 정보를 출력하는 기능이 추가 
* CocoaPods을 통해 배포 되는 Naver Auth Adapter에서 포함하고 있던 Naver ID Login SDK의 바이너리가 제거 되고 의존성 설정 방식으로 변경

### 1.11.1 (2018.07.05) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.1/GamebaseSDK-iOS.zip)

#### 기능 추가

* LINE IdP 추가

#### 기능 개선/변경

* Guest로그인 후 AddMapping 성공 시, loginForLastLoggedInPrivder를 하게되면, AddMapping 성공한 IdP계정을 사용하여 로그인하도록 변경
    
#### 버그수정

* 점검 해제 후 후속 API 진행(login/push/purchase 등)이 되지 않던 버그 수정

### 1.11.0 (2018.06.26) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Google IdP 추가
* Twitter IdP 추가
    
#### 기능 개선/변경
* LocalizedString 일본어 번역 추가
* 인증 API 호출 시 초기화, 로그인을 하지 않은 경우 명확히 에러 코드를 구분하도록 내부 로직을 개선
* Naver ID Login SDK 업데이트: iOS(4.0.10)
    
### 1.9.1 (2018.05.29) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.1/GamebaseSDK-iOS.zip)

#### 버그수정

* Gamebase 웹뷰 NavigationBar 영역에 타이틀, 뒤로 가기, 닫기 버튼이 나타나지 않는 현상을 수정
    
### 1.9.0 (2018.05.03) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Transfer 기능 추가
    * guest 사용자가 매핑없이 새로운 기기로 이전할 수 있는 기능
    * 추가된 API 
        * Transfer Key 발급 API (IssueTransferKey)
        * 발급된 TransferKey를 사용하여 계정 이전을 요청하는 API (RequestTransfer)

#### 버그 수정

* NAVER 계정을 이용한 로그인 중 App to Web 로그인 시도 시, 서버로부터 받아온 Scheme의 형식이 변경되어, 로그인이 되지 않는 현상 수정
* Adapter로부터 UnderlyingError 객체를 받아서 유저에게 전달되는 에러객체를 생성하는 로직에서 메시지 및 Underlying Error의 설정이 되지 않는 버그 수정

### 1.8.1 (2018.04.12) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.1/GamebaseSDK-iOS.zip)

#### 버그 수정

* registerPush를 호출 시 displayLanguageCode를 null로 전달하면 registerPush가 실패하는 버그 수정

### 1.8.0 (2018.04.05) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Kick out 기능 추가
    * 현재 게임 중인 전체 사용자의 연결을 끊는 기능(점검시 게임에서 전체 사용자의 연결을 끊고 싶을 때 사용할 수 있음)
    * kick out 이벤트를 받을 수 있는 API 추가
* 점검 웹페이지를 사용자가 Console에서 입력한 HTML 페이지로 사용할 수 있도록 기능을 개선
    * 이전에는 Gamebase에서 제공하는 웹페이지나 외부 웹페이지 연결만 가능했음
    * 웹서버가 없는 경우에도 점검페이지를 사용자가 원하는 형태로 만들 수 있음
* Observer 기능 개발 및 API 추가
    * 점검 등 앱 상태/네트워크 상태/유저 상태(이용 정지) 변경사항에 대한 Listener를 Observer 등록을 통하여 일괄 처리할 수 있도록 API 추가

#### 기능 개선/변경

* Observer 기능 추가에 따라 다음 API Deprecated: LaunchingStatus Listener, Network Listener(기존 사용자는 계속 사용 가능)
* PAYCO 간편로그인 3rd SDK v1.2.2 적용: 로그인 성공 시 토큰 만료 정보(expires_in) 제공, iPhoneX 로그인 UI 개선
* iPhoneX 지원을 위하여, 웹뷰 사용 인터페이스 수정

#### 버그 수정
* 국가코드(contry code)가 10자 이상인 경우 동접 데이터가 저장되지 않는 현상 수정

### 1.7.0 (2018.02.22) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.7.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* NAVER IdP 인증 추가
* Display Language 설정 추가: 단말기 언어와 별도로 게임내에서 게임유저의 노출 언어를 설정할 수 있도록 Display 언어를 추가하였습니다.

### 1.6.0 (2018.01.25) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.6.0/GamebaseSDK-iOS.zip)

#### 버그 수정

* 웹뷰 호출 시, 크래시가 일어날 수 있는 부분에 대한 방어로직 처리
