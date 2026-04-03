---
source: release-notes-android.md
section: "2.66.2 (2024. 08. 27.)-to-2.46.0 (2023. 01. 31.)"
order: 2
created_date: 2026-04-03
---

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
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > GPGS IdP](../../aos-started.md#gpgs-idp)

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
        * 자세한 내용은 [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Root level build.gradle](../../aos-started.md#root-level-buildgradle) 가이드를 참고하시기 바랍니다.
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

### 2.59.0 (2023. 12. 19.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.59.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.7.2)
* 내부 로직 개선

#### 버그 수정
* 고객 센터에서 .wav 형식 파일이 업로드되지 않는 문제를 수정했습니다.

### 2.58.0 (2023. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.58.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Kakaogame Android SDK(3.17.5)
* Twitter API 서버 인증서 갱신으로 인해 Twitter Adapter minSdkVersion을 21로 상향
* 내부 로직 개선

#### 버그 수정
* Gamebase.Logger.report(String message, ...) API의 message에 빈 문자열을 넣어도 크래시가 발생하지 않도록 방어 코드를 추가했습니다.

### 2.57.0 (2023. 10. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.57.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Naver Login Android SDK(5.8.0)

#### 기능 추가
* Exception을 Log & Crash Search로 전송할 수 있는 API가 추가되었습니다.

        Gamebase.Logger.report(String message, Throwable throwable);
        Gamebase.Logger.report(String message, Throwable throwable, Map<String, String> userFields);

#### 버그 수정
* Gamebase WebView close() 시에 간헐적으로 EmptyStackException이 발생하는 버그를 수정했습니다.

### 2.56.1 (2023. 10. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.56.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Android SDK (1.8.0)
    * Google billing client version 5.2.1 버전이 적용되었습니다.
    * 2023/11/01 이후 Google Play Store에 신규 및 앱 업데이트 시 해당 버전 적용이 반드시 필요합니다. 자세한 내용은 다음 링크를 참고 부탁드립니다.
    * [Google Play 결제 라이브러리 버전 지원 중단](https://developer.android.com/google/play/billing/deprecation-faq?hl=ko)

### 2.56.0 (2023. 09. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.56.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK (1.7.1)

### 2.55.0 (2023. 09. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.55.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Naver Login Android SDK(5.7.0), NHN Cloud Android SDK(1.7.1)
* 구버전 Naver Login SDK의 OAuthLoginInAppBrowserActivity에서 발생하던 Cross-app Scripting 취약점이 해결되었습니다.
* Naver IdP 사용 시 Naver IdP에서 지원하지 않는 API 21 미만 단말기에서도 크래시가 발생하지 않도록 방어 로직을 추가했습니다.

#### 버그 수정
* IdP Login 시 로딩 애니메이션 off가 적용되지 않는 현상이 수정되었습니다.
* API Level 28, 29 전체 화면 웹뷰에서 windowFocus가 변경되면 내비게이션 바가 다시 생겨나는 이슈가 수정되었습니다.
* Weibo 로그인에 성공했지만 간헐적으로 Weibo SDK에서 access token이 null로 리턴되는 경우 크래시가 발생하지 않도록 방어 로직을 추가했습니다.

### 2.53.0 (2023. 08. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.53.0/GamebaseSDK-Android.zip)

#### 기능 추가
* loginForLastLoggedInProvider 호출 중에 로딩 애니메이션을 숨기는 옵션을 지정할 수 있는 신규 API가 추가되었습니다.
    * Gamebase.loginForLastLoggedInProvider(Activity activity, Map&lt;String, Object&gt; additionalInfo, GamebaseDataCallback&lt;AuthToken&gt; callback);
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Login > Login Flow > Login as the Latest Login IdP](../../aos-authentication.md#login-as-the-latest-login-idp)

#### 기능 개선/변경
* 외부 SDK 업데이트: Facebook Android SDK(16.1.2), Line Android SDK(5.8.1), Weibo Android SDK(13.5.0)
* 고객 센터 웹뷰에서 파일을 첨부할 때 앨범, 카메라, 저장소 타입에 따라 자동으로 권한을 획득하고 타입에 맞는 기능을 실행하도록 개선되었습니다.
    * '고객 센터'의 개선된 파일 첨부 기능을 사용하려면 아래 가이드에 따라 AndroidManifest.xml에 권한 설정을 추가해야 합니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Contact](../../aos-started.md#contact)

### 2.52.1 (2023. 07. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 버전 변경: OkHttp 3.12.13(4.10.0에서 다운그레이드)

#### 버그 수정
* OkHttp 3.13부터 최소 지원 OS 버전이 21로 올라, Android 4.4(OS 19 Kitkat) 단말기에서 크래시가 발생하는 이슈를 수정했습니다.

### 2.52.0 (2023. 06. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.0/GamebaseSDK-Android.zip)

#### 기능 추가
* ONE store v21 Adapter가 추가되었습니다.
* 특정 메시지가 포함된 알림을 표시하지 않는 커스텀 푸시 리시버가 추가되었습니다.
    * 이 기능을 사용하려면 빌드 의존성에 **gamebase-adapter-push-notification** 모듈 선언을 추가해야 합니다.

            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-push-notification:$GAMEBASE_SDK_VERSION"
            }

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK 업데이트 1.6.0

#### 버그 수정
* Render outside safe area 가로 모드에서 내비게이션 바와 X 버튼이 겹쳐 보이는 오류를 수정했습니다.
* 약관 팝업에서 '더보기'를 클릭했을 때 약관 전문이 완전히 로딩되기 전에는 백그라운드를 클릭할 수 없도록 수정했습니다.

### 2.50.1 (2023. 07. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.50.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 버전 변경: OkHttp 3.12.13(4.10.0에서 다운그레이드)

#### 버그 수정
* OkHttp 3.13부터 최소 지원 OS 버전이 21로 올라, Android 4.4(OS 19 Kitkat) 단말기에서 크래시가 발생하는 이슈를 수정했습니다.

### 2.50.0 (2023. 05. 16.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.50.0/GamebaseSDK-Android.zip)

#### 기능 추가
* MyCard Adapter가 추가되었습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Android SDK 1.5.0, Gson 2.8.9, OkHttp 4.10.0, PAYCO Android SDK 1.5.12

#### 버그 수정
* 약관 API 호출 시 Activity 사이즈가 safe area 내로 줄어드는 오류를 수정했습니다.

### 2.49.0 (2023. 04. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-Android.zip)

```
최소 지원 버전이 Android 4.4 이상으로 상향되었습니다.(minSdk 16 -> 19)
```

#### 기능 개선/변경
* 내부 지표 개선

#### 버그 수정
* 다음 adapter를 빌드에 포함하는 경우 불필요한 READ_PHONE_STATE 권한이 추가되는 버그를 수정했습니다.
    * gamebase-adapter-auth-facebook
    * gamebase-adapter-auth-hangame
    * gamebase-adapter-auth-line
    * gamebase-adapter-purchase-google
    * gamebase-adapter-purchase-onestore
    * gamebase-adapter-purchase-onestore-external
    * gamebase-adapter-purchase-onestore-v16
    * gamebase-adapter-purchase-onestore-v19
    * gamebase-adapter-push-adm
    * gamebase-adapter-push-fcm

### 2.48.0 (2023. 03. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.48.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Android SDK(1.4.2), PAYCO Android SDK(1.5.11)
* DNS 장애를 대비한 Gamebase 서버 예비 도메인 적용
* 내부 로직 개선

#### 버그 수정
* Unity에서 proguard 적용 시 Purchase 관련 API 호출에 실패하는 버그를 수정하였습니다.

### 2.47.0 (2023. 02. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.47.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK (1.6.3)
* 내부 로직 개선

### 2.46.0 (2023. 01. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.46.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 구독 상태를 조회할 수 있는 API가 추가되었습니다.
    * Gamebase.Purchase.requestSubscriptionsStatus(Activity, PurchasableConfiguration, GamebaseDataCallback&lt;List&lt;PurchasableSubscriptionStatus&gt;&gt;)
    * PurchasableConfiguration.Builder.setIncludeExpiredSubscriptions(boolean) API로 만료된 구독 상태도 조회할 수 있습니다.
* 웹뷰에서 SafeArea를 무시하고 Cutout 영역에도 렌더링할 수 있는 옵션을 추가했습니다.
    * GamebaseWebViewConfiguration.Builder.setRenderOutsideSafeArea(boolean)

#### 기능 개선/변경
* 외부 SDK 업데이트: Kakaogame SDK (3.14.14)
