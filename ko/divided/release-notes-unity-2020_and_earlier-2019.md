## Game > Gamebase > 릴리스 노트 > Unity

### 2.6.2 (2019.12.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.2/GamebaseSDK-Unity.zip)

#### 기능 추가
* 쿠폰 > 쿠폰 발급: 키워드 쿠폰 기능 추가

#### 기능 개선/변경
* [SDK] 2.6.2
    * (공통) TOAST SDK 업데이트: Android(0.19.4), iOS(0.20.1), Unity(0.18.0)
    * (iOS) NAVER SDK 버전 업데이트(4.1.0)

### 2.6.1 (2019.11.20)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* [SDK] 2.6.1
    * (Unity)iOS Plugin 파일이 Package에 누락되어 iOS 빌드 시 에러가 발생하여 해당 파일을 추가: 'toast_sdk_wrap.m'
    * (Unity)UnityEditor에서 Standalone 이외의 플랫폼으로 실행시 Store Code가 Empty로 입력되어 초기화에 실패하는 오류 수정
    * (Unity)Initialize API 내부 zone type 처리 부분에서의 오류로 NullReferenceException 발생하던 오류 수정

### 2019. 11. 13.

#### 버그 수정
* GamebaseSettingTool
    * Gamebase v2.6.0 업데이트 시, 파일이 정상적으로 변경되지 않는 오류 수정


### 2.6.0 (2019.11.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.0/GamebaseSDK-Unity.zip)

```
Gamebase SDK 2.6.0 미만 버전에서 2.6.0으로 업그레이드 하는 경우
반드시 Upgrade Guide문서에 설명된 변경 사항을 반영해 주시기 바랍니다. 
가이드 위치: Game > Gamebase > Upgrade Guide
```

#### 기능 추가
* Google 구독 결제 기능 추가
    * [SDK] 2.6.0 Android
* [SDK] 2.6.0
    * (공통) 데이터를 Log&Crash 에 전송하여 각종 분석에 이용할 수 있도록 TOAST Logger 추가
    * (iOS) Sign In with Apple 인증 추가
    * (Android) Gamebase Android SDK가 Bintray 를 통해 배포되므로 gradle 설정만으로 Gamebase 를 사용할 수 있음

#### 기능 개선/변경
* [SDK] 2.6.0
    * (Unity) 로그인시 LaunchingStatus를 갱신하는 로직에 오류가 있어 수정
    * (Unity) Debug Log를 전송하는 기능을 Gamebase 콘솔에서 설정할 경우 Client에서 로그 전송을 무한 반복하는 오류 수정

### 2019. 10. 15.
#### 기능 개선/변경
* Sample App
    * Gamebase SDK 업데이트(v2.4.0)
    * Smart Downloader 적용(v1.5.8), Leaderboard 적용
    * 기능 추가: 게임리소스 다운로드, Leaderboard, TAA 지표 연동, 단말기 이전 기능, 강제 매핑 기능
    * 개선/변경: ServerPush 리스너 추가, Observer 점검 여부 감지 추가
    * 게임 리뉴얼
      
### 2.5.0 (2019.08.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.5.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.5.0
    * Console에서 입력한 CS URL을 웹뷰로 오픈하는 API 제공
    
### 2019. 08. 02.
#### 버그 수정
* [SDK] Setting Tool 1.4.3
    * Script 파일의 위치를 Editor 폴더 아래로 이동하여 빌드 오류를 해결
    * Mac OS에서 Multilanguage에 Language 파일의 전체 경로를 지정하면 동작하지 않던 문제 수정

### 2.4.4 (2019.07.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.4/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.4.4
    * (공통) 회원 오류 코드 포맷 변경
    * (Unity) GamebaseServerPushType에 키 추가(TRANSFER_KICKOUT)
* Setting Tool
    * 폴더 구조 변경: `기존 SettingTool을 완전히 삭제한 후 재설치해야 합니다.`
    * 다국어 지원 추가
    
