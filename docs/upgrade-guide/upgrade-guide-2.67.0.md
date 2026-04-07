---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.67.0, Unity, Unreal, Android, iOS"
section: 2.67.0
order: 13
---

## 2.67.0

### Unity

#### Changed Minimum Support Version

* 최소 지원 Unity 버전이 2020.3.0에서 2020.3.16으로 변경되었습니다.
* 하위 버전의 Unity 지원이 필요하다면 [고객 센터](https://toast.com/support/inquiry)로 문의해 주시기 바랍니다.

### Unreal

#### Changed Minimum Support Version

* 최소 지원 버전이 UE 4.26에서 UE 4.27로 변경되었습니다.

### Android, iOS

* Twitter 인증 방식을 OAuth 2.0으로 변경하여 아래의 설정 변경 없이는 로그인이 동작하지 않습니다.
    * OAuth 2.0 Client ID 및 Client Secret 발급
        * Twitter Developer Portal에서 OAuth 2.0 Client ID와 Client Secret을 생성한 후, Gamebase 콘솔에 등록합니다.
    * Callback URL 설정
        * Gamebase 콘솔에 Callback URL(https://id-gamebase.toast.com/oauth/callback)을 설정합니다. 
        * 동일한 Callback URL을 Twitter Developer Portal에 추가합니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > Authentication Information > 6. Twitter](../../oper-app.md#6-twitter)
