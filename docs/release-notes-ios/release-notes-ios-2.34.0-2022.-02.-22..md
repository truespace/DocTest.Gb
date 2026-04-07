---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "2.34.0 (2022. 02. 22.)"
section: "2.34.0 (2022. 02. 22.)"
order: 61
---

### 2.34.0 (2022. 02. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Gamebase 콘솔의 업데이트 필수 설정에서 **팝업 버튼 추가**를 선택하면 클라이언트의 업데이트 필수 팝업 창에 **자세히 보기** 버튼이 추가됩니다.
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * **[TCGBPush queryNotificationAllowedWithCompletion:]**
* 공통 약관 API 호출 후 약관 UI가 표시되었는지 여부를 알 수 있는 VO 클래스가 추가되었습니다.
    * **TCGBShowTermsViewResult**

#### 기능 개선/변경
* 이미지 공지 API를 호출했을 때 표시할 이미지 공지가 없는 경우, 배경이 잠시 어두워지는 현상을 수정하였습니다.
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드가 deprecated되었습니다.
    * **-[TCGBConfiguration enableKickoutPopup:]**
    * **-[TCGBConfiguration isEnableKickoutPopup]**
