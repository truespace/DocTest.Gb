---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "2.35.0 (2022. 03. 29.)"
section: "2.35.0 (2022. 03. 29.)"
order: 59
---

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 현재 약관 창이 화면에 표시되고 있는지를 알 수 있는 API를 추가하였습니다.
    * **[TCGBTerms isShowingTermsView]**

#### 기능 개선/변경
* 기존의 Google 웹 로그인 방식에서 Google SDK 로그인 방식으로 변경하였습니다.
* 한게임 로그인을 도중에 취소했을 경우, **TCGB_ERROR_AUTH_USER_CANCELED(3001)** 오류를 반환하도록 수정하였습니다.
