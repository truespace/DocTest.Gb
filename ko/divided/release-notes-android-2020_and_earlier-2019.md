## Game > Gamebase > 릴리스 노트 > Android

### 2.6.2 (2019.12.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.6.2
    * (공통) TOAST SDK 업데이트: Android(0.19.4), iOS(0.20.1), Unity(0.18.0)
    
### 2.6.1 (2019.12.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.1/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 2.6.1
    * (Android)Gamebase.initialize() 호출 전에 Gamebase.login() 을 호출할 때 크래시가 발생하는 문제 수정
    * (Android)TOAST Analytics User Data 를 java 주소 값으로 잘못 전송하는 문제 수정
    * (Android)IAP 상품을 활성화 시키지 않은 경우 발생하는 크래시 수정

### 2.6.0 (2019.11.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.0/GamebaseSDK-Android.zip)

```
Gamebase SDK 2.6.0 미만 버전에서 2.6.0으로 업그레이드 하는 경우
반드시 Upgrade Guide문서에 설명된 변경 사항을 반영해 주시기 바랍니다. 
가이드 위치: Game > Gamebase > Upgrade Guide
```

#### 기능 추가
* [SDK] 2.6.0
    * (공통) 데이터를 Log&Crash 에 전송하여 각종 분석에 이용할 수 있도록 TOAST Logger 추가
    * (Android) Google 구독 결제 기능 추가
    * (Android) Gamebase Android SDK가 Bintray 를 통해 배포되므로 gradle 설정만으로 Gamebase 를 사용할 수 있음

### 2.5.0 (2019.08.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.5.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.5.0
    * Console에서 입력한 CS URL을 웹뷰로 오픈하는 API 제공

### 2.4.4 (2019.07.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.4/GamebaseSDK-Android.zip)

#### 기능 개선/변경 
* [SDK] 2.4.4
    * (공통) 회원 오류 코드 포맷 변경

### 2.4.2 (2019.06.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.4.2
    * (공통)LaunchingInfo에 JSON string 형식의 TOAST Launching 정보를 추가

#### 버그수정
* [SDK] 2.4.2
    * (공통)Analytics 버그 수정: 로그아웃, 탈퇴, 계정 이전 시 저장된 지표 데이터를 초기화 하도록 수정

    
### 2.4.0 (2019.05.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.4.0
    * (공통) 지표관련 Class 변경
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히 보기 [Android](./aos-etc/#game-user-data-settings) / [iOS](./ios-etc/#game-user-data-settings) / [Unity](./unity-etc/#game-user-data-settings) / JavaScript]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히 보기 [Android](./aos-etc/#level-up-trace) / [iOS](./ios-etc/#level-up-trace) / [Unity](./unity-etc/#level-up-trace) / JavaScript]
    * (Android)NAVER SDK 버전 업데이트(v4.2.5): NAVER SDK 버그 수정(NAVER 로그인 도중에 앱 아이콘을 통해 앱을 재시작할 경우, Activity가 강제종료 되는 이슈로 인해 인증 프로세스가 중단되는 이슈가 해결)

### 2.3.1 (2019.05.16)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.3.1/GamebaseSDK-Android.zip)

#### 버그수정
* [SDK] 2.3.1
    * (Android)2.3.0버전에서 Twitter 로그인 되지 않던 문제 수정



### 2.3.0 (2019.04.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.3.0/GamebaseSDK-Android.zip)
    
```
Gamebase를 사용하면 50여개의 중국스토어 연동이 가능합니다.
중국출시에 관심 있으신 경우에는 고객 센터로 연락주세요.
```

#### 기능 추가
* [SDK] 2.3.0
    * (Android/Unity)중국스토어 인증/결제 추가

#### 기능 개선/변경
* [SDK] 2.3.0
    * (공통)Launching Status Code 추가: "심사중(204)", "테스트중(203)"
    * (Android)최근 로그인한 Provider로 로그인 및 웹소켓 응답 실패를 받았을 경우(Timeout, network disable 등) AuthToken을 삭제 처리하지 않도록 수정
    * (Android)IdP로그인 시 AuthAdapter 내부에서 발생하는 MemoryLeak을 수정

### 2.2.2 (2019.04.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.2/GamebaseSDK-Android.zip)

#### 버그수정
* [SDK] 2.2.2
    * (Android)Gamebase 초기화 이전 TransferAccount API 호출 시, 콜백이 오지 않는 이슈를 수정

### 2.2.0 (2019.03.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.0/GamebaseSDK-Android.zip)

#### 기능 추가
* TransferAccount 기능 추가: guest 사용자가 매핑없이 최대 2개의 키를 이용하여 새로운 기기로 이전할 수 있는 기능
    * (SDK공통)추가된 API 
        * TransferAccountInfo 발급 API (issueTransferAccount)
        * 발급된 TransferAccountInfo를 사용하여 계정 이전을 요청하는 API (transferAccountWithIdPLogin)
        * 발급된 TransferAccountInfo를 확인하는 API (queryTransferAccount)
        * 이미 발급된 TransferAccountInfo 갱신하는 API (renewTransferAccount)        
* 강제 매핑 기능 추가: 이미 다른 계정에 연동 되어있는 IdP계정을 매핑할 수 있는 기능
    * (SDK공통)추가된 API 
        * 강제 매핑하는 API (addMappingForcibly)

#### 기능 개선/변경
* [SDK] 2.2.0
    * (Android)IAP SDK 버전을 최신버전인 v1.5.3 버전으로 업데이트

### 2.1.0 (2019.02.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.1.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.1.0
    * (공통)TransferKey API 삭제
        * issueTransferKey : TransferKey 발급
        * requestTransfer : TransferKey 검증
        
#### 버그수정
* [SDK] 2.1.0
    * (Android)Gamebase 초기화 이전, onActivityResult()가 호출되면서 이상 동작하던 버그 수정

### 2.0.0 (2019.01.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.0.0/GamebaseSDK-Android.zip)

```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가
* [SDK] 2.0.0
    * (공통)Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK내부에서 자동 전송)
        * setGameUserData : 게임 로그인 이후 유저 레벨 정보 전송
        * traceLevelUpData : 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출


#### 기능 개선/변경
* [SDK] 2.0.0
    * (Android)Push SDK 업데이트(android:1.7.0)
    * (Android)Adapter API 변경
        * Launching 정보 전달
        * logout, withdraw API에 Callback 추가
