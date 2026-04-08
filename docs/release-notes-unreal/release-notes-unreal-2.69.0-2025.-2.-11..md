---
source: release-notes-unreal.md
section: "2.69.0 (2025. 2. 11.)"
order: 15
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Initialize, Authentication, Terms, Error, Android, iOS, Release Notes, 2.69.0
---

### 2.69.0 (2025. 2. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* `RequestLastLoggedInProvider` 비동기 API를 추가했습니다.
    * `GetLastLoggedInProvider` 동기 API가 타이밍상 정상적인 값을 반환하지 못할 때가 있습니다.
    * (Android) GPGS의 Auto Login 기능을 사용 시 GPGS 서버에서 데이터를 획득하는 시간이 필요하므로 Gamebase 초기화 직후 GetLastLoggedInProvider() 동기 API를 호출하면 정상적인 값을 획득할 수 없습니다.
        이때 RequestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;) 비동기 API는 정확한 값을 보장합니다.
        Auto Login을 사용하지 않는다면 GetLastLoggedInProvider() 동기 API를 사용해도 무방합니다.
* (Android) GPGS v2 인증 추가되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Android Settings](../unreal-started.md#android-settings)
* (Android) `FGamebaseWebViewConfiguration::CutoutColor` 필드를 추가했습니다.
    * GamebaseWebView의 `FGamebaseWebViewConfiguration::bRenderOutSideSafeArea` 필드를 **false**로 설정한 경우, cutout 영역에 자동으로 padding 여백을 추가합니다.
    * CutoutColor 필드는 이렇게 추가된 padding 영역의 색을 설정할 수 있습니다.
    * RenderOutsideSafeArea 필드를 false로 설정했지만 CutoutColor 필드는 설정하지 않는 경우에는 웹 페이지 'body'의 'background-color' 값으로 자동으로 padding 영역의 색상을 결정합니다.

#### 기능 개선/변경

* 내부 로직을 개선하였습니다.

#### 버그 수정

* 약관 조회 결과 API인 FGamebaseQueryTermsResult가 수정되었습니다.
    * TermsCountryType의 값이 설정되지 않는 문제를 수정했습니다.
    * bPushEnabled, bAdAgreement, bAdAgreementNight가 제거되었습니다.
* (Android) Windows 환경에서 빌드 시 포스트 빌드 프로세스에서 오류가 발생하지 않도록 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.69.0](../release-notes-android.md#2690-2025-01-21)
* [Gamebase iOS SDK 2.69.0](../release-notes-ios.md#2690-2025-01-21)
