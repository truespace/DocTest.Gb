## Game > Gamebase > 릴리스 노트 > Unity

### 2.59.0 (2023. 12. 19.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.59.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (Standalone) macOS 지원이 추가되었습니다.
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.59.0](./release-notes-android/#2590-2023-12-19)
* [Gamebase iOS SDK 2.59.0](./release-notes-ios/#2590-2023-12-19)

### 2.57.0 (2023. 10. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.57.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (공통) try/catch 구문에서 예외와 관련된 로그를 전송할 수 있는 Gamebase.Logger.Report API가 추가되었습니다.
* (iOS) AUTH_IDP_LOGIN_EXTERNAL_AUTHENTICATION_REQUIRED 오류 코드가 추가되었습니다. 

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.57.0](./release-notes-android/#2570-2023-10-31)
* [Gamebase iOS SDK 2.57.0](./release-notes-ios/#2570-2023-10-31)

### 2.55.0 (2023. 09. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.55.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (iOS) 사용자가 푸시 권한을 거부해도 토큰을 등록할 수 있도록 GamebaseRequest.Push.PushConfiguration.alwaysAllowTokenRegistration 필드가 추가되었습니다.

#### 기능 개선
* NHN Cloud Unity SDK가 서비스 종료 됨에 따라 Gamebase Unity SDK 내에서 제거되었습니다.
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.55.0](./release-notes-android/#2550-2023-09-12)
* [Gamebase iOS SDK 2.55.0](./release-notes-ios/#2550-2023-09-12)

### 2.54.0 (2023. 08. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.54.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (Android) Android 13 이상의 OS에서 RegisterPush API를 호출했을 때 Push 권한 요청 팝업이 자동으로 뜨지 않도록 할 수 있는 GamebaseRequest.Push.PushConfiguration.requestNotificationPermission 필드가 추가되었습니다.
* (Android) loginForLastLoggedInProvider 호출 중에 로딩 애니메이션을 숨기는 옵션을 지정할 수 있는 신규 API가 추가되었습니다.
    * Gamebase.LoginForLastLoggedInProvider(Dictionary<string, object> additionalInfo, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback);
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Login > Login Flow > Login as the Latest Login IdP](./unity-authentication/#login-as-the-latest-login-idp)

#### 버그 수정
* (Standalone) Gamebase 고객 센터 호출 시 서비스 오류 페이지가 출력되지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.53.0](./release-notes-android/#2530-2023-08-17)
* [Gamebase iOS SDK 2.54.0](./release-notes-ios/#2540-2023-08-29)

### 2.52.1 (2023. 07. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* (Standalone) Gamebase Logger 초기화가 완료되기 전에 로그를 전송하면 null reference exception이 발생하는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.52.1](./release-notes-android/#2521-2023-07-17)
* [Gamebase iOS SDK 2.53.0](./release-notes-ios/#2530-2023-07-25)

### 2.52.0 (2023. 06. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* Setting Tool (v2.7.0)
    * ONE Store v21 결제 어댑터가 추가되었습니다. (Android에 한함)
    * Gamebase Custom Push Receiver 어댑터가 추가되었습니다. (Android에 한함)

#### 기능 개선
* 외부 SDK 업데이트: NHN Cloud Unity SDK(0.28.3)
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.52.0](./release-notes-android/#2520-2023-06-27)
* [Gamebase iOS SDK 2.52.0](./release-notes-ios/#2520-2023-06-27)

### 2.51.0 (2023. 05. 30.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.51.0/GamebaseSDK-Unity.zip)

#### 기능 개선
* 외부 SDK 업데이트: NHN Cloud Unity SDK(0.28.1)
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.50.0](./release-notes-android/#2500-2023-05-16)
* [Gamebase iOS SDK 2.51.0](./release-notes-ios/#2510-2023-05-30)

### 2.50.0 (2023. 05. 16.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.50.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (Android) MyCard 스토어가 추가되었습니다.
* Setting Tool (v2.5.0)
    * MyCard 스토어가 추가되었습니다. (Android에 한함)
    * Huawei IAP 추가 시 Huawei repository 자동 설정 기능이 추가되었습니다.

#### 기능 개선
* 외부 SDK 업데이트: NHN Cloud Unity SDK(0.28.0)

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.50.0](./release-notes-android/#2500-2023-05-16)
* [Gamebase iOS SDK 2.49.2](./release-notes-ios/#2492-2023-04-28)

### 2.49.0 (2023. 04. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.49.0/GamebaseSDK-Unity.zip)

#### 기능 개선
* (iOS) 내부 로직을 개선하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.49.0](./release-notes-android/#2490-2023-04-25)
* [Gamebase iOS SDK 2.49.1](./release-notes-ios/#2491-2023-04-25)

### 2.48.0 (2023. 03. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.48.0/GamebaseSDK-Unity.zip)

#### 기능 개선
* 외부 SDK 업데이트: NHN Cloud Unity SDK (0.27.4)
* DNS 장애를 대비한 Gamebase 서버 예비 도메인 적용
* iOS
    * Xcode 최소 지원 버전이 14.1로 변경되었습니다. 
    * iOS 최소 지원 버전이 11.0으로 변경되었습니다.
    * armv7, armv7s, i386 아키텍처 지원을 중단하였습니다.
    * 더 이상 bitcode를 지원하지 않습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.48.0](./release-notes-android/#2480-2023-03-28)
* [Gamebase iOS SDK 2.48.0](./release-notes-ios/#2480-2023-03-28)

### 2.46.0 (2023. 01. 31.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.46.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (WebGL) Google 로그인 기능이 추가되었습니다.
* (Android) 웹뷰에서 고정 폰트 사이즈 사용 여부를 설정하는 필드를 재지원합니다.
    * GamebaseWebViewConfiguration.enableFixedFontSize
* (Android) 웹뷰에서 컷아웃(노치) 영역을 비롯한 모든 이용 가능한 스크린 공간을 사용하여 렌더링할 수 있는 설정이 추가되었습니다.
    * GamebaseWebViewConfiguration.renderOutsideSafeArea
* (Android) IAP 구독 상태를 조회할 수 있는 RequestSubscriptionsStatus API가 추가되었습니다.

#### 버그 수정
* (Standalone) 초기화 시 간헐적으로 ReflectionTypeLoadException 오류가 발생하는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.46.0](./release-notes-android/#2460-2023-01-31)
* [Gamebase iOS SDK 2.46.0](./release-notes-ios/#2460-2023-01-31)
