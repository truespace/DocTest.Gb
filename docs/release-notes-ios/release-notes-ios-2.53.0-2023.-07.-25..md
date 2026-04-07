---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "2.53.0 (2023. 07. 25.)"
section: "2.53.0 (2023. 07. 25.)"
order: 34
---

### 2.53.0 (2023. 07. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.53.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * Hangame iOS SDK (1.8.6)
* 아래 필드가 deprecated되었습니다.
    * **TCGBWebViewConfiguration.backgroundOpacity**
* iPad에서 [TCGBUtil showActionSheetWithTitle:message:blocks:] API 호출 시 ActionSheet이 화면 중앙에 오도록 수정하였습니다.
* 프로젝트에 추가하지 않은 인증 Adapter를 사용하는 경우 **TCGB_ERROR_AUTH_NOT_SUPPORTED_PROVIDER(3002)** 오류를 반환하도록 수정하였습니다.

#### 버그 수정
* 특정 상황에서 이용 정지 팝업 창이 표시되지 않는 버그를 수정하였습니다.
* Apple Silicon Mac에서 웹뷰가 정상적으로 표시되지 않는 버그를 수정하였습니다.
