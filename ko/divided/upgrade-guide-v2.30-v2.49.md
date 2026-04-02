## Game > Gamebase > Upgrade Guide

## 2.49.0

### Unreal

* 최소 지원 버전이 4.22에서 4.26으로 변경되었습니다.
* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Deprecated API
        void RequestItemListOfNotConsumed(const FGamebasePurchasableReceiptListDelegate& onCallback);
        // New API
        void RequestItemListOfNotConsumed(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableReceiptListDelegate& onCallback);

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **FGamebasePurchasableConfiguration.allStores**를 **true**로 설정해야 합니다.

            // Deprecated API
            void RequestActivatedPurchases(const FGamebasePurchasableReceiptListDelegate& onCallback);
            // New API
            void RequestActivatedPurchases(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableReceiptListDelegate& onCallback);

### Android

```
최소 지원 버전이 Android 4.4 이상으로 상향되었습니다.(minSdk 16 -> 19)
```

## 2.47.0

### Android

* Unity에서 Proguard 적용 시 Purchase 관련 API 호출에 실패합니다.
    * 해당 이슈는 2.48.0에서 수정되었습니다.

## 2.45.0

### Android, iOS, Unity

* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Unity: Deprecated API
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
        // Unity: New API
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                       GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
        // Android: Deprecated API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity activity,
                                                       GamebaseDataCallback<List<PurchasableReceipt>> callback);
        // Android: New API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity activity,
                                                       PurchasableConfiguration configuration,
                                                       GamebaseDataCallback<List<PurchasableReceipt>> callback);
        // iOS: Deprecated API
        + (void)requestItemListOfNotConsumedWithCompletion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
        // iOS: New API
        + (void)requestItemListOfNotConsumedWithConfiguration:(TCGBPurchasableConfiguration *)configuration
                                                   completion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **PurchasableConfiguration.allStores**를 **true**로 설정해야 합니다.

            // Unity: Deprecated API
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
            // Unity: New API
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                        GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
            // Android: Deprecated API
            Gamebase.Purchase.requestActivatedPurchases(Activity activity,
                                                        GamebaseDataCallback<List<PurchasableReceipt>> callback);
            // Android: New API
            Gamebase.Purchase.requestActivatedPurchases(Activity activity,
                                                        PurchasableConfiguration configuration,
                                                        GamebaseDataCallback<List<PurchasableReceipt>> callback);
            // iOS: Deprecated API
            + (void)requestActivatedPurchasesWithCompletion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;
            // iOS: New API
            + (void)requestActivatedPurchasesWithConfiguration:(TCGBPurchasableConfiguration *)configuration
                                                    completion:(void(^)(NSArray<TCGBPurchasableReceipt *> * _Nullable purchasableReceiptArray, TCGBError * _Nullable error))completion;

## 2.42.2

### Unity

* Gamebase Setting Tool (v2.5.0)에 ONE Store v19 결제 어댑터가 추가되었습니다.
    * **SettingTool > Android** 설정에서 ONE Store v19 어댑터 활성화 시 iap_sdk-v19.xx.xx.aar 다운로드 페이지로 연결되며, 해당 파일을 **Assets > Plugins > Android** 폴더에 복사해야 합니다.

## 2.44.0

### Android

* Gamebase Android SDK 2.44.0에서 registerPush를 호출하면 Android 6.0(M, API Level 23) 단말기에서 크래시가 발생합니다.
    * 문제가 해결된 Gamebase Android SDK 2.44.1을 사용하세요.

## 2.43.3

### Unreal

* Google Billing Client 5.0.0 버전으로 변경되었습니다. Unreal에서 제공하는 Online SubSystem GooglePlay 플러그인 사용 시 /Config/Android/AndroidEngine.ini 파일에 해당 값을 추가해야 빌드 시 오류가 발생하지 않습니다.

            [OnlineSubsystemGooglePlay.Store]
            bUseGooglePlayBillingApiV2=False

## 2.42.1

### Unity
    
#### Changed/Deprecated APIs
* FGamebaseWebViewConfiguration에서 enableFixedFontSize 필드는 더 이상 지원하지 않습니다.
* GamebaseWebViewConfiguration 일부 필드에 기본값이 추가되어 값을 설정하지 않은 경우 기존과 다르게 동작할 수 있습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다

### Unreal

