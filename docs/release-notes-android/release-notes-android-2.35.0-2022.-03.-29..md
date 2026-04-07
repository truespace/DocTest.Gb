---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.35.0 (2022. 03. 29.)"
section: "2.35.0 (2022. 03. 29.)"
order: 61
---

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-Android.zip)

```
Gamebase Android SDK는 이제 Maven Central로만 배포합니다.
더 이상 배포용 ZIP 파일에서 AAR 파일을 포함하지 않습니다.
```

#### 기능 추가
* 약관 창이 표시되었는지를 알 수 있는 API가 추가되었습니다.
    * **Gamebase.Terms.isShowingTermsView()**
* 웹뷰에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * **GamebaseWebViewConfiguration.Builder.enableFixedFontSize(boolean)**
* 약관 창에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * **GamebaseTermsConfiguration.Builder.enableFixedFontSize(boolean)**
* Facebook, NAVER 로그인 시 Facebook, NAVER 앱이 설치되어 있더라도 강제로 웹 로그인을 진행하는 기능이 추가되었습니다.
    * 이 기능을 사용하려면 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하세요.

```
{"enforce_app2web":true}
```

* 이제 NAVER 로그아웃 시 토큰을 삭제하지 않습니다.
    * 재로그인할 때 정보 제공 동의 창이 나타나지 않습니다.
    * 웹 로그인 시에는 계정이 변경되지 않습니다.
    * 이전 동작을 유지하려면 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하세요.

```
{"logout_and_delete_token":true}
```

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.29.1), Hangame Android SDK(1.4.4)
* 약관 창이 표시될 때 흰색 배경이 길게 표시되지 않도록 개선했습니다.

#### 버그 수정
* 웹뷰의 내비게이션 바를 숨기는 **GamebaseWebViewConfiguration.Builder.setNavigationBarVisible()** API가 정상적으로 동작하지 않는 문제를 수정했습니다.
