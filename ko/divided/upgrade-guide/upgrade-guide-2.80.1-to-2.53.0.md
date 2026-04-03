---
source: upgrade-guide.md
section: "2.80.1-to-2.53.0"
order: 1
created_date: 2026-04-03
---

## Game > Gamebase > Upgrade Guide

## 2.80.1

### Unity

* Auth.AuthToken의 extraParams 타입이 Dictionary&lt;string, string&gt;에서 Dictionary&lt;string, object&gt;로 변경되었습니다.

## 2.80.0

### iOS

* Xcode 최소 지원 버전이 16.0에서 26.0으로 변경되었습니다.
* **+[TCGBPurchase setPromotionIAPHandler:]** API가 deprecated되었습니다.

### Unreal

* (iOS) Project Settings에서 활성화한 기능에 따라 Info.plist에 필요한 항목이 자동으로 추가됩니다.
    * `AdditionalPlistData`로 직접 관리하려면 [iOS Settings](../../unreal-started.md#ios-settings)에서 **Disable Auto Info.plist Update**를 활성화하세요.

## 2.79.0

### iOS

* **+[TCGBConfiguration setStoreCode:]** API가 deprecated되었습니다.
* **-[TCGBPurchase setStoreCode:]** API가 deprecated되었습니다.
* **TCGBPurchase.storeCode** API가 deprecated되었습니다.

## 2.77.0

### Common

* Apple 계정을 revoke했을 때 발생하는 GamebaseEventHandler의 IdP Revoked 이벤트의 권장 가이드를 변경하였습니다.
    * 유저에게 IdP가 사용 중지된 것을 알리고, 탈퇴 대신 로그아웃 후 다시 로그인할 수 있도록 변경하시기 바랍니다.

### iOS

* **+[TCGBPurchase requestItemListAtIAPConsoleWithCompletion:]** API가 deprecated되었습니다.
    * **+[TCGBPurchase requestItemListPurchasableWithCompletion:]** API를 사용하세요.

### Unity

* **Gamebase.Purchase.RequestItemListAtIAPConsole():** API가 deprecated되었습니다.
    * **Gamebase.Purchase.RequestItemListPurchasable()** API를 사용하세요.

## 2.76.0

### Android

* **Gamebase.Purchase.requestItemListAtIAPConsole()** API가 deprecated되었습니다.
    * **Gamebase.Purchase.requestItemListPurchasable()** API를 사용하세요.
* 미국 텍사스, 유타, 루이지애나와 같은 관할권의 특정 연령 확인 법률에 따른 준수를 위해 추가된 연령 확인 API는 Play Age Signals 라이브러리 버전이 베타(0.0.1-beta02) 상태이므로 항상 예외가 발생합니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Age Signals Support](../../aos-etc.md#age-signals-support)
    * 향후 정상 동작을 위해서는 Play Age Signals 라이브러리 버전이 0.0.2로 업데이트된 Gamebase Android SDK 2.78.0을 사용하세요.

### Unreal

* `IGamebasePurchase::RequestItemListAtIAPConsole()` API가 deprecated되었습니다.
    * `IGamebasePurchase::RequestItemListPurchasable()` API를 사용하세요.

## 2.75.0

### iOS

* Kakaogame 인증의 Xcode 최소 지원 버전이 16.0에서 16.2로 변경되었습니다.

## 2.71.2

### Android

* Gamebase Android SDK 2.71.2는 다음 이슈가 발생합니다.
    * 네트워크 연결이 끊어진 후 복구되거나, 앱을 백그라운드로 내렸다가 포그라운드로 활성화한 경우 간헐적으로 웹소켓 모듈에서 ArrayIndexOutOfBoundsException으로 인한 크래시가 발생할 수 있습니다.
    * 이슈가 해결된 Gamebase Android SDK 2.72.0을 사용하세요.

## 2.70.0

### Android

* Gamebase Android SDK 2.70.0에서 사용하는 Google Play Billing Library 7.1.1은 Android 7.0(API Level 24) 미만 단말기에서 결제를 시도하는 경우 크래시가 발생합니다.
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

## 2.69.0

### Unity

* GPGS AutoLogin을 사용하는 경우, **GetLastLoggedInProvider()** 동기 API 대신 신규 추가된 **RequestLastLoggedInProvider(GamebaseCallback.GamebaseDelegate\<string> callback)** 비동기 API를 사용하세요.

### Unreal

* 약관 조회 결과 API인 FGamebaseQueryTermsResult가 수정되었습니다.
    * TermsCountryType의 값이 설정되지 않는 문제를 수정했습니다.
    * bPushEnabled, bAdAgreement, bAdAgreementNight가 제거되었습니다.
* GPGS AutoLogin을 사용하는 경우, **GetLastLoggedInProvider()** 동기 API 대신 신규 추가된 **RequestLastLoggedInProvider(GamebaseCallback.GamebaseDelegate\<string> callback)** 비동기 API를 사용하세요.

### Android

* **gamebase-adapter-auth-gpgs-autologin** 모듈을 빌드에 포함하는 경우, **getLastLoggedInProvider()** 동기 API 대신 신규 추가된 **requestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;)** 비동기 API를 사용하세요.

