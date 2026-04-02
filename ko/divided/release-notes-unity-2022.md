## Game > Gamebase > 릴리스 노트 > Unity

### 2.45.0 (2022. 12. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.45.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Deprecated API 
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
         
        // New API 
        Gamebase.Purchase.RequestItemListOfNotConsumed(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                       GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **GamebaseRequest.Purchase.PurchasableConfiguration.allStores**의 값을 **true**로 설정해야 합니다.

            // Deprecated API 
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);
             
            // New API
            Gamebase.Purchase.RequestActivatedPurchases(GamebaseRequest.Purchase.PurchasableConfiguration configuration,
                                                        GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback);

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Unity SDK (0.27.1)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.45.0](./release-notes-android/#2450-2022-12-27)
* [Gamebase iOS SDK 2.45.0](./release-notes-ios/#2450-2022-12-27)

### 2.44.2 (2022. 11. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.2/GamebaseSDK-Unity.zip)

#### 기능 추가

* Setting Tool (v2.5.0)
    * ONE Store v19 결제 어댑터가 추가되었습니다. (Android에 한함)
    * 기존 Setting Tool은 Unity 프로젝트에서 완전히 제거한 뒤 최신 버전으로 다시 설치해야 합니다.

#### 버그 수정
* (iOS) 게임 중 Screen.orientation을 변경하는 경우 웹뷰, 고객 센터 등 뷰 컨트롤러의 영향을 받는 API가 정상적으로 노출되지 않는 이슈를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.44.2](./release-notes-android/#2442-2022-11-29)
* [Gamebase iOS SDK 2.44.0](./release-notes-ios/#2440-2022-10-25)

### 2.44.0 (2022. 10. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Unity SDK(0.26.2)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.44.0](./release-notes-android/#2440-2022-10-11)
* [Gamebase iOS SDK 2.43.3](./release-notes-ios/#2433-2022-10-04)

### 2.43.0 (2022. 09. 07.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Unity SDK(0.26.1), Kakaogame Unity SDK(3.14.5)
* LINE 로그인을 수행 시 서비스를 제공할 Region을 입력하도록 변경되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Login with IdP](./unity-authentication/#login-with-idp)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.43.0](./release-notes-android/#2430-2022-09-07)
* [Gamebase iOS SDK 2.43.0](./release-notes-ios/#2430-2022-09-07)

### 2.42.1 (2022. 08. 09.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.1/GamebaseSDK-Unity.zip)

#### 기능 추가
* ForcingMappingTicket 클래스에 매핑 유저 상태를 나타내는 mappedUserValid 필드가 추가되었습니다.

#### 기능 개선/변경
* 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드는 더 이상 사용되지 않습니다.
    * **GamebaseWebViewConfiguration.enableFixedFontSize**
* GamebaseWebViewConfiguration의 기본값이 추가되었습니다.
    * 내비게이션 바의 색상 필드인 colorR, colorG, colorB, colorA의 기본값이 18, 93, 230, 255로 설정되었습니다.
    * 내비게이션 바 활성 여부를 지정하는 필드인 isNavigationBarVisible의 기본값이 true로 설정되었습니다.
    * 웹뷰 내 뒤로 가기 버튼 활성 여부를 지정하는 필드인 isBackButtonVisible의 기본값이 true로 설정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.42.1](./release-notes-android/#2421-2022-07-26)
* [Gamebase iOS SDK 2.42.1](./release-notes-ios/#2421-2022-08-09)

### 2.41.0 (2022. 07. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.6)
* GamebaseEventHandler의 GamebaseEventCategory에 **IDP_REVOKED** 타입이 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > IdP Revoked](./unity-etc/#idp-revoked)

#### 기능 개선/변경
* Unity의 Burst 패키지를 사용할 때 메모리 누수가 발생하는 이슈를 수정했습니다.
* Setting Tool (v2.4.0)
    * 내부 안정화 지표가 추가되었습니다.
    * 기존 SettingTool은 Unity 프로젝트에서 완전히 제거한 뒤 최신 버전으로 다시 설치해야 합니다.
    * SettingTool v1은 더 이상 지원하지 않습니다.

#### 버그 수정
* (iOS) 특정 환경에서 결제 후 크래시가 발생하는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.41.0](./release-notes-android/#2410-2022-07-05)
* [Gamebase iOS SDK 2.41.0](./release-notes-ios/#2410-2022-07-05)

### 2.40.0 (2022. 05. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.40.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.5)
* (Standalone) 아래 약관 API를 지원하도록 변경되었습니다.
    * Gamebase.Terms.QueryTerms
    * Gamebase.Terms.UpdateTerms

#### 기능 개선/변경
* 한글이 유니코드로 표시되는 현상이 개선되었습니다.
* (iOS) bitcode 지원하도록 수정되었습니다.

#### 버그 수정
* (Android) OpenContact API 호출 시 Configuration.additionalParameters가 적용되지 않는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.40.0](./release-notes-android/#2400-2022-05-24)
* [Gamebase iOS SDK 2.40.0](./release-notes-ios/#2400-2022-05-24)

### 2.39.0 (2022. 05. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.39.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.4)

#### 버그 수정
* 초기화 전에 GetLaunchingInformations() API를 호출 시 JsonException이 발생하지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.39.0](./release-notes-android/#2390-2022-05-10)
* [Gamebase iOS SDK 2.39.0](./release-notes-ios/#2390-2022-05-10)

### 2.38.0 (2022. 05. 03.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.38.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.3)

#### 기능 개선/변경
* Display Language의 중국어 번체(zh-TW) 언어셋에서 어색한 문장이 수정되었습니다.

#### 버그 수정
* (Android) API Level 24 미만에서 특정 API 호출 시 오류가 발생하지 않도록 수정되었습니다.
    * Gamebase.Purchase.RequestActivatedPurchases()
    * Gamebase.Purchase.RequestItemListOfNotConsumed()

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.38.0](./release-notes-android/#2380-2022-05-03)
* [Gamebase iOS SDK 2.38.0](./release-notes-ios/#2380-2022-05-03)

### 2.37.0 (2022. 04. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.37.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 고객 센터 URL 뒤에 파라미터를 추가할 수 있도록 다음 필드가 추가되었습니다.
    * GamebaseRequest.Contact.Configuration.additionalParameters

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.37.0](./release-notes-android/#2370-2022-04-26)
* [Gamebase iOS SDK 2.37.0](./release-notes-ios/#2370-2022-04-26)

### 2.36.0 (2022. 04. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.36.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.2)
* 결제 시 프로모션 여부를 알 수 있는 isPromotion 필드가 추가되었습니다.
    * GamebaseResponse.Purchase.PurchasableReceipt.isPromotion
* 결제 시 테스트 결제 여부를 알 수 있는 isTestPurchase 필드가 추가되었습니다.
    * GamebaseResponse.Purchase.PurchasableReceipt.isTestPurchase

#### 버그 수정
* 디바이스가 특정 문화권으로 설정되었을 때 결제 상품 가격 정보가 0으로 입력되는 오류가 수정되었습니다.
* (iOS) Push 알림 클릭 시 딥 링크가 동작하지 않는 오류가 수정되었습니다.
* (iOS) 프로젝트의 orientation이 Auto Rotation으로 설정되어 있고, 프로젝트 첫 신(scene)에 포함된 MonoBehaviour의 Awake에서 Gamebase API 호출 시 웹뷰 등의 UI 출력이 정상적으로 되지 않는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.36.0](./release-notes-android/#2360-2022-04-12)
* [Gamebase iOS SDK 2.36.0](./release-notes-ios/#2360-2022-04-12)

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 외부 SDK 업데이트: TOAST Unity SDK(0.25.1)
* 약관이 표시되었는지를 알 수 있는 API가 추가되었습니다.
    * Gamebase.Terms.IsShowingTermsView()
* 웹뷰에서 내비게이션 바를 숨길 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Webview.GamebaseWebViewConfiguration.isNavigationBarVisible
* (Android) 웹뷰에서 폰트 사이즈를 고정할 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Webview.GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 약관 창에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * GamebaseRequest.Terms.GamebaseTermsConfiguration.enableFixedFontSize
* Setting Tool
    * (Android) Amazon 스토어가 추가되었습니다.
    * (Android) Huawei 스토어가 추가되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.35.0](./release-notes-android/#2350-2022-03-29)
* [Gamebase iOS SDK 2.35.0](./release-notes-ios/#2350-2022-03-29)

### 2.34.1 (2022. 03. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.1/GamebaseSDK-Unity.zip)

#### 기능 추가
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * Gamebase.Push.QueryNotificationAllowed()

#### 버그 수정
* iOS에서 GamebaseWebViewConfiguration의 isBackButtonVisible 설정이 적용되지 않는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.34.0](./release-notes-android/#2340-2022-02-22)
* [Gamebase iOS SDK 2.34.1](./release-notes-ios/#2341-2022-03-15)

### 2.34.0 (2022. 02. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 공통 약관 API 호출 후 약관 UI가 표시되었는지 여부를 알 수 있는 VO 클래스가 추가되었습니다.
    * **GamebaseResponse.Terms.ShowTermsViewResult**

#### 기능 개선/변경
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드가 deprecated되었습니다.
    * **GamebaseConfiguration.enableKickoutPopup**
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.34.0](./release-notes-android/#2340-2022-02-22)
* [Gamebase iOS SDK 2.34.0](./release-notes-ios/#2340-2022-02-22)

### 2.33.0 (2022.01.25)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.33.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 공통 약관 창의 설정을 변경할 수 있는 신규 API가 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > UI > Terms > showTermsView](./unity-ui/#showtermsview)

#### 기능 개선/변경
* 오류 코드 추가 및 변경
    * GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode.SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.33.0](./release-notes-android/#2330-20220125)
* [Gamebase iOS SDK 2.33.0](./release-notes-ios/#2330-20220125)
