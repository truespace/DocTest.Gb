## Game > Gamebase > 릴리스 노트 > Android

### 1.14.5 (2018.12.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.5/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.14.5
    * deprecated 되었던 다음 API가 제거되었습니다.
        * (void)Gamebase.WebView.showWebBrowser(Activity, String)
        * (void)Gamebase.Network.addOnChangedListener(NetworkManager.OnChangedListener)
        * (void)Gamebase.Network.removeOnChangedListener(NetworkManager.OnChangedListener)
        * (void)Gamebase.Launching.addOnUpdatedListener(LaunchingOnUpdateListener)
        * (void)Gamebase.Launching.removeOnUpdatedListener(LaunchingOnUpdateListener)
    * 결제 모듈(gamebase-adapter-purchase-iap) 수정되었습니다.
        * IAP SDK를 1.5.2로 업데이트
        * Client에서는 사용되지 않는 IAP TEST Store 제거
        * 결제 재처리 로직(requestRetryTransaction)에서 데이터가 불완전할 때 호출이 실패하는 문제를 수정
        * 크래시를 방지하기 위해 모든 IAP SDK 호출부에 예외 처리

### 1.14.2 (2018.11.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.14.2
    * (Android)점검시, 데이터구조에서 점검 시작/종료 시간을 의미하는 epoch time의 타입을 기존 String에서 long으로 타입 변경 : 기존 Gamebase Unity와 연동 후 점검 호출 시 타입불일치로 콜백이 내려오지 않는 현상으로 인한 수정

#### 버그수정
* [SDK] 1.14.2
    * (Android)에뮬레이터 환경에서 스토어앱(PlayStore, OneStore 등)이 없는 상태에서 "앱 설치/업데이트"시 스토어 미체크로 인한 크래시 버그를 수정
    
### 1.14.1 (2018.10.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.1/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 1.14.0
    * (공통)Gamebase 웹뷰에서 파일첨부 기능 추가 : Android의 API 19, Kitcat 에서는 정상 동작하지 않습니다.
    
#### 기능 개선/변경
* [SDK] 1.14.0
    * (공통)이용 정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
    * Remove API : Webview, Network, Launching
        * (void)Gamebase.WebView.showWebBrowser(Activity, String)
        * (void)Gamebase.Network.addOnChangedListener(NetworkManager.OnChangedListener)
        * (void)Gamebase.Network.removeOnChangedListener(NetworkManager.OnChangedListener)
        * (void)Gamebase.Launching.addOnUpdatedListener(LaunchingOnUpdateListener)
        * (void)Gamebase.Launching.removeOnUpdatedListener(LaunchingOnUpdateListener)        
    * Deprecated  API 
        * (void)Gamebase.WebView.showWebView(Activity, String)
        * (void)Gamebase.WebView.showWebView(Activity, String, GamebaseWebViewConfiguration)
    
#### 버그수정
* [SDK] 1.14.1
    * (Android)Auth API 호출 후 콜백에서 다시 Auth API 중복 호출 시 정상 호출이 되지 않는 버그 수정
    
### 1.13.0 (2018.09.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.13.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.13.0
    * (공통)IAP SDK 최신버전 적용 (android:1.5.1, iOS:1.6.0)
    * (Android)Push API 호출 시, Gamebase 초기화/로그인 상태에 따라 호출 실패에 대한 에러 메시지를 보다 명확하게 개선
        * 초기화 전 호출 : NOT_INITIALIZED(1)
        * 초기화 이후 호출 시 Push 모듈이 없음 : NOT_SUPPORTED(10)
        * 초기화 성공 및 로그인 이전 호출 : NOT_LOGGED_IN(2)        
    
#### 버그수정
* [SDK] 1.13.0
    * (Android)NaverCafe SDK와의 충돌로 NAVER 로그인시 발생하던 오류 해결
        
### 1.12.2 (2018.08.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.12.2
    * (Android)WebSocket 타입아웃시 (API 호출 시간 경과), 크래시가 날 수 있는 버그에 대해 방어로직 처리
    
#### 버그수정
* [SDK] 1.12.2
    * (Android)auth-twitter-adapter 를 포함한 상태에서 TargetSdk 28로 빌드시 초기화 에러가 발생하는 문제 수정

### 1.12.1 (2018.08.09)

