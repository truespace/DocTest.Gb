---
source: release-notes-android.md
section: "2.80.0 (2026. 02. 13.)-to-2.66.3 (2024. 09. 10.)"
order: 1
created_date: 2026-04-03
---

## Game > Gamebase > 릴리스 노트 > Android

### 2.80.0 (2026. 02. 13.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.80.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 결제 요청 시 느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우, 신규로 추가된 **PURCHASE_PENDING(4008)** 오류가 발생합니다.
* Gamebase Event Handler의 GamebaseEventCategory.PURCHASE_UPDATED 이벤트 기능이 확장되었습니다.
    * 앱이 실행 중일 때 GamebaseEventHandler를 통해 Pending 결제(느린 결제, 부모 동의 등) 완료 이벤트를 제공 받을 수 있습니다.

#### 버그 수정

* 약관 창 사이즈가 간헐적으로 크게 보이는 이슈 수정
* 난독화 적용 시 알림 권한 자동 요청 팝업이 표시되지 않는 이슈 수정

### 2.79.0 (2026. 01. 27.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.79.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* targetSdk 36 빌드를 Android 16 단말기에서 실행 시 뒤로 가기가 정상 작동하지 않고 웹뷰가 그대로 닫히거나 앱이 종료되는 현상을 수정했습니다.
* 내부 로직 개선

### 2.78.0 (2025. 12. 23.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.78.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: Play Age Signals 라이브러리(0.0.2)
    * Play Age Signals 라이브러리가 업데이트되었습니다.

### 2.77.0 (2025. 12. 09.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.77.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 결제 관련 내부 로직 개선

### 2.76.0 (2025. 11. 28.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.76.0/GamebaseSDK-Android.zip)

#### 기능 추가

