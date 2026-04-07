---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.66.2, 기능개선, 변경"
section: "2.66.2 (2024. 08. 27.)"
order: 16
---

### 2.66.2 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * NHN Cloud iOS SDK (1.8.3)
        * 앱 스토어 심사에서 PrivacyInfo manifest 관련 경고 메일이 오지 않도록 수정되었습니다.
* 아래 필드가 deprecated되었습니다.
    * **TCGBWebViewConfiguration.orientationMask**
* 콘솔에 등록되지 않은 IdP로 로그인을 시도할 경우 TCGB_ERROR_AUTH_IDP_LOGIN_INVALID_IDP_INFO(3202) 오류가 발생하도록 수정했습니다.
* 롤링 이미지 공지의 웹뷰 내부에서 오류가 발생한 경우 기존의 성공 콜백 호출 대신 실패 콜백이 호출되도록 수정했습니다.
* 내부 로직 개선
