## Game > Gamebase > Unity SDK 사용 가이드 > 초기화

### Launching Information

Initialize API를 사용하여 Gamebase Unity SDK를 초기화하면 LaunchingInfo 객체가 결과값으로 전달됩니다.
이 LaunchingInfo 객체에는 Gamebase 콘솔에 설정한 값들과 게임 상태 등이 포함돼 있습니다.

#### 1. launching

Gamebase 론칭 정보입니다.

**1.1 status**

Gamebase Unity SDK 초기화 설정에 입력한 앱 버전의 게임 상태 정보입니다.

* code: 게임 상태 코드(점검 중, 업데이트 필수, 서비스 종료 등)
* message: 게임 상태 메시지

상태 코드는 아래 표를 참고하십시오.

| Status                      | Code | Description                              |
| --------------------------- | ---- | ---------------------------------------- |
| IN_SERVICE                  | 200  | 정상 서비스 중                                 |
| RECOMMEND_UPDATE            | 201  | 업데이트 권장                                  |
| IN_SERVICE_BY_QA_WHITE_LIST | 202  | 점검 중에는 서비스를 이용할 수 없지만 QA 단말기로 등록된 경우에는 점검과 상관없이 서비스에 접속해 테스트할 수 있습니다. |
| IN_TEST                     | 203  | 테스트 중 |
| IN_REVIEW                   | 204  | 심사 중 |
| IN_BETA                     | 205  | 베타 서버 환경 |
| REQUIRE_UPDATE              | 300  | 업데이트 필수                                  |
| BLOCKED_USER                | 301  | 접속 차단으로 등록된 단말기(디바이스 키)로 서비스에 접속한 경우입니다. |
| TERMINATED_SERVICE          | 302  | 서비스 종료                                   |
| INSPECTING_SERVICE          | 303  | 서비스 점검 중                                 |
| INSPECTING_ALL_SERVICES     | 304  | 전체 서비스 점검 중                              |
| INTERNAL_SERVER_ERROR       | 500  | 내부 서버 오류                                 |

[Game > Gamebase > 콘솔 사용 가이드 > 앱 > App](./oper-app/#app)

**1.2 app**

Gamebase 콘솔에 등록된 앱 정보입니다.

* accessInfo
    * serverAddress: 서버 주소
* customerService
    * accessInfo : 고객 센터 연락처
    * type : 고객 센터 유형
    * url : 고객 센터 URL
* relatedUrls
    * termsUrl: 이용약관
    * personalInfoCollectionUrl: 개인 정보 동의
    * punishRuleUrl: 이용 정지 규정
* install: 설치 URL
* idP: 인증 정보

[Game > Gamebase > 콘솔 사용 가이드 > 앱 > Client](./oper-app/#client)

**1.3 maintenance**

Gamebase 콘솔에 등록된 점검 정보입니다.

* url: 점검 페이지 URL
* timezone: 표준 시간대(timezone)
* beginDate: 시작 시간
* endDate: 종료 시간
* message: 점검 사유
* hideDate: 점검 시작, 종료 시간을 표시할 것인지 여부

[Game > Gamebase > 콘솔 사용 가이드 > 운영 > Maintenance](./oper-operation/#maintenance)

##### Change Default Maintenance HTML

`enablePopup`과 `enableLaunchingStatusPopup` 값이 모두 `true`인 경우, 게임이 점검 상태라면 자동으로 점검 팝업 창이 표시됩니다.
![](https://static.toastoven.net/prod_gamebase/DevelopersGuide/maintenance_popup_android_2.30.0.png)

여기서 **자세히 보기** 버튼을 클릭하면 점검 정보가 자동으로 웹뷰로 표시됩니다.
![](https://static.toastoven.net/prod_gamebase/DevelopersGuide/maintenance_webview_android_2.30.0.png)

이때 표시되는 html 파일을 수정하고 싶다면 다음 링크의 html 파일을 다운로드하여 원하는 대로 수정한 후 'Assets > StreamingAssets > Gamebase' 폴더에 두면 Gamebase SDK에 내장된 기본 html 파일 대신 해당 html 파일을 사용하여 점검 정보를 표시하게 됩니다.
[html 파일 다운로드 LINK](https://static.toastoven.net/prod_gamebase/DevelopersGuide/gamebase-maintenance.html)

**1.4 notice**

Gamebase 콘솔에 등록된 공지 정보입니다.

* message: 메시지
* title: 타이틀
* url: 점검 URL

[Game > Gamebase > 콘솔 사용 가이드 > 운영 > Notice](./oper-operation/#notice)

**1.5 user**

Gamebase 초기화를 실행한 사용자 정보입니다.

* testDevice: 테스트 단말기 정보(Status가 200대일 경우에만 전달)
    * matchingFlag: 사용자 단말기가 Gamebase 콘솔에 설정된 테스트 단말기의 정보와 동일한지 여부
    * matchingTypes
        * 테스트 단말기 정보와 매칭된 타입
        * matchingFlag가 true일 경우에만 전달

#### 2. tcProduct

Gamebase와 연계된 NHN Cloud 서비스의 appKey입니다.

* gamebase
* tcLaunching
* iap
* push

#### 3. tcIap

NHN Cloud 콘솔에 등록된 IAP 스토어 정보입니다.

* id: App ID
* name: App Name
* storeCode: Store Code
 
[Game > Gamebase > 콘솔 사용 가이드 > 결제](./oper-purchase/)

#### 4. tcLaunching

NHN Cloud Launching 콘솔에서 사용자가 입력한 정보입니다

* 사용자가 입력한 값을 JSON string으로 전달합니다.
* NHN Cloud Launching 상세 설정은 아래 가이드를 참고하시기 바랍니다.
 
[Game > Gamebase > 콘솔 사용 가이드 > 관리 > Config](./oper-management/#config)