* 미국 텍사스, 유타, 루이지애나와 같은 관할권의 특정 연령 확인 법률에 따른 준수 의무를 충족하는 데 도움이 되도록 Google Play Age Signals 기반의 연령 확인 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Age Signals Support](../../aos-etc.md#age-signals-support)
    * Play Age Signals 라이브러리 버전이 베타(0.0.1-beta02) 상태이므로 API는 항상 예외가 발생합니다.
        * 정상 동작을 위해서는 Play Age Signals 라이브러리 0.0.2 버전이 적용된 Gamebase Android SDK 2.78.0을 사용하세요.

#### 기능 개선/변경

* **Gamebase.Purchase.requestItemListAtIAPConsole()** API가 deprecated되었습니다.
    * **Gamebase.Purchase.requestItemListPurchasable()** API를 사용하세요.

### 2.75.1 (2025. 10. 17.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: Hangame Android SDK(1.17.3)
* 내부 로직 개선

### 2.75.0 (2025. 09. 23.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.75.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
 
* 외부 SDK 업데이트: NHN Cloud Android SDK(1.12.0), PAYCO Android SDK(1.5.17), Weibo Android SDK(13.10.5)
* Google Play의 16KB 페이지 제약 대응을 위한 외부 SDK 업데이트
    * NHN Cloud SDK / Weibo SDK 업데이트
    * 16KB 미대응 gamebase-adapter-auth-weibo-v4 모듈 제거
* 미사용 모듈 제거
    * gamebase-adapter-purchase-amazon, gamebase-adapter-push-adm
* 내부 로직 개선

### 2.73.1 (2025. 08. 12.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: Facebook Android SDK (18.0.0)
* 내부 로직 개선

#### 버그 수정

* AGP 8.5로 빌드 시 네이버 로그인이 실패하는 이슈를 수정하였습니다.
* 펀치홀이 있는 단말기에서 약관 > 더보기 실행 시 대화상자가 단말기 화면보다 커지는 문제를 수정했습니다.

### 2.73.0 (2025. 07. 15.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.0/GamebaseSDK-Android.zip)

```
최소 지원 버전이 Android 5.1 이상으로 상향되었습니다.(minSdk 21 → 22)
Android Gradle Plugin 최소 버전이 7.4.2 이상으로 상향되었습니다.(4.0.1 → 7.4.2)
```

#### 기능 개선/변경

* 내부 로직 개선

#### 버그 수정

* 로그인 웹뷰에서 화면 회전 시 여백 크기를 잘못 계산하는 오류를 수정했습니다.

### 2.72.0 (2025. 06. 24.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 웹소켓 모듈이 중복 호출되는 경우 ArrayIndexOutOfBoundsException이 발생할 수 있는 로직을 수정했습니다.
    * 이 문제는 Gamebase Android SDK 2.71.2에서만 발생합니다.

#### 버그 수정

* LINE IdP의 Region 추가 정보 대응이 되지 않아 매핑 관련 동작에서 발생하는 문제를 수정했습니다.
    * Gamebase.login("guest") -&gt; Gamebase.addMapping("line") -&gt; Gamebase.loginForLastLoggedInProvider() 호출 실패 이슈
    * Gamebase.login(idp) -&gt; Gamebase.addMapping("line") -&gt; AUTH\_ADD\_MAPPING\_ALREADY\_MAPPED\_TO\_OTHER\_MEMBER(3302) -&gt; Gamebase.changeLogin(ForcingMappingTicket) 호출 실패 이슈
    * Gamebase.login("line") -&gt; Gamebase.addMapping(idP) -&gt; AUTH\_ADD\_MAPPING\_ALREADY\_MAPPED\_TO\_OTHER\_MEMBER(3302) -&gt; Gamebase.changeLogin(ForcingMappingTicket) 호출 실패 이슈

### 2.71.2 (2025. 05. 20.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: Hangame Android SDK(1.17.2)
* 구버전 Google Play Service가 설치된 단말기에서 Sign-in with Google 로그인 지원
* 내부 로직 개선

### 2.71.1 (2025. 04. 29.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.1/GamebaseSDK-Android.zip)

#### 버그 수정

* 웹뷰 크기 계산 관련 오류를 수정하였습니다.

### 2.71.0 (2025. 04. 15.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-Android.zip)

#### 기능 추가

* '게임 공지' 신규 기능이 추가되었습니다.
    * Gamebase.GameNotice.openGameNotice(Activity activity, GamebaseCallback onCloseCallback);
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Android SDK 사용 가이드 > UI > GameNotice](../../aos-ui.md#gamenotice)

#### 기능 개선/변경

* storeCode를 null로 설정하여 Gamebase 초기화를 호출했을 때 예외가 발생하는 대신 **INVALID_PARAMETER(3)** 에러를 리턴하도록 동작을 변경했습니다.

### 2.70.1 (2025. 03. 13.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.1/GamebaseSDK-Android.zip)

#### 버그 수정

* Apple ID, Steam, Twitter 로그인 내비게이션 바의 X 버튼 사이즈를 재조정했습니다.
* Kotlin 파일에서 AuthProvider의 IdP constant(예: AuthProvider.GUEST 등)를 참조할 수 없는 문제를 수정했습니다.

### 2.70.0 (2025. 03. 11.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.0/GamebaseSDK-Android.zip)

#### 기능 추가

* 외부 SDK 업데이트: NHN Cloud SDK(1.9.5)
    * Google Play Billing Library 7.1.1이 적용되었습니다.
    * Android 7.0(API Level 24) 미만 단말기에서 결제를 시도하는 경우 Google Play Billing Library에서 크래시가 발생합니다.
        * 이 문제를 해결하기 위해서는 Gradle에 하위 OS를 위한 [Java 8+ API 디슈가링 지원](https://developer.android.com/studio/write/java8-support#library-desugaring) 선언을 추가해야 합니다.
        * 앱 모듈의 Gradle, Unity의 경우 launcherTemplate.gradle에 다음 선언을 추가하세요.
        
                android {
                    compileOptions {
                        // Flag to enable support for the new language APIs
                        coreLibraryDesugaringEnabled true
                    }
                }

                dependencies {
                    // desugar_jdk_libs 2.+ needs AGP 7.4+
                    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.1.5")
                }
        
        * desugar_jdk_libs 1.x 버전은 Kakaogame 로그인 시 크래시가 발생하므로 2.x 버전 적용을 권장합니다.
            * Unity Editor 버전에 따라 AGP 버전이 다르므로 AGP 및 Gradle 버전 업데이트가 필요할 수 있습니다.
* 'GPGS 자동 로그인' 기능 연동 시 유저에게 GPGS 로그인을 앱 설치 후 한번만 물어보는 초기화 옵션을 추가했습니다.
    * **GamebaseConfiguration.Builder.enableGPGSSignInCheck(boolean)**
    * 기본 설정은 true로, 유저가 GPGS 로그인을 거부하더라도 Gamebase 초기화 때 GPGS 로그인 창을 다시 표시합니다.
    * false로 설정하면 앱 최초 실행 시에만 GPGS 로그인 창이 한번 표시됩니다.
* 로그인 시 IdP 서버로부터 오류가 발생했음을 나타내는 신규 오류 코드가 추가되었습니다.
    * AUTH_AUTHENTICATION_SERVER_ERROR(3012)
* GamebaseWebView에 내비게이션 바 타이틀과 아이콘 틴트 컬러 설정 옵션을 추가했습니다.
    * **GamebaseWebViewConfiguration.Builder.setNavigationBarTitleColor(int)**
    * **GamebaseWebViewConfiguration.Builder.setNavigationBarIconTintColor(int)**

#### 기능 개선/변경

* 'GPGS 자동 로그인' 기능 연동시 유저가 GPGS 로그인을 하지 않으면 Gamebase 초기화, 로그인, 로그아웃 시 GPGS 로그인을 계속 시도하던 동작을 Gamebase 초기화 때만 시도하도록 변경했습니다.
* Apple ID, Steam, Twitter 로그인 내비게이션 바에 타이틀과 같은 색으로 X 버튼을 표시하도록 변경했습니다.

#### 버그 수정

* LaunchingInfo data가 유저 Event Handler에서 업데이트되지 않는 이슈를 수정했습니다.
* Unity 빌드에서 이미지 공지 비율이 원본 이미지 비율과 다르게 표시되는 문제를 수정했습니다.

### 2.69.0 (2025. 01. 21.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-Android.zip)

#### 기능 추가

* **Gamebase.requestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;) 비동기 API**를 추가했습니다.
    * **Gamebase.getLastLoggedInProvider() 동기 API**가 타이밍상 정상적인 값을 반환하지 못할 때가 있습니다.
    * **gamebase-adapter-auth-gpgs-autologin** 모듈을 빌드에 포함하는 경우 GPGS 서버에서 데이터를 획득하는 시간이 필요하므로 Gamebase 초기화 직후 getLastLoggedInProvider() 동기 API를 호출하면 정상적인 값을 획득할 수 없습니다.
    * 이때 requestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;) 비동기 API는 정확한 값을 보장합니다.
    * gamebase-adapter-auth-gpgs-autologin 모듈이 빌드에 포함되지 않은 경우에는 계속해서 getLastLoggedInProvider() 동기 API를 사용해도 무방합니다.
