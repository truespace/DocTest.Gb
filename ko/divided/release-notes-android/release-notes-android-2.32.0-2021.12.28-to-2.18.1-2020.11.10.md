---
source: release-notes-android.md
section: "2.32.0 (2021.12.28)-to-2.18.1 (2020.11.10)"
order: 4
created_date: 2026-04-03
---

### 2.32.0 (2021.12.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.0/GamebaseSDK-Android.zip)

#### 기능 추가
* GamebaseEventHandler의 GamebaseEventCategory에 **GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED** 타입이 추가되었습니다.
    * 이 이벤트의 활용 방법은 다음 문서를 참고하시기 바랍니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../../aos-etc.md#server-push)
* Gamebase Access Token이 만료되어 로그인이 필요할 때 동작하는 **GamebaseEventCategory.LOGGED_OUT** GamebaseEventHandler category가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../../aos-etc.md#logged-out)

#### 기능 개선/변경
* 웹뷰 URL이 **onestore://**로 시작하는 ONE store 딥링크가 동작하도록 웹뷰를 개선했습니다.

#### 버그 수정
* Gamebase Android SDK 2.31.0에서 로그아웃을 호출해도 IdP 로그아웃은 호출되지 않아 IdP 계정을 변경할 수 없는 버그를 수정했습니다.

