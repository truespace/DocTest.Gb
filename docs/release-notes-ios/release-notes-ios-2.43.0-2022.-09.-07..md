---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.43.0, 기능개선, 변경, Login, IdP"
section: "2.43.0 (2022. 09. 07.)"
order: 48
---

### 2.43.0 (2022. 09. 07.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.0.0)
    * ToastGamebaseIAP iOS SDK (0.14.0)
    * LINE iOS SDK (5.8.2)
    * Kakaogame iOS SDK (3.14.4)
    * Hangame iOS SDK (1.7.1)
* LINE 로그인 수행 시 서비스를 제공할 region을 입력할 수 있도록 변경하였습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > Login with IdP](../ios-authentication.md#login-with-idp)
* Gamebase와 호환성이 보장되지 않은 Gamebase Adapter를 사용하는 경우 초기화 시 에러가 발생하도록 수정하였습니다.
* SDK 내부 로직 개선