* (iOS) [iOS 설정 툴](./unreal-started/#ios-settings)에서 Xcode의 경로를 변경할 수 있도록 **Xcode Path** 설정이 추가되었습니다.
    * 변경하지 않는 경우 기본값으로 설정됩니다(기본값: /Applications/Xcode.app).

#### Changed/Deprecated APIs
* FGamebaseConfiguration의 enableKickoutPopup 속성을 더 이상 지원하지 않습니다.
* FGamebaseConfiguration 일부 필드에 기본값이 추가되어 값을 설정하지 않은 경우 기존과 다르게 동작할 수 있습니다.
    * enableLaunchingStatusPopup의 기본값이 true로 설정되었습니다.
    * enableBanPopup의 기본값이 true로 설정되었습니다.
* FGamebaseWebViewConfiguration에서 enableFixedFontSize 필드는 더 이상 지원하지 않습니다.
* FGamebaseWebViewConfiguration 일부 필드에 기본값이 추가되어 값을 설정하지 않은 경우 기존과 다르게 동작할 수 있습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255으로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다.

## 2.41.0

### Android

* 이제 웹뷰에 등록한 커스텀 스킴 이벤트가 동작할 때 자동으로 웹뷰가 종료됩니다.
    * 이전과 같이 커스텀 스킴 이벤트가 동작하더라도 웹뷰를 유지하려면 **GamebaseWebViewConfiguration.Builder.enableAutoCloseByCustomScheme(false)** API를 호출하세요.
* Gamebase Android SDK 2.41.0에는 약관 창의 '보기' 버튼이 동작하지 않는 버그가 존재합니다.
    * Gamebase 약관 창을 사용하려면 문제가 해결된 Gamebase Android SDK 2.41.1을 사용하세요.

### Unity

* Gamebase SettingTool 필수 업데이트가 추가되었습니다. (v2.4.0)
    * 기존 SettingTool은 Unity 프로젝트에서 완전히 제거한 뒤 최신 버전으로 다시 설치해야 합니다.
    * SettingTool v1은 더 이상 지원하지 않습니다.

## 2.40.0

### Unreal

* 일부 API의 이름이 변경되었습니다.
    * FGamebaseAnalyticesLevelUpData → FGamebaseAnalyticsLevelUpData
    * FGambaseBanInfoPtr → FGamebaseBanInfoPtr
* (iOS) iOS 설정 툴을 제공하면서 빌드 시 필요한 프레임워크만 포함되도록 수정되었습니다.
* (iOS) PLCrashReporter가 업데이트되어 엔진 내부에 PLCrashReporter도 업데이트가 필요합니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Installation > iOS Settings > PLCrashReporter](./unreal-started/#ios-settings)
* (iOS) Facebook iOS SDK가 9.2.0버전으로 업데이트되어 swift 사용을 위해 엔진 코드 수정이 필요합니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Installation > iOS Settings > Facebook SDK](./unreal-started/#ios-settings)

## 2.36.0

### Android

#### Hangame SDK
* Hangame Android SDK v1.4.5에서 sms_hash가 내부에서 생성되도록 개선되었습니다.
    * 더 이상 sms_hash를 설정하지 않아도 됩니다. 

## 2.35.0

### Android

#### NAVER IdP

* 이제 NAVER 로그아웃 시 토큰을 삭제하지 않습니다.
    * 재로그인할 때 정보 제공 동의 창이 나타나지 않습니다.
    * 웹 로그인 시에는 계정이 변경되지 않습니다.
    * 이전 동작을 유지하려면 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하세요.

```
{"logout_and_delete_token":true}
```

## 2.34.0

### Android

#### Changed/Deprecated APIs

* 킥아웃 팝업 표시 여부는 Gamebase 콘솔에서 킥아웃 등록시 설정할 수 있으므로 다음 필드가 deprecated 되었습니다.
    * **UIPopupConfiguration.enableKickoutPopup**

### iOS

#### Changed/Deprecated APIs

* 킥아웃 팝업 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 아래 API들이 deprecated되었습니다.
    * **-[TCGBConfiguration enableKickoutPopup:]**
    * **-[TCGBConfiguration isEnableKickoutPopup]**

### Unity

* GamebaseConfiguration의 enableKickoutPopup 속성을 더 이상 지원하지 않습니다.

## 2.33.0

### iOS

* TCGB_ERROR_UNKNOWN_ERROR 에러에 매핑된 오류 코드가 변경되었습니다.
    * TCGB_ERROR_UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 TCGB_ERROR_SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.

### Unity

* GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드가 변경되었습니다.
    * GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode.SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.

### Unreal

* GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드가 변경되었습니다.
    * GamebaseErrorCode::UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode::SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.

## 2.32.0

### Android

* Gamebase Access Token이 만료되어 복구되지 않을 때 발생하는 GamebaseEventHandler 이벤트 category가 **GamebaseEventCategory.OBSERVER_HEARTBEAT**에서 **GamebaseEventCategory.LOGGED_OUT**으로 변경되었습니다.
    * **GamebaseEventCategory.OBSERVER_HEARTBEAT** 이벤트에서 GamebaseEventObserverData.code 값이 **GamebaseError.AUTH_TOKEN_LOGIN_INVALID_TOKEN_INFO(3102)**일 때 로그인 하도록 구현했다면 **GamebaseEventCategory.LOGGED_OUT** 이벤트에서 로그인을 하도록 변경하시기 바랍니다.
