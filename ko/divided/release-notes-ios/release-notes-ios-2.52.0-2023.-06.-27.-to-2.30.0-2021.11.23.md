---
source: release-notes-ios.md
section: "2.52.0 (2023. 06. 27.)-to-2.30.0 (2021.11.23)"
order: 2
created_date: 2026-04-03
---

### 2.52.0 (2023. 06. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.4.0)
    * Weibo iOS SDK (3.3.3)
* 아래 API가 deprecated되었습니다.
    * **+[TCGBGamebase countryCode]**
    * **+[TCGBGamebase countryCodeOfUSIM]**
    * **+[TCGBGamebase carrierCode]**
    * **+[TCGBGamebase carrierName]**
    * **+[TCGBUtil countryCode]**
    * **+[TCGBUtil usimCountryCode]**
    * **+[TCGBUtil carrierCode]**
    * **+[TCGBUtil carrierName]**
* SDK 내부 로직 개선

### 2.51.0 (2023. 05. 30.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.51.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.3.1)
    * PAYCO iOS SDK (1.5.8)
* SDK 내부 로직 개선

### 2.49.2 (2023. 04. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.2/GamebaseSDK-iOS.zip)

#### 버그 수정
* 누락되었던 이전 버전의 변경 사항을 적용하였습니다.
    * 로그인 후 외부 인증 IdP의 인증 정보를 얻지 못하는 버그 수정

### 2.49.1 (2023. 04. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* 로그인 후 외부 인증 IdP의 인증 정보를 얻지 못하는 버그를 수정하였습니다.

### 2.49.0 (2023. 04. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.5)

### 2.48.0 (2023. 03. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.48.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 14.1로 변경되었습니다. 
* iOS 최소 지원 버전이 11.0으로 변경되었습니다.
* armv7, armv7s, i386 아키텍처 지원을 중단하였습니다.
* 더 이상 bitcode를 지원하지 않습니다.
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.3.0)
    * PAYCO iOS SDK (1.5.6)
* DNS 장애를 대비한 Gamebase 서버 예비 도메인 적용

#### 버그 수정
* 특정 상황에서 킥아웃 이벤트가 동작하지 않는 버그를 수정하였습니다.
* 웹뷰 커스텀 스킴 콜백이 호출되지 않는 버그를 수정하였습니다.

### 2.47.0 (2023. 02. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.47.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.4)

### 2.46.0 (2023. 01. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.46.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.2)
    * Kakaogame iOS SDK (3.14.14)
* SDK 내부 로직 개선

### 2.45.0 (2022. 12. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.45.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 어떤 스토어에 대한 결제 영수증인지 알 수 있도록 다음 필드가 추가되었습니다.
    * **TCGBPurchasableReceipt.storeCode**
* 결제 API 호출 시 추가 설정을 할 수 있는 **TCGBPurchasableConfiguration** VO를 추가하였습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 결제 > TCGBPurchasableConfiguration](../../ios-purchase.md#tcgbpurchasableconfiguration)
* **TCGBPurchasableConfiguration**을 파라미터로 받는 신규 미소비 내역 조회 API를 추가하였습니다.
    * **[TCGBPurchase requestItemListOfNotConsumedWithConfiguration:completion:]**
* **TCGBPurchasableConfiguration**을 파라미터로 받는 신규 활성화 구독 조회 API를 추가하였습니다.
    * **[TCGBPurchase requestActivatedPurchasesWithConfiguration:completion:]**

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.2.0)
    * Hangame iOS SDK (1.8.0)
* 아래 API가 deprecated되었습니다.
    * **+[TCGBPurchase requestItemListOfNotConsumedWithCompletion:]**
    * **+[TCGBPurchase requestActivatedPurchasesWithCompletion:]**
* SDK 내부 로직 개선

### 2.44.0 (2022. 10. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* LINE iOS SDK 의존성 변경

### 2.43.3 (2022. 10. 04.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.3/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* SDK 내부 로직 개선

### 2.43.2 (2022. 09. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.2/GamebaseSDK-iOS.zip)

#### 버그 수정
* Game Center 로그인 시 오류가 발생하는 버그를 수정하였습니다.

