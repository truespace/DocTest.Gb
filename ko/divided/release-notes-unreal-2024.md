## Game > Gamebase > 릴리스 노트 > Unreal

### 2.68.0 (2024. 12. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.
* (Windows) Twitter 인증 방식을 OAuth 2.0으로 변경하여, 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information](./oper-app/#authentication-information)

#### 버그 수정
* (Windows) 결제 프로세스에서 크래시가 발생하지 않도록 수정했습니다.
* (Windows) Steam 결제 중 ESC 키로 결제를 종료하는 경우 다음 결제 API가 동작하지 않는 이슈를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.68.0](./release-notes-android/#2680-2024-11-26)
* [Gamebase iOS SDK 2.68.1](./release-notes-ios/#2681-2024-12-10)

### 2.67.2 (2024. 11. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.2/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.

#### 버그 수정
* (Windows) Apple ID 로그인을 정상적으로 진행하지 못하는 문제가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.67.0](./release-notes-android/#2670-2024-10-29)
* [Gamebase iOS SDK 2.67.0](./release-notes-ios/#2670-2024-10-29)

### 2.67.1 (2024. 11. 14.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.1/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* (Windows) Purchase 설정 시 스토어를 하나만 선택할 수 있도록 변경되었습니다.
    * 스토어 재설정이 필요합니다.
* (Windows) Epic Games Store 사용 시 EOS SDK의 핸들을 등록하는 과정이 변경되었습니다.
    * Online Subsystem EOS를 사용하는 경우 Gamebase 초기화 시 StoreCode가 Epic Games Store의 해당하는 값이면 자동으로 핸들을 등록합니다.
    * Online Subsystem EOS를 사용하지 않는 경우 [Windows Settings](./unreal-started/#windows-settings) 가이드를 참고하여 EOS의 핸들을 등록하는 과정이 필요합니다.
* (Windows) Steamworks SDK 지원 버전이 1.59로 변경되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Windows Settings > Steamworks 서비스](./unreal-started/#windows-settings)

#### 버그 수정
* 헤더 파일을 정상적으로 참조할 수 있도록 수정했습니다.
* (Windows) 초기화를 여러번 시도 시 크래시가 발생하지 않도록 수정되었습니다.
* (Windows) 초기화 시 StoreCode가 Steam 혹은 Epic Games Store에 해당하는 코드를 입력 시 크래시가 발생하지 않도록 수정되었습니다.
* (Windows) 외부 브라우저를 이용한 로그인 시도 시 크래시가 발생할 수 있는 로직이 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.67.0](./release-notes-android/#2670-2024-10-29)
* [Gamebase iOS SDK 2.67.0](./release-notes-ios/#2670-2024-10-29)

### 2.67.0 (2024. 10. 30.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* Steam 인증이 추가되었습니다.
* Steam 결제가 추가되었습니다.
* 이미지 공지 기능에 신규 타입이 추가되었습니다.
    * 롤링 팝업 타입이 추가되었습니다.
    * 기존의 이미지 공지는 팝업 타입으로 표기되며, Windows에서는 지원되지 않습니다.
* (Windows) LINE 인증이 추가되었습니다.

#### 기능 개선/변경
* 엔진의 지원 버전이 4.27~5.4로 변경되었습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정
* 크래시 로그 발생 시 크래시가 발생할 수 있는 로직을 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.67.0](./release-notes-android/#2670-2024-10-29)
* [Gamebase iOS SDK 2.67.0](./release-notes-ios/#2670-2024-10-29)

### 2.66.1 (2024. 09. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.1/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.3](./release-notes-android/#2663-2024-09-10)
* [Gamebase iOS SDK 2.66.2](./release-notes-ios/#2662-2024-08-27)

### 2.66.0 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* API 사용 방식이 변경되었습니다.
    * `IModuleInterface`를 상속 받은 **IGamebase**에서 제공하던 API를 `UGameInstanceSubsystem`을 상속 받은 **UGamebaseSubsytem**에서 제공하도록 변경했습니다.
    * **UGamebaseSubsytem**은 GameInstance의 서브시스템이므로 GameInstance 생명 주기를 따르며 SDK API 호출 시 사용하는 GameInstance를 통해 해당 서브시스템을 찾아서 API를 사용해야 합니다.
* GamebaseInterface 모듈이 제거되었습니다. Gamebase 플러그인 사용 시 GamebaseInterface 모듈을 삭제 후 사용하시길 바랍니다.
* (Windows) GameInstance가 여러 개인 환경에서 사용할 수 있습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.2](./release-notes-android/#2662-2024-08-27)
* [Gamebase iOS SDK 2.66.2](./release-notes-ios/#2662-2024-08-27)

### 2.64.0 (2024. 06. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.64.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.

#### 버그 수정
* C++ 환경에 따라 경고가 발생하여 빌드 시 오류가 발생하는 코드가 수정되었습니다.
* (Android) ProGuard 선언이 누락되어 API 호출 시 오류가 발생하는 내용이 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.64.0](./release-notes-android/#2640-2024-05-28)
* [Gamebase iOS SDK 2.64.0](./release-notes-ios/#2640-2024-05-28)

### 2.63.0 (2024. 04. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.63.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* (Android) Firebase Notification 설정 방식이 변경되어 플러그인 내부에 google-services-json.xml 파일 수정이 아닌 [Android 설정 툴](./unreal-started/#android-settings)에서 google-services.json 파일 경로를 지정하도록 변경되었습니다.
* (iOS) Gamebase Unreal SDK에 Privacy manifest와 서명을 적용했습니다.

#### 기능 개선/변경
* (iOS) 빌드 시 오류가 발생하지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.63.0](./release-notes-android/#2630-2024-04-23)
* [Gamebase iOS SDK 2.63.0](./release-notes-ios/#2630-2024-04-23)

### 2.62.0 (2024. 03. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* (iOS) Gamebase SDK 내부 iOS 프레임워크에 Privacy manifest와 서명을 적용했습니다.

#### 기능 개선/변경
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.62.0](./release-notes-android/#2620-2024-03-26)
* [Gamebase iOS SDK 2.62.0](./release-notes-ios/#2620-2024-03-26)

### 2.60.0 (2024. 02. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.60.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.60.0](./release-notes-android/#2600-2024-01-23)
* [Gamebase iOS SDK 2.60.1](./release-notes-ios/#2601-2024-02-15)
