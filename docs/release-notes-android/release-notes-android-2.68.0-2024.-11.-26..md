---
source: release-notes-android.md
section: "2.68.0 (2024. 11. 26.)"
order: 17
split: true
created_date_time: 20260408_191848
keyword: Android, Login, WebView, Authentication, Release Notes, 2.68.0
---

### 2.68.0 (2024. 11. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.0/GamebaseSDK-Android.zip)

```
최소 지원 버전이 Android 5.0 이상으로 상향되었습니다.(minSdk 19 → 21)
```

#### 기능 추가
* Google Play 게임즈 서비스 계정을 통한 자동 로그인 연동 기능이 추가되었습니다.
    * 이 기능을 사용하려면 빌드 의존성에 **gamebase-adapter-auth-gpgs-autologin** 모듈 선언을 추가해야 합니다.

            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-auth-gpgs-autologin:$GAMEBASE_SDK_VERSION"
            }
            
    * 또한 다음 가이드 문서를 참고하여 추가 정보를 설정하세요.
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > GPGS IdP](../aos-started.md#gpgs-idp)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.17.0)
* Google 인증 라이브러리가 업데이트되었습니다.
    * Google Sign-In for Android가 deprecated 되어 Google Credential Manager로 전환했습니다.
    * 인증 방법이 AuthCode 방식에서 OIDC 토큰 방식으로 변경되었습니다.
* 웹뷰에서 등록한 커스텀 스킴이 매칭되었을 때 URL을 리다이렉트하지 않도록 수정했습니다.
