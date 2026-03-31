## Game > Gamebase > 릴리스 노트 > iOS

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

### 1.0.0 (2017.03.09) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.0.0/GamebaseSDK-iOS.zip)

#### 신규 상품 출시
* 게임에서 공통적으로 필요한 기능들을 제공하여 손쉽고 효율적으로 게임 개발이 가능하도록 돕는 서비스입니다.
    * 다양한 인증 지원: Guest , 3rd Party(Google , Facebook, GameCenter 등) 인증
    * 로그아웃 및 회원탈퇴 기능을 제공
    * 하나의 User가 여러 개의 외부 IDP를 동시에 사용할 수 있도록 mapping기능을 제공
    * 게임운영을 위한 게임 앱 상태관리, 점검, 긴급공지 등의 기능을 웹콘솔로 제공
    * 실시간 운영지표 확인 가능한 웹콘솔 화면 제공
    * TOAST Cloud상품 연동: PUSH, IAP
