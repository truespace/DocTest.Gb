---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, v2.68.0, 버그수정, 기능개선, 변경"
section: "2.68.0 (2024. 12. 10.)"
order: 17
---

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
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information](../oper-app.md#authentication-information)

#### 버그 수정
* (Windows) 결제 프로세스에서 크래시가 발생하지 않도록 수정했습니다.
* (Windows) Steam 결제 중 ESC 키로 결제를 종료하는 경우 다음 결제 API가 동작하지 않는 이슈를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.68.0](../release-notes-android.md#2680-2024-11-26)
* [Gamebase iOS SDK 2.68.1](../release-notes-ios.md#2681-2024-12-10)
