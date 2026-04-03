---
source: release-notes-android.md
section: "2.17.1 (2020.10.13)-to-1.14.2 (2018.11.15)"
order: 5
created_date: 2026-04-03
---

### 2.17.1 (2020.10.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.1/GamebaseSDK-Android.zip)
```
한게임 인증 사용을 원하는 경우 고객 센터로 미리 연락주세요.
```

#### 기능 추가
* Hangame IdP 인증 추가: SDK 2.17.0

#### 기능 개선/변경
* [SDK] 2.17.0
    * (공통) 고객 센터 첨부 이미지 클릭 시 다운로드 지원
    * (공통) TOAST SDK 업데이트: Android(0.23.2), Unity(0.21.2)

#### 버그 수정
* [SDK] 2.17.1
    * (Android) 2.17.0에서 ImageNotice API 호출 시 kotlinx-coroutine 모듈에서 크래시가 발생하는 문제 수정
    
### 2.16.0 (2020.09.22)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.16.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 고객 센터 기능 추가
    * [SDK] 2.16.0
        * (공통) API 추가(Gamebase.Contact.requestContactURL): 고객 센터 URL 반환
        * (공통) 고객 센터 API 에 userName 을 설정할 수 있도록 ContactConfiguration 파라미터 추가 
        
### 2.15.0 (2020.08.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.15.0/GamebaseSDK-Android.zip)

```
Gamebase SDK 2.15.0 버전에서 Google Billing Client 모듈이 업데이트 되었습니다.

'gamebase-adapter-purchase-google'을 사용한다면 Gamebase SDK 2.15.0 미만 버전에서 2.15.0 이상으로 업그레이드하는 경우 
반드시 이전 버전의 'Game Client Version'을 '업데이트 필수'로 설정해야 합니다.

아이템을 구매하다 오류가 발생하면 재처리를 수행하게 되는데 
여러 개의 단말기에서 서로 다른 Billing Client 버전이 적용된 상태에서는 재처리 수행 중에 문제가 생길 수 있기 때문입니다.
```

#### 기능 추가
* [SDK] 2.15.0
    * (공통) 푸시 토큰 등록시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
    * (공통) 푸시 API 추가: Push 토큰 정보 확인(Gamebase.Push.queryTokenInfo API)

#### 기능 개선/변경
* [SDK] 2.15.0
    * (공통) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)   

### 2.13.0 (2020.07.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.13.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.13.0
    * (Android) 이미지 공지의 팝업 창 이미지 비율 계산 로직 수정

#### 버그 수정
* [SDK] 2.13.0
    * (Android) 웹뷰 종료 시 종료 콜백에서 ANDROID_ACTIVITY_DESTROYED(31) 오류가 반환되는 문제 수정
    * (Android) 결제 모듈에 ProGuard 선언이 누락된 오류 수정
    
### 2.12.0 (2020.07.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.12.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 이미지 공지: 표시 기간과 우선순위에 따라 게임 내 이미지 팝업 창 표시
    * [SDK] 2.12.0: 이미지 공지 표시 API 추가
    
### 2.11.0 (2020.06.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.11.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.11.0
    * 결제 API 추가: 상품 ID로 결제 요청, 추가 정보(UserPayload) 입력해 결제 완료 시 확인할 수 있음

### 2.10.0 (2020.05.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.10.0
    * (공통) 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능

### 2.9.1 (2020.05.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.1/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 2.9.1
    * (Android) 매핑 이후 지표 레벨이 null이 되어 결제 지표에 정상적으로 반영되지 않는 오류 수정

### 2.9.0 (2020.04.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 탈퇴 유예 기능
    * [SDK] 2.9.0
        * (공통) API 추가: 탈퇴 유예 신청, 탈퇴 유예 신청 취소, 탈퇴 유예 상태에서 즉시 탈퇴, 유저의 탈퇴 유예 여부 확인
        
#### 기능 개선/변경
* [SDK] 2.9.0
    * (공통) TOAST SDK 업데이트: Android(v0.21.0), iOS(v0.23.0), Unity(0.20.1)
    * (공통) PAYCO Login SDK 업데이트: Android(v1.5.0), iOS(v1.4.0)

### 2.8.1 (2020.04.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.8.1 
    * (공통) Analytics 전송 결과 확인을 위한 내부 지표 추가
    * (Android) 프로세스 재시작 이후 크래시가 발생할 수 있는 코드를 수정
    
### 2.8.0 (2020.03.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.8.0
    * (공통) 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가

#### 기능 개선/변경
* [SDK] 2.8.0 
    * (공통) 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업 창이 추가로 노출하도록 개선
    * (Android) 로그인 직후 결제 관련 API를 호출할 때 초기화 타이밍 문제로 실패가 발생할 수 있는 코드를 수정

### 2.7.2 (2020.03.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.7.2 
      * Gamebase 초기화중 ToastLogger 초기화 부분에서 크래시가 발생할 수 있는 코드를 수정
      * 서버 버전을 v1.2.1 로 업데이트 하였습니다.

### 2.7.1 (2020.02.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.7.1
    * (공통) Guest로 Login 후 GetAuthProviderUserID 호출하면 값을 반환하도록 수정

### 2.7.0 (2020.01.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.0/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 2.7.0
    * (Android) 서버 응답(response)에서 traceError 필수 파라미터가 없더라도 크래시가 발생하지 않도록 수정
    * (Android) Firebase 설정이 누락되어 있을 때 예외가 발생하지 않도록 수정

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
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히 보기 [Android](../../aos-etc.md#game-user-data-settings) / [iOS](../../ios-etc.md#game-user-data-settings) / [Unity](../../unity-etc.md#game-user-data-settings) / JavaScript]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히 보기 [Android](../../aos-etc.md#level-up-trace) / [iOS](../../ios-etc.md#level-up-trace) / [Unity](../../unity-etc.md#level-up-trace) / JavaScript]
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
