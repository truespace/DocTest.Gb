---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.27.1, 버그수정, 기능개선, 변경, Login, Maintenance, IdP"
section: "2.27.1 (2021.09.14)"
order: 69
---

### 2.27.1 (2021.09.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO Android SDK(1.5.5), Hangame Android SDK(1.4.1), Weibo Android SDK(11.8.1)
* 에뮬레이터, 루팅 단말기에서 웹뷰가 정상적으로 표시되지 않을 때 재시도를 추가하여, 웹뷰가 정상적으로 표시되도록 개선하였습니다.
    * 대상은 웹뷰로 동작하는 이미지공지, 고객 센터, 공통 약관이 해당됩니다.
* Weibo IdP 인증을 개선하여 안정성을 향상시켰습니다.
    * 동기 API 이지만 실제로는 비동기로 동작하여 에러를 발생시키는 API에 예외 처리, 대기, 재시도 등을 추가였습니다.

#### 버그 수정
* '등록되지 않은 게임 버전' 에러 팝업 창이 영어로만 표시되는 버그를 수정하였습니다.
* 점검 팝업 창에 중국어가 표시되지 않는 버그를 수정하였습니다.
* [Credential Login](../../aos-authentication.md#login-with-credential) 을 한 경우, [Login as the Latest Login IdP](../../aos-authentication.md#login-as-the-latest-login-idp) 호출이 항상 실패하는 버그를 수정하였습니다.
