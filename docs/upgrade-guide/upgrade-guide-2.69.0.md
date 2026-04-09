---
source: upgrade-guide.md
section: "2.69.0"
order: 9
split: true
created_date_time: 20260408_184906
keyword: Terms, Android, Unity, Upgrade Guide, 2.69.0
---

## 2.69.0

### Unity

* GPGS AutoLogin을 사용하는 경우, **GetLastLoggedInProvider()** 동기 API 대신 신규 추가된 **RequestLastLoggedInProvider(GamebaseCallback.GamebaseDelegate\<string> callback)** 비동기 API를 사용하세요.

### Unreal

* 약관 조회 결과 API인 FGamebaseQueryTermsResult가 수정되었습니다.
    * TermsCountryType의 값이 설정되지 않는 문제를 수정했습니다.
    * bPushEnabled, bAdAgreement, bAdAgreementNight가 제거되었습니다.
* GPGS AutoLogin을 사용하는 경우, **GetLastLoggedInProvider()** 동기 API 대신 신규 추가된 **RequestLastLoggedInProvider(GamebaseCallback.GamebaseDelegate\<string> callback)** 비동기 API를 사용하세요.

### Android

* **gamebase-adapter-auth-gpgs-autologin** 모듈을 빌드에 포함하는 경우, **getLastLoggedInProvider()** 동기 API 대신 신규 추가된 **requestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;)** 비동기 API를 사용하세요.
