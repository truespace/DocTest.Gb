---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, XCode, v2.67.0, 버그수정, 기능개선, 기능추가, 변경"
section: "2.67.0 (2024. 10. 29.)"
order: 14
---

### 2.67.0 (2024. 10. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.67.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Steam 인증이 추가되었습니다.
* Twitter 인증 방식을 OAuth 2.0으로 변경하여 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](../oper-app.md#6-twitter)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * PAYCO iOS SDK (1.5.12)
        * PAYCO SDK가 Dynamic Framework로 변경되었습니다.
    * NAVER iOS SDK (4.2.3)
        * Xcode 16과 iOS 18 환경에서 정상 동작하도록 수정되었습니다.
    * Hangame iOS SDK (1.16.2)
        * Apple Silicon Mac에서 로그인이 실패하는 버그가 수정되었습니다.
* Gamebase SDK가 외부 SDK의 리소스를 포함하지 않도록 수정하였습니다.
* 내부 로직 개선

#### 버그 수정  
* 시스템 팝업 창 위에 Gamebase 론칭 팝업 창이 표시될 때 화면이 검게 변하는 버그를 수정하였습니다.