## 2.68.1

### Unreal

* (Windows) WebView 플러그인을 옵션으로 선택할 수 있도록 변경되었습니다.
    * [WebView 플러그인 가이드](../../unreal-started.md#windows-settings)를 확인하여 업데이트가 필요합니다.
* (Windows) 크래시 로그 전송 시 프로젝트 바이너리 경로에 심벌 파일을 압축한 파일이 생성되도록 추가되었습니다.
    * [크래시 로그 전송 가이드](../../unreal-logger.md#crash-reporter)

## 2.68.0

### Android

#### Changed Minimum Support Version

* 최소 지원 버전이 Android 5.0 이상으로 상향되었습니다.(minSdk 19 → 21)

## 2.67.1

### Unreal

* (Windows) Purchase 설정 시 스토어를 하나만 선택할 수 있도록 변경되었습니다.
    * 스토어 재설정이 필요합니다.
* (Windows) Epic Games Store 사용 시 EOS SDK의 핸들을 등록하는 과정이 변경되었습니다.
    * Online Subsystem EOS를 사용하는 경우 Gamebase 초기화 시 StoreCode가 Epic Games Store의 해당하는 값이면 자동으로 핸들을 등록합니다.
    * Online Subsystem EOS를 사용하지 않는 경우 [Windows Settings](../../unreal-started.md#windows-settings) 가이드를 참고하여 EOS의 핸들을 등록하는 과정이 필요합니다.
* (Windows) Steamworks SDK 지원 버전이 1.59로 변경되었습니다.
    * [Steamworks 업그레이드 가이드](../../unreal-started.md#windows-settings)를 확인하여 업데이트가 필요합니다.

## 2.67.0

### Unity

#### Changed Minimum Support Version

* 최소 지원 Unity 버전이 2020.3.0에서 2020.3.16으로 변경되었습니다.
* 하위 버전의 Unity 지원이 필요하다면 [고객 센터](https://toast.com/support/inquiry)로 문의해 주시기 바랍니다.

### Unreal

#### Changed Minimum Support Version

* 최소 지원 버전이 UE 4.26에서 UE 4.27로 변경되었습니다.

### Android, iOS

* Twitter 인증 방식을 OAuth 2.0으로 변경하여 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](../../oper-app.md#6-twitter)

## 2.66.3

### Unity

#### Changed Minimum Support Version

* 최소 지원 Unity 버전이 2018.4.0에서 2020.3.0으로 변경되었습니다.
* 하위 버전의 Unity 지원이 필요하다면 [고객 센터](https://toast.com/support/inquiry)로 문의해 주시기 바랍니다.

## 2.66.2

### iOS

#### Changed/Deprecated APIs

* 다음 필드가 deprecated 되었습니다.
    * **TCGBWebViewConfiguration.orientationMask**
    
## 2.66.0

### Unreal

* API 사용 방식이 변경되었습니다.
    * `IModuleInterface`를 상속 받은 **IGamebase**에서 제공하던 API를 `UGameInstanceSubsystem`을 상속 받은 **UGamebaseSubsytem**에서 제공하도록 변경했습니다.
    * **UGamebaseSubsytem**은 GameInstance의 서브시스템이므로 GameInstance 생명 주기를 따르며 SDK API 호출 시 사용하는 GameInstance를 통해 해당 서브시스템을 찾아서 API를 사용해야 합니다.
    * 언리얼 코딩 표준에 명명 규칙을 따르도록 변경되었습니다.

```cpp
if (UGamebaseSubsystem* GamebaseSubsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance()))
{
    GamebaseSubsystem->Initialize(...);
}
```

* **GamebaseInterace** 모듈이 제거되었으므로 Gamebase 사용 시 모듈 의존성에서 제거해야 합니다.

        PrivateDependencyModuleNames.AddRange(
            new[]
            {
                "Gamebase"
            }
        );

## 2.65.0

### Common

* Gamebase SDK 2.65.0에서 이미지 공지 기능 사용 시 발생하는 문제를 수정하였습니다.
    * 표시할 이미지 공지가 없는 경우 오류 대신 성공 콜백이 호출되도록 변경하였습니다.
    * 등록된 이미지 공지가 없는 경우 빈 공지 화면이 노출되고, 이때 Android에서는 '오늘은 그만 보기'를 체크한 뒤 화면을 닫으면 크래시가 발생하는 문제를 수정하였습니다.
    * 이슈가 해결된 Gamebase SDK 2.65.1 이상을 사용하세요.

### Android

* Google billing client version 6.2.1이 적용되어 Android OS 4.4(API Level 19) 단말기에서 결제하려면 추가 설정이 필요합니다.
    * 자세한 내용은 [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Root level build.gradle](../../aos-started.md#root-level-buildgradle) 가이드를 참고하시기 바랍니다.

### iOS

* Facebook SDK가 17.0.1로 업데이트되면서 Dynamic Framework로 변경되었습니다.
    * Gamebase SDK를 다운로드하여 Xcode에 직접 설정하는 경우, Facebook SDK를 Embeded Frameworks에 추가해야 합니다.
    * 자세한 내용은 [Game > Gamebase > iOS SDK 사용 가이드 > 시작하기 > Setting > Xcode Settings](../../ios-started.md#xcode-settings) 가이드를 참고하시기 바랍니다.


## 2.64.0

### iOS

* Kakaogame 인증 최소 지원 버전이 12.0에서 13.0으로 변경되었습니다.

## 2.63.0

### iOS

* Facebook SDK가 17.0.0으로 업데이트되면서 Info.plist에 FacebookClientToken과 FacebookDisplayName을 추가해야 합니다.
```
<key>FacebookClientToken</key>
<string>{FACEBOOK_CLIENT_TOKEN}</string>
<key>FacebookDisplayName</key>
<string>{FACEBOOK_DISPLAY_NAME}</string>
```

### Unreal

* Android Firebase Notification 설정 방법이 변경되어 플러그인 내부에 google-services-json.xml 파일이 아닌 설정 툴에서 직접 지정하도록 변경되었습니다.
    * 기존에 제공되었던 Gamebase/Source/Gamebase/ThirdParty/Android/res/values/google-services-json.xml 파일이 제거되었습니다.
    * Firebase 콘솔에서 다운로드한 google-services.json 파일을 [Android 설정 툴](../../unreal-started.md#android-settings)의 Push 항목 내 FCM 하위에 있는 `GoogleServicesFilePath` 값을 설정합니다.

## 2.62.0

### Android

* Gamebase Android SDK 2.62.0은 Android 7.0(API Level 24) 미만 단말기에서 다음 이슈가 발생합니다. 
    * Gamebase.loginForLastLoggedInProvider 호출이 항상 실패합니다.
    * Guest 계정이 유실됩니다.
    * 이슈가 해결된 Gamebase Android SDK 2.62.1을 사용하세요.

### iOS
* Xcode 최소 지원 버전이 14.1에서 15로 변경되었습니다.
* Gamebase iOS 최소 지원 버전이 11.0에서 12.0으로 변경되었습니다.
* Gamebase와 Gamebase Adapter에 Privacy Manifest와 서명을 적용했습니다.
    * 2024년 5월 1일 이후 신규 출시 또는 업데이트를 하는 경우, Apple 정책에 따라 Gamebase iOS SDK 2.62.0 이상을 적용해야 합니다.
* LINE 인증 최소 지원 버전이 11.0에서 13.0으로 변경되었습니다.

### Unity

* Apple 개인정보 보호 정책을 준수하기 위한 대응 조치가 완료되었습니다.
    * Privacy Manifest 파일이 추가되었습니다.
    * Framework에 서명이 적용되었습니다.
    * 2024년 5월 1일 이후에는 새로운 출시나 업데이트를 위해 Apple 정책에 따라 Gamebase SDK for Unity 2.62.0 이상을 적용해야 합니다.

## 2.59.0

### iOS

* GamebaseAuthNaverAdapter에서 사용하는 NAVER iOS SDK가 xcframework로 변경되었습니다.

## 2.58.0

### Android

#### Twitter IdP
* Twitter API 서버의 인증서 업데이트로 minSdkVersion이 19에서 21로 상향되었습니다.

### iOS

* GamebaseAuthPaycoAdapter에서 사용하는 PAYCO iOS SDK가 xcframework로 변경되었습니다.

## 2.57.0

### iOS

* Privacy manifest 파일을 추가했습니다.
    * Privacy manifest 파일에서 Gamebase iOS SDK가 수집하는 데이터와 허용된 사유를 명시해야 하는 API 목록들을 볼 수 있습니다.
    * Apple 정책에 따라 2024년 봄까지 Gamebase iOS SDK 2.57.0 이상으로 업데이트해 주시기 바랍니다.

### Unreal
 
* Gamebase 모듈이 분리되었습니다. Gamebase 코드를 사용하려면 모듈의 Build.cs 파일 내 **GamebaseInterface** 모듈을 의존 모듈로 추가해야 합니다.

        PrivateDependencyModuleNames.AddRange(
            new[]
            {
                "Gamebase",
                "GamebaseInterface"
            }
        );

## 2.56.0

### Unreal
 
* 제공되는 타입이 USTRUCT에서 일반 구조체로 변경되었습니다.
    * 결과로 받는 타입은 기본적으로 제공되지 않는 값인 경우 TOptional 형태로 제공됩니다. 기존에 사용하던 값인 경우 Value.IsSet()를 이용해 설정된 값인지 확인한 뒤 Value.GetValue()를 통해 값을 사용할 수 있습니다.

## 2.55.0

### Android

#### Naver IdP
* Naver Login SDK의 업데이트로 minSDK가 19에서 21로 상향되었습니다.

#### MyCard Adapter
* NHN Cloud SDK의 업데이트로 minSDK가 19에서 21로 상향되었습니다.

## 2.54.0

### iOS

* Gamebase SDK가 xcframework로 변경되었습니다.
* Facebook iOS SDK가 14.1.0으로 업데이트되었습니다. Gamebase Console의 AdditionalInfo에 Facebook Client Token을 설정해 주시기 바랍니다.
    * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > App > Authentication Information > 1. Facebook](../../oper-app.md#1-facebook)    

## 2.53.0

### Android

#### Contact

* '고객 센터' 기능을 사용하는 경우 첨부 파일 선택 시 권한 요청이 정상적으로 작동하도록 아래 가이드에 따라 AndroidManifest.xml에 권한 설정을 추가해야 합니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Contact](../../aos-started.md#contact)

#### Line IdP

* 기존 ['시작하기' 문서](../../aos-started.md)에서 Line IdP 사용 시 AndroidManifest.xml에 선언하도록 안내한 아래 내용은 Line SDK 업데이트로 인해 불필요해졌으므로 삭제하시기 바랍니다.

```xml
<manifest>
    <!-- [Android11] settings start -->
    <queries>
        <!-- [LINE] Configurations begin -->
        <package android:name="jp.naver.line.android" />
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="https" />
        </intent>
        <!-- [LINE] Configurations end -->
    </queries>
    <!-- [Android11] settings end -->
        
    <application
          tools:replace="android:allowBackup"
          ... >
</manifest>
```
