---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.53.0, 신규, 기능개선, 기능추가, 변경, Login, Contact, IdP"
section: "2.53.0 (2023. 08. 17.)"
order: 37
---

### 2.53.0 (2023. 08. 17.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.53.0/GamebaseSDK-Android.zip)

#### 기능 추가
* loginForLastLoggedInProvider 호출 중에 로딩 애니메이션을 숨기는 옵션을 지정할 수 있는 신규 API가 추가되었습니다.
    * Gamebase.loginForLastLoggedInProvider(Activity activity, Map&lt;String, Object&gt; additionalInfo, GamebaseDataCallback&lt;AuthToken&gt; callback);
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Login > Login Flow > Login as the Latest Login IdP](../aos-authentication.md#login-as-the-latest-login-idp)

#### 기능 개선/변경
* 외부 SDK 업데이트: Facebook Android SDK(16.1.2), Line Android SDK(5.8.1), Weibo Android SDK(13.5.0)
* 고객 센터 웹뷰에서 파일을 첨부할 때 앨범, 카메라, 저장소 타입에 따라 자동으로 권한을 획득하고 타입에 맞는 기능을 실행하도록 개선되었습니다.
    * '고객 센터'의 개선된 파일 첨부 기능을 사용하려면 아래 가이드에 따라 AndroidManifest.xml에 권한 설정을 추가해야 합니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Contact](../aos-started.md#contact)
