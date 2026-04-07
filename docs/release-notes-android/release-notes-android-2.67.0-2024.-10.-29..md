---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.67.0 (2024. 10. 29.)"
section: "2.67.0 (2024. 10. 29.)"
order: 18
---

### 2.67.0 (2024. 10. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Steam 인증 어댑터가 추가되었습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.3)
* Twitter 인증 방식을 OAuth 2.0으로 변경하여, 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](../../oper-app.md#6-twitter)

#### 버그 수정
* 약관 팝업 창이 열려 있는 상태에서 네트워크 연결을 끊고 detail을 터치하면 약관 팝업 창이 종료되는 문제가 수정되었습니다.
