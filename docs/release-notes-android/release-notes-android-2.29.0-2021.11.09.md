---
source: release-notes-android.md
section: "2.29.0 (2021.11.09)"
order: 67
split: true
created_date_time: 20260408_191848
keyword: Android, Login, Release Notes, 2.29.0
---

### 2.29.0 (2021.11.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.29.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Google 로그인시 Scope를 선언할 수 있는 기능을 추가하였습니다.
    * [https://developers.google.com/identity/protocols/oauth2/scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    * Scope로 **email**을 추가하면 프로필에서 Email 정보 획득이 가능합니다.
    * Scope는 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하면 로그인시 자동으로 설정됩니다.

```
{"scope":["email","myscope1","myscope2",...]}
```

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.27.4)
* DisplayLanguage 가이드 문서에서만 안내되고, 실제로 SDK에는 포함되어 있지 않았던 DisplayLanguage.Code 클래스를 추가하였습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Display Language > Gamebase에서 지원하는 언어코드의 종류](../aos-etc.md#gamebase)
