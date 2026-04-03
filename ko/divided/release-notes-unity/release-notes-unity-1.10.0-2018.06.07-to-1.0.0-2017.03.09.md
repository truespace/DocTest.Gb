---
source: release-notes-unity.md
section: "1.10.0 (2018.06.07)-to-1.0.0 (2017.03.09)"
order: 6
created_date: 2026-04-03
---

### 1.10.0 (2018.06.07)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.10.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.10.0
    * (Unity)StandaloneWebviewAdapter: html source rendering 지원    

#### 기능 개선/변경
* [SDK] 1.10.0
    * (Unity)Unity Adapter의 interface가 수정
        * v1.10.0 이상 사용 시에는 UnityAdapter 버전 업그레이드가 필요(GamebaseUnitySDK_FacebookAdapter_v1.5.0, GamebaseUnitySDK_StandaloneWebviewAdapter_v1.7.0)
    * (Unity)Login API 호출 시 Unity Adapter가 없는 경우 네이티브(Android/iOS)의 로그인 API를 호출하도록 로직 변경 : facebook, Google
    * (Unity)각 Adapter 폴더 구조 및 이름 오타 수정
        * 경로: Assets/Gamebase/Scripts/Adapter => Assets/Gamebase/Adapter
        * 오타: Adapater => Adapter    
    
### 1.9.0 (2018.05.18)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 1.9.0
    * Unity SDK(1.9.0) Google Adapter 신규버전(1.6.2)으로 교체하여 재배포
        * 5/3 배포된 Unity SDK(1.9.0)에 적용된 Google Adapter를 최신버전으로 교체(1.6.1->1.6.2)
    
### 1.9.0 (2018.05.03)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.9.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* Transfer 기능 추가
    * guest 사용자가 매핑없이 새로운 기기로 이전할 수 있는 기능
    * (SDK공통)추가된 API 
        * Transfer Key 발급 API (IssueTransferKey)
        * 발급된 TransferKey를 사용하여 계정 이전을 요청하는 API (RequestTransfer)
* 이용 정지 등록시 사용자의 리더보드(랭킹) 데이터를 삭제할 수 있는 옵션 추가(TOAST Leaderboard를 사용하는 경우에 한함)
    * 이용 정지 등록 메뉴를 이용하거나 App Guard 연동 페이지에서 사용 가능

### 1.8.1 (2018.04.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.1/GamebaseSDK-Unity.zip)
#### 버그 수정
* [SDK] 1.8.1
    * (Unity)UnityAndroid 플랫폼에서 아래 기능 사용 시 모듈 초기화가 되지 않아 NullReferenceException이 발생하여 수정
        * Launching, Purchase, Push, Util, Webview

### 1.8.0 (2018.04.05)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* Kick out 기능 추가
    * 현재 게임 중인 전체 사용자의 연결을 끊는 기능(점검시 게임에서 전체 사용자의 연결을 끊고 싶을 때 사용할 수 있음)
    * (SDK 공통)kick out 이벤트를 받을 수 있는 API 추가
* 점검 웹페이지를 사용자가 Console에서 입력한 HTML 페이지로 사용할 수 있도록 기능을 개선
    * 이전에는 Gamebase에서 제공하는 웹페이지나 외부 웹페이지 연결만 가능했음
    * 웹서버가 없는 경우에도 점검페이지를 사용자가 원하는 형태로 만들 수 있음
* Observer 기능 개발 및 API 추가
    * (SDK 공통) 점검 등 앱 상태/네트워크 상태/유저 상태(이용 정지) 변경사항에 대한 Listener를 Observer 등록을 통하여 일괄 처리할 수 있도록 API 추가

#### 기능 개선/변경
* [SDK] 1.8.0
    * (공통)Observer 기능 추가에 따라 다음 API Deprecated : LaunchingStatus Listener, Network Listener(기존 사용자는 계속 사용 가능)
    * (iOS)페이코 간편로그인 3rd SDK v1.2.2 적용 : 로그인 성공 시 토큰 만료 정보(expires_in) 제공, iPhoneX 로그인 UI 개선
    * (iOS)iPhoneX 지원을 위하여, 웹뷰 사용 인터페이스 수정

#### 버그 수정
* 국가코드(contry code)가 10자 이상인 경우 동접 데이터가 저장되지 않는 현상 수정
* [SDK] 1.8.0
    * (Setting Tool)Unity Facebook Adapter를 체크하면 에러가 나는 버그 수정

