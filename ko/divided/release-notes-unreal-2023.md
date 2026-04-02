## Game > Gamebase > 릴리스 노트 > Unreal

### 2.58.0 (2023. 11. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.58.0/GamebaseSDK-Unreal.zip)

#### 버그 수정
* (Windows) 서버 푸시가 동작하지 않는 이슈가 수정되었습니다.
* 초기화 시 크래시가 발생할 수 있는 로직이 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.58.0](./release-notes-android/#2580-2023-11-28)
* [Gamebase iOS SDK 2.58.0](./release-notes-ios/#2580-2023-11-28)

### 2.57.0 (2023. 11. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.57.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* Windows 플랫폼 지원 추가
    * [Windows 설정 툴](./unreal-started/#windows-settings)이 추가되었습니다.
    * 플랫폼에서 지원하는 API는 각 문서에 `UNREAL_WINDOWS` 항목을 확인하시기 바랍니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.57.0](./release-notes-android/#2570-2023-10-31)
* [Gamebase iOS SDK 2.57.0](./release-notes-ios/#2570-2023-10-31)

### 2.56.0 (2023. 10. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.56.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* [Android 설정 툴](./unreal-started/#android-settings)에서 스토어 설정이 추가되었습니다.
    * Amazon Appstore, Huawei AppGallery, MyCard 선택이 추가되었습니다.
    * ONE Store를 선택 시 스토어의 버전 선택 옵션이 추가되었습니다.
* [iOS 설정 툴](./unreal-started/#ios-settings)에서 Naver IdP 설정이 추가되었습니다.
* (Android) LoginForLastLoggedInProvider 호출 중에 로딩 애니메이션을 숨기는 옵션을 지정할 수 있는 신규 API가 추가되었습니다. 
    * LoginForLastLoggedInProvider(const UGamebaseJsonObject& additionalInfo, const FGamebaseAuthTokenDelegate& onCallback)
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > 인증 > Login > Login Flow > Login as the Latest Login IdP](./unreal-authentication/#login-as-the-latest-login-idp)
* (Android) Android 13 이상의 OS에서 RegisterPush API를 호출했을 때 Push 권한 요청 팝업이 자동으로 뜨지 않도록 할 수 있는 FGamebasePushConfiguration.requestNotificationPermission 필드가 추가되었습니다.
* (iOS) 사용자가 푸시 권한을 거부해도 토큰을 등록할 수 있도록 FGamebasePushConfiguration.alwaysAllowTokenRegistration 필드가 추가되었습니다.

#### 기능 개선/변경
* 제공되는 타입이 USTRUCT에서 일반 구조체로 변경되었습니다.
    * 결과로 받는 타입의 경우 기본적으로 제공되지 않는 값인 경우 TOptional 형태로 제공됩니다.

#### 버그 수정
* 로그인 후 탈퇴 유예 정보 및 결제 어뷰징 자동 해제 정보가 정상으로 전달되도록 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.56.0](./release-notes-android/#2560-2023-09-26)
* [Gamebase iOS SDK 2.55.2](./release-notes-ios/#2552-2023-09-26)

### 2.49.1 (2023. 04. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.1/GamebaseSDK-Unreal.zip)

#### 버그 수정
* (iOS) 결제 상품 조회 API를 호출 시 크래시가 발생하지 않도록 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.48.0](./release-notes-android/#2480-2023-03-28)
* [Gamebase iOS SDK 2.49.0](./release-notes-ios/#2490-2023-04-11)

### 2.49.0 (2023. 04. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
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

* (Android) IAP 구독 상태를 조회할 수 있는 RequestSubscriptionsStatus API가 추가되었습니다.
* (Android) 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드를 재지원합니다.
    * GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 웹뷰에서 컷아웃(노치) 영역을 비롯한 모든 이용 가능한 스크린 공간을 사용하여 렌더링할 수 있는 설정이 추가되었습니다.
    * GamebaseWebViewConfiguration.renderOutsideSafeArea

#### 기능 개선/변경
* Unreal의 최소 지원 버전이 4.26으로 변경되었습니다.
* (iOS) Xcode 14.1에서 빌드 시 오류가 발생되는 이슈가 수정되었습니다.
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.48.0](./release-notes-android/#2480-2023-03-28)
* [Gamebase iOS SDK 2.49.0](./release-notes-ios/#2490-2023-04-11)
