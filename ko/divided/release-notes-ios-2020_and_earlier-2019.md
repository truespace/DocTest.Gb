## Game > Gamebase > 릴리스 노트 > iOS

### 2.6.2 (2019.12.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: TOAST iOS SDK(0.20.1)
* NAVER iOS SDK 업데이트 (4.1.0)
    
### 2.6.1 (2019.12.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.1/GamebaseSDK-iOS.zip)
    
#### 버그 수정
* AddMapping(강제, Forcibly) 사용 시, 매핑이 되지 않는 문제 수정
* Unity Plugin으로 PushConfiguration의 displayLanguageCode를 설정하지 않을 경우, NSNull 객체에 의하여 크래시가 발생하는 문제를 수정
    

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
    * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [iOS](./ios-etc/#game-user-data-settings)]
    * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [iOS](./ios-etc/#level-up-trace)]

    
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
