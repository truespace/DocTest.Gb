---
source: release-notes.md
section: "2019. 05. 28.-to-2018. 08. 09."
order: 3
created_date: 2026-04-03
---

### 2019. 05. 28.

#### 기능 추가
* HANGAME mix 일본결제 추가
    * [SDK] 2.4.0
    	* (Unity)Standalone 일본 외부결제 추가
    	* (Unity)Standalone 일본 HANGAME 인증 추가
    * [Console] 
    	* 구매 > 스토어: 'HANGAME mix(JAPAN)' Store 추가
    	* 앱 > 클라이언트: Windows 클라이언트 등록 시 스토어 설정 항목 추가
    	* 앱 > 설치URL: Windo 설치 URL 추가 시 스토어 설정 항목 추가

#### 기능 개선/변경
* [SDK] 2.4.0
	* (공통) 지표관련 Class 변경
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [Android](http://docs.toast.com/ko/Game/Gamebase/ko/aos-etc/#game-user-data-settings) / [iOS](http://docs.toast.com/ko/Game/Gamebase/ko/ios-etc/#game-user-data-settings) / [Unity](http://docs.toast.com/ko/Game/Gamebase/ko/unity-etc/#game-user-data-settings) / [JavaScript](http://docs.toast.com/ko/Game/Gamebase/ko/js-etc/#game-user-data-settings)]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [Android](http://docs.toast.com/ko/Game/Gamebase/ko/aos-etc/#level-up-trace) / [iOS](http://docs.toast.com/ko/Game/Gamebase/ko/ios-etc/#level-up-trace) / [Unity](http://docs.toast.com/ko/Game/Gamebase/ko/unity-etc/#level-up-trace) / [JavaScript](http://docs.toast.com/ko/Game/Gamebase/ko/js-etc/#level-up-trace)]
    * (Android)Naver SDK 버전 업데이트(v4.2.5): Naver SDK 버그 수정(Naver 로그인 도중에 앱 아이콘을 통해 앱을 재시작할 경우, Activity가 강제종료 되는 이슈로 인해 인증 프로세스가 중단되는 이슈가 해결)
    * (Unity)StandaloneWebview가 32bit 빌드를 지원 (SDK 용량 53.6MB에서 99.2MB로 증가)
* [Server]
    * LTV 쿼리 수정 및 failover 로직 수정
* [Console]
    * LTV Grid ComplexColumns 지원 및 엑셀 다운로드 지원

### 2019. 05. 16.

#### 기능 추가
* [Console]
	* 단말기 이전 기능 추가(신규 메뉴)
		* 앱 > 기기 이전(Transfer account): 기기이전 기능 사용을 위한 설정값 저장
		* 회원 > 기기 이전: 발급된 키의 상태 및 이력 조회

#### 기능 개선/변경
* [Console]
	* 앱: AppleGameCenter, China IdP에 '토큰재검증' 옵션 Off
		* 해당 IdP에서는 실제 외부IdP 체크하지않고 내부토큰만 체크하므로 의미없는 옵션이므로 제거
	* 회원: 매핑 추가 가능한 조건 변경
		* 기존:Guest계정
		* 변경:Guest계정, Missing 계정

#### 버그수정
* [SDK] 2.3.1
	* (Android)2.3.0버전에서 Twitter 로그인 되지 않던 문제 수정
* [Console]
	* 회원: 구매 이력에서 영수증 검증이 되지 않던 문제 수정
	* Kickout: 조회 요청시 인증체크 추가하여 비정상 동작하던 이슈 수정
	
### 2019. 04. 23.

```
Gamebase를 사용하면 50여개의 중국스토어 연동이 가능합니다.
중국출시에 관심 있으신 경우에는 고객센터로 연락주세요.
```

#### 기능 추가
* [SDK] 2.3.0
	* (Android/Unity)중국스토어 인증/결제 추가

#### 기능 개선/변경
* [SDK] 2.3.0
	* (공통)Launching Status Code 추가: "심사중(204)", "테스트중(203)"
	* (Android)최근 로그인한 Provider로 로그인 및 웹소켓 응답 실패를 받았을 경우(Timeout, network disable 등) AuthToken을 삭제 처리하지 않도록 수정
	* (Android)IdP로그인 시 AuthAdapter 내부에서 발생하는 MemoryLeak을 수정

### 2019. 04. 11.

#### 기능 개선/변경
* [SDK] 2.2.2
	* (Unity)SDK 로그 개선
* [Console]
	* Analytics 메뉴 다국어 적용
	* 보안검수 관련 취약점 패치

#### 버그수정
* [SDK] 2.2.2
	* (Android)Gamebase 초기화 이전 TransferAccount API 호출시, 콜백이 오지 않는 이슈를 수정
	* (iOS)showBlockingPopup을 NO로 설정 할 경우 Gamebase 초기화 콜백이 호출되지 않는 이슈를 수정
	* (Unity)AddMappingForcibly API를 호출하면 크래시가 발생하여 수정

### 2019. 04. 02.

#### 버그수정
* [SDK] 2.2.1
	* (Unity) Unity Editor에서 Android 플랫폼을 선택하고 플레이를 하면 initialize시 서버에서 에러가 발생하는 이슈 수정

### 2019. 03. 26.

#### 기능 추가
* TransferAccount 기능 추가: guest 사용자가 매핑없이 최대 2개의 키를 이용하여 새로운 기기로 이전할 수 있는 기능
    - (SDK공통)추가된 API 
		* TransferAccountInfo 발급 API (issueTransferAccount)
		* 발급된 TransferAccountInfo를 사용하여 계정 이전을 요청하는 API (transferAccountWithIdPLogin)
		* 발급된 TransferAccountInfo를 확인하는 API (queryTransferAccount)
		* 이미 발급된 TransferAccountInfo 갱신하는 API (renewTransferAccount)		
	- (Server API)
		* 발급된 TransferAccount의 ID/PW 검증하는 서버 API (validateTransferAccount)
    - (console)회원메뉴의 매핑이력조회 탭에서 Transfer 이력 확인이 가능
* 강제매핑 기능 추가: 이미 다른 계정에 연동 되어있는 IdP계정을 매핑할 수 있는 기능
	- (SDK공통)추가된 API 
		* 강제매핑하는 API (addMappingForcibly)

#### 기능 개선/변경
* [SDK] 2.2.0
	* (Android)IAP SDK 버전을 최신버전인 v1.5.3 버전으로 업데이트
	* (iOS)LINE SDK의 App 로그인 기능이 비활성화
		* LINE SDK v4의 버그로 인해 iOS 12에서 앱 로그인이 실패 하는 이슈가 있어 Gamebase Line Adatper에서 Web 로그인만 지원하도록 변경
	* (Unity)GamebaseMainActivity의 Package Name이 변경
		* com.toast.gamebase.activity.GamebaseMainActivity -> com.toast.android.gamebase.activity.GamebaseMainActivity

### 2019. 02. 26.

#### 기능 개선/변경
* [SDK] 2.1.0
	* (공통)TransferKey API 삭제
		* issueTransferKey : TransferKey 발급
		* requestTransfer : TransferKey 검증
		
#### 버그수정
* [SDK] 2.1.0
	* (Android)Gamebase 초기화 이전, onActivityResult() 가 호출되면서 이상 동작하던 버그 수정
	* (iOS)Gamecenter를 Gamebase가 아닌 다른 로직에의해 로그인 한 후, Gamebase를 통하여 Gamecenter로그인을 시도할 때, 반응이 없는 버그 수정

### 2019. 01. 29.

```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가
* Console
	* Analytics : Gamebase 2.0 지표 신규 오픈
	* 앱 : 클라이언트의 디버그 로그를 실시간으로 변경할 수 있는 기능 추가
* [SDK] 2.0.0
	* (공통)Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK내부에서 자동 전송)
		* setGameUserData : 게임 로그인 이후 유저 레벨 정보 전송
		* traceLevelUpData : 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출
    * (JavaScript)SDK 신규 배포

#### 기능 개선/변경
* [SDK] 2.0.0
	* (Android)Push SDK 업데이트(android:1.7.0)
	* (Android)Adapter API 변경
		* Launching 정보 전달
		* logout, withdraw API에 Callback 추가
	* (iOS)IAP SDK 업데이트
		* 결제 실패 시 간헐적으로 크래시가 발생하던 현상 수정

#### 버그수정
* [SDK] 2.0.0
	* (iOS)iOS 12 이상의 시뮬레이터에서 debugMode On 상태로 Gamebase 초기화 시 크래시가 발생하던 현상 수정

### 2018. 12. 27.

#### 기능 추가
* Console
	* Push - 반복발송 기능 추가

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
* Console
	* 인증이 풀렸을 때 Rest API 요청에도 로그인페이지로 이동하도록 수정
	* IAP Transaction 조회 필터 추가

### 2018. 11. 15.

#### 기능 추가
* Console
	* 중국어 적용
	* 회원 : 구매이력에 App Store 영수증 검증 기능 추가	

#### 기능 개선/변경
* Console
	* 달력 다국어 지원 추가
* [SDK] 1.14.2
	* (Android)점검시, 데이터구조에서 점검 시작/종료 시간을 의미하는 epoch time의 타입을 기존 String에서 long으로 타입 변경 : 기존 Gamebase Unity와 연동 후 점검 호출 시 타입불일치로 콜백이 내려오지 않는 현상으로 인한 수정
	* (iOS)Provider Profile 획득 메서드 호출 시, 반환하는 TCGBAuthProviderProfile 객체의 description 메서드의 JSON 문자열 구조 변경으로 인하여 Gamebase iOS SDK 1.14.0와 Unity Plugin 1.14.0 적용시 crash가 발생될 수 있는 구조 수정

#### 버그수정
* Console
	* 푸시 : 특정대상 발송 이후 등록된 푸시건을 복사하여 등록할 때 등록 실패하던 문제 수정	
* [SDK] 1.14.2
	* (Android)에뮬레이터 환경에서 스토어앱(PlayStore, OneStore 등)이 없는 상태에서 "앱 설치/업데이트"시 스토어 미체크로 인한 crash 버그를 수정
	* (Unity)ShowWebView API 호출시 파라메타에 Callback을 넣지 않으면 crash가 발생되는 부분 수정
	* (Unity)iOS SDK의 Deleted API를 호출하는 코드가 있어 컴파일시 오류가 발생 되는 버그 수정
	
### 2018. 10. 23.

#### 기능 추가
* Console
	* IAP : 결제 정보메뉴에서 App Store 영수증 검증 기능 추가
* [SDK] 1.14.0
	* (공통)Gamebase Webview에서 파일첨부 기능 추가 : Android의 API 19, Kitcat 에서는 정상 동작하지 않습니다.
	
#### 기능 개선/변경
* Console
	* IAP : 결제 정보메뉴에서 결제내역 다운로드 검색 조건 개선(1일 ->30일)
* [SDK] 1.14.0
	* (공통)이용정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
	* (iOS)Payco SDK의 버전이 1.2.4로 업데이트 
	* (Unity)GamebaseSDKSetting 오브젝트가 있는 씬으로 돌아갈 경우 오브젝트가 중복으로 생기지 않도록 개선
	* Remove API : Webview, Network, Launching
		* (Android)5개
			- (void)Gamebase.WebView.showWebBrowser(Activity, String)
			- (void)Gamebase.Network.addOnChangedListener(NetworkManager.OnChangedListener)
			- (void)Gamebase.Network.removeOnChangedListener(NetworkManager.OnChangedListener)
			- (void)Gamebase.Launching.addOnUpdatedListener(LaunchingOnUpdateListener)
			- (void)Gamebase.Launching.removeOnUpdatedListener(LaunchingOnUpdateListener)
		* (iOS)9개
			- [TCGBUtil showToastWithMessage:duration:]
			- [TCGBWebView showWebBrowserWithURL:viewController:]
			- [TCGBWebView showWebViewWithURL:viewController:configuration:]
			- [TCGBLaunching addObserverOnChangedStatusNotification:]
			- [TCGBLaunching removeObserverOnChangedStatusNotification:]
			- [TCGBLaunching addUpdateStatusNotification]
			- [TCGBLaunching removeUpdateStatusNotification]
			- [TCGBNetwork addObserverOnChangedNetworkStatusWithHandler:]
			- [TCGBNetwork removeObserverOnChangedNetworkStatusWithHandler:]
		* (Unity)7개
			- ShowWebBrowser(string url)
			- ShowWebView(GamebaseRequest.Webview.GamebaseWebViewConfiguration configuration)
			- ShowToast(string message, int duration)
			- AddUpdateStatusListener(GamebaseCallback.DataDelegate<GamebaseResponse.Launching.LaunchingStatus> callback) 
			- RemoveUpdateStatusListener(GamebaseCallback.DataDelegate<GamebaseResponse.Launching.LaunchingStatus> callback)
			- AddOnChangedStatusListener(GamebaseCallback.DataDelegate<GamebaseNetworkType> callback)
			- RemoveOnChangedStatusListener(GamebaseCallback.DataDelegate<GamebaseNetworkType> callback)
			
	* Deprecated  API 
		* (Android)2개
			- (void)Gamebase.WebView.showWebView(Activity, String)
			- (void)Gamebase.WebView.showWebView(Activity, String, GamebaseWebViewConfiguration)
		* (iOS)1개
			- [TCGBGamebase languageCode]
		* (Unity)1개
			- GetLanguageCode()
* [SDK] Setting Tool		
	* 팝업 및 UI 개선
	
#### 버그수정
* [SDK] 1.14.1
	* (Android)Auth API 호출 후 콜백에서 다시 Auth API 중복 호출시 정상 호출이 되지 않는 버그 수정
	
### 2018. 10. 11.

#### 버그수정
* Console
	* 이용정지 : 대량등록시 발생하던 오류 수정
	
### 2018. 09. 20.

#### 버그수정
* Console
	* 관리 : 페이지 주소 오류로 인한 알람페이지 처리 실패 발생 수정

### 2018. 09. 13.

#### 기능 추가
* Console	
	* 회원: 계정의 IdP 추가 및 삭제 기능 추가, IdP ID 검색 기능 추가
	* 푸시: 푸시상태별로 발송이력 조회하는 기능 추가
* [SDK] 1.13.0
	* (iOS)App Store Promotion IAP를 지원하기 위한 API 추가


#### 기능 개선/변경
* [SDK] 1.13.0
	* (공통)IAP SDK 최신버전 적용 (android:1.5.1, iOS:1.6.0)
	* (Android)Push API 호출 시, Gamebase 초기화/로그인 상태에 따라 호출 실패에 대한 에러 메시지를 보다 명확하게 개선
		* 초기화 전 호출 : NOT_INITIALIZED(1)
		* 초기화 이후 호출시 Push 모듈이 없음 : NOT_SUPPORTED(10)
		* 초기화 성공 및 로그인 이전 호출 : NOT_LOGGED_IN(2)		
	* (iOS)authProviderProfileWithIDPCode api의 호출 결과의 구조가 1depth로 변경 (Android, Unity와 통일)
	* (Unity)로그에서 보여주는 json 데이터를 알아보기 쉽도록 출력 포맷 개선
* Console
	* 이용정지 : 앱가드를 이용한 이용정지 등록하는 UI 개선 - 기능 off시 데이터 초기화, Leaderboard 데이터 삭제 설정을 상태가 'on'인 경우에만 노출하도록 개선
	
#### 버그수정
* [SDK] 1.13.0
	* (Android)NaverCafe SDK와의 충돌로 Naver 로그인시 발생하던 오류 해결
	* (Unity)Unity 2017.2 이상 버전에서 Editor Play Mode 종료 시 websocke close 처리에서 발생하던 오류 수정
* Console
	* App : 정보 수정시 삭제버튼 뒤의 내용이 잘리는 현상 수정
		
### 2018. 08. 28.

#### 기능 추가
* Console	
	* 회원: 계정상태 변경 기능 추가, Push Token 조회 추가
	* 운영지표(유저통계) : 오늘 탈퇴자, 당일 가입 후 탈퇴자 지표 추가

#### 기능 개선/변경
* [SDK] 1.12.2
	* (Android)WebSocket 타입아웃시 (API 호출 시간 경과), 크래시가 날 수 있는 버그에 대해 방어로직 처리
	* (iOS)Google Auth Adapter, Naver Auth Adapter의 Callback URL Scheme 설정 개선
		* 콘솔에 "url_scheme_ios_only" 값을 설정하지 않으면 Default URL Scheme을 설정 하도록 개선 : Default URL Scheme을 사용하기 위해서는 XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.google 또는 tcgb.{Bundle ID}.naver 등록 필요
	* (iOS)Payco Auth Adapter 개선
		* URL Scheme 미설정으로 인해 의도치 않은 URL Scheme을 호출하던 문제 수정 : 설정 방법이 변경되어 업데이트를 위해서는 반드시 URL Scheme 설정 필요 (XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.payco를 등록)
* Console
	* 회원 : 아이디 매핑 이력 조회 기능 추가(최근 3개월 조회 -> 조회기간 직접 설정하도록 변경)
	* 구매(IAP) : 결제 정보 엑셀 다운로드 1일로 제한, 아이템 삭제 기능 삭제
	
#### 버그수정
* [SDK] 1.12.2
	* (Android)auth-twitter-adapter 를 포함한 상태에서 TargetSdk 28로 빌드시 초기화 에러가 발생하는 문제 수정

### 2018. 08. 09.

#### 기능 개선/변경
* [SDK] 1.12.1
	* (공통)IAP SDK 최신버전 적용 (1.5.0)
	* (공통)Gamebase 점검페이지에서 점검시간을 단말기 설정 국가시간에 맞추어 노출하도록 개선
	* (공통)점검페이지를 외부 페이지로 사용할 때 Console에 입력한 점검 정보를 사용할 수 있도록 기능 추가
	* (공통)IdP 매핑된 사용자의 Guest 매핑시도시 에러 발생(TCGB_ERROR_AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP)
	* (공통)인증 API 중복 호출시 에러 발생(AUTH_ALREADY_IN_PROGRESS_ERROR)
	* (Android)TencentPush SDK 업데이트 (3.2.3)
	* (Android)Onestore v17(API v5) 지원 : Gamebase에서는 v16(스토어코드=TS)은 제공하지 않습니다.
	* (iOS)에러코드 추가 : Gamecenter 로그인 거부(TCGB_ERROR_IOS_GAMECENTER_DENIED)
* [SDK] Setting Tool
	* 폴더명 변경 : TOAST -> Toast
	* 에러발생시 팝업 알림 추가 : File Download 실패, File Extract 실패, XML 파싱 실패
	
#### 버그수정
* [SDK] 1.12.1
	* (iOS)Naver 로그인 시 프로필 정보 조회 실패로 인해 로그인이 불가능한 버그 수정 : 프로필 정보 조회 실패하더라도 로그인은 성공하도록 변경	
* Console
	* 결제 내역: 'Reserved'상태에서 결제 상태 변경이 되지 않는 버그와 엑셀 다운로드 시 필터링이 적용되지 않던 문제 수정
