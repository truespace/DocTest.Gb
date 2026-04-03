---
source: release-notes-unity.md
section: "2.6.1 (2019.11.20)-to-1.10.1 (2018.06.11)"
order: 5
created_date: 2026-04-03
---

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
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [Android](../../aos-etc.md#game-user-data-settings) / [iOS](../../ios-etc.md#game-user-data-settings) / [Unity](../../unity-etc.md#game-user-data-settings) / JavaScript]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [Android](../../aos-etc.md#level-up-trace) / [iOS](../../ios-etc.md#level-up-trace) / [Unity](../../unity-etc.md#level-up-trace) / JavaScript]
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

### 1.14.2 (2018.11.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.2/GamebaseSDK-Unity.zip)
#### 기능 개선/변경
* [SDK] 1.14.2
    * (Android)점검시, 데이터구조에서 점검 시작/종료 시간을 의미하는 epoch time의 타입을 기존 String에서 long으로 타입 변경 : 기존 Gamebase Unity와 연동 후 점검 호출 시 타입불일치로 콜백이 내려오지 않는 현상으로 인한 수정
    * (iOS)Provider Profile 획득 메서드 호출 시, 반환하는 TCGBAuthProviderProfile 객체의 description 메서드의 JSON 문자열 구조 변경으로 인하여 Gamebase iOS SDK 1.14.0와 Unity Plugin 1.14.0 적용시 크래시가 발생될 수 있는 구조 수정

#### 버그수정
* [SDK] 1.14.2
    * (Unity)ShowWebView API 호출 시 파라메타에 Callback을 넣지 않으면 크래시가 발생되는 부분 수정
    * (Unity)iOS SDK의 Deleted API를 호출하는 코드가 있어 컴파일시 오류가 발생 되는 버그 수정
    
### 1.14.0 (2018.10.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.14.0
    * (공통)Gamebase 웹뷰에서 파일첨부 기능 추가 : Android의 API 19, Kitcat 에서는 정상 동작하지 않습니다.
    
#### 기능 개선/변경
* [SDK] 1.14.0
    * (공통)이용 정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
    * (Unity)GamebaseSDKSetting 오브젝트가 있는 씬으로 돌아갈 경우 오브젝트가 중복으로 생기지 않도록 개선
    * Remove API : Webview, Network, Launching
        * ShowWebBrowser(string url)
        * ShowWebView(GamebaseRequest.Webview.GamebaseWebViewConfiguration configuration)
        * ShowToast(string message, int duration)
        * AddUpdateStatusListener(GamebaseCallback.DataDelegate<GamebaseResponse.Launching.LaunchingStatus> callback) 
        * RemoveUpdateStatusListener(GamebaseCallback.DataDelegate<GamebaseResponse.Launching.LaunchingStatus> callback)
        * AddOnChangedStatusListener(GamebaseCallback.DataDelegate<GamebaseNetworkType> callback)
        * RemoveOnChangedStatusListener(GamebaseCallback.DataDelegate<GamebaseNetworkType> callback)
    * Deprecated  API 
        * GetLanguageCode()
* [SDK] Setting Tool        
    * 팝업 창 및 UI 개선
    
### 1.13.0 (2018.09.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.13.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 1.13.0
    * (공통)IAP SDK 최신버전 적용 (android:1.5.1, iOS:1.6.0)
    * (Unity)로그에서 보여주는 json 데이터를 알아보기 쉽도록 출력 포맷 개선
    
#### 버그수정
* [SDK] 1.13.0
    * (Unity)Unity 2017.2 이상 버전에서 Editor Play Mode 종료 시 websocke close 처리에서 발생하던 오류 수정
      
### 1.12.1 (2018.08.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 1.12.1
    * (공통)IAP SDK 최신버전 적용 (1.5.0)
    * (공통)Gamebase 점검페이지에서 점검시간을 단말기 설정 국가시간에 맞추어 노출하도록 개선
    * (공통)점검페이지를 외부 페이지로 사용할 때 Console에 입력한 점검 정보를 사용할 수 있도록 기능 추가
    * (공통)IdP 매핑된 사용자의 Guest 매핑시도시 에러 발생(TCGB_ERROR_AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP)
    * (공통)인증 API 중복 호출 시 에러 발생(AUTH_ALREADY_IN_PROGRESS_ERROR)
    * (Android)TencentPush SDK 업데이트 (3.2.3)
    * (Android)Onestore v17(API v5) 지원 : Gamebase에서는 v16(스토어코드=TS)은 제공하지 않습니다.
    * (iOS)오류 코드 추가 : Gamecenter 로그인 거부(TCGB_ERROR_IOS_GAMECENTER_DENIED)
* [SDK] Setting Tool
    * 폴더명 변경 : TOAST -> Toast
    * 에러 발생 시 팝업 창 알림 추가 : File Download 실패, File Extract 실패, XML 파싱 실패
    
### 1.12.0 (2018.07.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] Setting Tool
    * Setting Tool 최신 버전이 있을 경우 업데이트 알림 기능 추가 
    * 내부 null Exception 수정
    
#### 버그수정
* [SDK] 1.12.0
    * (Unity)IssueTransferKey API 호출 시 exception 발생하던 버그 수정
    * (Unity)Unity Google Adapter 제거 : 기존에 GoogleAdapter 사용중인 개발사는 아래 업데이트 가이드 참고
    

**Unity Google Adapter 업데이트 가이드**

* Unity SDK 1.6.0이상 1.11.0 이상 버전을 사용하는 경우 1.12.0 버전으로 업데이트 하기 전에 아래 내용을 필히 숙지하셔야 합니다.(1.6.0 미만 버전 사용중인 경우에는 GoogleAdapter를 미사용하기 때문에 영향이 없습니다.)
    1. Setting Tool 설정
        * GoogleAdapter가 제거됨에 따라 더이상 Unity 탭에서 Google 항목이 노출되지 않는다.
        * Google 인증을 사용할 경우에는 각 플랫폼 탭에서 Google 항목을 활성화한다.
            * Android > Authentication > Google 선택해서 설정
            * iOS > Authentication > Google 선택해서 설정
    2. Gamebase Login API (변경 없음)
        * Gamebase.Login(GamebaseAuthProvider.GOOGLE, callback);
    3. GPGS 기능을 사용하는 경우
        * GPGS SDK for Unity 유지
        * GPGS 관련 로직은 앱에서 별도로 관리
    4. GPGS 기능을 사용하지 않는 경우
        * GPGS SDK for Unity 삭제 

### 1.11.0 (2018.06.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* iOS Google IdP 추가 : iOS
* Twitter IdP 추가 : Android, iOS
* LINE IdP 추가 : Android만 제공. iOS는 2018년 7월 제공 예정입니다.
  
#### 기능 개선/변경
* [SDK] 1.11.0
    * (공통)LocalizedString 일본어 번역 추가
    * (공통)인증 API 호출 시 초기화, 로그인을 하지 않은 경우 명확히 에러 코드를 구분하도록 내부 로직을 개선
    * (Android)'android.permission.READ_PHONE_STATE' 권한 제거
    * (Android)GamebaseConfiguration.Builder의 필수 설정값인 setAppId, setAppVersion을 생성자에서 입력할 수 있도록 변경
    * (Android)GamebaseConfiguration.Builder 의 setServerApiVerseion API를 제거
    * (Android)getAuthBanInfo() API, class AuthBanInfo 이름을 변경 : getBanInfo(), class BanInfo
    * NAVER ID Login SDK 업데이트 : iOS(4.0.10)
* Sample App 
    * ServerPush 기능 및 Observer 기능 추가
    * Gamebase SDK 업데이트 : Android(1.9.0), iOS(1.9.0), Unity(1.10.1)    
    
### 1.10.1 (2018.06.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.10.1/GamebaseSDK-Unity.zip)

#### 버그수정
* [SDK] 1.10.1
    * (Unity)Unity Adapter가 없는 경우 AddMapping API 호출 시 내부적으로 로그인으로 처리하던 버그 수정