#### 기능 개선/변경
* [SDK] 1.12.1
    * (공통)IAP SDK 최신버전 적용 (1.5.0)
    * (공통)Gamebase 점검페이지에서 점검시간을 단말기 설정 국가시간에 맞추어 노출하도록 개선
    * (공통)점검페이지를 외부 페이지로 사용할 때 Console에 입력한 점검 정보를 사용할 수 있도록 기능 추가
    * (공통)IdP 매핑된 사용자의 Guest 매핑시도시 에러 발생(TCGB_ERROR_AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP)
    * (공통)인증 API 중복 호출 시 에러 발생(AUTH_ALREADY_IN_PROGRESS_ERROR)
    * (Android)TencentPush SDK 업데이트 (3.2.3)
    * (Android)Onestore v17(API v5) 지원 : Gamebase에서는 v16(스토어코드=TS)은 제공하지 않습니다.

### 1.11.1 (2018.07.05)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.11.1
    * (공통)Guest로그인 후 AddMapping 성공 시, loginForLastLoggedInPrivder를 하게되면, AddMapping 성공한 IdP계정을 사용하여 로그인하도록 변경
    
#### 버그수정
* [SDK] 1.11.1
    * (공통)점검 해제 후 후속 API 진행(login/push/purchase 등)이 되지 않던 버그 수정
    * (Android)Gamebase.addObserver()를 통해 ObserverMessage를 수신하였을 경우, ObserverMessage.data.code의 타입이 int가 아니라 String인 버그를 수정


### 1.11.0 (2018.06.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Twitter IdP 추가 : Android, iOS
* Line IdP 추가 : Android만 제공. iOS는 2018년 7월 제공 예정입니다.
    
#### 기능 개선/변경
* [SDK] 1.11.0
    * (공통)LocalizedString 일본어 번역 추가
    * (공통)인증 API 호출 시 초기화, 로그인을 하지 않은 경우 명확히 에러 코드를 구분하도록 내부 로직을 개선
    * (Android)'android.permission.READ_PHONE_STATE' 권한 제거
    * (Android)GamebaseConfiguration.Builder의 필수 설정값인 setAppId, setAppVersion을 생성자에서 입력할 수 있도록 변경
    * (Android)GamebaseConfiguration.Builder 의 setServerApiVerseion API를 제거
    * (Android)getAuthBanInfo() API, class AuthBanInfo 이름을 변경 : getBanInfo(), class BanInfo

### 1.9.0 (2018.05.03)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Transfer 기능 추가
    * guest 사용자가 매핑없이 새로운 기기로 이전할 수 있는 기능
    * (SDK공통)추가된 API 
        * Transfer Key 발급 API (IssueTransferKey)
        * 발급된 TransferKey를 사용하여 계정 이전을 요청하는 API (RequestTransfer)

#### 버그 수정
* [SDK] 1.9.0
    * (Android) Heartbeat 에서 잘못된 사용자로 판정되는 경우 이용 정지 팝업 창이 뜨지 않도록 수정(iOS 와 동일한 로직으로 수정)

### 1.8.1 (2018.04.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.1/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 1.8.1
    * (Android. iOS)registerPush를 호출 시 displayLanguageCode를 null로 전달하면 registerPush가 실패하는 버그 수정

### 1.8.0 (2018.04.05)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Kick out 기능 추가
    * 현재 게임 중인 전체 사용자의 연결을 끊는 기능(점검시 게임에서 전체 사용자의 연결을 끊고 싶을 때 사용할 수 있음)
    * (SDK 공통)kick out 이벤트를 받을 수 있는 API 추가
* Observer 기능 개발 및 API 추가
    * (SDK 공통) 점검 등 앱 상태/네트워크 상태/유저 상태(이용 정지) 변경사항에 대한 Listener를 Observer 등록을 통하여 일괄 처리할 수 있도록 API 추가

#### 기능 개선/변경
* [SDK] 1.8.0
    * (공통)Observer 기능 추가에 따라 다음 API Deprecated : LaunchingStatus Listener, Network Listener(기존 사용자는 계속 사용 가능)

### 1.7.0 (2018.02.22)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.7.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 1.7.0
    * NAVER IdP 인증 추가
    * Display Language 설정 추가: 단말기 언어와 별도로 게임내에서 게임유저의 노출 언어를 설정할 수 있도록 Display 언어를 추가하였습니다.