### 2.43.1 (2022. 09. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* CocoaPods을 통해 배포되는 LINE Auth Adpater가 LINE SDK 의존성 오류로 인해 Region을 설정할 수 없는 버그를 수정하였습니다.

### 2.43.0 (2022. 09. 07.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.0.0)
    * ToastGamebaseIAP iOS SDK (0.14.0)
    * LINE iOS SDK (5.8.2)
    * Kakaogame iOS SDK (3.14.4)
    * Hangame iOS SDK (1.7.1)
* LINE 로그인 수행 시 서비스를 제공할 region을 입력할 수 있도록 변경하였습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > Login with IdP](../../ios-authentication.md#login-with-idp)
* Gamebase와 호환성이 보장되지 않은 Gamebase Adapter를 사용하는 경우 초기화 시 에러가 발생하도록 수정하였습니다.
* SDK 내부 로직 개선

### 2.42.2 (2022. 08. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 웹뷰에서 사용하는 스킴 목록 중 "itms-services"가 앱 스토어 심사에서 거절되는 경우가 발생하여 제거하였습니다.

### 2.42.1 (2022. 08. 09.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* 대비 증가 옵션을 활성화한 경우 Gamebase 팝업 창이 정상적으로 표시되지 않는 버그를 수정하였습니다.
* SceneDelegate를 사용하는 프로젝트에서 Gamebase 팝업 창이 표시되지 않는 버그를 수정하였습니다.

### 2.42.0 (2022. 07. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 매핑 실패 시 반환되는 ForcingMappingTicket VO 클래스에 유저의 현재 상태를 알 수 있도록 필드가 추가되었습니다.
    * **TCGBForcingMappingTicket.mappedUserValid**
    * mappedUserValid에 저장된 값의 의미는 아래를 참고해 주세요.
        * [Game > Gamebase > API 가이드 > API v1.3 가이드 > Others > Mamber Vaild Code](../../api-guide.md#member-valid-code)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame iOS SDK (1.7.0)

#### 버그 수정
* 잘못된 AppID로 Gamebase를 초기화했을 때 콜백이 호출되지 않는 버그를 수정하였습니다.
* 한게임 IdP로 로그인한 상태에서 GamebaseEventHandler의 **kTCGBIdPRevoked** 이벤트가 발생하지 않는 버그를 수정하였습니다.

### 2.41.1 (2022. 07. 20.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 약관 창이 완전히 닫힌 후에 콜백을 호출하도록 수정하였습니다.

### 2.41.0 (2022. 07. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* GamebaseEventHandler의 GamebaseEventCategory에 **kTCGBIdPRevoked** 타입이 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > IdP Revoked](../../ios-etc.md#idp-revoked)

#### 기능 개선/변경
* 이미지 공지가 노출 중일 때 화면 방향에 따라 회전하도록 변경했습니다.

### 2.40.0 (2022. 05. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.40.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* SDK 내부 로직 개선

### 2.39.0 (2022. 05. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.39.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame iOS SDK (1.6.4)

### 2.38.0 (2022. 05. 03.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.38.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Display Language의 중국어 번체(zh-TW) 언어셋에서 어색한 문장을 수정했습니다.

### 2.37.0 (2022. 04. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.37.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 고객 센터 URL 뒤에 파라미터를 추가할 수 있도록 다음 필드가 추가되었습니다.
    * **TCGBContactConfiguration.additionalParameters**

### 2.36.0 (2022. 04. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.36.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 결제 영수증에서 Sandbox 및 프로모션 결제 여부를 알 수 있도록 다음 필드가 추가되었습니다.
    * **TCGBPurchasableReceipt.sandboxPayment**
    * **TCGBPurchasableReceipt.promotionPayment**

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST iOS SDK(0.30.0), ToastGamebaseIAP SDK(0.13.0), Hangame iOS SDK (1.6.3)

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 현재 약관 창이 화면에 표시되고 있는지를 알 수 있는 API를 추가하였습니다.
    * **[TCGBTerms isShowingTermsView]**

#### 기능 개선/변경
* 기존의 Google 웹 로그인 방식에서 Google SDK 로그인 방식으로 변경하였습니다.
* 한게임 로그인을 도중에 취소했을 경우, **TCGB_ERROR_AUTH_USER_CANCELED(3001)** 오류를 반환하도록 수정하였습니다.

### 2.34.1 (2022. 03. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.1/GamebaseSDK-iOS.zip)

#### 기능 추가
* Swift 프로젝트 사용자를 위해서 Public API에 NS_SWIFT_NAME 설정을 추가하였습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame iOS SDK (1.6.2)
* 디바이스가 가로 모드인 상태에서 showWebView API를 호출했을 때, 하단에 검은색 빈 공간이 출력되는 오류를 수정하였습니다.

### 2.34.0 (2022. 02. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Gamebase 콘솔의 업데이트 필수 설정에서 **팝업 버튼 추가**를 선택하면 클라이언트의 업데이트 필수 팝업 창에 **자세히 보기** 버튼이 추가됩니다.
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * **[TCGBPush queryNotificationAllowedWithCompletion:]**
* 공통 약관 API 호출 후 약관 UI가 표시되었는지 여부를 알 수 있는 VO 클래스가 추가되었습니다.
    * **TCGBShowTermsViewResult**

#### 기능 개선/변경
* 이미지 공지 API를 호출했을 때 표시할 이미지 공지가 없는 경우, 배경이 잠시 어두워지는 현상을 수정하였습니다.
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드가 deprecated되었습니다.
    * **-[TCGBConfiguration enableKickoutPopup:]**
    * **-[TCGBConfiguration isEnableKickoutPopup]**

### 2.33.0 (2022.01.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.33.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 공통 약관 창의 설정을 변경할 수 있는 신규 API가 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > UI > Terms > showTermsView](../../ios-ui.md#showtermsview)

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO iOS SDK (1.5.5)
* 오류 코드 추가 및 변경
    * TCGB_ERROR_UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 TCGB_ERROR_SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.

### 2.32.1 (2022.01.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 업데이트 권장 팝업 창에서 **지금 업데이트** 버튼을 클릭하면 팝업 창이 종료되지 않도록 수정하였습니다.
* SDK 안정성을 개선하였습니다.

### 2.32.0 (2021.12.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.32.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* GamebaseEventHandler의 GamebaseEventCategory에 **kTCGBServerPushAppKickoutMessageReceived** 타입이 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Server Push](../../ios-etc.md#server-push)
* GamebaseEventHandler의 GamebaseEventCategory에 **kTCGBLoggedOut** 타입이 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Logged Out](../../ios-etc.md#logged-out)

#### 기능 개선/변경
* 웹뷰 navigationBar의 기본 타이틀 색상이 **UIColor.whiteColor**로 변경되었습니다.

#### 버그 수정
* Hangame 로그아웃 호출 시, thirdIdP도 로그아웃되도록 수정하였습니다.

### 2.31.0 (2021.12.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.31.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 점검 팝업 창에서 점검 시간 표시 여부를 동적으로 설정할 수 있게 되었습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST iOS SDK (0.29.2), PAYCO iOS SDK (1.5.4)
* 이용 정지 웹뷰 내의 고객 센터 링크에서 이용 정지 유저 정보로 문의를 등록할 수 없는 문제를 해결하였습니다.
* 점검 팝업 창, 이용 정지 자세히보기 웹뷰에서 뒤로 가기 버튼이 표시되도록 수정하였습니다.

### 2.30.1 (2021.11.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* Unity 2019.3 이상에서 Cocoapods 설치를 했을 때, 결제와 푸시 API에서 에러가 발생하는 버그를 수정하였습니다.

### 2.30.0 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > Add Mapping Forcibly](../../ios-authentication.md#add-mapping-forcibly)
* 특정 IdP로 매핑 시도 후 **TCGB_ERROR_AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)** 에러가 발생했을 때, 해당 IdP로 계정을 변경할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > Change Login with ForcingMappingTicket](../../ios-authentication.md#change-login-with-forcingmappingticket)

#### 버그 수정
* loginForLastLoggedInProvider 로그인 이후, 특정 IdP에서 로그아웃 또는 탈퇴 기능이 동작하지 않는 버그를 수정하였습니다.
