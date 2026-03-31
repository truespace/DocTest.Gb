## Game > Gamebase > 릴리스 노트 > Unity

### 2.68.1 (2024. 12. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 플랫폼별 변경 사항

* [Gamebase iOS SDK 2.68.1](./release-notes-ios/#2681-2024-12-10)

### 2.68.0 (2024. 11. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.0/GamebaseSDK-Unity.zip)

#### 지원 종료

* FacebookAdapter for Unity 지원이 종료됩니다.

#### 기능 추가

* (Android) GameActivity를 지원합니다.

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 버그 수정

* NHN Cloud Console에서 네트워크 인사이트 설정을 활성화하면 JSON 파싱 오류가 발생하는 현상이 개선되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.68.0](./release-notes-android/#2680-2024-11-26)
* [Gamebase iOS SDK 2.68.0](./release-notes-ios/#2680-2024-11-26)

### 2.67.0 (2024. 10. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (Android, iOS) Steam 인증 추가

#### 기능 개선/변경

* Unity 최소 지원 버전 변경: 2020.3.16f1
* 롤링 이미지 공지의 WebView 내부에서 exception이 발생한 경우, 실패 콜백이 호출되도록 변경되었습니다.
* 내부 로직을 개선하였습니다.

#### 버그 수정

* storeCodeStandalone 코드로 인해 발생하는 오류가 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.67.0](./release-notes-android/#2670-2024-10-29)
* [Gamebase iOS SDK 2.67.0](./release-notes-ios/#2670-2024-10-29)

### 2.66.3 (2024. 09. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* Unity 최소 지원 버전 변경: 2020.3.0f1

### 2.66.3 (2024. 09. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.3/GamebaseSDK-Unity.zip)

#### 버그 수정
* (iOS) iOS 12 에서 결제 후 크래시가 발생하는 문제를 수정했습니다.

### 2.66.2 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.2/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 아래 필드가 iOS에서 deprecated 되었습니다. Android에서만 사용할 수 있습니다.
    * `GamebaseWebViewConfiguration.orientation`

### 2.66.1 (2024. 07. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.1/GamebaseSDK-Unity.zip)

#### 기능 추가

* (macOS) 개인정보 보호 정책이 대응되었습니다.

#### 기능 개선

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.1](./release-notes-android/#2661-2024-07-23)
* [Gamebase iOS SDK 2.66.0](./release-notes-ios/#2660-2024-07-23)

### 2.66.0 (2024. 07. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (Android) GPGS V2 인증이 추가되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.0](./release-notes-android/#2660-2024-07-10)
* [Gamebase iOS SDK 2.65.1](./release-notes-ios/#2651-2024-06-25)

#### Setting Tool (v2.9.0)

* GPGS V2 인증이 추가되었습니다. (Android에 한함)

### 2.65.1 (2024. 06. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 표시할 이미지 공지가 없는 경우 오류 대신 성공 콜백이 호출되도록 변경하였습니다.

#### 버그 수정
* 등록된 이미지 공지가 없을 경우 빈 공지 화면이 노출되는 문제를 수정하였습니다.
* (macOS) UnityEditor에서 GamebaseUtils.bundle 파일이 참조되지 않는 오류를 수정하였습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.65.1](./release-notes-android/#2651-2024-06-25)
* [Gamebase iOS SDK 2.65.1](./release-notes-ios/#2651-2024-06-25)

### 2.65.0 (2024. 06. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.65.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 이미지 공지 기능에 신규 타입이 추가되었습니다.
    * 롤링 팝업 타입이 추가되었습니다.
    * 기존의 이미지 공지는 팝업 타입으로 표기됩니다.
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.65.0](./release-notes-android/#2650-2024-06-11)
* [Gamebase iOS SDK 2.65.0](./release-notes-ios/#2650-2024-06-11)

### 2.64.0 (2024. 05. 28.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.64.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.64.0](./release-notes-android/#2620-2024-05-28)
* [Gamebase iOS SDK 2.64.0](./release-notes-ios/#2620-2024-05-28)

### 2.63.0 (2024. 04. 23.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.63.0/GamebaseSDK-Unity.zip)

#### 기능 추가

* (MacOS) WebView 신규 지원

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.63.0](./release-notes-android/#2620-2024-04-23)
* [Gamebase iOS SDK 2.63.0](./release-notes-ios/#2620-2024-04-23)

### 2.62.0 (2024. 03. 26.) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.62.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* iOS 개인정보 보호 정책이 대응되었습니다.
    * Gamebase SDK에 Privacy manifest와 서명을 적용했습니다.
* Gamebase 초기화 후 반환되는 LaunchingInfo VO에서 테스트 단말기임을 알 수 있도록 필드가 추가되었습니다.
    * **launchingInfo.user.testDevice**
* (MacOS, Windows) TOAST 타입 고객센터에 대해 FAQ/공지사항을 직접 열 수 있는 기능을 추가했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.62.0](./release-notes-android/#2620-2024-03-26)
* [Gamebase iOS SDK 2.62.0](./release-notes-ios/#2620-2024-03-26)

### 2.61.0 (2024. 02. 27.) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.61.0/GamebaseSDK-Unity.zip)

#### 버그 수정
* (macOS) 내부 bundle 파일이 정상적으로 로드되지 않는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.61.0](./release-notes-android/#2610-2024-02-27)
* [Gamebase iOS SDK 2.61.0](./release-notes-ios/#2610-2024-02-27)

### 2.60.0 (2024. 01. 23.) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.60.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.60.0](./release-notes-android/#2600-2024-01-23)
* [Gamebase iOS SDK 2.60.0](./release-notes-ios/#2600-2024-01-23)