### 1.7.1 (2018.03.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.7.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* [SDK] 1.7.1
    * (Unity)Inspector에서 설정된 SetDebugMode 값이 반영 안 되던 버그 수정
    * (Unity)Standalone, WebGL: Display Language에서 사용되는 리소스 파일 누락 부분 수정
    * (Unity)Google Adapter 1.6.2 배포: Google Adapter 1.6.1에서 AuthCode가 Empty로 반환되어 인증 실패하는 버그 수정

### 1.7.0 (2018.02.22)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.7.0/GamebaseSDK-Unity.zip)
#### 기능 추가
* [SDK] 1.7.0
    * Naver IdP 인증 추가
    * Display Language 설정 추가: 단말기 언어와 별도로 게임내에서 게임유저의 노출 언어를 설정할 수 있도록 Display 언어를 추가하였습니다.

### 1.6.0 (2018.01.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.6.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.6.0
    * (Unity)Standalone WinSDK 추가
        * 64비트 지원
        * 인증 지원 : facebook, google, payco

### 1.5.0 (2017.12.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.5.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.5.0
    * 웹뷰가 닫힐 때 발생하는 Close Callback 추가
    * 웹뷰에서 사용하는 Custom Scheme의 Event를 받을 수 있는 기능 추가
    * Unity Setting Tool 신규 배포

#### 버그 수정
* [SDK] 1.5.0
    * (Unity)UnityEditor에서 Guest로그인이 되지 않는 현상 수정
    * (Unity)TOAST Console에 Facebook 인증 정보를 등록하지 않고 Gamebase.Login("facebook") API를 호출할 경우, KeyNotFoundException이 발생하여 방어코드 추가

### 1.4.0 (2017.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.4.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.4.0 업데이트
    * (Unity)Gamebase Facebook Adapter가 추가 : Android, iOS, WebGL, Standalone Platform 및 UnityEditor 지원

### 1.3.0 (2017.10.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.3.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.3.0 업데이트
    * Credential을 이용한 AddMapping API추가

#### 기능 개선/변경
* [SDK] 1.3.0 업데이트
    * (Unity)CredentialInfo를 사용하는 Login API호출 시 iOSPlugin에서 Json 파싱이 안되던 버그를 수정

### 1.2.0 (2017.09.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.2.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 이용 정지(사용자처벌) 기능 추가
* [SDK] 1.2.0 업데이트
    * 이용 정지 사용자 팝업 창 노출

### 1.1.5 (2017.07.20)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.5/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* Gamebase 상품 이용 중지시 관련 데이터 삭제를 위한 일 배치 기능 추가
* [SDK] 1.1.5 업데이트
    * 시스템 팝업 창 API 추가 (showAlertWithTitle)
    * 국가코드를 대문자로 반환하도록 변경 (Android)
    * TCPush SDK 1.4.1 로 업데이트
    * IAP SDK 1.3.3.20170627 로 업데이트

### 1.1.4 (2017.05.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.4/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* Gamebase 상품 이용 중지시 관련 데이터 삭제를 위한 일 배치 기능 추가
* [SDK] 1.1.4 업데이트
    * 런타임 중 결제 Store를 변경할 수 있는 API 제공
    * (Android)TCPushSdk v1.4 적용, Tencent Push 기능 제공

### 1.1.2 (2017.04.04)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.2/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 1.1.2 업데이트
    * 게임 론칭시 점검, 긴급공지 팝업 창 개선
    * Unity Plugin 디버그로그 추가 및 익셉션 상세처리

### 1.1.0 (2017.03.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 1.1.0 업데이트
    * 외부 AccessToken을 받아서 idPLogin을 해주는 인터페이스를 추가
    * [UI 기능 추가](../../aos-ui.md) : Custom Webview, AlertDialog

### 1.0.0 (2017.03.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.0.0/GamebaseSDK-Unity.zip)

#### 신규 상품 출시
* 게임에서 공통적으로 필요한 기능들을 제공하여 손쉽고 효율적으로 게임 개발이 가능하도록 돕는 서비스입니다.
    * 다양한 인증 지원 : Guest , 3rd Party(Google , Facebook, GameCenter 등) 인증
    * 로그아웃 및 회원탈퇴 기능을 제공
    * 하나의 User가 여러 개의 외부 IDP를 동시에 사용할 수 있도록 mapping기능을 제공
    * 게임운영을 위한 게임 앱 상태관리, 점검, 긴급공지 등의 기능을 웹콘솔로 제공
    * 실시간 운영지표 확인 가능한 웹콘솔 화면 제공
    * TOAST Cloud상품 연동 : PUSH, IAP