* **GamebaseWebViewConfiguration.Builder.setCutoutAreaColor() API**를 추가했습니다.
    * GamebaseWebView의 **GamebaseWebViewConfiguration.Builder.renderOutsideSafeArea() API**를 **false**로 설정한 경우, cutout 영역에 자동으로 padding 여백을 추가합니다.
    * setCutoutAreaColor()는 이렇게 추가된 padding 영역의 색을 설정할 수 있습니다.
    * renderOutsideSafeArea()를 false로 설정했지만 setCutoutAreaColor()는 설정하지 않는 경우에는 웹 페이지 'body'의 'background-color' 값으로 자동으로 padding 영역의 색상을 결정합니다.

#### 기능 개선/변경

* **gamebase-adapter-auth-gpgs-autologin** 모듈을 빌드에 포함하는 경우 Gamebase 초기화와 동시에 **Gamebase.getLastLoggedInProvider() 동기 API**를 호출하면 내부 데이터가 초기화가 완료되지 않아 null이 반환되었으나, 이 경우 **'NOT\_INITIALIZED\_YET'**이라는 문자열을 반환하도록 내부 로직을 변경했습니다.
* **GamebaseWebViewConfiguration.Builder.renderOutsideSafeArea() API**를 **false**로 설정한 경우에도 cutout 영역까지 웹뷰를 모두 표시하도록(**edge-to-edge**) 내부 로직을 변경했습니다.
    * 그 대신 자동으로 padding 여백을 추가하여 콘텐츠가 가려지지 않도록 했습니다.

#### 버그 수정
 
* 로그인 전에 Gamebase.Push.getNotificationOptions() API를 호출하는 경우 크래시가 발생하지 않도록 수정했습니다.
* Loading Progress가 간헐적으로 사라지지 않거나 크래시가 발생하는 이슈에 대한 방어 코드를 추가했습니다.
* WebSocket에서 간헐적으로 내부 콜백 함수가 중복으로 호출되어 발생하는 크래시에 대한 방어 코드를 추가했습니다.

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
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > GPGS IdP](../../aos-started.md#gpgs-idp)

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
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](../../oper-app.md#6-twitter)

#### 버그 수정
* 약관 팝업 창이 열려 있는 상태에서 네트워크 연결을 끊고 detail을 터치하면 약관 팝업 창이 종료되는 문제가 수정되었습니다.

### 2.66.3 (2024. 09. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.2)
    * Android 13 이상 특정 디바이스에서 간헐적으로 Native Crash 로그가 리포팅되지 않는 문제가 수정되었습니다.
    * Amazon 결제 재처리가 개선되었습니다.
