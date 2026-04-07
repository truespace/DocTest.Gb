---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, v2.40.0, 기능개선, 기능추가, 변경, TermsView"
section: "2.40.0 (2022. 05. 24.)"
order: 36
---

### 2.40.0 (2022. 05. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.40.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
*  [iOS 설정 툴](../../unreal-started.md#ios-settings)을 제공합니다.
    * 기존 프로젝트 설정에서 **Gamebase**으로 표시되었지만 업데이트 이후 **Gamebase - Android**, **Gamebase - iOS**로 표시됩니다.
    * iOS 설정 툴을 제공하면서 빌드 시 필요한 프레임워크만 포함되도록 수정되었습니다.
* 공통 약관 API 호출 후 약관 UI가 표시되었는지를 알 수 있는 VO 클래스가 추가되었습니다.
    * FGamebaseShowTermsViewResult
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPush().QueryNotificationAllowed()
* 약관이 표시되었는지를 알 수 있는 API가 추가되었습니다.
    * UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTerms().IsShowingTermsView()
* 웹뷰에서 내비게이션 바를 숨길 수 있는 옵션이 추가되었습니다.
    * FGamebaseWebViewConfiguration.isNavigationBarVisible
* (Android) 웹뷰에서 폰트 사이즈를 고정할 수 있는 옵션이 추가되었습니다.
    * FGamebaseTermsConfiguration.enableFixedFontSize
* (Android) 약관 창에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * FGamebaseTermsConfiguration.enableFixedFontSize
* 결제 시 프로모션 여부를 알 수 있는 isPromotion 필드가 추가되었습니다.
    * FGamebasePurchasableReceipt.isPromotion
* 결제 시 테스트 결제 여부를 알 수 있는 isTestPurchase 필드가 추가되었습니다.
    * FGamebasePurchasableReceipt.isTestPurchase
* 고객 센터 URL 뒤에 파라미터를 추가할 수 있도록 다음 필드가 추가되었습니다.
    * FGamebaseContactConfiguration.additionalParameters

#### 기능 개선/변경
* API 결과 콜백 호출 시 GameThread로 전환하여 호출하도록 수정되었습니다.
* RequestActivatedPurchases API 호출 시 내부에서 2회 호출되는 문제가 수정되었습니다.
* 일부 API의 이름이 변경되었습니다.
    * FGamebaseAnalyticesLevelUpData → FGamebaseAnalyticsLevelUpData
    * FGambaseBanInfoPtr → FGamebaseBanInfoPtr
    
#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.40.0](../../release-notes-android.md#2400-2022-05-24)
* [Gamebase iOS SDK 2.40.0](../../release-notes-ios.md#2400-2022-05-24)
