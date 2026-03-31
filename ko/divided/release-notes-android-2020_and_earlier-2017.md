## Game > Gamebase > 릴리스 노트 > Android

### 1.5.0 (2017.12.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.5.0/GamebaseSDK-Android.zip)
#### 기능 추가
* [SDK] 1.5.0
    * 웹뷰가 닫힐 때 발생하는 Close Callback 추가
    * 웹뷰에서 사용하는 Custom Scheme의 Event를 받을 수 있는 기능 추가

### 1.4.0 (2017.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.4.0/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 1.4.0 업데이트
    * (Android)Gamebase 제공 팝업 창을 사용하지 않는 경우 이용 정지 정보가 null로 반환되는 오류 수정

### 1.3.0 (2017.10.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.3.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 1.3.0 업데이트
    * Credential을 이용한 AddMapping API추가

### 1.2.0 (2017.09.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.2.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 이용 정지(사용자처벌) 기능 추가
* [SDK] 1.2.0 업데이트
    * 이용 정지 사용자 팝업 창 노출


### 1.1.5 (2017.07.20)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.5/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.1.5 업데이트
    * 시스템 팝업 창 API 추가 (showAlertWithTitle)
    * 국가코드를 대문자로 반환하도록 변경 (Android)
    * TCPush SDK 1.4.1 로 업데이트
    * IAP SDK 1.3.3.20170627 로 업데이트

### 1.1.4 (2017.05.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.4/GamebaseSDK-Android.zip)
#### 기능 개선/변경
* [SDK] 1.1.4 업데이트
    * 런타임 중 결제 Store를 변경할 수 있는 API 제공
    * (Android)TCPushSdk v1.4 적용, Tencent Push 기능 제공

### 1.1.3 (2017.04.20)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.3/GamebaseSDK-Android.zip)
#### 기능 개선/변경
* [SDK] 1.1.3 업데이트
    * (Android)론칭 구조 및 팝업 창/점검 페이지 개선 :커스텀 점검 페이지 설정 기능 추가
    * (Android)인증 구조 개선 및 로그 추가 : 인증 Adapter 및 SDK 버전 로그 출력

#### 버그 수정
* [SDK] 1.1.3 업데이트
    * (Android)Facebook SDK v4.19.0 이상에서 초기화시 크래시 오류 수정


### 1.1.2 (2017.04.04)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.1.2 업데이트
    * 게임 론칭시 점검, 긴급공지 팝업 창 개선

### 1.1.0 (2017.03.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.1.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.1.0 업데이트
    * 외부 AccessToken을 받아서 idPLogin을 해주는 인터페이스를 추가
    * [UI 기능 추가](./aos-ui) : Custom Webview, AlertDialog

### 1.0.0 (2017.03.09) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.0.0/GamebaseSDK-Android.zip)

#### 신규 상품 출시
* 게임에서 공통적으로 필요한 기능들을 제공하여 손쉽고 효율적으로 게임 개발이 가능하도록 돕는 서비스입니다.
    * 다양한 인증 지원 : Guest , 3rd Party(Google , Facebook, GameCenter 등) 인증
    * 로그아웃 및 회원탈퇴 기능을 제공
    * 하나의 User가 여러 개의 외부 IDP를 동시에 사용할 수 있도록 mapping기능을 제공
    * 게임운영을 위한 게임 앱 상태관리, 점검, 긴급공지 등의 기능을 웹콘솔로 제공
    * 실시간 운영지표 확인 가능한 웹콘솔 화면 제공
    * TOAST Cloud상품 연동 : PUSH, IAP