### 2.4.3 (2019.07.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.3/GamebaseSDK-Unity.zip)

#### 버그 수정
* [SDK] 2.4.3
    * (Unity)iOS와 Android로 빌드시 AddMappingForcibly API가 동작하지 않는 오류 수정
    * (Unity)RequestRetryTransaction API 호출 시 iOSPlugin에서 JSON 파싱 오류가 있어 수정

### 2019. 06. 27.

#### 버그수정
* [SDK] Setting Tool 1.4.1
    * GamebaseSettingTool 실행시 기존 설정 정보를 가져오지 못하는 오류가 발생하여 수정

### 2.4.2 (2019.06.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.2/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.4.2
    * (공통)LaunchingInfo에 JSON string 형식의 TOAST Launching 정보를 추가

#### 버그수정
* [SDK] 2.4.2
    * (공통)Analytics 버그 수정: 로그아웃, 탈퇴, 계정 이전 시 저장된 지표 데이터를 초기화 하도록 수정

### 2.4.0 (2019.05.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* HANGAME mix 일본결제 추가
    * [SDK] 2.4.0
        * (Unity)Standalone 일본 외부결제 추가
        * (Unity)Standalone 일본 HANGAME 인증 추가

#### 기능 개선/변경
* [SDK] 2.4.0
    * (공통) 지표관련 Class 변경
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [Android](./aos-etc/#game-user-data-settings) / [iOS](./ios-etc/#game-user-data-settings) / [Unity](./unity-etc/#game-user-data-settings) / JavaScript]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [Android](./aos-etc/#level-up-trace) / [iOS](./ios-etc/#level-up-trace) / [Unity](./unity-etc/#level-up-trace) / JavaScript]
    * (Android)NAVER SDK 버전 업데이트(v4.2.5): NAVER SDK 버그 수정(NAVER 로그인 도중에 앱 아이콘을 통해 앱을 재시작할 경우, Activity가 강제종료 되는 이슈로 인해 인증 프로세스가 중단되는 이슈가 해결)
    * (Unity)StandaloneWebview가 32bit 빌드를 지원 (SDK 용량 53.6MB에서 99.2MB로 증가)

    
### 2.3.0 (2019.04.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.3.0/GamebaseSDK-Unity.zip)

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

### 2.2.2 (2019.04.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.2/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.2.2
    * (Unity)SDK 로그 개선

#### 버그수정
* [SDK] 2.2.2
    * (Unity)AddMappingForcibly API를 호출하면 크래시가 발생하여 수정

### 2.2.1 (2019.04.02)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.1/GamebaseSDK-Unity.zip)
#### 버그수정
* [SDK] 2.2.1
    * (Unity) Unity Editor에서 Android 플랫폼을 선택하고 플레이를 하면 initialize시 서버에서 에러가 발생하는 이슈 수정

### 2.2.0 (2019.03.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.2.0/GamebaseSDK-Unity.zip)
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
    * (iOS)LINE SDK의 App 로그인 기능이 비활성화
        * LINE SDK v4의 버그로 인해 iOS 12에서 앱 로그인이 실패 하는 이슈가 있어 Gamebase Line Adatper에서 Web 로그인만 지원하도록 변경
    * (Unity)GamebaseMainActivity의 Package Name이 변경
        * com.toast.gamebase.activity.GamebaseMainActivity -> com.toast.android.gamebase.activity.GamebaseMainActivity

### 2.1.0 (2019.02.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.1.0/GamebaseSDK-Unity.zip)
#### 기능 개선/변경
* [SDK] 2.1.0
    * (공통)TransferKey API 삭제
        * issueTransferKey : TransferKey 발급
        * requestTransfer : TransferKey 검증

### 2.0.0 (2019.01.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.0.0/GamebaseSDK-Unity.zip)
```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가
* [SDK] 2.0.0
    * (공통)Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK내부에서 자동 전송)
        * setGameUserData : 게임 로그인 이후 유저 레벨 정보 전송
        * traceLevelUpData : 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출
