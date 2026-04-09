---
source: unreal-initialization.md
section: "FGamebaseConfiguration"
order: 2
split: true
created_date_time: 20260408_184906
keyword: Unreal, Login, Purchase, Initialize, Android, Console
---

### FGamebaseConfiguration 

초기화 시 필요한 설정들은 아래와 같습니다.

| Setting value              | Supported Platform | Mandatory(M) / Optional(O) |
| -------------------------- | ------------------ | -------------------------- |
| AppID | ALL | M | 
| AppVersion | ALL | M |
| StoreCode | ALL | M |
| bEnablePopup | ALL | O |
| bEnableLaunchingStatusPopup | ALL | O |
| bEnableBanPopup | ALL | O |
| bEnableGPGSSignInCheck | Android | O |

#### 1. AppID

Gamebase Console에 등록된 프로젝트 ID입니다.

[Game > Gamebase > 콘솔 사용 가이드 > 앱 > App](../oper-app.md#app)


#### 2. AppVersion

Gamebase Console에 등록한 클라이언트 버전입니다.

[Game > Gamebase > 콘솔 사용 가이드 > 앱 > Client](../oper-app.md#client)

#### 3. StoreCode

NHN Cloud 통합 인앱 결제 서비스인 IAP(In-App Purchase)를 초기화하기 위해 필요한 스토어 정보입니다.

| Store       | Code | GamebaseStoreCode | Description  |
| ----------- | ---- | ------------ | ------------ |
| App Store | AS | GamebaseStoreCode::AppStore | iOS에 한함 |
| Google Play | GG | GamebaseStoreCode::Google | Android, Windows에 한함 |
| One Store | ONESTORE | GamebaseStoreCode::OneStore | Android에 한함 |
| Galaxy Store | GALAXY | GamebaseStoreCode::Galaxy | Android에 한함 |
| Huawei AppGallery | HUAWEI | GamebaseStoreCode::Huawei | Android에 한함 |
| MyCard | MYCARD | GamebaseStoreCode::MyCard | Android에 한함 |
| Windows Custom | WIN | GamebaseStoreCode::Windows | Windows에 한함 |
| Epic Games Store | EPIC | GamebaseStoreCode::EpicGames | Windows에 한함 |
| Steam | STEAM | GamebaseStoreCode::Steam | Windows에 한함 |

#### 4. bEnablePopup

시스템 점검, 이용 제재(ban) 등 게임 유저가 게임을 플레이할 수 없는 상황에서 팝업 창 등으로 사유를 표시해야 할 때가 있습니다.
Gamebase에서 제공하는 기본 팝업 창을 사용할 것인지에 대한 설정입니다.

* true: enableLaunchingStatusPopup, enableBanPopup 설정에 따라 팝업 창 노출 여부가 결정됩니다.
* false: Gamebase에서 제공하는 모든 팝업 창이 노출되지 않습니다.
* 기본값: false

#### 5. bEnableLaunchingStatusPopup

LaunchingStatus가 게임을 할 수 없는 상태일 경우, Gamebase에서 제공하는 기본 팝업 창을 사용할 것인지에 대한 설정입니다.
LaunchingStatus는 아래 Launching 절 아래 State, Code 부분을 참고하십시오.

* 기본값: true

#### 6. bEnableBanPopup

로그인 시 해당 게임 유저가 이용 정지 상태인 경우, Gamebase에서 제공하는 기본 팝업 창을 사용할 것인지에 대한 설정입니다.

* 기본값: true

#### 7. bEnableGPGSSignInCheck

Android 플랫폼에서 'GPGS 자동 로그인' 기능 연동 시 유저에게 GPGS 로그인을 앱 설치 후 한번만 물어보는 설정입니다.

* true: 유저가 GPGS 로그인을 거부하더라도 Gamebase 초기화 때 GPGS 로그인 창을 다시 표시합니다.
* false: 앱 최초 실행 시에만 GPGS 로그인 창이 한번 표시됩니다.
* 기본값: true
