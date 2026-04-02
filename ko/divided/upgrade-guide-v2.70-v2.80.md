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
    * `AdditionalPlistData`로 직접 관리하려면 [iOS Settings](./unreal-started/#ios-settings)에서 **Disable Auto Info.plist Update**를 활성화하세요.

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
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Age Signals Support](./aos-etc/#age-signals-support)
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
