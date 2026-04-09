---
source: release-notes-unity.md
section: "2.54.0 (2023. 08. 29.)"
order: 37
split: true
created_date_time: 20260408_184906
keyword: Unity, Login, Push, Authentication, Error, LoginForLastLoggedInProvider, RegisterPush, Android, iOS, Release Notes
---

### 2.54.0 (2023. 08. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.54.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* (Android) Android 13 이상의 OS에서 RegisterPush API를 호출했을 때 Push 권한 요청 팝업이 자동으로 뜨지 않도록 할 수 있는 GamebaseRequest.Push.PushConfiguration.requestNotificationPermission 필드가 추가되었습니다.
* (Android) loginForLastLoggedInProvider 호출 중에 로딩 애니메이션을 숨기는 옵션을 지정할 수 있는 신규 API가 추가되었습니다.
    * Gamebase.LoginForLastLoggedInProvider(Dictionary<string, object> additionalInfo, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback);
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unity SDK 사용 가이드 > 인증 > Login > Login Flow > Login as the Latest Login IdP](../unity-authentication.md#login-as-the-latest-login-idp)

#### 버그 수정
* (Standalone) Gamebase 고객 센터 호출 시 서비스 오류 페이지가 출력되지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.53.0](../release-notes-android.md#2530-2023-08-17)
* [Gamebase iOS SDK 2.54.0](../release-notes-ios.md#2540-2023-08-29)