### 2.31.0 (2021.12.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.31.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Amazon 스토어가 추가되었습니다.
    * **STORE_CODE**는 **AMAZON**입니다.
    * 스토어 설정 방법은 다음 가이드를 확인하시기 바랍니다.
        * [Game > Gamebase > 스토어 콘솔 가이드 > Amazon 콘솔 가이드](../../console-amazon-guide.md)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Define Adapters](../../aos-started.md#define-adapters)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Android 11](../../aos-started.md#android-11)
* Huawei 스토어가 추가되었습니다.
    * **STORE_CODE**는 **HUAWEI**입니다.
    * 스토어 설정 방법은 다음 가이드를 확인하시기 바랍니다.
        * [Game > Gamebase > 스토어 콘솔 가이드 > Huawei 콘솔 가이드](../../console-huawei-guide.md)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Define Adapters](../../aos-started.md#define-adapters)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Resources > Huawei Store](../../aos-started.md#resources)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.29.0)
* 이용 정지 웹뷰 내의 고객 센터 링크에서 이용 정지 유저 정보로 문의를 등록할 수 없는 문제를 해결하였습니다.
* 앱이 켜지자마자 Gamebase 초기화를 호출하는 경우, 론칭 팝업 창이 간헐적으로 영어로 표시되는 문제를 수정하였습니다.
* 앱이 백그라운드에서 포그라운드로 전환될 때는 항상 론칭 정보가 변경되지 않았는지 바로 체크하도록 스케줄러를 개선하였습니다.

### 2.30.0 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Mapping > Add Mapping Forcibly](../../aos-authentication.md#add-mapping-forcibly)
* Gamebase.addMapping() 호출 후 AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302) 에러가 발생했을 때, 해당 계정으로 로그인을 할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Mapping > Change Login with ForcingMappingTicket](../../aos-authentication.md#change-login-with-forcingmappingticket)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.4.2)
* Gamebase가 기본으로 제공하는 점검 상세보기 웹뷰 html을 사용자가 수정해서 사용할 수 있도록 개선하였습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 초기화 > Launching Information > 1. Launching > 1.3 Maintenance > Change Default Maintenance HTML](../../aos-initialization.md#change-default-maintenance-html)
* DisplayLanguageCode를 설정했음에도 기본 점검 웹뷰의 시간이 단말기 언어로 표시되는 오류를 수정하였습니다.
* 통신 오류 발생 시, 끊긴 커넥션으로 통신을 시도함으로 인해 반복적으로 발생하던 네트워크 오류를 개선하였습니다.

### 2.29.0 (2021.11.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.29.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Google 로그인시 Scope를 선언할 수 있는 기능을 추가하였습니다.
    * [https://developers.google.com/identity/protocols/oauth2/scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    * Scope로 **email**을 추가하면 프로필에서 Email 정보 획득이 가능합니다.
    * Scope는 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하면 로그인시 자동으로 설정됩니다.

```
{"scope":["email","myscope1","myscope2",...]}
```

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.27.4)
* DisplayLanguage 가이드 문서에서만 안내되고, 실제로 SDK에는 포함되어 있지 않았던 DisplayLanguage.Code 클래스를 추가하였습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Display Language > Gamebase에서 지원하는 언어코드의 종류](../../aos-etc.md#gamebase)

### 2.28.0 (2021.09.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.28.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Kakaogame 인증 추가
* '결제 어뷰징 자동 해제' 기능이 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > GraceBan](../../aos-authentication.md#graceban)
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용 정지가 됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 AuthToken.getGraceBanInfo() API 값을 확인하고, null이 아닌 유효한 GraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.
* 로그인 응답 대기중에 대기 아이콘이 표시됩니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO Android SDK(1.5.6)

### 2.27.1 (2021.09.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO Android SDK(1.5.5), Hangame Android SDK(1.4.1), Weibo Android SDK(11.8.1)
* 에뮬레이터, 루팅 단말기에서 웹뷰가 정상적으로 표시되지 않을 때 재시도를 추가하여, 웹뷰가 정상적으로 표시되도록 개선하였습니다.
    * 대상은 웹뷰로 동작하는 이미지공지, 고객 센터, 공통 약관이 해당됩니다.
* Weibo IdP 인증을 개선하여 안정성을 향상시켰습니다.
    * 동기 API 이지만 실제로는 비동기로 동작하여 에러를 발생시키는 API에 예외 처리, 대기, 재시도 등을 추가였습니다.

#### 버그 수정
* '등록되지 않은 게임 버전' 에러 팝업 창이 영어로만 표시되는 버그를 수정하였습니다.
* 점검 팝업 창에 중국어가 표시되지 않는 버그를 수정하였습니다.
* [Credential Login](../../aos-authentication.md#login-with-credential) 을 한 경우, [Login as the Latest Login IdP](../../aos-authentication.md#login-as-the-latest-login-idp) 호출이 항상 실패하는 버그를 수정하였습니다.

### 2.27.0 (2021.08.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.27.1)
* ONE store V16 스토어 추가

### 2.26.0 (2021.08.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.26.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* Display Language 기능이 개선되었습니다.
    * 지금까지는 언어셋을 추가하기 위해 gamebase-sdk-base-version.aar 파일을 직접 수정해야 했습니다.
        * 이제 프로젝트의 res/raw 폴더에 localizedstring.json 파일을 추가하면 되도록 개선하였습니다.
    * 지금까지는 Unity 가이드의 Display Language 언어셋 추가 방법은 Android에 적용할 수 없었습니다.
        * 이제 Unity 가이드에 따라 localizedstring.json 파일을 추가하더라도 Android 빌드에 반영되도록 개선하였습니다.
        * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Display Language > 신규 언어셋 추가](../../unity-etc.md#add-new-language-sets)
    * Display Language 언어셋에 중국어 간체(zh-CN), 중국어 번체(zh-TW), 태국어(th)가 추가되었습니다.
    * 기본 언어코드가 **en** 이었으나, Gamebase 콘솔에서 설정한 기본언어가 반영되도록 개선하였습니다.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > App > 언어 설정](../../oper-app.md#language-settings)
* showTermsView API 호출 후 생성할 수 있는 PushConfiguration 객체의 생성 기준이 다음과 같이 변경되었습니다.
    * 변경 전
        * 약관 항목 중에 **Push 수신** 항목이 존재하는 경우에만 null이 아닌 유효한 PushConfiguration이 반환되었습니다.
        * 유저가 주간, 야간 홍보성 Push 수신에 모두 거부한 경우 PushConfiguration.pushEnabled는 false로 생성되었습니다.
    * 변경 후
        * 약관 UI가 표시되었다면 항상 null이 아닌 유효한 PushConfiguration이 반환됩니다.
        * showTermsView가 반환하는 PushConfiguration 객체의 pushEnabled 값은 항상 true입니다.
    * 변경되지 않고 동일한 점
        * 이미 약관에 동의하여 약관 UI가 표시되지 않았다면 PushConfiguration은 null로 반환됩니다.

#### 버그 수정
* Push 언어 설정은 별다른 보조 처리가 없이 단말기의 언어코드를 그대로 적용되어, Push 콘솔에서 전송한 메시지의 언어코드가 일치하지 않는 문제를 수정하였습니다.

### 2.25.0 (2021.07.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.25.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 월 결제 한도 기능 추가
    * 월 결제 한도를 넘는 경우 **PURCHASE_LIMIT_EXCEEDED(4007)** 에러가 발생합니다.

#### 기능 개선/변경
* Android Support Library 의존성을 AndroidX 로 변경
* Push 항목이 존재하는 약관에서 PushConfiguration 객체 보장
    * 약관 UI에서 Push 수신 동의를 하지 않을 경우 Gamebase.Terms.showTermsView API 호출 결과로 생성되는 PushConfiguration이 null이었으나, 약관에 Push 항목이 존재한다면 PushConfiguration 객체가 항상 반환되도록 변경되었습니다.
    * Push 수신 거부 시 PushConfiguration 객체는 (푸시 동의 여부 = false, 광고성 푸시 동의 여부 = false, 야간 광고성 푸시 동의 여부 = false) 로 생성됩니다.
    * 약관에 Push 항목이 존재하지 않는다면 PushConfiguration 객체는 null입니다.
* 외부 SDK 업데이트
    * TOAST Android SDK(0.26.0)
    * Kotlin(1.5.21)
    * Google Play Services Auth(19.0.0)
    * Facebook Android SDK(11.1.0)
    * NAVER Android SDK(4.4.1)
    * LINE Android SDK(5.6.2)
    * Weibo Android SDK(11.6.0)
* Weibo 로그인시 발생하는 크래시 수정

### 2.24.0 (2021.06.29) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.24.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 내부 론칭 URL 변경
* SDK 첨부 문서에 잘못 작성된 문구 수정

### 2.23.0 (2021.06.14) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.23.0/GamebaseSDK-Android.zip)

#### 버그 수정
* 이용 정지 자세히 보기 웹뷰의 제목이 표시되지 않는 문제 수정

### 2.22.0 (2021.05.25) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.22.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.25.0), Hangame Android SDK(1.4.0)

#### 버그 수정
* 로그아웃 후 다른 유저 ID로 로그인했을 때 간헐적으로 Google Play 스토어 결제가 성공했음에도 실패가 반환되는 오류 수정
* 앱 패키지 이름에 대문자가 포함된 경우 Sign In with Apple 로그인이 실패하는 오류 수정

### 2.21.1 (2021.04.19) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.21.1/GamebaseSDK-Android.zip)

#### 버그 수정
* Hangame 로그인을 PAYCO로 진행하다 취소하면 크래시가 발생하는 문제 수정

### 2.21.0 (2021.04.13) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.21.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Hangame 일본 인증 추가     

#### 기능 개선/변경
* 외부 SDK 업데이트: Facebook Android SDK(6.5.1), LINE Android SDK(5.4.0)

#### 버그 수정
* Proguard를 적용한 빌드에서 결제 API 호출 시 크래시가 발생하는 오류 수정

### 2.20.2 (2021.03.30) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* Google Play 스토어의 Android 11 단말기에서의 결제 오류가 해결된 Billing Client 3.0.3 버전으로 업데이트

### 2.20.1 (2021.02.23) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.1/GamebaseSDK-Android.zip)

#### 버그 수정
* push-fcm 모듈 초기화 중 크래시가 발생할 수 있는 로직을 수정

### 2.20.0 (2021.02.09) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 공통 약관 기능 추가
    * 약관 웹뷰를 여는 API 추가
    * 약관 리스트 및 유저별 동의 여부를 조회하는 API 추가
    * 유저별 약관 동의 여부를 Gamebase 서버에 저장하는 API 추가

#### 기능 개선/변경
* 고객 센터 타입이 TOAST 조직 상품(Online Contact)인 경우 로그인을 하지 않아도 고객 센터가 표시되도록 변경

### 2.19.1 (2020.12.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.1/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.19.0
    * (공통) Weibo 인증 추가
    * (Android) Sign In with Apple 인증 추가
    
#### 기능 개선/변경
* [SDK] 2.19.0
    * (공통) 론칭 상태 코드 추가: 베타 서비스(205)

#### 버그 수정
* [SDK] 2.19.1
    * (Android) Weibo 로그인 시도 후 다른 IdP로 로그인 시 크래시가 발생하는 문제 수정
    
### 2.18.2 (2020.12.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.2/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 고객 센터 페이지 오픈 시 게임에서 정의한 extra data 전달: SDK 2.18.2
    * [Console] 고객 센터 > 고객 문의: 고객 문의 상세 조회 화면에서 추가로 등록한 extra data 확인 가능
* [SDK] 2.18.2
    * (공통) 개발사 자체 고객 센터 오픈 시 additionalURL 필드 추가
    * (공통) 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경
* [SDK] 2.18.2
    * (공통) TOAST SDK 업데이트: Android(0.24.2), iOS(0.27.1), Unity(0.21.3)
    * (Android) 암호화 로직 보안 경고 해결을 위한 외부 SDK 업데이트: PAYCO Login SDK(1.5.3), Hangame ID SDK(1.3.2)
    * (Android) Tencent Push 모듈 제거
    * (Android) Gamebase Android SDK 2.6.0에서 deprecated된 함수 제거
        * GamebaseConfiguration.Builder.setFCMSenderId()
        * GamebaseConfiguration.Builder.setTencentAccessKey()
        * GamebaseConfiguration.Builder.setTencentAccessId()

#### 버그 수정
* [SDK] 2.18.2
    * (Android) 5.0~6.0 OS 단말기에서 웹뷰 커스텀 스킴이 동작하지 않는 문제 수정

### 2.18.1 (2020.11.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.1/GamebaseSDK-Android.zip)

#### 기능 추가
* Galaxy 스토어 추가: SDK 2.18.0

#### 기능 개선/변경
* [SDK] 2.18.0
    * (Android) TOAST SDK 업데이트: Android(0.24.1) - GooglePlay Billing Library v.3.0.1 적용
    * (Android) WebView SSL 보안 경고 대응 처리 추가

#### 버그 수정
* [SDK] 2.18.1
    * (Android) 2.18.0 에서 Google 결제 후 크래시가 발생하는 문제 수정
