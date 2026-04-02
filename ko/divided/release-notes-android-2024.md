## Game > Gamebase > 릴리스 노트 > Android

### 2.68.0 (2024. 11. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.0/GamebaseSDK-Android.zip)

```
최소 지원 버전이 Android 5.0 이상으로 상향되었습니다.(minSdk 19 → 21)
```

#### 기능 추가
* Google Play 게임즈 서비스 계정을 통한 자동 로그인 연동 기능이 추가되었습니다.
    * 이 기능을 사용하려면 빌드 의존성에 **gamebase-adapter-auth-gpgs-autologin** 모듈 선언을 추가해야 합니다.

            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-auth-gpgs-autologin:$GAMEBASE_SDK_VERSION"
            }
            
    * 또한 다음 가이드 문서를 참고하여 추가 정보를 설정하세요.
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > GPGS IdP](./aos-started/#gpgs-idp)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.17.0)
* Google 인증 라이브러리가 업데이트되었습니다.
    * Google Sign-In for Android가 deprecated 되어 Google Credential Manager로 전환했습니다.
    * 인증 방법이 AuthCode 방식에서 OIDC 토큰 방식으로 변경되었습니다.
* 웹뷰에서 등록한 커스텀 스킴이 매칭되었을 때 URL을 리다이렉트하지 않도록 수정했습니다.

### 2.67.0 (2024. 10. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Steam 인증 어댑터가 추가되었습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.3)
* Twitter 인증 방식을 OAuth 2.0으로 변경하여, 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](./oper-app/#6-twitter)

#### 버그 수정
* 약관 팝업 창이 열려 있는 상태에서 네트워크 연결을 끊고 detail을 터치하면 약관 팝업 창이 종료되는 문제가 수정되었습니다.

### 2.66.3 (2024. 09. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.2)
    * Android 13 이상 특정 디바이스에서 간헐적으로 Native Crash 로그가 리포팅되지 않는 문제가 수정되었습니다.
    * Amazon 결제 재처리가 개선되었습니다.
    
### 2.66.2 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.1), Kakaogame SDK(3.19.3), PAYCO SDK(1.5.15)
* Amazon Appstore 결제 시 문제가 생겨 재처리가 동작할 때 처음 결제를 시도했던 User ID로 아이템을 지급하도록 하는 보완 로직이 추가되었습니다.
* Twitter 로그인 타이틀 바 색상과 이름이 변경되었습니다.
* 롤링 이미지 공지의 웹뷰 내부에서 오류가 발생한 경우 기존의 성공 콜백 호출 대신 실패 콜백이 호출되도록 수정했습니다.

#### 버그 수정
* Activity가 파괴되면 해당 Activity 위에 떠 있는 WebView가 닫히며 이 때 `close event callback`이 누락되는 오류가 수정되었습니다.
* Hangame 로그인 어댑터에서 외부 IdP 로그인 시 callback이 중복으로 오는 경우 `already resumed` 오류가 발생하지 않도록 방어 로직을 추가했습니다.

### 2.66.1 (2024. 07. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.1/GamebaseSDK-Android.zip)

#### 버그 수정
* targetSdk 34로 빌드했을 때 Android 14 단말기에서 `gamebase://dismiss` 스킴이 동작하지 않아 커스텀 스킴으로 웹뷰를 종료할 수 없는 이슈를 수정했습니다.

### 2.66.0 (2024. 07. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.0/GamebaseSDK-Android.zip)

#### 기능 추가
* GPGS v2 인증 추가
    * 설정 방법은 다음 가이드 문서를 참고하세요.
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > GPGS IdP](./aos-started/#gpgs-idp)

### 2.65.1 (2024. 06. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 표시할 이미지 공지가 없는 경우 오류 대신 성공 콜백이 호출되도록 변경하였습니다.

#### 버그 수정  
* 등록된 이미지 공지가 없는 경우 빈 공지 화면이 노출되고, 이때 '오늘은 그만 보기'를 체크한 뒤 화면을 닫으면 크래시가 발생되는 오류를 수정하였습니다.

### 2.65.0 (2024. 06. 11.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 이미지 공지 기능에 신규 타입이 추가되었습니다.
    * `롤링 팝업` 타입이 추가되었습니다.
    * 기존의 이미지 공지는 `개별 팝업` 타입으로 표기됩니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.0), Hangame Android SDK(1.13.0)
    * Google billing client version 6.2.1이 적용되었습니다.
    * Android OS 4.4(API Level 19) 단말기에서 결제하려면 추가 설정이 필요합니다.
        * 자세한 내용은 [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Root level build.gradle](./aos-started/#root-level-buildgradle) 가이드를 참고하시기 바랍니다.
* 내부 로직 개선

### 2.64.0 (2024. 05. 28.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.64.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Kakaogame SDK (3.19.0), PAYCO SDK (1.5.14)
* 약관 팝업이 열려 있는 상태에서 뒤로 가기 키(back key)가 동작하지 않도록 변경하였습니다.

#### 버그 수정
* API Level 23(OS 6.0, M) 이하 단말기에서 문자열 리소스 참조 실패로 Gamebase 내부 메시지가 정상 표시되지 않는 버그를 수정했습니다.

### 2.63.0 (2024. 04. 23.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.63.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 내부 로직 개선

### 2.62.1 (2024. 03. 29.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.1/GamebaseSDK-Android.zip)

#### 버그 수정
* Android 7.0(API Level 24) 미만 단말기에서 Gamebase.loginForLastLoggedInProvider 호출이 항상 실패하고 Guest 계정이 유실되는 버그를 수정했습니다.
    * 이 문제는 Gamebase Android SDK 2.62.0에서만 발생합니다.

### 2.62.0 (2024. 03. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 초기화 후 반환되는 LaunchingInfo VO에서 테스트 단말기임을 알 수 있도록 필드가 추가되었습니다.
    * **launchingInfo.user.testDevice**

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.9.0)
* Preference를 복사해서 사용할 수 없도록 내부 로직이 개선되었습니다.
* gamebase-sdk-base 모듈이 gamebase-sdk 단일 모듈로 통합되었습니다.

### 2.61.0 (2024. 02. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.61.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.8.4)
* Twitter callback URL 방식 로그인이 추가되었습니다.
* 고객 센터 사진 업로드 시 권한이 필요하지 않은 Photo Picker를 사용할 수 있도록 AndroidManifest에 선언을 추가하였습니다. 이에 따라 READ_EXTERNAL_STORAGE의 런타임 권한 요청이 제거되었습니다.
* 내부 로직 개선

### 2.60.0 (2024. 01. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.60.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO Android SDK(1.5.13)
* ONE store adapter 사용 시 필요한 queries 선언을 SDK 내부로 이동하였습니다.
* 내부 로직 개선

#### 버그 수정
* 앱 실행 시 간헐적으로 ConcurrentModifcationException 예외가 발생하는 문제를 수정했습니다.
