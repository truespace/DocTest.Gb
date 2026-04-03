---
source: release-notes-ios.md
section: "2.6.0 (2019.11.12)-to-1.1.0 (2017.03.21) "
order: 4
created_date: 2026-04-03
---

### 2.6.0 (2019.11.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 데이터를 Log&Crash 에 전송하여 각종 분석에 이용할 수 있도록 TOAST Logger 추가
* Sign In with Apple 인증 추가

### 2.5.2 (2019.10.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.5.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* UIWebView를 WKWebView로 교체

### 2.5.1 (2019.09.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.5.1/GamebaseSDK-iOS.zip)
    
#### 기능 개선/변경

* GamebasePushAdapter 에서 사용중인 TCPushSDK 를 1.7.0으로 업데이트
    * TCPushSDK가 Static Library 에서 Framework 파일로 변경되었으므로 프로젝트에 TCPushSDK.framework 를 추가해야 합니다.
    
### 2.5.0 (2019.08.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.5.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Console 에서 입력한 CS URL 을 웹뷰로 오픈하는 API 제공
    
### 2.4.3 (2019.07.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.3/GamebaseSDK-iOS.zip)

#### 버그 수정

* 인증 시도 시 오류가 발생했을 경우, 형식에 맞지 않는 오류 메시지 파싱 시도에 따른 크래시 발생 이슈 수정

### 2.4.2 (2019.06.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* LaunchingInfo에 JSON string 형식의 TOAST Launching 정보를 추가
* LINE iOS SDK 업데이트 (5.0.1)
    * LINE Adpater의 최소 지원 OS 버전이 iOS 10으로 변경 
    * LINE 앱을 통한 로그인 기능 추가

#### 버그수정

* Analytics 버그 수정: 로그아웃, 탈퇴, 계정 이전 시 저장된 지표 데이터를 초기화 하도록 수정
* 네트워크 연결 문제로 간헐적으로 크래시가 발생하던 현상 수정

### 2.4.1 (2019.06.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.1/GamebaseSDK-iOS.zip)

#### 버그수정

* Analytics 지표 전송 시 일부 파라미터가 누락 되어 지표가 제대로 출력되지 않는 버그 수정

### 2.4.0 (2019.05.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 지표관련 Class 변경
    * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [iOS](../../ios-etc.md#game-user-data-settings)]
    * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [iOS](../../ios-etc.md#level-up-trace)]

    
### 2.3.0 (2019.04.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.3.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Launching Status Code 추가: "심사중(204)", "테스트중(203)"

### 2.2.2 (2019.04.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.2/GamebaseSDK-iOS.zip)

#### 버그수정

* showBlockingPopup을 NO로 설정 할 경우 Gamebase 초기화 콜백이 호출되지 않는 이슈를 수정

### 2.2.0 (2019.03.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* TransferAccount 기능 추가: guest 사용자가 매핑없이 최대 2개의 키를 이용하여 새로운 기기로 이전할 수 있는 기능
    * 추가된 API 
        * TransferAccountInfo 발급 API (issueTransferAccount)
        * 발급된 TransferAccountInfo를 사용하여 계정 이전을 요청하는 API (transferAccountWithIdPLogin)
        * 발급된 TransferAccountInfo를 확인하는 API (queryTransferAccount)
        * 이미 발급된 TransferAccountInfo 갱신하는 API (renewTransferAccount)        
* 강제 매핑 기능 추가: 이미 다른 계정에 연동 되어있는 IdP계정을 매핑할 수 있는 기능
    * 추가된 API 
        * 강제 매핑하는 API (addMappingForcibly)

#### 기능 개선/변경

* LINE iOS SDK의 App 로그인 기능이 비활성화
    * LINE SDK v4의 버그로 인해 iOS 12에서 앱 로그인이 실패 하는 이슈가 있어 Gamebase Line Adatper에서 Web 로그인만 지원하도록 변경

### 2.1.0 (2019.02.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.1.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* TransferKey API 삭제
    * issueTransferKey: TransferKey 발급
    * requestTransfer: TransferKey 검증
        
#### 버그수정

* Gamecenter를 Gamebase가 아닌 다른 로직에의해 로그인 한 후, Gamebase를 통하여 Gamecenter로그인을 시도할 때, 반응이 없는 버그 수정

### 2.0.0 (2019.01.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.0.0/GamebaseSDK-iOS.zip)

```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가

* Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK 내부에서 자동 전송)
    * setGameUserData: 게임 로그인 이후 유저 레벨 정보 전송
    * traceLevelUpData: 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출

#### 기능 개선/변경

* IAP SDK 업데이트
    * 결제 실패 시 간헐적으로 크래시가 발생하던 현상 수정

#### 버그수정

* iOS 12 이상의 시뮬레이터에서 debugMode On 상태로 Gamebase 초기화 시 크래시가 발생하던 현상 수정

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

### 1.5.0 (2017.12.21) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.5.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 웹뷰가 닫힐 때 발생하는 Close Callback 추가
* 웹뷰에서 사용하는 Custom Scheme의 Event를 받을 수 있는 기능 추가
* Unity Setting Tool 신규 배포

### 1.4.0 (2017.11.23) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.4.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* close/back 버튼 리소스가 없을 때, "x", "<" 등의 텍스트로 노출되던 이슈를 디폴트 값으로 대체

#### 버그 수정

* 웹뷰 런치 후, 기기 회전시 NavigationBar Title 이 reset이 되는 오류 수정
* 웹뷰의 NavigationBar Height을 커스터마이징 할 때, NavigationBar 배경 부분이 겹쳐서 노출되는 오류 수정

### 1.3.0 (2017.10.26) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.3.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Credential을 이용한 AddMapping API추가

### 1.2.0 (2017.09.21) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.2.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 이용 정지(사용자처벌) 기능 추가
* 이용 정지 사용자 팝업 창 노출

### 1.1.5 (2017.07.20) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.5/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Gamebase 상품 이용 중지시 관련 데이터 삭제를 위한 일 배치 기능 추가
* 시스템 팝업 창 API 추가 (showAlertWithTitle)
* 국가코드를 대문자로 반환하도록 변경 (Android)
* TCPush SDK 1.4.1 로 업데이트
* IAP SDK 1.3.3.20170627 로 업데이트

### 1.1.4 (2017.05.25) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.4/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Gamebase 상품 이용 중지시 관련 데이터 삭제를 위한 일 배치 기능 추가
* 런타임 중 결제 Store를 변경할 수 있는 API 제공

### 1.1.2 (2017.04.04) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 게임론칭시 점검, 긴급공지 팝업 창 개선

### 1.1.0 (2017.03.21) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 외부 AccessToken을 받아서 idPLogin을 해주는 인터페이스를 추가
